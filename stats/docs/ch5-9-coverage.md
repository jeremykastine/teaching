# Chapters 5-9: coverage and prerequisite connections

These original discussion prompts follow the selected sections of OpenStax *Introductory Statistics 2e* by Barbara Illowsky and Susan Dean. Chapter 9 is a conceptual overview, rather than the textbook's full collection of computational procedures. Each page asks one focused question and leaves the explanation and worked solution to the instructor.

See the [complete textbook coverage audit](textbook-coverage-audit.md) for terminology and problem-type evidence by PDF page.

## Section coverage

| Section | Slides | Main objectives | Small reinforcement for later sections |
|---|---:|---|---|
| 5.1 Continuous Probability Functions | 18 | Density properties; interval area; exact versus rounded values; cumulative probabilities; complements; percentile meaning. | Reading upper tails and probabilities between cutoffs prepares normal calculations and p-value interpretation. |
| 5.2 The Uniform Distribution | 20 | Support, density, mean, SD, interval probabilities, percentiles, conditional probability, and checking a model. | One observation versus an average prepares the uniform examples in Chapter 7. |
| 5.3 The Exponential Distribution | 28 | Waiting-time variables, rate and units, mean and SD, tail and interval probabilities, percentiles, memorylessness, and Poisson-process connections. | Reciprocal rate/mean and one time versus an average prepare exponential CLT applications. |
| 6.1 The Standard Normal Distribution | 22 | Normal parameters, standardization, recovering values, symmetry, empirical-rule regions, and cumulative-table interpretation. | A z-score is a location, not a probability; standardization alone does not establish normality. |
| 6.2 Using the Normal Distribution | 26 | Lower, upper, and interval probabilities; complements; percentiles, quartiles, central regions, conditional probability, and model limitations. | Upper-tail cutoffs prepare critical values; individual mass versus average mass prepares standard error. |
| 7.1 The Central Limit Theorem for Sample Means (Averages) | 28 | Sampling distributions, their center, standard error, sample-size effects, normality conditions, probability calculations, and percentiles. | Explicit SD/SE distinctions prepare confidence intervals and tests. |
| 7.2 The Central Limit Theorem for Sums | 21 | Mean and SD of sums, normal approximation, total probabilities and percentiles, sum/mean equivalence, dependence, and fixed added quantities. | Reusing the same event as both a sum and a mean strengthens correct scale selection. |
| 7.3 Using the Central Limit Theorem | 37 | Selecting individual, mean, or sum models; uniform and exponential applications; quartiles/IQR and central intervals; normal approximation to the binomial with continuity correction; approximation boundaries; law of large numbers; precision and bias. | Unknown population parameters connect sampling distributions to inference. |
| 8.1 A Single Population Mean using the Normal Distribution | 28 | Point and interval estimates; confidence coverage; critical z; known-SD mean intervals; interpretation; width factors; sample-size planning. | Population mean versus individual values and fixed-parameter coverage prepare conclusions in Chapter 9. |
| 8.2 A Single Population Mean using the Student t Distribution | 26 | Estimated SE; t versus z; degrees of freedom; heavier tails; conditions; t margins and intervals; units; raw-data construction. | Using t when population SD is unknown prepares the matching interval/test connection. |
| 8.3 A Population Proportion | 32 | Count/proportion distinction; sample notation; estimated SE; normal-approximation intervals; conditions; plus-four adjustment; interpretation; planning. | Population p, sample estimate, and hypothesized p remain distinct; percentages and percentage points are distinguished. |
| 9.0 Hypothesis Testing: Conceptual Overview | 31 | Null/alternative hypotheses; direction; null sampling models; test statistics; p-values; significance; errors; power; practical importance; CI connection. | Integrates sampling design, probability tails, standard error, and confidence-interval interpretation. |

## Mathematical conventions and assumptions

- `N(μ,σ)` follows this textbook's mean/standard-deviation convention.
- CLT prompts distinguish exact normal results for independent normal observations from large-sample approximations. The general version requires independent, identically distributed observations with finite variance; no universal sample-size cutoff is asserted.
- Sampling without replacement uses the common sample-fraction guideline of at most 10% when invoking approximate independence. Random selection does not repair dependence or selection bias.
- Exponential and Poisson links refer to a constant-rate Poisson process. Waiting-time means are reciprocal to rates; count means also depend on interval length. Memoryless times are nonnegative.
- The binomial normal approximation in §7.3 includes the textbook’s expected-count criteria and all five equality/inequality continuity corrections.
- Mean intervals use z with known population SD and t with estimated population SD. Small-sample t questions state normality or ask whether skewness and outliers undermine the method.
- The ordinary proportion interval follows the textbook's rule of more than five observed successes and more than five observed failures. Its standard error uses the sample proportion. The plus-four method uses `(x+2)/(n+4)`, with the textbook's recommendation of confidence at least 90% and sample size at least 10.
- Confidence statements concern repeated-procedure coverage of a fixed parameter. They do not assign a post-data probability to a fixed parameter or describe the percentage of individual observations inside a mean interval.
- The confidence-interval/test equivalence is restricted to matching two-sided mean procedures. A proportion test's null-model SE is distinguished conceptually from an interval's estimated SE; full test calculations remain outside the Chapter 9 overview.

## Textbook references

The following primary OpenStax section titles, objectives, and relevant conditions were checked again in the October 8, 2026 full coverage review. Prompts, numerical scenarios, and synthetic data are original.

- [5.1 Continuous Probability Functions](https://openstax.org/books/introductory-statistics-2e/pages/5-1-continuous-probability-functions)
- [5.2 The Uniform Distribution](https://openstax.org/books/introductory-statistics-2e/pages/5-2-the-uniform-distribution)
- [5.3 The Exponential Distribution](https://openstax.org/books/introductory-statistics-2e/pages/5-3-the-exponential-distribution)
- [6.1 The Standard Normal Distribution](https://openstax.org/books/introductory-statistics-2e/pages/6-1-the-standard-normal-distribution)
- [6.2 Using the Normal Distribution](https://openstax.org/books/introductory-statistics-2e/pages/6-2-using-the-normal-distribution)
- [7.1 The Central Limit Theorem for Sample Means (Averages)](https://openstax.org/books/introductory-statistics-2e/pages/7-1-the-central-limit-theorem-for-sample-means-averages)
- [7.2 The Central Limit Theorem for Sums](https://openstax.org/books/introductory-statistics-2e/pages/7-2-the-central-limit-theorem-for-sums)
- [7.3 Using the Central Limit Theorem](https://openstax.org/books/introductory-statistics-2e/pages/7-3-using-the-central-limit-theorem)
- [8.1 A Single Population Mean using the Normal Distribution](https://openstax.org/books/introductory-statistics-2e/pages/8-1-a-single-population-mean-using-the-normal-distribution)
- [8.2 A Single Population Mean using the Student t Distribution](https://openstax.org/books/introductory-statistics-2e/pages/8-2-a-single-population-mean-using-the-student-t-distribution)
- [8.3 A Population Proportion](https://openstax.org/books/introductory-statistics-2e/pages/8-3-a-population-proportion)
- [Chapter 9 Introduction](https://openstax.org/books/introductory-statistics-2e/pages/9-introduction)
- [9.1 Null and Alternative Hypotheses](https://openstax.org/books/introductory-statistics-2e/pages/9-1-null-and-alternative-hypotheses)
- [9.2 Outcomes and the Type I and Type II Errors](https://openstax.org/books/introductory-statistics-2e/pages/9-2-outcomes-and-the-type-i-and-type-ii-errors)
- [9.4 Rare Events, the Sample, Decision and Conclusion](https://openstax.org/books/introductory-statistics-2e/pages/9-4-rare-events-the-sample-decision-and-conclusion)

- [9.3 Probability Distribution Needed for Hypothesis Testing](https://openstax.org/books/introductory-statistics-2e/pages/9-3-probability-distribution-needed-for-hypothesis-testing)
- [9.5 Additional Information and Full Hypothesis Test Examples](https://openstax.org/books/introductory-statistics-2e/pages/9-5-additional-information-and-full-hypothesis-test-examples) — terminology and interpretation only, within the conceptual overview scope.
