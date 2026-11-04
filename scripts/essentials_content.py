"""Original recall questions and worked examples for the course essentials pages.

Each entry contains question | answer pairs, then --- and problem | worked steps.
A tilde separates worked steps. Inline TeX is converted to native MathML at build time.
"""
CONTENT = {}

def add(course, number, text):
    questions, examples = text.strip().split('\n---\n')
    def pairs(block):
        return [tuple(part.strip() for part in line.split(' | ', 1))
                for line in block.strip().splitlines() if line.strip()]
    CONTENT[(course, number)] = {
        'questions': pairs(questions),
        'examples': [(q, a.split(' ~ ')) for q, a in pairs(examples)]}

add('tsm','1',r'''
What does it mean for a to divide b? | b is a whole-number multiple of a, with a nonzero.
How can multiplication check a division? | Multiply the quotient by the divisor; include any remainder.
How do you test divisibility by 3? | Add the digits; the sum must be divisible by 3.
How do you test divisibility by 2, 5, and 10? | The last digit is even; 0 or 5; and 0, respectively.
Dividing by 3 and then by 4 equals dividing by what? | By 12, the product of the divisors.
---
Compute 144 divided by 12 using successive division. | Divide by 3: 144 ÷ 3 = 48. ~ Divide by 4: 48 ÷ 4 = 12. ~ Check: 12 × 12 = 144.
Is 234 divisible by 6? Explain. | A number divisible by both 2 and 3 is divisible by 6. ~ 234 ends in an even digit, and 2 + 3 + 4 = 9 is divisible by 3. ~ Therefore 234 is divisible by 6; 234 ÷ 6 = 39.
''')
add('tsm','2',r'''
What is a prime number? | An integer greater than 1 with exactly two positive divisors: 1 and itself.
Is 1 prime? | No; it has only one positive divisor.
What is a composite number? | An integer greater than 1 that is not prime.
What is prime factorization? | Writing an integer greater than 1 as a product of primes.
How do you know a factor tree is finished? | Every factor at its ends is prime.
---
Find the prime factorization of 84. | 84 = 2 × 42 = 2 × 2 × 21. ~ 21 = 3 × 7, so \(84=2^2\cdot3\cdot7\). ~ Check: 4 × 3 × 7 = 84.
Find the prime factorization of 90. | 90 = 9 × 10. ~ Factor each part: 9 = 3 × 3 and 10 = 2 × 5. ~ Thus \(90=2\cdot3^2\cdot5\).
''')
add('tsm','3',r'''
How do you add numbers with opposite signs? | Subtract their absolute values and use the sign of the number with larger absolute value.
How do you subtract a signed number? | Add its opposite.
What sign results when multiplying two negative numbers? | Positive.
What sign results when dividing numbers with different signs? | Negative.
What is the difference between 0 ÷ 5 and 5 ÷ 0? | 0 ÷ 5 = 0; division by zero is undefined.
---
Evaluate −8 − (−3) + 2. | Subtracting −3 means adding 3. ~ −8 + 3 + 2 = −5 + 2 = −3.
Evaluate (−24) ÷ (−6), and explain why 7 ÷ 0 is undefined. | Equal signs give a positive quotient: (−24) ÷ (−6) = 4. ~ A quotient 7 ÷ 0 would require a number q with 0 × q = 7. ~ No such number exists.
''')
add('tsm','4',r'''
What makes two fractions equivalent? | They represent the same number.
What operation preserves a fraction's value? | Multiply or divide numerator and denominator by the same nonzero number.
What does simplest form mean? | The numerator and denominator have no common factor greater than 1.
Why can you not cancel a number appearing in only one term of a sum? | Cancellation divides entire numerator and denominator by a common factor.
What must be true of a denominator? | It must not equal zero.
---
Simplify 42/60. | The greatest common divisor of 42 and 60 is 6. ~ Divide both by 6: 42/60 = 7/10. ~ 7 and 10 share no factor greater than 1.
Simplify −18/24 and 0/9. | Divide −18 and 24 by 6: −18/24 = −3/4. ~ Zero divided by a nonzero number equals zero, so 0/9 = 0.
''')
add('tsm','5',r'''
What does a positive integer exponent count? | The number of equal factors of the base.
Why do parentheses matter in a negative base? | They determine whether the negative sign is included in the repeated factor.
What does the principal square root mean? | The nonnegative number whose square equals the radicand.
What is a perfect square? | A number equal to an integer squared.
What is \(a^0\) when a is nonzero? | 1.
---
Evaluate \(-3^4\) and \((-3)^4\). | Exponents precede a leading negative: \(-3^4=-(81)=-81\). ~ With parentheses, four negative factors give \((-3)^4=81\).
Evaluate \(\sqrt{144}\), \(-\sqrt{49}\), and \(2^5\). | The nonnegative square root of 144 is 12. ~ The negative sign stays outside: \(-\sqrt{49}=-7\). ~ Five factors of 2 give \(2^5=32\).
''')
add('tsm','6',r'''
What factor should you look for when simplifying a square root? | A perfect-square factor greater than 1.
For nonnegative a and b, how can \(\sqrt{ab}\) be separated? | As \(\sqrt a\sqrt b\).
When is a numerical square root fully simplified? | No perfect-square factor greater than 1 remains inside.
Can \(\sqrt{a+b}\) generally be split into \(\sqrt a+\sqrt b\)? | No.
How do you combine like radicals? | Add their coefficients while keeping the common radical.
---
Simplify \(\sqrt{72}\). | 72 = 36 × 2. ~ \(\sqrt{72}=\sqrt{36}\sqrt2=6\sqrt2\).
Simplify \(3\sqrt{12}-\sqrt{27}\). | \(\sqrt{12}=2\sqrt3\) and \(\sqrt{27}=3\sqrt3\). ~ Substitute: \(6\sqrt3-3\sqrt3=3\sqrt3\).
''')
add('tsm','7',r'''
What is the first priority in order of operations? | Evaluate grouped expressions, working from the inside out.
Which comes first: multiplication or division? | Neither has priority; work left to right.
Which comes first: addition or subtraction? | Neither has priority; work left to right.
How should you substitute a negative value into a power? | Put the substituted negative value in parentheses.
How does a fraction bar group an expression? | It groups the entire numerator and the entire denominator.
---
Evaluate \(18-2(3+1)^2\). | Parentheses give 4; squaring gives 16. ~ Multiply: 2 × 16 = 32. ~ Subtract: 18 − 32 = −14.
Evaluate \(2x^2-3x+1\) at x = −2. (TSM 099 assessment) | Substitute: \(2(-2)^2-3(-2)+1\). ~ Square first, then multiply: 8 + 6 + 1. ~ The value is 15.
''')
add('tsm','8',r'''
What is an expression? | A mathematical combination of numbers, variables, and operations without an equality claim.
What is an equation? | A statement that two expressions are equal.
What is an identity? | An equation true for every allowed value of its variable.
What does it mean to solve an equation? | Find all variable values making the equality true.
Does matching at one input prove two expressions always equal? | No; one counterexample disproves an identity, but one match does not prove it.
---
Compare 2(x + 3) and 2x + 6 at x = −1, then decide whether they always agree. | At −1 both give 4. ~ Distribution gives 2(x + 3) = 2x + 6 for every x. ~ The equality is an identity.
Classify x + 2 = 5 and x + 2 = x + 5. | The first equality holds only at x = 3. ~ Subtract x from both sides of the second to get 2 = 5. ~ The second has no solution.
''')
add('tsm','9',r'''
What are terms? | Parts of a sum separated by addition or subtraction, with their signs.
What makes terms like terms? | They have exactly the same variable factors and exponents.
What is a coefficient? | The numerical factor multiplying a variable part.
How do you combine like terms? | Add or subtract coefficients and keep the variable part.
Are x and x squared like terms? | No; their exponents differ.
---
Simplify \(4x-7+3x+2\). | Combine x terms: 4x + 3x = 7x. ~ Combine constants: −7 + 2 = −5. ~ Result: 7x − 5.
Simplify \(5x^2-2x+3x^2+6x\). | Combine squared terms: \(5x^2+3x^2=8x^2\). ~ Combine linear terms: −2x + 6x = 4x. ~ Result: \(8x^2+4x\).
''')
add('tsm','10',r'''
What are factors? | Quantities multiplied together.
What is the product rule for powers of the same base? | \(x^m x^n=x^{m+n}\).
What is the power-of-a-power rule? | \((x^m)^n=x^{mn}\).
How does a power apply to a product? | \((ab)^n=a^n b^n\).
Why is \(x^2+x^3\) not \(x^5\)? | The exponent-addition rule applies to multiplication, not addition.
---
Simplify \((3x^2)(-2x^4)\). | Multiply coefficients: 3(−2) = −6. ~ Add exponents on x: 2 + 4 = 6. ~ Result: \(-6x^6\).
Simplify \((-2x^3)^2\). | Square both factors: \((-2)^2(x^3)^2\). ~ The coefficient is 4 and the exponent is 3 × 2 = 6. ~ Result: \(4x^6\).
''')
add('tsm','11',r'''
State the distributive property. | \(a(b+c)=ab+ac\).
What must happen to every term inside parentheses? | Each term is multiplied by the outside factor.
How do you distribute a minus sign? | Multiply every term inside by −1.
What should follow distribution when possible? | Combine like terms.
What operation reverses distribution? | Factoring.
---
Expand −3(2x − 5). | Multiply −3 by 2x to get −6x. ~ Multiply −3 by −5 to get +15. ~ Result: −6x + 15.
Simplify 2(x + 4) − (3x − 1). | Distribute to get 2x + 8 − 3x + 1. ~ Combine like terms: −x + 9.
''')
add('tsm','12',r'''
How do you multiply two polynomials? | Multiply each term of one by each term of the other, then combine like terms.
What is a binomial? | A polynomial with two terms.
What do you do with exponents when multiplying powers of x? | Add the exponents.
What is \((a+b)^2\)? | \(a^2+2ab+b^2\).
What is \((a+b)(a-b)\)? | \(a^2-b^2\).
---
Expand (x + 3)(x − 5). | Multiply all four pairs: \(x^2-5x+3x-15\). ~ Combine linear terms: \(x^2-2x-15\).
Expand \((2x-1)(x^2+3x+4)\). | Distribute 2x: \(2x^3+6x^2+8x\). ~ Distribute −1: \(-x^2-3x-4\). ~ Combine: \(2x^3+5x^2+5x-4\).
''')
add('tsm','13',r'''
What is the greatest common divisor? | The largest positive integer dividing each given integer.
How can lists of divisors find a GCD? | List positive divisors of each number and take the largest shared one.
How do prime factorizations give a GCD? | Use only shared primes, with their smaller exponents.
What does relatively prime mean? | The GCD is 1.
How do you find the common variable factor in \(x^m\) and \(x^n\)? | Use x raised to the smaller exponent.
---
Find GCD(18, 24) by both methods. | Divisors of 18: 1, 2, 3, 6, 9, 18; of 24: 1, 2, 3, 4, 6, 8, 12, 24. Largest shared: 6. ~ Prime factors: \(18=2\cdot3^2\), \(24=2^3\cdot3\). Shared minimum powers give 2 × 3 = 6.
Find the GCF of \(18x^3\) and \(24x^2\). | The numerical GCD is 6. ~ The smaller x exponent is 2. ~ The GCF is \(6x^2\).
''')
add('tsm','14',r'''
What does factoring out a GCF accomplish? | It rewrites a sum as a product of the GCF and a remaining polynomial.
How is each term inside the parentheses found? | Divide its original term by the GCF.
If an original term equals the GCF, what remains inside? | 1.
How do you check a factorization? | Distribute to recover the original expression.
What must you check after factoring once? | Whether any common factor remains in all terms inside.
---
Factor \(12x^3-18x^2\). | The GCF is \(6x^2\). ~ Divide each term by it: 2x and −3. ~ Result: \(6x^2(2x-3)\); distribution recovers the original.
Factor 7x + 7. | The GCF is 7. ~ Dividing both terms by 7 gives x and 1. ~ Result: 7(x + 1).
''')
add('tsm','15',r'''
For \((mx+p)(nx+q)\), what determines the leading coefficient? | The product mn.
What determines the constant term? | The product pq.
What determines the middle coefficient? | The cross-term sum mq + np.
What sign pattern gives a negative constant? | Opposite signs on the constant factors.
What should you do if no integer factor pair works? | State that the polynomial is not factorable into integer linear factors.
---
Factor \(2x^2+7x+3\). | Try first terms 2x and x, and last terms 1 and 3. ~ (2x + 1)(x + 3) gives cross terms 6x + x = 7x. ~ Thus the factorization is (2x + 1)(x + 3).
Factor \(x^2-25\), and test \(2x^2+x+2\) for integer factors. | The difference of squares gives \(x^2-25=(x-5)(x+5)\). ~ For the second, first factors must be 2x and x; constant factors must both be 1 and 2, or both negative. ~ Possible middle coefficients are ±4 or ±5, never 1, so there are no integer linear factors.
''')
add('tsm','16',r'''
What is factoring by grouping? | Factoring groups of terms separately to create a common factor.
What must match after the first factoring step? | A common binomial or other polynomial factor.
Why might you factor a negative from a group? | To make its remaining factor match the other group's factor.
Can terms be reordered before grouping? | Yes, provided every term keeps its sign.
How do you check the final product? | Multiply it out and compare with the original.
---
Factor \(x^3+3x^2+2x+6\). | Group: \(x^2(x+3)+2(x+3)\). ~ Factor the shared binomial: \((x+3)(x^2+2)\).
Factor \(3x^3-6x^2-2x+4\). | Group: \(3x^2(x-2)-2(x-2)\). ~ Factor (x − 2): \((x-2)(3x^2-2)\).
''')
add('tsm','17',r'''
For \(ax^2+bx+c\), what product do you use in the sum-product method? | ac.
What sum must the two selected numbers have? | b.
What do you do with the selected numbers? | Split the middle term bx into their corresponding x terms.
What method finishes after splitting the middle term? | Factoring by grouping.
What should you check before using the method? | Factor out any GCF first.
---
Factor \(6x^2+11x+3\). | ac = 18; 9 and 2 have product 18 and sum 11. ~ Rewrite as \(6x^2+9x+2x+3\). ~ Group: 3x(2x + 3) + 1(2x + 3). ~ Result: (3x + 1)(2x + 3).
Factor \(4x^2-4x-3\). | ac = −12; −6 and 2 sum to −4. ~ Rewrite as \(4x^2-6x+2x-3\). ~ Group: 2x(2x − 3) + 1(2x − 3). ~ Result: (2x + 1)(2x − 3).
''')
add('tsm','18',r'''
What is a rational expression? | A quotient of polynomials with a nonzero denominator.
When should denominator restrictions be recorded? | From the original expression, before canceling.
What can be canceled? | Common nonzero factors of the whole numerator and denominator.
Why factor before canceling? | Factoring reveals products rather than separate terms of sums.
How are x − a and a − x related? | They are opposites: \(a-x=-(x-a)\).
---
Simplify \((x^2-9)/(x^2+3x)\). | The original denominator x(x + 3) excludes x = 0 and −3. ~ Factor the numerator as (x − 3)(x + 3). ~ Cancel x + 3 to get (x − 3)/x, retaining both restrictions.
Simplify \((x-4)/(4-x)\). | Require x ≠ 4. ~ Since 4 − x = −(x − 4), cancel the common factor. ~ The value is −1 for x ≠ 4.
''')
add('tsm','19',r'''
How do you multiply fractions? | Multiply numerators and multiply denominators, then simplify.
What is a reciprocal? | The number which multiplies a given nonzero number to give 1.
How do you divide by a fraction? | Multiply by its reciprocal.
Which fraction is inverted in a division? | The divisor, the second fraction.
What remains when the numerator cancels completely? | 1, not 0.
---
Compute \(\frac23\cdot\frac38\). | Cancel the common 3 and reduce 2/8. ~ The product is 1/4; the remaining numerator is 1.
Compute \(\frac5{12}\div\frac{10}9\). | Multiply by the reciprocal: \(\frac5{12}\cdot\frac9{10}\). ~ Reduce 5/10 to 1/2 and 9/12 to 3/4. ~ The result is 3/8.
''')
add('tsm','20',r'''
What should you do before multiplying rational expressions? | Factor all numerators and denominators.
How do you divide rational expressions? | Multiply by the reciprocal of the divisor.
What restrictions arise from a divisor? | It must be defined and nonzero, in addition to all original denominator restrictions.
May you cancel a term in an unfactored sum? | No; only common factors may be canceled.
What numerator remains after all its factors cancel? | 1.
---
Simplify \(\frac{x^2-9}{x^2-x-6}\cdot\frac{x-2}{x+3}\). | Factor: (x − 3)(x + 3) over (x − 3)(x + 2), times (x − 2)/(x + 3). ~ Original restrictions are x ≠ 3, −2, −3. ~ Cancel common factors to get (x − 2)/(x + 2), keeping all restrictions.
Simplify \(\frac{2x}{x^2-4}\div\frac{4x^2}{x+2}\). | Original denominators exclude ±2; the divisor is zero at x = 0, so exclude 0 too. ~ Multiply \(\frac{2x}{(x-2)(x+2)}\cdot\frac{x+2}{4x^2}\). ~ Cancel to get \(\frac1{2x(x-2)}\), with x ≠ −2, 0, 2.
''')
add('tsm','21',r'''
What is the least common multiple? | The smallest positive integer that is a multiple of every given positive integer.
How do prime factorizations give an LCM? | Use every prime appearing, with its largest exponent.
How does an LCM differ from a GCD? | An LCM is a shared multiple; a GCD is a shared divisor.
What is a least common denominator? | The LCM of the denominators.
Must the LCM equal the product? | No; shared factors can make it smaller.
---
Find LCM(12, 18). | \(12=2^2\cdot3\) and \(18=2\cdot3^2\). ~ Take largest powers: \(2^2\cdot3^2=36\).
Find the LCD of 1/8 and 5/12. | \(8=2^3\) and \(12=2^2\cdot3\). ~ The LCD is \(2^3\cdot3=24\). ~ The equivalent fractions are 3/24 and 10/24.
''')
add('tsm','22',r'''
What is required before adding fractions? | A common denominator.
With equal denominators, what do you add? | The numerators; keep the common denominator.
How do you change to an equivalent denominator? | Multiply numerator and denominator by the same missing factor.
Why should you use the LCD? | It gives the smallest convenient common denominator.
What is the final step? | Simplify the result.
---
Compute 5/6 − 1/4. | The LCD is 12. ~ Rewrite as 10/12 − 3/12 = 7/12.
Compute 2/9 + 5/6. | The LCD is 18. ~ Rewrite as 4/18 + 15/18 = 19/18. ~ This is already reduced; it also equals 1 and 1/18.
''')
add('tsm','23',r'''
What is the first step in finding an algebraic LCD? | Factor the denominators.
How do you build the LCD? | Include each distinct factor to its greatest needed power.
What changes when you subtract a rational expression? | Subtract its entire numerator, changing every sign as needed.
When may common factors be canceled? | After forming and factoring the complete numerator and denominator.
Which restrictions must be retained? | All original denominator exclusions.
---
Simplify \(\frac2{x-1}+\frac3{x+1}\). | Require x ≠ ±1; the LCD is (x − 1)(x + 1). ~ The numerator is 2(x + 1) + 3(x − 1) = 5x − 1. ~ Result: \(\frac{5x-1}{(x-1)(x+1)}\).
Simplify \(\frac{x}{x-2}-\frac2{x-2}\). | Require x ≠ 2. ~ Subtract numerators to obtain (x − 2)/(x − 2). ~ Cancel the common factor: 1, for x ≠ 2.
''')
add('tsm','24',r'''
What does solving ax = b require when a is nonzero? | Divide both sides by a.
Why do the same operation to both sides? | To preserve equality.
Can a coefficient of zero be divided out? | No; division by zero is undefined.
How do you check a solution? | Substitute it into the original equation.
What is the solution of 0x = 0? | Every real number.
---
Solve −6x = 42. | Divide both sides by −6 to obtain x = −7. ~ Check: −6(−7) = 42.
Solve x/5 = −3. | Multiply both sides by 5: x = −15. ~ Check: −15/5 = −3.
''')
add('tsm','25',r'''
What is the goal when solving a linear equation? | Isolate the variable with coefficient 1.
What should you do with like terms on the same side? | Combine them.
How can you collect variable terms on one side? | Add or subtract the same variable term on both sides.
What does a false statement such as 0 = 5 mean? | No solution.
What does a true statement such as 0 = 0 mean after variables cancel? | Every real number is a solution, if there are no other restrictions.
---
Solve 5x − 7 = 2x + 8. | Subtract 2x: 3x − 7 = 8. ~ Add 7: 3x = 15. ~ Divide by 3: x = 5; both original sides equal 18.
Solve 4x + 2 = 4x − 3. | Subtract 4x to get 2 = −3. ~ This is false, so the equation has no solution.
''')
add('tsm','26',r'''
How can you remove parentheses in a linear equation? | Distribute each outside factor to every term inside.
What happens when a negative multiplies a parenthesis? | Every enclosed term changes sign and magnitude according to that factor.
What follows distribution? | Combine like terms, collect variables, and isolate the variable.
Should you distribute to only the first term? | No; distribute to every term.
Where should a proposed solution be checked? | In the original equation.
---
Solve 3(x − 2) + 4 = 2x + 7. | Distribute and combine: 3x − 2 = 2x + 7. ~ Subtract 2x and add 2: x = 9. ~ Check: both sides are 25.
Solve 5 − 2(x + 3) = 7. | Distribute: 5 − 2x − 6 = 7. ~ Combine: −2x − 1 = 7, so −2x = 8 and x = −4. ~ Check: 5 − 2(−1) = 7.
''')
add('tsm','27',r'''
What is standard form for a quadratic equation? | \(ax^2+bx+c=0\), where a ≠ 0.
When can you use the zero-product property? | When a product equals zero.
What must be included when solving a squared expression equal to a positive number? | Both the positive and negative square roots.
State the quadratic formula. | \(x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}\).
What does the discriminant tell you about real solutions? | Positive: two; zero: one repeated solution; negative: none.
---
Solve \(x^2-5x+6=0\) by factoring. | Factor to (x − 2)(x − 3) = 0. ~ Set each factor equal to zero: x = 2 or x = 3.
Solve \((x-4)^2=25\) by square roots. | Take both roots: x − 4 = ±5. ~ Add 4: x = 9 or x = −1.
Solve \(2x^2+x-3=0\) by the quadratic formula. | Use a = 2, b = 1, c = −3; the discriminant is 1 + 24 = 25. ~ \(x=(-1\pm5)/4\). ~ The solutions are 1 and −3/2.
''')
add('tsm','28',r'''
How can fractions be cleared from an equation? | Multiply every term on both sides by an LCD.
Must constant terms also be multiplied by the LCD? | Yes; every term must be multiplied.
Does multiplying by an LCD change the solution set when denominators are fixed nonzero numbers? | No.
What do you do after clearing denominators? | Solve the resulting linear equation.
How should a fractional answer be written? | In reduced form.
---
Solve x/3 + 1/2 = 5/6. | Multiply every term by 6: 2x + 3 = 5. ~ Then 2x = 2, so x = 1. ~ Check: 1/3 + 1/2 = 5/6.
Solve (x − 1)/4 = (x + 2)/6. | Multiply by 12: 3(x − 1) = 2(x + 2). ~ Expand: 3x − 3 = 2x + 4. ~ Thus x = 7; both original sides equal 3/2.
''')
add('tsm','29',r'''
What is a rational equation? | An equation containing rational expressions.
What must you record before clearing denominators? | Values making any original denominator zero.
How are denominators cleared? | Multiply every term by an LCD on the allowed domain.
What is an extraneous candidate? | A candidate that does not satisfy the original equation.
What must happen to every candidate at the end? | Check restrictions and substitute into the original equation.
---
Solve \(\frac2{x-1}=\frac3{x+1}\). | Require x ≠ 1, −1. ~ Multiply by (x − 1)(x + 1): 2(x + 1) = 3(x − 1). ~ Solve: x = 5; both sides originally equal 1/2.
Solve \(\frac{x}{x-2}=\frac2{x-2}\). | Require x ≠ 2. ~ Clearing denominators gives x = 2. ~ That candidate is excluded, so there is no solution.
''')
add('tsm','30',r'''
What does a point on an equation's graph represent? | An ordered pair satisfying the equation.
How do you find an x-intercept? | Set y = 0 and solve for x.
How do you find a y-intercept? | Set x = 0 and solve for y.
How many distinct points determine a straight line? | Two; a third is useful for checking.
What do x = a and y = b graph as? | A vertical line and a horizontal line, respectively.
---
Graph 2x + y = 4 using intercepts. | Set y = 0 to get x = 2, giving (2, 0). ~ Set x = 0 to get y = 4, giving (0, 4). ~ Draw the straight line through them; (1, 2) checks the line.
Graph x = −3 and y = 2. | x = −3 contains all points with x-coordinate −3, so draw a vertical line through −3 on the x-axis. ~ y = 2 contains all points with y-coordinate 2, so draw a horizontal line through 2 on the y-axis.
''')
add('tsm','31',r'''
What is a solution of a system? | An ordered pair satisfying every equation in the system.
How are solutions located graphically? | At intersections of the graphs.
What do distinct parallel lines mean? | No solution.
What do coincident lines mean? | Infinitely many solutions.
How do you verify a visually estimated intersection? | Substitute its coordinates into both equations.
---
Solve y = x + 1 and y = −x + 5 by graphing. | Plot (0, 1) and (2, 3) for the first line. ~ Plot (0, 5) and (2, 3) for the second. ~ They intersect at (2, 3); 3 = 2 + 1 and 3 = −2 + 5 verify it.
Classify y = 2x + 1 and y = 2x − 3. | Both have slope 2 and different intercepts. ~ Their graphs are distinct parallel lines and never intersect. ~ The system has no solution.
''')
add('tsm','32',r'''
What is slope-intercept form? | y = mx + b.
What does m represent? | Slope: vertical change divided by horizontal change.
What point is identified by b? | The y-intercept (0, b).
What does a negative slope indicate? | The line falls as you move right.
Can a vertical line be written as y = mx + b? | No; its slope is undefined.
---
Graph y = −2x + 3. | Start at the y-intercept (0, 3). ~ Slope −2 = −2/1 means down 2 and right 1 to (1, 1). ~ Draw the line through these points; (2, −1) also lies on it.
Rewrite 3x + 2y = 6 and identify slope and intercept. | Subtract 3x: 2y = −3x + 6. ~ Divide by 2: y = −(3/2)x + 3. ~ The slope is −3/2 and the y-intercept is (0, 3).
''')
add('tsm','33',r'''
What does substitution replace? | A variable with an equal expression from another equation.
What is the goal of elimination? | Add equivalent equations so one variable cancels.
When multiplying an equation for elimination, what must be multiplied? | Every term on both sides.
After finding one variable, how is the other found? | Substitute into an original equation.
Where must the final ordered pair be checked? | In both original equations.
---
Solve y = 2x − 1 and x + y = 8 by substitution. | Substitute 2x − 1 for y: x + 2x − 1 = 8. ~ Thus 3x = 9 and x = 3. ~ Then y = 5; (3, 5) satisfies both equations.
Solve x + y = 7 and x − y = 1 by elimination. | Add the equations: 2x = 8. ~ Thus x = 4; substitute into x + y = 7 to get y = 3. ~ Check: 4 + 3 = 7 and 4 − 3 = 1.
''')
add('tsm','34',r'''
How do you find slope from two points? | \(m=(y_2-y_1)/(x_2-x_1)\), when x₂ ≠ x₁.
What is point-slope form? | \(y-y_1=m(x-x_1)\).
What slope does a horizontal line have? | Zero.
What slope does a vertical line have? | Undefined.
How can b be found when slope and a point are known? | Substitute the point into y = mx + b and solve for b.
---
Write the line through (1, 3) and (3, 7). | Slope: (7 − 3)/(3 − 1) = 2. ~ Use (1, 3): 3 = 2(1) + b, so b = 1. ~ The equation is y = 2x + 1.
A cost is $5 initially plus $3 per item. Write an equation. | Let x be the number of items and y the cost in dollars. ~ The fixed cost is the intercept; the per-item cost is the slope. ~ Thus y = 3x + 5, for nonnegative whole-number x.
''')
add('tsm','35',r'''
What does percent mean? | Per hundred.
How do you convert a percent to a decimal? | Divide by 100.
What equation relates part, rate, and whole? | Part = rate × whole, with rate in decimal form.
How do you find what percent one quantity is of another? | Divide part by whole, then multiply by 100%.
Which quantity is the base in a percent problem? | The whole to which the percentage applies.
---
Find 18% of 250. | Convert 18% to 0.18. ~ Multiply: 0.18 × 250 = 45.
Thirty is what percent of 120? | Divide part by whole: 30/120 = 0.25. ~ Convert to percent: 25%.
''')
add('tsm','36',r'''
How do you calculate a percent increase? | Multiply the original quantity by 1 plus the decimal rate.
How do you calculate a percent decrease? | Multiply the original quantity by 1 minus the decimal rate.
What denominator is used for percent change? | The original quantity.
Do a 20% increase and a 20% decrease cancel? | No; the second percent uses a different base.
How do you recover an original price from a discounted price? | Divide by the remaining fraction of the original price.
---
An $80 item is discounted 25%. Find its sale price. | The remaining fraction is 1 − 0.25 = 0.75. ~ Sale price = 80 × 0.75 = $60.
A price after 10% tax is $55. Find the price before tax. | Let p be the original price; 1.10p = 55. ~ Divide: p = 55/1.10 = $50. ~ Check: $50 plus $5 tax is $55.
''')
add('tsm','37',r'''
What should a variable definition include? | The quantity it represents and its units.
How do you translate five more than a number? | x + 5.
How do you translate five less than a number? | x − 5.
What does a word problem's solution need beyond algebra? | Units and a check that the answer makes sense in context.
What is the distance-rate-time relationship for constant speed? | Distance = rate × time.
---
Three more than twice a number is 17. Find the number. | Let x be the number; 2x + 3 = 17. ~ Subtract 3 and divide by 2: x = 7. ~ Check: 2(7) + 3 = 17.
A car travels at a constant 45 miles per hour for 2.5 hours. Find the distance. | Use distance = rate × time. ~ 45 × 2.5 = 112.5 miles. ~ The hour units cancel, leaving miles.
''')

add('101','1.1',r'''
What distinguishes rational from irrational real numbers? | Rational numbers are ratios of integers with nonzero denominator; irrational numbers are not.
State the distributive property. | \(a(b+c)=ab+ac\).
What is the additive inverse of a? | −a, because a + (−a) = 0.
What is absolute value? | Distance from zero on the number line.
What is the order of operations? | Grouping, exponents, multiplication/division left to right, then addition/subtraction left to right.
---
Evaluate \(3-2(5-8)^2\). | Parentheses give −3, whose square is 9. ~ Multiply: 2 × 9 = 18. ~ Subtract: 3 − 18 = −15.
Classify \(-7\), \(3/8\), and \(\sqrt2\) as rational or irrational. | −7 = −7/1 and 3/8 are ratios of integers, so both are rational. ~ √2 cannot be expressed as such a ratio, so it is irrational. ~ All three are real numbers.
''')
add('101','1.2',r'''
State the product rule for equal bases. | \(a^m a^n=a^{m+n}\).
State the quotient rule for equal nonzero bases. | \(a^m/a^n=a^{m-n}\).
What does a negative exponent mean? | A reciprocal: \(a^{-n}=1/a^n\), for a ≠ 0.
What is the power-of-a-power rule? | \((a^m)^n=a^{mn}\).
What is scientific notation? | \(a\times10^n\), with \(1\leq\lvert a\rvert<10\) and integer n.
---
Simplify \((2x^3)^2/x^4\), x ≠ 0. | Square the numerator to get \(4x^6\). ~ Subtract exponents in the quotient: \(4x^{6-4}=4x^2\).
Multiply \((3\times10^5)(2\times10^{-3})\). | Multiply coefficients: 3 × 2 = 6. ~ Add exponents: 5 + (−3) = 2. ~ Result: \(6\times10^2=600\).
''')
add('101','1.3',r'''
What does \(a^{1/n}\) represent? | The nth root of a, when defined over the reals.
What real restriction applies to an even root? | Its radicand must be nonnegative.
What is \(\sqrt{x^2}\) for real x? | \(\lvert x\rvert\).
What makes radicals like radicals? | They have the same index and simplified radicand.
What does rationalizing a denominator mean? | Rewriting an equivalent expression without a radical in its denominator.
---
Simplify \(\sqrt{50}+2\sqrt8\). | \(\sqrt{50}=5\sqrt2\) and \(\sqrt8=2\sqrt2\). ~ Combine: \(5\sqrt2+4\sqrt2=9\sqrt2\).
Evaluate \(27^{2/3}\) and rationalize \(3/\sqrt5\). | Take the cube root of 27 and square: \(27^{2/3}=3^2=9\). ~ Multiply the second expression by \(\sqrt5/\sqrt5\). ~ Result: \(3\sqrt5/5\).
''')
add('101','1.4',r'''
What is a polynomial in x? | A finite sum of terms with real coefficients and nonnegative integer exponents of x.
What is a polynomial's degree? | Its largest exponent with a nonzero coefficient, for a nonzero polynomial.
What are like terms? | Terms with identical variable factors and exponents.
How do you subtract a polynomial? | Distribute the subtraction to every term, then combine like terms.
How do you multiply polynomials? | Distribute every term of one across every term of the other.
---
Subtract \((2x^2-3x+1)-(x^2+4x-5)\). | Distribute the minus: \(2x^2-3x+1-x^2-4x+5\). ~ Combine: \(x^2-7x+6\).
Expand \((x-4)(2x+3)\). | Multiply pairs to obtain \(2x^2+3x-8x-12\). ~ Combine the middle terms: \(2x^2-5x-12\).
''')
add('101','1.5',r'''
What should you look for first when factoring? | A greatest common factor.
What reverses factoring? | Multiplication or distribution.
State the difference-of-squares identity. | \(a^2-b^2=(a-b)(a+b)\).
For \(x^2+bx+c\), what must the two constant factors do? | Multiply to c and add to b.
When is a polynomial completely factored over the integers? | Its remaining nonconstant factors cannot be factored further with integer coefficients.
---
Factor \(3x^3-12x\). | Remove the GCF: \(3x(x^2-4)\). ~ Factor the difference of squares: \(3x(x-2)(x+2)\).
Factor \(6x^2+x-2\). | ac = −12; 4 and −3 have sum 1. ~ Split the middle term: \(6x^2+4x-3x-2\). ~ Group as \(2x(3x+2)-(3x+2)\). ~ Result: (2x − 1)(3x + 2).
''')
add('101','1.6',r'''
What values are excluded from a rational expression? | Values making any original denominator zero.
What may be canceled in a fraction? | Common nonzero factors of numerator and denominator.
How do you divide rational expressions? | Multiply by the reciprocal, requiring the divisor to be defined and nonzero.
What is required before adding rational expressions? | A common denominator.
Do exclusions disappear after cancellation? | No; original restrictions remain.
---
Simplify \((x^2-4)/(x^2+x-6)\). | Factor: \((x-2)(x+2)/((x+3)(x-2))\). ~ Original restrictions: x ≠ −3, 2. ~ Cancel x − 2 to get (x + 2)/(x + 3), retaining both restrictions.
Add \(1/x+2/(x+1)\). | Require x ≠ 0, −1; use LCD x(x + 1). ~ Combine numerators: x + 1 + 2x = 3x + 1. ~ Result: \((3x+1)/(x(x+1))\).
''')
add('101','2.1',r'''
What does an ordered pair (x, y) specify? | Horizontal coordinate first and vertical coordinate second.
What does it mean for a point to lie on an equation's graph? | Its coordinates satisfy the equation.
How do you find intercepts? | Set y = 0 for x-intercepts; set x = 0 for y-intercepts.
State the distance formula. | \(d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}\).
State the midpoint formula. | \(((x_1+x_2)/2,(y_1+y_2)/2)\).
---
Find the intercepts of 2x + 3y = 12. | At y = 0, 2x = 12 gives (6, 0). ~ At x = 0, 3y = 12 gives (0, 4).
Find distance and midpoint between (−1, 2) and (3, 5). | Coordinate differences are 4 and 3. ~ Distance: \(\sqrt{4^2+3^2}=5\). ~ Midpoint: ((−1 + 3)/2, (2 + 5)/2) = (1, 3.5).
''')
add('101','2.2',r'''
What is a linear equation in one variable? | An equation reducible to ax + b = 0, with a ≠ 0.
What operations preserve equality? | Adding the same quantity or multiplying by the same nonzero quantity on both sides.
How do you clear fixed numerical denominators? | Multiply every term by an LCD.
What does a true statement after variables cancel indicate? | An identity on the original allowed domain.
What does a false statement after variables cancel indicate? | No solution.
---
Solve 3(2x − 1) = 4x + 9. | Distribute: 6x − 3 = 4x + 9. ~ Subtract 4x and add 3: 2x = 12, giving x = 6. ~ Both original sides equal 33.
Solve (x − 2)/3 + 1/2 = 5/6. | Multiply every term by 6: 2(x − 2) + 3 = 5. ~ Simplify: 2x − 1 = 5, so x = 3. ~ Check: 1/3 + 1/2 = 5/6.
''')
add('101','2.3',r'''
What should you state before writing a model equation? | What each variable measures, including units.
What distinguishes a model solution from a meaningful answer? | A meaningful answer also meets the context's restrictions.
What equation describes constant-speed motion? | Distance = rate × time.
What equation describes simple interest? | Interest = principal × annual rate × time in years.
How should a model answer be checked? | Substitute it and interpret its size, sign, and units in context.
---
A taxi charges $4 plus $2 per mile. How many miles cost $18? | Let m be miles: 4 + 2m = 18. ~ Solve 2m = 14, so m = 7 miles. ~ Check: $4 + $14 = $18.
How long does a 150-mile trip take at a constant 60 mph? | Use 150 = 60t with t in hours. ~ Divide: t = 2.5 hours. ~ This assumes constant speed and excludes stops.
''')
add('101','2.4',r'''
How is the imaginary unit i defined? | \(i^2=-1\).
For a positive real a, what is \(\sqrt{-a}\)? | \(i\sqrt a\), the principal square root.
What is standard complex form? | a + bi with real a and b.
In a + bi, what are the real and imaginary parts? | The real part is a; the imaginary part is b.
How does a principal square root differ from solving a squared equation? | A principal root gives one value; the equation can have both positive and negative roots.
---
Write \(\sqrt{-20}\) in standard form and identify its parts. | \(\sqrt{-20}=i\sqrt{4\cdot5}=2i\sqrt5\). ~ Its real part is 0 and its imaginary part is \(2\sqrt5\).
Evaluate \(\sqrt{-49}\), then solve \(x^2=-49\). | The principal root is 7i. ~ The equation has both solutions x = 7i and x = −7i. ~ The ± belongs to the equation's solution set.
''')
add('101','2.5',r'''
What is standard quadratic form? | \(ax^2+bx+c=0\), a ≠ 0.
When can the zero-product property be used? | After writing a product equal to zero.
What must accompany the square-root method? | Both signs, when the isolated square equals a positive number.
State the quadratic formula. | \(x=(-b\pm\sqrt{b^2-4ac})/(2a)\).
What does a negative discriminant imply about real roots? | There are no real roots.
---
Solve \(x^2-7x+12=0\). | Factor: (x − 3)(x − 4) = 0. ~ Set each factor to zero: x = 3 or 4.
Solve \(2x^2-3x-2=0\) using the quadratic formula. | Use a = 2, b = −3, c = −2; the discriminant is 9 + 16 = 25. ~ \(x=(3\pm5)/4\). ~ Thus x = 2 or −1/2.
Solve \((x+1)^2=12\). | Take both square roots: \(x+1=\pm2\sqrt3\). ~ Subtract 1: \(x=-1\pm2\sqrt3\).
''')
add('101','2.6',r'''
Why must radical-equation candidates be checked? | Squaring can introduce extraneous solutions.
What does \(\lvert u\rvert=c\) imply for c > 0? | u = c or u = −c.
What happens if an absolute value is set equal to a negative number? | There is no real solution.
How can a quadratic-type equation in \(x^2\) be simplified? | Substitute u = x², solve for u, then solve for x.
Why record denominator restrictions before solving? | A candidate at an excluded input is invalid.
---
Solve \(\sqrt{x+6}=x\). | The right side must be nonnegative, so x ≥ 0. ~ Square: x + 6 = x², giving (x − 3)(x + 2) = 0. ~ Check candidates: x = 3 works; x = −2 fails. The solution is 3.
Solve \(x^4-5x^2+4=0\). | Let u = x²: u² − 5u + 4 = (u − 1)(u − 4) = 0. ~ Thus x² = 1 or 4. ~ The real solutions are −2, −1, 1, 2.
''')
add('101','2.7',r'''
When must an inequality symbol reverse? | When multiplying or dividing both sides by a negative number.
What do interval parentheses mean? | The endpoint is excluded.
What do interval brackets mean? | A finite endpoint is included.
What does AND mean for solution sets? | Intersection: both conditions must hold.
For c > 0, what does \(\lvert x\rvert<c\) mean? | −c < x < c.
---
Solve −3x + 2 ≥ 11. | Subtract 2: −3x ≥ 9. ~ Divide by −3 and reverse: x ≤ −3. ~ Interval: \((-\infty,-3]\).
Solve \(\lvert x-2\rvert<5\). | Rewrite as −5 < x − 2 < 5. ~ Add 2 throughout: −3 < x < 7. ~ Interval: (−3, 7).
''')
add('101','3.1',r'''
What is a function? | A rule assigning exactly one output to each input in its domain.
What does f(a) mean? | The output of f at input a.
What is the vertical line test? | A graph represents a function if no vertical line intersects it more than once.
What is a one-to-one function? | A function whose distinct inputs have distinct outputs.
How does evaluating f(a) differ from solving f(x) = a? | Evaluation finds an output; solving finds inputs producing the specified output.
---
For f(x) = 2x − 3, find f(4), then solve f(x) = 7. | Evaluation: f(4) = 8 − 3 = 5. ~ Solving: 2x − 3 = 7 gives x = 5. ~ These are different tasks: an output of 5 versus an input of 5.
Does {(1, 2), (2, 3), (1, 4)} define a function? | Input 1 is paired with both 2 and 4. ~ A function allows exactly one output for each input. ~ Therefore this relation is not a function.
''')
add('101','3.1B',r'''
What does defining f(x) as an expression let you do? | Use f(x) as an abbreviation for the entire expression.
What must be replaced when evaluating f(−2)? | Every occurrence of x in f's defining expression.
Does f(x) mean f multiplied by x? | No; it denotes a function's output at input x.
If f(x) replaces part of a longer expression, what stays unchanged? | All parts not included in f's definition.
Can two functions of x be used in the same expression? | Yes; each abbreviation retains its own definition.
---
Let f(x) = x² + 3x − 1. Rewrite x² + 3x − 1 + 4x, then evaluate at x = 2. | The rewrite is f(x) + 4x. ~ f(2) = 4 + 6 − 1 = 9. ~ The full value is 9 + 8 = 17.
Let f(x) = 2x + 1 and g(x) = x² − 4. Rewrite 3(2x + 1) − (x² − 4) + x. | Replace the defined pieces: 3f(x) − g(x) + x. ~ At x = 1, f(1) = 3 and g(1) = −3. ~ The value is 3(3) − (−3) + 1 = 13.
''')
add('101','3.2',r'''
What is the domain of a graph? | All x-values represented on it.
What is the range of a graph? | All y-values represented on it.
What does an open endpoint mean? | That endpoint is not included.
What does a filled endpoint mean? | That endpoint is included.
Which brackets are used at infinity in interval notation? | Parentheses; infinity is not an attained endpoint.
---
GRAPH_DOMAIN_SEGMENT | Read horizontally: x runs from −3, included, to 2, excluded. ~ Domain: [−3, 2). ~ Read vertically: y runs from −2, included, to 3, excluded. Range: [−2, 3).
GRAPH_DOMAIN_PARABOLA | The left endpoint is open at (−2, 4); the right endpoint is filled at (1, 1). ~ Domain: (−2, 1]. ~ The lowest height 0 is attained at the vertex; height 4 is approached but excluded. Range: [0, 4).
''')
add('101','3.3',r'''
When is a function increasing on an interval? | Its y-values rise as x increases through that interval.
When is it decreasing? | Its y-values fall as x increases.
What is a local minimum? | An attained height no greater than nearby heights.
How is an absolute minimum different? | It is the smallest attained height on the entire graph.
Does an open endpoint attain a maximum or minimum? | No; its excluded point cannot be an attained extremum.
---
GRAPH_BEHAVIOR_W | Moving left to right, the graph decreases to (−2, −1), increases to (0, 2), decreases to (2, −2), then increases to (3, 1). ~ Decreasing intervals: (−4, −2) and (0, 2). Increasing intervals: (−2, 0) and (2, 3). ~ Local minima are (−2, −1) and (2, −2); the interior local maximum is (0, 2). The absolute minimum is −2 at x = 2; the absolute maximum is 3 at x = −4.
GRAPH_BEHAVIOR_OPEN | The graph rises from the filled point (−2, −1) toward the open point (2, 3). ~ It is increasing on (−2, 2). ~ The absolute minimum is −1 at x = −2. There is no absolute maximum because the upper endpoint is excluded and no point has the greatest height.
''')
add('101','3.4',r'''
What does \((f\circ g)(x)\) mean? | f(g(x)): apply g first, then f.
Does composition generally commute? | No; f(g(x)) and g(f(x)) can differ.
How do you compose formula rules? | Replace every input variable in the outer rule with the entire inner expression.
What inputs belong to a composition's domain? | Inputs allowed by the inner function whose outputs are allowed by the outer function.
How does composition differ from multiplying functions? | Composition feeds an output into another rule; multiplication multiplies two outputs at the same input.
---
Let f(x) = 2x + 1 and g(x) = x². Find both compositions at x = 3. | g(3) = 9, so f(g(3)) = f(9) = 19. ~ f(3) = 7, so g(f(3)) = g(7) = 49. ~ Reversing the order changes the answer.
For f(x) = √x and g(x) = x − 4, find f(g(x)) and its domain. | Substitute g(x) into f: \(\sqrt{x-4}\). ~ The inner rule accepts every real number, but the outer root requires x − 4 ≥ 0. ~ The domain is [4, ∞).
''')
add('101','3.5',r'''
What does f(x) + k do to a graph? | Shift it vertically by k.
What does f(x − h) do? | Shift it horizontally right by h when h > 0.
What does −f(x) do? | Reflect across the x-axis.
What does f(−x) do? | Reflect across the y-axis.
What does af(x), with a > 1, do? | Stretch all vertical distances from the x-axis by factor a.
---
Describe y = −2(x − 3)² + 1 from y = x². | Shift right 3, stretch vertically by 2, reflect across the x-axis, then shift up 1. ~ The vertex is (3, 1), and the parabola opens downward.
A point (2, 5) is on y = f(x). Where does it move on y = f(x + 1) − 4? | x + 1 shifts the graph left 1. ~ Subtracting 4 shifts it down 4. ~ The point becomes (1, 1).
''')
add('101','3.6',r'''
What does absolute value measure? | Distance from zero.
What shape is the graph of y = |x|? | A V with vertex at (0, 0).
Where is the vertex of \(y=a\lvert x-h\rvert+k\)? | (h, k).
When does \(a\lvert x-h\rvert+k\) open downward? | When a < 0.
How many solutions can |u| = c have when c > 0? | It produces the two cases u = c and u = −c; actual input solutions depend on u.
---
Describe y = 2|x − 1| − 3 and find its zeros. | Vertex: (1, −3); opens upward with vertical stretch 2. ~ Set y = 0: |x − 1| = 3/2. ~ Thus x = 1 ± 3/2, giving −1/2 and 5/2.
Solve |2x + 1| = 7. | The two cases are 2x + 1 = 7 and 2x + 1 = −7. ~ They give x = 3 and x = −4. ~ Each makes the absolute value 7.
''')
add('101','3.7',r'''
What does an inverse function do? | Reverse the original input-output assignment.
What condition lets a function have an inverse function? | It must be one-to-one on its domain.
Does \(f^{-1}(x)\) mean 1/f(x)? | No; it denotes the inverse function.
What happens to domain and range under inversion? | They exchange roles.
How do inverse graphs relate? | They reflect across the line y = x.
---
Find the inverse of f(x) = 3x − 5. | Write y = 3x − 5, swap x and y: x = 3y − 5. ~ Solve: y = (x + 5)/3. ~ Thus \(f^{-1}(x)=(x+5)/3\); substituting into f gives x.
Find the inverse of y = x² on x ≥ 0. | Swap coordinates: x = y². ~ The original domain requires the inverse output y ≥ 0, so choose y = √x. ~ The inverse has domain [0, ∞) and range [0, ∞).
''')
add('101','4.1',r'''
What is the form of a linear function? | f(x) = mx + b.
What does its slope measure? | Constant change in output per unit change in input.
How do you find slope from two points? | Change in y divided by change in x.
What slope relationship holds for parallel nonvertical lines? | Equal slopes.
What relationship holds for perpendicular nonvertical lines with nonzero slopes? | Their slopes multiply to −1.
---
Find the line through (−1, 4) and (3, −4). | Slope: (−4 − 4)/(3 − (−1)) = −2. ~ Substitute (−1, 4): 4 = −2(−1) + b, giving b = 2. ~ The equation is y = −2x + 2.
Find a line perpendicular to y = 2x + 1 through (0, 3). | The perpendicular slope is −1/2. ~ The point gives y-intercept 3. ~ The line is y = −x/2 + 3.
''')
add('101','4.2',r'''
What pattern suggests a linear model? | Equal changes in input produce equal changes in output.
What does the intercept represent in a cost model? | The initial or fixed cost, if input zero is meaningful.
Why state units for slope? | Slope is output units per input unit.
What is a break-even point? | An input at which revenue equals cost, or two compared costs are equal.
Why can a model's practical domain be smaller than all real numbers? | Negative inputs or fractional item counts may be meaningless.
---
A plan costs $12 plus $4 per visit. Write its model and find the cost for five visits. | For nonnegative whole-number v, C(v) = 12 + 4v dollars. ~ C(5) = 12 + 20 = $32.
Compare A(x) = 10 + 3x and B(x) = 22 + x. Where do costs match? | Set 10 + 3x = 22 + x. ~ Solve 2x = 12, giving x = 6. ~ Both costs are $28; below 6, A is cheaper, and above 6, B is cheaper.
''')
add('101','4.3',r'''
What does a scatter plot display? | Paired numerical observations as points.
What is a residual? | Observed y minus predicted y.
What does a least-squares line minimize? | The sum of squared vertical residuals.
What is interpolation? | Prediction within the observed input range.
Does strong correlation establish causation? | No; association alone does not show cause.
---
A fitted model is y = 2x + 5. An observation is (4, 15). Find its prediction and residual. | Predicted y = 2(4) + 5 = 13. ~ Residual = 15 − 13 = 2. ~ The observation is 2 output units above the fitted line.
Data were collected for x from 10 to 20. Classify predictions at 15 and 30. | At 15 the prediction is interpolation, within the observed range. ~ At 30 it is extrapolation. ~ Extrapolation needs extra justification because the pattern may change beyond the data.
''')
add('101','5.1',r'''
What is vertex form for a quadratic? | \(y=a(x-h)^2+k\), a ≠ 0.
Where is its vertex? | (h, k).
What is its axis of symmetry? | x = h.
How does a determine opening direction? | Positive opens upward; negative opens downward.
How do you find h from \(ax^2+bx+c\)? | \(h=-b/(2a)\).
---
Find the vertex and minimum of y = x² − 6x + 5. | Complete the square: y = (x − 3)² − 4. ~ Vertex: (3, −4); opens upward. ~ The minimum value is −4, and the range is [−4, ∞).
Find the zeros of y = −(x + 1)² + 9. | Set y = 0: (x + 1)² = 9. ~ Thus x + 1 = ±3, giving x = 2 and −4. ~ The vertex (−1, 9) lies midway between the two intercepts.
''')
add('101','5.2',r'''
What is a power function? | A function of the form kxᵖ with constant k and p on its allowed real domain.
Which exponents are allowed in a polynomial? | Nonnegative integers.
How is polynomial degree determined? | By the highest power with a nonzero coefficient after simplification.
What determines polynomial end behavior? | The degree's parity and the sign of the leading coefficient.
How many turning points can a degree-n polynomial have at most? | n − 1.
---
Describe the end behavior of \(y=-2x^4+3x-1\). | The leading term is −2x⁴: even degree and negative coefficient. ~ As x tends to either positive or negative infinity, y tends to negative infinity. ~ Both ends point down.
Identify which of \(3x^5\), \(2^x\), and \(x^2+1/x\) are polynomial functions. | 3x⁵ is a polynomial of degree 5 and also a power function. ~ 2ˣ has the variable in the exponent, so is exponential. ~ x² + 1/x includes x⁻¹, so is not a polynomial.
''')
add('101','5.3',r'''
What is a zero of a polynomial function? | An input where its output equals zero.
How does odd multiplicity affect a zero's graph? | The graph crosses the x-axis.
How does even multiplicity affect it? | The graph touches the x-axis without changing sign there.
What does the Intermediate Value Theorem guarantee for opposite-sign endpoint values? | At least one zero between them for a continuous function.
Can a polynomial graph have a break or corner? | No; polynomial graphs are continuous and smooth.
---
Analyze \(y=(x+2)^2(x-1)\). | Zeros are −2 of multiplicity 2 and 1 of multiplicity 1. ~ The graph touches at −2 and crosses at 1. ~ The positive cubic leading term gives left end down, right end up; the y-intercept is −4.
A polynomial has f(1) = −3 and f(2) = 4. What can be concluded? | A polynomial is continuous on [1, 2]. ~ Because 0 lies between −3 and 4, at least one c in (1, 2) has f(c) = 0. ~ The information does not guarantee exactly one zero.
''')
add('101','5.4',r'''
What identity relates dividend, divisor, quotient, and remainder? | Dividend = divisor × quotient + remainder.
How must the remainder's degree compare with the divisor's? | It must be smaller, unless the remainder is zero.
Why insert zero coefficients for missing powers? | To keep powers correctly aligned during division.
What divisor form is used for standard synthetic division? | x − c.
What does zero remainder tell you? | The divisor is a factor of the dividend.
---
Divide \(x^2+3x+2\) by x + 1. | The first quotient term is x; subtract x(x + 1) to leave 2x + 2. ~ The next term is 2; subtract 2(x + 1) to leave 0. ~ Quotient: x + 2; remainder: 0.
Divide \(x^2+1\) by x − 1. | Include the missing 0x term. ~ Subtract x(x − 1), leaving x + 1; then subtract 1(x − 1), leaving 2. ~ Quotient x + 1 and remainder 2; \((x^2+1)/(x-1)=x+1+2/(x-1)\), x ≠ 1.
''')
add('101','5.5',r'''
State the Factor Theorem. | x − c is a factor of f(x) exactly when f(c) = 0.
State the Remainder Theorem. | Division by x − c has remainder f(c).
What rational-zero candidates are possible for an integer-coefficient polynomial? | Ratios ±p/q, where p divides the constant and q divides the leading coefficient.
Is every rational-zero candidate an actual zero? | No; it must be tested.
How does multiplicity affect zero counting? | Repeated roots count according to their multiplicity.
---
Find the real zeros of \(x^3-2x^2-x+2\). | Group: \(x^2(x-2)-1(x-2)=(x-2)(x^2-1)\). ~ Factor completely: (x − 2)(x − 1)(x + 1). ~ The zeros are 2, 1, and −1.
List rational candidates for \(2x^2-3x+1\), then find its zeros. | Candidates: ±1 and ±1/2. ~ Testing gives f(1) = 0; factoring gives (2x − 1)(x − 1). ~ The actual zeros are 1/2 and 1.
''')
add('101','5.6',r'''
What determines a rational function's domain? | Its original denominator must be nonzero.
What does a canceled denominator factor typically produce? | A hole at the excluded input, if the simplified denominator is nonzero there.
What produces a vertical asymptote? | A denominator zero remaining after common factors are canceled.
For equal numerator and denominator degrees, what is the horizontal asymptote? | The ratio of leading coefficients.
May a graph cross a horizontal asymptote? | Yes.
---
Analyze \(y=(x^2-1)/(x-1)\). | Require x ≠ 1. ~ Cancel x − 1 to get y = x + 1 on that domain. ~ The graph is that line with a hole at (1, 2), and has no vertical asymptote.
Find domain and asymptotes of \(y=(2x+1)/(x-3)\). | Domain: all real x except 3. ~ The uncanceled denominator zero gives vertical asymptote x = 3. ~ Equal degrees give horizontal asymptote y = 2.
''')
add('101','5.7',r'''
Why may a quadratic need a restricted domain for inversion? | Its full graph is not one-to-one.
How do you select a square-root branch for an inverse? | Use the sign required by the original domain.
What happens to domain and range under inversion? | They exchange roles.
What is \(\sqrt{x^2}\) for all real x? | |x|.
What graph test detects one-to-one behavior? | The horizontal line test.
---
Invert f(x) = (x − 2)² + 1 on x ≥ 2. | Swap x and y: x = (y − 2)² + 1. ~ Since y must be at least 2, take y − 2 = √(x − 1). ~ The inverse is 2 + √(x − 1), with domain [1, ∞).
Invert f(x) = x³ − 4. | Swap: x = y³ − 4. ~ Add 4 and take the cube root: \(f^{-1}(x)=\sqrt[3]{x+4}\). ~ Both domain and range are all real numbers.
''')
add('101','6.1',r'''
What is the basic exponential form? | f(x) = abˣ, with b > 0 and b ≠ 1.
Which base values produce growth for a > 0? | b > 1.
Which produce decay for a > 0? | 0 < b < 1.
How does a constant percent change appear in an exponential model? | The output multiplies by the same factor for each equal input step.
What is the compound-interest formula? | \(A=P(1+r/n)^{nt}\), with annual decimal rate r and n compoundings per year.
---
For f(x) = 5(2ˣ), find f(0), f(3), and the growth factor. | f(0) = 5 and f(3) = 5 × 8 = 40. ~ Each increase of 1 in x multiplies the output by 2.
A quantity starts at 200 and decreases 10% per step. Find its value after two steps. | The multiplier is 1 − 0.10 = 0.9. ~ Model: A(t) = 200(0.9)ᵗ. ~ A(2) = 200 × 0.81 = 162.
''')
add('101','6.2',r'''
What is the domain of bˣ for b > 0? | All real numbers.
What is its range when b ≠ 1? | (0, ∞).
What is the horizontal asymptote of abˣ + k for a ≠ 0? | y = k.
How does a negative a affect abˣ? | It reflects the graph across the x-axis relative to positive |a|.
What happens to the y-intercept after a vertical shift? | The shift is added to the original y-intercept.
---
Analyze y = 2ˣ + 3. | Shift the basic growth curve up 3. ~ Domain: all reals; range: (3, ∞); horizontal asymptote: y = 3. ~ At x = 0, y = 4, so the y-intercept is (0, 4).
Analyze y = −(1/2)ˣ + 1. | Reflect the decay curve across the x-axis, then shift up 1. ~ Domain: all reals; range: (−∞, 1); horizontal asymptote: y = 1. ~ The graph increases and passes through (0, 0).
''')
add('101','6.3',r'''
What does log base b of x mean? | The exponent y such that bʸ = x.
What restrictions apply to a real logarithm? | Argument > 0, base > 0, and base ≠ 1.
What base is used by ln? | e.
What is \(\log_b1\)? | 0.
How are exponentials and logarithms related? | They are inverse functions for the same base.
---
Evaluate \(\log_2 32\) and \(\log_3(1/9)\). | Since 2⁵ = 32, the first value is 5. ~ Since 3⁻² = 1/9, the second value is −2.
Rewrite \(\log_5 125=3\) exponentially and evaluate ln(e²). | The logarithmic statement says 5³ = 125. ~ The inverse relationship gives ln(e²) = 2.
''')
add('101','6.4',r'''
What is the domain of y = log base b of x? | (0, ∞).
What is its range? | All real numbers.
What is its vertical asymptote? | x = 0.
Where does the basic logarithmic graph cross the x-axis? | (1, 0).
For y = log base b of (x − h) + k, what gives the domain? | x − h > 0, so x > h.
---
Analyze y = log₂(x − 3) + 1. | Shift the basic log₂ graph right 3 and up 1. ~ Domain: (3, ∞); range: all real numbers; asymptote: x = 3. ~ Since log₂1 = 0, the point (4, 1) lies on the graph.
Find the intercept and asymptote of y = ln(x + 2). | Require x + 2 > 0, giving domain (−2, ∞) and asymptote x = −2. ~ For y = 0, x + 2 = 1, so the x-intercept is (−1, 0). ~ At x = 0, the y-intercept is (0, ln 2).
''')
add('101','6.5',r'''
State the product rule for logarithms of positive arguments. | \(\log_b(MN)=\log_b M+\log_b N\).
State the quotient rule. | \(\log_b(M/N)=\log_b M-\log_b N\).
State the power rule for positive M. | \(\log_b(M^r)=r\log_b M\).
What is the change-of-base formula? | \(\log_b x=\ln x/\ln b\).
Is log(M + N) equal to log M + log N? | No; there is no corresponding sum rule.
---
Expand \(\ln(3x^2/y)\) for x > 0 and y > 0. | Use product and quotient rules: ln 3 + ln(x²) − ln y. ~ Apply the power rule: ln 3 + 2 ln x − ln y.
Condense \(2\log_3 x-\log_3 5\), x > 0. | Bring 2 into the exponent: log₃(x²) − log₃5. ~ Use the quotient rule to get \(\log_3(x^2/5)\). ~ Retain the original restriction x > 0.
''')
add('101','6.6',r'''
How can an exponential equation be solved when both sides have the same valid base? | Equate the exponents.
How can logarithms solve an exponential equation? | Isolate the exponential, take a logarithm, and use the power rule.
How do you solve log base b of u = c? | Rewrite as u = bᶜ, retaining u > 0.
Why check logarithmic-equation candidates? | The original logarithm arguments must all be positive.
Can a positive-base exponential equal a negative number? | No.
---
Solve \(3^{2x-1}=27\). | Write 27 as 3³. ~ Equate exponents: 2x − 1 = 3. ~ Thus x = 2.
Solve \(\ln(x-1)+\ln(x+1)=\ln8\). | The original domain requires x > 1. ~ Combine and equate positive arguments: (x − 1)(x + 1) = 8. ~ Then x² = 9 gives ±3, but only x = 3 meets the original domain.
''')
add('101','6.7',r'''
What is a continuous exponential growth or decay model? | A(t) = A₀eᵏᵗ.
What does the sign of k indicate? | Positive means growth; negative means decay.
What is doubling time for k > 0? | ln 2 divided by k.
What is half-life for k < 0? | ln 2 divided by |k|.
What does the carrying capacity of a logistic model describe? | Its limiting population level under the model.
---
A quantity starts at 80 and doubles every 3 hours. Find its value after 9 hours. | Write \(A(t)=80\cdot2^{t/3}\). ~ Nine hours is three doubling periods. ~ A(9) = 80 × 8 = 640.
A sample starts at 100 g with a 4-year half-life. Find the mass after 12 years. | Write \(A(t)=100(1/2)^{t/4}\). ~ Twelve years is three half-lives. ~ Remaining mass = 100/8 = 12.5 g.
''')
add('101','6.8',r'''
What data pattern suggests exponential growth? | Approximately constant output ratios over equal input steps.
How does this differ from linear growth? | Linear growth has approximately constant differences.
What is a residual? | Observed output minus model prediction.
Why be cautious with extrapolation? | A fitted pattern may not continue beyond the observed data.
What transformation linearizes y = abˣ when y > 0? | ln y = ln a + x ln b.
---
Fit an exact exponential model to (0, 3), (1, 6), (2, 12). | The initial value is a = 3. ~ Successive ratios are both 2, so b = 2. ~ The model is y = 3(2ˣ); it predicts 24 at x = 3.
A fitted model predicts 50 when x = 4; the observed value is 46. Find the residual and interpret it. | Residual = observed − predicted = 46 − 50 = −4. ~ The point is 4 output units below the model. ~ One residual alone does not establish whether an exponential model is appropriate overall.
''')
add('101','7.1',r'''
What is a solution to a two-equation system? | An ordered pair satisfying both equations.
What does substitution do? | Replace a variable with an equal expression.
What does elimination do? | Combine equations so a variable cancels.
What does a contradiction after elimination mean? | The system is inconsistent and has no solution.
What do dependent equations represent? | The same line, giving infinitely many solutions.
---
Solve 2x + y = 9 and x − y = 3. | Add equations: 3x = 12, so x = 4. ~ Substitute: 4 − y = 3, giving y = 1. ~ Check: 2(4) + 1 = 9 and 4 − 1 = 3.
Classify x + 2y = 4 and 2x + 4y = 8. | The second equation is twice the first. ~ Both represent the same line. ~ Infinitely many solutions: (4 − 2t, t) for any real t.
''')
add('101','7.3',r'''
What makes a system nonlinear? | At least one equation is nonlinear.
What do intersections of the graphs represent? | Ordered pairs solving every equation.
How can substitution solve a line-parabola system? | Substitute the line's expression for y into the parabola's equation.
When is an inequality boundary included? | For ≤ or ≥, use a solid boundary; for < or >, exclude it.
How do you combine inequalities in a system? | Take the overlap of their solution regions.
---
Solve y = x² and y = x + 2. | Set x² = x + 2, so (x − 2)(x + 1) = 0. ~ Inputs are 2 and −1. ~ Substitute to get intersections (2, 4) and (−1, 1).
Describe the region satisfying y ≥ x² and y ≤ 4. | Include both boundaries because both inequalities are inclusive. ~ Shade above the parabola and below the horizontal line. ~ They meet where x² = 4, at x = ±2; the shared region has −2 ≤ x ≤ 2 and x² ≤ y ≤ 4.
''')

add('stats','1.1',r'''
What is a population? | The entire group about which a study seeks information.
What is a sample? | The subset of the population actually observed.
How does a parameter differ from a statistic? | A parameter describes a population; a statistic describes a sample.
What is descriptive statistics? | Organizing and summarizing observed data.
What is inferential statistics? | Using sample evidence to draw conclusions about a population with uncertainty.
---
A university has 4,000 students. A survey of 100 finds mean study time 8 hours per week. Identify population, sample, and statistic. | The population is all 4,000 students; the sample is the 100 surveyed. ~ The sample mean of 8 hours is a statistic. ~ The mean for all 4,000 students would be the population parameter.
A report displays a class's exam average, then predicts the university average from that class. Identify the two types of statistics. | Summarizing the observed class is descriptive. ~ Generalizing to the university is inferential. ~ Whether that inference is justified depends on how representative the class is and on the sampling design.
''')
add('stats','1.2',r'''
How do qualitative and quantitative data differ? | Qualitative data give categories; quantitative data give numerical counts or measurements.
How do discrete and continuous quantitative data differ? | Discrete values are countable; continuous measurements can vary across an interval.
What is a simple random sample of size n? | Every possible subset of n population members has the same selection probability.
How do stratified and cluster sampling differ? | Stratified sampling samples within every stratum; cluster sampling randomly selects clusters and studies their members.
Does a larger sample automatically remove selection bias? | No.
---
Classify eye color, number of courses, and height. | Eye color is qualitative. ~ Number of courses is quantitative discrete. ~ Height is quantitative continuous, even if recorded to a limited precision.
A college samples 10 students at random from every major. Name the design and compare it with selecting three entire majors. | Sampling within every major is stratified sampling. ~ Randomly selecting three majors and surveying all their students is cluster sampling. ~ The designs use groups differently; neither guarantees freedom from nonresponse bias.
''')
add('stats','1.3',r'''
What is frequency? | The count of observations in a category or class.
What is relative frequency? | Frequency divided by total sample size.
What is cumulative frequency? | The running total through an ordered category or class.
What distinguishes nominal from ordinal data? | Ordinal categories have meaningful order; nominal categories do not.
What distinguishes interval from ratio measurements? | Ratio measurements have a meaningful zero and meaningful ratios; interval measurements do not.
---
Ratings low, medium, high have counts 2, 5, 3. Find relative and cumulative frequencies. | Total n = 10; relative frequencies are 0.2, 0.5, 0.3. ~ Cumulative counts in that order are 2, 7, 10. ~ The relative frequencies sum to 1.
Classify blood type, class rank, Celsius temperature, and mass by level of measurement. | Blood type is nominal; rank is ordinal. ~ Celsius is interval because zero does not mean absence of temperature. ~ Mass is ratio because zero and ratios are meaningful.
''')
add('stats','1.4',r'''
How does an experiment differ from an observational study? | An experiment assigns treatments; an observational study records without assigning them.
What is a confounding variable? | A variable whose effect cannot be separated from another explanatory effect in the study.
What is random assignment for? | To balance potential confounders across treatment groups in expectation.
What is blinding? | Concealing treatment assignments from participants or evaluators to reduce bias.
How do random sampling and random assignment serve different purposes? | Sampling supports population generalization; assignment supports causal comparisons.
---
Students choose whether to attend tutoring; attendees score higher. Does this establish tutoring caused the difference? | This is observational because students chose attendance. ~ Motivation or preparation could affect both attendance and scores. ~ The observed association alone does not establish causation.
Design an experiment comparing two study methods. | Randomly assign consenting students to the two methods. ~ Keep study time and the assessment comparable; blind graders to group. ~ Compare outcomes, recording attrition and recognizing the limits of the recruited population.
''')
add('stats','1.5',r'''
What is an operational definition? | A precise statement of how a variable will be measured.
Why record units with measurements? | Without units, recorded values may be ambiguous or incomparable.
Why use the same collection procedure for all participants? | To reduce differences caused by measurement procedures.
What should be done with missing responses? | Record them as missing and report how they are handled; do not silently treat them as zero.
Why protect participants' identities? | To respect privacy and reduce unnecessary disclosure.
---
Plan a small study of student commute times. | Define commute time as minutes from leaving home to arriving on campus for one specified day. ~ Use the same question and units for everyone; record missing responses separately. ~ Obtain appropriate consent and avoid collecting names unless necessary.
A dataset records 12, 18, blank, and 30 minutes. Find the mean of recorded times and report missingness. | Three times were recorded and one is missing. ~ Mean of recorded times = (12 + 18 + 30)/3 = 20 minutes. ~ Dividing by 4 would incorrectly treat the blank as zero; report the missing response.
''')
add('stats','1.6',r'''
Why do two random samples usually give different summaries? | Sampling variability.
What is a sampling frame? | The list or mechanism from which a sample is selected.
What can happen if the frame omits part of the population? | Undercoverage bias.
How can a simple random sample be selected reproducibly? | Label population members, use a random selection method, and record the procedure or seed.
Does one unusual sample prove random sampling failed? | No; random samples can differ by chance.
---
Select a simple random sample of 5 from a class roster of 30. Describe the procedure. | Label students 1 through 30. ~ Use a random-number tool to choose 5 distinct labels without replacement. ~ Record the method and selected labels; each possible five-student subset should have equal probability.
Two samples estimate mean commute time as 18 and 22 minutes. Explain the difference. | Different selected students can yield different means even under the same sound method. ~ This is sampling variability. ~ Without more information, neither mean can be declared the exact population mean or proof of bias.
''')
add('stats','2.1',r'''
What does a stem-and-leaf plot preserve? | Individual data values, along with distribution shape.
Why must a stemplot have a key? | The key explains each stem and leaf's place value and units.
What does a bar graph compare? | Frequencies or values for categories.
Why are gaps commonly used between bars in a categorical bar graph? | To distinguish separate categories.
What should every graph label clearly? | Variables, units, and any scale or encoding needed to interpret it.
---
Make a stemplot for 12, 15, 15, 21, 24. | Use tens as stems and ones as leaves. ~ Stem 1 has leaves 2, 5, 5; stem 2 has leaves 1, 4. ~ Key: 1 | 2 means 12. Repeated leaves preserve repeated observations.
A class has 8 biology majors, 5 business majors, and 7 other majors. Describe a bar graph. | Put the three categories on the horizontal axis and student counts on the vertical axis. ~ Draw separate bars of heights 8, 5, and 7 on a scale starting at zero. ~ The total count is 20; biology is the largest category.
''')
add('stats','2.2',r'''
What type of data is a histogram designed for? | Quantitative data grouped into numerical intervals.
What must be true of histogram classes? | They should not overlap and should account for the observations.
What is a frequency polygon? | Class-midpoint frequencies plotted and connected by line segments.
What is a time-series graph? | Measurements plotted in time order.
Why distinguish frequency from relative frequency on an axis? | One shows counts; the other shows proportions or percentages.
---
Group 1, 2, 2, 4, 5, 7 into classes [0, 3), [3, 6), [6, 9). | The first class contains 1, 2, 2: frequency 3. ~ The second contains 4, 5: frequency 2; the third contains 7: frequency 1. ~ Equal-width histogram bars have heights 3, 2, 1; midpoint-frequency pairs are (1.5, 3), (4.5, 2), (7.5, 1).
Values on Monday, Tuesday, Wednesday are 10, 14, 11. Describe their time-series graph. | Plot the values against days in chronological order. ~ Connect consecutive days to show a rise of 4 followed by a fall of 3. ~ Reordering the days by value would destroy the time pattern.
''')
add('stats','2.3',r'''
What does the median divide ordered data into? | A lower half and an upper half, with the middle value or middle pair determining the median.
What do Q₁ and Q₃ represent? | The first and third quartiles, near the 25th and 75th percentiles.
What is the interquartile range? | IQR = Q₃ − Q₁.
Why sort data before locating quartiles? | Quartiles describe positions in the ordered distribution.
Can quartile algorithms give slightly different answers? | Yes, especially for small datasets; state and consistently use the chosen convention.
---
Find the median and quartiles of 1, 3, 5, 7, 9, 11, 13, 15 using medians of halves. | The median is (7 + 9)/2 = 8. ~ The lower half is 1, 3, 5, 7, giving Q₁ = 4. ~ The upper half is 9, 11, 13, 15, giving Q₃ = 12; IQR = 8.
Interpret a 90th-percentile score of 82. | The cutoff is near the point at or below which 90% of scores lie, subject to the percentile convention and ties. ~ It is a position in the distribution. ~ It does not mean the student answered 90% of questions correctly.
''')
add('stats','2.4',r'''
What five numbers summarize an ordinary box plot? | Minimum, Q₁, median, Q₃, maximum.
What does the box span? | Q₁ to Q₃, the middle half of the distribution approximately.
What are the usual outlier fences? | Q₁ − 1.5 IQR and Q₃ + 1.5 IQR.
Where do whiskers end on a modified box plot? | At the most extreme observed values within the fences.
Does an outlier flag prove a recording error? | No; investigate it in context.
---
With Q₁ = 10 and Q₃ = 18, find fences and classify 31. | IQR = 18 − 10 = 8. ~ Fences: 10 − 12 = −2 and 18 + 12 = 30. ~ 31 exceeds the upper fence, so it is flagged as an outlier.
Describe an ordinary box plot with five-number summary 2, 4, 7, 10, 15. | Draw a box from 4 to 10 with a median line at 7. ~ Draw whiskers to 2 and 15. ~ The IQR is 10 − 4 = 6 and the range is 15 − 2 = 13.
''')
add('stats','2.5',r'''
How is the arithmetic mean calculated? | Sum the observations and divide by their count.
How is the median found for an even number of observations? | Sort the values and average the two middle values.
What is a mode? | A most frequent data value; there may be more than one.
Which center is more resistant to extreme values? | The median.
How is a weighted mean calculated? | Sum value × weight and divide by the sum of weights.
---
Find mean, median, and mode for 2, 4, 4, 6, 14. | The sum is 30, so the mean is 30/5 = 6. ~ The middle sorted value is 4, so median = 4. ~ The most frequent value is 4, so mode = 4.
Scores 70 and 90 have weights 1 and 3. Find the weighted mean. | Multiply and sum: 70(1) + 90(3) = 340. ~ Total weight = 4. ~ Weighted mean = 340/4 = 85.
''')
add('stats','2.6',r'''
How is skewness named? | By the direction of the longer tail.
Which way does a right-skewed distribution's tail extend? | Toward larger values.
How do outliers affect the mean compared with the median? | The mean is generally pulled more strongly toward extreme values.
What relationship often holds between mean and median under right skew? | Mean is often greater than median; this is a heuristic, not an infallible rule.
Does symmetry guarantee a single mode? | No; symmetric distributions can be multimodal.
---
Find mean and median for 1, 2, 2, 3, 12, and describe the tail. | The sum is 20, so mean = 4. ~ Median = 2. ~ The large value 12 extends the right tail and pulls the mean above the median.
Describe the shape of 0, 0, 2, 4, 4. | The values are symmetric about 2. ~ Mean and median are both 2. ~ Both 0 and 4 are modes, showing symmetry does not require one central mode.
''')
add('stats','2.7',r'''
What is the range? | Maximum minus minimum.
How is population variance calculated? | Average the squared deviations from the population mean, dividing by N.
How is sample variance calculated? | Sum squared deviations from the sample mean and divide by n − 1.
How is standard deviation related to variance? | It is the nonnegative square root of variance.
What does the empirical rule say for an approximately normal distribution? | About 68%, 95%, and 99.7% lie within 1, 2, and 3 standard deviations of the mean.
---
For the sample 2, 4, 6, find range, variance, and standard deviation. | Mean = 4; deviations are −2, 0, 2 and squared deviations sum to 8. ~ Range = 6 − 2 = 4; sample variance = 8/(3 − 1) = 4. ~ Sample standard deviation = √4 = 2. If these were the entire population, variance would instead be 8/3.
An approximately normal population has mean 70 and SD 5. Estimate the percentage between 60 and 80. | Both bounds are 10 units, or 2 SD, from the mean. ~ The empirical rule gives approximately 95% within this interval.
''')
add('stats','3.1',r'''
What is a sample space? | The set of all possible outcomes of an experiment.
What is an event? | A subset of the sample space.
What is the complement of an event? | All outcomes in the sample space that are not in the event.
What does conditional probability P(A|B) mean? | The probability of A when the outcome is known to be in B, with P(B) > 0.
What is the possible range of a probability? | From 0 to 1 inclusive.
---
Roll a fair six-sided die. Give the event of an even number and its probability. | Sample space: {1, 2, 3, 4, 5, 6}; event: {2, 4, 6}. ~ Three of six equally likely outcomes are favorable. ~ Probability = 3/6 = 1/2.
For the same die, find P(even | greater than 3). | The condition restricts outcomes to {4, 5, 6}. ~ Two of these, 4 and 6, are even. ~ Conditional probability = 2/3.
''')
add('stats','3.2',r'''
What does independence mean? | Knowing one event occurred does not change the other's probability.
What does mutually exclusive mean? | The events cannot occur together.
What product rule holds for independent A and B? | P(A and B) = P(A)P(B).
Can two mutually exclusive events with positive probabilities be independent? | No; occurrence of one rules out the other.
Does sampling without replacement usually preserve independence? | No; the first selection changes the remaining population.
---
A fair coin is tossed twice. Are first-toss heads and second-toss heads independent? | Each has probability 1/2; both together have probability 1/4. ~ Since 1/4 = (1/2)(1/2), they are independent. ~ They are not mutually exclusive because HH is possible.
A fair die is rolled. Are rolling 1 and rolling 2 independent? | The events cannot occur together, so they are mutually exclusive. ~ Their joint probability is 0, while the product is 1/36. ~ They are not independent.
''')
add('stats','3.3',r'''
State the general addition rule. | P(A or B) = P(A) + P(B) − P(A and B).
State the general multiplication rule. | P(A and B) = P(A)P(B|A), when P(A) > 0.
Why subtract the overlap in the addition rule? | It was counted once in each individual probability.
What is the complement rule? | P(not A) = 1 − P(A).
When may P(B|A) be replaced by P(B)? | When A and B are independent.
---
If P(A) = 0.4, P(B) = 0.3, and P(A and B) = 0.1, find P(A or B). | Add individual probabilities and subtract the overlap. ~ 0.4 + 0.3 − 0.1 = 0.6.
A bag has 3 red and 2 blue objects. Draw two without replacement. Find P(both red). | The first-red probability is 3/5. ~ After a red is removed, the second-red probability is 2/4. ~ Multiply: (3/5)(2/4) = 3/10.
''')
add('stats','3.4',r'''
What does a contingency table display? | Counts classified by two categorical variables.
What is a joint probability? | A probability involving both a row category and a column category.
How do you find a marginal probability? | Divide a row or column total by the grand total.
What denominator is used for a conditional probability? | The total for the conditioning group.
How can a table be used to check independence? | Compare a conditional probability with its matching marginal, or a joint probability with the product of marginals.
---
Of 40 students, 10 take tutoring and pass, 5 take tutoring and fail, 20 skip tutoring and pass, and 5 skip tutoring and fail. Find P(pass) and P(tutoring and pass). | Passing total = 10 + 20 = 30, so P(pass) = 30/40 = 3/4. ~ The joint count is 10, so P(tutoring and pass) = 10/40 = 1/4.
Using those same counts, find P(pass | tutoring) and check independence. | There are 10 + 5 = 15 tutoring students. ~ P(pass | tutoring) = 10/15 = 2/3. ~ This differs from P(pass) = 3/4, so the two events are not independent in this probability table.
''')
add('stats','3.5',r'''
What does a branch probability in a tree describe? | The probability of the next outcome conditional on that branch's history.
How is a complete path probability found? | Multiply conditional probabilities along the path.
How are probabilities of disjoint qualifying paths combined? | Add them.
What does the overlap in a Venn diagram represent? | Outcomes in both events.
What belongs outside both circles but inside the sample space? | Outcomes in neither event.
---
A bag has 2 red and 1 blue object. Draw two without replacement. Find P(exactly one red) using paths. | Red then blue has probability (2/3)(1/2) = 1/3. ~ Blue then red has probability (1/3)(2/2) = 1/3. ~ Add these disjoint paths to get 2/3.
Of 30 people, 18 like tea, 14 like coffee, and 8 like both. Fill the Venn regions. | Tea only: 18 − 8 = 10; coffee only: 14 − 8 = 6. ~ Both: 8; total in either: 10 + 8 + 6 = 24. ~ Neither: 30 − 24 = 6.
''')
add('stats','4.1',r'''
What is a random variable? | A numerical value assigned to each outcome of a random experiment.
What makes a random variable discrete? | Its possible values form a finite or countable set.
What two conditions must a discrete probability table satisfy? | Every probability is between 0 and 1, and all probabilities sum to 1.
How do you calculate P(X in a set) from a discrete table? | Add probabilities for the listed values in that set.
What is the support of a discrete random variable? | Its possible values with positive probability.
---
X has values 0, 1, 2 with probabilities 0.2, 0.5, 0.3. Verify validity and find P(X ≥ 1). | All probabilities lie between 0 and 1 and sum to 1. ~ P(X ≥ 1) = 0.5 + 0.3 = 0.8.
A table lists probabilities 0.15, 0.25, and k for three possible outcomes. Find k. | A complete distribution must sum to 1. ~ k = 1 − 0.15 − 0.25 = 0.60. ~ This is a valid probability because it lies between 0 and 1.
''')
add('stats','4.2',r'''
What is the expected value of a discrete random variable? | \(\mu=\sum_x xP(X=x)\).
Must an expected value be a possible individual outcome? | No; it is a long-run average under the model.
What is its population variance? | \(\sigma^2=\sum_x(x-\mu)^2P(X=x)\).
What is its standard deviation? | The square root of its variance, in the same units as X.
What does a larger standard deviation mean in a payoff comparison? | Greater variability in payoff; it does not by itself determine which option is preferred.
---
A net payoff is −$2 with probability 0.75 or $6 with probability 0.25. Find expected payoff and SD. | Mean: (−2)(0.75) + 6(0.25) = $0. ~ Variance: (−2 − 0)²(0.75) + (6 − 0)²(0.25) = 12 dollars squared. ~ SD = √12 ≈ $3.46.
Compare a guaranteed $2 with a payoff of $0 or $4, each with probability 1/2. | Both means are $2. ~ The guarantee has SD 0. The variable payoff has variance (0 − 2)²/2 + (4 − 2)²/2 = 4 and SD $2. ~ A person preferring less variability at the same mean would choose the guarantee.
''')
add('stats','4.3',r'''
What does a binomial random variable count? | Successes in a fixed number of independent two-outcome trials with constant success probability.
What parameters define it? | Number of trials n and success probability p.
What are its possible values? | 0, 1, …, n.
What is P(X = k)? | \(\binom{n}{k}p^k(1-p)^{n-k}\).
What are its mean and standard deviation? | \(\mu=np\) and \(\sigma=\sqrt{np(1-p)}\).
---
For three independent trials with p = 0.5, find P(exactly two successes). | There are \(\binom{3}{2}=3\) success/failure arrangements. ~ Each has probability (0.5)³ = 1/8. ~ Total probability = 3/8 = 0.375.
For a binomial model with n = 20 and p = 0.3, find mean and SD. | Mean = np = 20(0.3) = 6 successes. ~ Variance = 20(0.3)(0.7) = 4.2. ~ SD = √4.2 ≈ 2.05 successes.
''')
add('stats','4.4',r'''
What does X count in this course's geometric model? | The trial number of the first success, beginning at 1.
What assumptions are required? | Independent trials with a constant success probability p, where 0 < p ≤ 1.
What is P(X = k)? | \((1-p)^{k-1}p\), for k = 1, 2, … .
What is P(X > k)? | \((1-p)^k\), the probability of k initial failures.
What are mean and SD? | \(1/p\) and \(\sqrt{1-p}/p\), respectively.
---
With p = 0.25, find the probabilities of first success on trials 1, 2, and 3. | Trial 1: 0.25. ~ Trial 2: 0.75(0.25) = 0.1875. ~ Trial 3: (0.75)²(0.25) = 0.140625; the pattern is p, qp, q²p.
With p = 0.2, find P(X > 3) and E(X). | X > 3 means the first three trials all fail. ~ Probability = (0.8)³ = 0.512. ~ Mean trial number = 1/0.2 = 5.
''')
add('stats','4.5',r'''
What does a hypergeometric random variable count? | Successes in a fixed-size random sample without replacement from a finite population.
What parameters are needed? | Population size N, number of population successes K, and sample size n.
Why are draws generally dependent? | Each draw changes the remaining population.
What is P(X = k)? | \(\binom{K}{k}\binom{N-K}{n-k}/\binom{N}{n}\).
What are the feasible values of X? | Integers from max(0, n − (N − K)) to min(n, K).
---
A box has 3 red and 2 blue objects. Choose 2 uniformly without replacement. Find P(exactly one red). | Choose 1 of 3 red and 1 of 2 blue: 3 × 2 = 6 favorable samples. ~ All two-object samples: \(\binom{5}{2}=10\). ~ Probability = 6/10 = 0.6.
With N = 10, K = 4, and n = 3, find the support and mean. | The smallest possible success count is max(0, 3 − 6) = 0; the largest is min(3, 4) = 3. ~ Support: 0, 1, 2, 3. ~ Mean = nK/N = 3(4)/10 = 1.2 successes.
''')
add('stats','4.6',r'''
What does a Poisson random variable count? | Events in a fixed interval of time, space, area, or another exposure.
What parameter defines the distribution? | λ, the expected count for that exposure.
What assumptions support a Poisson process model? | A constant average rate, independent increments, and negligible probability of multiple events in a sufficiently small exposure.
What is P(X = k)? | \(e^{-\lambda}\lambda^k/k!\), k = 0, 1, 2, … .
What are its mean and variance? | Both equal λ; the SD is √λ.
---
Calls follow a Poisson model averaging 2 per minute. Find P(no calls in one minute). | The exposure is one minute, so λ = 2. ~ P(X = 0) = e⁻²(2⁰)/0! = e⁻² ≈ 0.1353.
Defects average 3 per square meter under a Poisson model. Find the mean and SD in 2 square meters. | Double the exposure, so λ = 3 × 2 = 6. ~ Expected count = 6 defects. ~ SD = √6 ≈ 2.45 defects.
''')
add('stats','5.1',r'''
How are continuous probabilities represented by a density curve? | As areas under the curve over intervals.
What is the total area under a density curve? | 1.
Can a density be negative? | No.
What is P(X = c) for a continuous random variable? | 0 for any single value c.
Do including or excluding interval endpoints change continuous probabilities? | No; individual endpoints have probability zero.
---
A density equals 0.25 on [0, 4] and zero elsewhere. Verify it and find P(1 < X < 3). | The density is nonnegative and its total area is 4(0.25) = 1. ~ The requested interval has width 2. ~ Its area and probability are 2(0.25) = 0.5.
For a continuous X, suppose P(X ≤ 7) = 0.8. Find P(X > 7) and P(X = 7). | The complement probability is 1 − 0.8 = 0.2. ~ The probability of the individual point 7 is zero. ~ Therefore P(X ≥ 7) is also 0.2.
''')
add('stats','5.2',r'''
What is a uniform density on [a, b]? | A constant density 1/(b − a), with b > a.
How is probability found within its support? | Interval length divided by total support length.
What is its mean? | (a + b)/2.
What is its standard deviation? | \((b-a)/\sqrt{12}\).
Do equal-length subintervals have equal probabilities? | Yes, when both lie within the support.
---
A waiting time is uniform from 0 to 10 minutes. Find P(2 ≤ X ≤ 5). | The interval length is 3; the full support length is 10. ~ Probability = 3/10 = 0.3.
For X uniform on [4, 16], find mean and SD. | Mean = (4 + 16)/2 = 10. ~ SD = (16 − 4)/√12 = √12 ≈ 3.46. ~ A central interval [7, 13] has probability 6/12 = 0.5.
''')
add('stats','5.3',r'''
What does the exponential model commonly measure? | Waiting time to the next event in a constant-rate Poisson process.
Using rate λ, what is its mean? | 1/λ.
Using rate λ, what is P(X > t) for t ≥ 0? | \(e^{-\lambda t}\).
What is its standard deviation? | 1/λ, equal to its mean.
What is the memoryless property? | P(X > s + t | X > s) = P(X > t), for nonnegative s and t.
---
A waiting time is exponential with mean 5 minutes. Find P(X > 10). | Rate λ = 1/5 per minute. ~ P(X > 10) = e⁻² ≈ 0.1353.
With rate 0.5 per minute, find the probability of waiting at most 2 minutes. | P(X ≤ 2) = 1 − P(X > 2). ~ This equals 1 − e⁻¹ ≈ 0.6321. ~ The mean waiting time is 1/0.5 = 2 minutes.
''')
add('stats','6.1',r'''
What are the mean and SD of the standard normal distribution? | Mean 0 and SD 1.
How do you standardize a normal value x? | \(z=(x-\mu)/\sigma\).
What does a negative z-score mean? | The value lies below the mean.
What area lies on each side of the standard normal mean? | 0.5.
What does a z-score measure? | Distance from the mean in standard-deviation units.
---
A normal variable has mean 100 and SD 15. Standardize x = 130. | z = (130 − 100)/15 = 2. ~ The value is two SD above the mean. ~ For a normal variable, the area below z = 2 is approximately 0.9772.
For standard normal Z, use P(Z ≤ 1) ≈ 0.8413 to find P(Z > 1) and P(−1 < Z < 1). | The upper tail is 1 − 0.8413 = 0.1587. ~ Symmetry gives P(Z ≤ −1) ≈ 0.1587. ~ Middle area ≈ 0.8413 − 0.1587 = 0.6826.
''')
add('stats','6.2',r'''
How is a normal interval probability calculated after standardizing? | Subtract the lower cumulative area from the upper cumulative area.
How do you find a value from a known z-score? | x = μ + zσ.
What is a percentile cutoff? | A value with the specified cumulative proportion at or below it.
What must be specified to use a normal model for an individual measurement? | A justified normal distribution with its mean and SD.
How do you find an upper-tail probability? | Subtract the cumulative probability from 1.
---
Let X be normal with mean 50 and SD 10. Find P(40 < X < 60). | Standardize bounds to −1 and 1. ~ Standard normal cumulative areas are approximately 0.1587 and 0.8413. ~ Probability ≈ 0.6826.
Find the 95th percentile of a normal population with mean 70 and SD 8. | The standard normal 95th-percentile z is approximately 1.645. ~ x = 70 + 1.645(8) = 83.16. ~ Approximately 95% of model values lie at or below 83.16.
''')
add('stats','7.1',r'''
What is a sampling distribution of the sample mean? | The distribution of means from repeated samples of the same size under the sampling model.
What is its mean for independent identically distributed observations with finite mean? | The population mean μ.
What is its standard error when the population SD is σ? | \(\sigma/\sqrt n\).
What does the Central Limit Theorem say? | With suitable independent observations and finite variance, standardized sample means approach a normal distribution as sample size grows.
Does n = 30 guarantee a good normal approximation for every population? | No; adequacy depends on skewness, outliers, tails, and sampling conditions.
---
A population has mean 80 and SD 12. For independent samples of size 36, find mean and SE of the sample mean. | Sampling-distribution mean = 80. ~ SE = 12/√36 = 2. ~ Its shape is exactly normal for a normal population, or approximately normal if CLT conditions and sample size make the approximation adequate.
From a normal population with mean 50 and SD 10, take n = 25 independent observations. Find P(sample mean > 54). | The sample mean is normal with SE = 10/5 = 2. ~ z = (54 − 50)/2 = 2. ~ Upper-tail probability ≈ 0.0228.
''')
add('stats','7.2',r'''
What is the expected sum of n independent identically distributed observations with mean μ? | nμ.
What is the variance of their sum if each has variance σ²? | nσ².
What is the SD of their sum? | \(\sigma\sqrt n\).
How is a sum related to the sample mean? | S = n times the sample mean.
What is essential when adding variances without covariance terms? | Independence, or at least zero covariance with suitable finite variances.
---
Independent package weights have mean 2 kg and SD 0.3 kg. Find mean and SD for a total of 100 packages. | Mean total = 100(2) = 200 kg. ~ Variance total = 100(0.3²) = 9 kg squared. ~ SD total = 3 kg.
Assume individual measurements are independent normal with mean 10 and SD 2. For 16 measurements, find P(sum > 176). | The sum is normal with mean 160 and SD 2√16 = 8. ~ z = (176 − 160)/8 = 2. ~ Probability ≈ 0.0228.
''')
add('stats','7.3',r'''
What should you identify before standardizing a probability question? | Whether the variable is an individual observation, sample mean, or sum.
Which SD belongs to a sample mean? | σ/√n.
Which SD belongs to a sum of n independent observations? | σ√n.
Why does independence matter? | Dependence can change the variance and invalidate the usual standard-error formulas.
What happens to a mean's SE when sample size quadruples? | It is halved, with the same population SD.
---
A normal population has mean 100 and SD 20. Compare the z-scores for an individual value 110 and a sample mean 110 with n = 16. | Individual z = (110 − 100)/20 = 0.5. ~ Mean SE = 20/4 = 5; mean z = (110 − 100)/5 = 2. ~ The same numerical deviation is more unusual for a sample mean.
How large must n be for a sample mean's SE to be at most 3 if σ = 18? | Solve 18/√n ≤ 3. ~ This requires √n ≥ 6, so n ≥ 36. ~ This precision calculation alone does not establish normality or correct a biased design.
''')
add('stats','8.1',r'''
When is a z interval for a population mean appropriate? | With known population SD σ and a sampling design and normality/large-sample conditions supporting the normal reference model.
What is the z-interval formula? | \(\bar x\pm z^*\sigma/\sqrt n\).
What is a margin of error? | The amount added to and subtracted from the point estimate.
What does 95% confidence describe? | In repeated sampling, about 95% of intervals from the procedure contain the fixed population parameter under the assumptions.
How does increasing confidence affect width with other factors fixed? | It makes the interval wider.
---
For x̄ = 50, known σ = 10, n = 100, find a 95% z interval, assuming conditions hold. | SE = 10/√100 = 1; use z* ≈ 1.96. ~ Margin = 1.96. ~ Interval: (48.04, 51.96), estimating the population mean.
Plan a 95% mean interval with margin at most 2 and known σ = 10. Find n. | Use \(n\geq(z^*\sigma/E)^2\). ~ (1.96 × 10/2)² = 96.04. ~ Round upward to n = 97, subject to the study design assumptions.
''')
add('stats','8.2',r'''
Why use Student's t for a mean interval? | The population SD is unknown and is estimated with sample SD s.
What degrees of freedom are used for a one-sample t interval? | n − 1.
What is its standard error estimate? | s/√n.
What is the interval formula? | \(\bar x\pm t^*s/\sqrt n\).
What conditions need special care for a small sample? | Independent observations from an approximately normal population without severe outliers.
---
For x̄ = 20, s = 4, n = 16, find a 95% t interval using t* = 2.131 and assuming conditions hold. | df = 15 and estimated SE = 4/4 = 1. ~ Margin = 2.131. ~ Interval: (17.869, 22.131), approximately (17.87, 22.13).
Two samples have the same x̄ = 30 and s = 6. Compare n = 9 and n = 36 using supplied 95% critical values 2.306 and 2.030. | For n = 9, margin = 2.306(6/3) = 4.612. ~ For n = 36, margin = 2.030(6/6) = 2.030. ~ The larger sample gives a narrower interval under the same appropriate assumptions.
''')
add('stats','8.3',r'''
What is the sample proportion? | Number of successes divided by sample size: p̂ = x/n.
What is the usual normal-approximation confidence interval for a proportion? | \(\hat p\pm z^*\sqrt{\hat p(1-\hat p)/n}\).
What counts should be checked before using that interval? | Observed successes and failures must both be sufficiently large; use at least 10 of each here.
What design assumptions matter? | A suitable random sample and independent observations; for sampling without replacement, the sample should be a small fraction of the population.
What planning value gives the largest required sample size when p is unknown? | p = 0.5.
---
In a suitable random sample, 60 of 100 respondents answer yes. Find an approximate 95% interval. | p̂ = 0.60; counts are 60 successes and 40 failures, meeting the count check. ~ SE = √(0.6 × 0.4/100) ≈ 0.04899; margin ≈ 1.96(0.04899) = 0.09602. ~ Interval ≈ (0.504, 0.696).
Plan a 95% proportion interval with margin at most 0.05 and no prior estimate. | Use p = 0.5 and \(n\geq(z^*/E)^2p(1-p)\). ~ (1.96/0.05)²(0.25) = 384.16. ~ Round upward to n = 385; this does not address selection bias.
''')
add('stats','9.0',r'''
What do null and alternative hypotheses describe? | Competing claims about a population parameter, with the equality boundary in the null.
What is a p-value? | Assuming the null model and its conditions, the probability of a result at least as extreme as observed in the direction(s) of the alternative.
What is a Type I error? | Rejecting a true null hypothesis.
What is a Type II error? | Failing to reject a false null hypothesis.
How is a test decision made using α? | Reject H₀ if p-value ≤ α; otherwise fail to reject H₀.
---
A claim is that mean completion time is 12 minutes. Test whether it differs, given p-value 0.03 and α = 0.05. | Set H₀: μ = 12 and Hₐ: μ ≠ 12. ~ Because 0.03 < 0.05, reject H₀. ~ The data provide evidence that the population mean differs from 12, assuming the test's conditions hold; the p-value is not the probability that H₀ is true.
A test for p > 0.60 has p-value 0.18 at α = 0.05. State the conclusion and describe a possible Type II error. | Since 0.18 > 0.05, fail to reject H₀. ~ There is insufficient evidence that the population proportion exceeds 0.60; this does not prove the null. ~ A Type II error would occur if the true proportion exceeds 0.60 but the test fails to detect it.
''')
