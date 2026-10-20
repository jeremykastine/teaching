/* Pure, seeded assignment generators. Keep v1 stable so saved links remain reproducible. */
(function (root) {
  'use strict';
  const VERSION = 1;
  const variants = {
    1: [['one-mode','One mode'],['two-modes','Two modes']],
    2: [['comma','Comma-separated whole numbers'],['semicolon','Semicolon-separated decimals'],['signed','Signed decimal values']],
    3: [['counts','Frequency chart'],['relative','Relative-frequency chart'],['four','Four categories']],
    4: [['mean-median','Mean and median'],['mean-sd','Mean and standard deviation'],['extremes-sd','Minimum, maximum, and standard deviation'],['median-extremes','Median, minimum, and maximum'],['mean-extremes','Mean, minimum, and maximum']],
    5: [['sample','Sample standard deviation'],['shift','Shift every observation'],['population','Population standard deviation']],
    6: [['forward','Condition on the row'],['reverse','Condition on the column'],['complement','Conditional complement']],
    7: [['die-mean','Mean of a fair die'],['die-event','Proportion of a die outcome'],['binary','Success proportion']],
    8: [['spread','Change the standard deviation'],['shift','Change the mean'],['cutoff','Move a cutoff']],
    9: [['confidence','Change the confidence level'],['mean','Shift the sample mean'],['size','Halve the margin of error']]
  };
  const round = (x, places=4) => Number(x.toFixed(places));
  const sum = a => a.reduce((s,x)=>s+x,0);
  const mean = a => sum(a)/a.length;
  const sd = (a,pop=false) => Math.sqrt(sum(a.map(x=>(x-mean(a))**2))/(a.length-(pop?0:1)));
  const median = a => { const b=[...a].sort((x,y)=>x-y), m=Math.floor(b.length/2); return b.length%2?b[m]:(b[m-1]+b[m])/2; };
  // Standard normal CDF approximation, absolute error below 8e-8.
  function normalCDF(z) {
    const x=Math.abs(z), t=1/(1+0.2316419*x);
    const tail=Math.exp(-x*x/2)/Math.sqrt(2*Math.PI)*t*(0.319381530+t*(-0.356563782+t*(1.781477937+t*(-1.821255978+t*1.330274429))));
    return z>=0?1-tail:tail;
  }
  function rng(seed) { let a=seed>>>0; return () => { a+=0x6D2B79F5; let t=a; t=Math.imul(t^(t>>>15),t|1); t^=t+Math.imul(t^(t>>>7),t|61); return ((t^(t>>>14))>>>0)/4294967296; }; }
  function generate(check, seed, requested='mixed') {
    if (!variants[check]) throw new Error('Unknown check');
    const r=rng(seed), int=(a,b)=>Math.floor(r()*(b-a+1))+a, pick=a=>a[int(0,a.length-1)];
    const shuffle=a=>{a=[...a]; for(let i=a.length-1;i>0;i--){let j=int(0,i);[a[i],a[j]]=[a[j],a[i]];} return a;};
    const variant=requested==='mixed'?pick(variants[check])[0]:requested;
    if (!variants[check].some(v=>v[0]===variant)) throw new Error('Unknown variation');
    const task={check,seed:seed>>>0,variant,title:variants[check].find(v=>v[0]===variant)[1],facts:[],steps:[],change:'',data:'',dataHelp:'',answers:[],meta:{}};
    const t=task;
    if(check===1) {
      const n=int(50,100), modeCount=variant==='two-modes'?2:1, frequency=int(5,8);
      const modes=shuffle(Array.from({length:81},(_,i)=>i+10)).slice(0,modeCount);
      const remaining=n-modeCount*frequency, lowCount=Math.round(remaining*0.65);
      let witness=[...modes.flatMap(x=>Array(frequency).fill(x)),
        ...shuffle(Array.from({length:181},(_,i)=>i+180)).slice(0,lowCount),
        ...shuffle(Array.from({length:201},(_,i)=>i+800)).slice(0,remaining-lowCount)];
      // Make the target mean an exact integer, without introducing another repeated value.
      const remainder=sum(witness)%n;
      if(remainder) {
        let adjusted=false;
        for(let i=modeCount*frequency;i<n&&!adjusted;i++) {
          for(const delta of [-remainder,n-remainder]) {
            const value=witness[i]+delta;
            if(value>=0&&value<=1000&&!witness.includes(value)) {witness[i]=value;adjusted=true;break;}
          }
        }
        if(!adjusted)throw new Error('Could not construct an exact mean');
      }
      // Mirror half the tasks to provide both low-mode and high-mode challenges.
      if(int(0,1))witness=witness.map(x=>1000-x);
      const counts=new Map();for(const x of witness)counts.set(x,(counts.get(x)||0)+1);
      const targetModes=[...counts].filter(([,c])=>c===frequency).map(([x])=>x).sort((a,b)=>a-b);
      const targets={count:n,mean:mean(witness),median:median(witness),modes:targetModes};
      t.title='Construct data to match count, mean, median, and mode(s)';
      t.facts=[['Count (exact)',n],['Mean (approximate match)',targets.mean],['Median (exact)',targets.median],
        [modeCount===1?'Mode (exact)':'Modes (both exact)',targetModes.join(', ')],['Allowed values','0–1,000 inclusive; decimals allowed']];
      t.steps=[`Open a new, blank Excel workbook. Enter exactly ${n} numbers of your own in column A, one number per cell, all between 0 and 1,000. The generator supplies targets only; its original numbers are hidden.`,
        'In a separate labeled summary area, use COUNT, AVERAGE, MEDIAN, and MODE.MULT formulas referencing column A. Keep the cells below MODE.MULT empty so a second mode can spill into the next row.',
        `Adjust your observations until count and median match exactly and MODE.MULT returns exactly ${modeCount===1?'the one listed mode':'the two listed modes'} in either order, with no additional modes. For two modes, both must occur equally often and more often than every other number.`,
        'Bring the mean as close as possible to its target; your instructor decides whether it is close enough. Display enough decimals to judge the actual difference. Keep count, median, and all modes exact while refining the mean. Do not replace formulas with typed answers.'];
      t.change='Explain how you could make the mean error arbitrarily small by adjusting decimal values while preserving the count, median, and mode(s). No second target is required.';
      t.answers=['Use your spreadsheet formulas to compare all four summaries with the targets. MODE.MULT must return all and only the listed modes; their order does not matter.',
        'The target mean is exact as displayed. Acceptance of an approximate mean is up to your instructor; rounding the display does not change the underlying result. Many datasets work. The hidden original dataset is not revealed.'];
      t.meta={witness,targets,frequency};
    }
    if(check===2) {
      const n=int(10,20), signed=variant==='signed', decimal=variant!=='comma';
      const data=Array.from({length:n},()=>decimal?int(signed?-150:10,250)/10:int(3,65));
      const delimiter=variant==='semicolon'?';':',', ascending=!!int(0,1), start=pick([6,7,8]);
      const old=Math.max(...data), value=round(old+int(5,15),1), changed=[...data]; changed[changed.indexOf(old)]=value;
      t.facts=[['Observations',n],['Delimiter',delimiter===','?'Comma (,)':'Semicolon (;)'],['Destination',`A${start}:A${start+n-1}`],['Sort order',ascending?'Smallest to largest':'Largest to smallest']];
      t.data=data.join(delimiter); t.dataHelp='Copy the line into A1 while editing that cell (double-click A1 first) so it stays in one cell. Keep this original text. Split a copy in A3, then transpose to the destination as editable numeric values.';
      t.steps=[`Split and transpose all ${n} observations, then sort in the requested order. Leave enough empty cells to the right for the split.`, 'Build labeled COUNT and AVERAGE formulas linked to the editable column. Show that all entries are numbers.'];
      t.change=`Replace one occurrence of the largest original value (${old}) with ${value}. Re-sort if needed and show the mean updating without changing the count.`;
      t.answers=[`Original count ${n}; mean ${round(mean(data))}.`,`After the correction: count ${n}; mean ${round(mean(changed))}.`]; t.meta={data,changed};
    }
    if(check===3) {
      const labels=pick([['Bus','Car','Walk','Bike'],['Blue','Green','Orange','Purple'],['Online','Print','Audio','Video']]).slice(0,variant==='four'?4:3);
      const counts=labels.map(()=>int(2,7)), data=shuffle(labels.flatMap((x,i)=>Array(counts[i]).fill(x)));
      const from=int(0,labels.length-1), to=(from+int(1,labels.length-1))%labels.length;
      t.facts=[['Observations',data.length],['Categories',labels.join(', ')],['Chart measure',variant==='relative'?'Relative frequency':'Frequency']];
      t.data=['Response',...data].join('\n');t.dataHelp='Paste in A1. The first line is a header; the remaining lines are observations.';
      t.steps=['Use COUNTIF with a fixed raw-data range and a changing category reference. Include every listed category.', 'Calculate frequency totals and relative frequencies with formulas; verify the count and 100% total.',`Create a labeled bar or column chart of ${variant==='relative'?'relative frequencies':'frequencies'} linked to the summary. Exclude the total row.`];
      t.change=`Change one ${labels[from]} response to ${labels[to]}. Show both affected rows and the chart updating.`;
      t.answers=labels.map((x,i)=>`${x}: ${counts[i]} (${round(100*counts[i]/data.length,2)}%).`);
      t.answers.push(`Total ${data.length}. The change subtracts 1 from ${labels[from]} and adds 1 to ${labels[to]}; the total stays fixed.`); t.meta={labels,counts,data};
    }
    if(check===4) {
      const n=pick([5,6,7,8,10]), c=int(12,35), d=int(4,10);
      let witness, follow;
      if(variant==='extremes-sd') {
        const build=a=>{const b=[c-d,c+d];while(b.length+1<n)b.push(c-a,c+a);if(b.length<n)b.push(c);return b.sort((a,b)=>a-b);};
        witness=build(d/4);follow=build(3*d/4);
      } else if(variant==='mean-sd') {
        const build=()=>{const b=[];for(let i=0;i<Math.floor(n/2);i++){const a=int(1,d);b.push(c-a,c+a);}if(n%2)b.push(c);return b.sort((a,b)=>a-b);};
        witness=build();follow=witness.map(x=>x+2);
      } else {
        witness=Array.from({length:n},()=>int(c-d,c+d)).sort((a,b)=>a-b);
        // Fix distinct endpoints so the construction and follow-up never degenerate.
        witness[0]=c-d;witness[n-1]=c+d;
        if(variant==='mean-median') {follow=[...witness];follow[n-1]+=n;}
        else {follow=witness.map(x=>x+2);}
      }
      const stats=a=>({mean:round(mean(a),2),median:median(a),min:Math.min(...a),max:Math.max(...a),sd:round(sd(a),2)});
      const targets=stats(witness), next=stats(follow);
      const keys={'mean-median':['mean','median'],'mean-sd':['mean','sd'],'extremes-sd':['min','max','sd'],'median-extremes':['median','min','max'],'mean-extremes':['mean','min','max']}[variant];
      const names={mean:'Mean',median:'Median',min:'Minimum',max:'Maximum',sd:'Sample standard deviation'};
      t.facts=[['Number of observations',n],['Allowed values',variant.includes('sd')?'Nonnegative numbers; decimals allowed':'Nonnegative whole numbers'],...keys.map(k=>[names[k],targets[k]])];
      t.steps=[`Enter exactly ${n} observations of your own. Build a live summary with COUNT, AVERAGE, MEDIAN, MIN, MAX, and STDEV.S. Use the actual observations in every formula.`, 'Adjust observations until every listed target is satisfied at once. Unlisted statistics are free to vary. Keep the count fixed.', 'For mean or standard-deviation targets, the underlying result must be within 0.05 of the displayed target. Median, minimum, and maximum must match exactly. Display enough decimal places to check this.'];
      if(variant==='mean-median')t.change=`Change only one observation to increase the mean by 1 while keeping the median fixed. Target mean: ${round(targets.mean+1,2)} (within 0.05).`;
      else if(variant==='mean-sd')t.change=`Increase the mean by 2 to ${next.mean} while preserving the sample standard deviation target. Explain how adding the same constant to all observations helps.`;
      else if(variant==='extremes-sd')t.change=`Keep the same minimum and maximum, but adjust interior values to make the sample standard deviation ${next.sd} (within 0.05).`;
      else t.change=`Add 2 to every observation. Verify that each listed target except count increases by 2. Explain what happens to the standard deviation.`;
      t.answers=[`One possible initial dataset: ${witness.join(', ')}.`,`One possible dataset after the change: ${follow.join(', ')}.`,`Initial mean ${round(mean(witness))}, median ${median(witness)}, sample standard deviation ${round(sd(witness))}. Other valid datasets are welcome.`];
      t.meta={witness,follow,targets,next,keys,n};
    }
    if(check===5) {
      const n=int(5,9), pop=variant==='population', data=Array.from({length:n},()=>int(-5,25));data[n-1]=data[0]+int(2,7);
      const delta=int(3,9), changed=variant==='shift'?data.map(x=>x+delta):data.map((x,i)=>i===n-1?x+delta*2:x);
      t.facts=[['Observations',n],['Treat the data as',pop?'The entire population':'A sample'],['Built-in verification',pop?'STDEV.P':'STDEV.S']];
      t.data=['Observation',...data].join('\n');t.dataHelp='Paste in A1. The header is not part of the numeric range.';
      t.steps=['Compute the mean and count with formulas. Fill down deviations from a fixed mean cell and their squares.',`Sum the squared deviations, divide by ${pop?'n (population size)':'n − 1 (sample size)'}, and take the square root. Keep full precision.`,`Compare with ${pop?'STDEV.P':'STDEV.S'} using the same range and calculate the absolute difference.`];
      t.change=variant==='shift'?`Add ${delta} to every observation. Show both methods updating and explain why standard deviation stays the same.`:`Increase the last observation (${data[n-1]}) by ${delta*2}. Show all deviations and both methods updating.`;
      t.answers=[`Initial mean ${round(mean(data))}; squared-deviation sum ${round(sum(data.map(x=>(x-mean(data))**2)))}; variance ${round(sd(data,pop)**2)}; standard deviation ${round(sd(data,pop))}.`,`After the change: mean ${round(mean(changed))}; standard deviation ${round(sd(changed,pop))}. The two methods should agree to computer precision.`];t.meta={data,changed,pop};
    }
    if(check===6) {
      const rows=pick([['Morning','Afternoon'],['Site 1','Site 2'],['Group X','Group Y']]), cols=pick([['A','B'],['Yes','No'],['Print','Digital']]);
      const counts=Array.from({length:2},()=>[int(1,5),int(1,5)]), data=shuffle(rows.flatMap((row,i)=>cols.flatMap((col,j)=>Array.from({length:counts[i][j]},()=>[row,col]))));
      const i=int(0,1), j=int(0,1), grand=data.length, rt=sum(counts[i]),ct=counts[0][j]+counts[1][j], joint=counts[i][j];
      const conditional=variant==='reverse'?`P(${rows[i]} given ${cols[j]})`:variant==='complement'?`P(${cols[1-j]} given ${rows[i]})`:`P(${cols[j]} given ${rows[i]})`;
      const num=variant==='complement'?counts[i][1-j]:joint,den=variant==='reverse'?ct:rt;
      t.facts=[['Records',grand],['Row labels',rows.join(', ')],['Column labels',cols.join(', ')],['Requested probabilities',`P(${cols[j]}); P(${rows[i]} and ${cols[j]}); ${conditional}`]];
      t.data=['Group\tChoice',...data.map(x=>x.join('\t'))].join('\n');t.dataHelp='Paste in A1 to fill two columns. Keep both fields of each record together when sorting.';
      t.steps=['Use COUNTIFS to create the 2 × 2 table from the records. Use mixed references so the formula fills across and down.', 'Add row totals, column totals, and a grand total. Calculate all three requested probabilities from the table using formulas. Explain each denominator.'];
      t.change=`Change one record (${rows[i]}, ${cols[j]}) to (${rows[i]}, ${cols[1-j]}). Recalculate the table and probabilities without retyping the answers.`;
      const changed=counts.map(a=>[...a]);changed[i][j]--;changed[i][1-j]++;
      const ct2=changed[0][j]+changed[1][j],num2=variant==='complement'?changed[i][1-j]:changed[i][j],den2=variant==='reverse'?ct2:rt;
      t.answers=[`Table rows (${cols.join(', ')}): ${rows[0]} = ${counts[0].join(', ')}; ${rows[1]} = ${counts[1].join(', ')}. Total ${grand}.`,`Initially: overall ${ct}/${grand}; joint ${joint}/${grand}; conditional ${num}/${den}.`,`After the change: overall ${ct2}/${grand}; joint ${joint-1}/${grand}; conditional ${den2?`${num2}/${den2}`:'undefined (the conditioning category has no records)'}.`];t.meta={data,counts,rows,cols,i,j};
    }
    if(check===7) {
      const k=pick([4,6,8,10]), face=int(1,k), p=pick([0.2,0.3,0.4,0.6,0.7,0.8]);
      const binary=variant==='binary', event=variant==='die-event', expected=binary?p:event?1/k:(1+k)/2;
      const formula=binary?`=IF(RAND()<${p},1,0)`:`=RANDBETWEEN(1,${k})`;
      t.facts=[['Experiment',binary?`Independent successes with probability ${p}`:`Fair die numbered 1 through ${k}`],['Statistic',event?`Proportion of rolls equal to ${face}`:binary?'Proportion of successes (mean of 0/1 values)':'Mean roll'],['Sample sizes','10, 100, 1,000 (nested)'],['Live generator formula',formula]];
      t.steps=[`Create 1,000 live random observations in A2:A1001 using ${formula}. Here 1 means success and 0 means failure for a binary experiment.`, `Use formulas to compare the first 10, first 100, and all 1,000 trials. ${event?`Use COUNTIF(range,${face})/COUNT(range).`:'Use AVERAGE for each range.'} Compute the theoretical expected value and absolute errors.`, 'Recalculate several times and explain the pattern across runs. Errors do not have to decrease at every sample size. Correct setup and interpretation determine success.'];
      t.change='Freeze one complete experiment by copying all 1,000 observations and pasting values into a separate column. Compute its three summaries from that column; show they stay fixed when the live experiment recalculates.';
      t.answers=[`Theoretical expected value: ${round(expected,6)}${event?` (1/${k})`:''}. For an observed sample, absolute error = ABS(observed statistic − expected value).`,'Observed results vary. Larger samples generally produce more stable statistics over repeated runs; no run is required to improve monotonically.'];t.meta={k,face,p,expected};
    }
    if(check===8) {
      const m=int(8,30)*5,s=pick([4,5,8,10,12,15]),lo=m-pick([0.5,1,1.5,2])*s,hi=m+pick([0.5,1,1.5,2])*s;
      const field=variant==='spread'?'Standard deviation':variant==='shift'?'Mean':'Upper cutoff', value=variant==='spread'?2*s:variant==='shift'?m+s:hi+s;
      const count=pick([100,200,500]), outside=!!int(0,1);
      t.facts=[['Model','Normal distribution'],['Mean',m],['Standard deviation',s],['Lower cutoff',lo],['Upper cutoff',hi],['Additional output',outside?'Probability outside the interval':`Expected number inside among ${count} observations`]];
      t.steps=['Put model parameters and both cutoffs in separate labeled input cells. Link all calculations to those inputs.', 'Use cumulative NORM.DIST with TRUE to calculate probabilities below the lower cutoff, between the cutoffs, and above the upper cutoff. Verify they sum to 1. (Sheets: NORMDIST.)', 'Calculate the additional output, and display probabilities as percentages without rounding intermediate formulas.'];
      t.change=`Change only ${field.toLowerCase()} to ${value}. Leave other inputs fixed. Show all outputs updating and interpret the changes.`;
      const probabilities=(mu,sigma,upper)=>{const below=normalCDF((lo-mu)/sigma), above=1-normalCDF((upper-mu)/sigma);return [below,1-below-above,above];};
      const initial=probabilities(m,s,hi), changed=probabilities(variant==='shift'?value:m,variant==='spread'?value:s,variant==='cutoff'?value:hi);
      const describe=(label,a)=>`${label}: below ${round(a[0]*100,2)}%; between ${round(a[1]*100,2)}%; above ${round(a[2]*100,2)}%. ${outside?`Outside ${round((a[0]+a[2])*100,2)}%.`:`Expected number inside ${round(a[1]*count,2)}.`}`;
      t.answers=[describe('Initially',initial),describe('After the change',changed),'Values are approximate. Outside probability is the sum of the tails. Expected count is observation count × middle probability. The three regions must always sum to 1.'];t.meta={m,s,lo,hi,field,value,initial,changed,count,outside};
    }
    if(check===9) {
      const m=int(10,40)*2,s=pick([6,8,10,12,15]),base=pick([16,25,36,49]),ns=[base,4*base,16*base];
      const levels=[['90%',1.645],['95%',1.96],['99%',2.576]],idx=int(0,2),level=levels[idx],other=levels[(idx+1)%3],delta=int(3,8);
      t.facts=[['Assumption','Independent random observations from a normal population; population standard deviation is known'],['Sample mean',m],['Known population standard deviation',s],['Confidence level',level[0]],['Supplied z critical value',level[1]],['Sample sizes',ns.join(', ')]];
      t.steps=['Store the shared inputs in labeled cells. Treat the three sample sizes as hypothetical comparisons with the same mean and known population standard deviation.', 'Build a three-row table with standard error, margin of error, lower endpoint, upper endpoint, and interval width. Fill formulas down using fixed references for shared inputs.', 'Use standard error = sigma/SQRT(n), margin = z × standard error, endpoints = mean ± margin, and width = 2 × margin.'];
      t.change=variant==='confidence'?`Change to ${other[0]} confidence using the supplied critical value ${other[1]}. Show the widths changing while standard errors stay fixed.`:variant==='mean'?`Increase only the sample mean by ${delta}. Explain why both endpoints shift by ${delta} while all widths stay the same.`:`For the smallest sample size (${base}), add a row with a size that halves its margin of error, holding other inputs fixed. Verify with formulas.`;
      t.answers=ns.map(n=>{const se=s/Math.sqrt(n),e=level[1]*se;return `n = ${n}: SE ${round(se)}; margin ${round(e)}; interval [${round(m-e)}, ${round(m+e)}]; width ${round(2*e)}.`;});
      if(variant==='size')t.answers.push(`The required size is ${4*base}, four times the original size. This matches the second comparison row.`);
      t.meta={m,s,ns,level,other,delta};
    }
    return t;
  }
  const api={VERSION,variants,generate,mean,sd,median};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;
  else root.ExcelCheckGenerators=api;
})(typeof globalThis!=='undefined'?globalThis:this);

