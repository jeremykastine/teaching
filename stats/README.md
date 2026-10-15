# Statistics class slides

Open `../index.html` to choose the schedule, class slides, homework, test banks and answer keys, or Excel competency checks under Statistics. Open `class-slides.html` for the 36 section PDFs aligned to OpenStax **Introductory Statistics 2e**. The course contains 854 portrait discussion pages.

Selected sections cover Chapters 1–8. Chapter 9 has one conceptual overview deck (9.0), rather than the full chapter’s computational procedures. Chapter 1 lab resources 1.5 and 1.6 are included in the review.

Each page contains one definition, concept, or problem with a focused question. All prompt content stays in the upper half of US Letter portrait pages; the lower half is clear for pen annotations. The instructor provides explanations and worked solutions.

The [October 2026 textbook coverage audit](docs/textbook-coverage-audit.md) maps section terminology, chapter glossary entries and major textbook problem types to specific revised PDF pages.

## Editing and rebuilding

Edit the appropriate `slides/source/chapter-NN.json`. From this course folder, run:

```bash
python -m pip install -r requirements.txt
python scripts/build_slides.py
```

To rebuild a selected set of chapters:

```bash
python scripts/build_slides.py --chapters 2 3 4 5 6 7 8 9
```

The shared renderer is `../scripts/slide_builder.py`. It requires DejaVu Sans fonts in `/usr/share/fonts/truetype/dejavu` (Debian/Ubuntu package `fonts-dejavu-core`). For another platform, change `FONT_DIR` in the shared renderer. Formulas and charts remain vector graphics in the PDFs.

`slides/coverage.json` records the planned sections; builds reject missing or unexpected sections. `docs/slide-specifications.md` records the presentation preferences. Chapter coverage documents under `docs/` map textbook objectives and prerequisite connections, including the small amount of extra emphasis given to ideas needed later. Those instructor notes are not printed on the slides.

## Sources and reuse

Barbara Illowsky and Susan Dean, *Introductory Statistics 2e*, OpenStax, Rice University. [Access for free](https://openstax.org/books/introductory-statistics-2e/pages/1-introduction). Each index entry links to its corresponding source section.

Slides and their source content are shared under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Definitions are concise paraphrases; examples, questions, scenarios, and datasets are original classroom adaptations. Synthetic datasets are identified on new slides. These are not official OpenStax slides.

## Homework

Compact PDF homework assignments are linked from `homework.html`. See [the homework design and coverage map](homework/README.md) for priorities, topic groupings, editable sources, and rebuild instructions. Students work on separate paper and upload one best representative page in Blackboard.

## Unit tests and public question banks

Four units pair Chapters 1-2, 3-4, 5-6, and 7-8. Chapter 9 is assignment or participation material, not tested. Each [public unit bank](question-banks/index.html) contains 100 multiple-choice questions, with student-visible answers, explanations, and source-slide references. Each unit has exactly two student HTML options: a complete bank with answers and explanations visible after each question, and a 10-question practice-test generator. The generator draws one question from each of ten topic pools (currently ten questions per pool), shuffles the questions and choices, and provides a score and explanations when students check their answers. Version links reproduce the same questions and choice order. Structured JSON files support building and validating the same questions.

Questions must not depend on a particular sample-quartile or sample-percentile convention, including whether an odd sample's median is included in either half, interpolation, and tie/rank choices. Supply any needed quartiles, percentile cutoffs, or fences explicitly, or choose data and answer options whose keyed choice is unchanged across reasonable methods. Use approximate language for sample percentile positions and middle-half interpretations; do not require exact observation counts at quartile boundaries or fence-equality minutiae. Continuous-model percentiles may still be assessed from their model probabilities. The October 15, 2026 audit is recorded in `question-banks/source/convention-audit.json`.

Rebuild from the Teaching root with `python stats/scripts/build_question_banks.py`. Editable question sources are in `question-banks/source/`. The build publishes HTML banks and generators, never bank or assessment PDFs. Instructor-requested printable tests are produced separately and saved outside the published Teaching repository. The existing PDF renderer requires an explicit output destination outside this repository. Keep future print tests aligned to the same ten pools in `question-banks/source/test-blueprint.json`; do not add student PDF links or AI generation prompts. Shared course navigation preserves direct bank and competency-check links when rebuilding slides or homework. The browser generator is `question-banks/test-generator.js`. Run `node stats/tests/question-bank-generator.cjs` to check pool coverage, shuffling, correct-answer remapping, and saved-version reproducibility.

## Excel competency checks

The [eight competency checks](excel-competency-checks.html) have detailed HTML preparation directions, practice examples, a roughly five-minute face-to-face demonstration, and alternative variations. They cover data preparation, frequency tables and charts, target means and medians, sample standard deviation, contingency tables and probabilities, random-trial simulation and the law of large numbers, normal probabilities, and sample-size/confidence-interval comparisons. Google Sheets differences appear in parentheses. Rebuild the index and directions with `python stats/scripts/build_competency_checks.py`; styling is in `excel-checks.css`.

Each skill page now includes a JavaScript assignment generator: regenerate a complete task, deliberately choose a practice variation, copy source data or the assignment, and reopen the exact task from its version link. Live check view hides learning examples and practice self-checks while the instructor observes the spreadsheet demonstration. It is a display option, not an exam-security mechanism. No workbook is uploaded or automatically graded.

The pure generators are in `excel-checks/generators.js`; browser controls are in `excel-checks/check-page.js`. The HTML builder preserves all controls and learning directions. Check 3 includes mean/median, mean/sample-standard-deviation, minimum/maximum/sample-standard-deviation, median/extremes, and mean/extremes constructions with 5–10 observations. Targets and feasible follow-ups come from witness datasets, which appear only in the expandable practice self-check. Mean and standard-deviation targets allow 0.05 absolute error; other targets are exact. Other checks vary data size, labels, requested summaries or conditionals, model inputs, and follow-up changes. Datasets are synthetic.

Assignment links use generator version `v=1`, an eight-digit hexadecimal seed, and the requested variation. Preserve the v1 generation rules and random-number call order when making compatible changes; if a future version changes those rules, retain v1 support for existing links. Invalid or unsupported links fail visibly rather than silently changing a saved task. Simulation trial outcomes in Excel remain random even when the assignment link is fixed.

Run `node stats/tests/competency-generators.cjs` from the Teaching root to validate 34,000 seeded assignments, all variation families, copied-data structures, achievable construction targets, and feasible follow-up changes. No npm packages are needed for the generator tests. Browser QA should also cover all eight pages, every variation, regenerate/reload, copying with a manual fallback, live check view, and a narrow mobile viewport.
