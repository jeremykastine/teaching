# TSM homework design and topic map

The current 37-topic lecture-note sequence and `planning/colisted-98-99-schedule.md` govern coverage. Eight assignments cover all 27 TSM 098 topics; nine cover all 37 TSM 099 topics. The ten 099-only topics are excluded from 098. Shared topics have course-appropriate difficulty. Topics 35-37 remain included in both courses, as in the current cross-listed schedule; an older online-section instruction to skip word problems does not change this current schedule.

Priorities come from the current lecture-note and test specifications, the instructor's earlier course-level distinctions, and the October 12, 2026 request. TSM 098 emphasizes signed arithmetic, ordinary fractions, polynomial operations (including a trinomial-by-trinomial product), introductory factoring, linear equations, and systems. TSM 099 adds radical simplification, nonmonic factoring/grouping, rational operations, all three quadratic methods, rational-equation restrictions/checks, and slope/line writing. Students work without a calculator before checking.

These are homework sets, not five- or ten-question tests. The newer lecture-note fraction-equation method takes precedence for homework: combine and simplify each side, then move each whole-side denominator to the opposite side; retain all original restrictions. Negative roots distinguish real-only and complex contexts. Numerical agreement at selected inputs is distinguished from proof of an identity.

The topic table of contents stays in its original continuous order without unit headings. A homework section lists exact topics for each course; completion-point lesson pages also link the relevant packet. Existing independent-practice packets remain distinct from homework.

Topic 5 is now **Evaluating Powers and Square Roots**: its power examples precede roots, and Topic 7 applies powers in mixed expressions. TSM 098 Homework 2 and TSM 099 Homework 1 already cover the affected topic ranges, so their problem sets and completion points remain appropriate; their descriptions explicitly identify powers. Topic 2 supplies the brief exponent-notation introduction needed for Homework 1 prime factorizations.

## Single-variable scope

Polynomial multiplication, GCFs and factoring, rational-expression operations, and rational equations use at most one variable per exercise, matching the October 20, 2026 lecture-note and test specifications. Earlier combining-terms, combining-factors, and introductory distribution practice may use multiple variables; graphing and linear systems retain two variables. Keep editorial answers consistent when changing an exercise.

## Format and workload

Match the approved Math 101 Chapter 1 approach: compact US Letter PDFs with no reserved working space or separate answer sheets. Students complete and show all work on separate paper, check and correct it, complete the Blackboard self-evaluation, upload one clear photo of their best representative page, and retain all work. Each set targets roughly 45-50 minutes of problem work plus 10-15 minutes of checking and submission. Times are planning estimates, not deadlines or measured student completion times. No points or test grading structure are imposed.

## Assignment map

| Assignment | Coverage | Emphasis | Problems | Estimated problem work |
|---|---|---|---:|---:|
| TSM 098 Homework 1 | Topics 1-4 | Number structure, signs, and fraction reduction | 17 | 48 min |
| TSM 098 Homework 2 | Topics 5, 7-8 | Powers, square roots, and expression evaluation | 16 | 47 min |
| TSM 098 Homework 3 | Topics 9-12 | Combining terms, distribution, and polynomial products | 17 | 48 min |
| TSM 098 Homework 4 | Topics 13-15 | Common factors and introductory factoring | 17 | 50 min |
| TSM 098 Homework 5 | Topics 19, 21-22 | Numerical fraction operations | 18 | 48 min |
| TSM 098 Homework 6 | Topics 24-26, 28 | Linear equations, parentheses, and fractions | 15 | 48 min |
| TSM 098 Homework 7 | Topics 30-31, 33 | Coordinate graphs and linear systems | 11 | 48 min |
| TSM 098 Homework 8 | Topics 35-37 | Percents and equations in context | 12 | 48 min |
| TSM 099 Homework 1 | Topics 1-8 | Number structure, powers, radicals, and evaluation | 17 | 50 min |
| TSM 099 Homework 2 | Topics 9-12 | Polynomial structure and operations | 16 | 48 min |
| TSM 099 Homework 3 | Topics 13-17 | Common factors and advanced factoring | 14 | 50 min |
| TSM 099 Homework 4 | Topics 18-20 | Simplifying, multiplying, and dividing fractions | 12 | 48 min |
| TSM 099 Homework 5 | Topics 21-23 | Common denominators and sums of fractions | 11 | 48 min |
| TSM 099 Homework 6 | Topics 24-28 | Linear and quadratic equations | 14 | 48 min |
| TSM 099 Homework 7 | Topics 29 | Rational equations and excluded values | 10 | 48 min |
| TSM 099 Homework 8 | Topics 30-34 | Lines, slopes, graphs, and systems | 11 | 49 min |
| TSM 099 Homework 9 | Topics 35-37 | Percents, models, and contextual systems | 12 | 48 min |

## Editing and rebuilding

Edit `source/assignments.json` in this folder. Each problem stores its prompt, optional typeset mathematics/table/graph, estimated minutes, and a concise editorial answer. Answers are used for content review and are never printed in student PDFs. The repository is public; source answers are not a private grading key.

From the Teaching repository root, run:

```bash
python scripts/build_homework.py
```

Use `--course 101`, `--course stats`, or `--course tsm` to rebuild a single course. Dependencies match the PDF/slide workflow: Python, ReportLab, Matplotlib, NumPy, pypdf, and DejaVu Sans fonts. The approved Chapter 1 PDF is outside the new builder and is not overwritten. The builder refreshes chapter homework links through the shared slide-index builder, and creates the TSM homework index and completion-point links. Later slide rebuilds preserve homework links by detecting the PDFs.

After edits, independently check the mathematics and original domain restrictions, confirm the topic map and workload, render and inspect the PDFs, and validate relative links before publishing. Avoid expanding the homework into an exhaustive checklist of every slide term; select representative skills within the one-hour budget.
