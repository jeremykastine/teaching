# Textbook-to-slide coverage audit

Audit date: October 8, 2026 (UTC). Textbook: Barbara Illowsky and Susan Dean, *OpenStax Introductory Statistics 2e*.

## Scope and method

All 36 existing PDF decks were checked against the corresponding online textbook sections, their definitions and highlighted terms, chapter glossaries and reviews, examples, practice and homework problem types. The editable sources were compared with the original PDF page counts, then revised and rebuilt. The current online edition supplies the source of record; the machine-readable audit records the retrieved pages and their SHA-256 hashes.

The course follows `course-schedule.md`: Chapters 1–8 through the selected sections, plus the two existing Chapter 1 labs. Chapter 9 remains one conceptual overview: §§9.1–9.5 supply terminology, assumptions, error classifications, p-value reasoning and interpretation of supplied results. Full numerical hypothesis-test algorithms and unscheduled sections/chapters remain outside this course scope. This is a review of the entire scheduled course, not the entire textbook.

The term tables map highlighted section terminology; the chapter glossary tables provide a second check and capture terms not highlighted in a section. Synonyms, plural forms and alternate notation are mapped to the same underlying definition. The marked word “Pearson” in the §1.1 markup is a person’s surname in a historical reference, not an instructional vocabulary item; it is excluded. The problem tables group examples and exercise variants by the method or reasoning they require, with representative slide pages. Additional terminology from unmarked definitions, graph labels and exercise instructions is included in the relevant problem and glossary mappings. Repeated exercises with different numbers are not duplicated.

Lab contexts are original adaptations (download counts and campus printers); collection, sampling, grouping and interpretation tasks are preserved. Definitions and numeric scenarios are original concise paraphrases/adaptations, with synthetic data labeled. The slides contain questions, not worked solutions.

## Findings and revisions

- §1.1 now explicitly defines numerical/quantitative and categorical/qualitative variables, with classification and complete study-identification prompts. Sampling, datum, representative samples, averages, long-run probability and dot plots are explicit.
- Chapter 1 adds missing sampling/error terminology, replacement conventions, consent/IRB vocabulary and ethical reporting tasks; both labs retain their original procedures and gain omitted grouping/allocation comparisons.
- Chapter 2 adds graph terminology and construction, class boundaries, overlaid polygons, percentile variants, grouped standard deviation, technology notation and standard error.
- Chapters 3–4 add probability terminology and conditional representations, graph/table construction, both geometric counting conventions, hypergeometric SD and Poisson approximation comparisons.
- Chapters 5–6 make PDF/CDF, decay-rate and normal-model terminology explicit and add graphing, inverse calculations and empirical-model comparisons.
- §7.3 now includes the previously absent normal approximation to the binomial, its conditions and all five equality/inequality continuity corrections. Chapters 7–8 gain quartile/IQR, inverse, raw-data and interval-diagram tasks and textbook notation.
- Chapter 9 gains terminology and interpretation coverage while retaining its scheduled conceptual scope.

## Conventions and source issues

- Normal notation is `N(μ, σ)`, with standard deviation as the second parameter, matching this textbook.
- Percentile-value prompts explicitly use the current §2.3 rule `i = (k/100)(n + 1)`: an integer picks that position; a noninteger averages adjacent positions. Percentile ranks count half of ties. Quartiles use the stated median-of-halves convention; the odd-size example excludes the median. Software conventions differ, so the rule is stated on the relevant prompts.
- Geometric trials-through-success and failures-before-success differ by one. Their means differ by one and their standard deviations are equal. The textbook’s inconsistent claim that changing the convention changes SD is not reproduced.
- Hypergeometric SD uses the finite-population factor `(N − n)/(N − 1)`.
- Binomial normal approximation uses the textbook’s `np > 5` and `n(1 − p) > 5` criteria, with larger expected counts preferred. Each continuity-correction prompt requires the correct half-unit boundary. A normal approximation is not asserted for arbitrarily small samples from an unknown population.
- Ordinary proportion intervals use the textbook’s more-than-five observed-success/failure rule; plus-four uses its stated confidence/sample-size recommendations. Proportion intervals estimate the SE from the sample; tests use the null model.
- Decisions follow the textbook’s strict `p-value < α` rule, using unrounded values. A failure to reject does not establish the null hypothesis.

## Page counts

| Chapter | Before | After | Change |
|---|---:|---:|---:|
| 1 | 106 | 145 | +39 |
| 2 | 128 | 160 | +32 |
| 3 | 92 | 101 | +9 |
| 4 | 114 | 131 | +17 |
| 5 | 57 | 66 | +9 |
| 6 | 42 | 48 | +6 |
| 7 | 65 | 86 | +21 |
| 8 | 77 | 86 | +9 |
| 9 | 20 | 31 | +11 |
| **Total** | **701** | **854** | **+153** |

## Section-by-section evidence

### 1.1 Definitions of Statistics, Probability, and Key Terms

16 → 24 pages. [Textbook 1.1](https://openstax.org/books/introductory-statistics-2e/pages/1-1-definitions-of-statistics-probability-and-key-terms)

| Textbook terminology | Revised PDF evidence |
|---|---|
| statistics | [§1.1 p. 1 — Statistics](../slides/section-1-1.pdf#page=1) |
| data; Data | [§1.1 p. 13 — Data](../slides/section-1-1.pdf#page=13) |
| descriptive statistics | [§1.1 p. 2 — Descriptive statistics](../slides/section-1-1.pdf#page=2) |
| inferential statistics | [§1.1 p. 3 — Inferential statistics](../slides/section-1-1.pdf#page=3) |
| Probability | [§1.1 p. 4 — Probability](../slides/section-1-1.pdf#page=4) |
| population | [§1.1 p. 6 — Population](../slides/section-1-1.pdf#page=6) |
| sample; sampling | [§1.1 p. 7 — Sample](../slides/section-1-1.pdf#page=7) |
| statistic | [§1.1 p. 15 — Statistic](../slides/section-1-1.pdf#page=15) |
| parameter | [§1.1 p. 14 — Parameter](../slides/section-1-1.pdf#page=14) |
| representative sample | [§1.1 p. 8 — Representative sample](../slides/section-1-1.pdf#page=8) |
| variable | [§1.1 p. 9 — Variable](../slides/section-1-1.pdf#page=9) |
| Numerical variables | [§1.1 p. 10 — Numerical variables](../slides/section-1-1.pdf#page=10) |
| Categorical variables | [§1.1 p. 11 — Categorical variables](../slides/section-1-1.pdf#page=11) |
| mean; average | [§1.1 p. 19 — Mean](../slides/section-1-1.pdf#page=19) |
| proportion | [§1.1 p. 20 — Proportion](../slides/section-1-1.pdf#page=20) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Classify variables and distinguish variables from observations | [§1.1 p. 10 — Numerical variables](../slides/section-1-1.pdf#page=10); [§1.1 p. 11 — Categorical variables](../slides/section-1-1.pdf#page=11); [§1.1 p. 12 — Classifying variables](../slides/section-1-1.pdf#page=12); [§1.1 p. 18 — Variable or value?](../slides/section-1-1.pdf#page=18) |
| Identify population, sample, parameter, statistic, variable and data in a study | [§1.1 p. 22 — The terms in a mean study](../slides/section-1-1.pdf#page=22); [§1.1 p. 23 — The terms in a proportion study](../slides/section-1-1.pdf#page=23) |
| Calculate and interpret averages and proportions | [§1.1 p. 19 — Mean](../slides/section-1-1.pdf#page=19); [§1.1 p. 20 — Proportion](../slides/section-1-1.pdf#page=20) |
| Interpret probability and represent numerical observations with dots | [§1.1 p. 5 — Long-run probability](../slides/section-1-1.pdf#page=5); [§1.1 p. 24 — Dot plots](../slides/section-1-1.pdf#page=24) |

### 1.2 Data, Sampling, and Variation in Data and Sampling

27 → 39 pages. [Textbook 1.2](https://openstax.org/books/introductory-statistics-2e/pages/1-2-data-sampling-and-variation-in-data-and-sampling)

| Textbook terminology | Revised PDF evidence |
|---|---|
| Qualitative data; categorical data | [§1.2 p. 1 — Qualitative data](../slides/section-1-2.pdf#page=1) |
| Quantitative data | [§1.2 p. 2 — Quantitative data](../slides/section-1-2.pdf#page=2) |
| discrete; quantitative discrete data | [§1.2 p. 3 — Discrete data](../slides/section-1-2.pdf#page=3) |
| continuous; quantitative continuous data | [§1.2 p. 4 — Continuous data](../slides/section-1-2.pdf#page=4) |
| pie chart | [§1.2 p. 12 — Pie charts](../slides/section-1-2.pdf#page=12) |
| bar graph | [§1.2 p. 11 — Bar graphs](../slides/section-1-2.pdf#page=11) |
| Pareto chart | [§1.2 p. 13 — Pareto charts](../slides/section-1-2.pdf#page=13) |
| random sampling | [§1.2 p. 17 — Simple random sampling](../slides/section-1-2.pdf#page=17) |
| stratified sample | [§1.2 p. 20 — Stratified sampling](../slides/section-1-2.pdf#page=20) |
| cluster sample | [§1.2 p. 21 — Cluster sampling](../slides/section-1-2.pdf#page=21) |
| systematic sample | [§1.2 p. 22 — Systematic sampling](../slides/section-1-2.pdf#page=22) |
| Convenience sampling | [§1.2 p. 23 — Convenience sampling](../slides/section-1-2.pdf#page=23) |
| Sampling with replacement | [§1.2 p. 26 — Sampling with replacement](../slides/section-1-2.pdf#page=26) |
| simple random sampling without replacement | [§1.2 p. 27 — Sampling without replacement](../slides/section-1-2.pdf#page=27) |
| sampling errors; nonsampling errors | [§1.2 p. 30 — Nonsampling error](../slides/section-1-2.pdf#page=30) |
| sampling bias | [§1.2 p. 33 — Sampling bias](../slides/section-1-2.pdf#page=33) |
| Variation | [§1.2 p. 28 — Sampling variation](../slides/section-1-2.pdf#page=28) |
| samples | [§1.2 p. 31 — Sample size and precision](../slides/section-1-2.pdf#page=31) |
| population | [§1.2 p. 18 — Random sampling](../slides/section-1-2.pdf#page=18) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Classify qualitative, quantitative, discrete and continuous data; recognize numerical labels | [§1.2 p. 6 — Classifying a variable](../slides/section-1-2.pdf#page=6); [§1.2 p. 7 — Classifying a count](../slides/section-1-2.pdf#page=7); [§1.2 p. 8 — Classifying a measurement](../slides/section-1-2.pdf#page=8); [§1.2 p. 9 — Numbers as labels](../slides/section-1-2.pdf#page=9); [§1.2 p. 10 — Numbers recoded as categories](../slides/section-1-2.pdf#page=10) |
| Read and critique categorical displays, denominators and omitted categories | [§1.2 p. 11 — Bar graphs](../slides/section-1-2.pdf#page=11); [§1.2 p. 12 — Pie charts](../slides/section-1-2.pdf#page=12); [§1.2 p. 13 — Pareto charts](../slides/section-1-2.pdf#page=13); [§1.2 p. 14 — Overlapping categories](../slides/section-1-2.pdf#page=14); [§1.2 p. 15 — Missing responses](../slides/section-1-2.pdf#page=15); [§1.2 p. 16 — Comparing different totals](../slides/section-1-2.pdf#page=16) |
| Select and carry out random, stratified, cluster, systematic and convenience sampling | [§1.2 p. 19 — Random number selection](../slides/section-1-2.pdf#page=19); [§1.2 p. 20 — Stratified sampling](../slides/section-1-2.pdf#page=20); [§1.2 p. 21 — Cluster sampling](../slides/section-1-2.pdf#page=21); [§1.2 p. 22 — Systematic sampling](../slides/section-1-2.pdf#page=22); [§1.2 p. 23 — Convenience sampling](../slides/section-1-2.pdf#page=23); [§1.2 p. 25 — Strata or clusters?](../slides/section-1-2.pdf#page=25) |
| Distinguish replacement rules and sources of variation | [§1.2 p. 26 — Sampling with replacement](../slides/section-1-2.pdf#page=26); [§1.2 p. 27 — Sampling without replacement](../slides/section-1-2.pdf#page=27); [§1.2 p. 29 — Sampling error](../slides/section-1-2.pdf#page=29); [§1.2 p. 30 — Nonsampling error](../slides/section-1-2.pdf#page=30); [§1.2 p. 31 — Sample size and precision](../slides/section-1-2.pdf#page=31) |
| Critique bias, nonresponse, influence, funding and causal claims | [§1.2 p. 33 — Sampling bias](../slides/section-1-2.pdf#page=33); [§1.2 p. 34 — Nonresponse](../slides/section-1-2.pdf#page=34); [§1.2 p. 35 — Question wording](../slides/section-1-2.pdf#page=35); [§1.2 p. 36 — Undue influence](../slides/section-1-2.pdf#page=36); [§1.2 p. 37 — Causality and confounding](../slides/section-1-2.pdf#page=37); [§1.2 p. 38 — Self-funded studies](../slides/section-1-2.pdf#page=38) |

### 1.3 Frequency, Frequency Tables, and Levels of Measurement

18 → 22 pages. [Textbook 1.3](https://openstax.org/books/introductory-statistics-2e/pages/1-3-frequency-frequency-tables-and-levels-of-measurement)

| Textbook terminology | Revised PDF evidence |
|---|---|
| level of measurement | [§1.3 p. 15 — Levels of measurement](../slides/section-1-3.pdf#page=15) |
| nominal scale | [§1.3 p. 16 — Nominal level](../slides/section-1-3.pdf#page=16) |
| ordinal scale | [§1.3 p. 17 — Ordinal level](../slides/section-1-3.pdf#page=17) |
| interval scale | [§1.3 p. 18 — Interval level](../slides/section-1-3.pdf#page=18) |
| ratio scale | [§1.3 p. 19 — Ratio level](../slides/section-1-3.pdf#page=19) |
| frequency | [§1.3 p. 1 — Frequency](../slides/section-1-3.pdf#page=1) |
| relative frequency | [§1.3 p. 3 — Relative frequency](../slides/section-1-3.pdf#page=3) |
| Cumulative relative frequency | [§1.3 p. 5 — Cumulative relative frequency](../slides/section-1-3.pdf#page=5) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Construct/check frequency, relative-frequency and cumulative tables | [§1.3 p. 2 — Frequency tables](../slides/section-1-3.pdf#page=2); [§1.3 p. 3 — Relative frequency](../slides/section-1-3.pdf#page=3); [§1.3 p. 5 — Cumulative relative frequency](../slides/section-1-3.pdf#page=5); [§1.3 p. 6 — Cumulative frequency](../slides/section-1-3.pdf#page=6); [§1.3 p. 9 — Checking a table](../slides/section-1-3.pdf#page=9) |
| Read strict/inclusive cutoffs and grouped intervals; recover interval frequency | [§1.3 p. 7 — At most or less than?](../slides/section-1-3.pdf#page=7); [§1.3 p. 8 — More than a cutoff](../slides/section-1-3.pdf#page=8); [§1.3 p. 11 — Reading a grouped frequency table](../slides/section-1-3.pdf#page=11); [§1.3 p. 12 — Recovering interval frequency](../slides/section-1-3.pdf#page=12) |
| Round summaries and interpret rounded totals | [§1.3 p. 13 — Rounding](../slides/section-1-3.pdf#page=13); [§1.3 p. 14 — Rounding totals](../slides/section-1-3.pdf#page=14) |
| Classify nominal, ordinal, interval and ratio scales and choose summaries | [§1.3 p. 15 — Levels of measurement](../slides/section-1-3.pdf#page=15); [§1.3 p. 16 — Nominal level](../slides/section-1-3.pdf#page=16); [§1.3 p. 17 — Ordinal level](../slides/section-1-3.pdf#page=17); [§1.3 p. 18 — Interval level](../slides/section-1-3.pdf#page=18); [§1.3 p. 19 — Ratio level](../slides/section-1-3.pdf#page=19); [§1.3 p. 22 — Choosing a summary](../slides/section-1-3.pdf#page=22) |

### 1.4 Experimental Design and Ethics

23 → 33 pages. [Textbook 1.4](https://openstax.org/books/introductory-statistics-2e/pages/1-4-experimental-design-and-ethics)

| Textbook terminology | Revised PDF evidence |
|---|---|
| explanatory variable | [§1.4 p. 4 — Explanatory variables](../slides/section-1-4.pdf#page=4) |
| response variable | [§1.4 p. 5 — Response variables](../slides/section-1-4.pdf#page=5) |
| treatments | [§1.4 p. 6 — Treatments](../slides/section-1-4.pdf#page=6) |
| experimental unit | [§1.4 p. 3 — Experimental units](../slides/section-1-4.pdf#page=3) |
| lurking variables | [§1.4 p. 7 — Lurking variables](../slides/section-1-4.pdf#page=7) |
| random assignment | [§1.4 p. 9 — Random assignment](../slides/section-1-4.pdf#page=9) |
| control group | [§1.4 p. 12 — Control groups](../slides/section-1-4.pdf#page=12) |
| placebo | [§1.4 p. 13 — Placebos](../slides/section-1-4.pdf#page=13) |
| Blinding | [§1.4 p. 15 — Blinding](../slides/section-1-4.pdf#page=15) |
| double-blind experiment | [§1.4 p. 16 — Double blinding](../slides/section-1-4.pdf#page=16) |
| Institutional Review Boards (IRB) | [§1.4 p. 25 — Institutional Review Board](../slides/section-1-4.pdf#page=25) |
| informed consent | [§1.4 p. 24 — Informed consent](../slides/section-1-4.pdf#page=24) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Identify experimental units, variables, treatments and study components | [§1.4 p. 3 — Experimental units](../slides/section-1-4.pdf#page=3); [§1.4 p. 4 — Explanatory variables](../slides/section-1-4.pdf#page=4); [§1.4 p. 5 — Response variables](../slides/section-1-4.pdf#page=5); [§1.4 p. 6 — Treatments](../slides/section-1-4.pdf#page=6); [§1.4 p. 22 — The parts of an experiment](../slides/section-1-4.pdf#page=22) |
| Distinguish observation from experimentation; reason about confounding and causality | [§1.4 p. 1 — Observational studies](../slides/section-1-4.pdf#page=1); [§1.4 p. 2 — Experiments](../slides/section-1-4.pdf#page=2); [§1.4 p. 7 — Lurking variables](../slides/section-1-4.pdf#page=7); [§1.4 p. 8 — Confounding](../slides/section-1-4.pdf#page=8); [§1.4 p. 18 — Causal conclusions](../slides/section-1-4.pdf#page=18); [§1.4 p. 20 — When assignment is impossible](../slides/section-1-4.pdf#page=20) |
| Design assignment, controls, masking, replication and treatment order | [§1.4 p. 11 — Random sampling or assignment?](../slides/section-1-4.pdf#page=11); [§1.4 p. 12 — Control groups](../slides/section-1-4.pdf#page=12); [§1.4 p. 13 — Placebos](../slides/section-1-4.pdf#page=13); [§1.4 p. 16 — Double blinding](../slides/section-1-4.pdf#page=16); [§1.4 p. 17 — Replication](../slides/section-1-4.pdf#page=17); [§1.4 p. 21 — Treatment order](../slides/section-1-4.pdf#page=21) |
| Evaluate consent, review, risk, privacy and reporting ethics | [§1.4 p. 24 — Informed consent](../slides/section-1-4.pdf#page=24); [§1.4 p. 25 — Institutional Review Board](../slides/section-1-4.pdf#page=25); [§1.4 p. 26 — Risk and benefit](../slides/section-1-4.pdf#page=26); [§1.4 p. 27 — Privacy](../slides/section-1-4.pdf#page=27); [§1.4 p. 30 — Fabrication and falsification](../slides/section-1-4.pdf#page=30); [§1.4 p. 31 — Stopping when results look favorable](../slides/section-1-4.pdf#page=31) |
| Critique misleading graphs and counts with unequal denominators | [§1.4 p. 32 — Graph scales and ethical reporting](../slides/section-1-4.pdf#page=32); [§1.4 p. 33 — Comparing complaint rates](../slides/section-1-4.pdf#page=33) |

### 1.5 Data Collection Experiment

12 → 15 pages. [Textbook 1.5](https://openstax.org/books/introductory-statistics-2e/pages/1-5-data-collection-experiment)

This lab introduces no separately marked vocabulary; sampling and table terminology is established in §§1.1–1.4 and applied below.

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Collect systematic sample data and compare starting points | [§1.5 p. 2 — Collecting observations](../slides/section-1-5.pdf#page=2); [§1.5 p. 3 — A systematic sample](../slides/section-1-5.pdf#page=3); [§1.5 p. 14 — A different starting point](../slides/section-1-5.pdf#page=14) |
| Construct exact-value, relative, cumulative and grouped frequency tables | [§1.5 p. 5 — An exact-value table](../slides/section-1-5.pdf#page=5); [§1.5 p. 6 — Relative frequencies](../slides/section-1-5.pdf#page=6); [§1.5 p. 7 — Cumulative frequencies](../slides/section-1-5.pdf#page=7); [§1.5 p. 8 — A grouped table](../slides/section-1-5.pdf#page=8) |
| Explain which cutoff questions grouping can answer | [§1.5 p. 9 — Information lost in grouping](../slides/section-1-5.pdf#page=9); [§1.5 p. 10 — Interpreting a cutoff](../slides/section-1-5.pdf#page=10); [§1.5 p. 11 — Above a cutoff](../slides/section-1-5.pdf#page=11); [§1.5 p. 12 — Above a class boundary](../slides/section-1-5.pdf#page=12); [§1.5 p. 13 — Choosing a grouping](../slides/section-1-5.pdf#page=13) |
| State the scope of a classroom sample | [§1.5 p. 15 — Scope of the evidence](../slides/section-1-5.pdf#page=15) |

### 1.6 Sampling Experiment

10 → 12 pages. [Textbook 1.6](https://openstax.org/books/introductory-statistics-2e/pages/1-6-sampling-experiment)

This lab introduces no separately marked vocabulary; sampling and table terminology is established in §§1.1–1.4 and applied below.

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Construct simple random, systematic, stratified and cluster samples | [§1.6 p. 2 — A simple random sample](../slides/section-1-6.pdf#page=2); [§1.6 p. 3 — A systematic sample](../slides/section-1-6.pdf#page=3); [§1.6 p. 4 — Stratifying by building](../slides/section-1-6.pdf#page=4); [§1.6 p. 5 — A cluster sample](../slides/section-1-6.pdf#page=5) |
| Contrast strata and clusters; change stratifying characteristic | [§1.6 p. 6 — Same groups, different method](../slides/section-1-6.pdf#page=6); [§1.6 p. 8 — Stratifying by another characteristic](../slides/section-1-6.pdf#page=8) |
| Compute proportional allocations and rounding effects | [§1.6 p. 7 — Unequal strata](../slides/section-1-6.pdf#page=7); [§1.6 p. 9 — Rounding allocations](../slides/section-1-6.pdf#page=9) |
| Assess ordering and explain a reproducible sampling procedure | [§1.6 p. 10 — Ordering matters](../slides/section-1-6.pdf#page=10); [§1.6 p. 11 — A reproducible procedure](../slides/section-1-6.pdf#page=11); [§1.6 p. 12 — Choosing a method](../slides/section-1-6.pdf#page=12) |

### 2.1 Stem-and-Leaf Graphs (Stemplots), Line Graphs, and Bar Graphs

16 → 20 pages. [Textbook 2.1](https://openstax.org/books/introductory-statistics-2e/pages/2-1-stem-and-leaf-graphs-stemplots-line-graphs-and-bar-graphs)

| Textbook terminology | Revised PDF evidence |
|---|---|
| outlier | [§2.1 p. 8 — A possible outlier](../slides/section-2-1.pdf#page=8) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Construct/read keyed stemplots with repetition, decimals and empty stems | [§2.1 p. 3 — Reading the key](../slides/section-2-1.pdf#page=3); [§2.1 p. 4 — Build a stemplot](../slides/section-2-1.pdf#page=4); [§2.1 p. 5 — Repeated values](../slides/section-2-1.pdf#page=5); [§2.1 p. 6 — Decimal leaves](../slides/section-2-1.pdf#page=6); [§2.1 p. 7 — An empty stem](../slides/section-2-1.pdf#page=7) |
| Identify possible outliers and compare back-to-back stemplots | [§2.1 p. 8 — A possible outlier](../slides/section-2-1.pdf#page=8); [§2.1 p. 10 — Keeping an unusual value](../slides/section-2-1.pdf#page=10); [§2.1 p. 11 — Comparing two groups](../slides/section-2-1.pdf#page=11) |
| Construct/read frequency line graphs | [§2.1 p. 13 — A line graph](../slides/section-2-1.pdf#page=13); [§2.1 p. 14 — Frequency from a graph](../slides/section-2-1.pdf#page=14); [§2.1 p. 15 — Build a frequency line graph](../slides/section-2-1.pdf#page=15) |
| Construct/read categorical bar graphs using counts or proportions | [§2.1 p. 16 — A bar graph](../slides/section-2-1.pdf#page=16); [§2.1 p. 17 — Counts or proportions?](../slides/section-2-1.pdf#page=17); [§2.1 p. 19 — Constructing a bar graph](../slides/section-2-1.pdf#page=19); [§2.1 p. 20 — Choose a display](../slides/section-2-1.pdf#page=20) |

### 2.2 Histograms, Frequency Polygons, and Time Series Graphs

20 → 29 pages. [Textbook 2.2](https://openstax.org/books/introductory-statistics-2e/pages/2-2-histograms-frequency-polygons-and-time-series-graphs)

| Textbook terminology | Revised PDF evidence |
|---|---|
| histogram | [§2.2 p. 1 — A histogram](../slides/section-2-2.pdf#page=1) |
| frequency | [§2.2 p. 9 — Frequency to percentage](../slides/section-2-2.pdf#page=9) |
| relative frequency | [§2.2 p. 15 — Relative-frequency histogram](../slides/section-2-2.pdf#page=15) |
| intervals | [§2.2 p. 2 — Define the intervals](../slides/section-2-2.pdf#page=2) |
| Frequency polygons | [§2.2 p. 19 — Comparing frequency polygons](../slides/section-2-2.pdf#page=19) |
| skewed | [§2.2 p. 13 — Describe the shape](../slides/section-2-2.pdf#page=13) |
| paired data set | [§2.2 p. 21 — Paired data sets](../slides/section-2-2.pdf#page=21) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Choose class boundaries/widths; construct frequency and relative-frequency histograms | [§2.2 p. 3 — Class width and boundaries](../slides/section-2-2.pdf#page=3); [§2.2 p. 4 — Precision and boundaries](../slides/section-2-2.pdf#page=4); [§2.2 p. 5 — Count the bins](../slides/section-2-2.pdf#page=5); [§2.2 p. 6 — Constructing a histogram](../slides/section-2-2.pdf#page=6); [§2.2 p. 15 — Relative-frequency histogram](../slides/section-2-2.pdf#page=15) |
| Read intervals/percentages and assess shape, gaps and grouping | [§2.2 p. 8 — Read an interval](../slides/section-2-2.pdf#page=8); [§2.2 p. 9 — Frequency to percentage](../slides/section-2-2.pdf#page=9); [§2.2 p. 10 — Information hidden by grouping](../slides/section-2-2.pdf#page=10); [§2.2 p. 11 — Bin width](../slides/section-2-2.pdf#page=11); [§2.2 p. 12 — A gap](../slides/section-2-2.pdf#page=12); [§2.2 p. 13 — Describe the shape](../slides/section-2-2.pdf#page=13) |
| Construct/read/overlay frequency polygons | [§2.2 p. 17 — Build a frequency polygon](../slides/section-2-2.pdf#page=17); [§2.2 p. 18 — Read a frequency polygon](../slides/section-2-2.pdf#page=18); [§2.2 p. 19 — Comparing frequency polygons](../slides/section-2-2.pdf#page=19) |
| Construct/read time series and preserve paired order | [§2.2 p. 21 — Paired data sets](../slides/section-2-2.pdf#page=21); [§2.2 p. 22 — Constructing a time series graph](../slides/section-2-2.pdf#page=22); [§2.2 p. 23 — Read a time series](../slides/section-2-2.pdf#page=23) |
| Critique unequal widths, misleading axes and pie-chart comparisons | [§2.2 p. 25 — Unequal widths](../slides/section-2-2.pdf#page=25); [§2.2 p. 27 — Misleading vertical scales](../slides/section-2-2.pdf#page=27); [§2.2 p. 28 — Misleading time scales](../slides/section-2-2.pdf#page=28); [§2.2 p. 29 — Comparing pie charts](../slides/section-2-2.pdf#page=29) |

### 2.3 Measures of the Location of the Data

18 → 23 pages. [Textbook 2.3](https://openstax.org/books/introductory-statistics-2e/pages/2-3-measures-of-the-location-of-the-data)

| Textbook terminology | Revised PDF evidence |
|---|---|
| quartiles; Quartiles | [§2.3 p. 6 — Quartiles](../slides/section-2-3.pdf#page=6) |
| percentiles | [§2.3 p. 22 — Ties in percentile statements](../slides/section-2-3.pdf#page=22) |
| median | [§2.3 p. 4 — The median](../slides/section-2-3.pdf#page=4) |
| first quartile | [§2.3 p. 7 — The lower quartile](../slides/section-2-3.pdf#page=7) |
| third quartile | [§2.3 p. 8 — The upper quartile](../slides/section-2-3.pdf#page=8) |
| interquartile range | [§2.3 p. 10 — Interquartile range](../slides/section-2-3.pdf#page=10) |
| outlier | [§2.3 p. 12 — An outlier rule](../slides/section-2-3.pdf#page=12) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Find medians, quartiles and IQR in even/odd data | [§2.3 p. 4 — The median](../slides/section-2-3.pdf#page=4); [§2.3 p. 5 — An even number of values](../slides/section-2-3.pdf#page=5); [§2.3 p. 7 — The lower quartile](../slides/section-2-3.pdf#page=7); [§2.3 p. 8 — The upper quartile](../slides/section-2-3.pdf#page=8); [§2.3 p. 9 — Quartiles with an odd sample size](../slides/section-2-3.pdf#page=9); [§2.3 p. 10 — Interquartile range](../slides/section-2-3.pdf#page=10) |
| Calculate percentile values with integer/noninteger positions and frequency tables | [§2.3 p. 16 — A percentile location](../slides/section-2-3.pdf#page=16); [§2.3 p. 17 — A percentile calculation](../slides/section-2-3.pdf#page=17); [§2.3 p. 18 — An integer percentile position](../slides/section-2-3.pdf#page=18); [§2.3 p. 19 — A percentile from a frequency table](../slides/section-2-3.pdf#page=19) |
| Calculate percentile ranks including ties and interpret context | [§2.3 p. 15 — Percentile from a rank](../slides/section-2-3.pdf#page=15); [§2.3 p. 20 — Percentile rank with ties](../slides/section-2-3.pdf#page=20); [§2.3 p. 21 — Interpreting a percentile in context](../slides/section-2-3.pdf#page=21); [§2.3 p. 22 — Ties in percentile statements](../slides/section-2-3.pdf#page=22) |
| Apply IQR outlier fences and interpret boundary cases | [§2.3 p. 12 — An outlier rule](../slides/section-2-3.pdf#page=12); [§2.3 p. 13 — Flag a value](../slides/section-2-3.pdf#page=13); [§2.3 p. 14 — At the fence](../slides/section-2-3.pdf#page=14) |

### 2.4 Box Plots

16 → 18 pages. [Textbook 2.4](https://openstax.org/books/introductory-statistics-2e/pages/2-4-box-plots)

| Textbook terminology | Revised PDF evidence |
|---|---|
| Box plots | [§2.4 p. 9 — Coinciding quartiles](../slides/section-2-4.pdf#page=9) |
| box-and-whisker plots; box-whisker plots | [§2.4 p. 2 — Box plot terminology](../slides/section-2-4.pdf#page=2) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Construct/read box plots from five-number summaries | [§2.4 p. 1 — Five-number summary](../slides/section-2-4.pdf#page=1); [§2.4 p. 3 — Build a box plot](../slides/section-2-4.pdf#page=3); [§2.4 p. 4 — Read the median](../slides/section-2-4.pdf#page=4); [§2.4 p. 5 — Read the box](../slides/section-2-4.pdf#page=5); [§2.4 p. 6 — Read the range](../slides/section-2-4.pdf#page=6); [§2.4 p. 7 — Read the IQR](../slides/section-2-4.pdf#page=7) |
| Interpret concentration and equal-count quarters, including coincidences | [§2.4 p. 8 — Length is not count](../slides/section-2-4.pdf#page=8); [§2.4 p. 9 — Coinciding quartiles](../slides/section-2-4.pdf#page=9); [§2.4 p. 10 — Within a quarter](../slides/section-2-4.pdf#page=10); [§2.4 p. 11 — Concentration](../slides/section-2-4.pdf#page=11) |
| Compare distributions and identify what box plots cannot show | [§2.4 p. 14 — Compare centers](../slides/section-2-4.pdf#page=14); [§2.4 p. 15 — Compare middle spreads](../slides/section-2-4.pdf#page=15); [§2.4 p. 16 — Same summary, different data](../slides/section-2-4.pdf#page=16) |
| Distinguish modified whiskers and investigate outliers | [§2.4 p. 12 — A modified box plot](../slides/section-2-4.pdf#page=12); [§2.4 p. 13 — The whisker endpoint](../slides/section-2-4.pdf#page=13); [§2.4 p. 18 — Investigate an outlier](../slides/section-2-4.pdf#page=18) |

### 2.5 Measures of the Center of the Data

20 → 24 pages. [Textbook 2.5](https://openstax.org/books/introductory-statistics-2e/pages/2-5-measures-of-the-center-of-the-data)

| Textbook terminology | Revised PDF evidence |
|---|---|
| mean | [§2.5 p. 1 — The mean](../slides/section-2-5.pdf#page=1) |
| median | [§2.5 p. 5 — The median](../slides/section-2-5.pdf#page=5) |
| mode | [§2.5 p. 8 — The mode](../slides/section-2-5.pdf#page=8) |
| sampling distribution | [§2.5 p. 23 — Sampling distribution](../slides/section-2-5.pdf#page=23) |
| frequency table; midpoint | [§2.5 p. 16 — A grouped estimate](../slides/section-2-5.pdf#page=16) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Calculate and interpret mean, median and mode, including bimodal/categorical data | [§2.5 p. 2 — A mean with units](../slides/section-2-5.pdf#page=2); [§2.5 p. 6 — An even-sized sample](../slides/section-2-5.pdf#page=6); [§2.5 p. 7 — Median position and value](../slides/section-2-5.pdf#page=7); [§2.5 p. 8 — The mode](../slides/section-2-5.pdf#page=8); [§2.5 p. 9 — Two modes](../slides/section-2-5.pdf#page=9); [§2.5 p. 10 — A categorical mode](../slides/section-2-5.pdf#page=10) |
| Choose a center and assess extreme observations | [§2.5 p. 11 — Compare mean and median](../slides/section-2-5.pdf#page=11); [§2.5 p. 12 — Sensitivity to one value](../slides/section-2-5.pdf#page=12); [§2.5 p. 13 — Choosing a typical value](../slides/section-2-5.pdf#page=13) |
| Calculate frequency-weighted and estimated grouped means | [§2.5 p. 14 — A mean from frequencies](../slides/section-2-5.pdf#page=14); [§2.5 p. 15 — Why weight the values?](../slides/section-2-5.pdf#page=15); [§2.5 p. 17 — Estimate a grouped mean](../slides/section-2-5.pdf#page=17); [§2.5 p. 18 — Exact or estimated?](../slides/section-2-5.pdf#page=18) |
| Connect sample statistics, population parameters and repeated-sample averages | [§2.5 p. 4 — Sample and population means](../slides/section-2-5.pdf#page=4); [§2.5 p. 22 — Law of Large Numbers](../slides/section-2-5.pdf#page=22); [§2.5 p. 23 — Sampling distribution](../slides/section-2-5.pdf#page=23); [§2.5 p. 24 — A statistic estimates a parameter](../slides/section-2-5.pdf#page=24) |

### 2.6 Skewness and the Mean, Median, and Mode

16 → 18 pages. [Textbook 2.6](https://openstax.org/books/introductory-statistics-2e/pages/2-6-skewness-and-the-mean-median-and-mode)

This lab introduces no separately marked vocabulary; sampling and table terminology is established in §§1.1–1.4 and applied below.

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Recognize symmetry, modality and the direction of skew | [§2.6 p. 1 — Symmetry](../slides/section-2-6.pdf#page=1); [§2.6 p. 2 — Unimodal and bimodal distributions](../slides/section-2-6.pdf#page=2); [§2.6 p. 5 — Read a right tail](../slides/section-2-6.pdf#page=5); [§2.6 p. 6 — Read a left tail](../slides/section-2-6.pdf#page=6); [§2.6 p. 11 — Skew names the tail](../slides/section-2-6.pdf#page=11) |
| Compare mean, median and mode using graphs/data | [§2.6 p. 7 — Mean and a right tail](../slides/section-2-6.pdf#page=7); [§2.6 p. 8 — Mean and a left tail](../slides/section-2-6.pdf#page=8); [§2.6 p. 12 — The mode and shape](../slides/section-2-6.pdf#page=12); [§2.6 p. 13 — Comparing dot plots and centers](../slides/section-2-6.pdf#page=13) |
| Distinguish common orderings from universal rules; choose a center | [§2.6 p. 14 — A common pattern](../slides/section-2-6.pdf#page=14); [§2.6 p. 15 — Symmetry without one peak](../slides/section-2-6.pdf#page=15); [§2.6 p. 16 — Choosing the center](../slides/section-2-6.pdf#page=16) |

### 2.7 Measures of the Spread of the Data

22 → 28 pages. [Textbook 2.7](https://openstax.org/books/introductory-statistics-2e/pages/2-7-measures-of-the-spread-of-the-data)

| Textbook terminology | Revised PDF evidence |
|---|---|
| standard deviation | [§2.7 p. 8 — Sample standard deviation](../slides/section-2-7.pdf#page=8) |
| variance | [§2.7 p. 7 — Sample variance](../slides/section-2-7.pdf#page=7) |
| sampling variability of a statistic | [§2.7 p. 25 — Sampling variability of a statistic](../slides/section-2-7.pdf#page=25) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Calculate deviations, variance, range and sample/population SD | [§2.7 p. 2 — The range](../slides/section-2-7.pdf#page=2); [§2.7 p. 3 — A deviation](../slides/section-2-7.pdf#page=3); [§2.7 p. 5 — Sum of deviations](../slides/section-2-7.pdf#page=5); [§2.7 p. 7 — Sample variance](../slides/section-2-7.pdf#page=7); [§2.7 p. 8 — Sample standard deviation](../slides/section-2-7.pdf#page=8); [§2.7 p. 9 — Population variance](../slides/section-2-7.pdf#page=9); [§2.7 p. 10 — Choose the denominator](../slides/section-2-7.pdf#page=10) |
| Calculate SD from exact frequencies or grouped midpoints and read technology output | [§2.7 p. 11 — Standard deviation from frequencies](../slides/section-2-7.pdf#page=11); [§2.7 p. 12 — Grouped standard deviation](../slides/section-2-7.pdf#page=12); [§2.7 p. 13 — Technology and notation](../slides/section-2-7.pdf#page=13) |
| Interpret units, compare spread and assess transformations | [§2.7 p. 14 — Units of spread](../slides/section-2-7.pdf#page=14); [§2.7 p. 16 — Compare variability](../slides/section-2-7.pdf#page=16); [§2.7 p. 18 — One value changes](../slides/section-2-7.pdf#page=18); [§2.7 p. 19 — Adding a constant](../slides/section-2-7.pdf#page=19); [§2.7 p. 20 — Scaling every value](../slides/section-2-7.pdf#page=20) |
| Find standardized distances, recover values and compare relative standing | [§2.7 p. 21 — Distance in standard deviations](../slides/section-2-7.pdf#page=21); [§2.7 p. 22 — Below the mean](../slides/section-2-7.pdf#page=22); [§2.7 p. 23 — Recovering a data value](../slides/section-2-7.pdf#page=23); [§2.7 p. 24 — Compare relative positions](../slides/section-2-7.pdf#page=24) |
| Distinguish sampling variability/SE and distribution bounds | [§2.7 p. 25 — Sampling variability of a statistic](../slides/section-2-7.pdf#page=25); [§2.7 p. 26 — Standard error of the mean](../slides/section-2-7.pdf#page=26); [§2.7 p. 27 — Chebyshev’s bound](../slides/section-2-7.pdf#page=27); [§2.7 p. 28 — Empirical rule](../slides/section-2-7.pdf#page=28) |

### 3.1 Terminology

18 → 19 pages. [Textbook 3.1](https://openstax.org/books/introductory-statistics-2e/pages/3-1-terminology)

| Textbook terminology | Revised PDF evidence |
|---|---|
| experiment; probability | [§3.1 p. 1 — A probability experiment](../slides/section-3-1.pdf#page=1) |
| outcome; Equally likely; fair | [§3.1 p. 4 — Equally likely outcomes](../slides/section-3-1.pdf#page=4) |
| sample space | [§3.1 p. 2 — Sample space](../slides/section-3-1.pdf#page=2) |
| event | [§3.1 p. 3 — An event](../slides/section-3-1.pdf#page=3) |
| long-term relative frequency; law of large numbers | [§3.1 p. 8 — Law of large numbers](../slides/section-3-1.pdf#page=8) |
| unfair | [§3.1 p. 5 — Unequal probabilities](../slides/section-3-1.pdf#page=5) |
| "OR" Event | [§3.1 p. 12 — The union](../slides/section-3-1.pdf#page=12) |
| "AND" Event | [§3.1 p. 11 — The intersection](../slides/section-3-1.pdf#page=11) |
| complement of event A | [§3.1 p. 9 — A complement](../slides/section-3-1.pdf#page=9) |
| conditional probability | [§3.1 p. 14 — Conditional probability](../slides/section-3-1.pdf#page=14) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Describe sample spaces/events; compute equally likely and empirical probabilities | [§3.1 p. 1 — A probability experiment](../slides/section-3-1.pdf#page=1); [§3.1 p. 2 — Sample space](../slides/section-3-1.pdf#page=2); [§3.1 p. 3 — An event](../slides/section-3-1.pdf#page=3); [§3.1 p. 4 — Equally likely outcomes](../slides/section-3-1.pdf#page=4); [§3.1 p. 5 — Unequal probabilities](../slides/section-3-1.pdf#page=5); [§3.1 p. 7 — Relative frequency](../slides/section-3-1.pdf#page=7) |
| Translate complements, intersections, inclusive unions and inequalities | [§3.1 p. 10 — Translate “not”](../slides/section-3-1.pdf#page=10); [§3.1 p. 11 — The intersection](../slides/section-3-1.pdf#page=11); [§3.1 p. 12 — The union](../slides/section-3-1.pdf#page=12); [§3.1 p. 13 — Inclusive “or”](../slides/section-3-1.pdf#page=13); [§3.1 p. 19 — Write a probability event](../slides/section-3-1.pdf#page=19) |
| Interpret conditioning and distinguish reversed conditions | [§3.1 p. 14 — Conditional probability](../slides/section-3-1.pdf#page=14); [§3.1 p. 15 — The conditional-probability formula](../slides/section-3-1.pdf#page=15); [§3.1 p. 16 — The conditioned group](../slides/section-3-1.pdf#page=16); [§3.1 p. 17 — Reverse the condition](../slides/section-3-1.pdf#page=17) |
| Check bounds and long-run interpretations | [§3.1 p. 6 — Probability bounds](../slides/section-3-1.pdf#page=6); [§3.1 p. 8 — Law of large numbers](../slides/section-3-1.pdf#page=8) |

### 3.2 Independent and Mutually Exclusive Events

20 → 21 pages. [Textbook 3.2](https://openstax.org/books/introductory-statistics-2e/pages/3-2-independent-and-mutually-exclusive-events)

| Textbook terminology | Revised PDF evidence |
|---|---|
| independent events; dependent events | [§3.2 p. 1 — Independent events](../slides/section-3-2.pdf#page=1) |
| replacement | [§3.2 p. 12 — With replacement](../slides/section-3-2.pdf#page=12) |
| mutually exclusive | [§3.2 p. 8 — Mutually exclusive events](../slides/section-3-2.pdf#page=8) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Test independence and dependence using conditional probabilities/products | [§3.2 p. 2 — Test independence](../slides/section-3-2.pdf#page=2); [§3.2 p. 3 — Dependence](../slides/section-3-2.pdf#page=3); [§3.2 p. 4 — Independent product](../slides/section-3-2.pdf#page=4); [§3.2 p. 15 — A conditional check](../slides/section-3-2.pdf#page=15) |
| Distinguish mutually exclusive from independent events | [§3.2 p. 8 — Mutually exclusive events](../slides/section-3-2.pdf#page=8); [§3.2 p. 10 — Positive-probability disjoint events](../slides/section-3-2.pdf#page=10); [§3.2 p. 11 — Disjoint or independent?](../slides/section-3-2.pdf#page=11) |
| Enumerate combined sample spaces and model replacement | [§3.2 p. 7 — Counting a combined sample space](../slides/section-3-2.pdf#page=7); [§3.2 p. 12 — With replacement](../slides/section-3-2.pdf#page=12); [§3.2 p. 13 — Without replacement](../slides/section-3-2.pdf#page=13) |
| Evaluate model assumptions and the mistaken idea that outcomes are due | [§3.2 p. 14 — Which assumption fails?](../slides/section-3-2.pdf#page=14); [§3.2 p. 18 — Empirical association](../slides/section-3-2.pdf#page=18); [§3.2 p. 19 — Coin tosses and “due” outcomes](../slides/section-3-2.pdf#page=19) |

### 3.3 Two Basic Rules of Probability

20 → 23 pages. [Textbook 3.3](https://openstax.org/books/introductory-statistics-2e/pages/3-3-two-basic-rules-of-probability)

| Textbook terminology | Revised PDF evidence |
|---|---|
| sample space | [§3.3 p. 4 — A disjoint union](../slides/section-3-3.pdf#page=4) |
| independent | [§3.3 p. 12 — An independent product](../slides/section-3-3.pdf#page=12) |
| mutually exclusive | [§3.3 p. 5 — Addition for disjoint events](../slides/section-3-3.pdf#page=5) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Calculate unions, intersections and complements from counts/probabilities | [§3.3 p. 3 — A union from counts](../slides/section-3-3.pdf#page=3); [§3.3 p. 4 — A disjoint union](../slides/section-3-3.pdf#page=4); [§3.3 p. 6 — Complement of a union](../slides/section-3-3.pdf#page=6); [§3.3 p. 7 — An intersection from a union](../slides/section-3-3.pdf#page=7) |
| Apply dependent/independent multiplication and reverse conditioning | [§3.3 p. 9 — A dependent product](../slides/section-3-3.pdf#page=9); [§3.3 p. 10 — A different order](../slides/section-3-3.pdf#page=10); [§3.3 p. 11 — Either order](../slides/section-3-3.pdf#page=11); [§3.3 p. 12 — An independent product](../slides/section-3-3.pdf#page=12); [§3.3 p. 15 — A conditional ratio](../slides/section-3-3.pdf#page=15) |
| Calculate exactly/at least one and conditional complements | [§3.3 p. 13 — At least one](../slides/section-3-3.pdf#page=13); [§3.3 p. 14 — Exactly one](../slides/section-3-3.pdf#page=14); [§3.3 p. 16 — A conditional complement](../slides/section-3-3.pdf#page=16); [§3.3 p. 22 — A complement shortcut](../slides/section-3-3.pdf#page=22) |
| Recover an unknown probability and check coherent assumptions | [§3.3 p. 23 — Recovering a missing probability](../slides/section-3-3.pdf#page=23); [§3.3 p. 17 — A zero denominator](../slides/section-3-3.pdf#page=17); [§3.3 p. 20 — Check coherence](../slides/section-3-3.pdf#page=20) |

### 3.4 Contingency Tables

16 → 18 pages. [Textbook 3.4](https://openstax.org/books/introductory-statistics-2e/pages/3-4-contingency-tables)

| Textbook terminology | Revised PDF evidence |
|---|---|
| contingency table | [§3.4 p. 1 — A contingency table](../slides/section-3-4.pdf#page=1) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Read joint/marginal probabilities and unions from counts | [§3.4 p. 2 — A joint count](../slides/section-3-4.pdf#page=2); [§3.4 p. 4 — A marginal probability](../slides/section-3-4.pdf#page=4); [§3.4 p. 5 — A joint probability](../slides/section-3-4.pdf#page=5); [§3.4 p. 6 — A union probability](../slides/section-3-4.pdf#page=6); [§3.4 p. 7 — Neither category](../slides/section-3-4.pdf#page=7) |
| Compute conditional probabilities using the correct row/column or combined group | [§3.4 p. 8 — Condition on a row](../slides/section-3-4.pdf#page=8); [§3.4 p. 9 — Condition on a column](../slides/section-3-4.pdf#page=9); [§3.4 p. 10 — Different denominators](../slides/section-3-4.pdf#page=10); [§3.4 p. 15 — Conditioning on a combined category](../slides/section-3-4.pdf#page=15) |
| Complete missing counts and construct a probability table | [§3.4 p. 13 — Complete the counts](../slides/section-3-4.pdf#page=13); [§3.4 p. 14 — A probability contingency table](../slides/section-3-4.pdf#page=14) |
| Test independence and mutual exclusivity and state scope | [§3.4 p. 11 — An independence check](../slides/section-3-4.pdf#page=11); [§3.4 p. 12 — Mutual exclusivity check](../slides/section-3-4.pdf#page=12); [§3.4 p. 17 — A dependent table](../slides/section-3-4.pdf#page=17); [§3.4 p. 18 — Scope of the table](../slides/section-3-4.pdf#page=18) |

### 3.5 Tree and Venn Diagrams

18 → 20 pages. [Textbook 3.5](https://openstax.org/books/introductory-statistics-2e/pages/3-5-tree-and-venn-diagrams)

| Textbook terminology | Revised PDF evidence |
|---|---|
| tree diagram | [§3.5 p. 1 — A tree diagram](../slides/section-3-5.pdf#page=1) |
| sample space; Venn diagram | [§3.5 p. 13 — A Venn diagram](../slides/section-3-5.pdf#page=13) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Construct trees, label probabilities, multiply paths and add outcomes | [§3.5 p. 2 — Build a two-stage tree](../slides/section-3-5.pdf#page=2); [§3.5 p. 3 — Multiply along a path](../slides/section-3-5.pdf#page=3); [§3.5 p. 4 — Add terminal paths](../slides/section-3-5.pdf#page=4); [§3.5 p. 7 — Branch totals](../slides/section-3-5.pdf#page=7) |
| Use trees with/without replacement, frequencies and unequal branch weights | [§3.5 p. 5 — Tree without replacement](../slides/section-3-5.pdf#page=5); [§3.5 p. 8 — A tree with replacement](../slides/section-3-5.pdf#page=8); [§3.5 p. 9 — Frequency-labeled trees](../slides/section-3-5.pdf#page=9); [§3.5 p. 10 — A weighted path](../slides/section-3-5.pdf#page=10); [§3.5 p. 11 — Sum successful paths](../slides/section-3-5.pdf#page=11) |
| Recover reverse conditional probabilities | [§3.5 p. 12 — Reverse the conditioning](../slides/section-3-5.pdf#page=12) |
| Fill/read/shade Venn regions and compute conditional probabilities | [§3.5 p. 14 — Fill the regions](../slides/section-3-5.pdf#page=14); [§3.5 p. 15 — Only one category](../slides/section-3-5.pdf#page=15); [§3.5 p. 16 — Outside both circles](../slides/section-3-5.pdf#page=16); [§3.5 p. 17 — Shade a union](../slides/section-3-5.pdf#page=17); [§3.5 p. 18 — Shade a complement](../slides/section-3-5.pdf#page=18); [§3.5 p. 19 — Conditional probability in a Venn diagram](../slides/section-3-5.pdf#page=19); [§3.5 p. 20 — Disjoint circles](../slides/section-3-5.pdf#page=20) |

### 4.1 Probability Distribution Function (PDF) for a Discrete Random Variable

18 → 19 pages. [Textbook 4.1](https://openstax.org/books/introductory-statistics-2e/pages/4-1-probability-distribution-function-pdf-for-a-discrete-random-variable)

| Textbook terminology | Revised PDF evidence |
|---|---|
| probability distribution function | [§4.1 p. 9 — A discrete probability distribution](../slides/section-4-1.pdf#page=9) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Define a discrete random variable and map outcomes to possible values | [§4.1 p. 2 — Variable or realization?](../slides/section-4-1.pdf#page=2); [§4.1 p. 3 — The possible values](../slides/section-4-1.pdf#page=3); [§4.1 p. 4 — Discrete versus continuous](../slides/section-4-1.pdf#page=4); [§4.1 p. 6 — Outcomes versus values](../slides/section-4-1.pdf#page=6) |
| Construct and validate a discrete PDF, including missing probabilities | [§4.1 p. 7 — Build a distribution](../slides/section-4-1.pdf#page=7); [§4.1 p. 8 — Equal values, unequal chances](../slides/section-4-1.pdf#page=8); [§4.1 p. 10 — Probability requirements](../slides/section-4-1.pdf#page=10); [§4.1 p. 11 — A missing probability](../slides/section-4-1.pdf#page=11); [§4.1 p. 12 — An invalid distribution](../slides/section-4-1.pdf#page=12) |
| Calculate exact, cumulative, complementary and interval probabilities | [§4.1 p. 13 — At most two](../slides/section-4-1.pdf#page=13); [§4.1 p. 14 — Fewer than two](../slides/section-4-1.pdf#page=14); [§4.1 p. 15 — At least one](../slides/section-4-1.pdf#page=15); [§4.1 p. 16 — A complement](../slides/section-4-1.pdf#page=16); [§4.1 p. 17 — A probability interval](../slides/section-4-1.pdf#page=17) |
| Convert observed frequencies to a model and interpret its scope | [§4.1 p. 18 — From data to a model](../slides/section-4-1.pdf#page=18); [§4.1 p. 19 — Distribution versus one observation](../slides/section-4-1.pdf#page=19) |

### 4.2 Mean or Expected Value and Standard Deviation

20 → 22 pages. [Textbook 4.2](https://openstax.org/books/introductory-statistics-2e/pages/4-2-mean-or-expected-value-and-standard-deviation)

| Textbook terminology | Revised PDF evidence |
|---|---|
| expected value | [§4.2 p. 1 — Expected value](../slides/section-4-2.pdf#page=1) |
| mean | [§4.2 p. 2 — The weighted mean formula](../slides/section-4-2.pdf#page=2) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Calculate/interpret expected value as a weighted long-run mean | [§4.2 p. 2 — The weighted mean formula](../slides/section-4-2.pdf#page=2); [§4.2 p. 3 — Not an unweighted average](../slides/section-4-2.pdf#page=3); [§4.2 p. 4 — A mean between integers](../slides/section-4-2.pdf#page=4); [§4.2 p. 7 — Law of large numbers for averages](../slides/section-4-2.pdf#page=7); [§4.2 p. 8 — Expected total](../slides/section-4-2.pdf#page=8) |
| Calculate probability-weighted variance and SD | [§4.2 p. 11 — Calculate a model variance](../slides/section-4-2.pdf#page=11); [§4.2 p. 12 — Calculate model standard deviation](../slides/section-4-2.pdf#page=12); [§4.2 p. 13 — Unequal probability weights](../slides/section-4-2.pdf#page=13); [§4.2 p. 14 — Same mean, different spread](../slides/section-4-2.pdf#page=14) |
| Construct net-gain variables, expected payoff and fair fees | [§4.2 p. 16 — Net gain](../slides/section-4-2.pdf#page=16); [§4.2 p. 17 — Expected net gain](../slides/section-4-2.pdf#page=17); [§4.2 p. 18 — Fair entry fee](../slides/section-4-2.pdf#page=18); [§4.2 p. 19 — A negative expected gain](../slides/section-4-2.pdf#page=19) |
| Compare model and sample summaries and transformed values | [§4.2 p. 15 — Model versus sample](../slides/section-4-2.pdf#page=15); [§4.2 p. 20 — Changing the variable](../slides/section-4-2.pdf#page=20); [§4.2 p. 21 — Shift and spread](../slides/section-4-2.pdf#page=21); [§4.2 p. 22 — A weighted average beyond games](../slides/section-4-2.pdf#page=22) |

### 4.3 Binomial Distribution

22 → 27 pages. [Textbook 4.3](https://openstax.org/books/introductory-statistics-2e/pages/4-3-binomial-distribution)

| Textbook terminology | Revised PDF evidence |
|---|---|
| binomial probability distribution | [§4.3 p. 8 — Binomial notation](../slides/section-4-3.pdf#page=8) |
| Bernoulli Trial | [§4.3 p. 2 — Bernoulli trials](../slides/section-4-3.pdf#page=2) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Check binomial conditions, define success, parameters and possible values | [§4.3 p. 1 — A binomial experiment](../slides/section-4-3.pdf#page=1); [§4.3 p. 2 — Bernoulli trials](../slides/section-4-3.pdf#page=2); [§4.3 p. 3 — Define success](../slides/section-4-3.pdf#page=3); [§4.3 p. 5 — Identify n and p](../slides/section-4-3.pdf#page=5); [§4.3 p. 7 — Possible values](../slides/section-4-3.pdf#page=7) |
| Calculate exact, cumulative and complement probabilities | [§4.3 p. 14 — The binomial probability](../slides/section-4-3.pdf#page=14); [§4.3 p. 16 — No successes](../slides/section-4-3.pdf#page=16); [§4.3 p. 17 — At least one success](../slides/section-4-3.pdf#page=17); [§4.3 p. 18 — A cumulative probability](../slides/section-4-3.pdf#page=18); [§4.3 p. 20 — PDF and CDF commands](../slides/section-4-3.pdf#page=20) |
| Construct and graph the complete probability distribution | [§4.3 p. 15 — A full binomial distribution](../slides/section-4-3.pdf#page=15) |
| Calculate mean, variance and SD and assess suitability | [§4.3 p. 21 — Expected successes](../slides/section-4-3.pdf#page=21); [§4.3 p. 22 — Standard deviation](../slides/section-4-3.pdf#page=22); [§4.3 p. 23 — Binomial variance](../slides/section-4-3.pdf#page=23); [§4.3 p. 24 — A fixed count?](../slides/section-4-3.pdf#page=24); [§4.3 p. 25 — Sampling without replacement](../slides/section-4-3.pdf#page=25); [§4.3 p. 26 — Changing probabilities](../slides/section-4-3.pdf#page=26) |

### 4.4 Geometric Distribution

20 → 25 pages. [Textbook 4.4](https://openstax.org/books/introductory-statistics-2e/pages/4-4-geometric-distribution)

| Textbook terminology | Revised PDF evidence |
|---|---|
| geometric distribution | [§4.4 p. 5 — Geometric notation](../slides/section-4-4.pdf#page=5) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Define the stopping rule, support and success probability | [§4.4 p. 1 — A geometric experiment](../slides/section-4-4.pdf#page=1); [§4.4 p. 2 — Our counting convention](../slides/section-4-4.pdf#page=2); [§4.4 p. 3 — Possible values](../slides/section-4-4.pdf#page=3); [§4.4 p. 4 — Identify p](../slides/section-4-4.pdf#page=4) |
| Calculate first-success, upper-tail and cumulative probabilities | [§4.4 p. 6 — First success on trial four](../slides/section-4-4.pdf#page=6); [§4.4 p. 10 — A tail probability](../slides/section-4-4.pdf#page=10); [§4.4 p. 11 — Success by trial three](../slides/section-4-4.pdf#page=11); [§4.4 p. 12 — At least three trials](../slides/section-4-4.pdf#page=12) |
| Calculate expected trials/SD and interpret memorylessness | [§4.4 p. 13 — Expected trials](../slides/section-4-4.pdf#page=13); [§4.4 p. 14 — Standard deviation](../slides/section-4-4.pdf#page=14); [§4.4 p. 15 — Expectation is not a deadline](../slides/section-4-4.pdf#page=15); [§4.4 p. 16 — Memoryless waiting](../slides/section-4-4.pdf#page=16); [§4.4 p. 17 — Additional waiting](../slides/section-4-4.pdf#page=17) |
| Translate to failures-before-success and compare mean/spread | [§4.4 p. 19 — Count failures instead](../slides/section-4-4.pdf#page=19); [§4.4 p. 20 — Failures-before-success probabilities](../slides/section-4-4.pdf#page=20); [§4.4 p. 21 — Expected failures](../slides/section-4-4.pdf#page=21); [§4.4 p. 22 — Spread under a change of convention](../slides/section-4-4.pdf#page=22) |
| Recognize the common ratio and graph geometric probabilities | [§4.4 p. 23 — The common ratio](../slides/section-4-4.pdf#page=23); [§4.4 p. 24 — Graphing geometric probabilities](../slides/section-4-4.pdf#page=24) |

### 4.5 Hypergeometric Distribution

16 → 18 pages. [Textbook 4.5](https://openstax.org/books/introductory-statistics-2e/pages/4-5-hypergeometric-distribution)

| Textbook terminology | Revised PDF evidence |
|---|---|
| hypergeometric probability | [§4.5 p. 11 — An exact probability](../slides/section-4-5.pdf#page=11) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Identify sampling without replacement, parameters and support bounds | [§4.5 p. 1 — A hypergeometric experiment](../slides/section-4-5.pdf#page=1); [§4.5 p. 3 — The parameters](../slides/section-4-5.pdf#page=3); [§4.5 p. 5 — A maximum count](../slides/section-4-5.pdf#page=5); [§4.5 p. 6 — A minimum count](../slides/section-4-5.pdf#page=6); [§4.5 p. 7 — The support](../slides/section-4-5.pdf#page=7) |
| Count samples and compute exact/cumulative/tail probabilities | [§4.5 p. 9 — Count possible samples](../slides/section-4-5.pdf#page=9); [§4.5 p. 10 — Count favorable samples](../slides/section-4-5.pdf#page=10); [§4.5 p. 11 — An exact probability](../slides/section-4-5.pdf#page=11); [§4.5 p. 12 — At most one](../slides/section-4-5.pdf#page=12); [§4.5 p. 13 — A hypergeometric upper tail](../slides/section-4-5.pdf#page=13) |
| Calculate expected count and standard deviation | [§4.5 p. 14 — An expected count](../slides/section-4-5.pdf#page=14); [§4.5 p. 15 — Hypergeometric standard deviation](../slides/section-4-5.pdf#page=15) |
| Choose between hypergeometric/binomial designs | [§4.5 p. 16 — Compare sampling designs](../slides/section-4-5.pdf#page=16); [§4.5 p. 17 — A small sampling fraction](../slides/section-4-5.pdf#page=17); [§4.5 p. 18 — Select the distribution](../slides/section-4-5.pdf#page=18) |

### 4.6 Poisson Distribution

18 → 20 pages. [Textbook 4.6](https://openstax.org/books/introductory-statistics-2e/pages/4-6-poisson-distribution)

| Textbook terminology | Revised PDF evidence |
|---|---|
| Poisson probability distribution | [§4.6 p. 5 — Poisson notation](../slides/section-4-6.pdf#page=5) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Define a Poisson count and scale rates to time or spatial intervals | [§4.6 p. 2 — Define the interval](../slides/section-4-6.pdf#page=2); [§4.6 p. 3 — Scale the mean](../slides/section-4-6.pdf#page=3); [§4.6 p. 4 — Time units matter](../slides/section-4-6.pdf#page=4); [§4.6 p. 13 — A spatial interval](../slides/section-4-6.pdf#page=13) |
| Calculate exact, zero, cumulative and tail probabilities | [§4.6 p. 7 — Exact count probability](../slides/section-4-6.pdf#page=7); [§4.6 p. 8 — No events](../slides/section-4-6.pdf#page=8); [§4.6 p. 9 — At least one event](../slides/section-4-6.pdf#page=9); [§4.6 p. 10 — Fewer than three](../slides/section-4-6.pdf#page=10); [§4.6 p. 11 — More than two](../slides/section-4-6.pdf#page=11) |
| Calculate mean/SD and graph the distribution | [§4.6 p. 12 — Mean and standard deviation](../slides/section-4-6.pdf#page=12); [§4.6 p. 20 — Graphing a Poisson distribution](../slides/section-4-6.pdf#page=20) |
| Evaluate assumptions and compare exact binomial with Poisson approximation | [§4.6 p. 14 — A variable rate](../slides/section-4-6.pdf#page=14); [§4.6 p. 15 — Clustering](../slides/section-4-6.pdf#page=15); [§4.6 p. 16 — Binomial or Poisson?](../slides/section-4-6.pdf#page=16); [§4.6 p. 17 — A rare-event approximation](../slides/section-4-6.pdf#page=17); [§4.6 p. 18 — Checking a Poisson approximation](../slides/section-4-6.pdf#page=18); [§4.6 p. 19 — Count versus waiting time](../slides/section-4-6.pdf#page=19) |

### 5.1 Continuous Probability Functions

17 → 18 pages. [Textbook 5.1](https://openstax.org/books/introductory-statistics-2e/pages/5-1-continuous-probability-functions)

This lab introduces no separately marked vocabulary; sampling and table terminology is established in §§1.1–1.4 and applied below.

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Interpret density/area, valid distributions and probability statements | [§5.1 p. 2 — A probability density](../slides/section-5-1.pdf#page=2); [§5.1 p. 3 — The entire distribution](../slides/section-5-1.pdf#page=3); [§5.1 p. 4 — Probability as area](../slides/section-5-1.pdf#page=4); [§5.1 p. 5 — An interval probability](../slides/section-5-1.pdf#page=5); [§5.1 p. 6 — Graphing a continuous density](../slides/section-5-1.pdf#page=6) |
| Distinguish point probabilities, rounded observations and endpoints | [§5.1 p. 7 — Height is not probability](../slides/section-5-1.pdf#page=7); [§5.1 p. 8 — One exact value](../slides/section-5-1.pdf#page=8); [§5.1 p. 9 — Rounded measurements](../slides/section-5-1.pdf#page=9); [§5.1 p. 10 — Endpoints](../slides/section-5-1.pdf#page=10) |
| Use a CDF for cumulative, tail and interval probabilities | [§5.1 p. 12 — A cumulative probability](../slides/section-5-1.pdf#page=12); [§5.1 p. 13 — Beyond a cutoff](../slides/section-5-1.pdf#page=13); [§5.1 p. 14 — Between two cutoffs](../slides/section-5-1.pdf#page=14); [§5.1 p. 15 — Outside an interval](../slides/section-5-1.pdf#page=15); [§5.1 p. 16 — A possible cumulative function](../slides/section-5-1.pdf#page=16) |
| Interpret a percentile cutoff | [§5.1 p. 17 — A percentile](../slides/section-5-1.pdf#page=17) |

### 5.2 The Uniform Distribution

18 → 20 pages. [Textbook 5.2](https://openstax.org/books/introductory-statistics-2e/pages/5-2-the-uniform-distribution)

| Textbook terminology | Revised PDF evidence |
|---|---|
| equally likely | [§5.2 p. 1 — The uniform distribution](../slides/section-5-2.pdf#page=1) |
| conditional probability | [§5.2 p. 15 — A conditional interval](../slides/section-5-2.pdf#page=15) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Specify and graph a uniform density and its support | [§5.2 p. 1 — The uniform distribution](../slides/section-5-2.pdf#page=1); [§5.2 p. 2 — The range](../slides/section-5-2.pdf#page=2); [§5.2 p. 3 — Uniform density](../slides/section-5-2.pdf#page=3); [§5.2 p. 4 — A waiting interval](../slides/section-5-2.pdf#page=4) |
| Calculate interval, tail and partially out-of-support probabilities | [§5.2 p. 5 — A short wait](../slides/section-5-2.pdf#page=5); [§5.2 p. 6 — A long wait](../slides/section-5-2.pdf#page=6); [§5.2 p. 7 — A partially overlapping interval](../slides/section-5-2.pdf#page=7); [§5.2 p. 8 — Outside the support](../slides/section-5-2.pdf#page=8) |
| Calculate theoretical mean/SD and compare empirical summaries | [§5.2 p. 9 — The center of a uniform distribution](../slides/section-5-2.pdf#page=9); [§5.2 p. 11 — Calculating uniform spread](../slides/section-5-2.pdf#page=11); [§5.2 p. 19 — Theoretical and empirical summaries](../slides/section-5-2.pdf#page=19) |
| Find lower/upper percentile cutoffs and central intervals | [§5.2 p. 12 — A percentile cutoff](../slides/section-5-2.pdf#page=12); [§5.2 p. 13 — An upper-tail cutoff](../slides/section-5-2.pdf#page=13); [§5.2 p. 14 — The middle half](../slides/section-5-2.pdf#page=14) |
| Calculate conditional probabilities and conditioned density | [§5.2 p. 15 — A conditional interval](../slides/section-5-2.pdf#page=15); [§5.2 p. 16 — The conditional density](../slides/section-5-2.pdf#page=16); [§5.2 p. 18 — Checking the model](../slides/section-5-2.pdf#page=18) |

### 5.3 The Exponential Distribution

22 → 28 pages. [Textbook 5.3](https://openstax.org/books/introductory-statistics-2e/pages/5-3-the-exponential-distribution)

| Textbook terminology | Revised PDF evidence |
|---|---|
| exponential distribution; continuous random variable | [§5.3 p. 1 — An exponential waiting model](../slides/section-5-3.pdf#page=1) |
| cumulative distribution function (CDF) | [§5.3 p. 11 — Exponential CDF](../slides/section-5-3.pdf#page=11) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Convert mean, rate and time units; specify and sketch the exponential density | [§5.3 p. 3 — Rate notation](../slides/section-5-3.pdf#page=3); [§5.3 p. 4 — Mean waiting time](../slides/section-5-3.pdf#page=4); [§5.3 p. 5 — Converting a mean to a rate](../slides/section-5-3.pdf#page=5); [§5.3 p. 8 — Sketching the exponential density](../slides/section-5-3.pdf#page=8); [§5.3 p. 14 — Units in the exponent](../slides/section-5-3.pdf#page=14) |
| Calculate cumulative, upper-tail and interval probabilities | [§5.3 p. 9 — The upper tail](../slides/section-5-3.pdf#page=9); [§5.3 p. 10 — A wait within a deadline](../slides/section-5-3.pdf#page=10); [§5.3 p. 11 — Exponential CDF](../slides/section-5-3.pdf#page=11); [§5.3 p. 12 — Between two waits](../slides/section-5-3.pdf#page=12) |
| Find percentiles and median; compute SD and expected total lifetime | [§5.3 p. 15 — An exponential percentile](../slides/section-5-3.pdf#page=15); [§5.3 p. 16 — An inverse exponential calculation](../slides/section-5-3.pdf#page=16); [§5.3 p. 17 — Mean and median](../slides/section-5-3.pdf#page=17); [§5.3 p. 18 — Exponential spread](../slides/section-5-3.pdf#page=18); [§5.3 p. 19 — Expected total lifetime](../slides/section-5-3.pdf#page=19) |
| Calculate conditional remaining waits and compare memorylessness | [§5.3 p. 20 — The memoryless property](../slides/section-5-3.pdf#page=20); [§5.3 p. 21 — A remaining wait](../slides/section-5-3.pdf#page=21); [§5.3 p. 22 — Comparing waiting models](../slides/section-5-3.pdf#page=22) |
| Relate exponential waits to Poisson counts and assess assumptions | [§5.3 p. 24 — A Poisson connection](../slides/section-5-3.pdf#page=24); [§5.3 p. 25 — Computing the linked count probability](../slides/section-5-3.pdf#page=25); [§5.3 p. 26 — An empty interval](../slides/section-5-3.pdf#page=26); [§5.3 p. 27 — Model assumptions](../slides/section-5-3.pdf#page=27) |

### 6.1 The Standard Normal Distribution

20 → 22 pages. [Textbook 6.1](https://openstax.org/books/introductory-statistics-2e/pages/6-1-the-standard-normal-distribution)

| Textbook terminology | Revised PDF evidence |
|---|---|
| standard normal distribution | [§6.1 p. 3 — The standard normal](../slides/section-6-1.pdf#page=3) |
| z-scores | [§6.1 p. 21 — Normality matters](../slides/section-6-1.pdf#page=21) |
| Empirical Rule | [§6.1 p. 15 — Empirical Rule](../slides/section-6-1.pdf#page=15) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Read normal notation and identify center, SD and standard normal | [§6.1 p. 2 — Normal notation](../slides/section-6-1.pdf#page=2); [§6.1 p. 3 — The standard normal](../slides/section-6-1.pdf#page=3); [§6.1 p. 7 — At the mean](../slides/section-6-1.pdf#page=7); [§6.1 p. 13 — The center divides the area](../slides/section-6-1.pdf#page=13) |
| Standardize observations, reverse z-scores and compare scales | [§6.1 p. 5 — A positive z-score](../slides/section-6-1.pdf#page=5); [§6.1 p. 6 — A negative z-score](../slides/section-6-1.pdf#page=6); [§6.1 p. 8 — Returning to original units](../slides/section-6-1.pdf#page=8); [§6.1 p. 9 — Comparing different scales](../slides/section-6-1.pdf#page=9); [§6.1 p. 10 — Scores are not probabilities](../slides/section-6-1.pdf#page=10) |
| Apply the empirical rule to central and partial bands | [§6.1 p. 14 — One standard deviation](../slides/section-6-1.pdf#page=14); [§6.1 p. 15 — Empirical Rule](../slides/section-6-1.pdf#page=15); [§6.1 p. 16 — Two standard deviations](../slides/section-6-1.pdf#page=16); [§6.1 p. 17 — Three standard deviations](../slides/section-6-1.pdf#page=17); [§6.1 p. 18 — Areas between standard deviations](../slides/section-6-1.pdf#page=18) |
| Read cumulative normal areas and assess model assumptions | [§6.1 p. 19 — Using a cumulative table](../slides/section-6-1.pdf#page=19); [§6.1 p. 20 — A negative cumulative cutoff](../slides/section-6-1.pdf#page=20); [§6.1 p. 21 — Normality matters](../slides/section-6-1.pdf#page=21) |

### 6.2 Using the Normal Distribution

22 → 26 pages. [Textbook 6.2](https://openstax.org/books/introductory-statistics-2e/pages/6-2-using-the-normal-distribution)

| Textbook terminology | Revised PDF evidence |
|---|---|
| Area to the left | [§6.2 p. 2 — A lower-tail probability](../slides/section-6-2.pdf#page=2) |
| Area to the right | [§6.2 p. 3 — An upper-tail probability](../slides/section-6-2.pdf#page=3) |
| critical value | [§6.2 p. 15 — Critical value](../slides/section-6-2.pdf#page=15) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Define/shade/compute lower-tail, upper-tail, interval and outside probabilities | [§6.2 p. 2 — A lower-tail probability](../slides/section-6-2.pdf#page=2); [§6.2 p. 3 — An upper-tail probability](../slides/section-6-2.pdf#page=3); [§6.2 p. 4 — A probability between cutoffs](../slides/section-6-2.pdf#page=4); [§6.2 p. 5 — Outside an acceptable range](../slides/section-6-2.pdf#page=5); [§6.2 p. 7 — A technology input](../slides/section-6-2.pdf#page=7); [§6.2 p. 8 — Shading a normal probability](../slides/section-6-2.pdf#page=8) |
| Calculate percentile and upper-tail cutoffs with inverse normal | [§6.2 p. 12 — Finding a percentile](../slides/section-6-2.pdf#page=12); [§6.2 p. 13 — Inverse normal input](../slides/section-6-2.pdf#page=13); [§6.2 p. 14 — An upper-tail cutoff](../slides/section-6-2.pdf#page=14); [§6.2 p. 16 — A lower-tail cutoff](../slides/section-6-2.pdf#page=16) |
| Find central intervals, quartiles and IQR | [§6.2 p. 17 — The middle 90%](../slides/section-6-2.pdf#page=17); [§6.2 p. 18 — Quartiles from a model](../slides/section-6-2.pdf#page=18); [§6.2 p. 19 — An interquartile range](../slides/section-6-2.pdf#page=19) |
| Convert probability to expected count; compare empirical frequencies and model limits | [§6.2 p. 10 — From probability to expected count](../slides/section-6-2.pdf#page=10); [§6.2 p. 26 — Checking an empirical normal model](../slides/section-6-2.pdf#page=26); [§6.2 p. 24 — A model boundary](../slides/section-6-2.pdf#page=24) |

### 7.1 The Central Limit Theorem for Sample Means (Averages)

25 → 28 pages. [Textbook 7.1](https://openstax.org/books/introductory-statistics-2e/pages/7-1-the-central-limit-theorem-for-sample-means-averages)

| Textbook terminology | Revised PDF evidence |
|---|---|
| normally distributed; central limit theorem; central limit theorem for means | [§7.1 p. 11 — The central limit theorem](../slides/section-7-1.pdf#page=11) |
| sample size | [§7.1 p. 3 — Sample size versus repetitions](../slides/section-7-1.pdf#page=3) |
| standard error of the mean. | [§7.1 p. 7 — Standard error of the mean](../slides/section-7-1.pdf#page=7) |
| sample mean; mean | [§7.1 p. 2 — Data or sample means?](../slides/section-7-1.pdf#page=2) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Distinguish observations, sample means, sample size and repetitions | [§7.1 p. 2 — Data or sample means?](../slides/section-7-1.pdf#page=2); [§7.1 p. 3 — Sample size versus repetitions](../slides/section-7-1.pdf#page=3); [§7.1 p. 4 — An observation and an average](../slides/section-7-1.pdf#page=4) |
| Specify the sampling distribution and its mean/SE | [§7.1 p. 5 — Center of the sample means](../slides/section-7-1.pdf#page=5); [§7.1 p. 7 — Standard error of the mean](../slides/section-7-1.pdf#page=7); [§7.1 p. 9 — Changing sample size](../slides/section-7-1.pdf#page=9); [§7.1 p. 10 — Reducing standard error](../slides/section-7-1.pdf#page=10); [§7.1 p. 17 — A sampling model](../slides/section-7-1.pdf#page=17) |
| Choose exact normal versus approximate CLT reasoning and check assumptions | [§7.1 p. 12 — An exactly normal population](../slides/section-7-1.pdf#page=12); [§7.1 p. 13 — A skewed population](../slides/section-7-1.pdf#page=13); [§7.1 p. 14 — No universal cutoff](../slides/section-7-1.pdf#page=14); [§7.1 p. 15 — Independence](../slides/section-7-1.pdf#page=15); [§7.1 p. 16 — Sampling without replacement](../slides/section-7-1.pdf#page=16) |
| Calculate tail/interval probabilities, percentiles, quartiles and inverse standardized values | [§7.1 p. 19 — An upper-tail average](../slides/section-7-1.pdf#page=19); [§7.1 p. 20 — A lower-tail average](../slides/section-7-1.pdf#page=20); [§7.1 p. 21 — An average within a range](../slides/section-7-1.pdf#page=21); [§7.1 p. 22 — A percentile of sample means](../slides/section-7-1.pdf#page=22); [§7.1 p. 23 — Quartiles of sample means](../slides/section-7-1.pdf#page=23); [§7.1 p. 24 — A specified standard-error distance](../slides/section-7-1.pdf#page=24) |
| Compare individual and average probabilities and assess a surprising mean | [§7.1 p. 25 — One value versus a mean](../slides/section-7-1.pdf#page=25); [§7.1 p. 27 — A surprising sample mean](../slides/section-7-1.pdf#page=27) |

### 7.2 The Central Limit Theorem for Sums

19 → 21 pages. [Textbook 7.2](https://openstax.org/books/introductory-statistics-2e/pages/7-2-the-central-limit-theorem-for-sums)

| Textbook terminology | Revised PDF evidence |
|---|---|
| normally distributed; central limit theorem for sums | [§7.2 p. 9 — A normal approximation for sums](../slides/section-7-2.pdf#page=9) |
| sample size | [§7.2 p. 5 — Recovering sample size](../slides/section-7-2.pdf#page=5) |
| percentile | [§7.2 p. 14 — A capacity cutoff](../slides/section-7-2.pdf#page=14) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Define sums, their mean/SD and recover sample size | [§7.2 p. 1 — A sample sum](../slides/section-7-2.pdf#page=1); [§7.2 p. 3 — The center of sums](../slides/section-7-2.pdf#page=3); [§7.2 p. 4 — The spread of sums](../slides/section-7-2.pdf#page=4); [§7.2 p. 5 — Recovering sample size](../slides/section-7-2.pdf#page=5); [§7.2 p. 6 — Independent variation](../slides/section-7-2.pdf#page=6) |
| Specify exact/approximate normal sums and check dependence | [§7.2 p. 8 — A sum can be normal](../slides/section-7-2.pdf#page=8); [§7.2 p. 9 — A normal approximation for sums](../slides/section-7-2.pdf#page=9); [§7.2 p. 19 — A skewed population total](../slides/section-7-2.pdf#page=19); [§7.2 p. 20 — Checking dependence](../slides/section-7-2.pdf#page=20) |
| Compute total probabilities, percentile cutoffs and values at given z-scores | [§7.2 p. 11 — A total above a limit](../slides/section-7-2.pdf#page=11); [§7.2 p. 12 — A total below a limit](../slides/section-7-2.pdf#page=12); [§7.2 p. 13 — A total within a range](../slides/section-7-2.pdf#page=13); [§7.2 p. 14 — A capacity cutoff](../slides/section-7-2.pdf#page=14); [§7.2 p. 15 — A specified distance for a sum](../slides/section-7-2.pdf#page=15) |
| Translate between sum and mean events | [§7.2 p. 16 — An equivalent event](../slides/section-7-2.pdf#page=16); [§7.2 p. 17 — The same standardized distance](../slides/section-7-2.pdf#page=17); [§7.2 p. 18 — Sums versus averages](../slides/section-7-2.pdf#page=18) |

### 7.3 Using the Central Limit Theorem

21 → 37 pages. [Textbook 7.3](https://openstax.org/books/introductory-statistics-2e/pages/7-3-using-the-central-limit-theorem)

| Textbook terminology | Revised PDF evidence |
|---|---|
| central limit theorem | [§7.3 p. 22 — Two different ideas](../slides/section-7-3.pdf#page=22) |
| law of large numbers | [§7.3 p. 21 — The law of large numbers](../slides/section-7-3.pdf#page=21) |
| uniform distribution | [§7.3 p. 12 — A uniform total](../slides/section-7-3.pdf#page=12) |
| mean | [§7.3 p. 7 — A mean percentile](../slides/section-7-3.pdf#page=7) |
| exponential distribution | [§7.3 p. 2 — One observation](../slides/section-7-3.pdf#page=2) |
| normal approximation to the binomial; binomial distribution | [§7.3 p. 24 — Normal approximation to the binomial](../slides/section-7-3.pdf#page=24) |
| continuity correction factor | [§7.3 p. 27 — Continuity correction factor](../slides/section-7-3.pdf#page=27) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Choose an individual, average or sum model, especially from exponential data | [§7.3 p. 1 — Choosing the random variable](../slides/section-7-3.pdf#page=1); [§7.3 p. 2 — One observation](../slides/section-7-3.pdf#page=2); [§7.3 p. 3 — An average of observations](../slides/section-7-3.pdf#page=3); [§7.3 p. 4 — Comparing the two events](../slides/section-7-3.pdf#page=4); [§7.3 p. 5 — A total duration](../slides/section-7-3.pdf#page=5); [§7.3 p. 6 — An equivalent threshold](../slides/section-7-3.pdf#page=6) |
| Calculate probabilities and percentiles for uniform-population means/sums | [§7.3 p. 9 — A uniform population](../slides/section-7-3.pdf#page=9); [§7.3 p. 11 — A lower-tail mean](../slides/section-7-3.pdf#page=11); [§7.3 p. 12 — A uniform total](../slides/section-7-3.pdf#page=12); [§7.3 p. 13 — A uniform mean percentile](../slides/section-7-3.pdf#page=13); [§7.3 p. 14 — A uniform total percentile](../slides/section-7-3.pdf#page=14) |
| Find quartiles, IQR and central intervals for means and sums | [§7.3 p. 15 — Quartiles and IQR of sample means](../slides/section-7-3.pdf#page=15); [§7.3 p. 16 — Quartiles and IQR of sums](../slides/section-7-3.pdf#page=16); [§7.3 p. 17 — A central interval for totals](../slides/section-7-3.pdf#page=17) |
| Check binomial approximation criteria, mean/SD and continuity correction | [§7.3 p. 24 — Normal approximation to the binomial](../slides/section-7-3.pdf#page=24); [§7.3 p. 25 — Approximation conditions](../slides/section-7-3.pdf#page=25); [§7.3 p. 26 — The approximating normal model](../slides/section-7-3.pdf#page=26); [§7.3 p. 27 — Continuity correction factor](../slides/section-7-3.pdf#page=27) |
| Apply all five discrete inequality/equality corrections and compare exact probability | [§7.3 p. 28 — At least: continuity correction](../slides/section-7-3.pdf#page=28); [§7.3 p. 29 — At most: continuity correction](../slides/section-7-3.pdf#page=29); [§7.3 p. 30 — More than: continuity correction](../slides/section-7-3.pdf#page=30); [§7.3 p. 31 — Fewer than: continuity correction](../slides/section-7-3.pdf#page=31); [§7.3 p. 32 — Exactly: continuity correction](../slides/section-7-3.pdf#page=32); [§7.3 p. 33 — Checking the approximation](../slides/section-7-3.pdf#page=33) |
| Distinguish CLT from the law of large numbers and assess sampling claims | [§7.3 p. 19 — A population shape problem](../slides/section-7-3.pdf#page=19); [§7.3 p. 20 — A selection problem](../slides/section-7-3.pdf#page=20); [§7.3 p. 22 — Two different ideas](../slides/section-7-3.pdf#page=22); [§7.3 p. 23 — A repeated-sample experiment](../slides/section-7-3.pdf#page=23); [§7.3 p. 37 — A claim about the mean](../slides/section-7-3.pdf#page=37) |

### 8.1 A Single Population Mean using the Normal Distribution

26 → 28 pages. [Textbook 8.1](https://openstax.org/books/introductory-statistics-2e/pages/8-1-a-single-population-mean-using-the-normal-distribution)

| Textbook terminology | Revised PDF evidence |
|---|---|
| error bound for a population mean | [§8.1 p. 5 — Margin of error](../slides/section-8-1.pdf#page=5) |
| confidence level | [§8.1 p. 6 — Confidence level](../slides/section-8-1.pdf#page=6) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Identify parameter, point estimate, margin, confidence and alpha | [§8.1 p. 1 — The target parameter](../slides/section-8-1.pdf#page=1); [§8.1 p. 2 — A point estimate](../slides/section-8-1.pdf#page=2); [§8.1 p. 5 — Margin of error](../slides/section-8-1.pdf#page=5); [§8.1 p. 6 — Confidence level](../slides/section-8-1.pdf#page=6); [§8.1 p. 8 — The two tails](../slides/section-8-1.pdf#page=8) |
| Find critical z and construct known-SD intervals from summaries/raw data | [§8.1 p. 10 — Finding the critical value](../slides/section-8-1.pdf#page=10); [§8.1 p. 11 — The known-SD method](../slides/section-8-1.pdf#page=11); [§8.1 p. 13 — The mean margin of error](../slides/section-8-1.pdf#page=13); [§8.1 p. 14 — Constructing a mean interval](../slides/section-8-1.pdf#page=14); [§8.1 p. 15 — A mean interval from raw data](../slides/section-8-1.pdf#page=15) |
| Sketch/interpret intervals and recover estimate or margin | [§8.1 p. 16 — Interpreting the interval](../slides/section-8-1.pdf#page=16); [§8.1 p. 17 — A fixed parameter](../slides/section-8-1.pdf#page=17); [§8.1 p. 18 — Mean versus individual values](../slides/section-8-1.pdf#page=18); [§8.1 p. 19 — Recovering the point estimate](../slides/section-8-1.pdf#page=19); [§8.1 p. 20 — Recovering the margin](../slides/section-8-1.pdf#page=20); [§8.1 p. 28 — Sketching the confidence interval](../slides/section-8-1.pdf#page=28) |
| Assess confidence/precision/sample-size tradeoffs and calculate a minimum n | [§8.1 p. 21 — More confidence](../slides/section-8-1.pdf#page=21); [§8.1 p. 22 — More observations](../slides/section-8-1.pdf#page=22); [§8.1 p. 23 — More population variation](../slides/section-8-1.pdf#page=23); [§8.1 p. 24 — Planning a sample size](../slides/section-8-1.pdf#page=24); [§8.1 p. 25 — A precision target](../slides/section-8-1.pdf#page=25); [§8.1 p. 26 — Precision and bias](../slides/section-8-1.pdf#page=26) |

### 8.2 A Single Population Mean using the Student t Distribution

24 → 26 pages. [Textbook 8.2](https://openstax.org/books/introductory-statistics-2e/pages/8-2-a-single-population-mean-using-the-student-t-distribution)

| Textbook terminology | Revised PDF evidence |
|---|---|
| standard deviation | [§8.2 p. 1 — An unknown population SD](../slides/section-8-2.pdf#page=1) |
| confidence interval | [§8.2 p. 26 — Sketching the confidence interval](../slides/section-8-2.pdf#page=26) |
| Student's t-distribution; normal distribution | [§8.2 p. 4 — The t distribution](../slides/section-8-2.pdf#page=4) |
| z-score | [§8.2 p. 3 — A t statistic](../slides/section-8-2.pdf#page=3) |
| degrees of freedom | [§8.2 p. 5 — Degrees of freedom](../slides/section-8-2.pdf#page=5) |
| error bound for a population mean | [§8.2 p. 16 — The t margin of error](../slides/section-8-2.pdf#page=16) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Identify unknown sigma, estimated SE, t statistic and degrees of freedom | [§8.2 p. 1 — An unknown population SD](../slides/section-8-2.pdf#page=1); [§8.2 p. 2 — An estimated standard error](../slides/section-8-2.pdf#page=2); [§8.2 p. 3 — A t statistic](../slides/section-8-2.pdf#page=3); [§8.2 p. 5 — Degrees of freedom](../slides/section-8-2.pdf#page=5); [§8.2 p. 6 — Why n-1?](../slides/section-8-2.pdf#page=6) |
| Read t critical values and assess conditions/method selection | [§8.2 p. 8 — A critical t value](../slides/section-8-2.pdf#page=8); [§8.2 p. 9 — Reading a t table](../slides/section-8-2.pdf#page=9); [§8.2 p. 10 — Comparing critical values](../slides/section-8-2.pdf#page=10); [§8.2 p. 12 — A small normal sample](../slides/section-8-2.pdf#page=12); [§8.2 p. 13 — A problematic small sample](../slides/section-8-2.pdf#page=13); [§8.2 p. 15 — Choosing z or t](../slides/section-8-2.pdf#page=15) |
| Construct intervals from summaries/raw data and sketch/interpret them | [§8.2 p. 16 — The t margin of error](../slides/section-8-2.pdf#page=16); [§8.2 p. 17 — Constructing a t interval](../slides/section-8-2.pdf#page=17); [§8.2 p. 18 — Interpreting a t interval](../slides/section-8-2.pdf#page=18); [§8.2 p. 22 — A raw-data interval](../slides/section-8-2.pdf#page=22); [§8.2 p. 26 — Sketching the confidence interval](../slides/section-8-2.pdf#page=26) |
| Assess changes in n/confidence, preserve units and evaluate a claim | [§8.2 p. 19 — Individual spread and mean precision](../slides/section-8-2.pdf#page=19); [§8.2 p. 20 — A higher confidence level](../slides/section-8-2.pdf#page=20); [§8.2 p. 21 — A larger sample](../slides/section-8-2.pdf#page=21); [§8.2 p. 23 — Retaining units](../slides/section-8-2.pdf#page=23); [§8.2 p. 25 — An interval and a claim](../slides/section-8-2.pdf#page=25) |

### 8.3 A Population Proportion

27 → 32 pages. [Textbook 8.3](https://openstax.org/books/introductory-statistics-2e/pages/8-3-a-population-proportion)

| Textbook terminology | Revised PDF evidence |
|---|---|
| confidence intervals | [§8.3 p. 23 — Changing confidence](../slides/section-8-3.pdf#page=23) |
| error bound | [§8.3 p. 15 — A proportion margin of error](../slides/section-8-3.pdf#page=15) |
| confidence level | [§8.3 p. 24 — Changing sample size](../slides/section-8-3.pdf#page=24) |
| binomial distribution | [§8.3 p. 6 — A binary outcome](../slides/section-8-3.pdf#page=6) |
| normal distribution | [§8.3 p. 8 — A proportion sampling model](../slides/section-8-3.pdf#page=8) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| Distinguish count/proportion/parameter, notation, sampling model and estimated SE | [§8.3 p. 2 — A sample proportion](../slides/section-8-3.pdf#page=2); [§8.3 p. 3 — Two notation choices](../slides/section-8-3.pdf#page=3); [§8.3 p. 5 — Count or proportion?](../slides/section-8-3.pdf#page=5); [§8.3 p. 8 — A proportion sampling model](../slides/section-8-3.pdf#page=8); [§8.3 p. 9 — Standardizing a sample proportion](../slides/section-8-3.pdf#page=9); [§8.3 p. 10 — An estimated standard error](../slides/section-8-3.pdf#page=10) |
| Check success/failure counts, independence and sample fraction | [§8.3 p. 11 — Successes and failures](../slides/section-8-3.pdf#page=11); [§8.3 p. 12 — A sparse success sample](../slides/section-8-3.pdf#page=12); [§8.3 p. 13 — Independence for proportions](../slides/section-8-3.pdf#page=13); [§8.3 p. 14 — A sample fraction](../slides/section-8-3.pdf#page=14) |
| Construct/interpret/graph ordinary and plus-four intervals | [§8.3 p. 16 — Constructing a proportion interval](../slides/section-8-3.pdf#page=16); [§8.3 p. 17 — Interpreting a proportion interval](../slides/section-8-3.pdf#page=17); [§8.3 p. 21 — When to use plus four](../slides/section-8-3.pdf#page=21); [§8.3 p. 22 — A plus-four interval](../slides/section-8-3.pdf#page=22); [§8.3 p. 31 — Sketching the confidence interval](../slides/section-8-3.pdf#page=31) |
| Recover estimates/margins and distinguish percentage points | [§8.3 p. 18 — Percentage points](../slides/section-8-3.pdf#page=18); [§8.3 p. 32 — Recovering a proportion estimate](../slides/section-8-3.pdf#page=32) |
| Plan sample size with/without prior estimates and assess precision/bias | [§8.3 p. 25 — Planning a proportion sample](../slides/section-8-3.pdf#page=25); [§8.3 p. 26 — Planning without an estimate](../slides/section-8-3.pdf#page=26); [§8.3 p. 27 — A conservative planning problem](../slides/section-8-3.pdf#page=27); [§8.3 p. 23 — Changing confidence](../slides/section-8-3.pdf#page=23); [§8.3 p. 24 — Changing sample size](../slides/section-8-3.pdf#page=24); [§8.3 p. 28 — Precision cannot remove bias](../slides/section-8-3.pdf#page=28); [§8.3 p. 29 — A claim and an interval](../slides/section-8-3.pdf#page=29) |

### 9.0 Hypothesis Testing: Conceptual Overview

20 → 31 pages. [Textbook overview](https://openstax.org/books/introductory-statistics-2e/pages/9-introduction) · [Textbook 9.1](https://openstax.org/books/introductory-statistics-2e/pages/9-1-null-and-alternative-hypotheses) · [Textbook 9.2](https://openstax.org/books/introductory-statistics-2e/pages/9-2-outcomes-and-the-type-i-and-type-ii-errors) · [Textbook 9.3](https://openstax.org/books/introductory-statistics-2e/pages/9-3-probability-distribution-needed-for-hypothesis-testing) · [Textbook 9.4](https://openstax.org/books/introductory-statistics-2e/pages/9-4-rare-events-the-sample-decision-and-conclusion) · [Textbook 9.5](https://openstax.org/books/introductory-statistics-2e/pages/9-5-additional-information-and-full-hypothesis-test-examples)

| Textbook terminology | Revised PDF evidence |
|---|---|
| Confidence intervals | [§9.0 p. 29 — An interval connection](../slides/section-9-0.pdf#page=29) |
| hypothesis testing; hypothesis test | [§9.0 p. 1 — A claim about a population](../slides/section-9-0.pdf#page=1) |
| hypotheses | [§9.0 p. 5 — Complementary hypotheses](../slides/section-9-0.pdf#page=5) |
| null hypothesis | [§9.0 p. 2 — The null hypothesis](../slides/section-9-0.pdf#page=2) |
| alternative hypothesis | [§9.0 p. 3 — The alternative hypothesis](../slides/section-9-0.pdf#page=3) |
| Type I error | [§9.0 p. 23 — Type I error](../slides/section-9-0.pdf#page=23) |
| Type II error | [§9.0 p. 24 — Type II error](../slides/section-9-0.pdf#page=24) |
| simple random sample; assumption | [§9.0 p. 13 — An assumption check](../slides/section-9-0.pdf#page=13) |
| normally distributed; Central Limit Theorem | [§9.0 p. 9 — The Central Limit Theorem in testing](../slides/section-9-0.pdf#page=9) |
| standard deviation; Student's t-distribution | [§9.0 p. 10 — Choosing a reference distribution](../slides/section-9-0.pdf#page=10) |
| binomial distribution | [§9.0 p. 11 — A proportion test model](../slides/section-9-0.pdf#page=11) |
| p-value | [§9.0 p. 14 — The p-value](../slides/section-9-0.pdf#page=14) |
| α; level of significance | [§9.0 p. 19 — Significance level](../slides/section-9-0.pdf#page=19) |

| Major textbook task or reasoning type | Representative revised PDF pages |
|---|---|
| State null/alternative hypotheses for means/proportions and choose tail direction | [§9.0 p. 2 — The null hypothesis](../slides/section-9-0.pdf#page=2); [§9.0 p. 3 — The alternative hypothesis](../slides/section-9-0.pdf#page=3); [§9.0 p. 4 — Direction of the question](../slides/section-9-0.pdf#page=4); [§9.0 p. 5 — Complementary hypotheses](../slides/section-9-0.pdf#page=5); [§9.0 p. 6 — Mean or proportion hypotheses](../slides/section-9-0.pdf#page=6) |
| Explain the null sampling model, reference distribution, CLT and assumptions | [§9.0 p. 8 — The null sampling model](../slides/section-9-0.pdf#page=8); [§9.0 p. 9 — The Central Limit Theorem in testing](../slides/section-9-0.pdf#page=9); [§9.0 p. 10 — Choosing a reference distribution](../slides/section-9-0.pdf#page=10); [§9.0 p. 11 — A proportion test model](../slides/section-9-0.pdf#page=11); [§9.0 p. 12 — A test statistic](../slides/section-9-0.pdf#page=12); [§9.0 p. 13 — An assumption check](../slides/section-9-0.pdf#page=13) |
| Interpret/shade p-values and use rare-event reasoning | [§9.0 p. 14 — The p-value](../slides/section-9-0.pdf#page=14); [§9.0 p. 15 — Rare-event reasoning](../slides/section-9-0.pdf#page=15); [§9.0 p. 16 — One tail or two?](../slides/section-9-0.pdf#page=16); [§9.0 p. 17 — Shading the p-value](../slides/section-9-0.pdf#page=17); [§9.0 p. 18 — A p-value is not a hypothesis probability](../slides/section-9-0.pdf#page=18) |
| Make reject/nonreject decisions from supplied p-values and write conclusions | [§9.0 p. 20 — A rejection decision](../slides/section-9-0.pdf#page=20); [§9.0 p. 21 — A nonrejection decision](../slides/section-9-0.pdf#page=21); [§9.0 p. 22 — The decision rule](../slides/section-9-0.pdf#page=22); [§9.0 p. 30 — A careful conclusion](../slides/section-9-0.pdf#page=30); [§9.0 p. 31 — Interpreting a supplied test result](../slides/section-9-0.pdf#page=31) |
| Identify Type I/II errors, alpha/beta, power and consequences | [§9.0 p. 23 — Type I error](../slides/section-9-0.pdf#page=23); [§9.0 p. 24 — Type II error](../slides/section-9-0.pdf#page=24); [§9.0 p. 25 — Alpha and beta](../slides/section-9-0.pdf#page=25); [§9.0 p. 26 — Consequences of errors](../slides/section-9-0.pdf#page=26); [§9.0 p. 27 — Power](../slides/section-9-0.pdf#page=27) |
| Distinguish statistical/practical importance and connect matching intervals | [§9.0 p. 28 — Statistical and practical importance](../slides/section-9-0.pdf#page=28); [§9.0 p. 29 — An interval connection](../slides/section-9-0.pdf#page=29) |

## Chapter glossary cross-check

Each glossary term is mapped to a definition or application in its chapter. These supplement the section tables above.

### Chapter 1 glossary

[Textbook glossary](https://openstax.org/books/introductory-statistics-2e/pages/1-key-terms)

| Term | Revised PDF evidence |
|---|---|
| Average | [§1.1 p. 19 — Mean](../slides/section-1-1.pdf#page=19) |
| Blinding | [§1.4 p. 15 — Blinding](../slides/section-1-4.pdf#page=15) |
| Categorical Variable | [§1.1 p. 11 — Categorical variables](../slides/section-1-1.pdf#page=11) |
| Cluster Sampling | [§1.2 p. 21 — Cluster sampling](../slides/section-1-2.pdf#page=21) |
| Continuous Random Variable | [§1.2 p. 5 — Continuous random variable](../slides/section-1-2.pdf#page=5) |
| Control Group | [§1.4 p. 12 — Control groups](../slides/section-1-4.pdf#page=12) |
| Convenience Sampling | [§1.2 p. 23 — Convenience sampling](../slides/section-1-2.pdf#page=23) |
| Cumulative Relative Frequency | [§1.3 p. 5 — Cumulative relative frequency](../slides/section-1-3.pdf#page=5) |
| Data | [§1.1 p. 13 — Data](../slides/section-1-1.pdf#page=13) |
| Double-blind experiment | [§1.4 p. 16 — Double blinding](../slides/section-1-4.pdf#page=16) |
| Experimental Unit | [§1.4 p. 3 — Experimental units](../slides/section-1-4.pdf#page=3) |
| Explanatory Variable | [§1.4 p. 4 — Explanatory variables](../slides/section-1-4.pdf#page=4) |
| Frequency | [§1.3 p. 1 — Frequency](../slides/section-1-3.pdf#page=1) |
| Informed Consent | [§1.4 p. 24 — Informed consent](../slides/section-1-4.pdf#page=24) |
| Institutional Review Board | [§1.4 p. 25 — Institutional Review Board](../slides/section-1-4.pdf#page=25) |
| Lurking Variable | [§1.4 p. 7 — Lurking variables](../slides/section-1-4.pdf#page=7) |
| Nonsampling Error | [§1.2 p. 30 — Nonsampling error](../slides/section-1-2.pdf#page=30) |
| Numerical Variable | [§1.1 p. 10 — Numerical variables](../slides/section-1-1.pdf#page=10) |
| Parameter | [§1.1 p. 14 — Parameter](../slides/section-1-1.pdf#page=14) |
| Placebo | [§1.4 p. 13 — Placebos](../slides/section-1-4.pdf#page=13) |
| Population | [§1.1 p. 6 — Population](../slides/section-1-1.pdf#page=6) |
| Probability | [§1.1 p. 4 — Probability](../slides/section-1-1.pdf#page=4) |
| Proportion | [§1.1 p. 20 — Proportion](../slides/section-1-1.pdf#page=20) |
| Qualitative Data | [§1.2 p. 1 — Qualitative data](../slides/section-1-2.pdf#page=1) |
| Quantitative Data | [§1.2 p. 2 — Quantitative data](../slides/section-1-2.pdf#page=2) |
| Random Assignment | [§1.4 p. 9 — Random assignment](../slides/section-1-4.pdf#page=9) |
| Random Sampling | [§1.2 p. 17 — Simple random sampling](../slides/section-1-2.pdf#page=17) |
| Relative Frequency | [§1.3 p. 3 — Relative frequency](../slides/section-1-3.pdf#page=3) |
| Representative Sample | [§1.1 p. 8 — Representative sample](../slides/section-1-1.pdf#page=8) |
| Response Variable | [§1.4 p. 5 — Response variables](../slides/section-1-4.pdf#page=5) |
| Sample | [§1.1 p. 7 — Sample](../slides/section-1-1.pdf#page=7) |
| Sampling Bias | [§1.2 p. 33 — Sampling bias](../slides/section-1-2.pdf#page=33) |
| Sampling Error | [§1.2 p. 29 — Sampling error](../slides/section-1-2.pdf#page=29) |
| Sampling with Replacement | [§1.2 p. 26 — Sampling with replacement](../slides/section-1-2.pdf#page=26) |
| Sampling without Replacement | [§1.2 p. 27 — Sampling without replacement](../slides/section-1-2.pdf#page=27) |
| Simple Random Sampling | [§1.2 p. 17 — Simple random sampling](../slides/section-1-2.pdf#page=17) |
| Statistic | [§1.1 p. 15 — Statistic](../slides/section-1-1.pdf#page=15) |
| Stratified Sampling | [§1.2 p. 20 — Stratified sampling](../slides/section-1-2.pdf#page=20) |
| Systematic Sampling | [§1.2 p. 22 — Systematic sampling](../slides/section-1-2.pdf#page=22) |
| Treatments | [§1.4 p. 6 — Treatments](../slides/section-1-4.pdf#page=6) |
| Variable | [§1.1 p. 9 — Variable](../slides/section-1-1.pdf#page=9) |

### Chapter 2 glossary

[Textbook glossary](https://openstax.org/books/introductory-statistics-2e/pages/2-key-terms)

| Term | Revised PDF evidence |
|---|---|
| Box plot | [§2.4 p. 2 — Box plot terminology](../slides/section-2-4.pdf#page=2) |
| First Quartile | [§2.3 p. 7 — The lower quartile](../slides/section-2-3.pdf#page=7) |
| Frequency | [§2.1 p. 12 — Frequency line graphs](../slides/section-2-1.pdf#page=12) |
| Frequency Polygon | [§2.2 p. 16 — A frequency polygon](../slides/section-2-2.pdf#page=16) |
| Frequency Table | [§2.3 p. 19 — A percentile from a frequency table](../slides/section-2-3.pdf#page=19) |
| Histogram | [§2.2 p. 1 — A histogram](../slides/section-2-2.pdf#page=1) |
| Interquartile Range | [§2.3 p. 10 — Interquartile range](../slides/section-2-3.pdf#page=10) |
| Interval | [§2.2 p. 2 — Define the intervals](../slides/section-2-2.pdf#page=2) |
| Mean | [§2.5 p. 1 — The mean](../slides/section-2-5.pdf#page=1) |
| Median | [§2.3 p. 4 — The median](../slides/section-2-3.pdf#page=4) |
| Midpoint | [§2.2 p. 16 — A frequency polygon](../slides/section-2-2.pdf#page=16) |
| Mode | [§2.5 p. 8 — The mode](../slides/section-2-5.pdf#page=8) |
| Outlier | [§2.1 p. 8 — A possible outlier](../slides/section-2-1.pdf#page=8) |
| Paired Data Set | [§2.2 p. 21 — Paired data sets](../slides/section-2-2.pdf#page=21) |
| Percentile | [§2.3 p. 1 — Percentile](../slides/section-2-3.pdf#page=1) |
| Quartiles | [§2.3 p. 6 — Quartiles](../slides/section-2-3.pdf#page=6) |
| Relative Frequency | [§2.2 p. 15 — Relative-frequency histogram](../slides/section-2-2.pdf#page=15) |
| Skewed | [§2.6 p. 3 — Right skew](../slides/section-2-6.pdf#page=3) |
| Standard Deviation | [§2.7 p. 8 — Sample standard deviation](../slides/section-2-7.pdf#page=8) |
| Variance | [§2.7 p. 7 — Sample variance](../slides/section-2-7.pdf#page=7) |

### Chapter 3 glossary

[Textbook glossary](https://openstax.org/books/introductory-statistics-2e/pages/3-key-terms)

| Term | Revised PDF evidence |
|---|---|
| AND Event | [§3.1 p. 11 — The intersection](../slides/section-3-1.pdf#page=11) |
| Complement Event | [§3.1 p. 9 — A complement](../slides/section-3-1.pdf#page=9) |
| Conditional Probability | [§3.1 p. 14 — Conditional probability](../slides/section-3-1.pdf#page=14) |
| Conditional Probability of A GIVEN B | [§3.1 p. 14 — Conditional probability](../slides/section-3-1.pdf#page=14) |
| Conditional Probability of One Event Given Another Event | [§3.1 p. 14 — Conditional probability](../slides/section-3-1.pdf#page=14) |
| contingency table | [§3.4 p. 1 — A contingency table](../slides/section-3-4.pdf#page=1) |
| Dependent Events | [§3.2 p. 1 — Independent events](../slides/section-3-2.pdf#page=1) |
| Equally Likely | [§3.1 p. 4 — Equally likely outcomes](../slides/section-3-1.pdf#page=4) |
| Event | [§3.1 p. 3 — An event](../slides/section-3-1.pdf#page=3) |
| Experiment | [§3.1 p. 1 — A probability experiment](../slides/section-3-1.pdf#page=1) |
| Independent Events | [§3.2 p. 1 — Independent events](../slides/section-3-2.pdf#page=1) |
| Mutually Exclusive | [§3.2 p. 8 — Mutually exclusive events](../slides/section-3-2.pdf#page=8) |
| Or Event | [§3.1 p. 12 — The union](../slides/section-3-1.pdf#page=12) |
| Outcome | [§3.1 p. 4 — Equally likely outcomes](../slides/section-3-1.pdf#page=4) |
| Probability | [§3.1 p. 1 — A probability experiment](../slides/section-3-1.pdf#page=1) |
| Sample Space | [§3.3 p. 4 — A disjoint union](../slides/section-3-3.pdf#page=4) |
| Tree Diagram | [§3.5 p. 1 — A tree diagram](../slides/section-3-5.pdf#page=1) |
| Venn Diagram | [§3.5 p. 13 — A Venn diagram](../slides/section-3-5.pdf#page=13) |

### Chapter 4 glossary

[Textbook glossary](https://openstax.org/books/introductory-statistics-2e/pages/4-key-terms)

| Term | Revised PDF evidence |
|---|---|
| Bernoulli Trials | [§4.3 p. 2 — Bernoulli trials](../slides/section-4-3.pdf#page=2) |
| Binomial Experiment | [§4.3 p. 1 — A binomial experiment](../slides/section-4-3.pdf#page=1) |
| Binomial Probability Distribution | [§4.3 p. 8 — Binomial notation](../slides/section-4-3.pdf#page=8) |
| Expected Value | [§4.2 p. 1 — Expected value](../slides/section-4-2.pdf#page=1) |
| Geometric Distribution | [§4.4 p. 5 — Geometric notation](../slides/section-4-4.pdf#page=5) |
| Geometric Experiment | [§4.4 p. 1 — A geometric experiment](../slides/section-4-4.pdf#page=1) |
| Hypergeometric Experiment | [§4.5 p. 1 — A hypergeometric experiment](../slides/section-4-5.pdf#page=1) |
| Hypergeometric Probability | [§4.5 p. 11 — An exact probability](../slides/section-4-5.pdf#page=11) |
| Mean | [§4.2 p. 2 — The weighted mean formula](../slides/section-4-2.pdf#page=2) |
| Mean of a Probability Distribution | [§4.2 p. 1 — Expected value](../slides/section-4-2.pdf#page=1) |
| Poisson Probability Distribution | [§4.6 p. 5 — Poisson notation](../slides/section-4-6.pdf#page=5) |
| Probability Distribution Function (PDF) | [§4.1 p. 9 — A discrete probability distribution](../slides/section-4-1.pdf#page=9) |
| Random Variable (RV) | [§4.1 p. 1 — A random variable](../slides/section-4-1.pdf#page=1) |
| Standard Deviation of a Probability Distribution | [§4.2 p. 12 — Calculate model standard deviation](../slides/section-4-2.pdf#page=12) |
| The Law of Large Numbers | [§4.2 p. 7 — Law of large numbers for averages](../slides/section-4-2.pdf#page=7) |

### Chapter 5 glossary

[Textbook glossary](https://openstax.org/books/introductory-statistics-2e/pages/5-key-terms)

| Term | Revised PDF evidence |
|---|---|
| Conditional Probability | [§5.2 p. 15 — A conditional interval](../slides/section-5-2.pdf#page=15) |
| decay parameter | [§5.3 p. 3 — Rate notation](../slides/section-5-3.pdf#page=3) |
| Exponential Distribution | [§5.3 p. 1 — An exponential waiting model](../slides/section-5-3.pdf#page=1) |
| memoryless property | [§5.3 p. 20 — The memoryless property](../slides/section-5-3.pdf#page=20) |
| Poisson distribution | [§5.3 p. 24 — A Poisson connection](../slides/section-5-3.pdf#page=24) |
| Uniform Distribution | [§5.2 p. 1 — The uniform distribution](../slides/section-5-2.pdf#page=1) |

### Chapter 6 glossary

[Textbook glossary](https://openstax.org/books/introductory-statistics-2e/pages/6-key-terms)

| Term | Revised PDF evidence |
|---|---|
| Normal Distribution | [§6.1 p. 1 — A normal distribution](../slides/section-6-1.pdf#page=1) |
| Standard Normal Distribution | [§6.1 p. 3 — The standard normal](../slides/section-6-1.pdf#page=3) |
| z-score | [§6.1 p. 5 — A positive z-score](../slides/section-6-1.pdf#page=5) |

### Chapter 7 glossary

[Textbook glossary](https://openstax.org/books/introductory-statistics-2e/pages/7-key-terms)

| Term | Revised PDF evidence |
|---|---|
| Average | [§7.1 p. 4 — An observation and an average](../slides/section-7-1.pdf#page=4) |
| Central Limit Theorem | [§7.1 p. 11 — The central limit theorem](../slides/section-7-1.pdf#page=11) |
| Exponential Distribution | [§7.3 p. 2 — One observation](../slides/section-7-3.pdf#page=2) |
| Mean | [§7.1 p. 2 — Data or sample means?](../slides/section-7-1.pdf#page=2) |
| Normal Distribution | [§7.3 p. 24 — Normal approximation to the binomial](../slides/section-7-3.pdf#page=24) |
| Sampling Distribution | [§7.1 p. 1 — A sampling distribution](../slides/section-7-1.pdf#page=1) |
| Standard Error of the Mean | [§7.1 p. 7 — Standard error of the mean](../slides/section-7-1.pdf#page=7) |
| Uniform Distribution | [§7.3 p. 12 — A uniform total](../slides/section-7-3.pdf#page=12) |

### Chapter 8 glossary

[Textbook glossary](https://openstax.org/books/introductory-statistics-2e/pages/8-key-terms)

| Term | Revised PDF evidence |
|---|---|
| Binomial Distribution | [§8.3 p. 6 — A binary outcome](../slides/section-8-3.pdf#page=6) |
| Confidence Interval (CI) | [§8.1 p. 1 — The target parameter](../slides/section-8-1.pdf#page=1) |
| Confidence Level (CL) | [§8.1 p. 6 — Confidence level](../slides/section-8-1.pdf#page=6) |
| Degrees of Freedom (df) | [§8.2 p. 5 — Degrees of freedom](../slides/section-8-2.pdf#page=5) |
| Error Bound for a Population Mean (EBM) | [§8.1 p. 5 — Margin of error](../slides/section-8-1.pdf#page=5) |
| Inferential Statistics | [§8.1 p. 1 — The target parameter](../slides/section-8-1.pdf#page=1) |
| Normal Distribution | [§8.2 p. 4 — The t distribution](../slides/section-8-2.pdf#page=4) |
| Parameter | [§8.1 p. 1 — The target parameter](../slides/section-8-1.pdf#page=1) |
| Point Estimate | [§8.1 p. 2 — A point estimate](../slides/section-8-1.pdf#page=2) |
| Standard Deviation | [§8.2 p. 1 — An unknown population SD](../slides/section-8-2.pdf#page=1) |
| Student's t-Distribution | [§8.2 p. 4 — The t distribution](../slides/section-8-2.pdf#page=4) |

### Chapter 9 glossary

[Textbook glossary](https://openstax.org/books/introductory-statistics-2e/pages/9-key-terms)

| Term | Revised PDF evidence |
|---|---|
| Binomial Distribution | [§9.0 p. 11 — A proportion test model](../slides/section-9-0.pdf#page=11) |
| Central Limit Theorem | [§9.0 p. 9 — The Central Limit Theorem in testing](../slides/section-9-0.pdf#page=9) |
| Confidence Interval (CI) | [§9.0 p. 29 — An interval connection](../slides/section-9-0.pdf#page=29) |
| Hypothesis | [§9.0 p. 2 — The null hypothesis](../slides/section-9-0.pdf#page=2) |
| Hypothesis Testing | [§9.0 p. 1 — A claim about a population](../slides/section-9-0.pdf#page=1) |
| Level of Significance of the Test | [§9.0 p. 19 — Significance level](../slides/section-9-0.pdf#page=19) |
| Normal Distribution | [§9.0 p. 10 — Choosing a reference distribution](../slides/section-9-0.pdf#page=10) |
| p-value | [§9.0 p. 14 — The p-value](../slides/section-9-0.pdf#page=14) |
| Standard Deviation | [§9.0 p. 10 — Choosing a reference distribution](../slides/section-9-0.pdf#page=10) |
| Student's t-Distribution | [§9.0 p. 10 — Choosing a reference distribution](../slides/section-9-0.pdf#page=10) |
| Type I Error | [§9.0 p. 23 — Type I error](../slides/section-9-0.pdf#page=23) |
| Type II Error | [§9.0 p. 24 — Type II error](../slides/section-9-0.pdf#page=24) |

## Verification record

Verification completed on all 36 PDFs and 854 pages: the rebuild passed formula/table width and page-midpoint checks; PDF checks passed page counts, US Letter geometry, source-text completeness, source links and a raster scan of the blank annotation area. All 854 pages were rendered and visually reviewed in 43 contact sheets, with enlarged individual-page checks after corrections. All term/problem evidence references matched the final editable sources and PDF page counts. Numerical checks passed for weighted moments, geometric/hypergeometric formulas, continuity corrections, approximation examples, supplied critical values and confidence calculations. The JSON record includes a SHA-256 hash of each final PDF.

The companion [machine-readable audit](textbook-coverage-audit.json) records every section/term/problem mapping and the source retrieval manifest. Page references must be updated when content is inserted or reordered.
