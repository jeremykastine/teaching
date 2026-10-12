# Statistics homework design

One assignment per scheduled chapter: Chapters 1-8 and the Chapter 9 conceptual overview. Chapter 1 focuses on sections 1.1-1.4; the supporting labs do not create extra homework. Chapter 9 does not require test-statistic or p-value calculations.

Priorities come from `course-schedule.md`, `docs/slide-specifications.md`, the chapter coverage notes and textbook audit, and the instructor's earlier assessment discussion and October 12, 2026 request. Pair calculations with interpretation: sampling design, variable types, frequency denominators, shape/center/spread, conditional denominators, independence, expected value, model assumptions, tail areas, individual versus mean/sum distributions, standard error, confidence intervals, and hypothesis-test conclusions. Free-response justifications serve the earlier emphasis on conclusions supported by reasoning. These homework sets do not inherit exam question-count or multiple-choice rules.

A four-function calculator is sufficient. Normal probabilities, critical values, exponential/logarithm approximations, and nontrivial square roots are supplied when needed. Excel skills remain a separate assessment category; these PDFs can be completed on paper. Datasets and scenarios are labeled fictional, avoiding the disliked term “synthetic.”

Conventions checked against OpenStax Introductory Statistics 2e: [7.3 CLT and binomial approximation](https://openstax.org/books/introductory-statistics-2e/pages/7-3-using-the-central-limit-theorem) and [8.3 proportion intervals](https://openstax.org/books/introductory-statistics-2e/pages/8-3-a-population-proportion). Use the stated >5 success/failure criteria, continuity correction for the binomial approximation, and sample-proportion standard error for the ordinary interval. Quartiles use the explicitly stated median-of-halves convention. Normality/independence conditions are identified; a large sample does not fix selection bias.

## Format and workload

Match the approved Math 101 Chapter 1 approach: compact US Letter PDFs with no reserved working space or separate answer sheets. Students complete and show all work on separate paper, check and correct it, complete the Blackboard self-evaluation, upload one clear photo of their best representative page, and retain all work. Each set targets roughly 45-50 minutes of problem work plus 10-15 minutes of checking and submission. Times are planning estimates, not deadlines or measured student completion times. No points or test grading structure are imposed.

## Assignment map

| Assignment | Coverage | Emphasis | Problems | Estimated problem work |
|---|---|---|---:|---:|
| Statistics Chapter 1 Homework | Sections 1.1-1.4 | Sampling, data, and study design | 9 | 48 min |
| Statistics Chapter 2 Homework | Sections 2.1-2.7 | Describing distributions | 11 | 48 min |
| Statistics Chapter 3 Homework | Sections 3.1-3.5 | Probability and conditional reasoning | 11 | 48 min |
| Statistics Chapter 4 Homework | Sections 4.1-4.6 | Discrete random variables and expected value | 11 | 49 min |
| Statistics Chapter 5 Homework | Sections 5.1-5.3 | Continuous models, areas, and waiting times | 12 | 50 min |
| Statistics Chapter 6 Homework | Sections 6.1-6.2 | Normal distributions and percentiles | 11 | 48 min |
| Statistics Chapter 7 Homework | Sections 7.1-7.3 | Sampling distributions and the CLT | 11 | 48 min |
| Statistics Chapter 8 Homework | Sections 8.1-8.3 | Confidence intervals and their interpretation | 10 | 48 min |
| Statistics Chapter 9 Homework | Chapter 9 conceptual coverage only | Hypothesis testing: conceptual overview | 10 | 48 min |

## Editing and rebuilding

Edit `source/assignments.json` in this folder. Each problem stores its prompt, optional typeset mathematics/table/graph, estimated minutes, and a concise editorial answer. Answers are used for content review and are never printed in student PDFs. The repository is public; source answers are not a private grading key.

From the Teaching repository root, run:

```bash
python scripts/build_homework.py
```

Use `--course 101`, `--course stats`, or `--course tsm` to rebuild a single course. Dependencies match the PDF/slide workflow: Python, ReportLab, Matplotlib, NumPy, pypdf, and DejaVu Sans fonts. The approved Chapter 1 PDF is outside the new builder and is not overwritten. The builder refreshes chapter homework links through the shared slide-index builder, and creates the TSM homework index and completion-point links. Later slide rebuilds preserve homework links by detecting the PDFs.

After edits, independently check the mathematics and original domain restrictions, confirm the topic map and workload, render and inspect the PDFs, and validate relative links before publishing. Avoid expanding the homework into an exhaustive checklist of every slide term; select representative skills within the one-hour budget.
