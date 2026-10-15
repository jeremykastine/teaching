'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {generate,VERSION}=require('../question-banks/test-generator.js');
let tests=0;
for(let unit=1;unit<=4;unit++) {
  const bank=JSON.parse(fs.readFileSync(path.join(__dirname,`../question-banks/unit-${unit}-question-bank.json`),'utf8'));
  const original=JSON.stringify(bank),seen=new Set(),firstPositions=new Set(),answerOrders=new Set();
  assert.equal(bank.questions.length,100);assert.equal(bank.groups.length,10);
  const byId=new Map(bank.questions.map(q=>[q.id,q]));
  for(const group of bank.groups)assert.equal(bank.questions.filter(q=>q.group===group.id).length,10);
  for(let seed=0;seed<10000;seed++) {
    const selected=generate(bank,seed);
    assert.equal(selected.length,10);assert.equal(new Set(selected.map(q=>q.id)).size,10);
    assert.deepEqual([...selected.map(q=>q.group)].sort(),bank.groups.map(g=>g.id).sort());
    if(seed<50)assert.deepEqual(selected,generate(bank,seed),'version seed must reproduce questions and answer order');
    firstPositions.add(selected[0].group);
    for(const q of selected) {
      const source=byId.get(q.id);assert.ok(source);
      assert.equal(q.stem,source.stem);assert.equal(q.explanation,source.explanation);
      assert.deepEqual([...q.choices].sort(),[...source.choices].sort());
      assert.equal(q.choices[q.answer_index],source.choices[source.answer_index],'shuffled key must identify original correct text');
      seen.add(q.id);answerOrders.add(q.choices.join('|'));
    }
    tests++;
  }
  assert.equal(JSON.stringify(bank),original,'generator must not mutate bank sources');
  assert.equal(seen.size,100,'all questions must be reachable');
  assert.equal(firstPositions.size,10,'every topic pool can appear first');
  assert.ok(answerOrders.size>100,'answer-choice order should vary');
}
assert.equal(VERSION,1);
assert.throws(()=>generate({groups:[],questions:[]},0));
console.log(`Validated ${tests.toLocaleString()} generated tests: ten distinct questions, one per pool, correct keys after shuffling, and reproducible versions.`);
