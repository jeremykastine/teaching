#!/usr/bin/env python3
"""Build the spreadsheet-check index and directions for Checks 1 and 2."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

COURSE = ROOT / 'stats'
OUT = COURSE / 'excel-checks'

# Existing URL slugs are stable so previously saved version links keep working.
CHECKS = [
    ('01-match-summary', 'Match Count, Mean, Median, and Mode', 'Chapter 2',
     'Create 20–30 observations of your own to match generated summary statistics.', '''
<h2>Set up your spreadsheet</h2>
<p>Open a new, blank Excel workbook. Put <strong>Observation</strong> in A1 and enter your own numbers in A2 downward, one number per cell. Reserve column A for observations only.</p>
<p>One possible summary layout is:</p>
<div class="spreadsheet-table-wrap"><table class="task-table spreadsheet-layout"><thead><tr><th>Label cell</th><th>Label</th><th>Formula cell</th><th>Formula</th></tr></thead><tbody>
<tr><td>C2</td><td>Count</td><td>D2</td><td><code>=COUNT(A:A)</code></td></tr>
<tr><td>C3</td><td>Mean</td><td>D3</td><td><code>=AVERAGE(A:A)</code></td></tr>
<tr><td>C4</td><td>Median</td><td>D4</td><td><code>=MEDIAN(A:A)</code></td></tr>
<tr><td>C5</td><td>Mode(s)</td><td>D5</td><td><code>=MODE.MULT(A:A)</code></td></tr>
</tbody></table></div>
<p>Keep D6 empty. Enter <code>MODE.MULT</code> once in D5; two modes spill into D5:D6. If you see <code>#SPILL!</code>, clear the cells blocking the results. If you see <code>#N/A</code>, check whether any observation repeats. The text header in A1 is ignored by these formulas.</p>
<p>Changing a number in column A should immediately update the summary. Display enough decimal places to judge the mean error; changing the number format does not change the underlying answer.</p>
<h2>Reason about the median</h2>
<p>Think about your observations in sorted order. For an odd count, the median is the middle observation. For an even count, it is the average of the two middle observations.</p>
<p>For example, with 24 observations, the median comes from positions 12 and 13. Because the header occupies A1, those positions are A13 and A14 after sorting the observations. Decide what the middle value or pair must be, then consider how many observations should lie on either side. Recheck the middle positions whenever an adjustment changes the order.</p>
<h2>Reason about the mode or modes</h2>
<p>A mode is a value occurring most often. For a one-mode target, that value must occur more often than every other value. For two modes, both target values must tie for the highest frequency, with every other value occurring less often. Watch for accidental repetitions as you edit. The order in which <code>MODE.MULT</code> lists two modes does not matter.</p>
<h2>Reason about the mean</h2>
<p>The required total is count × target mean. Changing the total by a small amount changes the mean by that amount divided by the count. If your mean is too low, the total must increase; if it is too high, the total must decrease.</p>
<p>Experiment with values away from the middle positions and required repetitions. Use progressively smaller decimal adjustments while staying between 0 and 1,000. Recheck the count, median, and mode(s) after each adjustment. Your instructor decides whether the mean is close enough; there is no fixed numerical tolerance.</p>
<p>There are many possible datasets. Use these ideas to guide your own guesses and corrections, and be ready to explain how you could narrow the mean error further while preserving the exact requirements.</p>
'''),
    ('01-prepare-data', 'Match Mean, Range, and Spread', 'Chapter 2',
     'Create ten observations to match a generated mean, range, and standard deviation or variance, showing the spread calculation step by step.', '''
<h2>Set up your spreadsheet</h2>
<p>Open a new, blank Excel workbook. Put <strong>Observation</strong> in A1 and enter exactly ten numbers of your own in A2:A11, one per cell. All values must be between 0 and 1,000 inclusive; decimals are allowed. Reserve column A for observations only.</p>
<p>Work from left to right. One possible layout is:</p>
<div class="spreadsheet-table-wrap"><table class="task-table spreadsheet-layout mobile-cards"><thead><tr><th>Column</th><th>Heading in row 1</th><th>Formula in row 2</th><th>What to do</th></tr></thead><tbody>
<tr><td data-label="Column">A</td><td data-label="Heading in row 1">Observation</td><td data-label="Formula in row 2">Your chosen numbers</td><td data-label="What to do">Enter ten values in A2:A11.</td></tr>
<tr><td data-label="Column">B</td><td data-label="Heading in row 1">Mean</td><td data-label="Formula in row 2"><code>=AVERAGE(A:A)</code></td><td data-label="What to do">Fill B2 down through B11.</td></tr>
<tr><td data-label="Column">C</td><td data-label="Heading in row 1">Deviation from mean</td><td data-label="Formula in row 2"><code>=A2-B2</code></td><td data-label="What to do">Fill C2 down through C11.</td></tr>
<tr><td data-label="Column">D</td><td data-label="Heading in row 1">Squared deviation</td><td data-label="Formula in row 2"><code>=C2^2</code></td><td data-label="What to do">Fill D2 down through D11.</td></tr>
<tr><td data-label="Column">E</td><td data-label="Heading in row 1">Sum of squared deviations</td><td data-label="Formula in row 2"><code>=SUM(D:D)</code></td><td data-label="What to do">Enter once in E2.</td></tr>
<tr><td data-label="Column">F</td><td data-label="Heading in row 1">Population variance or Sample variance</td><td data-label="Formula in row 2">Choose the formula below.</td><td data-label="What to do">Enter once in F2.</td></tr>
<tr><td data-label="Column">G</td><td data-label="Heading in row 1">Population standard deviation or Sample standard deviation</td><td data-label="Formula in row 2"><code>=SQRT(F2)</code></td><td data-label="What to do">Use G2 only when standard deviation is requested.</td></tr>
</tbody></table></div>
<p>In B2, <code>=AVERAGE(A:A)</code> calculates the mean of the entire observation column. Drag the fill handle down through B11 (or select B2:B11 and use Fill Down). Every copied formula still refers to column A, so <strong>the same current mean appears in all ten rows</strong>. You do not need dollar signs. Do not use a moving range such as <code>=AVERAGE(A2:A11)</code> and drag it down: that would leave out observations as the range shifts. The text heading in A1 is ignored.</p>
<p>Fill C2 and D2 down through row 11. Each deviation uses the observation and mean on its own row. When you change any observation, the mean in every row and all the deviations must update. Squaring the deviations prevents positive and negative differences from canceling.</p>
<h2>Choose the correct division and stopping point</h2>
<div class="spreadsheet-table-wrap"><table class="task-table spreadsheet-layout mobile-cards"><thead><tr><th>Requested measure</th><th>Formula in F2</th><th>Final result</th></tr></thead><tbody>
<tr><td data-label="Requested measure">Population variance</td><td data-label="Formula in F2"><code>=E2/COUNT(A:A)</code></td><td data-label="Final result">F2; divide by n = 10 and stop.</td></tr>
<tr><td data-label="Requested measure">Population standard deviation</td><td data-label="Formula in F2"><code>=E2/COUNT(A:A)</code></td><td data-label="Final result">G2 with <code>=SQRT(F2)</code>.</td></tr>
<tr><td data-label="Requested measure">Sample variance</td><td data-label="Formula in F2"><code>=E2/(COUNT(A:A)-1)</code></td><td data-label="Final result">F2; divide by n − 1 = 9 and stop.</td></tr>
<tr><td data-label="Requested measure">Sample standard deviation</td><td data-label="Formula in F2"><code>=E2/(COUNT(A:A)-1)</code></td><td data-label="Final result">G2 with <code>=SQRT(F2)</code>.</td></tr>
</tbody></table></div>
<p>Use the row matching your generated problem. Label F1 with the correct kind of variance, and G1 with the correct kind of standard deviation if needed. Variance is the division result; take its square root only when the problem asks for standard deviation. Show these steps rather than using <code>VAR.P</code>, <code>VAR.S</code>, <code>STDEV.P</code>, or <code>STDEV.S</code> as a shortcut.</p>
<h2>Calculate the range separately</h2>
<p>Put <strong>Range</strong> in I2 and <code>=MAX(A:A)-MIN(A:A)</code> in J2. Put <strong>Count</strong> in I3 and <code>=COUNT(A:A)</code> in J3. Keep these summaries outside column A so they are not counted as observations. Your count must remain exactly 10.</p>
<p>Keep full precision in every calculation. Display enough decimal places to compare your mean and requested spread with their targets; rounding the display does not change the underlying result. These formulas also work in Google Sheets.</p>
<h2>Reason about the mean and range</h2>
<p>The required total is 10 × target mean. If the current mean is too low, increase the total; if it is too high, decrease the total. Increasing the total by 1 increases the mean by 0.1.</p>
<p>Choose a minimum and maximum whose difference is the required range. Their locations are yours to choose; the problem does not give a required minimum or maximum. To keep the range fixed, retain at least one observation at each endpoint and keep the other values between them. If the target mean is difficult to reach within those endpoints, try shifting the entire interval.</p>
<p>Adding the same amount to every observation shifts the mean by that amount and leaves both range and spread unchanged. Stay between 0 and 1,000. This can help you correct the mean after you have a suitable range and spread.</p>
<h2>Reason about the spread</h2>
<p>With the mean and endpoints fixed, moving two interior values apart by equal amounts increases their spread while preserving their total. Moving them closer together decreases spread. Keep each value within the endpoints and watch the spreadsheet recalculate.</p>
<p>Try different arrangements: values clustered near the center, values clustered near both endpoints, or many values near one end with a few farther away. A fixed range does not determine the variance or standard deviation. Recheck the mean, range, and count after each adjustment, and use progressively smaller decimal changes to refine the requested spread.</p>
<p>The spread target is rounded to four decimal places. Aim for a mean and requested spread as close as possible to the displayed targets; your instructor decides whether they are close enough, as in Check 1. Count and range must match exactly. There is no fixed numerical tolerance.</p>
<p>Many datasets can work. You do not need to recover the hidden original observations or reproduce their shape. Use your own guesses and corrections, and be ready to explain your division, your stopping point, and how you could refine the remaining errors.</p>
'''),
    ('02-frequency-table', 'Compare Risk and Reward', 'Chapter 4',
     'Use one live calculation table for two probability distributions, record both results, and orally compare expected net gain and short-term variability.', None),
    ('04-binomial-distribution', 'Compare Binomial Theory and Simulation', 'Chapter 4',
     'Build a probability triangle and compare its final row with the results of 100 simulated experiments.', None),
]


def build_summary_check(body):
    (OUT / '01-match-summary.html').write_text('''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Check 1: Match Count, Mean, Median, and Mode · Statistics</title><link rel="stylesheet" href="../excel-checks.css"><script defer src="generators.js"></script><script defer src="match-summary-page.js?v=20261020-underline-phrases"></script></head>
<body><main><header><p class="eyebrow">Statistics · Excel competency check 1</p>
<h1>Match Count, Mean, Median, and Mode</h1>
<p id="summary-problem" aria-live="polite">Loading your problem…</p>
<p>Make an Excel spreadsheet that helps you guess and check which observations would have these outcomes.</p></header>
<noscript><p class="callout">Enable JavaScript to generate a problem.</p></noscript>
<div class="generator-toolbar"><button id="regenerate" class="primary" type="button">Regenerate problem</button></div>
<section aria-labelledby="requirements-heading"><h2 id="requirements-heading">Requirements</h2>
<ul>
<li>A new Excel workbook with your own values in column A, one observation per cell, all between 0 and 1,000 inclusive. Decimals are allowed.</li>
<li>Exactly the required number of numerical observations.</li>
<li>An exact match for the median and the complete set of modes, with no additional modes. For two modes, both occur equally often and more frequently than every other value.</li>
<li>A mean approximately equal to the target, close enough to satisfy your instructor.</li>
<li>Labeled, live formulas using <code>COUNT</code>, <code>AVERAGE</code>, <code>MEDIAN</code>, and <code>MODE.MULT</code>, linked to column A and updating when its values change.</li>
</ul></section>
<p><a href="01-match-summary-help.html">Talk me through the spreadsheet setup and how to reason about adjustments →</a></p>
<footer><nav aria-label="Other checks" class="links"><a href="../excel-competency-checks.html">All checks</a><a href="01-prepare-data.html">Next check</a></nav></footer>
</main></body></html>''')
    (OUT / '01-match-summary-help.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Spreadsheet setup and reasoning · Excel check 1</title><link rel="stylesheet" href="../excel-checks.css"></head>
<body><main><header><p class="eyebrow">Statistics · Excel competency check 1 · Help</p>
<h1>Spreadsheet setup and reasoning</h1><p><a href="01-match-summary.html">Back to the problem</a></p></header>
{body}
<footer><a href="01-match-summary.html">Back to the problem</a></footer></main></body></html>''')


def build_spread_check(body):
    # Keep the old Check 2 URL so existing course links open its replacement.
    (OUT / '01-prepare-data.html').write_text('''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Check 2: Match Mean, Range, and Spread · Statistics</title><link rel="stylesheet" href="../excel-checks.css?v=20261023-mobile"><script defer src="match-spread-generator.js?v=20261023"></script><script defer src="match-spread-page.js?v=20261023"></script></head>
<body><main><header><p class="eyebrow">Statistics · Excel competency check 2</p>
<h1>Match Mean, Range, and Spread</h1>
<p id="spread-problem" aria-live="polite">Loading your problem…</p>
<p>Make an Excel spreadsheet that helps you guess and check which observations would have these outcomes.</p></header>
<noscript><p class="callout">Enable JavaScript to generate a problem.</p></noscript>
<div class="generator-toolbar"><button id="regenerate" class="primary" type="button">Regenerate problem</button></div>
<section aria-labelledby="requirements-heading"><h2 id="requirements-heading">Requirements</h2>
<ul>
<li>A new Excel workbook with exactly ten of your own values in A2:A11, one observation per cell, all between 0 and 1,000 inclusive. Decimals are allowed.</li>
<li>An exact match for the count and range.</li>
<li>A mean and the requested standard deviation or variance approximately equal to their targets, close enough to satisfy your instructor. The spread target is rounded to four decimal places.</li>
<li>Labeled, live formulas from left to right: observations, a column repeating the current mean, deviations from that mean, squared deviations, their sum, the correct division, and a square root only if standard deviation is requested.</li>
<li>Calculate the mean with <code>AVERAGE</code> of the entire observation column and fill it down. Use <code>SUM</code> and division by n for a population or n − 1 for a sample. Show the spread calculation step by step rather than using a built-in variance or standard-deviation shortcut.</li>
<li>A separate range calculation using <code>MAX</code> minus <code>MIN</code>, and a <code>COUNT</code> formula to confirm ten observations. All calculations must update when your observations change.</li>
</ul></section>
<p><a href="02-match-spread-help.html">Talk me through the spreadsheet setup and how to reason about adjustments →</a></p>
<footer><nav aria-label="Other checks" class="links"><a href="01-match-summary.html">Previous check</a><a href="../excel-competency-checks.html">All checks</a><a href="02-frequency-table.html">Next check</a></nav></footer>
</main></body></html>''')
    (OUT / '02-match-spread-help.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Spreadsheet setup and reasoning · Excel check 2</title><link rel="stylesheet" href="../excel-checks.css?v=20261023-mobile"></head>
<body><main><header><p class="eyebrow">Statistics · Excel competency check 2 · Help</p>
<h1>Spreadsheet setup and reasoning</h1><p><a href="01-prepare-data.html">Back to the problem</a></p></header>
{body}
<footer><a href="01-prepare-data.html">Back to the problem</a></footer></main></body></html>''')


def main():
    OUT.mkdir(exist_ok=True)
    # Checks 3 and 4 have their own student pages and generators.
    build_summary_check(CHECKS[0][4])
    build_spread_check(CHECKS[1][4])
    rows = ''.join(f'<li><p class="meta">Check {i} · {coverage}</p><h2><a href="excel-checks/{slug}.html">{escape(title)}</a></h2><p>{escape(summary)}</p></li>'
                   for i, (slug, title, coverage, summary, _) in enumerate(CHECKS, 1))
    (COURSE / 'excel-competency-checks.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Excel competency checks · Statistics</title><link rel="stylesheet" href="excel-checks.css"></head>
<body><main><header><h1>Excel Competency Checks</h1></header>
<section aria-label="Competency checks"><ul class="resources">{rows}</ul></section>
<section><h2>How to prepare</h2><ul>
<li>Open the page for the check and practice its complete workflow in Excel until you can build it efficiently from a fresh worksheet with new data. Relevant Google Sheets differences appear in parentheses.</li>
<li>A prepared demonstration should take about five minutes. The detailed directions are for learning in advance; practice itself may take longer.</li>
<li>Every check has a <strong>Regenerate problem</strong> button that changes the data, parameters, or requirements within the same skill. Check 1 randomly alternates between one and two modes. Check 2 randomly chooses a population or sample standard deviation or variance. Check 4 supplies a probability of success and a number of trials for a 100-experiment simulation. Use one generated task throughout your attempt.</li>
<li>For a live check, open the skill page, regenerate a fresh problem in front of the instructor, and use that version for the entire attempt. Demonstrate the work in Excel or Sheets; these pages do not submit or grade a workbook.</li>
<li>Follow the instructions link on each check page to learn the worksheet setup and practice the formulas.</li>
<li>Use labeled formulas linked to the data and inputs. Be able to fill formulas across or down and show how the results update. For Check 3, record both games’ results in a separate comparison area. For Check 4, keep both charts linked to the probability and simulation tables.</li>
<li>Use clear labels and readable number formats. Keep full precision in calculations. These examples assume English function names and comma argument separators; regional settings may use semicolons.</li>
</ul></section>
<footer><p>Course alignment includes descriptive statistics, expected value and standard deviation, and the binomial distribution.</p>
<details><summary>Spreadsheet help</summary><ul>
<li><a href="https://support.microsoft.com/en-us/excel/split-a-cell-in-excel">Microsoft: splitting text and transposing values</a></li>
<li><a href="https://support.microsoft.com/en-us/excel/statistical-functions-reference">Microsoft: statistical functions</a></li>
<li><a href="https://support.microsoft.com/en-us/excel/functions/rand-function">Microsoft: RAND and recalculation</a></li>
<li><a href="https://support.google.com/docs/answer/6325535?hl=en">Google Sheets: splitting text into columns</a></li>
<li><a href="https://support.google.com/docs/table/25273?hl=en">Google Sheets: function reference</a></li>
</ul></details></footer></main></body></html>''')
    print('Built competency-check index and directions for Checks 1 and 2.')


if __name__ == '__main__':
    main()

