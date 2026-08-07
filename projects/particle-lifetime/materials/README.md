# Supplementary materials

## Run 2 → Run 3 sensitivity scaling for the CMS inelastic dark matter search

`make_run3_sensitivity_plot.py` produces `cms_idm_run3_sensitivity.png/.pdf`,
a simple projection of how the expected sensitivity of the CMS search for
inelastic dark matter with a displaced muon pair and missing transverse
momentum ([arXiv:2305.11649](https://arxiv.org/abs/2305.11649), 138 fb⁻¹ of
Run 2 data) would scale with the CMS Run 3 dataset.

The expected 95% CL upper limit on σB is shown relative to the Run 2 result
as a function of integrated luminosity, bracketed by the two limiting
statistical regimes:

- **background-free** (limit ∝ 1/L) — appropriate for the most displaced,
  essentially zero-background signal regions of this search;
- **background-limited** (limit ∝ 1/√L) — appropriate where residual
  background dominates.

Run 3 delivered 355 fb⁻¹ to CMS; scaling by the Run 2 good-for-physics /
delivered ratio (~85%) gives a ~300 fb⁻¹ analysis-quality dataset, i.e. an
expected limit **~1.5–2.2× stronger** from Run 3 alone and **~1.8–3.2×
stronger** for Run 2 + Run 3 combined. The ~5–10% larger signal cross section
at 13.6 TeV and any analysis improvements are not included, so the projection
is conservative.

Requires `numpy` and `matplotlib`; run with

```bash
python3 make_run3_sensitivity_plot.py
```
