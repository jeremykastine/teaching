# Essentials reviews

The three course lecture-note indexes define coverage: 37 TSM topics shared by
TSM 098/099 with the existing course assignment labels, 41 College Algebra
sections including 3.1B and optional applications, and 36 Statistics sections.
Each topic has a separate static HTML page in its course's `essentials/` folder.
Course hubs are `tsm/essentials.html`, `101/essentials.html`, and
`stats/essentials.html`.

Edit original questions, answer keys, and worked solutions in
`essentials_content.py`. Every topic has five short-answer recall questions and
two worked examples, except the two quadratic-equation topics, which have three
examples. Answers use native expandable HTML; formulas are compiled to native
MathML so students need neither JavaScript nor a remote equation renderer.
The four graphical Algebra examples use inline accessible SVG. Algebra 3.2 and
3.3 retain their current graph-only scope; 2.4 retains introductory imaginary
numbers without complex arithmetic. TSM algebra examples use a single variable
through rational expressions. TSM 099 assessment material in Topic 7 is labeled.

Rebuild with:

```sh
python -m pip install -r scripts/essentials-requirements.txt
python scripts/build_essentials.py
python scripts/verify_essentials.py
```

The builder checks coverage against the live lecture indexes, renders the pages,
and adds links from the Teaching index, each lecture index, and each lesson.
It preserves existing lesson content and can be run repeatedly without adding
duplicate links. Run it again after rebuilding any lecture-note pages. The
coverage manifest records each generated path and its question/example counts.
Use the standard browser Print command; open whichever answers you wish to
include before printing.
