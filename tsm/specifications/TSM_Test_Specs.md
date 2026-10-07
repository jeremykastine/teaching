# TSM 098-099 AI Assessment Master Specification

STATUS: CONTROLLING GENERATION SPECIFICATION  
AUDIENCE: AI SYSTEMS ONLY  
OWNER: Professor Jeremy Kastine  
UPDATED: September 2026

PURPOSE: Use this file as the controlling prompt for generating TSM 098 and TSM 099 unit tests, diagnostics, practice finals, official finals, answer sheets, answer keys, and optional compliance reports. It defines content, difficulty, variation, ordering, validation, institutional-assessment requirements, scoring, and presentation. Do not summarize or reinterpret these requirements before generating an assessment. Apply them directly.

# Contents and use

The guide moves from broad rules to course-level expectations and then to exact requirements for each assessment. When requirements conflict, the more specific instruction controls.

## Document hierarchy

- **Part I - Universal generation and presentation standards.** Rules that apply to every assessment and every batch.
- **Part II - Course-level expectations.** The intended boundary between TSM 098 and TSM 099.
- **Part III - Unit-test specifications.** Question maps and detailed construction rules for the nine five-question unit tests.
- **Part IV - Diagnostic and final-exam specifications.** Ten-question exam architecture, institutional item banks, supplemental selection rules, and ordering modes.
- **Part V - Final pre-delivery audit.** Internal checks required before any generated assessment is delivered.

## Assessment index

- TSM 098 Arithmetic Test
- TSM 098 Polynomials Test
- TSM 098 Fractions Test
- TSM 098 Linear Equations and Linear Systems Test
- TSM 099 Arithmetic Test
- TSM 099 Polynomials Test
- TSM 099 Rational Expressions Test
- TSM 099 Quadratic and Rational Equations Test
- TSM 099 Graphing Test
- TSM 098 Diagnostic / Practice Final / Official Final
- TSM 099 Diagnostic / Practice Final / Official Final

## How to issue a future request

State the assessment name and number of versions. The standardized presentation and packaging rules below apply unless the request explicitly asks for a different delivery format. Examples include:

- "Create one new version of every test for Fall Quarter."
- "Create 20 distinct versions of the TSM 099 Rational Expressions Test."
- "Create four versions of the TSM 098 Fractions Test."
- "Create a randomized TSM 099 diagnostic."
- "Create an official TSM 098 final using the standardized order supplied in my request."
- "Create a TSM 099 diagnostic and include the compliance report."

# Part I. Universal generation and presentation standards

## 1. Instruction hierarchy

- Follow the individual test specification first, then the course-level specification, then these universal rules.
- A test-specific exception overrides a general preference. For example, TSM 098 polynomial multiplication intentionally extends beyond the binomial-only multiplication item on the TSM 099 Polynomials Test.
- Treat a numbered question as one question unit even when it contains lettered parts.
- Do not silently add assessed skills that are not named in the applicable test section.
- Presentation rules in this Part I do not alter the mathematical content rules in Parts II-IV.

## 2. Version and batch rules

- Every Part III unit test contains exactly five numbered question units. Every Part IV diagnostic, practice final, and official final contains exactly ten numbered question units.
- For Part III unit tests, randomize the five question units independently for every version. Keep the parts of a multipart question together.
- For Part IV exams, follow the requested ordering mode: STANDARDIZED for an official final when a fixed item-number map is supplied; RANDOMIZED for a diagnostic or practice final unless the request states otherwise.
- A new version must use genuinely new numerical values and expressions; merely reordering the same problems does not create a new version.
- Within a batch, avoid duplicate questions, equivalent coefficient sets, repeated graphs, and identical answer patterns when reasonable.
- **Do not use lettered labels such as Version A/B.**
- A single generated version uses a **12-digit timestamp identifier** in the format `YYYYMMDDHHMM`, using the user's local date/time, a 24-hour clock, and the nearest minute, with no punctuation.
- Multiple versions generated in the same request use the same timestamp plus `.1`, `.2`, `.3`, and so on.
- Use the same version identifier on the exam booklet, student answer sheet, answer key, requested compliance report, and filename when practical.
- When an option is meant to vary across versions, distribute the options as evenly as practical across a large batch rather than relying on uncontrolled randomness.
- Randomization must never weaken a required constraint. Generate first, verify second, and replace any item that fails the specification.

## 3. Mathematical quality

- Work every problem completely before presenting it. Verify operations, factoring, domains, intersections, discriminants, candidate solutions, excluded values, graphs, and final reductions.
- Use integer coefficients and manageable values unless a specification explicitly requires a fractional answer or irrational result.
- Avoid accidental cancellation, unintended extra solutions, unintended factoring methods, ambiguous notation, and answers outside the stated graphing window.
- Do not use decimals unless explicitly requested. Express rational answers as reduced fractions and irrational quadratic-formula answers in simplified radical form.
- Do not introduce complex numbers except where the TSM 099 Arithmetic Test explicitly asks for an imaginary square root.
- Keep arithmetic secondary to the skill being assessed; difficulty should come from the intended concept rather than oversized numbers.
- Internal verification is mandatory even when no compliance report is requested.

## 4. Scoring

- Every five-question Part III unit test is worth **100 points total**, with each numbered main question unit worth **20 points**.
- Every ten-question Part IV diagnostic, practice final, or official final is worth **100 points total**, with each numbered main question unit worth **10 points**.
- If a main question has multiple parts, assign subpart point values that sum to the full value of that main question: **20 points for Part III unit-test questions** and **10 points for Part IV exam questions**.
- Prefer whole-number point values; half-points are acceptable when needed for an even or sensible distribution.
- Point weights should reflect the mathematical work expected rather than merely the number of blanks.
- Do **not** print point values in the exam booklet by default. Point values belong on the student answer sheet and answer key unless a request explicitly asks for them in the booklet.

## 5. Exam-booklet presentation

- Begin with the exact assessment title, version identifier, and short directions applicable to that test.
- Include a student-name line. Do **not** include a section/course-section field.
- Do not label questions by hidden role, such as basic problem, exceptional case, formula problem, institutional item, supplemental item, or cancellation problem.
- Use conventional mathematical notation, clear grouping symbols, and unambiguous subtraction signs.
- Keep prompts **compact**. Short feature lists or one- or two-word response categories should usually be written in one sentence rather than stacked vertically.
- Keep vertical subparts only when they represent genuinely different tasks or a deliberate sequence of work.
- Multiple-choice options may remain vertical when clearer.
- Avoid unnecessary blank vertical space simply to separate short questions.
- Provide adequate workspace only where the mathematical task itself calls for substantial written work, tables, or graphs.
- For graphing questions, provide accurate coordinate grids with the required scale in the exam booklet.
- Keep answer-key content and compliance metadata off student-facing pages.

## 6. Student answer sheet and answer key

Every generated assessment version includes a student answer sheet and a paired answer key unless the request explicitly asks for a different format.

### Content

- The answer sheet contains **no problem statements**.
- Include the version identifier, **student name**, question numbers, concise part labels, point values, and appropriately sized answer lines/boxes.
- Do **not** include a section/course-section field.
- Follow the actual randomized or standardized numbering/order of that version.
- For Part III unit tests, each main question visibly totals **20 points** and multipart point values sum to 20.
- For Part IV diagnostics, practice finals, and official finals, each main question visibly totals **10 points** and multipart point values sum to 10.
- For a single-part question, show the question once with its full point value (`20 points` on a Part III unit test or `10 points` on a Part IV exam); do not invent a redundant A/1 subpart or a second point-value label beneath it.
- For graphing work performed directly on a grid in the exam booklet, the answer sheet may use a concise label such as `Graph (see booklet)` with its point value rather than duplicating the entire grid, unless a generation request says otherwise.

### Row geometry

- Left part labels/descriptors occupy a narrow left column; point values occupy a narrow right column.
- For multipart rows, the response line runs essentially the **full usable width between the left label and the right-aligned point value**.
- Do not leave a short isolated blank in the middle of a row.
- Use **solid horizontal rules only between main questions**.
- Use **dashed horizontal rules only between successive parts of the same main question**.
- Dashed rules appear only *between* parts: two parts -> one dashed rule; three parts -> two; four parts -> three; and so on.
- Do **not** draw a dashed rule after the final part of a multipart question.
- Do **not** draw any dashed internal separator for a single-part question.
- Never stack a dashed rule and a solid main-question rule beneath the same final response area.

### Key-first matched layout

- Build the **answer key first** as the canonical layout.
- Generate the student answer sheet from the same source/template so page breaks, row heights, spacing, line lengths, labels, point-value positions, and separator rules are geometrically identical.
- Preferred method: typeset the key answers and create the student version by hiding the answer text (for example, white text) while preserving dimensions.
- The answer key is a concise grading reference. When a test-specific rule requires essential method steps, checks, rejected candidates, or a graph feature, include that information compactly in the corresponding key area while preserving the matched layout.
- Extended worked solutions are not included by default; provide them separately only when explicitly requested.

## 7. Standard output package and duplex-safe printing

By default, deliver **one combined PDF per version** in this order:

1. Exam booklet
2. Student answer sheet
3. Answer key
4. Optional compliance report only when explicitly requested

Printing rules:

- Each included section begins on an **odd-numbered PDF page**, i.e. the front of a fresh physical sheet when printed duplex starting with page 1 as a front side.
- Insert completely blank padding pages wherever needed so a section never begins on the back side of the preceding section.
- Student answer sheet and answer key must always have the **same page count and matched geometry**.
- For a five-question unit test, keep the answer sheet and key to **one page each when practical**; if additional space is genuinely needed, use the same increased page count for both.
- For a ten-question diagnostic, practice final, or official final, use **two pages for the answer sheet and two pages for the key** unless a problem-specific graphical requirement makes that genuinely impractical; if so, preserve identical page count/geometry between sheet and key and maintain duplex-safe section starts.
- If a requested compliance report is included, it begins on a fresh front side after the answer key.
- If the user explicitly requests separate files or a different packaging order, follow that request instead.

## 8. Compliance reports and default behavior

- **Do not automatically include a compliance report, generation audit, institutional mapping report, or similar metadata.**
- All compliance machinery and verification requirements in this specification remain active internally on every generation.
- If a compliance report is explicitly requested, generate the detailed report specified later in this document and include it as instructor-only material.
- If asked for one test by name, generate only that assessment.
- If asked for every unit test, generate the nine Part III assessments. Do not silently add diagnostics or finals.
- If asked for a complete quarterly assessment batch, generate only the assessment families explicitly requested. Ask one concise question if it is unclear whether diagnostics or finals are included.
- If asked for multiple versions, apply every batch rule and create a separate standardized combined PDF for each version unless another format is requested.
- Do not revise the specification itself while generating tests. Flag a genuine impossibility or contradiction instead of quietly relaxing a rule.

# Part II. Course-level expectations

## 9. Shared expectations

- Both courses emphasize correct substitution, signed-number reasoning, complete written work, and checking answers when checking is mathematically appropriate.
- Both courses include polynomial operations and basic factoring, but the depth and application differ by course.
- Question values should support hand calculation and clear reasoning. Do not make calculator burden the source of difficulty.
- Equivalent-expression and equation-checking tasks should require numerical evidence and appropriately cautious conclusions.

## 10. TSM 098 profile

TSM 098 emphasizes foundational arithmetic and algebraic structure. Students work with signed numbers, ordinary numerical fractions, simpler expression evaluation, combining like terms and factors, distribution, polynomial operations, foundational factoring, linear equations, and linear systems.

- Arithmetic questions emphasize signed operations, division by zero, fraction reduction, and direct substitution.
- Fraction operations use numerical fractions rather than rational expressions.
- Polynomial multiplication includes binomial, trinomial, and larger products; this breadth is intentional.
- Factoring is limited to GCF, simple guess-and-check trinomials, and difference of squares unless a specific test says otherwise.
- Equation solving centers on linear equations and systems by substitution or elimination, including identities, contradictions, dependent systems, and inconsistent systems.
- Expression-comparison questions should use polynomial operations, distribution, combining like terms, or introductory factoring forms taught in TSM 098.

## 11. TSM 099 profile

TSM 099 extends the shared foundation into radicals, more complex evaluation, advanced trinomial factoring, rational expressions, quadratic equations, rational equations, and graphing of linear relationships.

- Arithmetic adds real and imaginary square roots, radical simplification, and more advanced substitution or formula evaluation.
- Polynomial multiplication on the TSM 099 Polynomials Test is limited to binomial-by-binomial multiplication; additional difficulty comes from nonmonic factoring and factoring by grouping.
- Rational-expression work includes simplification and all four operations, with factoring supporting rather than dominating the task.
- Equation solving includes quadratics by factoring, the quadratic formula, and square roots, plus rational equations and extraneous-solution checks.
- Graphing includes slope-intercept form, standard form through intercepts, systems by graphing, reading an equation from a graph, and writing a line through two points.

## 12. Assessment inventory

| **Course** | **Assessment**                           | **Primary domain**                                          |
|------------|------------------------------------------|-------------------------------------------------------------|
| TSM 098    | Arithmetic Test                          | Signed arithmetic, fraction reduction, and evaluation       |
| TSM 098    | Polynomials Test                         | Addition, subtraction, distribution, and multiplication     |
| TSM 098    | Fractions Test                           | Adding, subtracting, multiplying, and dividing fractions    |
| TSM 098    | Linear Equations and Linear Systems Test | Linear equations and algebraic systems                      |
| TSM 099    | Arithmetic Test                          | Fractions, radicals, and advanced evaluation                |
| TSM 099    | Polynomials Test                         | Binomial multiplication and factoring                       |
| TSM 099    | Rational Expressions Test                | Simplification and four operations                          |
| TSM 099    | Quadratic and Rational Equations Test    | Quadratic methods, rational equations, extraneous solutions |
| TSM 099    | Graphing Test                            | Graphing, systems, slope, and line equations                |
| TSM 098    | Diagnostic / Practice Final / Final      | Ten-question cumulative exam; six institutional items       |
| TSM 099    | Diagnostic / Practice Final / Final      | Ten-question cumulative exam; six institutional items       |

# Part III. Five-question unit-test specifications

**Generation rule:** Each assessment section begins with its five-question map. The detailed requirements that follow are mandatory construction and verification rules, not suggestions. Presentation and scoring follow Part I without changing the question content described here.

# 13. TSM 098 Arithmetic Test

**Assessment overview:** Five question units covering signed-number operations, numerical fraction reduction, two-variable evaluation, quadratic-trinomial evaluation, and numerical comparison of two algebraic expressions.

## Question-unit map

1. Signed-number operations - four parts
2. Simplifying numerical fractions - two parts
3. Evaluate one linear expression in x and y
4. Evaluate one quadratic trinomial at x = 10, x = -10, and x = 0
5. Compare two expressions at three supplied x-values

## Signed-number operations

Present four lettered parts in randomized order. Include exactly one item of each type below.

- **Division involving zero.** Use either n/0, whose answer is undefined, or 0/n, whose answer is 0, with n nonzero. Rotate forms; never use 0/0.
- **Double-negative subtraction.** Use a - (-b), with b positive. Rotate between a positive first value, which becomes positive plus positive, and a negative first value, which becomes an opposite-sign sum. Avoid a zero result.
- **Signed multiplication or division.** Use nonzero values and either one negative or two negatives. Rotate multiplication and exact division; keep facts manageable.
- **Complementary addition or subtraction.** Do not use a double negative. If the double-negative item becomes positive plus positive, use opposite signs that require subtracting absolute values. If it becomes negative plus positive, use two negative quantities that require adding absolute values and retaining a negative sign.

## Simplifying numerical fractions

- Use two parts and randomize their order.
- One fraction has a GCF equal to exactly one prime number, preferably 2, 3, 5, or 7; after one division, the result is in lowest terms.
- The other fraction has a GCF containing at least two distinct primes, such as 6, 10, 14, 15, 21, or 30; it may be reduced in one complete step or multiple valid steps.
- Use positive values, keep original numerator and denominator preferably below 150, and do not make the second result a whole number.

## Evaluate a linear expression in x and y

- Use a linear expression such as ax + by + c, with nonzero coefficients for x and y.
- Supply one integer value for each variable. Vary the signs of coefficients and inputs across versions.
- Include at least one meaningful signed-number issue and require the substituted numerical expression before evaluation.
- Use no exponents; keep the final value preferably between -100 and 100.

## Evaluate a quadratic trinomial

- Use the same standard-form trinomial ax^2 + bx + c for three parts: x = 10, x = -10, and x = 0.
- All three coefficients are nonzero integers; include at least one negative coefficient.
- At x = -10, require parentheses around the substituted value so (-10)^2 is handled correctly.
- Choose coefficients so the three results are distinct and preferably between -500 and 500.

## Compare two expressions by evaluation

- Place two TSM 098-level expressions on opposite sides of an equals sign and supply three distinct inputs: one positive, one negative, and 0.
- Use expression pairs involving pre/post polynomial multiplication, pre/post distribution and combining like terms, or expanded/factored forms using GCF, a simple monic trinomial, or difference of squares.
- Rotate among three outcomes: equal at all three inputs, equal at exactly one input, or equal at none. Do not reveal the outcome.
- For a matching-all-three version, use genuinely equivalent expressions. For other versions, use a plausible sign, coefficient, exponent, distribution, or like-term error.
- Provide a four-column table: x-value, left value, right value, and equality decision. The conclusion applies to the tested values; three matches are evidence consistent with equivalence, not a proof by themselves.

**Output:** Apply the standardized Part I output package. Compliance reporting is included only when explicitly requested, but every test-specific verification item above remains mandatory internally.

# 14. TSM 098 Polynomials Test

**Assessment overview:** Five question units covering polynomial addition, polynomial subtraction, monomial distribution, two levels of binomial multiplication, and one larger polynomial product.

## Question-unit map

1. Add two polynomials
2. Subtract two polynomials
3. Distribute a monomial through a polynomial
4. Multiply two binomials - two parts
5. Multiply two larger polynomials

## Add two polynomials

- Use two parenthesized polynomials with at least five nonzero terms each and at least six distinct exponents across the pair.
- Write both in the same descending exponent order; do not scramble the order.
- Omit at least one exponent entirely from one polynomial, without a zero placeholder, so at least one term has no like term in the other polynomial.
- Include multiple genuine like-term pairs. Keep the final polynomial at five or more nonzero terms when practical and avoid excessive cancellation.

## Subtract two polynomials

- Use P(x) - (Q(x)); Q(x) contains exactly three nonzero terms and exactly one internal plus sign and one internal minus sign.
- The leading subtraction must change an internal positive term to negative and an internal negative term to positive.
- Use at least three terms in P(x), at least two like-term pairs across the polynomials, descending order, and no nested parentheses.
- Require students to show distribution of -1 before combining like terms.

## Distribute a monomial

- Use ax^m(P(x)), where the outside monomial includes a numerical coefficient of absolute value 2-9 and a variable factor x or x^m.
- Use two, three, or four distinct-exponent terms inside, favoring three or four; include at least two variable terms and optionally a constant.
- Require coefficient multiplication, sign handling, and the product rule x^a times x^b = x^(a+b). Include at least one negative factor or term.
- Do not create like terms after distribution; keep resulting exponents preferably no greater than 8.

## Multiply two binomials

- Part (a) is monic: (x + a)(x + b), with varied sign patterns and a nonzero middle term. The result is a quadratic trinomial.
- Part (b) is nonmonic: (ax + b)(cx + d), with both variable coefficients having absolute value greater than 1, preferably 2-5. The result is a quadratic trinomial.
- Avoid difference-of-squares shortcuts and routine repetition of perfect-square trinomials. Require four partial products and combination of the middle terms.

## Larger polynomial multiplication

- Rotate among binomial x trinomial (six partial products), binomial x four-term polynomial (eight), and trinomial x trinomial (nine).
- Write both factors in descending order, use small coefficients and mixed signs, and create several like-term groups.
- Keep the final degree preferably no greater than 6 and the final answer at four or more nonzero terms when the structure permits.
- Do not use monomials or special products that bypass systematic distribution. This item must be clearly more involved than the binomial items.

**Output:** Apply the standardized Part I output package. Compliance reporting is included only when explicitly requested, but every test-specific verification item above remains mandatory internally.

# 15. TSM 098 Fractions Test

**Assessment overview:** Four core operation questions - one addition, subtraction, multiplication, and division - plus one randomly selected basic operation with no extra step.

## Question-unit map

1. Core addition with unlike denominators
2. Core subtraction with unlike denominators
3. Core multiplication with exactly three factors
4. Core division
5. One additional basic operation selected from the four operations

## General fraction controls

- Use positive numerical fractions only; no variables, decimals, mixed numbers, or complex fractions.
- Leave improper fractions as improper fractions and require every final answer in lowest terms.
- Randomize all five question units and do not identify the extra basic problem.

## Core addition and subtraction

- Both begin with different denominators and require a common denominator; keep the LCD preferably no greater than 60.
- Exactly one of the two combined results must require final reduction, with a manageable GCF greater than 1 and a non-whole final result.
- The other combined result must already be in lowest terms. Randomize which operation receives the final reduction.
- The subtraction result is positive and nonzero. Use clear subtraction notation and no negative fractions.

## Core multiplication and division

- The multiplication item always has exactly three factors. If it contains a whole number, use n times a/b times c/d; otherwise use three fractions.
- The division item is n divided by a/b, a/b divided by n, or a/b divided by c/d. Require rewriting as multiplication by the reciprocal.
- Across these two core items, exactly one contains a whole number written as a whole number. Randomize its location.
- Exactly one item is designed for manageable straight-across multiplication followed by one reduction; keep raw products preferably no greater than 250.
- Exactly one item is designed to reward cancellation before multiplication. After any reciprocal step, include at least one two-digit numerator and one two-digit denominator, preferably two cross-cancellations, and an uncanceled product preferably above 500. Keep original values generally no greater than 60.

## Additional basic operation

- Choose addition, subtraction, multiplication, or division with approximately equal frequency across a batch.
- For addition or subtraction, use an already-common denominator and an already-reduced nonzero result.
- For multiplication, use exactly two small fractions, no useful cross-cancellation, and an already-reduced product.
- For division, use exactly two small fractions; after the reciprocal, multiply straight across with no cancellation or final reduction.
- Do not use a whole number and do not make the answer 0 or 1.

**Output:** Apply the standardized Part I output package. Compliance reporting is included only when explicitly requested, but every test-specific verification item above remains mandatory internally.

# 16. TSM 098 Linear Equations and Linear Systems Test

**Assessment overview:** Two linear equations with unique solutions, two systems with unique integer solutions, and one hidden exceptional equation or system.

## Question-unit map

1. Linear equation with numerical fractions
2. Longer linear equation requiring two distributions
3. Basic system ready for direct substitution or elimination
4. General system requiring preparation
5. Hidden exceptional equation or system

## Directions and hidden exceptional case

- At the top, direct students to solve and check numerical answers by substitution into the original equation or both original system equations.
- Warn generally that an equation may have no solution or all real numbers and a system may have no solution or infinitely many solutions.
- Do not identify which question is exceptional. Exactly one question is exceptional on each version.

## Equation with numerical fractions

- Use at least two distinct numerical denominators with LCD preferably no greater than 24; no variable denominators or complex fractions.
- At least one numerator has more than one term. The intended first step is multiplying every term on both sides by the LCD.
- After clearing denominators, the equation is linear and has exactly one solution.

## Long distribution equation

- Use exactly two required distribution steps: one numerical coefficient, such as 3(2x - 5), and one stand-alone negative, such as -(4x + 7).
- Include terms outside both parentheses and preferably variable terms on both sides.
- Require distribution, combining like terms, moving terms, and dividing. Use integer coefficients in the original equation and no nested parentheses.

## Solution balance for the two ordinary equations

- Exactly one ordinary equation has a non-integer reduced rational solution; the other has an integer solution.
- Randomize which equation type has the fractional answer. Keep its denominator preferably 2-6 and numerator/denominator absolute values preferably no greater than 12.

## Basic system

- Rotate between direct substitution and direct elimination.
- For substitution, one variable is already isolated with coefficient 1 in a nonconstant expression; no rearrangement is needed.
- For elimination, one variable's coefficients are already opposites; adding immediately eliminates it.
- Use exactly one integer ordered-pair solution, preferably nonzero coordinates between -8 and 8, and require checking in both equations.

## General system

- Do not begin with an isolated variable or coefficients already equal/opposite.
- Require a preparatory step: multiply one or both equations for elimination, or rearrange before substitution.
- Prefer elimination as the cleaner method unless intentionally rotating to preparatory substitution. Use small multipliers and an integer ordered-pair solution between -8 and 8.

## Exceptional equation or system

- Rotate among: equation with no solution, equation true for all real numbers, inconsistent system with no solution, and dependent system with infinitely many solutions.
- For equations, variable terms cancel to a false or true numerical statement. For systems, elimination produces a contradiction or true statement.
- Make equivalent equations or expressions visibly different and substantial enough to require algebra; do not present obviously identical forms.

**Output:** Apply the standardized Part I output package. Compliance reporting is included only when explicitly requested, but every test-specific verification item above remains mandatory internally.

# 17. TSM 099 Arithmetic Test

**Assessment overview:** Five question units covering fraction reduction, real and imaginary roots, one-step radical simplification, advanced evaluation, and testing values in a rational equation.

## Question-unit map

1. Simplify two numerical fractions
2. Evaluate one real and one imaginary square root
3. Simplify one square root
4. Advanced order-of-operations or formula evaluation
5. Test three values in an equation containing two rational expressions

## Simplifying numerical fractions

Use the same two-part requirements as the TSM 098 Arithmetic Test: one fraction whose GCF is exactly one prime and one whose GCF contains at least two distinct primes. Randomize the parts, use positive manageable values, and finish in lowest terms.

## Evaluate square roots

- Use two randomized parts: the principal square root of a positive perfect square and the principal square root of the negative of a perfect square.
- The answers are a positive integer and ki, respectively. Do not use plus-or-minus notation because the task is evaluating a radical, not solving an equation.
- Use different absolute radicands, preferably from 16 through 144; do not use 0 or 1.

## Simplify a square root

- Use sqrt(k^2 p), where p is exactly 2, 3, or 5 and k is a small positive integer, preferably prime.
- Choose k^2 as the greatest nontrivial perfect-square factor so the radical simplifies directly to k sqrt(p) in one step.
- Use no variables, outside coefficient, fraction, negative radicand, or repeated simplification.

## Advanced evaluation - randomized format

Choose one of the following formats for each version and distribute the formats evenly across a large batch.

- **Standard-form quadratic polynomial.** Evaluate ax^2 + bx + c at one positive and one negative integer input, using the same polynomial in two parts.
- **Factored quadratic polynomial.** Evaluate a(x - h)(x - k) or an equivalent two-binomial product at one positive and one negative integer input, using the same expression in two parts.
- **Quadratic formula.** Supply values for a, b, and c and require substitution into x = [-b +/- sqrt(b^2 - 4ac)]/(2a). Choose a nonnegative perfect-square discriminant so every resulting solution is rational. Solutions may be positive or negative, integers or reduced fractions.
- For polynomial formats, include x^2, use inputs preferably of absolute value 2-4, require parentheses for a negative input, and keep final values preferably within 100 in absolute value.
- For the quadratic-formula format, keep coefficients small, avoid unnecessary common factors, require both formula branches unless the discriminant is 0, and reduce fractional solutions.
- Keep the three formats comparable in total order-of-operations demand.

## Test values in a rational equation

- Give one rational expression on each side and exactly three integer x-values. Students evaluate each side separately; they do not solve, factor, simplify symbolically, or cross-multiply.
- Use simple linear or quadratic numerators, constant or linear denominators, and at least one occurrence of x^2.
- No supplied value may make a denominator zero. Every numerator must divide evenly by its denominator at every supplied input, so all six evaluated values are integers.
- Rotate among three designs: all three inputs work and the equation is genuinely an identity; exactly one input works; none of the supplied inputs works, preferably while another unsupplied solution exists.
- Provide columns for x, left value, right value, and solution decision. Require a cautious conclusion: a found equality gives a solution; one failure disproves an identity; three successes are consistent with an identity but do not prove it by substitution alone; no tested success does not prove that no solution exists.

**Output:** Apply the standardized Part I output package. Compliance reporting is included only when explicitly requested, but every test-specific verification item above remains mandatory internally.

# 18. TSM 099 Polynomials Test

**Assessment overview:** Five numbered question units and seven tasks covering binomial multiplication, GCF factoring, basic factoring patterns, nonmonic guess-and-check factoring, prime recognition, and one demanding factoring-by-grouping item.

## Question-unit map

1. Multiply two linear binomials
2. Factor out a greatest common factor
3. Basic factoring - monic trinomial and difference of squares
4. Two nonmonic trinomials - one factorable and one prime
5. Factor-rich nonmonic trinomial requiring the ac-method and grouping

## Multiply two binomials

- Use (ax + b)(cx + d) in one variable with small integers and varied signs.
- Require multiplication and combination of middle terms. Prefer a quadratic trinomial result.
- Do not make this a special-product or factoring problem.

## Factor out a GCF

- Use a three- or four-term polynomial whose complete GCF contains a variable.
- The GCF must contain both a numerical factor greater than 1 and a variable, or a variable raised to at least the second power. Alternate patterns across versions.
- After removing the complete GCF, prefer an inside polynomial that requires no substantial additional factoring.

## Basic factoring - two parts

- Part (a): a readily factorable monic trinomial x^2 + bx + c with small integer factor constants and few factor pairs. Vary sign patterns and avoid constant repetition of perfect squares.
- Part (b): a straightforward difference of squares A^2 - B^2, with leading coefficient 1 or a perfect-square coefficient greater than 1. Do not require a preliminary GCF or further factoring.

## Nonmonic trinomials with small search spaces - two parts

- Both are primitive ax^2 + bx + c with a greater than 1. One factors over the integers and one is prime; randomize which is Part (a).
- Use a small factor search: |ac| preferably has no more than four positive factor pairs and no more than three prime factors counted with multiplicity.
- The factorable item yields two integer linear factors and is not a difference of squares or perfect square.
- The prime item has a discriminant that is not a nonnegative perfect square. Direct students to factor completely or write prime.

## Factor-rich nonmonic trinomial

- Use a primitive, factorable ax^2 + bx + c with a greater than 1, no GCF, and no special-product shortcut.
- Choose |ac| with many possibilities, preferably at least eight positive unordered factor pairs; suitable products include 72, 96, 120, and 144.
- Keep a and |c| individually preferably no greater than 15. Choose the successful factor pair so it is not the first obvious guess.
- Require calculation of ac, identification of two integers with product ac and sum b, splitting the middle term, and factoring the four-term result by grouping. The key must show that method.

**Output:** Apply the standardized Part I output package. Compliance reporting is included only when explicitly requested, but every test-specific verification item above remains mandatory internally.

# 19. TSM 099 Rational Expressions Test

**Assessment overview:** Five questions: simplify, add, subtract, multiply, and divide rational expressions, with factoring distributed across the version and exactly one final cancellation among addition and subtraction.

## Question-unit map

1. Simplify a rational expression
2. Add two rational expressions
3. Subtract two rational expressions
4. Multiply two rational expressions
5. Divide two rational expressions

## Global construction rules

- Every question requires at least one factoring step. Use one variable, integer coefficients, and factoring over the integers.
- Across the test include: difference of squares, numerical GCF, common variable factor, monic trinomial, and exactly one required nonmonic trinomial.
- The one nonmonic trinomial has a small leading coefficient, preferably 2 or 3. No other required trinomial may have leading coefficient other than 1.
- Do not factor or expand beyond degree 2. Already-factored products may have greater combined degree, but students multiply no more than two linear binomials.
- At least one item reduces numerical coefficients without complete numerical cancellation, such as 6/9 to 2/3.
- Do not require excluded values unless specifically requested in the generation request; the key may note them for verification.

## Simplifying

- Present one unfactored rational expression. At least one numerator or denominator requires factoring and at least one polynomial factor cancels.
- The final answer must differ from the original expression.

## Adding and subtracting

- Each uses two expressions with initially different denominators; at least one denominator requires factoring before identifying the LCD.
- Require a single combined rational expression and make subtraction signs unambiguous.
- Exactly one of the two resulting numerators factors and cancels with the denominator. The other has no final common factor. Randomize which operation has the final cancellation.

## Multiplying and dividing

- Each has at least one numerator or denominator requiring factoring and at least one polynomial cancellation.
- The division item explicitly requires rewriting as multiplication by the reciprocal.
- Do not require multiplying anything more complicated than two linear binomials.

**Output:** Apply the standardized Part I output package. Compliance reporting is included only when explicitly requested, but every test-specific verification item above remains mandatory internally.

# 20. TSM 099 Quadratic and Rational Equations Test

**Assessment overview:** Three quadratic equations using three distinct methods and two rational equations that produce three total candidate solutions with exactly one extraneous solution.

## Question-unit map

1. Quadratic equation solved by factoring
2. Quadratic equation requiring the quadratic formula
3. Quadratic equation solved by taking square roots
4. Rational equation that becomes quadratic
5. Rational equation that becomes linear

## Quadratic solved by factoring

- Require a genuine quadratic binomial or trinomial factorization, not merely factoring out x.
- The equation may require moving terms to one side and must factor into integer linear factors with two real solutions.
- Factoring must be the clearly natural method.

## Quadratic formula

- Use a standard-form quadratic that does not factor over the integers and is not easily solved by square roots.
- The discriminant is positive but not a perfect square, giving two real irrational solutions. Keep it manageable and require radical simplification when possible.

## Square-root method

- Use a form such as a(x - h)^2 = k. Besides taking positive and negative square roots, require only one or two algebraic steps.
- Do not require expanding the squared binomial. Choose a positive radicand and two simple real solutions; a perfect-square radicand is acceptable and preferred for emphasis.

## Rational equation becoming quadratic

- After multiplying every term by the LCD, the result is a factorable quadratic with exactly two candidate solutions.
- Either exactly one candidate is extraneous or both are valid, depending on the linear rational equation.

## Rational equation becoming linear

- After clearing denominators, the result is linear with exactly one candidate solution.
- That candidate is valid unless this question carries the version's one extraneous solution.

## Extraneous solutions and factoring

- Across the two rational equations there are exactly three candidates: two from the quadratic result and one from the linear result. Exactly one is extraneous because it makes an original denominator zero; the other two are valid.
- At least one denominator in each rational equation requires factoring before finding the LCD.
- Across the pair require at least three types from: difference of squares, numerical GCF, common variable factor, monic trinomial, and nonmonic trinomial.
- Do not factor beyond degree 2, use sums/differences of cubes, or require four-term grouping. Direct students to list excluded values and check every candidate in the original equation.

**Output:** Apply the standardized Part I output package. Compliance reporting is included only when explicitly requested, but every test-specific verification item above remains mandatory internally.

# 21. TSM 099 Graphing Test

**Assessment overview:** Five questions covering two forms of graphing a line, solving a system by graphing, writing an equation from a displayed line, and finding a line through two points.

## Question-unit map

1. Graph a line from slope-intercept form
2. Graph a line from standard form using intercepts
3. Solve a linear system by graphing
4. Write a slope-intercept equation from a graph
5. Find the slope-intercept equation through two points

## Global graphing rules

- Every grid runs from -10 to 10 on both axes with equal scale and one unit per square. Axes are darker than gridlines, numbered clearly, labeled x and y, and include arrowheads.
- All defining points, intercepts, and intersections lie within the window. Prefer important coordinates within -8 to 8 and system intersections within -6 to 6.
- Across all lines include at least two positive and two negative slopes and at least one simple fractional slope. Avoid vertical and horizontal lines unless specifically requested.
- Do not repeat slopes unnecessarily. Use exact graphs, not visual approximations.

## Graph from slope-intercept form

- Give y = mx + b with integer b between -5 and 5 and manageable nonzero m: an integer or simple fraction such as 1/2, 2/3, or 3/2 with either sign.
- The line contains at least two visible lattice points. Provide a blank grid and no table of values.

## Graph from standard form

- Give Ax + By = C with nonzero integer A and B and no unnecessary common factor.
- Both x- and y-intercepts are nonzero integer coordinates, preferably absolute values 2-8. Require students to find both and graph through them.

## Solve a system by graphing

- Use two nonparallel, nonidentical lines with one integer intersection, preferably both coordinates nonzero within -6 to 6.
- Each line has at least two easily plotted lattice points and the lines meet at a visibly clear angle.
- Require both lines on the same blank grid and the solution as an ordered pair. State that algebra alone is insufficient.

## Write an equation from a graph

- Display one exact line, no equation, with a clear integer y-intercept and at least one additional countable lattice point.
- Use a nonzero integer or simple fractional slope with numerator and denominator no greater than 4 in absolute value.
- The two useful points may be marked but not coordinate-labeled. Require y = mx + b.

## Equation through two points

- Give two distinct integer-coordinate points, neither the y-intercept, preferably within -8 to 8 and with different x-values.
- The slope is a manageable integer or reduced fraction; coordinate differences are no greater than 6 in absolute value.
- Choose points producing an integer y-intercept between -6 and 6. Require the slope formula, determination of b, and final slope-intercept form.

**Output:** Apply the standardized Part I output package. Compliance reporting is included only when explicitly requested, but every test-specific verification item above remains mandatory internally.

# Part IV. Ten-question diagnostics and finals

## 22. Exam families and shared architecture

Each course has one ten-question cumulative architecture used for three assessment modes:

- **DIAGNOSTIC:** beginning-of-quarter pre-assessment parallel to the course final. Default order is RANDOMIZED.
- **PRACTICE_FINAL:** practice version parallel to the official final. Default order is RANDOMIZED.
- **OFFICIAL_FINAL:** summative final used for institutional reporting. Order is STANDARDIZED when the instructor supplies or has embedded an official ten-position item map.

Every version contains exactly ten numbered questions:

- Six institutional-assessment questions: three questions for SLO 1 and three questions for SLO 2.
- Four supplemental questions selected from the applicable Part III unit-test specifications to broaden topic coverage.

The diagnostic and final for a course must be parallel in assessed constructs, workload, and difficulty. They must not reuse identical numerical content. A practice final must also be parallel but numerically distinct.

## 23. Ordering modes

- **RANDOMIZED:** Shuffle all ten question units. Keep any multipart unit together. Use for diagnostics and practice finals unless the request states otherwise.
- **STANDARDIZED:** Place all ten question units according to the instructor's official position map so item numbers are comparable for item analysis. Use for an official final only when the position map is present in this specification or supplied in the request.
- The semantic institutional IDs below, such as I098-1, do not by themselves establish official item numbers.
- If asked to create an OFFICIAL_FINAL and no official position map is available, ask for the map. Do not guess, use the listed bank order as a substitute, or randomize.
- When a standardized position contains a supplemental question, follow any topic-family restriction attached to that position. If no such restriction has been supplied, ask for clarification before creating an official final.

## 24. Institutional-item generation protocol

For each institutional ID, select one of the four listed bank examples as the structural model. The bank examples are archetypes, not questions to repeat indefinitely.

Allowed microvariation:

- Change small integer coefficients, constants, and signs while preserving the same algebraic structure.
- Preserve the required method, number of meaningful steps, answer type, factoring burden, cancellation count, and approximate coefficient size.
- Preserve all explicit restrictions, including monic versus nonmonic form, factorability, discriminant class, denominator structure, and presence or absence of extraneous solutions.

Forbidden variation:

- Do not replace the question with a merely related skill.
- Do not add an extra distribution, factoring stage, cancellation stage, exceptional case, or domain complication.
- Do not change a unique-solution item into an identity, contradiction, multiple-solution equation, or extraneous-solution item.
- Do not use the exact same coefficients in two versions in the same batch.
- Do not repeatedly favor one bank archetype. Distribute A-D as evenly as practical across a batch.

The internal generation record must track the institutional ID and bank archetype used and verify the essential solution and binary correct-answer criterion suitable for institutional reporting. Student copies must not display institutional IDs or archetype labels. The matched answer key should remain a grading document aligned with the student answer sheet. If a compliance report is explicitly requested, that report must expose the institutional ID/archetype mapping and reporting criterion described in Section 30.

## 25. TSM 098 institutional-assessment bank

TSM 098 SLO 1: Simplify and multiply polynomial expressions.  
TSM 098 SLO 2: Solve single-variable linear equations.

### I098-1 - Multiply binomials

Required controls: Multiply two linear binomials. Do not use a difference-of-squares product. Require distribution and combination of middle terms.

- A. `(2x - 5)(x + 2)`; answer `2x^2 - x - 10`.
- B. `(3x + 4)(x - 5)`; answer `3x^2 - 11x - 20`.
- C. `(2x + 3)(3x - 4)`; answer `6x^2 + x - 12`.
- D. `(x - 6)(4x + 1)`; answer `4x^2 - 23x - 6`.

### I098-2 - Distribute a monomial

Required controls: The outside monomial contains a numerical factor and a variable factor. Use a three-term polynomial inside. Require coefficient multiplication and the product rule for exponents.

- A. `3x^4(x^2 - 4x + 5)`; answer `3x^6 - 12x^5 + 15x^4`.
- B. `-2x^3(3x^2 + x - 4)`; answer `-6x^5 - 2x^4 + 8x^3`.
- C. `4x^2(2x^3 - 5x + 1)`; answer `8x^5 - 20x^3 + 4x^2`.
- D. `-3x(2x^3 - 4x^2 + 5)`; answer `-6x^4 + 12x^3 - 15x`.

### I098-3 - Add polynomials and combine like terms

Required controls: Use addition only. Do not require distribution; superfluous outer parentheses are allowed. Include at least two unlike term types and at least two genuine like-term combinations. Preserve descending exponent order inside each polynomial.

- A. `(3x^2 + 5x - 2) + (-x^2 - 6x - 1)`; answer `2x^2 - x - 3`.
- B. `(4x^3 - 2x^2 + 5x - 7) + (3x^2 - x + 4)`; answer `4x^3 + x^2 + 4x - 3`.
- C. `(2x^4 + 3x^2 - 5) + (-x^4 + 6x - 2)`; answer `x^4 + 3x^2 + 6x - 7`.
- D. `(5x^3 - x + 8) + (-2x^3 + 4x^2 - 6)`; answer `3x^3 + 4x^2 - x + 2`.

### I098-4 - Linear equation without parentheses

Required controls: Use four to six visible terms, no parentheses, and exactly one solution. Use variable terms on both sides. Keep the solution an integer or a reduced fraction with a small denominator.

- A. `2x - 3 = -4x + 5 + x`; answer `x = 8/5`.
- B. `3x + 7 = 2x - 5 + 4`; answer `x = -8`.
- C. `5x - 4 = -2x + 9 + x`; answer `x = 13/6`.
- D. `-3x + 8 = 4x - 6 - 2x`; answer `x = 14/5`.

### I098-5 - Exceptional linear equation

Required controls: Require at least one distribution. The result is either no solution or all real numbers. Balance the two outcomes across a batch. Do not reveal the outcome type in the student prompt.

- A. `2(x - 2) + 5 = 3x - (x + 2)`; answer `no solution`.
- B. `3(x + 2) - 4 = 3x + 2`; answer `all real numbers`.
- C. `4(x - 1) + 7 = 2(2x + 3) - 3`; answer `all real numbers`.
- D. `5(x - 2) + 3 = 5x - 4`; answer `no solution`.

### I098-6 - Linear equation containing fractions

Required controls: Use at least two distinct numerical denominators, at least one numerator with more than one term, and exactly one solution. The intended first move is multiplication by the LCD. Keep the LCD manageable.

- A. `(2/3)x + 3/2 = (4x - 6)/9`; answer `x = -39/4`.
- B. `x/4 + 2/3 = (3x + 2)/6`; answer `x = 4/3`.
- C. `(3x - 1)/5 - x/2 = 7/10`; answer `x = 9`.
- D. `(2x + 5)/6 + x/4 = 3/2`; answer `x = 8/7`.

## 26. TSM 099 institutional-assessment bank

TSM 099 SLO 1: Factor polynomials and perform operations on rational expressions.  
TSM 099 SLO 2: Solve quadratic and rational equations.

### I099-1 - Factor a nonmonic trinomial

Required controls: Use a primitive, factorable quadratic trinomial with no GCF and leading coefficient greater than 1. Keep the factor search comparable to the examples. Do not use a difference of squares or perfect-square trinomial.

- A. `8x^2 - 22x + 15`; answer `(4x - 5)(2x - 3)`.
- B. `6x^2 + x - 2`; answer `(3x + 2)(2x - 1)`.
- C. `10x^2 - 19x + 6`; answer `(5x - 2)(2x - 3)`.
- D. `12x^2 + 11x - 5`; answer `(3x - 1)(4x + 5)`.

### I099-2 - Multiply rational expressions

Required controls: At least two polynomial components require factoring and at least two pairs of polynomial factors cancel. Use one variable and factor only through degree 2. Require one multiplication sign and no addition or subtraction between rational expressions.

- A. `[(x^2 - 9)/(x^2 - 2x - 35)] * [(x + 5)/(x^2 + 3x)]`; answer `(x - 3)/[x(x - 7)]`.
- B. `[(x^2 - 4)/(x^2 + x - 6)] * [(x - 2)/(x^2 + 5x + 6)]`; answer `(x - 2)/(x + 3)^2`.
- C. `[(x^2 - 16)/(x^2 + x - 12)] * [(x - 3)/(x^2 - 4x)]`; answer `1/x`.
- D. `[(2x^2 - 8)/(x^2 - 5x + 6)] * [(x - 3)/(x^2 + 2x)]`; answer `2/x`.

### I099-3 - Add rational expressions

Required controls: Use two rational expressions with different denominators. At least one denominator requires factoring before identifying the LCD. Keep numerators constant and denominators quadratic, matching the source examples. In this institutional bank, the combined numerator must not cancel with the denominator; do not add a final cancellation stage.

- A. `3/(x^2 - x) + 4/(x^2 - 1)`; answer `(7x + 3)/[x(x - 1)(x + 1)]`.
- B. `2/(x^2 + 3x) + 5/(x^2 + 5x + 6)`; answer `(7x + 4)/[x(x + 2)(x + 3)]`.
- C. `4/(x^2 - 4) + 3/(x^2 + x - 6)`; answer `(7x + 18)/[(x - 2)(x + 2)(x + 3)]`.
- D. `5/(x^2 - 2x) + 2/(x^2 - 4x + 4)`; answer `(7x - 10)/[x(x - 2)^2]`.

### I099-4 - Solve a monic quadratic by factoring

Required controls: The quadratic has leading coefficient 1 after rearranging and combining. It factors into integer linear factors and has two real integer solutions. Factoring must be the natural method.

- A. `x^2 = -5x - 6`; answers `x = -2, -3`.
- B. `x^2 + 7x = -12`; answers `x = -3, -4`.
- C. `x^2 - 5x = 14`; answers `x = 7, -2`.
- D. `x^2 + 2 = 3x`; answers `x = 1, 2`.

### I099-5 - Solve a nonfactorable quadratic with the quadratic formula

Required controls: After rearranging and combining, use a quadratic with a positive non-perfect-square discriminant. The equation has two real irrational solutions. Do not use a quadratic that factors over the integers or is naturally solved by square roots.

- A. `7x^2 - 6 = x + 4`; answers `x = (1 +/- sqrt(281))/14`.
- B. `3x^2 = x + 1`; answers `x = (1 +/- sqrt(13))/6`.
- C. `2x^2 + 3x = 1`; answers `x = (-3 +/- sqrt(17))/4`.
- D. `4x^2 + x = 2`; answers `x = (-1 +/- sqrt(33))/8`.

### I099-6 - Solve a rational equation with one valid solution

Required controls: Use at least two visibly different denominators, with at least one requiring factorization. Clearing denominators produces a linear equation with exactly one candidate. The candidate is valid; there are no multiple or extraneous solutions. Require checking in the original equation.

- A. `36/(3x - 15) + 1/(x - 5) = 13/3`; answer `x = 8`.
- B. `20/(2x - 6) + 3/(x - 3) = 13/2`; answer `x = 5`.
- C. `18/(3x + 6) - 1/(x + 2) = 5/2`; answer `x = 0`.
- D. `28/(4x - 8) + 2/(x - 2) = 9/4`; answer `x = 6`.

## 27. Four supplemental questions - general selection algorithm

These are coverage-balancing questions, not four unrestricted random draws.

For each exam version:

1. Mark the skills already represented by the six institutional questions.
2. Build an eligible pool from the course's Part III unit-test question types.
3. Remove a candidate if it substantially duplicates an institutional question, is a one-step recognition/direct-operation problem, ordinarily requires four or more major transformations, or depends on an exceptional trick.
4. Select four candidates that fill the largest coverage gaps. Use at least three distinct topic families among the four when possible.
5. Keep the four questions mutually complementary. Do not choose four variants of the same operation or unit.
6. Across a batch, rotate eligible types evenly while keeping total workload comparable.

Definition of a meaningful step:

- A meaningful step is a major mathematical decision or transformation, such as substituting supplied values, finding an LCD, rewriting division as multiplication, factoring a quadratic, clearing denominators, graphing one line from usable information, or back-substituting after elimination.
- Individual arithmetic products, sign calculations, and simplification within one transformation do not each count as separate steps.
- Target two meaningful steps. Three are acceptable when natural. Reject a question requiring only one meaningful step or ordinarily requiring four or more.

Difficulty controls:

- Use standard representative forms from the applicable unit-test section.
- Use manageable values and familiar structures. Do not use trick questions, rare edge cases, unnecessarily large numbers, long searches, or hidden exceptional behavior.
- A multipart question is allowed only when its complete workload remains comparable to one ordinary two- or three-step question.
- Solve and step-count every candidate before accepting it.

## 28. TSM 098 supplemental coverage rules

The six institutional questions already emphasize polynomial operations and single-variable linear equations. Therefore the four supplemental questions should primarily repair coverage in these families:

- Arithmetic and expression evaluation from the TSM 098 Arithmetic Test.
- Numerical fraction operations from the TSM 098 Fractions Test.
- Linear systems from the TSM 098 Linear Equations and Linear Systems Test.
- A fourth underrepresented standard skill from those families or, when needed for balance, polynomial subtraction or another Part III skill not duplicated by the institutional items.

Selection targets:

- Include at least one numerical-fraction question.
- Include at least one linear-system question with one integer ordered-pair solution.
- Include at least one arithmetic or substitution/evaluation question.
- Choose the fourth question to maximize coverage without violating the two- or three-step limit.
- Prefer a basic system already arranged for substitution or elimination. Use the more general preparatory system only if its complete solution remains within three meaningful steps.
- Do not use another multiply-binomials, distribute-monomial, add-polynomials, or single-variable-equation question unless the instructor explicitly requests intentional repetition.

## 29. TSM 099 supplemental coverage rules

The six institutional questions already cover one nonmonic factorization, multiplication and addition of rational expressions, quadratic factoring, the quadratic formula, and one rational equation. Therefore prioritize:

- Graphing and writing linear equations from the TSM 099 Graphing Test.
- Radical simplification or advanced evaluation from the TSM 099 Arithmetic Test.
- The square-root method for a quadratic equation.
- Rational-expression simplification, subtraction, or division, or a polynomial skill not already duplicated by the institutional items.

Selection targets:

- Include at least one graphing or line-writing question; prefer two different graphing-family questions when the other two questions still broaden coverage.
- Include at least one arithmetic, radical, or evaluation question.
- Use the remaining positions for the square-root quadratic method or an uncovered standard rational-expression/polynomial operation.
- Avoid factor-rich grouping items when they would require a long factor-pair search.
- Avoid an additional quadratic-formula, quadratic-by-factoring, rational-expression addition/multiplication, or rational-equation question unless explicitly requested.

## 30. Institutional reporting controls

- The six institutional questions correspond to SLO 1 and SLO 2, three questions each.
- Institutional reporting records each assessment question as correct or incorrect. If partial credit is awarded instructionally, the instructor applies judgment when converting the result to the binary institutional report.
- Questions may technically be free response or multiple choice. Default to free response unless the generation request asks for multiple choice.
- The four supplemental questions are not institutional-reporting items unless the instructor explicitly states otherwise.
- Maintain an internal mapping for each institutional ID, archetype letter, actual item number, SLO, final answer, and correct/incorrect scoring criterion.
- **If and only if a compliance report is explicitly requested**, the report must list that institutional mapping along with the relevant supplemental selections and version-specific constraint checks.

# Part V. Final pre-delivery audit for any generated batch

Before returning tests created from this guide, the generating system must confirm all of the following internally whether or not an audit report is requested.

- The requested assessment names and number of versions are correct.
- Every Part III unit-test version contains exactly five numbered question units. Every Part IV exam version contains exactly ten numbered question units. Required multipart structures remain intact.
- Every Part III unit-test main question is worth **20 points** and each Part III test totals **100 points**; every Part IV exam main question is worth **10 points** and each Part IV exam totals **100 points**. Multipart point values sum correctly to the applicable main-question value.
- Question order follows the correct mode: randomized for unit tests, diagnostics, and practice finals unless otherwise requested; standardized for an official final only when the official position map is available. Numerical content varies across versions without violating constraints.
- Version identifiers follow the timestamp convention `YYYYMMDDHHMM`, with `.1`, `.2`, `.3`, etc. only for multiple versions generated together.
- Every diagnostic or final has exactly six institutional items and four coverage-balancing supplemental items.
- Institutional archetypes are distributed fairly across a batch, and microvariation has not altered the measured construct or difficulty.
- Every problem has been solved independently and checked for unintended behavior.
- Student copies reveal no hidden roles, intended methods, exceptional locations, institutional IDs, or compliance metadata.
- Exam booklets are compact and omit point values by default.
- Student answer sheets contain no problem statements and no section field.
- Answer sheets and keys use matched key-first geometry, full-width response lines, solid main-question separators, dashed internal-part separators, and no redundant separator after a final part.
- Answer keys include the required essential steps, checks, rejected candidates, and graph features when test-specific rules require them.
- The default combined PDF is duplex-safe and ordered exam booklet -> student answer sheet -> answer key.
- A compliance report is **not** included unless explicitly requested.
- If a compliance report is requested, it identifies every required randomized option, institutional mapping, supplemental selection, and version-specific constraint needed to certify the generated assessment.
- Formatting is readable, notation is unambiguous, graphs are exact, and no answer-key content appears visibly on a student page.

**Source basis:** This guide compiles the instructor's assessment-design specifications, the cross-listed TSM 098-099 curriculum schedule, and the institutional TSM Assessment Procedure. It is intended to be reused as a controlling prompt for future AI-generated assessment batches.