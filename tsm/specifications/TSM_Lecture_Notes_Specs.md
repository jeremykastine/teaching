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

Begin each topic with its established title, Assigned to line, brief Overview, and Key definitions. Keep detailed procedures, warnings, reasoning, and examples in the worked solutions near the steps where they become relevant.

## 5. Worked examples and browser behavior

- Publish one HTML file for each topic, numbered Topic 1 through Topic 37.
- Place a simple `index.html` at the repository root and list all topic links in numerical order as one continuous table of contents.
- Do not imitate Word pages or insert page breaks in the HTML edition. Let each topic flow continuously in the browser.
- Use the full browser width for worked examples, with modest text gutters and an edge-to-edge horizontal rule. Do not reserve a side column or impose a narrow maximum width on lecture pages. Begin every worked example with the horizontal rule and a bold **Problem N** label. Number examples in document order and restart at **Problem 1** on every topic page.
- Write each problem statement as a concise, precise, self-contained task that can be understood and attempted with the solution hidden. State the action (evaluate, simplify, factor, solve, graph, find, or explain) and include every given expression, equation, value, condition, and requested answer form. Wording such as “Consider,” “Start with,” “Begin with,” or “Worked example” does not state a task by itself.
- Keep answers, intermediate steps, and procedural explanations in the worked solution unless the problem explicitly supplies them as givens. Do not make a problem depend on a previous solution or a hidden continuation; keep successive steps of one problem together. For comparisons, display every expression being compared and say what to evaluate or explain.
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

Normally, place only one problem in a worked-example section.

More than one problem may share a section only when the problems are intentionally presented as a comparison. In that case:

- begin with wording such as `Compare and contrast the following two problems.` or `Compare and contrast the following four problems.`;
- place all compared problem statements in the problem statement, before the solution area; and
- make the solution both solve the problems and explicitly compare their structures, methods, or results.

Do not use the compare/contrast exception merely to save space.

Topic 5 must contain five separate worked-example sections: evaluate `sqrt(36)`, evaluate `sqrt(81)`, evaluate `sqrt(-25)` in terms of `i`, evaluate `sqrt(-121)` in terms of `i`, and compare evaluating `sqrt(9)` with solving `x^2 = 9`. Give each section its own complete problem statement and independently toggled solution area. Do not combine these into one large exercise.

## 7. Examples-first instructional style

- Introduce procedures through problems rather than through a long preliminary lecture.
- A student may initially see a problem without yet knowing the method. The worked explanation must then be complete enough for an absent student to reconstruct the lesson.
- Put the detailed rule, method, warning, and reasoning near the step where it becomes relevant.
- Keep student-facing prose direct and relatively short.
- Preserve useful conceptual explanations, but integrate them into worked solutions instead of creating separate sections headed “Procedure,” “Summary,” “Common Mistake,” or similar.

## 8. Worked-solution standards

- Show the intermediate steps students are expected to learn, not only the starting expression and final answer.
- Keep each algebraic line equivalent to the preceding line unless the prose clearly explains a substitution, comparison, or check.
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

- All 37 topics remain linked from `index.html` in numerical order, without unit headings or grouping.
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
