(function () {
  'use strict';

  const problem = document.getElementById('binomial-problem');
  const regenerate = document.getElementById('regenerate');
  const percentages = [30, 35, 40, 45, 50, 55, 60, 65, 70];
  const trialCounts = [6, 7, 8, 9, 10, 11, 12];
  const parameterCount = percentages.length * trialCounts.length;
  let previous = -1;

  function render() {
    const choices = previous < 0 ? parameterCount : parameterCount - 1;
    let index = Math.floor(Math.random() * choices);
    if (previous >= 0 && index >= previous) index += 1;
    previous = index;

    const percentage = percentages[index % percentages.length];
    const trials = trialCounts[Math.floor(index / percentages.length)];
    problem.textContent = `Use p = ${percentage}% and n = ${trials} trials per experiment. Simulate 100 experiments.`;
  }

  regenerate.addEventListener('click', render);
  render();
})();
