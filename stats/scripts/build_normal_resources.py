#!/usr/bin/env python3
"""Rebuild the simplified normal table and exact, static lesson plots.

Run from any directory with a Python environment containing matplotlib.
The lesson HTML is hand-authored; this script only rebuilds its resources.
"""
from pathlib import Path
from math import comb, erf, exp, pi, sqrt
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

STATS = Path(__file__).resolve().parents[1]
ASSETS = STATS / "assets" / "normal"
ASSETS.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "svg.fonttype": "none", "svg.hashsalt": "normal-lesson",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.labelcolor": "#243b53", "text.color": "#243b53",
    "axes.edgecolor": "#829ab1", "xtick.color": "#486581",
    "ytick.color": "#486581",
})


def cdf(z):
    return (1 + erf(z / sqrt(2))) / 2


def density(z):
    return exp(-z*z/2) / sqrt(2*pi)


def save(fig, filename, description):
    fig.savefig(ASSETS / filename, bbox_inches="tight",
                metadata={"Date": None, "Description": description})
    plt.close(fig)


def plots():
    xs = [-4 + i/100 for i in range(801)]
    ys = [density(x) for x in xs]
    for n in [4, 16, 64, 256]:
        mean, sd = n/2, sqrt(n/4)
        zs = [(k-mean)/sd for k in range(n+1)]
        masses = [comb(n, k) / 2**n for k in range(n+1)]
        width = 1/sd
        fig, ax = plt.subplots(figsize=(6.2, 4.1), layout="constrained")
        ax.bar(zs, [p/width for p in masses], width=width,
               color="#c5dcef", edgecolor="#467ba5", linewidth=.6,
               label="Binomial bars")
        ax.plot(xs, ys, color="#b54327", linewidth=2.5, label="Normal curve")
        ax.set(xlim=(-4, 4), ylim=(0, .46), xlabel="z = (heads − n/2) / √(n/4)",
               ylabel="Density (bar area = probability)", title=f"{n} fair coin tosses")
        ax.set_xticks([-4, -2, 0, 2, 4])
        ax.set_yticks([0, .2, .4])
        ax.legend(loc="upper left", frameon=False, fontsize=10)
        save(fig, f"binomial-{n:03d}.svg",
             f"Exact Binomial({n}, 0.5), standardized to mean zero and SD one. "
             "Bars have width one over the binomial SD and area equal to the exact mass; "
             "the overlaid curve is the standard normal density. All panels use identical axes.")

    regions = [
        ("left", lambda z: z <= .8, "Area to the left", "F(0.8)", [.8]),
        ("right", lambda z: z >= .8, "Area to the right", "1 − F(0.8)", [.8]),
        ("between", lambda z: -.8 <= z <= 1.4, "Area between cutoffs", "F(1.4) − F(−0.8)", [-.8, 1.4]),
    ]
    for name, included, title, label, cuts in regions:
        fig, ax = plt.subplots(figsize=(6.2, 3.2), layout="constrained")
        ax.fill_between(xs, ys, where=[included(x) for x in xs],
                        color="#b8d7ee", interpolate=True)
        ax.plot(xs, ys, color="#245985", linewidth=2)
        for cut in cuts:
            ax.vlines(cut, 0, density(cut), color="#b54327", linewidth=1.5)
        ax.set(xlim=(-3.5, 3.5), ylim=(0, .47), xlabel="z", title=title)
        ax.set_xticks(sorted(set([-3, 0, 3] + cuts)))
        ax.set_yticks([])
        ax.text(.03, .92, label, transform=ax.transAxes, fontsize=13)
        save(fig, f"normal-{name}.svg", f"Standard normal curve: {title.lower()}. {label}.")

    fig, ax = plt.subplots(figsize=(8.5, 3.8), layout="constrained")
    ax.plot(xs, ys, color="#245985", linewidth=2.5)
    ax.set(xlim=(-3.5, 3.5), ylim=(0, .44), xlabel="z-score", title="Same positions, different units")
    ticks = list(range(-3, 4))
    ax.set_xticks(ticks)
    ax.set_yticks([])
    top = ax.secondary_xaxis("top", functions=(lambda z: 70+10*z, lambda x: (x-70)/10))
    top.set_xlabel("Score X: mean 70, standard deviation 10")
    top.set_xticks([40, 50, 60, 70, 80, 90, 100])
    ax.axvline(0, color="#829ab1", linestyle="--", linewidth=1)
    save(fig, "standardizing.svg", "A normal curve labeled in score units above and z-scores below: "
         "scores 40, 50, 60, 70, 80, 90, 100 align with z-scores minus three through three.")


def table_html():
    def table(start, end, caption):
        rows = []
        for tenth in range(start, end+1):
            z = tenth/10
            rows.append(f'          <tr data-z="{z:.1f}" data-probability="{cdf(z):.3f}">'
                        f'<th scope="row">{z:.1f}</th><td>{cdf(z):.3f}</td></tr>')
        return f'''      <table>
        <caption>{caption}</caption>
        <thead><tr><th scope="col">z</th><th scope="col">Area to the left, F(z)</th></tr></thead>
        <tbody>
{chr(10).join(rows)}
        </tbody>
      </table>'''
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Simplified Standard Normal Table | MSC 201</title>
  <link rel="stylesheet" href="../tsm/styles.css">
  <link rel="stylesheet" href="lecture-notes.css">
  <link rel="stylesheet" href="normal-lesson.css">
</head>
<body><main class="lecture-notes normal-lesson normal-table-page">
  <nav class="topic-nav" aria-label="Page navigation">
    <a href="lessons/section-6-1-6-2-normal-distribution.html">Combined 6.1–6.2 notes</a>
    <a href="lecture-notes.html">Lecture notes index</a>
  </nav>
  <p class="series-title">MSC 201 · Reference table</p>
  <h1>Simplified standard normal table</h1>
  <p><strong>Every entry is the area to the left:</strong> F(z) = P(Z ≤ z). Z has mean 0 and standard deviation 1.</p>
  <p>Round a calculated z-score to the nearest <strong>tenth</strong>, then look up its probability. Probabilities are rounded to <strong>three decimal places</strong>. Do not interpolate. For a halfway z-score, round away from zero.</p>
  <p>For a percentile, find the table probability closest to the requested left-tail probability and read its z-score. If entries are equally close, use the z-score closer to zero. Then use x = μ + zσ.</p>
  <p>Right tail: 1 − F(z). Between two cutoffs: F(upper z) − F(lower z).</p>
  <figure class="table-key"><img src="assets/normal/normal-left.svg" width="620" height="320" alt="A standard normal curve with the area to the left of a positive cutoff shaded. The table gives this shaded area."><figcaption>At z = 0.8, the table gives F(0.8) = 0.788.</figcaption></figure>
  <div class="normal-table-columns">
{table(-40, -1, 'Negative z-scores')}
{table(0, 40, 'Zero and positive z-scores')}
  </div>
  <p><strong>Rounding is approximate.</strong> A displayed 0.000 or 1.000 is rounded; finite normal cutoffs never have exactly zero or one cumulative probability. Beyond z = ±4.0, the corresponding tails also round to 0.000 at this precision.</p>
  <p>This table uses 0.1 increments for classroom approximation. Rounding a z-score can change a cumulative probability by about two percentage points near the center. Interval probabilities combine two endpoint approximations.</p>
  <footer class="attribution">Standard normal cumulative probabilities, rounded for classroom use. Every entry gives area to the left.</footer>
</main></body>
</html>
'''


if __name__ == "__main__":
    plots()
    (STATS / "normal-table.html").write_text(table_html())
    print("Built eight static SVG figures and the 81-entry simplified normal table.")
