#!/usr/bin/env python3
"""Transcribe Listen-and-Repeat recordings locally and compare them with the prompt text.

Usage:
  python tools/lr_transcribe.py [DIR] [--test 3] [--models small.en medium.en]

DIR defaults to recordings/speaking/listen-and-repeat. It must hold the files written by
practice/4a. listen-and-repeat.html: LR_T<test>_<run>.json (manifest) + LR_T<test>_<run>_Q<n>.webm.
Output: LR_T<test>_<run>_report.json and _report.md next to the manifest.

Setup (once):  python3 -m venv ~/.venvs/fw && ~/.venvs/fw/bin/pip install faster-whisper numpy
Needs ffmpeg on PATH. Models come from the Hugging Face cache (small.en, medium.en).

Design rules (see guides/speaking.md):
 - VERBATIM: no initial_prompt, no script bias, no LLM clean-up, temperature 0.
 - Two models; a word they disagree on, or one with low probability, is 'uncertain', not an error.
 - The report never gives the final 0-5 score. That is done afterwards against the ETS rubric.
"""
import argparse, difflib, glob, json, os, re, subprocess, sys, tempfile, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SENT = json.load(open(os.path.join(HERE, "lr_sentences.json")))
LOW_P = 0.60
FILL = {"um", "uh", "uhm", "er", "erm", "hmm", "mm", "ah", "eh"}

CONTR = [(r"\blet's\b", "let us"), (r"\bcan't\b", "can not"), (r"\bwon't\b", "will not"), (r"n't\b", " not"),
         (r"'re\b", " are"), (r"'ll\b", " will"), (r"'ve\b", " have"), (r"'m\b", " am")]
SPELL = {"centre": "center", "aides": "aids", "colour": "color", "programme": "program", "theatre": "theater",
         "cheque": "check", "grey": "gray", "metre": "meter", "organise": "organize", "recognise": "recognize"}

def norm(s):
    s = s.lower().replace("\u2019", "'").replace("\u2018", "'").replace("-", " ")
    s = re.sub(r"[^a-z0-9' ]", " ", s)
    for a, b in CONTR:
        s = re.sub(a, b, s)
    s = s.replace("'", "")  # leftover 's possessives: visitor's -> visitors
    return [SPELL.get(w, w) for w in s.split()]

def split_fill(tokens):
    return [w for w in tokens if w not in FILL], [w for w in tokens if w in FILL]

def to_wav(src, dst):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-ar", "16000", "-ac", "1", dst], check=True)
    w = wave.open(dst)
    return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768

def level_stats(a):
    dur = len(a) / 16000
    if dur == 0:
        return dict(dur=0, peak=0, rms=0, voiced_start=None, voiced_end=None)
    fr = 320  # 20 ms
    n = len(a) // fr
    e = np.sqrt((a[: n * fr].reshape(n, fr) ** 2).mean(axis=1)) if n else np.array([0.0])
    thr = max(0.01, 0.15 * float(np.percentile(e, 95)))
    idx = np.where(e > thr)[0]
    return dict(dur=round(dur, 2), peak=round(float(np.abs(a).max()), 3), rms=round(float(np.sqrt((a ** 2).mean())), 4),
                voiced_start=round(idx[0] * 0.02, 2) if len(idx) else None,
                voiced_end=round((idx[-1] + 1) * 0.02, 2) if len(idx) else None)

def transcribe(model, audio):
    segs, _ = model.transcribe(audio, language="en", temperature=0, beam_size=5, condition_on_previous_text=False,
                               word_timestamps=True)
    segs = list(segs)
    words = [dict(w=w.word.strip(), p=round(float(w.probability), 2), s=round(w.start, 2), e=round(w.end, 2))
             for s in segs for w in (s.words or [])]
    ns = [round(float(s.no_speech_prob), 2) for s in segs]
    return dict(text=" ".join(s.text.strip() for s in segs).strip(), words=words, no_speech=max(ns) if ns else None)

def align(target, heard):
    """Word-level diff. Returns ops list and counts."""
    sm = difflib.SequenceMatcher(None, target, heard, autojunk=False)
    ops = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        ops.append(dict(kind={"replace": "changed", "delete": "missing", "insert": "added"}[tag],
                        target=" ".join(target[i1:i2]), heard=" ".join(heard[j1:j2]), at=i1))
    return ops

def best_target(item, heard):
    cands = [item["text"]] + item.get("alts", [])
    scored = []
    for c in cands:
        t = norm(c)
        scored.append((len(align(t, heard)), difflib.SequenceMatcher(None, t, heard).ratio() * -1, c, t))
    scored.sort(key=lambda x: (x[0], x[1]))
    return scored[0][2], scored[0][3]

def process(manifest_path, models, mnames):
    mp = json.load(open(manifest_path))
    folder = os.path.dirname(manifest_path)
    test = str(mp["test"])
    rep = dict(test=mp["test"], run=mp["run"], started=mp.get("started"), models=mnames, items=[])
    for it in mp["items"]:
        n = str(it["n"])
        item = SENT[test][n]
        r = dict(n=it["n"], script=item["text"], file=it.get("file"), win=it.get("win"), rec_ms=it.get("recMs"),
                 stopped_early=it.get("stoppedEarly"), replays=it.get("replays", 0), prompt_ended_before_rec=True)
        f = os.path.join(folder, it["file"]) if it.get("file") else None
        if not f or not os.path.exists(f):
            r["error"] = "recording file missing"; rep["items"].append(r); continue
        with tempfile.TemporaryDirectory() as td:
            audio = to_wav(f, os.path.join(td, "a.wav"))
        r["audio"] = level_stats(audio)
        r["heard"] = {}
        for mn, m in zip(mnames, models):
            r["heard"][mn] = transcribe(m, audio)
        primary = r["heard"][mnames[0]]
        h0, fill0 = split_fill(norm(primary["text"]))
        r["fillers"] = fill0
        chosen, t = best_target(item, h0)
        r["compared_to"] = chosen
        r["diff"] = {}
        for mn in mnames:
            r["diff"][mn] = align(t, split_fill(norm(r["heard"][mn]["text"]))[0])
        # disagreement between models, and low-probability words
        hs = [split_fill(norm(r["heard"][mn]["text"]))[0] for mn in mnames]
        r["models_agree"] = all(h == hs[0] for h in hs)
        low = []
        for mn in mnames:
            for w in r["heard"][mn]["words"]:
                if w["p"] < LOW_P:
                    low.append(dict(model=mn, word=w["w"], p=w["p"]))
        r["low_conf"] = low
        ws = primary["words"]
        r["first_word_s"] = ws[0]["s"] if ws else None
        r["last_word_end_s"] = ws[-1]["e"] if ws else None
        flags = []
        a = r["audio"]
        if a["peak"] < 0.03 or a["voiced_start"] is None:
            flags.append("VERY QUIET OR EMPTY - check the mic; any transcript here is probably a hallucination")
        if a["peak"] > 0.98:
            flags.append("CLIPPING - recording may be distorted")
        if primary["no_speech"] is not None and primary["no_speech"] > 0.6:
            flags.append("model thinks there is little speech")
        if r["win"] and a["dur"] and a["voiced_end"] and a["voiced_end"] > a["dur"] - 0.25 and not r["stopped_early"]:
            flags.append("speech still running at the end of the window - may be cut off")
        if not r["models_agree"]:
            flags.append("models disagree - uncertain words, do not penalise")
        r["flags"] = flags
        rep["items"].append(r)
    base = manifest_path[:-5]
    json.dump(rep, open(base + "_report.json", "w"), indent=1, ensure_ascii=False)
    open(base + "_report.md", "w").write(to_md(rep, mnames))
    return base + "_report.md"

def to_md(rep, mnames):
    L = [f"# Listen and Repeat - Test {rep['test']} - run {rep['run']}", "",
         f"Models: {', '.join(mnames)} (verbatim, temperature 0, no script prompt). **No score here**: scoring is done against the ETS rubric.", ""]
    for r in rep["items"]:
        L.append(f"## Q{r['n']}")
        L.append(f"- **Script:** {r['script']}")
        if r.get("error"):
            L.append(f"- **ERROR:** {r['error']}"); L.append(""); continue
        if r["compared_to"] != r["script"]:
            L.append(f"- Compared against accepted variant: {r['compared_to']}")
        for mn in mnames:
            L.append(f"- **Heard ({mn}):** {r['heard'][mn]['text'] or '(nothing)'}")
        for mn in mnames:
            d = r["diff"][mn]
            txt = "none" if not d else "; ".join(f"{x['kind']}: script '{x['target']}' / heard '{x['heard']}'" for x in d)
            L.append(f"- Differences ({mn}): {txt}")
        a = r["audio"]
        L.append(f"- Audio: {a['dur']}s recorded, voiced {a['voiced_start']}-{a['voiced_end']}s, peak {a['peak']}; first word {r['first_word_s']}s, last word ends {r['last_word_end_s']}s; window {r['win']}s" + (" (stopped early)" if r.get("stopped_early") else ""))
        if r.get("fillers"):
            L.append("- Fillers (not counted as errors): " + ", ".join(r["fillers"]))
        if r.get("replays"):
            L.append(f"- Prompt replays: {r['replays']}")
        if r["low_conf"]:
            L.append("- Low-confidence words: " + ", ".join(f"{x['word']} ({x['p']}, {x['model']})" for x in r["low_conf"]))
        for fl in r["flags"]:
            L.append(f"- FLAG: {fl}")
        L.append("")
    return "\n".join(L)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", nargs="?", default="recordings/speaking/listen-and-repeat")
    ap.add_argument("--test"); ap.add_argument("--models", nargs="+", default=["small.en", "medium.en"])
    ap.add_argument("--redo", action="store_true")
    a = ap.parse_args()
    from faster_whisper import WhisperModel
    mans = sorted(p for p in glob.glob(os.path.join(a.dir, "LR_T*.json")) if not p.endswith("_report.json"))
    if a.test:
        mans = [p for p in mans if os.path.basename(p).startswith(f"LR_T{a.test}_")]
    mans = [p for p in mans if a.redo or not os.path.exists(p[:-5] + "_report.json")]
    if not mans:
        print("nothing new to transcribe in", a.dir); return
    models = [WhisperModel(m, device="cpu", compute_type="int8") for m in a.models]
    for p in mans:
        print("->", process(p, models, a.models))

if __name__ == "__main__":
    main()
