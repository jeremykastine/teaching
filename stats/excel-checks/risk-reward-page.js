(function () {
  'use strict';
  const api = window.ExcelRiskRewardGenerator, body = document.getElementById('game-data');
  if (!api || !body) return;
  function render() {
    let seed;
    if (window.crypto?.getRandomValues) {
      const values = new Uint32Array(1);
      window.crypto.getRandomValues(values);
      seed = values[0];
    } else seed = Math.floor(Math.random() * 4294967296);
    const { games } = api.generate(seed);
    body.replaceChildren();
    for (const [i, game] of games.entries()) {
      const row = document.createElement('tr');
      const values = [`Game ${i === 0 ? 'A' : 'B'}`, `$${game.fee}`,
        ...game.prizes.map((prize, j) => `$${prize} (${game.percentages[j]}%)`)];
      values.forEach((value, j) => {
        const cell = document.createElement(j === 0 ? 'th' : 'td');
        if (j === 0) cell.scope = 'row';
        cell.textContent = value;
        cell.dataset.label = ['Game', 'Entry fee', 'No prize', 'Small prize', 'Large prize'][j];
        row.append(cell);
      });
      body.append(row);
    }
  }
  document.getElementById('regenerate').addEventListener('click', render);
  render();
})();
