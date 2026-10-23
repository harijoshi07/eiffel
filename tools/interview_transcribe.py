#!/usr/bin/env python3
"""Transcribe Take an Interview recordings locally and report speaking metrics.

Usage:
  python tools/interview_transcribe.py [DIR] [--test 1] [--models small.en medium.en]

DIR defaults to ~/Downloads, where the page's downloads land. It must hold the files written by
practice/4b. take-an-interview.html: INT_T<test>_<run>.json (manifest) + INT_T<test>_<run>_Q<n>.webm.
Output: INT_T<test>_<run>_report.json and _report.md next to the manifest.

Setup (once):  python3 -m venv ~/.venvs/fw && ~/.venvs/fw/bin/pip install faster-whisper numpy
Needs ffmpeg on PATH. Models come from the Hugging Face cache (small.en, medium.en).

Design rules (see guides/speaking.md):
 - VERBATIM: no initial_prompt, no script bias, no LLM clean-up, temperature 0.
 - Two models; a word they disagree on, or one with low probability, is 'uncertain', not an error.
 - The report never gives the final 0-5 score. That is evaluated against the ETS rubric.
"""
import argparse, glob, json, os, re, subprocess, sys, tempfile, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
QUESTIONS = {str(t["id"]): t for t in json.load(open(os.path.join(HERE, "interview_questions.json")))}
LOW_P = 0.60
FILL = {"um", "uh", "uhm", "er", "erm", "hmm", "mm", "ah", "eh"}

def to_wav(src, dst):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-ar", "16000", "-ac", "1", dst], check=True)
    w = wave.open(dst)
    return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768

def level_stats(a):
    dur = len(a) / 16000
    if dur == 0:
        return dict(dur=0, peak=0, rms=0, voiced_start=None, voiced_end=None)
    fr = 320  # 20 ms frames
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

def find_pauses(words, threshold=1.5):
    """Find silent gaps between consecutive words >= threshold seconds."""
    pauses = []
    for i in range(len(words) - 1):
        gap = round(words[i + 1]["s"] - words[i]["e"], 2)
        if gap >= threshold:
            pauses.append(dict(after=words[i]["w"], before=words[i + 1]["w"], gap=gap, at=words[i]["e"]))
    return pauses

def process(manifest_path, models, mnames):
    mp = json.load(open(manifest_path))
    folder = os.path.dirname(manifest_path)
    test_id = str(mp["test"])
    test_info = QUESTIONS.get(test_id, {})
    items_map = {it["n"]: it for it in test_info.get("items", [])}
    
    rep = dict(test=mp["test"], label=test_info.get("label", f"Test {test_id}"),
               scenario=test_info.get("scenario", ""), run=mp["run"],
               started=mp.get("started"), models=mnames, items=[])
    
    for it in mp["items"]:
        n = it["n"]
        prompt_item = items_map.get(n, {})
        r = dict(n=n, prompt=prompt_item.get("text", ""), file=it.get("file"),
                 win=it.get("win", 45), rec_ms=it.get("recMs"),
                 stopped_early=it.get("stoppedEarly"), replays=it.get("replays", 0))
        
        f = os.path.join(folder, it["file"]) if it.get("file") else None
        if not f or not os.path.exists(f):
            r["error"] = "recording file missing"
            rep["items"].append(r)
            continue
            
        with tempfile.TemporaryDirectory() as td:
            audio = to_wav(f, os.path.join(td, "a.wav"))
            
        r["audio"] = level_stats(audio)
        r["heard"] = {}
        for mn, m in zip(mnames, models):
            r["heard"][mn] = transcribe(m, audio)
            
        primary = r["heard"][mnames[0]]
        tokens = [re.sub(r"[^a-z0-9']", "", w.lower()) for w in primary["text"].split()]
        tokens = [w for w in tokens if w]
        fillers = [w for w in tokens if w in FILL]
        
        words_list = primary["words"]
        word_count = len(tokens)
        r["word_count"] = word_count
        r["fillers"] = fillers
        
        dur = r["audio"]["dur"]
        # speech duration (from first to last word)
        if words_list:
            speech_dur = max(0.5, words_list[-1]["e"] - words_list[0]["s"])
            wpm = round((word_count / speech_dur) * 60, 1)
        else:
            speech_dur = dur
            wpm = 0.0
            
        r["speech_dur"] = round(speech_dur, 2)
        r["wpm"] = wpm
        
        # pauses >= 1.5s
        pauses = find_pauses(words_list, threshold=1.5)
        r["pauses"] = pauses
        
        # model agreement on word tokens
        hs = [" ".join(re.findall(r"[a-z0-9']+", r["heard"][mn]["text"].lower())) for mn in mnames]
        r["models_agree"] = all(h == hs[0] for h in hs)
        
        low = []
        for mn in mnames:
            for w in r["heard"][mn]["words"]:
                if w["p"] < LOW_P:
                    low.append(dict(model=mn, word=w["w"], p=w["p"]))
        r["low_conf"] = low
        
        flags = []
        a = r["audio"]
        if a["peak"] < 0.03 or a["voiced_start"] is None:
            flags.append("VERY QUIET OR EMPTY - check the microphone")
        if a["peak"] > 0.98:
            flags.append("CLIPPING - possible distortion")
        if primary["no_speech"] is not None and primary["no_speech"] > 0.6:
            flags.append("model thinks there is little speech")
        if a["dur"] > 44.0 and not r["stopped_early"] and a["voiced_end"] and a["voiced_end"] > 44.2:
            flags.append("speech was still running when 45s timer expired - may be cut off mid-thought")
        if len(pauses) >= 3:
            flags.append(f"multiple noticeable pauses (>= 1.5s: {len(pauses)}) - may affect fluency rating")
        if word_count < 45 and not r["stopped_early"]:
            flags.append(f"low word count ({word_count} words in 45s; ETS sample 5s are ~65-95 words)")
        r["flags"] = flags
        rep["items"].append(r)
        
    base = manifest_path[:-5]
    json.dump(rep, open(base + "_report.json", "w"), indent=1, ensure_ascii=False)
    open(base + "_report.md", "w").write(to_md(rep, mnames))
    return base + "_report.md"

def to_md(rep, mnames):
    L = [
        f"# Take an Interview - {rep['label']} - run {rep['run']}",
        f"Scenario: {rep['scenario']}",
        "",
        f"Models: {', '.join(mnames)} (verbatim, temperature 0). Evaluated against ETS 0-5 Rubric.",
        ""
    ]
    for r in rep["items"]:
        L.append(f"## Question {r['n']}")
        L.append(f"- **Interviewer:** {r['prompt']}")
        if r.get("error"):
            L.append(f"- **ERROR:** {r['error']}\n")
            continue
        for mn in mnames:
            L.append(f"- **Transcript ({mn}):** {r['heard'][mn]['text'] or '(nothing)'}")
        a = r["audio"]
        L.append(f"- **Speech metrics:** {r['word_count']} words · {r['wpm']} WPM (paced across {r['speech_dur']}s spoken of {a['dur']}s recorded, window {r['win']}s)")
        if r["pauses"]:
            p_desc = ", ".join(f"{p['gap']}s after '{p['after']}'" for p in r["pauses"])
            L.append(f"- **Pauses (>=1.5s):** {len(r['pauses'])} pause(s): {p_desc}")
        if r.get("fillers"):
            L.append(f"- **Fillers:** {len(r['fillers'])} ({', '.join(r['fillers'])}) - *Note: natural fillers do not lower a 5*")
        if r.get("replays"):
            L.append(f"- Prompt replays: {r['replays']}")
        if r["low_conf"]:
            L.append("- Low-confidence words: " + ", ".join(f"{x['word']} ({x['p']}, {x['model']})" for x in r["low_conf"]))
        for fl in r["flags"]:
            L.append(f"- **FLAG:** {fl}")
        L.append("")
    return "\n".join(L)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", nargs="?", default=os.path.expanduser("~/Downloads"))
    ap.add_argument("--test")
    ap.add_argument("--models", nargs="+", default=["small.en", "medium.en"])
    ap.add_argument("--redo", action="store_true")
    a = ap.parse_args()
    
    from faster_whisper import WhisperModel
    mans = sorted(p for p in glob.glob(os.path.join(a.dir, "INT_T*.json")) if not p.endswith("_report.json"))
    if a.test:
        mans = [p for p in mans if os.path.basename(p).startswith(f"INT_T{a.test}_")]
    mans = [p for p in mans if a.redo or not os.path.exists(p[:-5] + "_report.json")]
    if not mans:
        print("nothing new to transcribe in", a.dir)
        return
    models = [WhisperModel(m, device="cpu", compute_type="int8") for m in a.models]
    for p in mans:
        print("->", process(p, models, a.models))

if __name__ == "__main__":
    main()
