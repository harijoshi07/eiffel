# TOEFL iBT 2026 prep

## Layout
- `00 - Test Map.md`: format and scoring.
- `01 - Study Plan.md`: 8-week plan.
- `logs/`: one log per section (`reading.md`, `listening.md`, `writing.md`, `speaking.md`). Each entry holds your exact answers, the questions, your reasoning, the error, and the fix.
- `logs/reading-guide.md`: short error guide for reading (scores, patterns, per-task routine).
- `practice/`: interactive pages. `complete-the-words.html` and `daily-life-reading.html` (Reading).
- `resources/pdfs/`: the 7 test PDFs (`full-length-1/2`, `teacher-resources-1` to `-5`) and 3 guides (`guide-writing-rubrics`, `guide-lesson-writing`, `guide-lesson-listening`). Each PDF has a `.md` beside it. **Use the `.md` as the input.**
- `resources/audio/`: `lessons/listening`, `lessons/speaking`, `samples/speaking`, and `tests/<student-1|student-2|teacher-1..5>/<listening|speaking>/`.

## Log entry format
1. Context: test, module, and the PDF page (PDF page number).
2. Exact question and options.
3. Your answer and the correct answer (from the answer-key pages).
4. Why it was wrong (your reasoning, or "not recorded").
5. The fix: the rule to apply next time.

Each section log also ends with Difficulties, Improvements, and Tips.

## Rules
- Answers come from the PDF answer-key pages. Never from reasoning about the passage.
- Write "not recorded" instead of guessing missing data.
- PDFs and audio stay local (listed in `.gitignore`). Markdown, logs, and HTML are committed.
