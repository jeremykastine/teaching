# Statistics lecture-note sources

The manifest covers the 36 topics in the course coverage registry. Textbook snapshots are the page bodies of OpenStax *Introductory Statistics 2e* (Barbara Illowsky and Susan Dean, Rice University), retrieved October 27, 2026. Source URLs are recorded through the manifest slugs at https://openstax.org/books/introductory-statistics-2e/pages/ . The material is licensed CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/ . These adaptations use the same license.

`answers.py` supplies solutions for textbook Try It and collaborative exercises, as well as corrected or rephrased prompts. `special.py` supplies the guided labs and the conceptual-only hypothesis-testing overview. The approved 3.4 and 3.5 documents remain hand-authored; the builder only updates their navigation. The other sections preserve textbook exposition, examples, practice order, and native MathML. Historical data remain classroom exercises rather than current factual claims.

Run `python scripts/build_lecture_notes.py` from the repository root. Dependencies are beautifulsoup4 and scipy. Figures are shared in `notes-assets/` and mapped to source URLs in its manifest. `scripts/lecture-notes-coverage.json` records page and solution counts. All answers are static HTML; the shared TSM controls reveal them on double-click, double-tap, Enter, or Space.
