# Statistics class slides

Open `index.html` for section links to the Chapter 1 PDF slides for OpenStax *Introductory Statistics 2e*.

The six PDFs contain 106 discussion slides. Pages use US Letter portrait orientation with the lower half clear for pen annotations. Each page presents one definition, concept, or problem with a question and blank room for pen annotations. Solutions are intentionally omitted.

## Editing and rebuilding

Edit `slides/source/chapter-01.json`, then run:

```bash
python -m pip install -r requirements.txt
python scripts/build_slides.py
```

The builder requires DejaVu Sans fonts in `/usr/share/fonts/truetype/dejavu` (Debian/Ubuntu package `fonts-dejavu-core`). If using another platform, change `FONT_DIR` in the script to the local DejaVu font folder. It regenerates both the PDFs and `index.html`.

See `docs/slide-specifications.md` for the instructional requirements. Sections 1.5 and 1.6 use original alternative lab activities aligned with the textbook objectives. Synthetic data are marked on the slides.

## Sources and reuse

Barbara Illowsky and Susan Dean, *Introductory Statistics 2e*, OpenStax, Rice University, 2023. [Access for free](https://openstax.org/books/introductory-statistics-2e/pages/1-introduction). Each index entry links to the corresponding source section.

The slides and their source content are shared under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The definitions are concise paraphrases and the discussion prompts, scenarios, and datasets are original classroom adaptations. These are not official OpenStax slides.
