/* Check 2 has its own generator so the older checks' saved v1 tasks stay stable. */
(function (root) {
  'use strict';
  const measures = [
    { id: 'population-sd', label: 'population standard deviation', population: true, squareRoot: true },
    { id: 'population-variance', label: 'population variance', population: true, squareRoot: false },
    { id: 'sample-sd', label: 'sample standard deviation', population: false, squareRoot: true },
    { id: 'sample-variance', label: 'sample variance', population: false, squareRoot: false }
  ];
  const shapes = ['bell', 'anti-bell', 'right-skewed', 'left-skewed'];
  function rng(seed) {
    let a = seed >>> 0;
    return () => {
      a += 0x6D2B79F5;
      let t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function generate(seed) {
    const random = rng(seed);
    const int = (low, high) => low + Math.floor(random() * (high - low + 1));
    // Two independent uniform four-way choices: each combination has probability 1/16.
    const measure = measures[int(0, 3)];
    const shape = shapes[int(0, 3)];
    let positions;
    if (shape === 'bell' || shape === 'anti-bell') {
      const lower = shape === 'bell'
        ? [0, int(25, 32), int(40, 44), int(45, 48), int(48, 49)]
        : [0, int(1, 4), int(5, 8), int(9, 12), int(13, 16)];
      positions = lower.flatMap(x => [x, 100 - x]);
    } else {
      positions = [0, int(1, 3), int(4, 7), int(8, 11), int(12, 15),
        int(16, 20), int(21, 26), int(28, 35), int(48, 58), 100];
      if (shape === 'left-skewed') positions = positions.map(x => 100 - x);
    }
    const scale = int(2, 6);
    const offset = int(30, 970 - 100 * scale);
    const witness = positions.map(x => offset + scale * x);
    for (let i = witness.length - 1; i > 0; i--) {
      const j = int(0, i);
      [witness[i], witness[j]] = [witness[j], witness[i]];
    }
    const mean = witness.reduce((total, x) => total + x, 0) / 10;
    const squaredDeviationSum = witness.reduce((total, x) => total + (x - mean) ** 2, 0);
    const variance = squaredDeviationSum / (measure.population ? 10 : 9);
    const spread = measure.squareRoot ? Math.sqrt(variance) : variance;
    return {
      seed: seed >>> 0, measure, shape, witness,
      targets: { count: 10, mean, range: Math.max(...witness) - Math.min(...witness),
        spread: Number(spread.toFixed(4)) }
    };
  }
  const api = { generate, measures, shapes };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.ExcelSpreadGenerator = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
