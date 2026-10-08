# Independent practice during course-specific lessons

The lecture-note index links each TSM 099-only lesson to a TSM 098 practice
packet and separate answer key. Each packet has three core pages and one
extension page. The current lesson labels, not the older 38-topic plan,
control the course split.

`independent-practice.json` records the review topics, links, counts, and
planning estimates. The problems and exact answers are generated together
from `../scripts/build_independent_practice.py` using fixed seeds. Fraction
and linear-equation calculations use exact rational arithmetic. Polynomial
products and system solutions are checked before PDFs are written.

To rebuild from the repository root:

```bash
python tsm/scripts/build_independent_practice.py
```

The builder requires reportlab, matplotlib, pypdf, and DejaVu Sans fonts at
`/usr/share/fonts/truetype/dejavu`. It embeds mathematical notation as vector
PDF content and checks page counts and layout bounds. Render and visually
inspect all final pages after rebuilding, then check the index and schedule
links before publishing. Keep answer keys separate from student practice.
