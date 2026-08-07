#!/usr/bin/env python3
"""Expected-sensitivity scaling for the CMS inelastic dark matter search
(arXiv:2305.11649) from the Run 2 dataset to the Run 3 dataset.

The paper sets expected 95% CL upper limits on sigma(pp -> A' -> chi1 chi2) x
B(chi2 -> chi1 mu mu) using 138 fb^-1 of 13 TeV data (Run 2). With no change
to the analysis, the expected limit improves with integrated luminosity L as

  * ~ 1/L        if the search is background-free (the limit tracks the
                   signal yield; true for the most displaced signal regions)
  * ~ 1/sqrt(L)  if the search is background-dominated

so the two curves bracket the realistic expectation. Luminosities:

  * Run 2 "good for physics": 138 fb^-1 (the paper's dataset)
  * Run 3 delivered to CMS: 355 fb^-1; scaled by the Run 2 ratio of
    good-for-physics to delivered luminosity (138/163 ~ 0.85) -> ~300 fb^-1

The ~5-10% larger signal cross section at 13.6 TeV vs 13 TeV is not included,
so the projection is slightly conservative.
"""

import matplotlib.pyplot as plt
import numpy as np

# Palette (light mode)
BLUE = "#2a78d6"       # series 1: background-free scaling
ORANGE = "#eb6834"     # series 2: background-limited scaling
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASELINE = "#c3c2b7"

LUMI_RUN2 = 138.0                      # fb^-1, dataset of arXiv:2305.11649
LUMI_RUN3 = round(355 * 138 / 163)     # ~300 fb^-1 good-for-physics estimate
LUMI_BOTH = LUMI_RUN2 + LUMI_RUN3

lumi = np.linspace(100, 480, 400)
lim_bkgfree = LUMI_RUN2 / lumi            # expected limit ~ 1/L
lim_bkglim = np.sqrt(LUMI_RUN2 / lumi)    # expected limit ~ 1/sqrt(L)

fig, ax = plt.subplots(figsize=(8, 5.2), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)

ax.fill_between(lumi, lim_bkgfree, lim_bkglim, color=BLUE, alpha=0.08, lw=0)
ax.plot(lumi, lim_bkglim, color=ORANGE, lw=2,
        label=r"background-limited ($\propto 1/\sqrt{L}$)")
ax.plot(lumi, lim_bkgfree, color=BLUE, lw=2,
        label=r"background-free ($\propto 1/L$)")

# Reference point: the paper's Run 2 expected limit
ax.plot([LUMI_RUN2], [1.0], marker="o", ms=8, color=INK, zorder=5)
ax.annotate("Run 2 (paper)\n138 fb$^{-1}$", xy=(LUMI_RUN2, 1.0),
            xytext=(146, 1.045), color=INK, fontsize=9.5)

# Projection markers at Run 3 and Run 2 + Run 3
for L, name, dx in [(LUMI_RUN3, "Run 3 alone", 6), (LUMI_BOTH, "Run 2 + Run 3", 6)]:
    ax.axvline(L, color=BASELINE, lw=1, ls=(0, (4, 4)), zorder=1)
    ax.annotate(f"{name}\n{L:.0f} fb$^{{-1}}$", xy=(L, 1.10), xytext=(L + dx, 1.065),
                color=INK2, fontsize=9.5)
    for scale, color in [(np.sqrt(LUMI_RUN2 / L), ORANGE), (LUMI_RUN2 / L, BLUE)]:
        ax.plot([L], [scale], marker="o", ms=8, color=color, zorder=5,
                markeredgecolor=SURFACE, markeredgewidth=1.5)
        ax.annotate(f"{scale:.2f}", xy=(L, scale), xytext=(L + 6, scale + 0.01),
                    color=color, fontsize=9.5, fontweight="bold")

ax.set_xlim(100, 480)
ax.set_ylim(0, 1.15)
ax.set_xlabel(r"Integrated luminosity  $L$  [fb$^{-1}$]", color=INK2)
ax.set_ylabel("Expected 95% CL limit on $\\sigma B$,\nrelative to Run 2 (lower is better)",
              color=INK2)
ax.set_title("Expected sensitivity vs. dataset size:\n"
             "CMS inelastic dark matter search, displaced $\\mu^+\\mu^-$ + $p_T^{miss}$"
             " (arXiv:2305.11649)",
             color=INK, fontsize=11.5, pad=12)

ax.grid(axis="y", color=GRID, lw=0.8)
ax.set_axisbelow(True)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color(BASELINE)
ax.tick_params(colors=MUTED, labelcolor=INK2)

ax.legend(loc="lower left", frameon=False, fontsize=9.5, labelcolor=INK2)

fig.text(0.055, 0.015,
         "Run 3 good-for-physics luminosity estimated as 355 fb$^{-1}$ delivered "
         "$\\times$ 85% (Run 2 ratio). Statistical scaling only;\nthe ~5–10% larger "
         "signal cross section at 13.6 TeV and any analysis improvements are not "
         "included (conservative).",
         color=MUTED, fontsize=7.5, va="bottom")

fig.tight_layout(rect=(0, 0.055, 1, 1))
for ext in ("png", "pdf"):
    fig.savefig(f"cms_idm_run3_sensitivity.{ext}", facecolor=SURFACE,
                bbox_inches="tight")
print(f"Run 2: {LUMI_RUN2:.0f} fb^-1 (reference, 1.00)")
for L, name in [(LUMI_RUN3, "Run 3 alone"), (LUMI_BOTH, "Run 2 + Run 3")]:
    print(f"{name}: {L:.0f} fb^-1 -> expected limit x{LUMI_RUN2 / L:.2f} "
          f"(background-free) to x{np.sqrt(LUMI_RUN2 / L):.2f} (background-limited)")
