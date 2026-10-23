'use strict';
const assert = require('node:assert/strict');
const { generate, measures, shapes } = require('../excel-checks/match-spread-generator.js');
const combinations = new Map();
const near = (actual, expected, tolerance = 1e-8) =>
  assert.ok(Math.abs(actual - expected) <= tolerance, `${actual} differs from ${expected}`);
const total = 16000;
for (let seed = 0; seed < total; seed++) {
  const task = generate(seed);
  assert.deepEqual(task, generate(seed), 'a seed must reproduce its targets');
  const { witness: data, targets, shape, measure } = task;
  assert.equal(data.length, 10);
  assert.equal(targets.count, 10);
  assert.ok(data.every(x => Number.isFinite(x) && x >= 0 && x <= 1000));
  const lo = Math.min(...data), hi = Math.max(...data);
  const mean = data.reduce((s, x) => s + x, 0) / data.length;
  // Pairwise identity independently checks the requested deviations-based calculation.
  let pairwise = 0;
  for (let i = 0; i < data.length; i++) {
    for (let j = i + 1; j < data.length; j++) pairwise += (data[i] - data[j]) ** 2;
  }
  const sumSquares = pairwise / data.length;
  const variance = sumSquares / (measure.population ? 10 : 9);
  near(targets.mean, mean);
  assert.equal(targets.range, hi - lo);
  near(targets.spread, measure.squareRoot ? Math.sqrt(variance) : variance, 0.00005001);
  assert.ok(targets.spread > 0);
  // Check the actual geometry, not just the generator's shape label.
  const normalized = data.map(x => (x - lo) / (hi - lo));
  const centerCount = normalized.filter(x => x >= 0.39 && x <= 0.61).length;
  const moment3 = data.reduce((s, x) => s + (x - mean) ** 3, 0) / 10;
  const skew = moment3 / (sumSquares / 10) ** 1.5;
  if (shape === 'bell') { assert.equal(centerCount, 6); near(skew, 0); }
  if (shape === 'anti-bell') {
    assert.ok(normalized.every(x => x <= 0.161 || x >= 0.839));
    near(skew, 0);
  }
  if (shape === 'right-skewed') assert.ok(skew > 1 && normalized.filter(x => x <= 0.36).length === 8);
  if (shape === 'left-skewed') assert.ok(skew < -1 && normalized.filter(x => x >= 0.64).length === 8);
  const key = `${shape}/${measure.id}`;
  combinations.set(key, (combinations.get(key) || 0) + 1);
}
assert.equal(combinations.size, 16);
for (const shape of shapes) {
  for (const measure of measures) {
    const count = combinations.get(`${shape}/${measure.id}`);
    assert.ok(count > 850 && count < 1150, `unbalanced combination ${shape}/${measure.id}: ${count}`);
  }
}
console.log(`Validated ${total.toLocaleString()} Check 2 tasks: feasible targets, four shapes, four spread measures, and balanced independent choices.`);
