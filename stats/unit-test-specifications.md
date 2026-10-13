# Statistics unit tests and public question banks

Instructor: Jeremy Kastine. Course: MSC 201 Statistics. Textbook: OpenStax *Introductory Statistics 2e*.

These specifications record the instructor's October 12, 2026 decisions. They apply to the four unit tests and supersede any earlier plan for a separate test per chapter. Chapter 9 is not tested; its conceptual overview remains assignment or participation material. This document does not establish or change a cumulative final-exam policy.

## Unit boundaries

| Unit | Chapters | Scheduled sections | Focus |
|---|---|---|---|
| 1 | 1-2 | 1.1-1.4 and 2.1-2.7 | Collecting and describing data |
| 2 | 3-4 | 3.1-3.5 and 4.1-4.6 | Probability and discrete models |
| 3 | 5-6 | 5.1-5.3 and 6.1-6.2 | Continuous probability models |
| 4 | 7-8 | 7.1-7.3 and 8.1-8.3 | Sampling distributions and estimation |

Chapter 1 sections 1.5-1.6 are supporting labs, not additional tested material. Under the current schedule the units finish in Weeks 3, 5, 7, and 9; these are coverage milestones, not newly imposed test dates.

## Test form

- Exactly 10 questions, each worth 10 points; 100 points total.
- All questions are single-answer multiple choice with four options, A-D. Exactly one option must be correct.
- Select from the matching public bank of 100 questions. Each bank contains ten named skill groups of ten questions. Select exactly one question from each skill group, then mix the order of the ten selected questions.
- At least seven questions must carry a non-calculation reasoning tag. At most three may carry `calculate`.
- Include at least two `evaluate` questions, at least two `interpret` questions, and at least one question tagged `compare` or `predict`. A `compare` item must require statistical reasoning, even when a very small arithmetic check helps.
- A four-function calculator is allowed. Supply every needed critical value, normal probability, nontrivial square root, or exponential/logarithm approximation. Do not require scientific-calculator functions, distribution software, spreadsheet calculations, factorials, or summing a lengthy dataset.
- Prefer interpretation, prediction, data comparisons, assumptions, and conclusions. Do not introduce stand-alone vocabulary-recall questions. Terms may appear within an applied problem.
- A small calculation should normally involve one or two straightforward operations; occasional three-operation arithmetic is acceptable only when the central task stays conceptual. Do not require multi-stage distribution or interval calculations. Supplying a standard error or tail probability can preserve the concept without asking students to derive it.
- Plan for a short test, approximately 20-30 minutes. This is a design estimate; adjust after observing actual student completion times.

## Ten-question coverage blueprint

Each row supplies one question. Selecting one per group gives a varied test rather than ten variants of one familiar task.

| Slot | Unit 1 | Unit 2 | Unit 3 | Unit 4 |
|---|---|---|---|---|
| 1 | Sampling scope and variables | Events, complements, and probability claims | Continuous densities, areas, and cumulative probabilities | Sampling distributions and their centers |
| 2 | Sampling design and bias | Independence, dependence, and conditions | Uniform probabilities and cutoffs | Standard error and sample-size effects |
| 3 | Study design and evidence | Probability rules and shortcuts | Uniform changes, conditioning, and assumptions | CLT assumptions, shape, and sampling quality |
| 4 | Frequencies and meaningful comparisons | Tables, trees, and Venn reasoning | Exponential shape, rates, and tails | Sums versus means |
| 5 | Reading displays | Discrete distributions and support | Exponential memorylessness and count connections | Choosing models, areas, and approximations |
| 6 | Median, quartiles, and box plots | Expected value, costs, and spread | Normal location, spread, and symmetry | Confidence interval meaning and reading |
| 7 | Mean, weights, and changes | Binomial reasoning | Standardized comparisons and units | Interval width, conditions, and planning |
| 8 | Shape and outlier effects | Geometric reasoning | Normal areas and supplied probabilities | Student t and estimated uncertainty |
| 9 | Spread and transformations | Hypergeometric and sampling design | Normal percentiles and critical cutoffs | Proportion estimates, intervals, and interpretation |
| 10 | Comparing distributions and summaries | Poisson counts and model comparisons | Model choice and integrated comparisons | Proportion conditions, precision, and adjustment |

Unit 1 has four groups devoted to Chapter 1 and six to Chapter 2. Unit 2 has four Chapter 3 groups and six Chapter 4 groups, including probability-distribution and expected-value foundations. Units 3 and 4 have five groups centered on each chapter, with occasional prerequisite connections. Topic importance and reasoning variety, rather than equal numbers per textbook section, determine the allocation.

## Cosmetic variations only

Allowed changes are neutral context names, equivalent nonstatistical wording, option order, question order, and small numerical variations **only after all options and the key are independently rechecked**. These variations do not authorize a new problem type or harder calculations.

Preserve the tested concept, assumptions, counting convention, inequality direction, model support, uniqueness of the answer, and approximate difficulty. The original bank question remains the reference problem. Keep its ID on the instructor key along with an exact change log. Test questions may use a simple 1-10 numbering.

Numbers can determine an answer, so changing them is not automatically harmless. For example:

- A data change must preserve the intended mean/median ordering, outlier effect, ties, or distribution shape.
- Changing a sample size must not inadvertently change a success-failure check, sampling fraction, degrees of freedom, or approximation decision.
- Uniform endpoints, count-model support bounds, conditioning denominators, and supplied normal/exponential areas must remain internally consistent.
- A mean/SD unit conversion must also convert any thresholds and interval endpoints.
- Changing a confidence level or model assumption is a substantive change, not a cosmetic one; do not do it when making a test form.
- Any figure or table must be updated to match a permitted numerical change. If the variant cannot be checked confidently, keep the bank's original numbers.

After option shuffling, recompute answer letters from the option texts. Do not rely on remembered letters or use answer-location-dependent choices. Aim for an unobtrusive mix of A-D answers without weakening coverage. Across different forms, avoid repeating IDs where a comparable alternative in the same group is available.

## Slide alignment and intentional reduction of calculation load

All 400 items are original adaptations of concepts found in the existing Chapter 1-8 slide source files. Each item records the section PDF page, exact slide title, reasoning tag, and skill group. This page number refers to the current section PDF, not a chapter-wide page count. The builder records the SHA-256 of each slide source to make the alignment snapshot reviewable.

The slides are the coverage and emphasis guide. They include computational examples that are intentionally transformed here into interpretation, model-selection, comparison, supplied-intermediate-result, or small-arithmetic items. The banks do not reproduce all slide computations or demand every glossary term. In particular, long variance sums, binomial/hypergeometric formulas, exponential inverses, full normal-table searches, and complete raw-data confidence-interval construction are not test tasks. Binomial continuity correction remains a conceptual event-boundary task because it is explicitly taught in section 7.3. Chapter 9 and hypothesis-test decisions/calculations are excluded.

Course conventions retained from the slides:

- `N(mean, SD)` uses the textbook's mean/standard-deviation convention.
- Geometric X counts trials through and including first success. A failures-before-success variable is X-1.
- Exact and at-most/fewer-than count events remain distinct; continuous strict/inclusive endpoints have equal probability.
- Median calculations use ordered data. No item depends on an unstated quartile interpolation convention. The 1.5 IQR flag applies strictly beyond a fence.
- The empirical rule requires an appropriate bell-shaped normal setting; Chebyshev supplies a general finite-variance bound.
- Independent-sampling SE and sum-SD formulas require their stated assumptions. The at-most-10% sample-fraction check is a common approximation guideline, not a guarantee of independence or representativeness.
- The binomial normal check uses np>5 and n(1-p)>5 as stated in the slides. The ordinary proportion interval check uses more than five observed successes and more than five observed failures. Plus-four recommendations are confidence at least 90% and n at least 10.
- Confidence describes repeated-procedure coverage of a fixed population parameter; it does not describe the percentage of individuals inside a mean interval.

## Public study resources and generation prompt

Each unit has an accessible HTML bank with revealable answers, a printable PDF with an answer/explanation section, and a structured JSON download. All contain the same 100 questions. Students are allowed to see all questions, correct answers, explanations, and source references. No answer file in this public repository is treated as confidential.

Student prompt: "Quiz me from this statistics unit bank, one question at a time. Keep all four choices visible, but withhold the correct answer and explanation until I respond. Ask me to explain my reasoning. Then give feedback, cite the question ID, and revisit missed concepts later. Use a mix of skill groups. Do not invent harder calculations."

The ready-to-copy instructor prompt is [question-banks/create-unit-test-prompt.txt](question-banks/create-unit-test-prompt.txt). Use the matching JSON bank alongside it. The selected IDs and the key are required for traceability.

## Validation and maintenance

Rebuild with `python stats/scripts/build_question_banks.py` from the Teaching root. The authoring files are `stats/question-banks/source/unit-N.txt`; each line contains slide reference, reasoning tag, stem, correct option, three distractors, and explanation separated by pipes. The ten `@` headings define the blueprint groups. Generated JSON carries explicit answer indices and balanced, shuffled original option orders.

Before publishing: confirm exactly 100 unique stems per unit, four distinct choices, one keyed answer, complete explanations, valid section/page references, no Chapter 9 items, all required groups, feasible ten-question selection constraints, checked arithmetic, correctly rendered figures, intact PDFs, and working relative links. Run `python stats/scripts/validate_question_banks.py` to independently recompute the approved calculation answers, verify source references against actual section PDFs, and check local links. Inspect rendered pages as well as extracted text. Recheck slide alignment when sources change. The shared slide-index builder preserves question-bank links after future slide or homework rebuilds.

Existing source references: [course schedule](course-schedule.md), [slide coverage](slides/coverage.json), [Chapters 2-4 coverage](docs/ch2-4-coverage.md), [Chapters 5-9 coverage](docs/ch5-9-coverage.md), and [textbook audit](docs/textbook-coverage-audit.md). These are the coverage sources, not restrictions requiring exhaustive testing of every slide detail.
