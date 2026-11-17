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
    const gainPercent = gains.reduce((sum, x, i) => sum + (x > 0 ? game.percentages[i] : 0), 0);
    return { gains, mean, sd: Math.sqrt(variance), gainPercent };
  }
  function compare(a, b) {
    const x = summarize(a), y = summarize(b);
    const meanGap = Math.abs(x.mean - y.mean), sdGap = Math.abs(x.sd - y.sd);
    const meaningfulMean = meanGap >= 3 && meanGap >= 0.2 * Math.max(Math.abs(x.mean), Math.abs(y.mean));
    const meaningfulSpread = sdGap >= 5 && Math.max(x.sd, y.sd) >= 2 * Math.min(x.sd, y.sd);
    return { a: x, b: y, meaningfulMean, meaningfulSpread };
  }
  function matchesComparison(kind, { a, b, meaningfulMean, meaningfulSpread }) {
    if (a.mean >= 0 || b.mean >= 0 || a.gains.some((gain, i) => gain === b.gains[i])) return false;
    if (kind === 'similar-mean') {
      return Math.abs(a.mean - b.mean) <= 0.25 && meaningfulSpread && a.sd < b.sd &&
        a.mean + a.sd <= -1 && b.mean + b.sd >= 1 && a.gainPercent <= 10 && b.gainPercent >= 25;
    }
    if (!meaningfulMean || a.mean <= b.mean) return false;
    if (kind === 'similar-spread') {
      return Math.abs(a.sd - b.sd) <= Math.min(0.5, 0.1 * Math.min(a.sd, b.sd));
    }
    return meaningfulSpread && (kind === 'tradeoff' ? a.sd > b.sd : a.sd < b.sd);
  }

  // The pairs are ordered as expected by matchesComparison, before shuffling Games A and B.
  const fallbackGames = {
    'similar-mean': [
      { fee: 10, prizes: [0, 14, 35], percentages: [93, 5, 2] },
      { fee: 21, prizes: [0, 28, 70], percentages: [68, 24, 8] }
    ],
    'both-measures': [
      { fee: 10, prizes: [0, 14, 35], percentages: [93, 5, 2] },
      { fee: 25, prizes: [0, 34, 85], percentages: [80, 13, 7] }
    ],
    tradeoff: [
      { fee: 21, prizes: [0, 28, 70], percentages: [68, 24, 8] },
      { fee: 17, prizes: [0, 23, 44], percentages: [94, 5, 1] }
    ],
    'similar-spread': [
      { fee: 19, prizes: [0, 27, 50], percentages: [80, 8, 12] },
      { fee: 25, prizes: [0, 35, 73], percentages: [81, 16, 3] }
    ]
  };
  const kinds = Object.keys(fallbackGames);

  function generate(seed) {
    const random = rng(seed), int = (lo, hi) => lo + Math.floor(random() * (hi - lo + 1));
    const kind = kinds[int(0, kinds.length - 1)];
    const similarMean = kind === 'similar-mean';

    function game(targetMean, minGainPercent = 10, maxGainPercent = 45, maxLargeGain = 80) {
      const gainPercent = int(minGainPercent, maxGainPercent);
      const largePercent = int(1, Math.min(18, gainPercent - 1));
      const smallPercent = gainPercent - largePercent;
      const lossPercent = 100 - gainPercent;
      const smallGain = int(2, 18), largeGain = int(25, maxLargeGain);
      // Solve for the fee that produces the target mean, then round it to whole dollars.
      const fee = Math.round((smallGain * smallPercent + largeGain * largePercent - 100 * targetMean) / lossPercent);
      return { fee, prizes: [0, fee + smallGain, fee + largeGain], percentages: [lossPercent, smallPercent, largePercent] };
    }

    let games;
    for (let attempt = 0; attempt < 500; attempt++) {
      const targetMean = -int(5, 12);
      const a = similarMean ? game(targetMean, 5, 10, 35) : game(targetMean);
      const b = similarMean ? game(targetMean, 25, 45) : game(targetMean - int(4, 8));
      if (a.fee < 5 || a.fee > 25 || b.fee < 5 || b.fee > 25 ||
          a.percentages.some((p, i) => p === b.percentages[i])) continue;
      if (matchesComparison(kind, compare(a, b))) {
        games = [a, b];
        break;
      }
    }
    // Keep the requested comparison even if a seed exhausts its attempts.
    if (!games) {
      games = fallbackGames[kind].map(({ fee, prizes, percentages }) => ({
        fee, prizes: [...prizes], percentages: [...percentages]
      }));
    }
    if (random() < 0.5) games.reverse();
    return { seed: seed >>> 0, kind, games, comparison: compare(...games) };
  }
  const api = { generate, summarize, compare };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.ExcelRiskRewardGenerator = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
