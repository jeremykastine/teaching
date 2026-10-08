# Statistics lecture slides

- Textbook: OpenStax **Introductory Statistics 2e**, Barbara Illowsky and Susan Dean.
- Organize PDFs by numbered textbook section. Chapter 1 includes sections 1.1-1.6, including the two labs.
- Put one definition, concept, or problem on each slide.
- Each slide should ask a focused discussion question whenever possible. Definition slides pair a brief definition with a question about applying it.
- Do not include solutions, worked steps, explanatory paragraphs, or presenter narration. The instructor supplies explanations and writes the work with a pen.
- Use large, dark text on white US Letter portrait pages (8.5 × 11 inches). Keep prompts in the upper half and the lower half clear for pen annotations; do not add ruled answer lines or decorative images.
- Keep problems self-contained and precise. Repeated data may appear again when needed to solve a new question.
- Use original problems and explicitly label synthetic data. Preserve textbook scope without reproducing every textbook exercise.
- Keep index.html simple, responsive, and organized by chapter and section. Link both the PDF and the matching textbook section.
- Maintain editable content in slides/source/chapter-NN.json, one file per chapter, and regenerate with scripts/build_slides.py. The shared renderer is ../scripts/slide_builder.py.
- Check all rendered pages, page boundaries, page counts, and local index links before publishing.

## Chapter 1 coverage

1.1: descriptive and inferential statistics; probability and long-run behavior; population, sample, sampling, representative sample, variable, numerical/quantitative and categorical/qualitative variables, data/datum, parameter, statistic; mean/average and proportion; complete study identification and dot plots.

1.2: qualitative and quantitative data; discrete and continuous values; categorical displays; sampling methods; replacement rules; sampling/nonsampling error, variation, bias, nonresponse, undue influence, causality/confounding and self-interest studies.

1.3: frequency tables; relative and cumulative relative frequencies; interpreting inequalities; grouping, rounding, and measurement levels.

1.4: observation and experimentation; variables, units, treatments, lurking variables and confounding; random assignment; controls, placebos and blinding; replication; informed consent, IRB review, risk/benefit, privacy, fabrication/falsification and ethical reporting.

1.5: alternative data-collection lab using download counts; systematic selection; exact and grouped frequency tables; cutoff interpretation and sampling variation.

1.6: alternative sampling lab using fictional campus printers; simple random, systematic, stratified, and cluster samples; proportional allocation and ordering effects.

## Whole-course coverage and sequencing

- Use `course-schedule.md` and `slides/coverage.json` to determine the covered sections. Do not expand into unscheduled chapters.
- Cover every statistical term introduced in each scheduled reading, including synonyms and alternate notation, and represent every major textbook problem type. Check the section prose, examples, chapter glossary, review, practice and homework; matching learning-objective headings alone is insufficient. Maintain `textbook-coverage-audit.md` and its JSON evidence map when pages change.
- Keep textbook emphasis as the main guide. Give a little extra practice to prerequisite ideas that later sections depend on, rather than adding repeated drill.
- Introduce an idea before a problem requires it. Revisit it in a new context when it becomes useful; repeat necessary data and assumptions so each prompt can stand alone.
- Include concise definition questions, representative procedural tasks, interpretation questions, and misconception checks as each section warrants. Preserve one task or concept per page.
- Record objective coverage and relationships between sections in the chapter coverage documents under `docs/`; keep those instructor notes out of the slides.
- Build with `python scripts/build_slides.py` from this course folder. To rebuild selected chapters, pass `--chapters` followed by the chapter numbers. The index always lists all available source sections.
- Mathematical formulas and chart/table layouts must pass width and page-midpoint checks. Review rendered pages, not just source strings.

Statistics: cover the scheduled sections in Chapters 1–8 and preserve the existing Chapter 1 lab decks. Chapter 9 receives one conceptual overview (PDF identifier 9.0), not the full chapter’s calculation procedures. Reinforce frequencies and denominators, distribution shape and spread, conditional probability, random variables, tail areas, sampling distributions and standard errors, and interval/test interpretations. Use the textbook’s stated approximation criteria and explicitly identify the method when conventions differ.
