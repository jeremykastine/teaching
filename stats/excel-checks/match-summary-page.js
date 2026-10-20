/* Minimal problem display for the first Excel competency check. */
(function () {
  'use strict';
  const api = window.ExcelCheckGenerators;
  const problem = document.getElementById('summary-problem');
  const regenerate = document.getElementById('regenerate');
  if (!api || !problem || !regenerate) return;
  function freshSeed() {
    if (window.crypto?.getRandomValues) {
      const values = new Uint32Array(1);
      window.crypto.getRandomValues(values);
      return values[0];
    }
    return Math.floor(Math.random() * 4294967296);
  }
  function render(seed, variation = 'mixed') {
    const { targets } = api.generate(1, seed, variation).meta;
    const { count, mean, median, modes } = targets;
    const modalText = modes.length === 1 ? `a mode of ${modes[0]}` : `modes of ${modes[0]} and ${modes[1]}`;
    problem.textContent = `Suppose ${count} observations have a mean of ${mean}, a median of ${median}, and ${modalText}.`;
  }
  regenerate.addEventListener('click', () => render(freshSeed()));
  // Previously shared links still open their original task, without visible version controls.
  const params = new URLSearchParams(window.location.search);
  const seed = params.get('seed');
  const variant = params.get('variant') || 'mixed';
  const supported = !params.get('v') || params.get('v') === String(api.VERSION);
  const validVariant = ['mixed', 'one-mode', 'two-modes'].includes(variant);
  if (supported && seed && /^[0-9a-f]{8}$/i.test(seed) && validVariant) {
    render(parseInt(seed, 16), variant);
  } else {
    render(freshSeed());
  }
})();
