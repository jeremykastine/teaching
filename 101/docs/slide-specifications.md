# MATH 101 lecture slides

- Textbook: OpenStax **College Algebra 2e**, Jay Abramson (2021). Use the second edition.
- Organize PDFs by numbered textbook section, with one linked PDF per section in index.html.
- Use the same teaching format as the statistics slides: one definition, concept, or problem per page, with a focused discussion question whenever possible.
- Keep definitions brief. Omit worked solutions, explanation paragraphs, and presenter narration. The instructor explains concepts and writes the work with a pen.
- Use white US Letter portrait pages (8.5 × 11 inches), large dark text, and conventional mathematical notation. Keep all prompt content in the upper half and the lower half clear for annotations.
- Typeset fractions, radicals, superscripts, and grouping correctly. Formulas must fit horizontally and vertically without clipping or scroll bars. Split an overly long formula or problem instead of shrinking it to an unreadable size.
- Make each problem precise and self-contained. State nonzero, positivity, or coefficient-domain assumptions when relevant. Preserve original domain restrictions after simplifying rational expressions.
- Use original examples aligned to each section's objectives, rather than reproducing textbook exercises.
- Add questions that expose misconceptions alongside procedural examples.
- Cover all six Chapter 1 sections. Section 1.2 should emphasize exponent rules, consistent with course-schedule.md, while providing a brief scientific-notation review.
- Maintain editable content in slides/source/chapter-NN.json, one file per chapter. Generate PDFs and index.html with scripts/build_slides.py; the shared renderer is ../scripts/slide_builder.py.
- Visually review all pages, confirm annotation space, check mathematical correctness, and verify local index links before publishing.
- Lecture-slide layout is separate from the compact assessment layout in final-exam-specifications.md. Do not apply exam page-count, problem-count, grading, or workspace rules to lecture slides.

## Chapter 1 coverage

1.1: real number sets; order of operations; commutative, associative, distributive, identity and inverse properties; evaluating and simplifying expressions.

1.2: exponent rules; simplifying combinations of powers; brief scientific-notation review.

1.3: principal and higher roots; real-number restrictions; simplifying and combining radicals; rationalizing denominators; rational exponents.

1.4: polynomial definitions; degree and leading coefficient; addition, subtraction, multiplication and special products; several variables; area expressions.

1.5: greatest common factors; grouping; trinomials; differences of squares; perfect squares; sums and differences of cubes; fractional and negative exponents; checking complete factorization.

1.6: rational-expression domains; cancellation of factors; multiplication and division; common denominators; addition and subtraction; complex rational expressions; average-cost models.

## Whole-course coverage and sequencing

- Use `course-schedule.md` and `slides/coverage.json` to determine the covered sections. Do not expand into unscheduled chapters.
- Keep textbook emphasis as the main guide. Give a little extra practice to prerequisite ideas that later sections depend on, rather than adding repeated drill.
- Introduce an idea before a problem requires it. Revisit it in a new context when it becomes useful; repeat necessary data and assumptions so each prompt can stand alone.
- Include concise definition questions, representative procedural tasks, interpretation questions, and misconception checks as each section warrants. Preserve one task or concept per page.
- Record objective coverage and relationships between sections in the chapter coverage documents under `docs/`; keep those instructor notes out of the slides.
- Build with `python scripts/build_slides.py` from this course folder. To rebuild only later chapters and retain approved Chapter 1 PDFs, pass `--chapters` followed by the chapter numbers. The index always lists all available source sections.
- Mathematical formulas and chart/table layouts must pass width and page-midpoint checks. Review rendered pages, not just source strings.

Algebra: include the schedule’s optional applications 2.3, 4.2, 4.3, 6.7, and 6.8, clearly labeled in the index. Keep 2.4 focused on complex arithmetic needed for quadratic and polynomial solutions. Reinforce domains, factoring and zeros, function inputs, transformations, inverse restrictions, and graph intersections where later sections use them.
