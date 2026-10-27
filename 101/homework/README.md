# MATH 101 homework design

These are homework assignments, not ten-question exams. The approved Chapter 1 PDF is retained unchanged. Chapters 2-7 cover the scheduled core sections; optional application sections 2.3, 4.2-4.3, and 6.7-6.8 do not add required homework. Homework 4 combines Sections 4.1 and 5.1 (linear and quadratic functions); Homework 5 covers Sections 5.2-5.7. This assignment grouping was revised October 27, 2026. Stable PDF filenames are retained for existing links.

Priorities come from `course-schedule.md`, `final-exam-specifications.md`, the chapter coverage notes in `docs/`, and the instructor's October 12, 2026 request. Emphasize skills reused later, exact answers, clear grouping, domains, complete solution sets, and checking. Use a basic four-function calculator only if needed. Retain polynomial long division before quadratic-formula zeros, graph-based transformations, holes versus asymptotes, inverse branches, useful logarithm properties, and line/parabola and line/circle systems. Preliminary equation skills get representative practice without displacing the function-centered emphasis.

## Format and workload

Match the approved Math 101 Chapter 1 approach: compact US Letter PDFs with no reserved working space or separate answer sheets. Students complete and show all work on separate paper, check and correct it, complete the Blackboard self-evaluation, upload one clear photo of their best representative page, and retain all work. Each set targets roughly 45-50 minutes of problem work plus 10-15 minutes of checking and submission. Times are planning estimates, not deadlines or measured student completion times. No points or test grading structure are imposed.

## Assignment map

| Assignment | Coverage | Emphasis | Problems | Estimated problem work |
|---|---|---|---:|---:|
| Chapter 1 (existing) | 1.1-1.6 | Essential prerequisites; scientific notation omitted | 20 | 45-50 min |
| MATH 101 Chapter 2 Homework | Sections 2.1-2.2 and 2.4-2.7 | Equations and inequalities | 16 | 48 min |
| MATH 101 Chapter 3 Homework | Sections 3.1-3.7 | Functions, composition, and inverses | 11 | 48 min |
| MATH 101 Homework 4 | Sections 4.1 and 5.1 | Linear and quadratic functions | 9 | 48 min |
| MATH 101 Homework 5 | Sections 5.2-5.7 | Power, polynomial, rational, and radical functions | 10 | 48 min |
| MATH 101 Chapter 6 Homework | Sections 6.1-6.6 | Exponential and logarithmic functions | 15 | 49 min |
| MATH 101 Chapter 7 Homework | Sections 7.1 and 7.3 | Systems of equations and inequalities | 10 | 48 min |

## Editing and rebuilding

Edit `source/assignments.json` in this folder. Each problem stores its prompt, optional typeset mathematics/table/graph, estimated minutes, and a concise editorial answer. Answers are used for content review and are never printed in student PDFs. The repository is public; source answers are not a private grading key.

From the Teaching repository root, run:

```bash
python scripts/build_homework.py
```

Use `--course 101`, `--course stats`, or `--course tsm` to rebuild a single course. Dependencies match the PDF/slide workflow: Python, ReportLab, Matplotlib, NumPy, pypdf, and DejaVu Sans fonts. The approved Chapter 1 PDF is outside the new builder and is not overwritten. The builder refreshes chapter homework links through the shared slide-index builder, and creates the TSM homework index and completion-point links. Later slide rebuilds preserve homework links by detecting the PDFs.

After edits, independently check the mathematics and original domain restrictions, confirm the topic map and workload, render and inspect the PDFs, and validate relative links before publishing. Avoid expanding the homework into an exhaustive checklist of every slide term; select representative skills within the one-hour budget.
