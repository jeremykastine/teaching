# Statistics lecture-note sources

The manifest covers the course topics, with Sections 5.1–5.2 combined in one lesson. Textbook snapshots are the page bodies of OpenStax *Introductory Statistics 2e* (Barbara Illowsky and Susan Dean, Rice University), retrieved October 27, 2026. Source URLs are recorded through the manifest slugs at https://openstax.org/books/introductory-statistics-2e/pages/ . The material is licensed CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/ . These adaptations use the same license.

`answers.py` supplies solutions for textbook Try It and collaborative exercises, as well as corrected or rephrased prompts. `special.py` supplies the guided labs and the conceptual-only hypothesis-testing overview. The approved 3.4 and 3.5 documents remain hand-authored; the builder only updates their navigation. The other sections preserve textbook exposition, examples, practice order, and native MathML. Historical data remain classroom exercises rather than current factual claims.

Section 4.2 uses the audited, hand-maintained body in `section-4-2.html`. Edit that file to update its exposition, prompts, tables, or solutions; `answers.py` and the textbook snapshot are not the build source for this section. Its native MathML uses explicit parentheses rather than unsupported `mfenced` elements. The November 2, 2026 review checked all twelve examples and Try Its, corrected the product-column label to xP(x), and formatted calculations and headings consistently. The original licensed textbook snapshot is retained unchanged.

Sections 5.1–5.2 use the hand-authored [wait-time lesson](../lessons/section-5-1-5-2-continuous-and-uniform-distributions.html). The manifest preserves the two separate Essentials reviews.

Run `python scripts/build_lecture_notes.py` from the repository root. Dependencies are beautifulsoup4 and scipy. Figures are shared in `notes-assets/` and mapped to source URLs in its manifest. `scripts/lecture-notes-coverage.json` records page and solution counts. All answers are static HTML; the shared TSM controls reveal them on double-click, double-tap, Enter, or Space.

