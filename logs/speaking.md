# Speaking log

Records only. How to improve lives in `guides/speaking.md`.

Sources: `resources/audio/lessons/speaking/`, `resources/audio/samples/speaking/` (model answers), and `resources/audio/tests/*/speaking/`.

## Tool and data checks (2026-10-23)
Page: `practice/4a. listen-and-repeat.html`. Transcription: `tools/lr_transcribe.py` (faster-whisper small.en and medium.en, verbatim). No attempts yet.
- 49 Listen and Repeat sentences (7 tests x 7) were taken from the PDFs (Test 1 p.34, 2 p.35, 3 p.33, 4 p.35, 5 p.38, 6 p.38, 7 p.37) and checked against the audio by transcription: all 49 match. Two harmless variants: Test 4 Q4 "aids" (PDF) vs "aides" (heard), Test 6 Q3 "area's" (PDF) vs "area is" (heard). Both are accepted by the tool.
- Test 4 Q4 differs in the Word file ("assitance" typo, wrapped as "assis tance" in the PDF). The PDF wording was kept and the line-wrap split removed. Word files were checked for Tests 1-4 only (Tests 5-7 are page images).
- Speaking windows (8, 10 or 12 s by sentence length) are my guess. ETS says only "8-12 s".
- `tools/serve.py` (local server, 127.0.0.1 only) writes recordings into `recordings/speaking/listen-and-repeat/`. Tested with a fake microphone: 7 recordings and the manifest landed on disk. Path-traversal, bad-name and foreign-origin requests were rejected. Test files were deleted afterwards.
- The page was tested in Chromium with a fake microphone. The folder picker was tested with a stub, not the real picker. **Not tested in Arc.**

## Attempts
No attempts logged yet. Add one row per item:

| Task | Test | Prompt or sentence (exact) | Recording file | Score (0–5) | What was wrong | Fix |
|---|---|---|---|---|---|---|

## Difficulties
- None logged yet.
