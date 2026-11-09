'use strict';
// Run from any directory: node stats/tests/competency-generators.cjs
// Independent statistical checks, not snapshots of generated output.
const assert=require('node:assert/strict');
const api=require('../excel-checks/generators.js');
const avg=a=>a.reduce((s,x)=>s+x,0)/a.length;
const med=a=>{const s=[...a].sort((a,b)=>a-b);return (s[Math.floor((s.length-1)/2)]+s[Math.ceil((s.length-1)/2)])/2;};
const near=(x,y,tol=1e-8)=>assert.ok(Math.abs(x-y)<=tol,`${x} differs from ${y}`);
let total=0;
for(let check=1;check<=3;check++) {
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
      total++;
    }
  }
  assert.equal(seen.size,api.variants[check].length,`random mode should reach every variation for check ${check}`);
}
assert.throws(()=>api.generate(4,0));assert.throws(()=>api.generate(1,0,'missing'));
console.log(`Validated ${total.toLocaleString()} generated assignments, including feasible construction targets and follow-ups across all variations.`);

