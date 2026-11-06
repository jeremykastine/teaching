# Statistics Test Specifications

## Controlling presentation update (October 30, 2026)

Apply [Shared test presentation](../../docs/test-presentation.md) to every version. This update supersedes all conflicting presentation rules below: upper-left course/test title; upper-right random five-digit version; Name and Date below; basic non-scientific calculator only; no notes or other technology; final answers in the right column (Statistics: circle choices in the right column); one student page preferred; continuation-only footers; large centered version-only key header; compact left-aligned page-matching key columns; and exact vertical alignment of every answer, including the specific correct multiple-choice option. Generate 20 fresh versions per requested test in an unlinked, duplex-safe instructor PDF batch. Preserve the mathematical blueprints and point totals below.

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
**Updated:** November 5, 2026\
**Status:** Standing requirements for all future statistics tests, exams, retakes, diagnostics, finals, and practice versions unless the instructor explicitly requests a different format.

## Controlling requirements

Use the shared October 30, 2026 presentation update above. These requirements supersede older separate-booklet/answer-sheet layouts, two-page answer keys, timestamp identifiers, and eight-question multipart defaults. The instructor's latest explicit directions take precedence.

Teaching (`jeremykastine/teaching`, `main`) is the active repository. Use `stats/`; do not create or update a separate Statistics repository. Keep instructor assessment PDFs separate from the public student website.

## Content and selection

- Default to 10 numbered multiple-choice questions, each worth 10 points, for 100 points. Each question has four choices labeled A–D and exactly one defensible answer. No required multipart justifications or free-response calculations by default.
- Emphasize conceptual understanding, interpretation, and application. Include only short, manageable calculations; avoid definition-only recall and tedious computation.
- Unit tests cover Chapters 1–2, 3–4, 5–6, and 7–8, respectively, using OpenStax *Introductory Statistics 2e*. Chapter 9 is not tested.
- Exclude the Poisson distribution (Section 4.6) from all assessments. Assess Chapter 4 and the binomial normal approximation conceptually. Ask students to interpret discrete distributions and compare binomial, geometric, and hypergeometric assumptions, sampling designs, stopping rules, and what each variable counts. Require no calculation of specific probabilities, means, or other numerical results for these topics.
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

## Student test, instructor key, and duplex printing

Follow [Shared test presentation](../../docs/test-presentation.md). Prefer one student page and use more when needed. Use equal-width question and choice columns; students circle A-D in the right column. The compact key uses only its large centered version number at the top, plus one narrow left-aligned column per student page. Place each correct letter at the exact vertical baseline of that choice on the test. Omit routine footers and use continuation prompts only when another student page follows. Student and key sections each start on a fresh front side; pad every complete packet to an even page count, including the last. Preserve 10 questions and 100 points.

## Public bank and generator

Each unit has two student HTML options: the complete bank with answers and explanations immediately after each question, and a practice generator selecting one question from each of ten pools. Keep approximately ten questions per pool and 100 per unit. When editing questions, update the source, JSON, complete bank, and embedded generator data consistently. Do not publish instructor assessment PDFs or their answer keys on the student site.

## Required checks before delivery

- Confirm requested version count, ten questions per test, one selection per unit pool, four choices per question, and 100 total points.
- Independently check answer correctness, calculation accuracy, and shuffled answer-letter mapping. Check exactly one defensible correct option.
- Confirm unchanged content and identifiers when reformatting existing versions.
- Verify natural student pagination, compact page-matching key columns, required blank padding, and odd-page starts for every test and key.
- Compare key-column row boundaries against the corresponding student answer cells; verify every key letter and version label.
- Render and visually inspect the PDF for clipping, overlapping text, unreadable figures, poor wrapping, and unintended page breaks. Confirm student response cells contain no answers.
- Validate bank/generator consistency and relevant repository checks when source questions change.

## Implementation references

- Current banks and pool blueprint: `stats/question-banks/`, especially `source/test-blueprint.json`.
- Approved PDF exporter: `stats/scripts/export_test_packets.py`. Use `scripts/export_assessment_batches.py` from the repository root for all unit tests, diagnostics, and finals; it implements the October 30 layout.
- Reformatting an existing batch: use the saved internal packet record to preserve all content and identifiers.

The older October 4 diagnostic/final specification is superseded wherever it conflicts with these standing requirements. It is not the default generation plan.
