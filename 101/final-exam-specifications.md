# MATH 101 Assessment Specifications

## Calculator policy (October 21, 2026)

Include this instruction in the student directions of every future test/exam and practice test/exam, including unit tests, retakes, diagnostics, and finals: **"Students may use a basic, non-scientific calculator only."** A basic four-function calculator is permitted; scientific, graphing, and CAS calculators are not permitted.

## Purpose
Standing specification for generating MATH 101 (College Algebra) assessments and their practice versions, including practice diagnostics, diagnostics, practice finals, finals, and comparable generated tests. Use this unless a later instruction explicitly changes a rule.

Unless a rule is explicitly limited to a particular assessment, the presentation, directions, answer-sheet, answer-key, verification, and packaging conventions in this document apply equally to practice and non-practice versions and to diagnostics and finals.

## Assessment scope and unit tests
- All MATH 101 tests assess strictly algebraic content, including graph interpretation. Word problems, contextual applications, modeling, regression, and optimization applications are classroom activities/labs, not test items.
- For the four five-question, 30-minute unit tests and their practice/retake versions, use [unit-test-specifications.md](unit-test-specifications.md). Each unit-test question is worth 20 points; its unit-specific structure and scoring override the cumulative architecture below. Shared presentation, calculator, identifier, verification, and packaging rules still apply.
- The ten problem types and ten-point question amounts below define the cumulative diagnostic/final family; they are not the question map for a unit test.

## Instruction hierarchy and verification
- Follow the problem-type specification first, then the global rules in this document.
- A specific problem-type requirement overrides a general presentation preference when the two conflict.
- Do not silently add assessed skills that are not named in the applicable problem type.
- Generate first, verify second, and replace any item that fails a required constraint.
- Work every problem completely before presenting it. Verify algebra, domains, intercepts, roots, graphs, and final simplifications.
- A new version must use genuinely new numerical values, expressions, or graphs where applicable; merely reordering the same questions does not create a new version.

## Global structure — cumulative diagnostics and finals
- Exactly **10 main questions**, one from each problem type below.
- **100 points total; 10 points per main question.** A question may have multiple parts, but all parts stay on one topic.
- Presentation order is **randomized by default** unless explicitly fixed.
- Students may use a **basic four-function calculator only**. No scientific, graphing, CAS, or calculator-app functions.
- Favor exact answers and clean arithmetic; do not require numerical logarithm approximations.
- Balance difficulty at the **whole-exam level**. If one randomized item is harder than average for its type, offset it with easier approved items elsewhere. Avoid several upper-end items on the same version.

## Version identifiers
For every newly generated test/exam or practice test/exam version, independently choose a random five-digit integer from 10000 through 99999 as its version identifier. Apply this to single versions and every version in a requested batch, including unit tests, retakes, diagnostics, and finals. Do not use timestamps, sequential numbering, lettered labels, or batch suffixes; no numerical ordering is required. Duplicate identifiers are acceptable; no uniqueness check or registry is required. Use the same identifier on the student test, corresponding answer key, and filename when practical.

## Standard presentation and output conventions

### Combined student test and instructor key

Follow the approved [algebra test format](../docs/algebra-test-format.md) for practice and actual unit tests, diagnostics, and finals. It replaces the former booklet -> separate answer sheet -> key format.

- Use US Letter portrait pages with print-safe margins: questions in the left two-thirds of the usable width and vertically aligned final-answer areas in the right one-third.
- Keep prompts compact, notation conventional, and each main question together with its response areas. Include the title, identifier, and student name; omit the course-section field.
- Directions must tell students to complete and show all work on separate paper and write exact final answers in the right column. Maintain the four-function-calculator policy.
- Put blank grids students complete in the right answer column; supplied graphs they interpret stay with the left-hand prompt. Maintain legible scales and labels.
- Aim for one or two student pages; permit longer finals when needed for adequate answer space and readable material.
- The key should fit one page, front only, using exactly one, two, or three columns when the student test has one, two, or three pages. Each column identifies and matches its corresponding test page. Longer tests may require additional key pages with up to three columns per page.
- Compute the key-first layout, then use the same fixed row heights, vertical answer positions, labels, part points, and separator boundaries for the student pages. Key columns may be wider than the student answer column; do not scale their vertical geometry. Student and key page counts no longer need to be equal.
- Never put hidden, white, or transparent key answers on student pages. Omit answers while preserving the shared geometry.
- Use open response areas without internal baselines. Solid rules separate main questions; light dotted/dashed rules occur only between subparts, never after the final part or in a single-part area.
- Show points only at the bottom of each response part, not beside problem headings. Each cumulative question totals 10 points; each unit question totals 20 points. Do not invent redundant single-part sublabels.
- Keep the key concise. Include necessary grading information; provide extended worked solutions only when requested. Wrap long key answers and increase matched row heights instead of making notation too small.

### Optional compliance/audit material
- Do **not** include a compliance report, generation audit, or similar metadata automatically.
- The generating system must still perform the full internal verification checklist every time.
- If a compliance report or audit is explicitly requested, provide it as a separate instructor-only section after the answer key and keep it off all student-facing pages.

## Combined duplex-safe deliverable

Deliver one PDF per version: combined student test, any required completely blank padding page, then the instructor key. There is no separate student answer sheet.

- The student test and key each start on an odd-numbered PDF page (a fresh front side).
- Insert a blank page before the key for an odd-length test; insert none for an even-length test.
- If merging complete version packets, pad as needed before the next test so it starts on a fresh sheet.
- Include compliance/audit material only when requested, starting on a fresh front side after the key.
- Retain identifiers and filenames when reformatting existing versions. Honor explicit requests for separate files or alternate packaging.

---

# Required Problem Types

## 1. Composition of Functions — Section 3.4
Multiple-choice recognition. Give `h(x)` naturally expressible as `f(g(x))`; choices propose pairs `f,g`. Student identifies the correct inside/outside functions. Distractors may reverse composition or misplace constants/coefficients.

## 2. Transformations from Graphs — Section 3.5
Show original `y=f(x)` and transformed `y=g(x)` on the same coordinate plane, with no algebraic formula for the original. Multiple choice asks for `g` in terms of `f`.

Approved families:
- horizontal/vertical translations (may combine with each other);
- vertical stretch/compression and/or x-axis reflection;
- horizontal stretch/compression and/or y-axis reflection.
Do not combine vertical and horizontal scaling/reflection families, and do not combine those families with translations unless later changed. Use an asymmetric graph.

## 3. Construct Polynomial from Graph — Section 5.3
Give a degree 3–5 polynomial graph. All real zeros and multiplicities must be visually clear, plus one labeled point to determine leading constant `a`. Student writes the polynomial, preferably factored. Choose data so `a` is an integer or simple fraction.

## 4. Find All Polynomial Zeros — Section 5.5
Degree 3 or 4 polynomial with exactly two real irrational roots plus one rational root (degree 3) or two rational roots (degree 4).
Student must:
1. list all Rational Root Theorem candidates;
2. test only a small subset supplied by the problem;
3. identify rational root(s);
4. use **polynomial long division** to reduce to a quadratic;
5. use the **quadratic formula** for the final two roots.
Remaining quadratic has positive nonsquare discriminant; no complex final roots.

## 5. Rational Function Behavior — Section 5.6
Choose one comparable form:

**Form A:** numerator/denominator already fully factored; no slant asymptote; may include a hole. Ask for relevant domain, hole, vertical/horizontal asymptotes/end behavior, and intercepts.

**Form B:** no hole; simple unfactored degree-2 numerator over degree-1 denominator; student uses polynomial division for a slant asymptote. Do not add difficult factoring.

## 6. Radical Function Analysis — Section 5.7
Give a transformed square-root function. Ask for domain, range, x-intercept, y-intercept when applicable, and end behavior. Choose clean exact values. Prompt may be one compact sentence.

## 7. Exponential Graph Matching — Section 6.2
Show four `a b^x` graphs on one coordinate plane and four algebraic functions. No horizontal/vertical shifts. Students distinguish `a`, growth vs decay, and relative rates.

Graph style:
- all four curves use the **same solid-line style**;
- label curves **A, B, C, D at both the far left and far right edges** of the graph window;
- choose the window so labels are unambiguous;
- do not make the task solvable merely by separating growth from decay.

## 8. Transformed Logarithmic Function — Section 6.4
Give a transformed logarithmic function. Ask for domain, range, vertical asymptote, x-intercept, and end behavior. Choose values so the x-intercept is exact and corresponds to a familiar power of the base. No decimal log approximation.

## 9. Logarithmic Properties — Section 6.5
Short exact-evaluation items using product, quotient, power, and/or change-of-base properties. The property must make a real difference: individual logs should not already be easy by inspection. Prefer decimal common-log patterns that combine to powers of 10. Change-of-base items remain exact and hand-solvable. Usually one or two properties per subproblem.

## 10. Equation / Nonlinear-System Solving
Choose top-level category with equal probability:
- 25% radical equation
- 25% exponential equation
- 25% logarithmic equation
- 25% nonlinear system
Subtypes within a category are equally likely.

### 10A Radical equation — Section 5.7
Always exactly **one radical**; never two-radical equations.
- 50%: easy isolation -> quadratic -> two candidates, exactly one extraneous.
- 50%: one radical -> quadratic -> both solutions valid.

### 10B Exponential equation — Section 6.6
Different-looking bases that rewrite to a common base; equate exponents. No logarithms required. Preferred level: `8^(x-1)=4^(x+1)`.

### 10C Logarithmic equation — Section 6.6
Require exactly one logarithmic property before converting to exponential form. Three equally likely subtypes:
1. product property -> linear equation;
2. quotient property -> linear equation;
3. product property -> quadratic plus domain rejection.
No scientific-calculator approximation.

### 10D Nonlinear system — Section 7.3
Two equally likely subtypes:
1. line + parabola;
2. line + circle.
Solve algebraically by substitution/equivalent method, normally with two intersections. Exclude unnecessary quartics, cases where one variable is simply given as a constant, and ordinary linear systems.

## Coverage philosophy
The final emphasizes function-centered College Algebra. Quadratic equations and ordinary linear systems are prerequisite material rather than dedicated final topics, though quadratic solving may appear as a supporting skill. Domain/range are embedded in function-analysis questions.

## Generation checklist
Before finalizing, verify all 10 problem types appear once; default order is randomized; Question 10 probabilities/subtype probabilities are respected; four-function-calculator limit is honored; graphs are legible; exponential graph labels follow the A–D solid-curve rule; exact values are used where possible; Q4 uses RRT + limited testing + long division + quadratic formula; Q5 uses approved Form A/B; log-property items genuinely benefit from the properties; whole-exam difficulty is balanced; scoring totals 100; points appear only in right-hand response areas and key; student test/key are key-first vertically matched layouts with open response areas and **no internal answer baselines**; question headings do **not** repeat `10 points`, while point values appear only with the response parts; solid rules separate questions and light dotted/dashed rules only separate internal parts; no redundant separators or single-part sublabels; **no section field appears**; version IDs follow the random five-digit rule (duplicates acceptable; no sequence required); internal verification has been completed; optional compliance/audit material is omitted unless requested; and the final PDF is duplex-safe with combined student test -> required blank padding -> page-matching key columns.