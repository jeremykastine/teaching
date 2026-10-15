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

Four units pair Chapters 1-2, 3-4, 5-6, and 7-8. Chapter 9 is assignment or participation material, not tested. Each [public unit bank](question-banks/index.html) contains 100 multiple-choice questions, with student-visible answers, explanations, and source-slide references. Students can read HTML or printable PDF versions. Structured JSON files support building and validating the same questions.

Rebuild from the Teaching root with `python stats/scripts/build_question_banks.py`. Editable question sources are in `question-banks/source/`. Keep the student pages focused on questions and answer keys; there are no separate statistics practice tests, generation prompts, or test-form specifications. Shared course navigation preserves direct bank and competency-check links when rebuilding slides or homework.

## Excel competency checks

The [eight competency checks](excel-competency-checks.html) have detailed HTML preparation directions, practice examples, a roughly five-minute face-to-face demonstration, and alternative variations. They cover data preparation, frequency tables and charts, target means and medians, sample standard deviation, contingency tables and probabilities, random-trial simulation and the law of large numbers, normal probabilities, and sample-size/confidence-interval comparisons. Google Sheets differences appear in parentheses. Rebuild the index and directions with `python stats/scripts/build_competency_checks.py`; styling is in `excel-checks.css`.
