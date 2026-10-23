/* Minimal target-only display, parallel to Check 1. */
(function () {
  'use strict';
  const api = window.ExcelSpreadGenerator;
  const problem = document.getElementById('spread-problem');
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
  function render() {
    // Only summaries reach the DOM; the witness data and shape are never displayed.
    const { targets, measure } = api.generate(freshSeed());
    const target = value => {
      const node = document.createElement('u');
      node.className = 'summary-target';
      node.textContent = value;
      return node;
    };
    problem.replaceChildren('Suppose ', target(`${targets.count} observations`), ' have a ',
      target(`mean of ${targets.mean}`), ', a ', target(`range of ${targets.range}`),
      ', and a ', target(`${measure.label} of ${targets.spread}`), '.');
  }
  regenerate.addEventListener('click', render);
  render();
})();
