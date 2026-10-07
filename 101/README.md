# MATH 101 course materials

College Algebra lecture slides aligned to **OpenStax College Algebra 2e**.

Open `index.html` to find the six section PDFs for Chapter 1, Prerequisites. The PDFs contain 130 portrait pages. Each page has one definition, concept, or problem with a discussion question, with the lower half clear for pen annotations. The instructor supplies explanations and worked solutions.

The existing `course-schedule.md` and `final-exam-specifications.md` remain the course schedule and assessment specifications. Lecture-slide preferences are in `docs/slide-specifications.md`.

## Editing and rebuilding

Edit `slides/source/chapter-01.json`, then run:

```bash
python -m pip install -r requirements.txt
python scripts/build_slides.py
```

The builder uses ReportLab for page layout, Matplotlib for mathematical typography, and PyMuPDF to place vector formulas into each PDF. It requires DejaVu Sans fonts in `/usr/share/fonts/truetype/dejavu` (Debian/Ubuntu package `fonts-dejavu-core`). On other platforms, change `FONT_DIR` in the script to the local DejaVu font folder.

## Sources and reuse

Jay Abramson, *College Algebra 2e*, OpenStax, Rice University, 2021. [Access for free](https://openstax.org/books/college-algebra-2e/pages/1-introduction-to-prerequisites). The index links to each corresponding section.

The slides and their content are shared under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Definitions are concise paraphrases and problems are original classroom adaptations. These are not official OpenStax slides.
