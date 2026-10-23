# Speaking log

Records only. How to improve lives in `guides/speaking.md`.

Sources: `resources/audio/lessons/speaking/`, `resources/audio/samples/speaking/` (model answers), and `resources/audio/tests/*/speaking/`.

## Scoreboard (2026-10-23)

Scoring model: 11 items total (7 Listen & Repeat + 4 Take an Interview) scored 0-5 each = **raw max 55** (Updated Test Overview, Table 1). Scaled score is linear approximation (`30 * raw / 55`). Bands map tentatively to ETS Table 6 Speaking column (28-30 -> 6, 27 -> 5.5, 25-26 -> 5, 23-24 -> 4.5, 20-22 -> 4).
*Caveat: ETS uses weighted equipercentile linking to convert raw to scaled speaking scores, so linear scaling is an approximation.*

| Test | Source | Listen & Repeat (/35) | Take an Interview (/20) | Raw (/55) | Scaled (/30) | Tentative Band |
|---|---|---:|---:|---:|---:|---:|
| 1 | Full-length 1 | 28–30 | 18–19 | 46–49 | 25.1–26.7 | 5.0 (to 5.5) |
| 2 | Full-length 2 | 28–32 | (pending) | | | |
| 3 | Teacher Resources 1 | | | | | |
| 4 | Teacher Resources 2 | | | | | |
| 5 | Teacher Resources 3 | | | | | |
| 6 | Teacher Resources 4 | | | | | |
| 7 | Teacher Resources 5 | | | | | |
| **Attempted** | | **56–62 / 70** | **18–19 / 20** | **46–49 / 55** | **25.1–26.7** | **5.0 (to 5.5)** |

## Tool and data checks (2026-10-23)
- **Task A (Listen & Repeat):** `practice/4a. listen-and-repeat.html` + `tools/lr_transcribe.py` (faster-whisper small.en + medium.en).
  - 49 prompt sentences match audio across all 7 tests.
  - Downloads audio clips directly to `~/Downloads` (`LR_T*`).
- **Task B (Take an Interview):** `practice/4b. take-an-interview.html` + `tools/interview_transcribe.py`.
  - 28 interview questions (7 tests x 4) verified against media. Tests 1, 2, 5, 6, 7 are video (`.mp4`); Tests 3, 4 are audio (`.mp3`).
  - All 35 media files (7 directions + 28 questions) verified on disk.
  - Test 1 Q1: video asks the city-travel question from the Test Overview ("think back to the last time you visited a city..."), which is reflected in the page and tool.
  - Downloads audio clips directly to `~/Downloads` (`INT_T*`).
  - Automated Playwright suite (`/tmp/iv/pw_interview.py`): 8/8 checks passed with zero errors.

## Attempts

### Test 1 · Full-length 1

#### Listen and Repeat (run 20261023-113029) · Score: 28–30 / 35
| Q | Script (manager) | What was heard (small.en / medium.en) | Score | Analysis |
|---|---|---|:---:|---|
| 1 | We have a variety of wildlife. | exact | 5 | Exact repetition. |
| 2 | Bears, wolves, and large cats are to the right. | "last cats" | 3–4 | "large" heard as "last" by both models. 4 if pronunciation slip; 3 if actual word substitution. |
| 3 | You can find sea lions and elephants further down the path. | "see sea lions" | 4 | "find" replaced with related word "see". Meaning preserved (ETS 4 pattern). |
| 4 | Please, no outside food or drinks, and do not feed the animals. | "foods or drinks" | 4 | Number marker changed ("food" -> "foods"). Meaning preserved. |
| 5 | Avoid banging or tapping on the displays and enclosures. | "and encloses" | 3–4 | "or" -> "and", "enclosures" -> "encloses". 4 if pronunciation slip; 3 if wrong word form. |
| 6 | For those with children, we offer summer camps and educational opportunities. | exact | 5 | Exact repetition. |
| 7 | The visitor’s center, located near the front entrance, can give you more information. | "visitor... at" | 4 | Possessive dropped ("visitor's" -> "visitor") and preposition swapped ("near" -> "at"). Meaning preserved. |

#### Take an Interview (run 20261023-120624) · Score: 18–19 / 20
Scenario: Research study on urban life.

| Q | Interviewer question | Your response (verbatim transcript) | Spoken (s) | Words | WPM | Score | Analysis |
|---|---|---|---|---|---|:---:|---|
| 1 | Last time you visited a city | "The last time I visited a different city than the one I live in was Pokhara. I visited Pokhara about six months ago and I really like the ambitious and I really like the vibe and the nightlife of Pokhara. You see, it's lively and it never fades away. And the purpose for my visit was for refreshment and for celebrating my birthday party." | 37.2 | 64 | 103.2 | 4.5–5 | Fully answers both parts (why traveled: refreshment & birthday; what liked: vibe, nightlife). Conversational markers ("You see, it's lively and it never fades away"). Minor vocabulary approximation slip: "ambitious" for "ambiance/ambience". |
| 2 | Reaction to cities & why | "Yes, cities can feel draining and overwhelming, but for me, cities have always been exciting and it's full of life for me. And I feel so because the night life and the sunsets and the people we find to interact in our daily lives is really mesmerizing. I love interacting with people, I love having those long meetings, I love having access to talk with all the influential people and everybody, I can pick minds from everybody. That's why I find cities exciting." | 39.9 | 83 | 124.9 | 5 | Outstanding response. 83 words matches the ETS sample 5 benchmark (83 words / 133 WPM). Directly acknowledges the prompt contrast ("draining and overwhelming, but for me..."), elaborates with concrete details (sunsets, meetings, influential people), and wraps up cleanly. Minor idiom slip ("pick minds" for "pick brains") does not affect high score. |
| 3 | Do city dwellers live more interesting lives? | "In my opinion, the people who live in the cities definitely have more exciting life and interesting life. As you have mentioned, they have a lot of more professional opportunities and exciting things to do every day. I completely agree with the stance that people here have more opportunities than there in the village. It's not only about professional opportunities, but it's also about having access to all the transportation and food and beverages, etc." | 42.1 | 77 | 109.8 | 4–4.5 | Clear stance taken and supported. Connects prompt points with original ideas (transportation, food, beverages). Pacing steady (110 WPM). Leans slightly on prompt wording early on and ends on "etc." rather than a full concluding wrap-up sentence. |
| 4 | Should city governments create more parks? | "I completely agree with the fact that cities should have more green spaces such as parks. It directly contributes to the happiness of the individuals living around the city. As you know most of the cities are made haphazardly there's no proper planning and urbanization and due to that there are no trees and parks available but the government should definitely separate places to make more parks because that allows people to gather together in a natural environment and enjoy." | 43.6 | 80 | 110.1 | 4.5–5 | Strong, confident flow for 43.6s without long pauses. Uses strong vocabulary ("haphazardly", "natural environment", "directly contributes"). Solid policy reasoning (unplanned growth leads to lack of trees, so government must set aside park land for social gathering). Minor slip: "separate places" (meant "set aside space") and "planning and urbanization" (meant "urban planning"). |

### Test 2 · Full-length 2

#### Listen and Repeat (run 20261023-113819) · Score: 28–32 / 35
| Q | Script (speaker) | What was heard (small.en / medium.en) | Score | Analysis |
|---|---|---|:---:|---|
| 1 | Welcome to our campus gym. | "Sim" / "Simi" | 4 | Both models heard non-word for "gym". Imprecise pronunciation, meaning otherwise clear. |
| 2 | Cardio machines are near the entrance. | "Cardiomycenes" / exact | 4–5 | Disagreement between models; medium.en heard exact phrase. |
| 3 | Free weights are in the back. | "wits" / exact | 4–5 | Disagreement between models; medium.en heard exact phrase. |
| 4 | All of our locker rooms are equipped with showers and towels. | "sours and dowels" | 3–4 | Both models heard "sours and dowels". Sound-level articulation slip. |
| 5 | Our fitness instructors hold exercise classes over here. | exact | 5 | Exact repetition. |
| 6 | You can check the schedule for available classes and timings. | added "the" | 4 | Function word inserted ("the available"). Meaning preserved. |
| 7 | If you have any questions, please seek assistance from the attendants at the help desk. | "attendance" / exact | 4–5 | Disagreement between models; medium.en heard exact phrase. |

#### Take an Interview (pending)
| Q | Interviewer question | Your response | Spoken (s) | Words | WPM | Score | Notes |
|---|---|---|---|---|---|:---:|---|
| 1 | Important to live close to school/work? | | | | | | |
| 2 | Commute by car vs public transit? | | | | | | |
| 3 | Ways to make commuting more enjoyable | | | | | | |
| 4 | Effects if commuting disappears entirely | | | | | | |

## Difficulties
- Word-ending precision: dropped possessive ("visitor's"), plural swap ("foods"), verb ending ("encloses"). Matches CTW ending vulnerability.
- Consonant articulation under speed: "showers and towels" -> "sours and dowels".
