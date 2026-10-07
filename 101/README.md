# MATH 101 course materials

Open `index.html` for the 40 section PDFs aligned to OpenStax **College Algebra 2e**. The course contains 844 portrait discussion pages.

Selected sections through Chapter 7 follow `course-schedule.md`; application options 2.3, 4.2, 4.3, 6.7, and 6.8 are labeled optional. Complex-number work in 2.4 is limited to what supports quadratic and polynomial solutions.

Each page contains one definition, concept, or problem with a focused question. All prompt content stays in the upper half of US Letter portrait pages; the lower half is clear for pen annotations. The instructor provides explanations and worked solutions.

## Editing and rebuilding

Edit the appropriate `slides/source/chapter-NN.json`. From this course folder, run:

```bash
python -m pip install -r requirements.txt
python scripts/build_slides.py
```

To rebuild later chapters without changing the approved Chapter 1 PDFs:

```bash
python scripts/build_slides.py --chapters 2 3 4 5 6 7
```

The shared renderer is `../scripts/slide_builder.py`. It requires DejaVu Sans fonts in `/usr/share/fonts/truetype/dejavu` (Debian/Ubuntu package `fonts-dejavu-core`). For another platform, change `FONT_DIR` in the shared renderer. Formulas and charts remain vector graphics in the PDFs.

`slides/coverage.json` records the planned sections; builds reject missing or unexpected sections. `docs/slide-specifications.md` records the presentation preferences. Chapter coverage documents under `docs/` map textbook objectives and prerequisite connections, including the small amount of extra emphasis given to ideas needed later. Those instructor notes are not printed on the slides.

## Sources and reuse

Jay Abramson, *College Algebra 2e*, OpenStax, Rice University. [Access for free](https://openstax.org/books/college-algebra-2e/pages/1-introduction-to-prerequisites). Each index entry links to its corresponding source section.

Slides and their source content are shared under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Definitions are concise paraphrases; examples, questions, scenarios, and datasets are original classroom adaptations. Synthetic datasets are identified on new slides. These are not official OpenStax slides.
