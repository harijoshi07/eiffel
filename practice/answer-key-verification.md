# Daily Life Reading: Answer Key Verification

Checked: all 70 Reading in Daily Life answers (Q11–15 in 14 modules) in `read_in_daily_life_clean.json` against the "Answer Key" pages of `resources/pdfs/*/toefl-ibt-*practice-test-*.pdf`.

Result: **70 / 70 match.** No changes needed to the answer data.

| Test | Module | PDF key page | Q11 | Q12 | Q13 | Q14 | Q15 |
|---|---|---|---|---|---|---|---|
| Full-Length Practice Test 1 | 1 | p.13 | D | C | B | C | B |
| Full-Length Practice Test 1 | 2 | p.14 | C | C | A | C | D |
| Full-Length Practice Test 2 | 1 | p.13 | C | C | C | A | A |
| Full-Length Practice Test 2 | 2 | p.14 | B | C | B | A | C |
| Teacher Resources Test 1 | 1 | p.12 | B | D | D | B | A |
| Teacher Resources Test 1 | 2 | p.13 | B | B | C | C | A |
| Teacher Resources Test 2 | 1 | p.13 | C | B | B | D | C |
| Teacher Resources Test 2 | 2 | p.14 | B | B | B | A | D |
| Teacher Resources Test 3 | 1 | p.13 | C | D | A | C | D |
| Teacher Resources Test 3 | 2 | p.14 | B | C | C | B | A |
| Teacher Resources Test 4 | 1 | p.13 | B | C | C | B | C |
| Teacher Resources Test 4 | 2 | p.14 | A | B | B | A | C |
| Teacher Resources Test 5 | 1 | p.13 | A | D | B | C | A |
| Teacher Resources Test 5 | 2 | p.14 | A | C | D | B | C |

## Wording verification (passages, questions, options)

Checked every passage, question stem, and option in `read_in_daily_life_clean.json` against the text layer of the matching PDF module.

- Passages: 28 / 28 verbatim matches
- Question stems: 70 / 70 verbatim matches
- Options: 280 / 280 verbatim matches
- Order check: all 350 stems and options appear in the PDF in the correct sequence (stem, then A–D)

Fixed during this check:
- **Full-Length Practice Test 2, Module 1, Q15 option D:** the JSON option had the next passage ("The Impact of Sports on Social Integration…") merged into it, plus highlight markers. Corrected to "Employees might have free time then."

Notes:
- The layout of "(begin highlight)" / "(end highlight)" markers in the PDFs is an extraction artifact. The JSON keeps the plain text.
- Page footers ("TOEFL iBT® Practice Test N", "Teacher Resources - Practice Test N") and "Read a …" headings are excluded from the data.
