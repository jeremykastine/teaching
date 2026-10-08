# Statistics class slides

Open `index.html` for the 36 section PDFs aligned to OpenStax **Introductory Statistics 2e**. The course contains 854 portrait discussion pages.

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
