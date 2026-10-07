# Statistics Chapters 2–4: coverage and connections

These original discussion prompts follow OpenStax **Introductory Statistics 2e** section scope. Numerical datasets are labeled synthetic; abstract probability models and standard fair-coin/die experiments state their assumptions. Definitions and formulas introduce a single discussion task. No student slide contains a solution or worked calculation.

## Chapter 2: Descriptive Statistics

The chapter develops displays, position, center, and spread. Numerical summaries retain units; graph questions require reading the actual display before calculating. Larger emphasis on weighted averages and standard-deviation units prepares Chapters 4, 6, 7, and 8.

| Section | Selected objectives | Prerequisites and later connections | Source |
|---|---|---|---|
| 2.1 | Read and construct keyed stemplots; retain repeated values and empty stems; compare groups; read frequency line graphs; select categorical bar displays. | Builds on Chapter 1 variable types and frequency. Preserves exact values before grouping in 2.2 and numerical summaries in 2.3–2.7. | [OpenStax 2.1](https://openstax.org/books/introductory-statistics-2e/pages/2-1-stem-and-leaf-graphs-stemplots-line-graphs-and-bar-graphs) |
| 2.2 | Assign interval endpoints; read frequency and relative-frequency histograms; vary bin width; identify gaps and tails; build frequency polygons; interpret chronological time series. | Reuses frequencies and relative frequencies. Histogram shape prepares skewness in 2.6 and continuous distributions in Chapters 5–6. | [OpenStax 2.2](https://openstax.org/books/introductory-statistics-2e/pages/2-2-histograms-frequency-polygons-and-time-series-graphs) |
| 2.3 | Compute and interpret medians, quartiles, IQR, percentile ranks, and percentile values; apply the 1.5 IQR fences; handle ties. | Ordering from 2.1; spread of the middle half leads to box plots and robust summaries. Percentiles recur in normal-distribution problems. | [OpenStax 2.3](https://openstax.org/books/introductory-statistics-2e/pages/2-3-measures-of-the-location-of-the-data) |
| 2.4 | Construct and read five-number-summary box plots; distinguish quarter lengths from counts; compare centers and IQRs; distinguish min/max whiskers from modified outlier plots. | Reuses 2.3 directly. Comparison questions prepare choosing summaries and reading distributions without exact observations. | [OpenStax 2.4](https://openstax.org/books/introductory-statistics-2e/pages/2-4-box-plots) |
| 2.5 | Calculate mean, median, and mode; choose a meaningful center; weight frequencies; estimate a grouped mean using midpoints; combine unequal-sized groups; track shifts and unit changes. | Frequency tables supply weights. Weighted means prepare expected value in 4.2; sample/population notation prepares inference. | [OpenStax 2.5](https://openstax.org/books/introductory-statistics-2e/pages/2-5-measures-of-the-center-of-the-data) |
| 2.6 | Identify symmetry and tail direction; compare mean, median, and mode; assess the effect of extreme values; distinguish common patterns from universal rules. | Uses graph shape and center. Symmetry and bell shape prepare the normal model while skewed examples discourage uncritical use of it. | [OpenStax 2.6](https://openstax.org/books/introductory-statistics-2e/pages/2-6-skewness-and-the-mean-median-and-mode) |
| 2.7 | Calculate range, deviations, sample/population variance, and SD; retain variance/SD units; compare spreads; standardize distances; recognize Chebyshev and empirical-rule scopes. | Means and center are reused. Standard-deviation units receive modest extra practice for z scores, sampling distributions, and confidence intervals. | [OpenStax 2.7](https://openstax.org/books/introductory-statistics-2e/pages/2-7-measures-of-the-spread-of-the-data) |

Quartile exercises state the median-of-halves convention and use even-sized samples. Graph datasets have repeated quartile values, so the renderer’s percentile interpolation agrees with the stated convention. Percentile-value questions use the current textbook rule: `i = (k/100)(n + 1)`; an integer selects that position, while a noninteger averages its adjacent positions. Percentile-rank questions include half the tied observations in the count. Other software conventions can differ.

## Chapter 3: Probability Topics

The chapter separates intersection, union, complement, and conditioning before applying rules. Conditioning repeatedly asks which group supplies the denominator. Independence and mutual exclusivity receive distinct examples so repeated-trial models in Chapter 4 have a clear foundation.

| Section | Selected objectives | Prerequisites and later connections | Source |
|---|---|---|---|
| 3.1 | Identify experiment, outcome, sample space, and event; use equally likely outcomes appropriately; interpret complements, AND, inclusive OR, and conditional probabilities. | Counts and relative frequencies from Chapter 1 lead to probability models. Event inequalities prepare Chapter 4 discrete cumulative probabilities. | [OpenStax 3.1](https://openstax.org/books/introductory-statistics-2e/pages/3-1-terminology) |
| 3.2 | Test independence by products and conditional probabilities; distinguish disjoint events; evaluate replacement and shared influences; reject “due” outcomes. | Conditional probability from 3.1 is essential. Independence and constant success probability prepare binomial and geometric models. | [OpenStax 3.2](https://openstax.org/books/introductory-statistics-2e/pages/3-2-independent-and-mutually-exclusive-events) |
| 3.3 | Apply general addition and multiplication rules; compute conditional ratios; use complements for at-least-one questions; distinguish exactly one from at least one; check probability coherence. | Reuses 3.1–3.2. Complement and cumulative reasoning recur in every later distribution; products prepare ordered sequences. | [OpenStax 3.3](https://openstax.org/books/introductory-statistics-2e/pages/3-3-two-basic-rules-of-probability) |
| 3.4 | Read joint and marginal counts; use row/column conditional denominators; complete totals; check independence and mutual exclusivity in tables. | Links frequency tables to event rules. Explicit conditioning groups prevent reversing P(A given B) and P(B given A). | [OpenStax 3.4](https://openstax.org/books/introductory-statistics-2e/pages/3-4-contingency-tables) |
| 3.5 | Construct and read two-stage trees; multiply paths and add disjoint paths; compare replacement designs; read Venn-only, overlap, union, and neither regions. | Visualizes the preceding rules. Conditional tree weights preview probability-weighted means in 4.2 and dependence in 4.5. | [OpenStax 3.5](https://openstax.org/books/introductory-statistics-2e/pages/3-5-tree-and-venn-diagrams) |

The scheduled scope stops at 3.5; the textbook lab sections are not included here. All contingency totals and Venn regions agree. Basic coin trees use independent fair tosses; token trees explicitly use uniform draws without replacement.

## Chapter 4: Discrete Random Variables

The chapter begins by separating a random variable from one realization. The common distribution, inequality, complement, expectation, and spread ideas recur across models. Model-selection questions focus on experimental design rather than recognizing a keyword.

| Section | Selected objectives | Prerequisites and later connections | Source |
|---|---|---|---|
| 4.1 | Define discrete random variables and support; map outcomes to values; construct and validate probability distributions; calculate exact, cumulative, and complementary probabilities. | Combines Chapter 1 variables with Chapter 3 events. Support and strict/non-strict inequalities prepare all subsequent distribution calculations. | [OpenStax 4.1](https://openstax.org/books/introductory-statistics-2e/pages/4-1-probability-distribution-function-pdf-for-a-discrete-random-variable) |
| 4.2 | Calculate probability-weighted expected value and variance/SD; interpret a noninteger mean; distinguish expectation from a guaranteed result; calculate net gain and a fair game fee. | Weighted frequency means and squared deviations from 2.5/2.7 are reused. Model mean/SD prepares normal and sampling-distribution notation. | [OpenStax 4.2](https://openstax.org/books/introductory-statistics-2e/pages/4-2-mean-or-expected-value-and-standard-deviation) |
| 4.3 | Check all binomial conditions; define n, p, and success count; count arrangements; calculate exact/cumulative/complement probabilities; interpret np and SD. | Products, independence, complements, and expected value are prerequisites. One expected-success/failure question prepares later normal approximation without teaching that later method here. | [OpenStax 4.3](https://openstax.org/books/introductory-statistics-2e/pages/4-3-binomial-distribution) |
| 4.4 | Check geometric conditions; count trials including success; calculate first-success and tail probabilities; interpret mean/SD; apply precise memorylessness; relate trials to failures. | Reuses independent constant-p trials but changes the stopping rule. Waiting-time questions anticipate the exponential model in Chapter 5. | [OpenStax 4.4](https://openstax.org/books/introductory-statistics-2e/pages/4-4-geometric-distribution) |
| 4.5 | Identify finite sampling without replacement; determine both support bounds; use combinations for exact probabilities; calculate expected sample count; compare exact and approximate binomial designs. | Conditional denominators from Chapter 3 make dependence visible. Population/sample design connects back to Chapter 1. | [OpenStax 4.5](https://openstax.org/books/introductory-statistics-2e/pages/4-5-hypergeometric-distribution) |
| 4.6 | Identify count intervals and Poisson-process assumptions; scale means with units; calculate exact/tail/complement probabilities; use √μ; compare counts, trials, and waiting times. | Complements and expected counts recur. The rare-binomial approximation links 4.3 to 4.6; count versus waiting time prepares the exponential model. | [OpenStax 4.6](https://openstax.org/books/introductory-statistics-2e/pages/4-6-poisson-distribution) |

Geometric formulas consistently use support 1, 2, 3, … for trials through first success. The memoryless statement is `P(X > m + k | X > m) = P(X > k)` for nonnegative integer m, k. The failures-before-success variant is introduced by `X = Y + 1`; no claim equates their means. Poisson examples specify a model or its assumptions rather than inferring a Poisson distribution from an average alone.

## Source counts and verification

- Chapter 2: 128 slides across 7 sections.
- Chapter 3: 92 slides across 5 sections.
- Chapter 4: 114 slides across 6 sections.
- Every slide has a focused question; body text is at most 45 words and questions at most 25 words.
- Mathematical rules, sample spaces, support bounds, table totals, and probability-model assumptions were checked. Layout is validated by the shared renderer before publication.
