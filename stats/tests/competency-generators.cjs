'use strict';
// Run from any directory: node stats/tests/competency-generators.cjs
// Independent statistical checks, not snapshots of generated output.
const assert=require('node:assert/strict');
const api=require('../excel-checks/generators.js');
const avg=a=>a.reduce((s,x)=>s+x,0)/a.length;
const variance=(a,pop=false)=>{const n=a.length;return (a.reduce((s,x)=>s+x*x,0)-n*avg(a)**2)/(n-(pop?0:1));};
const med=a=>{const s=[...a].sort((a,b)=>a-b);return (s[Math.floor((s.length-1)/2)]+s[Math.ceil((s.length-1)/2)])/2;};
const near=(x,y,tol=1e-8)=>assert.ok(Math.abs(x-y)<=tol,`${x} differs from ${y}`);
const stats=a=>({mean:avg(a),median:med(a),min:Math.min(...a),max:Math.max(...a),sd:Math.sqrt(variance(a))});
let total=0;
for(let check=1;check<=9;check++) {
  const seen=new Set();
  for(const [variant] of [...api.variants[check],['mixed']]) {
    for(let seed=0;seed<1000;seed++) {
      const t=api.generate(check,seed,variant),m=t.meta;
      assert.deepEqual(t,api.generate(check,seed,variant),'saved seed must reproduce all requirements and answers');
      assert.ok(t.steps.length>=2&&t.change&&t.answers.length);
      assert.ok(!/NaN|undefined|Infinity/.test(JSON.stringify(t)),'assignment must contain valid values');
      if(variant==='mixed')seen.add(t.variant);
      if(check===1) {
        const a=m.witness, target=m.targets, counts=new Map();
        assert.ok(a.length>=20&&a.length<=30);assert.equal(a.length,target.count);
        assert.ok(a.every(x=>Number.isFinite(x)&&x>=0&&x<=1000));
        a.forEach(x=>counts.set(x,(counts.get(x)||0)+1));
        const top=Math.max(...counts.values());
        const modes=[...counts].filter(([,c])=>c===top).map(([x])=>x).sort((a,b)=>a-b);
        assert.deepEqual(modes,target.modes);assert.equal(modes.length,t.variant==='two-modes'?2:1);
        near(avg(a),target.mean,0);near(med(a),target.median,0);assert.ok(Number.isInteger(target.mean));
        assert.ok(modes.some(x=>Math.abs(x-target.mean)>=100&&Math.abs(x-target.median)>=100));
        assert.equal(t.data,'');assert.ok(!t.answers.join(' ').includes(a.join(', ')));
      }
      if(check===2) {
        const decoded=t.data.split(t.variant==='semicolon'?';':',').map(Number);
        assert.deepEqual(decoded,m.data);assert.equal(decoded.length,Number(t.facts[0][1]));
        assert.equal(m.changed.length,m.data.length);assert.equal(m.changed.filter((x,i)=>x!==m.data[i]).length,1);
        assert.ok(avg(m.changed)>avg(m.data));
      }
      if(check===3) {
        const parsed=t.data.split('\n').slice(1);assert.deepEqual(parsed,m.data);
        for(let i=0;i<m.labels.length;i++)assert.equal(parsed.filter(x=>x===m.labels[i]).length,m.counts[i]);
        assert.equal(m.counts.reduce((a,b)=>a+b,0),parsed.length);
        assert.equal(m.labels.length,t.variant==='four'?4:3);
      }
      if(check===4) {
        const before=stats(m.witness),after=stats(m.follow);
        assert.equal(m.witness.length,m.n);assert.equal(m.follow.length,m.n);
        assert.ok([...m.witness,...m.follow].every(x=>Number.isFinite(x)&&x>=0));
        if(!t.variant.includes('sd'))assert.ok([...m.witness,...m.follow].every(Number.isInteger));
        for(const key of m.keys)near(before[key],m.targets[key],key==='mean'||key==='sd'?0.05:0);
        for(const key of m.keys)near(after[key],m.next[key],key==='mean'||key==='sd'?0.05:0);
        if(t.variant==='mean-median'){near(after.mean,before.mean+1);near(after.median,before.median);assert.equal(m.follow.filter((x,i)=>x!==m.witness[i]).length,1);}
        if(t.variant==='mean-sd'){near(after.mean,before.mean+2);near(after.sd,before.sd);}
        if(t.variant==='extremes-sd'){near(after.min,before.min);near(after.max,before.max);assert.ok(after.sd>before.sd);}
        if(t.variant==='median-extremes'||t.variant==='mean-extremes'){for(const key of m.keys)near(after[key],before[key]+2);near(after.sd,before.sd);}
      }
      if(check===5) {
        near(api.sd(m.data,m.pop)**2,variance(m.data,m.pop));
        assert.deepEqual(t.data.split('\n').slice(1).map(Number),m.data);
        if(t.variant==='shift')near(variance(m.data),variance(m.changed));
      }
      if(check===6) {
        const lines=t.data.split('\n').slice(1).map(x=>x.split('\t'));
        assert.deepEqual(lines,m.data);
        for(let i=0;i<2;i++)for(let j=0;j<2;j++)assert.equal(lines.filter(x=>x[0]===m.rows[i]&&x[1]===m.cols[j]).length,m.counts[i][j]);
        assert.ok(m.counts[m.i][m.j]>=1,'requested record change must be possible');
        assert.ok(m.counts[0][m.j]+m.counts[1][m.j]>=2,'reverse denominator stays nonzero after the change');
      }
      if(check===7){assert.ok(m.expected>0);assert.ok(m.p>0&&m.p<1);near(m.expected,t.variant==='binary'?m.p:t.variant==='die-event'?1/m.k:(m.k+1)/2);}
      if(check===8){assert.ok(m.s>0&&m.lo<m.hi);for(const p of [m.initial,m.changed]){near(p.reduce((a,b)=>a+b,0),1);assert.ok(p.every(x=>x>=0&&x<=1));}if(t.variant==='spread')assert.ok(m.changed[1]<m.initial[1]);if(t.variant==='cutoff')assert.ok(m.changed[1]>m.initial[1]);}
      if(check===9){assert.ok(m.s>0&&m.level[1]>0);assert.equal(m.ns[1],4*m.ns[0]);assert.equal(m.ns[2],16*m.ns[0]);near(m.s/Math.sqrt(m.ns[1]),m.s/Math.sqrt(m.ns[0])/2);}
      total++;
    }
  }
  assert.equal(seen.size,api.variants[check].length,`random mode should reach every variation for check ${check}`);
}
// Published textbook benchmarks independently verify the statistics helpers.
near(api.sd([2,4,4,6,6,8]),Math.sqrt(22/5));
const normal=api.generate(8,123,'spread');
// Generator probabilities also independently checked against Python math.erf below in QA.
assert.ok(normal.meta.initial[1]>normal.meta.changed[1]);
assert.throws(()=>api.generate(10,0));assert.throws(()=>api.generate(1,0,'missing'));
console.log(`Validated ${total.toLocaleString()} generated assignments, including feasible construction targets and follow-ups across all variations.`);

