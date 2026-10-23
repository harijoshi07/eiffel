# Speaking: how to improve

Your attempts and mistakes are in `logs/speaking.md`. When a pattern shows up there, add a rule here.
Tags: **[ETS]** official, **[mine]** my suggestion or inference, **[data]** from your log.

## 1. How Speaking is scored
- **[ETS]** Speaking and Writing responses are scored by ETS's AI scoring engine, using the scoring guides. Human ratings train the engine and provide oversight (Teacher FAQ, Q12, local PDF text).
- **[ETS]** Each item is scored **0-5**. 7 Listen and Repeat items + 4 Interview items = raw 0-55 (Test Overview, Table 1). Raw points are converted with weighted equipercentile linking (FAQ). ETS publishes no raw-to-band table, so any Speaking band from practice is an estimate.
- **[ETS]** The engine works from your **audio**, not from a transcript. A transcript shows what words you said. It does not show accent, rhythm or clarity.

## 2. Format
| | Listen and Repeat | Take an Interview |
|---|---|---|
| Items | 7 sentences, one scenario, getting longer | 4 questions from a recorded interviewer |
| Speaking time | 8-12 s per sentence, heard once | 45 s per answer |
| Preparation | none | none |
| Scored on | exact repetition and intelligibility | elaboration, pace, pronunciation and rhythm, grammar and vocabulary |

## 3. Listen and Repeat scoring guide (ETS, condensed)
| Score | What ETS says |
|---|---|
| **5** | Exact repetition, fully intelligible. |
| **4** | Meaning captured, not exact. One or two function words missing or changed; a content word missing (longer prompts) or replaced by a related word; tense, aspect or number marker missing or wrong; two words swapped. One or two content words may be ambiguous from imprecise pronunciation. A successful self-correction is fine. |
| **3** | Essentially a full sentence but the meaning is not accurate. Majority of content words present. Multiple function words changed or missing; one or more content words missing or substantively changed. Intelligibility problems cause occasional difficulty (struggling over a word, running words together). |
| **2** | A significant part missing and/or highly inaccurate. Often the first part is repeated, then the speaker stops or fills with wrong content. Meaning is fragmentary. Low intelligibility. |
| **1** | Very little captured, or largely unintelligible. |
| **0** | No response, entirely unintelligible, no English, or unconnected. |

Source: `resources/pdfs/guide-speaking-rubrics.pdf` (page 1).

**What the ETS samples show** (`guide-speaking-sample-responses.pdf`, audio in `resources/audio/samples/speaking/`). One prompt, three scored students:
- **3:** "done" for "finished", "unchecked materials", "in the reducing time". Several words changed, meaning lost.
- **4:** "printout" for "checked-out". One content word replaced with a related word.
- **5:** says "you are" for "you're". ETS still gives a 5, so expanding a contraction costs nothing **[mine: inferred from this one sample]**.
- The page `practice/4a. listen-and-repeat.html` has a calibration screen with these three.

## 4. How I score your recordings
1. Run `python tools/serve.py` in the vault, then open the address it prints (`http://localhost:8765/practice/4a.%20listen-and-repeat.html`). The page plays each sentence once and records your answer. The server writes each recording straight into `recordings/speaking/listen-and-repeat/`. Git ignores that folder, so your voice is not pushed. (A browser page cannot write to a path by itself, which is why the server exists. Without it, the page falls back to a folder picker or your Downloads folder.)
2. `python tools/lr_transcribe.py` transcribes each clip locally with faster-whisper `small.en` and `medium.en`. **Verbatim**: temperature 0, no script given to the model, no LLM clean-up, so an error is not repaired by the tool.
3. It aligns the transcript with the prompt word by word and lists: missing, added and changed words, fillers (not counted), low-confidence words, timing, and warnings (quiet, clipped, cut off).
4. I read that report and give each sentence 0-5 against the table in section 3, quoting the rubric line. The tool itself never scores.
5. A word the two models disagree on, or read with low confidence, is **uncertain**. I do not mark you down for it. Where it matters, you tell me what you said, or listen to the clip.

**Limits [mine]**
- Whisper leans toward fluent text, so a subtle slip (wrong article, missing plural) can be repaired by the model. Two models and word confidence reduce this. They do not remove it.
- It cannot judge accent, stress or rhythm. A mispronounced word that Whisper still guesses right will look perfect. For "fully intelligible" I only have confidence scores as a rough clue.
- It cannot separate a stumble from a silent gap.
- My scores are an estimate of ETS's engine, not a prediction of it.

**Tool checks done (2026-10-23)** [data]: all 49 prompts matched the printed sentences by transcription (2 homophone/contraction variants accepted: Test 4 Q4 "aids/aides", Test 6 Q3 "area's/area is"). Synthetic test responses (a changed word, a dropped word, a missing plural, fillers, a cut-off sentence, silence) were all reported correctly, and silence was flagged. The three ETS samples transcribe as in the table above.

## 5. Tips
- **[mine]** Listen and Repeat: hold the meaning first, then content words (nouns, verbs, adjectives, numbers), then the small words and endings. Endings (plural -s, past -ed) are the likeliest 4-versus-5 slips, as in your Reading misses.
- **[mine]** Do not stop and restart. The rubric allows a successful self-correction, but a restart can eat the window.
- **[mine]** Interview: Point, Reason, Example, Point again. One clear idea. ETS's own scored interview samples contain "um" and "uh" and still score 5, so fluency does not mean no fillers.
- Compare each interview recording with the samples in `resources/audio/samples/speaking/`.

## 6. Patterns from my log
- None yet. List repeated mistakes here with a one-line fix once recordings are logged.

## 7. Redo queue
- None yet.
