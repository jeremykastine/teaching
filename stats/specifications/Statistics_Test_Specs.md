# Statistics Test Specifications

## Minimal answer-area labels (October 26, 2026)

- Keep each student answer area as clean as possible: include only the question number, necessary part labels such as (a) and (b), and the applicable points. For a single-part question, use just its number and points; do not invent a part label.
- Do not print redundant answer-type words or descriptors such as “Polynomial,” “Value,” “Result,” “Solution,” “Equation,” or “Factored form” in the answer area. Put the task and required answer form in the question prompt.
- When several answers must be distinguished, label the requested outputs as parts in the prompt and use only those matching part labels in the response areas. Add no explanatory wording merely to fill a response area.
- Retain only structures essential to answering the question, such as a required blank graph grid with its axis labels or a table students must complete. These do not justify extra answer-type captions.
- Use the same minimal question/part labels in the matched instructor key, alongside the actual answers and points. This is a standing rule for future generation; do not regenerate existing tests solely to apply it.

## Final-answer directions and grading (October 26, 2026)

This policy applies to every test, exam, retake, diagnostic, final, and practice version and overrides any conflicting method or presentation language elsewhere in these specifications.

- Student-facing directions and individual prompts must never ask students to show work, show substitution, show checks, show partial products, explain a calculation method, or display particular intermediate steps. Do not prescribe a solution method or require separate-paper work.
- Ask only for the requested final result, such as an exact value, simplified expression, factorization, solution set, graph, or requested function feature. Use concise directions such as “Write exact final answers in the right column.” Retain the calculator policy.
- Grade the requested answer in the right-hand response area. Do not imply that shown work earns partial credit or that missing work loses credit. Assign points to final-answer outputs, never to intermediate work, checks, or use of a particular method.
- References to methods or checks describe authoring, expected difficulty, internal verification, or instructor-key content only. They must not become student directions, intermediate response rows, or method-based grading criteria. Independently solve and verify every item before delivery.


**Owner:** Jeremy Kastine  
**Updated:** October 23, 2026  
**Status:** Standing requirements for all future statistics tests, exams, retakes, diagnostics, finals, and practice versions unless the instructor explicitly requests a different format.

## Controlling requirements

Use the format approved in `Statistics_Test_1_20_Versions.pdf` on October 23, 2026. These requirements supersede older separate-booklet/answer-sheet layouts, two-page answer keys, timestamp identifiers, and eight-question multipart defaults. The instructor's latest explicit directions take precedence.

Teaching (`jeremykastine/teaching`, `main`) is the active repository. Use `stats/`; do not create or update a separate Statistics repository. Keep instructor assessment PDFs separate from the public student website.

## Content and selection

- Default to 10 numbered multiple-choice questions, each worth 10 points, for 100 points. Each question has four choices labeled A–D and exactly one defensible answer. No required multipart justifications or free-response calculations by default.
- Emphasize conceptual understanding, interpretation, and application. Include only short, manageable calculations; avoid definition-only recall and tedious computation.
- Unit tests cover Chapters 1–2, 3–4, 5–6, and 7–8, respectively, using OpenStax *Introductory Statistics 2e*. Chapter 9 is not tested.
- For a unit test, independently draw one question from each of its ten current topic pools, then shuffle the ten selected questions and their answer choices. Preserve the correct answer after shuffling. The bank and machine-readable pool blueprint are authoritative for current coverage.
- For a cumulative final or diagnostic, retain this presentation and scoring format but use coverage appropriate to the requested assessment. Do not simply use the Unit 1 pools for every test or revive the old eight-question multipart design.
- Use the requested batch size; 20 is not a mandatory batch size. Random versions may share questions. Keep an internal record of question IDs, printed order, choices, correct letters, version numbers, and random seeds where applicable.
- When only reformatting an existing batch, preserve its exact questions, values, choice order, question order, and version identifiers.
- Avoid dependence on a particular quartile/percentile algorithm, interpolation convention, or tie rule. Supply necessary quartiles, fences, or cutoffs, or choose questions whose correct answer is unchanged under reasonable conventions.
- Test 1 excludes Chebyshev-bound questions and questions about adding a constant to or scaling every observation, including effects on mean, median, mode, shape, range, IQR, variance, or standard deviation. Retain empirical-rule problems, comparisons of distributions, and questions about individual outliers or adding/removing individual observations. This content exclusion is specific to Test 1; the formatting requirements apply to all statistics assessments.

## Calculator directions and version numbers

Print this instruction verbatim on student tests:

**Students may use a basic, non-scientific calculator only.**

Keep calculations feasible with a basic four-function calculator. Supply advanced intermediate values when needed; do not require scientific, graphing, CAS, or statistical-software functions.

For each new version independently choose a random five-digit integer from 10000 through 99999. Do not use timestamps, sequential labels, lettered versions, or batch suffixes. Duplicate identifiers are acceptable; no uniqueness registry is required. Use the same number on both student pages and the corresponding key, and in a filename when practical. For a combined batch PDF, use a descriptive batch filename.

## Student test: one sheet, front and back

- Use US Letter portrait with print-safe margins, approximately 0.5 inch on each side. Default to exactly two student pages: questions 1–5 on page 1 and 6–10 on page 2.
- Put each complete question, its supplied graph/table, and all four choices together on one page. Use readable body type, approximately 10–11 points. Do not shrink text or figures excessively to force a fit.
- Combine questions and response spaces on the same page; there is no separate answer sheet or separate exam booklet.
- Use a wide question column and a narrow right-hand answer column. The approved width for the answer column is approximately 0.75 inch; only one letter is entered. Label it **Answer**. The question column uses the remaining width.
- Align each answer cell vertically with its question. Use solid horizontal rules between questions and a vertical divider between question and answer columns. Do not add internal answer baselines or unnecessary writing space.
- Place **10 points** at the lower right of each answer cell, once per question. Do not repeat points in the question heading.
- Size rows to their actual content rather than stretching them to fill the page. Natural whitespace at the bottom is acceptable.
- Include the course/assessment title, student-name line, five-digit version number, and **Page 1 of 2** or **Page 2 of 2**. Do not add a course-section field. Include a term only when requested.
- Use these response directions: **Choose one answer per question. Write A, B, C, or D in the right column.** Include the exact calculator sentence above.
- Supplied figures belong in the question column and must be readable in grayscale with legible labels and scales.
- Student answer cells must be genuinely empty: no hidden, white, transparent, or extractable correct answers.

## Instructor key: one page, two columns

- Produce exactly one answer-key page per two-page test. Do not repeat the questions, choices, or graphs.
- Use a two-column table: the left column is labeled **Student page 1** and contains answers 1–5; the right is labeled **Student page 2** and contains answers 6–10.
- Show each question number and its correct letter clearly. Retain the point label at the bottom right of each cell.
- Match each column's question-row heights, horizontal separator positions, and vertical starting position to its corresponding student page. The two columns may have different row heights; do not force their rows to align with each other if the student pages differ.
- Include the assessment title, **ANSWER KEY**, and the matching five-digit version number. No student-name line is needed on the key.
- Build student pages and the key from shared row geometry so the vertical alignment is exact. Keep explanations and worked solutions in internal records unless separately requested.

## Combined PDF and duplex printing

For each version, use this exact four-page sequence:

1. Student test, page 1: questions 1–5.
2. Student test, page 2: questions 6–10.
3. One-page, two-column instructor answer key.
4. Completely blank page for the back of the key.

Repeat that sequence for every version in a requested combined batch. The blank page must have no header, footer, page number, or notice. Include it after the final version as well. Every test and key starts on an odd-numbered PDF page, on a fresh front side.

Print duplex with **long-edge flipping**, at actual size. Each version uses two physical sheets. A batch of 20 versions therefore has 80 PDF pages, including 20 blank pages, and prints on 40 sheets.

Deliver one combined PDF when a batch is requested, unless the instructor requests separate files. Do not add unrequested cover pages, compliance reports, mappings, or rationale pages. If an explicitly requested longer assessment cannot fit this structure legibly, adapt the page count while preserving page-matched key columns and duplex-safe section starts.

## Public bank and generator

Each unit has two student HTML options: the complete bank with answers and explanations immediately after each question, and a practice generator selecting one question from each of ten pools. Keep approximately ten questions per pool and 100 per unit. When editing questions, update the source, JSON, complete bank, and embedded generator data consistently. Do not publish instructor assessment PDFs or their answer keys on the student site.

## Required checks before delivery

- Confirm requested version count, ten questions per test, one selection per unit pool, four choices per question, and 100 total points.
- Independently check answer correctness, calculation accuracy, and shuffled answer-letter mapping. Check exactly one defensible correct option.
- Confirm unchanged content and identifiers when reformatting existing versions.
- Verify two student pages, one key page, and one genuinely blank page per version; every next test starts on a front side.
- Compare key-column row boundaries against the corresponding student answer cells; verify every key letter and version label.
- Render and visually inspect the PDF for clipping, overlapping text, unreadable figures, poor wrapping, and unintended page breaks. Confirm student response cells contain no answers.
- Validate bank/generator consistency and relevant repository checks when source questions change.

## Implementation references

- Current banks and pool blueprint: `stats/question-banks/`, especially `source/test-blueprint.json`.
- Approved PDF exporter: `stats/scripts/export_test_packets.py`. This currently selects Unit 1 questions; generalize its bank selection when exporting another unit, while preserving this layout.
- Reformatting an existing batch: use the saved internal packet record to preserve all content and identifiers.

The older October 4 diagnostic/final specification is superseded wherever it conflicts with these standing requirements. It is not the default generation plan.
