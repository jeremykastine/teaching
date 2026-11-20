#!/usr/bin/env python3
"""Build exact sample-mean curves for the condensed CLT lesson.

The illustrative population is Gamma(shape=4, scale=3), so its mean is 12
and SD is 6. The mean of n iid observations is Gamma(4*n, 3/n).
The lesson does not require students to know the gamma distribution.
"""
from pathlib import Path
import argparse

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma, norm

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "stats/assets/clt"


def build(preview=None):
    DEST.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 14, "svg.fonttype": "none"})
    fig, axes = plt.subplots(1, 3, figsize=(13.2, 5.16), sharex=True, sharey=True)
    x = np.linspace(0, 32, 1400)
    for ax, n, title in zip(axes, [1, 9, 36], ["One observation", "Average of 9", "Average of 36"]):
        y = gamma.pdf(x, a=4*n, scale=3/n)
        ax.fill_between(x[::8], y[::8], color="#246b9b", alpha=0.13)
        ax.plot(x, y, color="#246b9b", linewidth=2.6, label="Exact distribution")
        ax.axvline(12, color="#687787", linestyle=":", linewidth=1.4)
        if n == 36:
            ax.plot(x, norm.pdf(x, loc=12, scale=1), color="#b74924", linewidth=2.2,
                    linestyle="--", label="Normal approximation")
        ax.set_title(title, fontsize=16, fontweight="bold", pad=30)
        ax.text(0.5, 1.035, f"n = {n}  |  center = 12  |  {'SD' if n == 1 else 'SE'} = {6/np.sqrt(n):g}",
                transform=ax.transAxes, ha="center", fontsize=12)
        ax.set_xlim(0, 32)
        ax.set_ylim(0, 0.44)
        ax.set_xticks([0, 6, 12, 18, 24, 30])
        ax.set_xlabel("Minutes")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=0.15)
    axes[0].set_ylabel("Probability density")
    axes[2].legend(loc="upper right", bbox_to_anchor=(1.02, 0.91), fontsize=9, frameon=False)
    fig.subplots_adjust(left=0.07, right=0.985, bottom=0.17, top=0.77, wspace=0.17)
    fig.suptitle("Averages keep the center and reduce the spread", y=0.98, fontsize=19, fontweight="bold")
    fig.savefig(DEST / "sample-means.svg", metadata={"Date": None})
    if preview:
        fig.savefig(preview, dpi=130)
    plt.close(fig)
    print("Built stats/assets/clt/sample-means.svg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview", type=Path, help="Optional PNG preview path")
    build(parser.parse_args().preview)
