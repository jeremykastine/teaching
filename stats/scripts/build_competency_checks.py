#!/usr/bin/env python3
"""Build student directions for eight short, face-to-face spreadsheet checks."""
from html import escape
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from course_pages import navigation

COURSE = ROOT / 'stats'
OUT = COURSE / 'excel-checks'

CHECKS = [
    ('01-prepare-data', 'Prepare comma-separated data for analysis', 'Chapters 1–2',
     'Split text into values, transpose to one editable column, sort, and summarize.', '''
<h2>What to learn</h2>
<p>Turn a line of comma-separated numbers into individual numeric cells, arrange the observations in one column, and summarize them with formulas. Keep the original text available so you can check your work.</p>
<h2>Practice example</h2>
<p>Paste this entire line into cell A1 as text:</p>
<pre>12,8,15,10,7,14,9,11,13,6,16,10,8,12,9</pre>
<ol>
<li>Copy A1 to A3. Select A3 and use <strong>Data → Text to Columns → Delimited → Comma</strong>. The 15 observations should occupy A3:O3; leave the cells to the right empty before splitting. If the menus look different, choose the available split-by-delimiter tool and select comma.</li>
<li>Copy A3:O3. Select A6 and use <strong>Paste Special → Transpose</strong> so the observations occupy A6:A20. Paste values if necessary: the final column must contain individually editable numbers.</li>
<li>Select only A6:A20 and sort smallest to largest. Be able to sort largest to smallest as well. With a multi-column record list, select the whole record range before sorting so related fields stay together.</li>
<li>In a separate labeled summary area, calculate the number of observations with <code>=COUNT(A6:A20)</code> and the mean with <code>=AVERAGE(A6:A20)</code>. Confirm the count is 15 and the mean is approximately 10.6667. A count below 15 may mean some entries are still text.</li>
<li>Change the largest observation from 16 to 26. Confirm the mean becomes approximately 11.3333 and the count stays 15. The original text should still be available in A1.</li>
</ol>
<p class="aside">(Excel for the web or a version without the wizard: enter <code>=TEXTSPLIT(A1,",")</code> in A3 if available, then copy its results and paste transposed <em>values</em> into A6. Google Sheets: select the copied text and use <strong>Data → Split text to columns</strong>, choosing comma; then use <strong>Edit → Paste special → Transposed</strong>. You can also split with <code>=SPLIT(A1,",")</code>. Convert formula results to values before sorting or editing individual observations.)</p>
<h2>During your check</h2>
<p>From a new supplied line of data, create a sorted, editable column and a formula-based count and mean. Make one requested correction and show the summary updating.</p>
<h2>Variations to prepare for</h2>
<ul><li>A different number of observations or a different destination cell.</li><li>Semicolons or tabs as the delimiter; negative or decimal values.</li><li>Descending instead of ascending order, or deleting a specified observation. If deleting, ensure the summary still includes all remaining observations.</li></ul>
<h2>Be ready to explain</h2><p>Why one cell containing a whole line of text is not yet a column of numerical observations, and how you verified that no observations were lost.</p>
'''),
    ('02-frequency-table', 'Build a frequency table and bar chart', 'Chapters 1–2',
     'Count categories, calculate relative frequencies, and connect a chart to the results.', '''
<h2>What to learn</h2><p>Build a summary that stays connected to a raw list of categorical observations. Use formulas for the counts and proportions, and make a bar or column chart from the summary.</p>
<h2>Practice example</h2>
<p>Put the heading <strong>Transportation</strong> in A1. Paste these responses into A2:A16, one response per cell:</p>
<pre>Bus
Car
Walk
Car
Bus
Walk
Car
Car
Bus
Walk
Bus
Car
Walk
Bus
Car</pre>
<ol>
<li>In D1:F1 enter <strong>Category</strong>, <strong>Frequency</strong>, and <strong>Relative frequency</strong>. Put Bus, Car, and Walk in D2:D4.</li>
<li>In E2 enter <code>=COUNTIF($A$2:$A$16,D2)</code>, then fill down through E4. The dollar signs keep the raw-data range fixed; the category reference changes as you copy.</li>
<li>In E5 calculate the total with <code>=SUM(E2:E4)</code>. In F2 enter <code>=E2/$E$5</code> and fill through F4. Format F2:F4 as percentages. In F5 use <code>=SUM(F2:F4)</code>.</li>
<li>Check the results: Bus 5, Car 6, Walk 4; total frequency 15 and total relative frequency 100%. Keep the underlying values unrounded.</li>
<li>Select D1:E4 and insert a bar or column chart. Give it a descriptive title. The categories should identify the bars; the total row must not become an extra category.</li>
<li>Change one Car response to Walk. Show the two affected frequencies, relative frequencies, and chart updating while the total stays 15.</li>
</ol>
<p class="aside">(Google Sheets: the formulas are the same. Use <strong>Insert → Chart</strong>, then choose a bar or column chart in the chart editor and check the category labels and data range.)</p>
<h2>During your check</h2><p>Using a supplied short list with three or four categories, create the frequency and relative-frequency table, verify its totals, make the chart, and demonstrate one requested data change.</p>
<h2>Variations to prepare for</h2><ul><li>Different category names, counts, or list length; adjust every raw-data reference.</li><li>A chart of relative frequency instead of frequency.</li><li>One additional category: add a summary row and extend totals and the chart range.</li></ul>
<h2>Be ready to explain</h2><p>What a relative frequency measures and why its denominator is the total number of observations. If the frequencies do not sum to the data count, check for an omitted category or an inconsistent spelling.</p>
'''),
    ('03-target-mean-median', 'Create data with a target mean and median', 'Chapter 2',
     'Build a live summary, then adjust observations to satisfy two statistical targets.', '''
<h2>What to learn</h2><p>Use a spreadsheet to construct a dataset with specified properties. Enter formulas once, then adjust the data while watching the mean and median respond.</p>
<h2>Practice example</h2>
<ol>
<li>Use A2:A6 for exactly five observations. Put labels <strong>Count</strong>, <strong>Sum</strong>, <strong>Mean</strong>, and <strong>Median</strong> in D2:D5. In E2:E5 enter <code>=COUNT(A2:A6)</code>, <code>=SUM(A2:A6)</code>, <code>=AVERAGE(A2:A6)</code>, and <code>=MEDIAN(A2:A6)</code>.</li>
<li>Enter five nonnegative whole numbers with <strong>mean 10 and median 8</strong>. Keep the count at 5. Before experimenting, calculate the required total: count × target mean. Keep the values sorted while you reason about which observation must be in the middle.</li>
<li>Use the summary to check your choices. One possible dataset is 4, 6, 8, 12, 20. Many other solutions work.</li>
<li>Now change only one observation so the <strong>mean becomes 12 while the median remains 8</strong>. With five observations, increasing the mean by 2 requires increasing the total by 10. For the example above, changing 20 to 30 works.</li>
<li>Finally, experiment with changing the median while holding the total, and therefore the mean, fixed. Offset an increase in one observation with an equal decrease in another; check the middle position after each change.</li>
</ol>
<p>Use the underlying results to check your work. Formatting 9.96 to display as 10 does not make its actual value equal to 10. Avoid changing the formulas to display the requested answer.</p>
<p class="aside">(Google Sheets: these formulas and cell-reference rules are the same.)</p>
<h2>During your check</h2><p>Create the summary formulas and a dataset meeting the supplied count, mean, median, and number restrictions. Then make one requested adjustment while preserving the other target. The instructor will choose attainable targets.</p>
<h2>Variations to prepare for</h2><ul><li>Different attainable target means and medians, or allowing negative values.</li><li>Six observations instead of five: the median is the average of the third and fourth values after sorting. Update the formula ranges and required total.</li><li>Preserve the mean while changing the median, or preserve the median while changing the mean. A request to change two values may be used when necessary.</li></ul>
<h2>Be ready to explain</h2><p>How the required total helps you control the mean, why changing an extreme observation can leave the median unchanged, and why the number of observations must remain fixed.</p>
'''),
    ('04-standard-deviation', 'Calculate sample standard deviation two ways', 'Chapter 2',
     'Show deviations and squared deviations, then verify against the built-in function.', '''
<h2>What to learn</h2><p>Show the calculation of a sample standard deviation in visible spreadsheet steps. Use the same data with Excel’s built-in function and verify that the two methods agree.</p>
<h2>Practice example</h2><p>Put the heading <strong>Observation</strong> in A1 and the values 2, 4, 4, 6, 6, 8 in A2:A7. Put <strong>Deviation</strong> in B1 and <strong>Squared deviation</strong> in C1.</p>
<ol>
<li>Build a summary in E2:F8. In E2:E8 put the labels Mean, Count, Squared-deviation sum, Sample variance, Sample standard deviation, Built-in standard deviation, and Difference.</li>
<li>In F2 enter <code>=AVERAGE(A2:A7)</code>; in F3 enter <code>=COUNT(A2:A7)</code>.</li>
<li>In B2 enter <code>=A2-$F$2</code>. In C2 enter <code>=B2^2</code>. Fill both down through row 7. Check that the mean reference stays F2 while each observation reference changes.</li>
<li>In F4 enter <code>=SUM(C2:C7)</code>. In F5 enter <code>=F4/(F3-1)</code>. In F6 enter <code>=SQRT(F5)</code>.</li>
<li>In F7 enter <code>=STDEV.S(A2:A7)</code>. In F8 enter <code>=ABS(F6-F7)</code>. Both standard deviations should be approximately 2.0976; the difference should be zero or extremely small because of computer rounding.</li>
<li>Change the last observation from 8 to 28. Watch the mean, <em>all</em> deviations, variance, and both standard-deviation results update. The two methods must still agree.</li>
</ol>
<p>Keep full precision in formulas and use number formatting to shorten the display. Squaring the deviations prevents positive and negative deviations from canceling. For a <em>sample</em>, divide the squared-deviation sum by n − 1.</p>
<p class="aside">(Google Sheets: <code>STDEV.S</code> works; <code>STDEV</code> also calculates the sample standard deviation. The other formulas are the same.)</p>
<h2>During your check</h2><p>From a supplied list of about six observations, construct both methods, show their agreement, and demonstrate one requested data change. Fill formulas down rather than typing every row separately.</p>
<h2>Variations to prepare for</h2><ul><li>A different list or number of observations: update all affected ranges and use a count formula.</li><li>Add the same constant to every observation and compare the mean and standard deviation before and after.</li><li>If explicitly asked for a population standard deviation, divide by n and compare with <code>STDEV.P</code> instead. Do not mix sample and population methods.</li></ul>
<h2>Be ready to explain</h2><p>Why the mean reference is fixed, why changing one observation affects every deviation, and why the standard deviation uses the original measurement units.</p>
'''),
    ('05-two-way-probability', 'Build a two-way table and compare probabilities', 'Chapter 3',
     'Summarize paired categorical data and choose the correct probability denominators.', '''
<h2>What to learn</h2><p>Use formulas to summarize two categorical variables in a contingency table. Calculate an overall probability, a joint probability, and a conditional probability from that table.</p>
<h2>Practice example</h2><p>Put <strong>Group</strong> and <strong>Choice</strong> in A1:B1. Paste these tab-separated records into A2:B13:</p>
<pre>Morning\tA
Morning\tA
Morning\tA
Morning\tA
Morning\tB
Morning\tB
Afternoon\tA
Afternoon\tA
Afternoon\tB
Afternoon\tB
Afternoon\tB
Afternoon\tB</pre>
<ol>
<li>Set up the table with Group in D1, A in E1, B in F1, and Total in G1. Put Morning in D2, Afternoon in D3, and Total in D4.</li>
<li>In E2 enter <code>=COUNTIFS($A$2:$A$13,$D2,$B$2:$B$13,E$1)</code>. Fill across to F2, then down through row 3. Fixed raw ranges and mixed references let one formula count all four combinations.</li>
<li>Use <code>=SUM(E2:F2)</code> in G2 and fill down to G3. Use <code>=SUM(E2:E3)</code> in E4 and fill across through G4. Check the four inner counts are 4, 2, 2, 4 and the grand total is 12.</li>
<li>In a separate labeled area calculate P(A) with <code>=E4/G4</code>, P(Morning and A) with <code>=E2/G4</code>, and P(A given Morning) with <code>=E2/G2</code>. The results are 1/2, 1/3, and 2/3.</li>
<li>Change one Morning record from A to B. Show the table and all three probabilities updating. Explain why the conditional probability uses the Morning total.</li>
</ol>
<p class="aside">(Google Sheets: the formulas are the same. If the pasted records land in one column, select that column and use <strong>Data → Split text to columns</strong> with the appropriate separator.)</p>
<h2>During your check</h2><p>Build a 2×2 table with totals from a supplied list of about 12 records, calculate the requested probabilities, and demonstrate one changed record. Explain the denominator for each probability.</p>
<h2>Variations to prepare for</h2><ul><li>Different labels or list length; adjust the raw-data ranges.</li><li>The reverse conditional probability, such as P(Morning given A), which uses <code>=E2/E4</code>.</li><li>A complement, such as P(B given Morning), or comparing P(A given Morning) with P(A) to discuss independence in the observed table. Approximate equality in a small sample does not establish population independence.</li></ul>
<h2>Be ready to explain</h2><p>How “and” differs from “given,” and why switching the condition usually changes the denominator and the result.</p>
'''),
    ('06-random-trials', 'Simulate random trials and the law of large numbers', 'Chapters 3–4',
     'Generate 1,000 trials and compare results from 10, 100, and 1,000 observations.', '''
<h2>What to learn</h2><p>Generate random observations efficiently and compare their sample mean with a theoretical expected value. Repeated simulations show how sample size affects the stability of an average.</p>
<h2>Practice example: a fair six-sided die</h2>
<ol>
<li>Put <strong>Roll</strong> in A1. In A2 enter <code>=RANDBETWEEN(1,6)</code>. Fill through A1001. There should be 1,000 simulated rolls. Use the Name Box (the address field beside the formula bar) to select A2:A1001, then <strong>Fill Down</strong> or Ctrl+D; you do not need to drag through 1,000 rows.</li>
<li>Set up D1:G4 with headings <strong>Number of rolls</strong>, <strong>Observed mean</strong>, <strong>Expected mean</strong>, and <strong>Absolute error</strong>. Put 10, 100, and 1000 in D2:D4.</li>
<li>In E2 enter <code>=AVERAGE(A2:A11)</code>; in E3 enter <code>=AVERAGE(A2:A101)</code>; in E4 enter <code>=AVERAGE(A2:A1001)</code>. These are nested samples: the first 10, first 100, and all 1,000 from the same experiment.</li>
<li>In F2 enter <code>=(1+2+3+4+5+6)/6</code>, giving the expected mean 3.5. Link F3 and F4 to F2. In G2 enter <code>=ABS(E2-F2)</code> and fill down through G4.</li>
<li>Show at least four decimal places for means and errors. Compare the three errors, then press <strong>F9</strong> or use <strong>Formulas → Calculate Now</strong> several times to generate new experiments in desktop Excel. All three summaries must update together. In Excel for the web, change a spare cell to trigger recalculation.</li>
<li>Explain the pattern across repeated experiments. Larger samples generally have more stable means and are more likely to be close to 3.5. An individual experiment can have a larger error at 100 rolls than at 10 rolls, or at 1,000 than at 100.</li>
</ol>
<p class="aside">(Google Sheets: use the same formulas and fill-down approach. To trigger a fresh calculation, change a value in an otherwise unused cell. Random functions recalculate as the sheet recalculates; there is no need to use Excel’s F9 shortcut.)</p>
<h2>During your check</h2><p>Generate the 1,000 rolls, create the three-row comparison with formula-based means and errors, and explain several recalculations. Your result does not have to get closer at every sample size. Correct construction and interpretation are what you demonstrate.</p>
<h2>Variations to prepare for</h2><ul><li>A fair die numbered 1 through 8 or 1 through 10: change both the generator and the theoretical mean. For equally likely integers 1 through k, the expected mean is <code>=(1+k)/2</code>.</li><li>Compare the observed proportion of sixes with 1/6 instead of the mean: use, for example, <code>=COUNTIF(A2:A11,6)/COUNT(A2:A11)</code> and corresponding ranges for 100 and 1,000 rolls.</li><li>Preserve one experiment: copy the generated observations and <strong>Paste Special → Values</strong> into a separate area. These snapshots stay fixed; live random formulas change on recalculation. In Sheets use <strong>Paste special → Values only</strong>.</li></ul>
<h2>Optional practice extension</h2><p>Build a running mean with <code>=AVERAGE($A$2:A2)</code> in B2 and fill down. Plot it against trial number with a horizontal reference at 3.5. This graph is extra practice, beyond the basic five-minute check.</p>
<h2>Be ready to explain</h2><p>The law of large numbers concerns the long-run behavior of an average; it does not guarantee that every added observation improves it or that a particular outcome is “due.” Each die roll still has the same outcome probabilities.</p>
'''),
    ('07-normal-probabilities', 'Compare probabilities in a normal model', 'Chapter 6',
     'Link three probability calculations to shared inputs and verify that they sum to one.', '''
<h2>What to learn</h2><p>Build a normal-probability model with separate input cells. Calculate the probabilities below, between, and above two cutoffs, then change an input and interpret the updated results.</p>
<h2>Practice example</h2>
<ol>
<li>Put the labels Mean, Standard deviation, Lower cutoff, and Upper cutoff in A2:A5. Put 100, 15, 85, and 115 in B2:B5. These describe a normally distributed measurement; the standard deviation must be positive and the lower cutoff must be below the upper cutoff.</li>
<li>In D2:D7 label the outputs Cumulative at lower cutoff, Cumulative at upper cutoff, Below lower cutoff, Between cutoffs, Above upper cutoff, and Total probability.</li>
<li>In E2 enter <code>=NORM.DIST(B4,$B$2,$B$3,TRUE)</code>; in E3 enter <code>=NORM.DIST(B5,$B$2,$B$3,TRUE)</code>. <code>TRUE</code> requests cumulative probability, the area to the left of the cutoff.</li>
<li>In E4 enter <code>=E2</code>, in E5 enter <code>=E3-E2</code>, and in E6 enter <code>=1-E3</code>. In E7 enter <code>=SUM(E4:E6)</code>. The three disjoint regions cover the entire distribution.</li>
<li>Format E4:E7 as percentages. Expect approximately 15.87%, 68.27%, 15.87%, and 100%. Keep full precision in the formulas.</li>
<li>Increase B3 from 15 to 30, leaving both cutoffs fixed. The middle probability drops to about 38.29%, and each outer probability increases to about 30.85%. Explain why a wider distribution puts less probability inside this fixed interval.</li>
</ol>
<p class="aside">(Google Sheets: use <code>=NORMDIST(B4,$B$2,$B$3,TRUE)</code> and the corresponding upper-cutoff formula. The remaining formulas are unchanged.)</p>
<h2>During your check</h2><p>Build the linked calculations for supplied parameters and cutoffs, verify the probability total, and demonstrate a requested input change. Briefly explain the affected region or regions.</p>
<h2>Variations to prepare for</h2><ul><li>Different means, positive standard deviations, or asymmetric cutoffs.</li><li>Change the mean while holding the cutoffs fixed, or move one cutoff while keeping the distribution fixed.</li><li>Report the probability outside the interval by adding the two tails, or the expected count inside the interval among a supplied number of independent observations using count × probability.</li></ul>
<h2>Be ready to explain</h2><p>Why the middle region requires subtraction and the upper tail requires a complement. <code>FALSE</code> returns a density height, which is not the requested area. For a continuous normal variable, including or excluding a single endpoint does not change the probability.</p>
'''),
    ('08-confidence-intervals', 'Compare sample sizes and confidence intervals', 'Chapters 7–8',
     'Fill a comparison table for standard errors, margins of error, and interval endpoints.', '''
<h2>What to learn</h2><p>Build linked confidence-interval calculations for several sample sizes. Separate fixed inputs from calculations, use cell references correctly, and explain how the margin of error changes.</p>
<h2>Practice example: known population standard deviation</h2>
<p>Assume independent random observations from a normal population with <em>known</em> population standard deviation. Use a sample mean of 50 and population standard deviation of 10. The supplied critical value 1.96 gives an approximately 95% confidence interval. Hold the mean and population standard deviation fixed to isolate the effect of sample size.</p>
<ol>
<li>Put Sample mean, Population standard deviation, and Critical value in A2:A4; enter 50, 10, and 1.96 in B2:B4.</li>
<li>In D1:I1 enter <strong>Sample size</strong>, <strong>Standard error</strong>, <strong>Margin of error</strong>, <strong>Lower endpoint</strong>, <strong>Upper endpoint</strong>, and <strong>Interval width</strong>. Put 25, 100, and 400 in D2:D4.</li>
<li>In E2 enter <code>=$B$3/SQRT(D2)</code>. In F2 enter <code>=$B$4*E2</code>. In G2 enter <code>=$B$2-F2</code>; in H2 enter <code>=$B$2+F2</code>; in I2 enter <code>=H2-G2</code>.</li>
<li>Fill E2:I2 down through row 4. Verify the input references stay fixed while the sample-size and intermediate-result references move with the row.</li>
<li>Check that standard errors are 2, 1, and 0.5; margins of error are 3.92, 1.96, and 0.98; and the interval endpoints are 46.08–53.92, 48.04–51.96, and 49.02–50.98.</li>
<li>Change the supplied critical value from 1.96 to 2.576, representing approximately 99% confidence. Show the margins and widths increasing while the standard errors stay fixed.</li>
</ol>
<p class="aside">(Google Sheets: all formulas and cell-reference rules are the same.)</p>
<h2>During your check</h2><p>Build the three-row comparison using supplied inputs and a supplied critical value, fill formulas efficiently, and demonstrate one requested change. You do not need to calculate the critical value yourself.</p>
<h2>Variations to prepare for</h2><ul><li>Different positive sample sizes, means, population standard deviations, or supplied critical values.</li><li>Find a sample size that halves the margin of error: multiply the original sample size by four when the population standard deviation and confidence level stay fixed. Verify with the table.</li><li>Change the sample mean alone and explain why both endpoints shift by the same amount while interval widths stay unchanged.</li></ul>
<h2>Be ready to explain</h2><p>The difference between population standard deviation and standard error; why quadrupling sample size halves the standard error; and why higher confidence requires a wider interval. The confidence level describes the long-run success rate of the interval procedure, rather than the percentage of individual observations in this interval.</p>
<p>This check uses known population standard deviation and a z critical value. If the population standard deviation is unknown, a procedure using sample standard deviation and a t critical value is a different model; do not substitute it into these directions without an explicit instruction.</p>
'''),
]

def main():
    OUT.mkdir(exist_ok=True)
    for i, (slug, title, coverage, summary, body) in enumerate(CHECKS, 1):
        previous = f'<a href="{CHECKS[i-2][0]}.html">Previous check</a>' if i > 1 else ''
        following = f'<a href="{CHECKS[i][0]}.html">Next check</a>' if i < len(CHECKS) else ''
        (OUT / f'{slug}.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Check {i}: {escape(title)} · Statistics</title><link rel="stylesheet" href="../excel-checks.css"></head>
<body><main><header><p class="eyebrow">Statistics · Excel competency check {i} · {coverage}</p>
<nav aria-label="Breadcrumb"><a href="../../index.html#stats">Teaching</a> / <a href="../excel-competency-checks.html">Excel competency checks</a></nav>
<h1>{escape(title)}</h1><p>{escape(summary)}</p>
<p class="callout">Prepare to build and explain a working spreadsheet face to face in about five minutes after practicing. The example below teaches the steps; your instructor may supply new data and choose one of the listed variations. Variations are alternatives, not additional tasks all required in one check.</p></header>
{body}<footer><nav aria-label="Other checks" class="links">{previous}<a href="../excel-competency-checks.html">All eight checks</a>{following}</nav></footer>
</main></body></html>''')
    rows = ''.join(f'<li><p class="meta">Check {i} · {coverage}</p><h2><a href="excel-checks/{slug}.html">{escape(title)}</a></h2><p>{escape(summary)}</p></li>'
                   for i, (slug, title, coverage, summary, _) in enumerate(CHECKS, 1))
    (COURSE / 'excel-competency-checks.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Excel competency checks · Statistics</title><link rel="stylesheet" href="excel-checks.css"></head>
<body><main><header><p class="eyebrow">MSC 201 · Statistics</p><h1>Excel competency checks</h1>{navigation('stats', 'excel-competency-checks.html')}
<p>Learn these spreadsheet skills, practice with the examples, and demonstrate them to your instructor face to face. Each check combines several connected calculations or operations with a short explanation.</p></header>
<section><h2>How to prepare</h2><ul>
<li>Open the page for the check and practice its complete workflow in Excel until you can build it efficiently from a fresh worksheet with new data. Relevant Google Sheets differences appear in parentheses.</li>
<li>A prepared demonstration should take about five minutes. The detailed directions are for learning in advance; practice itself may take longer.</li>
<li>The instructor supplies the task data, targets, and any needed critical values. Be ready for a listed variation and one small input change. You do not need to complete every variation in one check.</li>
<li>Use formulas linked to the data and inputs. Be able to show the formulas, fill them across or down, explain fixed versus changing cell references, and explain the result. A page of typed final answers does not demonstrate these skills.</li>
<li>Use clear labels and readable number formats. Keep full precision in calculations. These examples assume English function names and comma argument separators; regional settings may use semicolons.</li>
</ul></section><section><h2>The eight checks</h2><ul class="resources">{rows}</ul></section>
<footer><p>Course alignment: sampling and descriptive statistics, probability and expected value, normal models, sampling distributions, and confidence intervals. The random-trial experiment illustrates the law of large numbers.</p>
<details><summary>Spreadsheet help</summary><ul>
<li><a href="https://support.microsoft.com/en-us/excel/split-a-cell-in-excel">Microsoft: splitting text and transposing values</a></li>
<li><a href="https://support.microsoft.com/en-us/excel/statistical-functions-reference">Microsoft: statistical functions</a></li>
<li><a href="https://support.microsoft.com/en-gb/excel/functions/randbetween-function">Microsoft: RANDBETWEEN and recalculation</a></li>
<li><a href="https://support.google.com/docs/answer/6325535?hl=en">Google Sheets: splitting text into columns</a></li>
<li><a href="https://support.google.com/docs/table/25273?hl=en">Google Sheets: function reference</a></li>
</ul></details></footer></main></body></html>''')
    print('Built competency-check index and eight student direction pages.')


if __name__ == '__main__':
    main()
