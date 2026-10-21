# Reading log

Records only: what happened, with exact answers. How to improve lives in `guides/reading.md`.

Sources: `resources/pdfs/*.pdf` (page refs = PDF page number). Answer keys: the answer-key pages of each PDF.

## Reading scoreboard: all 7 tests (2026-10-21)

Test numbers follow the order of the PDFs: Test 1 = Full-Length 1, Test 2 = Full-Length 2, Tests 3-7 = Teacher Resources 1-5. Each test has 2 modules of 20 questions (10 Complete the Words, 5 Daily Life, 5 Academic), so 40 per test.

| Test | Source | CTW /20 | Daily Life /10 | Academic /10 | **Raw /40** | % | Scaled /30 | **Tentative band** | Lost points |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FL1 | 20 | 10 | 10 | **40** | 100% | 30.0 | **6** | none |
| 2 | FL2 | 19 | 9 | 10 | **38** | 95% | 28.5 | **5.5 (to 6)** | CTW M1 (unrecorded), DL Q13 |
| 3 | TR1 | 19 | 9 | 10 | **38** | 95% | 28.5 | **5.5 (to 6)** | CTW `struc[5]`, DL Q13 |
| 4 | TR2 | 19 | 10 | 8 | **37** | 92.5% | 27.75 | **5.5** | CTW `Discov[5]`, AP Q18, AP Q20 |
| 5 | TR3 | 20 | 10 | 9 | **39** | 97.5% | 29.25 | **6** | AP Q19 |
| 6 | TR4 | 20 | 8 | 10 | **38** | 95% | 28.5 | **5.5 (to 6)** | DL Q11, DL Q13 |
| 7 | TR5 | 19 | 10 | 8 | **37** | 92.5% | 27.75 | **5.5** | CTW `proc[5]`, AP Q20 (M1), AP Q20 (M2) |
| | **All 7** | **136/140** | **66/70** | **65/70** | **267/280** | **95.4%** | **28.6** | **5.5 (to 6)** | 13 points |

Per-section accuracy: Complete the Words 97.1%, Daily Life 94.3%, Academic 92.9%. Average per test: 38.1/40.

### How the band is estimated
1. Scaled score = 30 x raw / 40, a straight-line estimate.
2. Band = ETS's own mapping of the old 0-30 Reading scale to bands (ETS, *A banded score scale for the TOEFL iBT test*, 2026, Table 6): 6 = 29-30, 5.5 = 27-28, 5 = 24-26, 4.5 = 22-23, 4 = 18-21.
3. Where a test sits on a boundary the band is shown as a range: the lower number if you round the scaled score down, the upper if you round up. At 28.5 the result is 28 (5.5) or 29 (6).

### Limits of this estimate
- **No official raw-to-band table exists.** ETS scores Reading with item response theory and does not publish raw-to-scaled conversions. The linear step in 1 is my assumption.
- **The real section is adaptive.** The second module is easier or harder depending on how you do on the first. Practice modules are fixed, so a score of 38/40 here does not equal 38 on a real upper-level module.
- **One question matters at the top.** Each raw point is 0.75 scaled points, so one question is enough to move a result between 5.5 and 6.
- **This is Reading only.** The overall band is the average of Reading, Listening, Writing and Speaking, rounded to the nearest half band.
- Only 5.5 or 6 is claimed, because 267/280 is the only data. Treat it as an estimate and not a prediction.

### What the seven tests show
- **Lost points by type:** Academic 5, Daily Life 4, Complete the Words 4. They are spread out, so no single area explains the gap between 5.5 and 6.
- **Weakest tests:** Tests 4 and 7 (37/40). Both lose two points on Academic, and each includes one of your two missed insert-sentence items (Test 4 AP Q20, Test 7 AP Q20 in M1).
- **Clean sets:** there are 42 module-section scores (14 modules x 3 sections). 30 were perfect. The other 12 each lost one point, except Test 6 Daily Life M1, which lost two (3/5).
- **Recurring losses:** the same causes repeat across tests (word-form traps, near-paraphrase options, insert sentences). They are listed in `guides/reading.md`.

## 1. Complete the Words

### Context
- Task: fill the missing letters of a paragraph. `[N]` = blank of N letters (`struc[5]` = 5 letters).
- 10 items per module, 14 modules (FL1, FL2, TR1–TR5; M1 and M2 each).
- Session 2026-10-20: **136/140 (97.1%)**, about 17 min total.
- Source files: `full-length-1.pdf`, `full-length-2.pdf`, `teacher-resources-1.pdf` to `teacher-resources-5.pdf`.

### Results
| Test | M1 | M2 |
|---|---|---|
| FL1 | 10/10 (0:24) | 10/10 (0:23) |
| FL2 | **9/10** (0:32) | 10/10 (0:32) |
| TR1 | **9/10** (2:07) | 10/10 (0:44) |
| TR2 | 10/10 (1:43) | **9/10** (2:23) |
| TR3 | 10/10 (1:35) | 10/10 (1:39) |
| TR4 | 10/10 (0:56) | 10/10 (0:44) |
| TR5 | 10/10 (0:50) | **9/10** (0:53) |

Only misses were logged per item. Typed answers for the 10/10 modules were not recorded.

### Misses
| # | Module, item (from md) | Blank | You typed (word) | Correct | Why it was wrong |
|---|---|---|---|---|---|
| 1 | TR1 M1, Q3: `...social struc[5], written lang[5]...` | 5 | structure | structures | Dropped the plural -s. The list "social structures, written languages, and..." needs a plural noun. |
| 2 | TR2 M2, Q10: `...hide oce[3] beneath. Discov[5]...` | 5 | discoveries | discovering | Found a plural noun that fit 5 letters and stopped. You only generated "discoveries". The blank starts a sentence, so it needs a gerund (-ing). |
| 3 | TR5 M2, Q7: `...to unc[4] the proc[5] that ha[2] influenced...` | 5 | procedure | processes | Fit the letters but not the meaning. "Procedures" are steps; the sentence means natural processes. |
| 4 | FL2 M1 | ? | not recorded | ? | Item not logged. Re-do FL2 M1 and record it here. |

Thought process: for #2 you explained it (generated only the plural noun). For #1 and #3 it was not recorded. Likely cause: you accepted the first word that fit the letter count.

### Difficulties
- Suffix traps: same-length pairs (structure/structures, discoveries/discovering, procedure/processes).
- Speed was not the only cause: the slowest modules (TR1 M1 2:07, TR2 M2 2:23) both had misses, but FL2 M2 (0:32) was perfect.

## 2. Read in Daily Life (Questions 11–15)

### Context
- Each module: one notice (Q11–12) and one social-media post or email (Q13–15). 14 modules, 70 questions.
- Source: `resources/pdfs/full-length-1.pdf` and the other test PDFs. Keys verified against the answer-key pages on 2026-10-20 (70/70).
- Session 2026-10-20 (export 10:33 PM): **66/70 (94%)**, four misses. FL1 M1 was redone after a wrong saved note was fixed, and it scored 5/5.

### Results
| Module | Score | Time |
|---|---|---|
| FL1 M1 | 5/5 | 00:35 |
| FL1 M2 | 5/5 | 01:13 |
| FL2 M1 | **4/5** | 01:02 |
| FL2 M2 | 5/5 | 01:36 |
| TR1 M1 | **4/5** | 02:08 |
| TR1 M2 | 5/5 | 03:11 |
| TR2 M1 | 5/5 | 02:31 |
| TR2 M2 | 5/5 | 02:30 |
| TR3 M1 | 5/5 | 02:49 |
| TR3 M2 | 5/5 | 02:14 |
| TR4 M1 | **3/5** | 01:18 |
| TR4 M2 | 5/5 | 02:21 |
| TR5 M1 | 5/5 | 02:19 |
| TR5 M2 | 5/5 | 01:37 |

### Misses (exact text from the answer data)

**1. FL2 M1, Q13** · type: Purpose (the page tagged it Detail) · You: **A** · Correct: **C**
- Why did Ms. Rogers send the email to Mr. Suzuki?
  - A. To assist him with an audit process
  - B. To remind him to update inventory logs every day
  - C. To inform him of an upcoming event
  - D. To request his input on how to revise a process
- Your reasoning: the email says department heads must "attend and assist with the audit process." That sentence is in the email, but it is a detail, not the purpose.
- Why it was wrong: you picked a true detail instead of the purpose. The email's main reason is the upcoming event (the other items are supporting details).
- Fix: for "why did X send the email", find the sentence that starts the message, not the sentence with the most detail.

**2. TR1 M1, Q13** · type: Inference · You: **A** · Correct: **D**
- What can be inferred about Mr. Santiago?
  - A. He is about to celebrate his birthday.
  - B. He has used Rebecca Yang's facility in the past.
  - C. He is a professional event organizer.
  - D. He has requested information about Rebecca Yang's facility.
- Your note: you knew the party was for his mother's birthday, not his own. Then you doubted the passage and nearly checked the PDF to see whether it said his birthday.
- Why it was wrong: an inference must follow from the text. Option A repeats a surface detail, and you went with it.
- Fix: check who the celebration belongs to, then check that the option is the one the text supports, not one that reuses a word.

**3. TR4 M1, Q11** · type: Detail · You: **C** · Correct: **B**
- How many people will dine with Ms. Green?
  - A. 2 · B. 3 · C. 4 · D. 5
- Your reasoning: the reservation is for 4, so you chose 4 directly.
- Why it was wrong: the reservation count includes Ms. Green. She is one of the 4, so 3 more people dine with her.
- Fix: read the question's subject ("with Ms. Green") and subtract the person named in it.

**4. TR4 M1, Q13** · type: Purpose · You: **A** · Correct: **C**
- What is this form used for?
  - A. Applying for a new library card
  - B. Reporting problems with library computers
  - C. Booking time to use library computers
  - D. Requesting software installation on computers
- Your reasoning: the form asks for a library card number, so you chose "applying for a card".
- Why it was wrong: an ID on a form does not show its purpose. The form's title and the field labels show what it is for.
- Fix: for "what is this form used for", read the title and the action words first.

### Hesitations and conflicts (recorded, not verified)
- TR3 M1, Q13 ("What can be concluded about the library?"): you were torn between A and B and chose A. Scored correct, but the reasoning was a guess. Re-check it.
- TR5 M2, Q14 (where the event takes place): you guessed "Town Square" from the parking note. Scored 5/5 in the export, so the guess was right. Re-check the reasoning before you rely on it.
- TR2 M2, Q13: not straightforward, but no option contradicted your choice. Scored correct.
- **Your narrative conflicts with the export:**
  - You described FL2 M1 as a miss on Q1, and "to ask" is not an option. The export shows Q13, your answer A.
  - You described the TR1 M1 inference as Q30. Daily Life runs Q11–15, so this is Q13.
  - Please confirm these, and I will correct the log.

### Difficulties
- Distractors that reuse a passage word or a true detail (audit, birthday, library card).
- Purpose and inference questions (Q13 in four modules) were the weakest type.
- Counting question misread: the person named in the question is part of the total.

## 3. Read an Academic Passage (Q16–20)

### Context
- Each module: one passage of about 200 words (1–3 paragraphs) and 5 questions. 14 modules, 70 questions.
- Keys: TR3–TR5 checked against the PDF answer-key pages; FL1, FL2, TR1 and TR2 checked against the Word key text.
- Session 2026-10-21 (export 10:21 AM): **65/70 (92.9%)**. Page: `practice/1c. academic-passages.html`.
- Type tags come from keyword matching and can be wrong.
- Timer: only 7 of 14 modules were timed (the rest show 00:00).

### Results
| Module | Passage | Score | Time |
|---|---|---|---|
| FL1 M1 | The Mirror Test | 5/5 | – |
| FL1 M2 | The Paradox of Choice | 5/5 | – |
| FL2 M1 | The Impact of Sports on Social Integration | 5/5 | – |
| FL2 M2 | The Human Microbiome | 5/5 | – |
| TR1 M1 | The Effects of Urbanization on Bird Populations | 5/5 | 03:06 |
| TR1 M2 | The History of Photography | 5/5 | – |
| TR2 M1 | Aqueducts | **4/5** | 03:02 |
| TR2 M2 | Sleep Patterns | **4/5** | 02:40 |
| TR3 M1 | Jet Stream Dynamics | 5/5 | – |
| TR3 M2 | The Golden Age of Television | **4/5** | 03:00 |
| TR4 M1 | Ancient Egyptian Medicine | 5/5 | – |
| TR4 M2 | The Origins of Theater | 5/5 | 04:27 |
| TR5 M1 | Mysterious Viking Sunstones | **4/5** | 06:54 |
| TR5 M2 | Renaissance Art Techniques | **4/5** | 02:37 |

Timed modules averaged 3:41. The slowest (TR5 M1, 6:54) was still a miss, so the problem there was method, not time.

### Misses
Failure-mode codes (F1–F5) are defined in `guides/reading.md`.

**A1. TR2 M1 Q18** · Purpose · You: **D** · Key: **B** · Mode: **F2**
- Why does the author mention the Pont du Gard in France?
  - A. To illustrate how aqueducts were constructed
  - B. To give an example of a well-preserved aqueduct
  - C. To explain the importance of aqueducts in France
  - D. To describe the engineering techniques used by the Romans
- Deciding sentence: "Some Roman aqueducts, like the Pont du Gard in France, **are still standing today**, showcasing the Romans' remarkable engineering skills."
- Your reasoning: you were torn between B and D. You read "showcasing" as "describing", and noted that "still standing today" pointed to B but chose D. Your own verdict: "I made a mistake."
- What went wrong: you answered with the topic of the sentence (engineering skill). The question asks about the job of the example. The claim attached to the example is *still standing*, so the answer is preserved. Nothing in that sentence describes techniques.
- Rule: "why mention X" means the claim attached to X.

**A2. TR2 M2 Q20** · Insert · You: **A** · Key: **C** · Mode: **F4** · Your cause tag: Guessed
- Insert: "But what affects birds' sleep norms?"
- Position C is the start of paragraph 3, right before "Sleep patterns have evolved based on environmental needs."
- Your reasoning: you eliminated C and D early and compared only A and B. You rejected C because it starts a different paragraph. You liked A because the next sentence is about migratory flights affecting sleep.
- What went wrong: you never tested C, and a paragraph start is a legal position. "But" needs a finished bird statement before it, and C follows the last bird sentence. The question needs its answer right after, and "environmental needs" answers it; "sleep norms" echoes "Sleep patterns" in that very sentence. At A, "But" follows only "Many bird species can sleep while flying", which gives it nothing to contrast with.
- Rule: run the four-step insert check on all four positions, not two.

**A3. TR3 M2 Q19** · Structure · You: **D** · Key: **C** · Mode: **F3** · Your cause tag: Vocabulary (reclassified)
- What is the relationship between paragraphs 2 and 3?
  - A. Paragraph 3 expands on the challenges mentioned in paragraph 2.
  - B. Paragraph 3 provides examples of the formats discussed in paragraph 2.
  - C. Paragraph 3 introduces a new issue that was not covered in paragraph 2.
  - D. Paragraph 3 contradicts the success of TV shows mentioned in paragraph 2.
- Deciding text: P2 describes shows (The Twilight Zone, I Love Lucy, live broadcasts). P3 opens "However, the Golden Age was not without challenges" and ends "Nonetheless, the period left an indelible mark".
- Your reasoning: you thought paragraph 2 already covered "issues", so C looked false. You read "However" plus challenges as a contradiction of the success in paragraph 2, and chose D. (Your note has dictation garbles, "sows" and "sakshas", which I left out.)
- What went wrong: "issues" does appear in P2, but there it is the social issues I Love Lucy tackled. In P3 the problems are the industry's challenges. Same word, different referent. D fails because P3 ends "Nonetheless… indelible mark", so it does not deny the success. A fails because P2 mentions no challenges.
- Rule: write each paragraph's job in six words first. P2 is examples of the era's shows, and P3 is challenges and legacy.

**A4. TR5 M1 Q20** · Insert · You: **C** · Key: **A** · Mode: **F4** · No cause tag
- Insert: "This is all the more remarkable considering the lack of technology at the time."
- Position A is right after sentence 1 ("…navigated their ships with remarkable precision across the North Atlantic during the medieval period").
- Your note: "i thought it made sense at 3rd position. not initially." It is unclear whether A was your first choice.
- What went wrong: "remarkable" echoes "remarkable precision" in sentence 1, and "at the time" echoes "medieval period". At C, the sentence follows a description of the sunstone, which is itself a tool, and sits just before "However, evidence of actual sunstone use remains scarce".
- Rule: find the nearest earlier word the inserted sentence repeats.

**A5. TR5 M2 Q20** · Detail · You: **C** · Key: **B** · Mode: **F3** · Your cause tag: Inference (reclassified)
- What was one benefit of oil paints over tempera paints?
  - A. They were easier to make.
  - B. They could be applied in layers.
  - C. They were available in more realistic colors.
  - D. They could be easily removed if necessary.
- Deciding sentence: "Because oil paints dry more slowly than tempera paints, artists could use blending and **layering** to create more texture and richer colors."
- Your reasoning: the text says more texture and richer colors, and you took richer colors to mean more realistic colors.
- What went wrong: "richer" is not "realistic". "More realistic" is from paragraph 1, about Renaissance paintings in general. No inference was needed; the stated result is layering.
- Rule: choose the option whose words are in the sentence that holds both X and the contrast.

### Difficulties
- Options that sound like the passage but change one word (realistic, issues, techniques).
- Insert questions: 2 of 4 missed.
- Relationship questions, where the same word can refer to different things in different paragraphs.

