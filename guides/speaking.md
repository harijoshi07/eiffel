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

**What the ETS L&R samples show** (`guide-speaking-sample-responses.pdf`, audio in `resources/audio/samples/speaking/`):
- **3:** "done" for "finished", "unchecked materials", "in the reducing time". Several words changed, meaning lost.
- **4:** "printout" for "checked-out". One content word replaced with a related word.
- **5:** says "you are" for "you're". ETS still gives a 5, so expanding a contraction costs nothing **[mine: inferred from this one sample]**.
- Practice page: `practice/4a. listen-and-repeat.html`.

## 4. Take an Interview scoring guide (ETS, official)
| Score | What ETS says |
|---|---|
| **5** | **Fully successful response.** Fully addresses the question, clear and fluent. On topic and well elaborated. Good conversational pace maintained with appropriate, natural pauses. Pronunciation easily intelligible; rhythm and intonation effectively convey meaning. Range of accurate grammar and vocabulary allows clear expression of precise meanings. |
| **4** | **Generally successful response.** Addresses the question, reasonably clear. On topic and elaborated, but may lack effective connectors. Good speaking pace generally maintained, with some pausing that may minimally affect flow. Intelligibility and meaning not impeded by pronunciation, rhythm and intonation, though occasional words/phrases require minor effort. Grammar and vocabulary adequate to express general meanings most of the time. |
| **3** | **Partially successful response.** Generally on topic, but elaboration may be relatively limited and/or unclear. Frequent or lengthy pauses result in a choppy pace; filler words are frequent. Intelligibility sometimes affected by inaccuracies in word-level pronunciation or stress/rhythm. Limited range and accuracy of grammar and vocabulary noticeably restrict precision and clarity. |
| **2** | **Mostly unsuccessful response.** Minimally connected to the question; little or no relevant elaboration or consists mainly of language from the question. Intelligibility is limited; intended meaning is often difficult to discern. Very limited range of grammar and vocabulary. |
| **1** | **Unsuccessful response.** Ineffective attempt. Telegraphic language (short, disconnected phrases), serious and frequent errors, minimal original language. |
| **0** | Blank, rejects topic, not in English, entirely copied or unconnected. |

Source: `resources/pdfs/guide-speaking-rubrics.pdf` (page 2) and `Updated TOEFL iBT Test Overview` (page 27).

**What the ETS Interview samples show** (`resources/audio/samples/speaking/`):
- **Prompt:** "Some people believe reading helps improve imagination and creativity. Do you agree, or are there other activities that enhance these skills? Why?"
- **Response 1 (Score 3):** 75 words, 98 WPM, 45.8s. Limited elaboration, noticeable errors ("make you more creative", "on the book", "make the creativity improve"), choppy rhythm and pauses.
- **Response 2 (Score 4):** 61 words, 95 WPM, 38.5s. On topic with concrete examples (Harry Potter, painting, music). Steady pace and clear pronunciation, but simpler connectors and repetitive phrasing keep it from a 5.
- **Response 3 (Score 5):** 83 words, 133 WPM, 37.5s. Clear, fluent, confident delivery at a natural conversational pace. Varied vocabulary ("enhance and improve", "describing its personality"), good rhythm.
- **Test Overview 5s (City Interview):** 4 responses to the urban life interview (Q1 68 words, Q2 72 words, Q3 68 words, Q4 94 words). All 4 earned Score 5. ETS noted: *"Delivery is generally smooth and easy to follow. Pauses and fillers, such as 'um' and 'uh', are natural and do not interfere with meaning."*
- Practice page: `practice/4b. take-an-interview.html`.

## 5. Question archetypes in the Interview
Each interview has 4 questions progressing from personal to broad:
1. **Q1 Personal Recall:** memory, routine, or life experience (e.g. last time you visited a city, your commuting habits). Warm-up for fluency.
2. **Q2 Reaction or Preference:** explore feelings, pros/cons, or choice between two options (e.g. car vs public transit; quiet vs dynamic).
3. **Q3 Opinion with Support:** take a stand on a claim and justify it with reasons (e.g. do city dwellers live more interesting lives? Should companies offer flexible hours?).
4. **Q4 Policy or Future Prediction:** evaluate a broader societal trend, technological change, or policy recommendation (e.g. should governments build more parks? What happens if commuting disappears?).

## 6. How I score your recordings
1. **Recording:** `4a. listen-and-repeat.html` and `4b. take-an-interview.html` record in browser and save directly to your **Downloads** folder (`LR_T*` and `INT_T*`). They are not in git, so your voice is never pushed.
2. **Transcription:** `python tools/lr_transcribe.py` (for Task A) and `python tools/interview_transcribe.py` (for Task B) transcribe clips locally with faster-whisper `small.en` and `medium.en` verbatim (temperature 0, no script prompt, no LLM clean-up).
3. **Metrics extracted:** word count, duration spoken, speaking rate (WPM), long pauses (>= 1.5s), filler words, and audio level stats.
4. **Scoring:** I read the report and evaluate each response against the ETS rubric (0-5) in the terminal. The tool never assigns the final score.
5. **Uncertain words:** where models disagree or confidence is low, I do not penalise you.

**Limits [mine]**
- Whisper transcribes words accurately, but cannot grade accent, intonation contours, or physical voice resonance.
- For pronunciation intelligibility, we cross-check model agreement and confidence scores.
- My scores are human estimates aligned to ETS rubric standards.

## 7. Tips
- **Listen and Repeat:** hold meaning first, then key content words (nouns, verbs), then endings (-s, -ed). Do not restart.
- **Interview timing structure (45s):**
  - *Direct answer* (5s): answer the question immediately in one sentence.
  - *Primary reason* (15s): state why with a clear connective (*"First of all...", "I think this because..."*).
  - *Specific example or detail* (15-20s): give a concrete memory, scenario, or contrast (*"For instance, when I...", "Unlike X, Y allows..."*).
  - *Wrap-up* (5s): quick concluding summary (*"So that's why I prefer..."*).
- **Target pacing:** aim for ~65 to 85 words in 45s (~95 to 125 WPM). Speaking too fast causes stumbling; speaking under 50 words leaves ideas unelaborated.
- **Fillers:** do not panic over an "um" or "uh". ETS sample 5s have natural fillers. What hurts is long silence (> 2 seconds of dead air).

## 6. Patterns from my log
- None yet. List repeated mistakes here with a one-line fix once recordings are logged.

## 7. Redo queue
- None yet.
