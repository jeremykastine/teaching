#!/usr/bin/env python3
"""Build student directions for nine short, face-to-face spreadsheet checks."""
from html import escape
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from course_pages import navigation

COURSE = ROOT / 'stats'
OUT = COURSE / 'excel-checks'

# Existing URL slugs are stable so previously saved version links keep working.
CHECKS = [
    ('01-match-summary', 'Match Count, Mean, Median, and Mode', 'Chapter 2',
     'Create 50–100 observations of your own to match generated summary statistics.', '''
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
<p>For example, with 60 observations, the median comes from positions 30 and 31. Because the header occupies A1, those positions are A31 and A32 after sorting the observations. Decide what the middle value or pair must be, then consider how many observations should lie on either side. Recheck the middle positions whenever an adjustment changes the order.</p>
<h2>Reason about the mode or modes</h2>
<p>A mode is a value occurring most often. For a one-mode target, that value must occur more often than every other value. For two modes, both target values must tie for the highest frequency, with every other value occurring less often. Watch for accidental repetitions as you edit. The order in which <code>MODE.MULT</code> lists two modes does not matter.</p>
<h2>Reason about the mean</h2>
<p>The required total is count × target mean. Changing the total by a small amount changes the mean by that amount divided by the count. If your mean is too low, the total must increase; if it is too high, the total must decrease.</p>
<p>Experiment with values away from the middle positions and required repetitions. Use progressively smaller decimal adjustments while staying between 0 and 1,000. Recheck the count, median, and mode(s) after each adjustment. Your instructor decides whether the mean is close enough; there is no fixed numerical tolerance.</p>
<p>There are many possible datasets. Use these ideas to guide your own guesses and corrections, and be ready to explain how you could narrow the mean error further while preserving the exact requirements.</p>
'''),
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
    ('03-target-mean-median', 'Create data with specified statistical properties', 'Chapter 2',
     'Adjust observations to match varying combinations of mean, median, extremes, and standard deviation.', '''
<h2>What to learn</h2><p>Use a spreadsheet to construct a dataset with specified properties. Enter formulas once, then adjust the observations while watching your summary update. The generated assignment specifies which statistics must match; the others may vary.</p>
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
<h2>How to approach the generated variations</h2><ul>
<li><strong>Mean and median:</strong> aim for a total of count × target mean (with whole numbers, use an attainable integer total within the stated mean tolerance). Sort the values and control the middle observation (or the average of the middle pair). Increasing one maximum raises the mean without changing the median.</li>
<li><strong>Mean and sample standard deviation:</strong> use <code>AVERAGE</code> and <code>STDEV.S</code>. Start with pairs equally far above and below the target mean; for an odd count, add the mean itself. Move pairs farther apart to increase spread, or closer together to decrease it. Decimals are allowed. Adding a constant to every observation shifts the mean and leaves standard deviation unchanged.</li>
<li><strong>Minimum, maximum, and sample standard deviation:</strong> keep one observation at each required endpoint. Start the remaining values near the midpoint, and move interior pairs toward the endpoints to increase spread. Adjust and recheck until the standard deviation is within the stated tolerance.</li>
<li><strong>Median with extremes:</strong> fix both endpoints, then place the middle observation or middle pair at the requested median.</li>
<li><strong>Mean with extremes:</strong> fix both endpoints, subtract their sum from the required total, then distribute the remaining total among the interior observations without exceeding the endpoints.</li>
</ul><p>Use <code>COUNT</code>, <code>AVERAGE</code>, <code>MEDIAN</code>, <code>MIN</code>, <code>MAX</code>, and <code>STDEV.S</code> for the live summary. (Google Sheets supports the same functions.) Exact-match requirements and tolerances appear in the generated task. Keep all underlying precision; number formatting alone does not satisfy a target.</p>
<h2>During your check</h2><p>Meet all the generated requirements at once, using the specified count and allowed values. Demonstrate the listed follow-up change and explain which statistics it preserves. The targets are generated from attainable datasets; many different answers may work.</p>
<h2>Variations to prepare for</h2><ul><li>Use the selector to practice all five target combinations above. Only the listed targets are required for an attempt.</li><li>The count can be 5, 6, 7, 8, or 10. For an even count, the median is the average of the two middle values after sorting. Update all summary ranges.</li><li>Some tasks require whole numbers; the standard-deviation constructions allow decimals. Read the allowed-values row and the follow-up before starting.</li></ul>
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
<h2>Be ready to explain</h2><p>Why the middle region requires subtraction and the upper tail requires a complement. <code>FALSE</code> returns a density hnine, which is not the requested area. For a continuous normal variable, including or excluding a single endpoint does not change the probability.</p>
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


def generator_section(i):
    return f'''<section class="generator" data-check="{i}" aria-labelledby="generator-heading">
<h2 id="generator-heading">Your generated assignment</h2>
<p>Practice from a fresh worksheet. Regenerate for another attempt; at your live check, generate a new version in front of your instructor and keep that version throughout the attempt.</p>
<noscript><p class="callout">Enable JavaScript to generate an assignment. The worked example below remains available without JavaScript.</p></noscript>
<div id="generator-controls"><div class="generator-toolbar">
<label class="field" for="variation">Practice variation<select id="variation"><option value="mixed">Random variation</option></select></label>
<button id="regenerate" class="primary" type="button">Regenerate problem</button></div>
<label class="toggle"><input type="checkbox" id="live-check">Live check view — hide worked examples and practice answers</label></div>
<p id="task-status" role="status" aria-live="polite"></p>
<div id="generated-content">
<p class="task-version">Version <span id="version-code"></span> · <a id="version-link">Reopen this version</a></p>
<h3 id="task-title"></h3><table class="task-table"><caption class="aside">Requirements for this attempt</caption><tbody id="task-facts"></tbody></table>
<ol id="task-steps"></ol>
<div id="task-data-wrap" hidden><h3>Source data</h3><p id="data-help"></p>
<label for="task-data">Data to copy (read only)</label><textarea id="task-data" readonly spellcheck="false"></textarea>
<div class="button-row"><button id="copy-data" type="button">Copy data</button></div></div>
<h3>{"Be ready to explain" if i == 1 else "Follow-up change"}</h3><p id="task-change" class="task-change"></p>
<div class="button-row"><button id="copy-task" type="button">Copy assignment</button><button id="copy-link" type="button">Copy version link</button></div>
<details id="answers"><summary>Practice self-check — open after your attempt</summary><p>These checks help you review your practice. At a live check, demonstrate your spreadsheet formulas and explain your results to the instructor.</p><ul id="task-answers"></ul></details>
</div>
<div id="copy-fallback-wrap" hidden><label for="copy-fallback">Select and copy this text manually</label><textarea id="copy-fallback" readonly rows="6"></textarea></div>
</section>'''

def build_summary_check(body):
    (OUT / '01-match-summary.html').write_text('''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Check 1: Match Count, Mean, Median, and Mode · Statistics</title><link rel="stylesheet" href="../excel-checks.css"><script defer src="generators.js"></script><script defer src="match-summary-page.js"></script></head>
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
<footer><nav aria-label="Other checks" class="links"><a href="../excel-competency-checks.html">All nine checks</a><a href="01-prepare-data.html">Next check</a></nav></footer>
</main></body></html>''')
    (OUT / '01-match-summary-help.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Spreadsheet setup and reasoning · Excel check 1</title><link rel="stylesheet" href="../excel-checks.css"></head>
<body><main><header><p class="eyebrow">Statistics · Excel competency check 1 · Help</p>
<h1>Spreadsheet setup and reasoning</h1><p><a href="01-match-summary.html">Back to the problem</a></p></header>
{body}
<footer><a href="01-match-summary.html">Back to the problem</a></footer></main></body></html>''')


def main():
    OUT.mkdir(exist_ok=True)
    for i, (slug, title, coverage, summary, body) in enumerate(CHECKS, 1):
        if i == 1:
            build_summary_check(body)
            continue
        previous = f'<a href="{CHECKS[i-2][0]}.html">Previous check</a>' if i > 1 else ''
        following = f'<a href="{CHECKS[i][0]}.html">Next check</a>' if i < len(CHECKS) else ''
        (OUT / f'{slug}.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Check {i}: {escape(title)} · Statistics</title><link rel="stylesheet" href="../excel-checks.css"><script defer src="generators.js"></script><script defer src="check-page.js"></script></head>
<body><main><header><p class="eyebrow">Statistics · Excel competency check {i} · {coverage}</p>
<nav aria-label="Breadcrumb"><a href="../../index.html#stats">Teaching</a> / <a href="../excel-competency-checks.html">Excel competency checks</a></nav>
<h1>{escape(title)}</h1><p>{escape(summary)}</p>
<p class="callout">Prepare to build and explain a working spreadsheet face to face in about five minutes after practicing. The generated assignment is your task for this attempt. The expandable directions below teach the workflow; their example numbers are separate from your generated version.</p></header>
{generator_section(i)}
<details class="learning"><summary>Learn the workflow and see a worked example</summary>
{body}</details><footer><nav aria-label="Other checks" class="links">{previous}<a href="../excel-competency-checks.html">All nine checks</a>{following}</nav></footer>
</main></body></html>''')
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
<li>Every check has a <strong>Regenerate problem</strong> button that changes the data, parameters, or requirements within the same skill. Check 1 randomly alternates between one and two modes; the other checks also offer a practice variation selector. Complete one generated task and its listed explanation or follow-up per attempt.</li>
<li>For a live check, open the skill page, regenerate a fresh problem in front of the instructor, and use that version for the entire attempt. On Checks 2–9, Live check view hides practice answers and worked examples. Demonstrate the work in Excel or Sheets; these pages do not submit or grade a workbook.</li>
<li>Copy data directly from the generated task when provided. On Checks 2–9, use <strong>Copy version link</strong> to save or share the exact requirements and data. Refreshing that link keeps the same task; press Regenerate for a new one. Random spreadsheet trial results in Check 7 will still vary on recalculation.</li>
<li>For Check 1, follow the help link for setup and reasoning. For Checks 2–9, expand the worked directions to learn the method. Their fixed example is separate from the generated assignment. After practice, use the self-check to review your results. No practice-answer reveal is needed during the live demonstration.</li>
<li>Use formulas linked to the data and inputs. Be able to show the formulas, fill them across or down, explain fixed versus changing cell references, and explain the result. A page of typed final answers does not demonstrate these skills.</li>
<li>Use clear labels and readable number formats. Keep full precision in calculations. These examples assume English function names and comma argument separators; regional settings may use semicolons.</li>
</ul></section>
<footer><p>Course alignment: sampling and descriptive statistics, probability and expected value, normal models, sampling distributions, and confidence intervals. The random-trial experiment illustrates the law of large numbers.</p>
<details><summary>Spreadsheet help</summary><ul>
<li><a href="https://support.microsoft.com/en-us/excel/split-a-cell-in-excel">Microsoft: splitting text and transposing values</a></li>
<li><a href="https://support.microsoft.com/en-us/excel/statistical-functions-reference">Microsoft: statistical functions</a></li>
<li><a href="https://support.microsoft.com/en-gb/excel/functions/randbetween-function">Microsoft: RANDBETWEEN and recalculation</a></li>
<li><a href="https://support.google.com/docs/answer/6325535?hl=en">Google Sheets: splitting text into columns</a></li>
<li><a href="https://support.google.com/docs/table/25273?hl=en">Google Sheets: function reference</a></li>
</ul></details></footer></main></body></html>''')
    print('Built competency-check index and nine student direction pages.')


if __name__ == '__main__':
    main()

