# College Algebra lecture-note sources

The manifest covers all 40 topics in the course coverage registry. Textbook snapshots are the page bodies of OpenStax *College Algebra 2e* (Jay Abramson, Rice University), retrieved October 27, 2026. Source URLs use the manifest slugs at https://openstax.org/books/college-algebra-2e/pages/ . The material is licensed CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/ . These adaptations use the same license.

The builder retains exposition and the textbook's worked Example / Try It order, excludes the separate homework exercise bank, and pairs Try It exercises with the chapter answer key by exercise ID rather than displayed number. Key snapshots retain only the Try It solution areas. Some Try It keys give a final answer rather than full working; their preceding worked examples provide the method.

Section 2.4 intentionally follows the course's restricted scope: imaginary unit, standard form, simplifying negative radicands, and principal roots versus the two solutions of x² = −a. No complex arithmetic, conjugates, division, powers of i, or complex-plane plotting is introduced. Sections 2.3, 4.2, 4.3, 6.7, and 6.8 are marked optional applications. Other sections retain the textbook's problem types.

Run `python scripts/build_lecture_notes.py` from the repository root. Dependencies are beautifulsoup4 and scipy. Figures are stored in `notes-assets/`; controls and layout reuse `tsm/solutions.js`, `tsm/styles.css`, and `stats/lecture-notes.css`. All answers are static HTML and can be revealed by double-click, double-tap, Enter, or Space.
