/* Independent of the legacy generators so saved tasks for other checks stay stable. */
(function (root) {
  'use strict';
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
  function summarize(game) {
    const gains = game.prizes.map(x => x - game.fee);
    const mean = gains.reduce((sum, x, i) => sum + x * game.percentages[i] / 100, 0);
    const variance = gains.reduce((sum, x, i) => sum + (x - mean) ** 2 * game.percentages[i] / 100, 0);
    return { gains, mean, sd: Math.sqrt(variance) };
  }
  function compare(a, b) {
    const x = summarize(a), y = summarize(b);
    const meanGap = Math.abs(x.mean - y.mean), sdGap = Math.abs(x.sd - y.sd);
    // Dollar and proportional floors avoid differences that are merely rounding noise.
    const meaningfulMean = meanGap >= 3 && meanGap >= 0.2 * Math.max(Math.abs(x.mean), Math.abs(y.mean));
    const meaningfulSpread = sdGap >= 5 && sdGap >= 0.35 * Math.min(x.sd, y.sd);
    return { a: x, b: y, meaningfulMean, meaningfulSpread };
  }
  function generate(seed) {
    const random = rng(seed), int = (lo, hi) => lo + Math.floor(random() * (hi - lo + 1));
    const kind = ['tradeoff', 'similar-mean', 'both-measures'][int(0, 2)];
    function game() {
      const fee = int(5, 25), loss = int(35, 75), big = int(5, Math.min(25, 95 - loss));
      return { fee, prizes: [0, fee + int(2, 18), fee + int(25, 120)], percentages: [loss, 100 - loss - big, big] };
    }
    let games;
    for (let attempt = 0; attempt < 2000; attempt++) {
      const a = game(), b = game(), c = compare(a, b);
      if (a.fee === b.fee || a.percentages.some((p, i) => p === b.percentages[i]) ||
          c.a.gains.some((x, i) => x === c.b.gains[i])) continue;
      const direction = (c.a.mean - c.b.mean) * (c.a.sd - c.b.sd);
      const accepted = kind === 'similar-mean' ? Math.abs(c.a.mean - c.b.mean) <= 1 && c.meaningfulSpread
        : c.meaningfulMean && c.meaningfulSpread && (kind === 'tradeoff' ? direction > 0 : direction < 0);
      if (accepted) { games = [a, b]; break; }
    }
    // Bounded, validated fallback for every requested comparison type.
    if (!games) {
      const safe = { fee: 10, prizes: [0, 15, 30], percentages: [50, 40, 10] };
      const alternatives = {
        tradeoff: { fee: 15, prizes: [0, 20, 100], percentages: [60, 20, 20] },
        'similar-mean': { fee: 15, prizes: [0, 20, 80], percentages: [65, 23, 12] },
        'both-measures': { fee: 25, prizes: [0, 30, 100], percentages: [70, 20, 10] }
      };
      games = [safe, alternatives[kind]];
    }
    if (random() < 0.5) games.reverse();
    return { seed: seed >>> 0, kind, games, comparison: compare(...games) };
  }
  const api = { generate, summarize, compare };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.ExcelRiskRewardGenerator = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
