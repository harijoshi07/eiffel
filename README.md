# TOEFL iBT 2026 prep

## Layout
- `00 - Test Map.md`: format and scoring.
- `01 - Study Plan.md`: 8-week plan.
- `logs/`: **what happened.** One record per section (`reading.md`, `listening.md`, `writing.md`, `speaking.md`): exact questions, your answers, the key, your reasoning, the error.
- `guides/`: **how to improve.** One playbook per section (same four names): failure modes, per-question-type routines, quick-reference tips, and the redo queue. Update these when the logs show a pattern.
- `practice/`: interactive pages. `complete-the-words.html`, `daily-life-reading.html` and `academic-passages.html` (Reading), and `listen-and-respond.html` (Listening Type A; plays audio from `resources/audio`).
- `resources/pdfs/`: the 7 test PDFs (`full-length-1/2`, `teacher-resources-1` to `-5`) and 3 guides (`guide-writing-rubrics`, `guide-lesson-writing`, `guide-lesson-listening`). The PDFs are the source of truth. `resources/docx/` holds Word copies for cross-checking only (TR3–TR5 are page images).
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
