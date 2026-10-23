# TOEFL iBT 2026 prep

## Layout
- `00 - Test Map.md`: format at a glance (items per task, timing, can I go back) and scoring.
- `01 - Study Plan.md`: 8-week plan.
- `logs/`: **what happened.** One record per section (`reading.md`, `listening.md`, `writing.md`, `speaking.md`): exact questions, your answers, the key, your reasoning, the error.
- `guides/`: **how to improve.** One playbook per section (same four names): failure modes, per-question-type routines, quick-reference tips, and the redo queue. Update these when the logs show a pattern.
- `practice/`: interactive pages. `1a. complete-the-words.html`, `1b. daily-life-reading.html` and `1c. academic-passages.html` (Reading), and `2a. listen-and-respond.html` (Listening Type A), `2b. listen-to-conversation.html` (Type B), `2c. listen-to-announcement.html` (Type C) and `2d. listen-to-academic-talk.html` (Type D); the Listening pages play audio from `resources/audio`. `3a. build-a-sentence.html` (Writing, Build a Sentence) and `3b. write-an-email.html` (Write an Email: 7-minute timer, word count, rubric self-rating; no auto-score) and `3c. academic-discussion.html` (Academic Discussion: 10-minute timer, professor and student posts, word count, rubric self-rating; no auto-score), and `4a. listen-and-repeat.html` (Speaking, Listen and Repeat: plays each sentence once, records you, saves the audio to `recordings/`).
- `resources/pdfs/`: the 7 test PDFs (`full-length-1/2`, `teacher-resources-1` to `-5`) and 5 guides (`guide-writing-rubrics`, `guide-lesson-writing`, `guide-lesson-listening`, `guide-speaking-rubrics`, `guide-speaking-sample-responses`). The PDFs are the source of truth. `resources/docx/` holds Word copies for cross-checking only (TR3–TR5 are page images).
- `tools/`: `serve.py` serves the vault on localhost and saves speaking recordings straight into `recordings/` (start it before the speaking pages). `lr_transcribe.py` transcribes the Listen and Repeat recordings locally (faster-whisper) and compares them with the prompts. It does not score. `lr_sentences.json` holds the 49 prompt sentences.
- `recordings/`: your own voice recordings from the speaking pages. Local only, git-ignored.
- `resources/audio/`: `lessons/listening`, `lessons/speaking`, `samples/speaking`, and `tests/<student-1|student-2|teacher-1..5>/<listening|speaking>/`.

## Log entry format
1. Context: test, module, and the PDF page (PDF page number).
2. Exact question and options.
3. Your answer and the correct answer (from the answer-key pages).
4. Why it was wrong (your reasoning, or "not recorded").
5. The fix: one line in the log, and the general rule in `guides/`.

Each log ends with Difficulties. Fixes and rules go in the matching file in `guides/`, not in the log.

## Rules
- Answers come from the PDF answer-key pages. Never from reasoning about the passage.
- Write "not recorded" instead of guessing missing data.
- PDFs and audio stay local (listed in `.gitignore`). Markdown, logs, and HTML are committed.
