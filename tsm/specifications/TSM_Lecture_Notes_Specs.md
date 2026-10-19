# TSM Lecture Notes Specifications

This file governs the TSM 098–099 HTML lecture notes. Treat it as authoritative unless a newer explicit instruction supersedes it; when that happens, apply the new instruction and update this file.

## 1. Purpose and maintained source

The notes serve as assigned readings for students who miss class or need independent review and as lecture notes the instructor can isolate with the Windows Snipping Tool and mark up during class. Prioritize clear worked examples, unobstructed work areas, and fast navigation.

Edit the HTML files in `lessons/` directly. Keep one maintained copy of each topic rather than a parallel Word edition.

All 37 topics were compared with the Word documents before removing them. Topics 2–37 matched in content after accounting for formatting. The older Topic 1 examples and multiplication/division fact guidance have been incorporated into the current Topic 1 HTML lesson. The HTML notes now contain all instructional material from the former Word documents. Do not recreate or synchronize a parallel Word edition.

## 2. Topic files and sequence

Maintain one HTML file per topic using the established filenames, numbered Topic 1 through Topic 37. Keep the established instructional order and topic numbers unless explicitly instructed. Present the topics as one continuous sequence without unit headings or unit labels in the table of contents or on individual topic pages.

## 3. Terminology and course labels

- Label the lecture-note collection **TSM Lecture Notes**, with individual pages labeled by topic. Do not add unit delineations to the table of contents or topic pages.
- Assessments are called **tests**, not “unit tests.”
- Use **TSM 098** and **TSM 099** consistently.
- Preserve every topic's **Assigned to** line. Do not infer assessment coverage from a topic's course assignment.

## 4. Topic introduction

Begin each topic with its established title, Assigned to line, brief Overview, and Key definitions. Place brief general background before the first related problem, including at the start of a new section within a topic. Keep introductions conceptual: definitions, notation, the purpose of a method, and essential rules. Do not solve specific examples in introductions. Keep detailed calculations and reasoning for a stated problem in its own worked solution.

## 5. Worked examples and browser behavior

- Publish one HTML file for each topic, numbered Topic 1 through Topic 37.
- Use the root Teaching `index.html` as the single navigation page, with Lecture notes, Homework, and Practice tests linked directly under the TSM 098 / 099 heading. `tsm/index.html` redirects to that heading. List all topic links in numerical order as one continuous table of contents in `tsm/lecture-notes.html`.
- Do not imitate Word pages or insert page breaks in the HTML edition. Let each topic flow continuously in the browser.
- Use the full browser width for worked examples, with modest text gutters and an edge-to-edge horizontal rule. Do not reserve a side column or impose a narrow maximum width on lecture pages. Begin every worked example with the horizontal rule and a bold **Problem N** label. Number examples in document order and restart at **Problem 1** on every topic page.
- Write each problem statement as a concise, precise, self-contained task that can be understood and attempted with the solution hidden. State the action (evaluate, simplify, factor, solve, graph, find, or explain) and include every given expression, equation, value, condition, and requested answer form. Wording such as “Consider,” “Start with,” “Begin with,” or “Worked example” does not state a task by itself.
- Keep answers, intermediate steps, and procedural explanations in the worked solution unless the problem explicitly supplies them as givens. Do not introduce a separate problem or practice task inside another problem's solution; give each additional task its own visible problem statement and independently toggled worked solution. Do not make a problem depend on a previous solution or a hidden continuation; keep successive steps of one problem together. For comparisons, display every expression being compared and say what to evaluate or explain.
- Place each worked solution directly beneath its complete problem statement in the document flow, and begin it with the corresponding bold **Solution N** label.
- Conceal solutions only by matching their foreground and background colors (white on white). Keep the full solution text and TeX in the static HTML, rendered document, and accessibility tree. Do not conceal panels with `visibility: hidden`, zero opacity, `display: none`, `hidden`, `aria-hidden`, or removal/lazy insertion of content. Preserve the full natural height. Apply the matching color to descendants, MathJax glyphs, fraction/radical borders, and text selection as well, so the blank work area stays visually blank.
- Do not display a show/hide button. Double-clicking or double-tapping anywhere in the solution area must reveal or hide its contents without moving later content. Keep a visible input wrapper around the hidden solution; hiding the contents must not prevent the blank area from receiving input.
- Use the native `dblclick` event for a mouse and explicit double-tap detection for touch/stylus input, with a Touch Events fallback when Pointer Events are unavailable. Require two short nearby taps; reject dragging, scrolling, long presses, canceled gestures, and multi-touch gestures. Suppress synthesized mouse double-clicks after touch input so each double-tap toggles exactly once.
- Apply `touch-action: manipulation` only to the solution area to avoid double-tap zoom conflicts while preserving scrolling and pinch zoom. Do not disable page zoom.
- Make the solution area keyboard focusable with an accessible action label and expanded state. Enter or Space must toggle it; assistive-technology activation must work too. Show a focus outline only during keyboard navigation. Include one brief gesture/keyboard instruction near the top of each topic, leaving the hidden solution area completely blank.
- Include initial white foreground/background colors directly in each solution panel's HTML. The shared stylesheet enforces matching colors for all descendants; JavaScript changes only the reveal class and foreground color. Double-click/double-tap or keyboard activation restores normal text colors without changing layout or removing text from extraction. Color concealment makes the source available to text readers but does not guarantee extraction by every AI service.
- Keep the entire problem and naturally sized blank solution region unobstructed for instructor screenshots.
- Preserve topic titles, **Assigned to** lines, overviews, key definitions, mathematical notation, instructional order, and worked explanations.
- Keep the HTML design simple, readable, responsive, and suitable for GitHub Pages.
- Keep the co-listed schedule and both specification files in the repository. Keep lecture-note content in HTML only.

## 6. One-problem rule and compare/contrast exception

Normally, place only one problem in a worked-example section. Topic 5 Problems 2 and 4 are explicitly requested multipart exercises; keep each exercise and its complete solution in one section, with matching lettered parts.

Apart from the explicitly requested multipart exercises above, more than one problem may share a section only when the problems are intentionally presented as a comparison. In that case:

- begin with wording such as `Compare and contrast the following two problems.` or `Compare and contrast the following four problems.`;
- place all compared problem statements in the problem statement, before the solution area; and
- make the solution both solve the problems and explicitly compare their structures, methods, or results.

Do not use the compare/contrast exception merely to save space.

After the power examples, Topic 5 must retain these five separate square-root worked-example sections: evaluate `sqrt(36)`, evaluate `sqrt(81)`, evaluate `sqrt(-25)` in terms of `i`, evaluate `sqrt(-121)` in terms of `i`, and compare evaluating `sqrt(9)` with solving `x^2 = 9`. Give each section its own complete problem statement and independently toggled solution area. Do not combine these into one large exercise.

## 7. Brief background followed by problems and solutions

- Keep most of each topic in the problem–solution pattern, but do not force all instruction into solution panels.
- At the start of a topic or a new section, provide concise, visible background students need to approach the upcoming problems. Introductions may explain notation, concepts, general rules, and method selection without working specific numerical or algebraic examples.
- A solution must address only its complete visible problem statement. Keep explanations of its actual steps, sign choices, and checks with that solution.
- Move broad introductions and material about later problem types before the first relevant problem. Condense repeated general summaries instead of hiding them in the final solution.
- Give an embedded worked example its own visible task and independently toggled solution. Do not put solved examples into the general background. Avoid duplicate illustrations and incomplete practice prompts.
- Keep prose concise, while leaving enough worked reasoning for independent study.

## 8. Worked-solution standards

- Show the intermediate steps students are expected to learn, not only the starting expression and final answer. General background does not replace the reasoning needed for the particular problem.
- Reserve a centered display line for the original mathematical object or a complete equivalent form of it. Expressions must retain the same value on the original domain; equations and systems must retain the same solution set under the stated restrictions. Prose does not create an exception for a nonequivalent displayed step.
- Put supporting arithmetic, coefficient or exponent calculations, trial values, bounds, approximations, reference formulas, isolated pieces of an expression, and substitution checks inline within explanatory prose, preferably in parentheses when appropriate. Do not place these on standalone math-only lines.
- Preserve the whole expression in each displayed rewrite. For a system, retain all required conditions together in every displayed step; put work on an isolated consequence inline. In an intentional comparison, each displayed chain must clearly belong to one of the original objects being compared.
- Word-problem displays may show a model representing the full stated relationships and equivalent transformations of that model. Keep variable definitions and contextual restrictions explicit. Approximate numerical results belong inline and must use approximation notation.
- Explain important sign changes, distribution, cancellation, common denominators, factoring decisions, equation-solving operations, and graphing choices in plain language.
- State restrictions from the original equation before canceling factors or moving variable denominators to the opposite side.
- Check possible extraneous solutions in the original rational equation.
- Include both answers when taking an even square root in an equation unless context restricts the result.
- Do not hide a substantial expected step behind “after simplifying.”
- Use conventional notation with MathJax-compatible TeX in the HTML. Keep equations as editable text rather than screenshots or plain-text approximations.
- Formulas must fit the available content width, using mathematical line breaks when needed. Do not give formulas horizontal or vertical scrollbars, crop them, hide overflowing glyphs, or use fixed heights. Fractions, radicals, exponents, and every wrapped line must remain fully visible.
- Use the shared MathJax 4 configuration with `displayOverflow: 'linebreak'`, inline line breaking enabled, and a line width of `100%` of the formula container. Keep inline math in the paragraph flow, rather than placing the whole expression in an unbreakable inline-block. Leave formula-container overflow visible.
- Recompute display-equation metrics and line breaks when the content width changes, including phone rotation and switching between desktop and mobile gutters. Preserve readable math sizing and natural solution height; do not shrink every formula to avoid wrapping.
- Add explicit TeX breakpoints such as `\allowbreak` to long comma-separated mathematical lists when their default breakpoints do not permit wrapping.
- When a particularly wide indivisible expression cannot fit, rewrite its layout with equivalent, logically grouped mathematical lines. Do not solve overflow by adding a scrollbar or truncating notation.

## 9. Difficulty and example selection

- Progress from a clear standard case to modest variations.
- Keep coefficients and constants focused on the intended concept.
- Include positive and negative cases when sign behavior matters.
- Use fractional answers when instructionally relevant, but not in every example.
- Avoid large or unpleasant numbers unless they deliberately motivate a useful strategy, such as simplifying before multiplying.
- Avoid unnecessary arithmetic, expansion, or factoring that distracts from the topic.
- Remain within the established TSM 098/099 course scope and schedule.

## 10. Practice material

- Clearly distinguish an assigned practice set from a worked lecture example.
- Do not place multiple unrelated practice problems in a worked-example section.
- If a practice problem is incorporated into the lecture-note sequence as an example, give it the same section structure: problem, then a complete worked solution with its natural height reserved when hidden.
- Unsolved practice sets should be maintained separately or added only when explicitly requested; they should not interrupt the standard worked-problem sequence.

## 11. Cross-listed consistency

- Preserve the established topic sequence for the cross-listed TSM 098/099 course.
- Keep TSM 098 examples at the established foundational level and TSM 099 examples at the established intermediate-algebra level.
- Do not use lecture-note edits to redefine test coverage; assessment specifications are maintained separately.

## 12. Editing workflow

For a topic-specific revision, edit the affected HTML topic files and update this specification when the instructional requirements change. Preserve titles, topic numbers, assignment labels, navigation links, and the existing solution-reveal behavior.

For a global change, apply the requirement consistently across all affected HTML files. Avoid unrelated content changes.

Before pushing, review every changed problem and worked solution, check the mathematics, and verify local links and HTML structure. For layout or interaction changes, inspect the affected pages and confirm that revealing or hiding a solution does not move later content. Check formulas after initial rendering and after resizing at desktop and phone widths: no formula scrollbars or vertical clipping, and long expressions wrap at mathematical breakpoints. Check full-width separators and problem statements at desktop and mobile widths; test mouse double-click, touch double-tap, keyboard activation, and rejection of scroll/pinch gestures. Confirm that touch input cannot toggle twice through synthesized mouse events.

## 13. Quality-control checklist

- All 37 topics remain linked from `lecture-notes.html` in numerical order, without unit headings or grouping.
- Topic titles, assignment labels, overviews, and key definitions are intact.
- Worked problems and solutions are correctly numbered in document order, restarting with Problem 1 and Solution 1 on each topic.
- Each example begins with a horizontal rule and contains a complete problem statement and worked solution.
- With every solution hidden, each problem still states a concise, precise task with all required givens, comparison items, and answer requirements. Revealing the solution shows work and answers for that exact task.
- Only intentional compare/contrast sections contain multiple problems.
- Solutions begin hidden while reserving their full natural height.
- Solution areas toggle with double-click/double-tap and keyboard or assistive-technology activation. No side buttons, visible placeholders, or instructions obstruct the blank work areas. Scrolling and pinch zoom remain available.
- Mathematical notation, intermediate steps, restrictions, and final answers are complete and correct.
- There are no formula scrollbars, clipped expressions, overlapping controls, missing glyphs, broken links, or placeholder text. Long formulas wrap within the available width, and tall notation is never cropped vertically.
- Documentation and the contents page refer only to files that remain in the repository.

## 14. Solving equations with numerical or variable denominators

Apply this approach consistently in Topic 28 and Topic 29, in the HTML notes:

- Combine and simplify each side first, using a common denominator within a side when needed. Reduce fractions and cancel common nonzero factors where possible.
- Once each side is a single simplified expression, move any remaining denominators to multiply the opposite side. When both sides have denominators, move both in the same step. Each denominator multiplies the entire opposite numerator.
- Include examples with a denominator on only one side and with denominators on both sides. Simplification may also remove all denominators before any need to move them.
- Use fraction notation throughout this instruction. Do not write reciprocal factors with negative exponents and do not use the term “cross-multiply” or its variants.
- Teach the method through these worked steps rather than instructing students to multiply every term of the original equation by an LCM or LCD. Common denominators are still used to combine fractions within each side.
- Explain the equality-preserving multiplication where it first becomes relevant. Move a denominator only when it divides the whole side, and retain parentheses around sums and differences.
- For variable denominators, state restrictions from every original denominator before simplifying. Retain them even after a denominator disappears. Divide out a common factor only when it is nonzero for allowable values, and check every candidate in the original equation.

## 15. Integer-pair preparation for factoring

At the end of Topic 3, include separate worked examples asking students to find two integers with a specified sum and product. Prepare students for later trinomial factoring while keeping the task focused on signed-number operations.

- Include positive products with positive and negative sums, negative products with positive, negative, and zero sums, repeated integers, and a zero-product case.
- Make every problem self-contained and give it its own complete hidden solution using the established reveal behavior.
- Explain how the product restricts the signs and how the sum determines the signs or relative sizes. Search factor pairs and verify both the sum and product with the same pair.
- Include the example with sum `-2` and product `-48`. Do not introduce trinomial factoring procedures in this topic.

## 16. Topic 6: approximation before radical simplification

- Begin with an exploration of `sqrt(40)` using squared trial values to bracket the root between integers and then tenths, hundredths, thousandths, and ten-thousandths. A four-function calculator is appropriate; do not use a square-root key for the exploration.
- Explain that approximations can become arbitrarily close, but no finite decimal equals this irrational root. State that its decimal expansion never terminates or eventually repeats. Leave the proof of the non-repeating property beyond the course scope; do not imply that finitely many trials prove irrationality.
- Follow with a self-contained short-table problem: use a supplied approximation for `sqrt(10)` to estimate `sqrt(40)` after rewriting it exactly as `2sqrt(10)`. Distinguish exact equality from decimal approximation.
- Include a brief linked historical note establishing the use of square-root tables and their savings in manual calculation. Describe the short-table example as a practical application; do not claim that this was the primary historical origin or motivation for radical simplification without evidence.
- Give `sqrt(75)`, `sqrt(90)`, `sqrt(-45)`, `sqrt(12)`, `sqrt(50)`, `sqrt(98)`, and `sqrt(-80)` separate visible problems and complete, independently toggled solutions. Do not bury these tasks in another solution.
- State the nonnegative-real-factor condition when introducing the product property. Handle negative radicands by introducing `i` and then simplifying the positive radical.

## 17. Course labels and independent work during exclusive lessons

- Keep the index's course labels consistent with each lesson's Assigned to line. The current 37-topic sequence labels Topics 6, 16, 17, 18, 20, 23, 27, 29, 32, and 34 as TSM 099 only; all others are shared. There are currently no TSM 098-only lessons. The user selected these current lesson labels over the older 38-topic schedule on October 8, 2026.
- Every course-exclusive index entry must show only the other course label, the exact review topic numbers or consecutive ranges, and one link to a printable practice PDF with its answers appended on separate pages. Do not include review-note links or an additional description in the box. Apply this symmetrically if TSM 098-only lessons are added later.
- Use the review assignments recorded in the co-listed schedule, mapped by title to the current topic numbers. Align the schedule with the maintained lecture-note index rather than retaining obsolete topic numbers.
- For Topic 32, use earlier linear equations and checking proposed solutions of systems; do not require substitution or elimination before Topic 33. For Topic 34, include algebraic systems now that Topic 33 has been taught.
- Each current combined packet contains eight pages: three core practice pages, one extension practice page, then four answer pages. Provide a substantive range of standard problems, signs, and relevant reasoning tasks. Plan approximately 45-60 minutes for core work and 15-25 minutes for extensions, recognizing individual pacing. These are practice packets, not tests; do not impose test question-count, scoring, or booklet/answer-sheet packaging rules.
- Keep core and extension tasks within material already taught to the practicing course. For TSM 098 factoring, use GCF, monic trinomials, and difference of squares; include broader polynomial multiplication without assigning TSM 099-only advanced factoring.
- In numerical-fraction equations, follow the Topic 28 method: combine/simplify each side before moving remaining denominators to multiply the opposite side.
- Maintain reproducible source in `scripts/build_independent_practice.py` and packet metadata in `practice/independent-practice.json`. Keep combined student practice-and-answer PDFs in `practice/independent/`. Answers start on a new page after all practice pages. Preserve older standalone answer URLs for compatibility, but link only the combined packet from review boxes. Record practice/answer page counts and the first answer page in the manifest; the builder must reproduce the combined files. Check every answer exactly, render all final pages, and verify index links before publishing.


## 18. Topic 3: signed-number reasoning

- For addition and subtraction, first identify the sign of the first term, then decide whether the second term supports or opposes it. Consider the operation and every sign attached to the second number together.
- Supporting terms combine their sizes and keep their common sign. Opposing terms ask “Which one wins, and by how much?” Use the difference of their sizes and the winner’s sign. Equal opposing sizes give zero. Zero is neither positive nor negative.
- Use this language instead of the former team metaphor. Do not require rewriting every addition or subtraction expression.
- Keep the first addition solution and the first multiplication solution focused on their own expressions. Put shared background before the respective problem sequences.
- End the integer-pair sequence with harder examples using integers in the teens or twenties and larger products, covering two positives, two negatives, and opposite signs with both positive and negative sums. Show factor-pair reasoning and verify both conditions.

## 19. Topic 5: real and complex square roots

- Explain that a negative radicand has no real square root. In a real-only problem or application, “no real value” is a complete answer; proceeding to imaginary numbers is not required.
- Explain that other applications and classroom directions permit or require complex answers. In that setting, use the imaginary unit and continue. The context determines the intended number system; lack of a real value does not imply lack of a complex value.
- Keep the existing problems that explicitly request answers in terms of `i`, and explain in their solutions why that instruction calls for continuing beyond the real numbers. Keep the general distinction in visible background before those problems.


## 20. Powers before square roots (October 14, 2026)

- Keep all 37 topic numbers and established filenames. Title Topic 5 **Evaluating Powers and Square Roots**, retaining its existing URL and heading anchor so prior links still work.
- In Topic 2, briefly introduce positive-integer exponent notation as shorthand for repeated prime factors; identify the base and explain that the exponent counts factors, not multiplication by the exponent. Link to Topic 5 for the fuller treatment.
- Keep numerical-power instruction in Topic 5, before the square-root material; Section 22 governs its current four-problem arrangement. Begin with identifying the base/exponent, expansion, and evaluation of a positive integer power. Then extend the decreasing-exponent pattern to zero and negative exponents.
- Cover negative bases with even and odd exponents, parentheses versus an outside negative sign (positive, zero, and negative exponents), with integer bases. Omit the standalone numerical fractional-base examples from Topic 5. Topic 10 is limited to products under Section 24. State that zero and negative exponent rules require a nonzero base. Negative exponents indicate reciprocals, not negative values.
- Connect squaring to square roots and retain all five square-root examples, the principal-root versus equation-solution distinction, and the real-only versus complex-context guidance.
- Topic 7 applies powers in mixed expressions and substitution rather than repeating the standalone power lesson. Its overview links back to Topic 5. Its example set and assessment labels are governed by Section 21 below.
- Keep the existing reveal behavior and renumber problems automatically within each topic. Topic 5 has nine worked examples (four power exercises followed by five square-root exercises); Topic 7 now has 16 under Section 21. Allow more than one meeting for Topic 5 within the general schedule.
- Update the contents page, co-listed schedule, homework descriptions and affected PDFs, and assessment prerequisite guidance. This relocation does not redefine test question types or point structures.


## 21. Topic 7: unified evaluation and assessment labels (October 15, 2026)

- Keep Topic 7 assigned to both courses. All students study and attempt every example in one continuous sequence. Remove course-separated sections, stop instructions, and parallel review assignments within Topics 7 and 8.
- Explain near the beginning that **Assessment: TSM 099 only** concerns independent test expectations, not participation in instruction. Put the exact label beside selected problem statements, never on a whole instructional section.
- Retain all 16 worked examples and their independently revealed solutions. Begin with three numerical examples: basic precedence; a long unparenthesized expression with equal-precedence division/multiplication; and grouped arithmetic with a fraction bar.
- Continue with two-variable linear substitution, parenthesized linear expressions, a linear numerator over a constant denominator, a linear combination, and direct factored-polynomial evaluation. Retain quadratic and cubic polynomials at -10, 0, and 10, two rational expressions with linear/quadratic variable denominators, and four quadratic-formula examples covering positive/negative b, negative c, and negative a.
- Every actual division and every final value in Topic 7 must be an integer. Evaluate each quadratic-formula branch with perfect-square radicands. Keep formula evaluation distinct from equation solving.
- Apply the test specifications by actual demand. Problems 1-9 remain unlabeled: in particular, the standard-form quadratic at -10, 0, and 10 is explicitly assessed in TSM 098 Arithmetic Question 4. Factored products and expanded polynomial forms also occur in TSM 098 expression comparisons; their appearance alone does not justify a TSM 099 label.
- Problems 11-16 carry the TSM 099 assessment label: variable-denominator rational evaluation and quadratic-formula evaluation exceed TSM 098 test requirements and support TSM 099 work.
- **Assessment ambiguity retained explicitly:** Problem 10's standalone cubic evaluation is named in neither course's Arithmetic Test evaluation map. TSM 098 does assess higher-degree polynomial operations/comparisons; TSM 099's standalone polynomial evaluation formats specify quadratics. Preserve the cubic for the requested instructional range, but leave it unlabeled rather than implying a settled TSM 099-only test requirement. The label must not be treated as an exhaustive list of test formats. Similarly, Problem 12's quadratic denominator supports later TSM 099 rational-expression work; TSM 099 Arithmetic Question 5 itself specifies constant or linear denominators. Do not silently expand either test map.
- Keep every requested input/branch visible and explicitly compare results in each relevant solution. Preserve complete-expression displayed rewrites, with supporting calculations inline. Retain former heading anchors for compatibility, but give them content-based headings.
- Keep the contents page, planning schedule, README, and assessment prerequisite guidance consistent with the unified instruction. Do not alter test question maps, scoring, or complexity controls through this lesson revision.


## 22. Division foundation and power table (October 14, 2026)

- Title Topic 1 **Division and Divisibility**, preserving its filename and heading anchor. State basic addition, subtraction, and multiplication as prerequisites.
- Begin with division reversing multiplication; notation using a division symbol, slash, and fraction bar; and expressing a division with a fraction bar to keep an exact answer. Explain grouping. Defer unit-fraction terminology and division as multiplication by a reciprocal until the fuller treatment of fractions later in the course. Exclude zero divisors.
- Teach **successive divisions** from left to right, combining them into one division by the product of the divisors and separating one division by a product into successive divisions by its factors. Keep this instruction in Topic 1 alongside divisibility, without unit-fraction multiplication. Include unequal divisors, three successive divisions by 3, and a division-by-6 example separated into division by 2 followed by division by 3; explain that the first quotient is divisible by the second factor. Preserve all existing multiplication facts, table-pattern investigations, and divisibility examples after the division instruction.
- Topic 5 Problem 1 contains one large visible table with rows from 3^4 through 3^(-3). Prefill only the exponential-expression column; leave base, exponent, multiplication/division indicated, and final-answer cells blank. Keep rows content-sized with only 3px of vertical cell padding and no fixed row height, on desktop and mobile. Supply a completed copy inside its independently toggled solution.
- Establish 1 as the starting value. Show positive powers as repeated multiplication from 1, zero as **Do nothing** with answer 1, and negative powers as horizontal repeated division from 1. Give fractional final answers. Refer to Topic 1 for combining and separating successive divisions, using division notation.
- Topic 5 Problem 2 is a four- or five-part standalone exercise using assorted positive integer bases and positive, zero, and negative integer exponents in a mixed order. Use no negative bases or outside minus signs. Give exact fractional answers where needed and complete worked solutions for every part.
- Topic 5 Problem 3 is a two-column comparison table: `-5^n` on the left and `(-5)^n` on the right, for exponents 3, 2, 1, 0, -1, -2 in that order. Left-align the expression in each cell, keep rows content-sized, and provide a completed comparison table with explanations in its independently toggled solution.
- Topic 5 Problem 4 is a four- or five-part standalone exercise mixing negative bases in parentheses and outside minus signs, with assorted integer bases and positive, zero, and negative integer exponents. Ask students to identify the base and evaluate; show all parts and complete worked solutions.
- These four power exercises replace the previous standalone power examples. Keep the five existing square-root exercises as Problems 5–9, with their individual solutions. Omit numerical fractional-base examples without relocating them.


## 23. Topic 8: when an equation is true (revised October 16, 2026)

- Preserve the established title, URL, Assigned to line, navigation, homework links, and shared solution interactions. Connect Topic 7 evaluation to substituting the same chosen number into both sides of an equation. Use ordinary expression notation, without function notation or formal domain terminology.
- Present every comparison as an equation, with an equals sign between two complete expressions. Explain that writing an equals sign states equality; students must investigate when that statement is true. Define equation, solution, identity, and equivalent/interchangeable expressions.
- Introduce these outcomes in order: **The equation is true for every value of x.** (always; an identity with interchangeable sides); **The equation is true for one or a few scattered values of x.** (sometimes; the matching values are solutions); **The equation is true for no value of x.** (never; no solution). Keep the instructor-approved explanation below the first heading: sometimes “every” means every value under consideration, because certain values make a calculation impossible. Avoid advanced qualifications about other types of solution sets.
- Evaluate each side separately at every supplied input, identify true/false substitutions and solutions, and classify the equation. Explain interchangeability. Do not require general equation-solving methods at this stage. Prove identities or impossibility with brief algebraic reasoning where requested, rather than treating finite substitution evidence as proof.
- The first three equations are fixed: Problem 1, `3(2x-5)+4=6x-11`, at -2, 0, 3 (identity; distribute and combine constants); Problem 2, `2x^2+6=6x+2`, at -1, 1, 2, 3 (sometimes; exactly two supplied values are solutions); Problem 3, `2(3x+1)=6x+3`, at -2, 0, 3 (never; multiply the first term but incorrectly add 2 to the second term). Explain how the correct simpler expression in Problem 1 can replace the more complicated expression. In Problem 2, call attention to the similar-looking sides without assuming they are equivalent. In Problem 3, explain that distribution requires multiplication of both terms and that the sides differ by 1 for every input.
- These three set the minimum difficulty. Remove the former simpler comparisons `2(x+4)` versus `3x+5`, `3(x-2)+x` versus `4x-6`, and `x(x+2)` versus `3x`. Retain the more involved factored, multiple-factor, and rational comparisons as equations, with complete solutions for every supplied input.
- The nine-problem sequence is: (1) `3(2x-5)+4=6x-11`; (2) `2x^2+6=6x+2`; (3) `2(3x+1)=6x+3`; (4) `(x-3)(x+3)=x^2-9`; (5) `(x+1)x(x-1)=0`; (6) `(x^2-1)/(x-1)=x+1`; (7) `(x^2-1)/(x-1)=3/(x-1)`; (8) `(x^2-1)/(x-1)=(2x+2)/(x-1)`; (9) `(x-2)^2+1=x^2-4x+6`. The final squared-expression example now has a constant contradiction, rather than relying on a sign argument that excludes complex numbers.
- Problems 6-8 retain **Assessment: TSM 099 only** for variable-denominator comparisons. All students study all problems. Do not alter assessment specifications through this lesson revision.
- Keep division-by-zero handling concrete: x=1 is excluded from the rational examples and is not a solution. Remember that restriction when replacing the fraction with a simpler expression. For Problem 6, identify an identity for the values under consideration; do not claim unrestricted interchangeability.
- Retain three true substitutions followed by a false one, and three false substitutions followed by a true one. One match does not prove an identity; one disagreement disproves an identity; several disagreements do not establish no solution. Use constant contradictions for the never-true examples, avoiding examples that admit imaginary solutions.
- Keep complete calculations and explanations in static solution panels with their natural height reserved. Preserve MathJax notation, full-width problem areas, relative links, and double-click/double-tap/keyboard reveal behavior.


## 24. Topic 10: combining like factors (October 19, 2026)

- Retain only Problems 1–11 and their complete worked solutions, ending with the four-part comparison of addition and multiplication involving `3x^4` and `3x^5`. Preserve the original first eleven problems without reordering or rewriting them.
- Remove everything after Problem 11 in the instructional content, including Problems 12–24 and the sections on powers of powers, powers of products and quotients, quotient rules, negative-exponent manipulation, and nonzero-base restrictions. Preserve bottom lesson navigation.
- Limit the overview and definitions to counting repeated factors, multiplying coefficients, combining powers with the same base by adding exponents, and distinguishing products from sums. Do not relocate the removed material or change assessment specifications.
