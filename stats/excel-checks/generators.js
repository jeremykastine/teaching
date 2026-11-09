/* Pure, seeded assignment generators. Keep v1 stable so saved links remain reproducible. */
(function (root) {
  'use strict';
  const VERSION = 1;
  const variants = {
    1: [['one-mode','One mode'],['two-modes','Two modes']],
    2: [['comma','Comma-separated whole numbers'],['semicolon','Semicolon-separated decimals'],['signed','Signed decimal values']],
    3: [['counts','Frequency chart'],['relative','Relative-frequency chart'],['four','Four categories']]
  };
  const round = (x, places=4) => Number(x.toFixed(places));
  const sum = a => a.reduce((s,x)=>s+x,0);
  const mean = a => sum(a)/a.length;
  const sd = (a,pop=false) => Math.sqrt(sum(a.map(x=>(x-mean(a))**2))/(a.length-(pop?0:1)));
  const median = a => { const b=[...a].sort((x,y)=>x-y), m=Math.floor(b.length/2); return b.length%2?b[m]:(b[m-1]+b[m])/2; };
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
      const n=int(20,30), modeCount=variant==='two-modes'?2:1, frequency=int(5,8);
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
    return t;
  }
  const api={VERSION,variants,generate,mean,sd,median};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;
  else root.ExcelCheckGenerators=api;
})(typeof globalThis!=='undefined'?globalThis:this);

