# MATH 101 Assessment Specifications

## Purpose
Standing specification for generating MATH 101 (College Algebra) assessments and their practice versions, including practice diagnostics, diagnostics, practice finals, finals, and comparable generated tests. Use this unless a later instruction explicitly changes a rule.

Unless a rule is explicitly limited to a particular assessment, the presentation, directions, answer-sheet, answer-key, verification, and packaging conventions in this document apply equally to practice and non-practice versions and to diagnostics and finals.

## Instruction hierarchy and verification
- Follow the problem-type specification first, then the global rules in this document.
- A specific problem-type requirement overrides a general presentation preference when the two conflict.
- Do not silently add assessed skills that are not named in the applicable problem type.
- Generate first, verify second, and replace any item that fails a required constraint.
- Work every problem completely before presenting it. Verify algebra, domains, intercepts, roots, graphs, and final simplifications.
- A new version must use genuinely new numerical values, expressions, or graphs where applicable; merely reordering the same questions does not create a new version.

## Global structure
- Exactly **10 main questions**, one from each problem type below.
- **100 points total; 10 points per main question.** A question may have multiple parts, but all parts stay on one topic.
- Presentation order is **randomized by default** unless explicitly fixed.
- Students may use a **basic four-function calculator only**. No scientific, graphing, CAS, or calculator-app functions.
- Favor exact answers and clean arithmetic; do not require numerical logarithm approximations.
- Balance difficulty at the **whole-exam level**. If one randomized item is harder than average for its type, offset it with easier approved items elsewhere. Avoid several upper-end items on the same version.

## Version identifiers
- Do not use lettered labels such as Version A/B.
- Single version: `YYYYMMDDHHMM` using the user's local time, 24-hour clock, nearest minute, no punctuation.
- Batch versions: same timestamp plus `.1`, `.2`, `.3`, etc.
- Use the same identifier on the exam booklet, student answer sheet, answer key, and filename when practical.

## Standard presentation and output conventions

### Exam booklet
- Do **not** print point values in the exam booklet unless specifically requested.
- Keep prompts compact. Short feature lists should usually be written in one sentence rather than one item per line.
- Keep vertical subparts only when they represent meaningfully different procedures or a deliberate sequence of work.
- Multiple-choice options may remain vertical when clearer.
- Use conventional mathematical notation, clear grouping symbols, and unambiguous subtraction signs.
- Do **not** reserve or insert workspace for students to show work in the exam booklet. The booklet should be compact and content-flow-driven rather than spaced as a worksheet.
- Standard directions must explicitly tell students to **complete and show all work on a separate sheet of paper**.
- Continue to tell students to give exact answers unless a problem explicitly requests an approximation.
- When a separate student answer sheet is included, directions must tell students to record final answers on that sheet. If a practice version intentionally has no answer sheet, omit only that answer-sheet clause.
- Natural unused space at the end of a page is acceptable, but do not deliberately create blank regions as working space.

### Student answer sheet and answer key
When a student answer sheet is included, it must be paired with a geometrically matched answer key. A practice version may omit the student answer sheet when explicitly requested; the remaining layout rules still apply to any answer key that is produced.

#### Content and scoring
- The answer sheet contains **no problem statements**.
- Include version identifier, **student name**, question numbers, concise part labels, and point values.
- **Do not include a section/course-section field.** Only one section is being taught.
- Follow the actual randomized numbering/order of that version.
- Each main question totals 10 points. Multipart point values sum to 10.
- Do **not** print a redundant `10 points` label in the question heading/header line (for example, next to “Question 1,” “Question 2,” etc.).
- Show point values only at the response-part level, positioned with the corresponding answer area. For multipart questions, show the appropriate per-part values such as `2 pts`, `3 pts`, etc.
- For a single-part 10-point question, show `10 pts` once with that single response area; do not repeat it in the question heading and do not invent a redundant A/1 subpart.
- Point weights should reflect the mathematical work expected rather than merely the number of blanks.
- Do not add unnecessary writing space. The answer sheet is for concise final answers, not for showing work.
- Whenever a student answer sheet is included, it must fit on **one physical sheet front/back**, i.e. exactly **2 PDF pages**, unless a later instruction explicitly overrides this.

#### Row geometry
- Left part labels/descriptors occupy a narrow left column; point values occupy a narrow right column.
- The middle of each response row is an **open answer area**. Do **not** draw a separate writing/baseline inside that area.
- Use **solid horizontal rules only between main questions**.
- Use a light **dotted/dashed horizontal separator only between successive parts of the same question**.
- The separator itself defines the boundary of the answer area: there must never be both a part separator and an additional answer line within the same space.
- Dotted/dashed separators occur only *between* parts: 2 parts -> 1 separator; 3 parts -> 2; 4 parts -> 3.
- No dotted/dashed separator after the final part, and none at all for a single-part question.
- Never stack a dotted/dashed part separator and a solid question separator beneath the same final response area.
- Keep row heights compact while leaving enough open space for a concise final answer.

#### Key-first matched layout
- Build the **answer key first** as the canonical layout.
- The student sheet and answer key must be generated from the same source/template, with identical page breaks, row heights, spacing, separator positions, labels, and point-value positions.
- The answer key places the answer text in the same open middle area that is blank on the student sheet.
- The student PDF must contain **no answer text, including hidden white/transparent answer text**. Preserve matching geometry with fixed row dimensions or equivalent shared-template layout rather than embedding hidden answers.
- The default key is a concise grading reference rather than a worked-solutions document. Worked solutions or extended instructor notes are included only when separately requested.

### Optional compliance/audit material
- Do **not** include a compliance report, generation audit, or similar metadata automatically.
- The generating system must still perform the full internal verification checklist every time.
- If a compliance report or audit is explicitly requested, provide it as a separate instructor-only section after the answer key and keep it off all student-facing pages.

## Combined duplex-safe deliverable
By default, deliver **one combined PDF per version** in this order:
1. Exam booklet
2. Student answer sheet
3. Answer key
4. Optional compliance/audit section only when explicitly requested

Printing rules:
- Each included section begins on an **odd-numbered PDF page**, i.e. the front of a fresh duplex sheet.
- Insert blank padding pages wherever needed so one section never begins on the back of the preceding section.
- Whenever included, the student answer sheet is exactly **2 PDF pages** (one sheet front/back).
- The answer key is exactly **2 PDF pages** and geometrically identical to the answer sheet.
- Add padding if ever needed so the key or any requested audit section also starts on a fresh front side.
- If a request explicitly asks for separate files or a different packaging format, follow that request instead.

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
Before finalizing, verify all 10 problem types appear once; default order is randomized; Question 10 probabilities/subtype probabilities are respected; four-function-calculator limit is honored; graphs are legible; exponential graph labels follow the A–D solid-curve rule; exact values are used where possible; Q4 uses RRT + limited testing + long division + quadratic formula; Q5 uses approved Form A/B; log-property items genuinely benefit from the properties; whole-exam difficulty is balanced; scoring totals 100; exam booklet omits points; answer sheet/key are key-first matched layouts with open response areas and **no internal answer baselines**; question headings do **not** repeat `10 points`, while point values appear only with the response parts; solid rules separate questions and light dotted/dashed rules only separate internal parts; no redundant separators or single-part sublabels; **no section field appears**; version IDs follow the timestamp rule; internal verification has been completed; optional compliance/audit material is omitted unless requested; and the final PDF is duplex-safe with exam -> answer sheet -> key.