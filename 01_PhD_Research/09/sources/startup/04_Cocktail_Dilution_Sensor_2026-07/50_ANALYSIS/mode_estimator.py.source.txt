#!/usr/bin/env python3
"""Burst mode-of-histogram estimator — reference implementation (v0).

Core idea (ESTIMATOR_SPEC.md): bubble outliers on a fringing-field
capacitor are ONE-SIDED (eps -> 1, i.e. capacitance drops), so the
mean and even the median of a corrupted burst are biased low. The
histogram mode of the burst recovers the clean-liquid level even with
heavy corruption. Firmware ports this math; it must not diverge from
this file without a DECISIONS.md entry.

Usage:
    python 50_ANALYSIS/mode_estimator.py --selftest
    python 50_ANALYSIS/mode_estimator.py burst.csv --col cap --bin-scale 3
"""
import argparse
import sys

import numpy as np


def mode_estimate(samples: np.ndarray, noise_sigma: float, bin_scale: float = 3.0):
    """Return (mode_value, n_valid, occlusion_fraction).

    samples     : 1-D array of burst capacitance readings (any units)
    noise_sigma : sensor noise floor (same units) — sets histogram bin
                  width = bin_scale * noise_sigma (measure in P0-E0)
    Method: histogram -> modal bin -> local quadratic refinement over
    the modal bin and its neighbors (sub-bin resolution).
    """
    x = np.asarray(samples, dtype=float)
    x = x[np.isfinite(x)]
    if x.size < 20:
        raise ValueError("burst too short for a mode estimate (<20 samples)")

    bw = max(bin_scale * noise_sigma, 1e-12)
    lo, hi = x.min(), x.max()
    nbins = max(int(np.ceil((hi - lo) / bw)), 3)
    counts, edges = np.histogram(x, bins=nbins)
    k = int(np.argmax(counts))
    centers = 0.5 * (edges[:-1] + edges[1:])

    # local quadratic refinement around the modal bin
    if 0 < k < nbins - 1 and counts[k - 1] + counts[k + 1] > 0:
        c_m1, c_0, c_p1 = counts[k - 1], counts[k], counts[k + 1]
        denom = (c_m1 - 2 * c_0 + c_p1)
        delta = 0.0 if denom == 0 else 0.5 * (c_m1 - c_p1) / denom
        delta = float(np.clip(delta, -0.5, 0.5))
        mode = centers[k] + delta * bw
    else:
        mode = centers[k]

    # samples within ±2 bins of the mode count as "clean"
    valid = np.abs(x - mode) <= 2 * bw
    n_valid = int(valid.sum())
    occlusion = 1.0 - n_valid / x.size
    return float(mode), n_valid, float(occlusion)


def _synthetic_burst(n=2000, clean_level=100.0, noise=0.05,
                     corrupt_frac=0.4, seed=0):
    """Clean Gaussian level + one-sided bubble excursions toward air."""
    rng = np.random.default_rng(seed)
    x = clean_level + noise * rng.standard_normal(n)
    m = rng.random(n) < corrupt_frac
    # bubbles pull capacitance DOWN by 5–60 % of the water-air contrast
    x[m] -= rng.uniform(5, 60, m.sum())
    return x


def selftest():
    print("corrupt%   mean_err   median_err   mode_err   (units: same as level; clean level=100, sigma=0.05)")
    ok = True
    for frac in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5):
        errs_mode = []
        errs_mean = []
        errs_med = []
        for seed in range(20):
            x = _synthetic_burst(corrupt_frac=frac, seed=seed)
            mode, _, _ = mode_estimate(x, noise_sigma=0.05)
            errs_mode.append(mode - 100.0)
            errs_mean.append(x.mean() - 100.0)
            errs_med.append(np.median(x) - 100.0)
        em, ed, eo = np.mean(np.abs(errs_mean)), np.mean(np.abs(errs_med)), np.mean(np.abs(errs_mode))
        print(f"  {frac:4.0%}    {em:8.3f}   {ed:9.3f}   {eo:8.3f}")
        if frac <= 0.4 and eo > 0.05:  # mode must stay within ~1 noise sigma
            ok = False
    print("SELFTEST", "PASS" if ok else "FAIL",
          "- mode stays unbiased to >=40% corruption; mean/median do not")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", nargs="?", help="burst CSV file")
    ap.add_argument("--col", default="cap", help="column name (default: cap)")
    ap.add_argument("--noise-sigma", type=float, default=None,
                    help="sensor noise floor; default = robust MAD of the burst")
    ap.add_argument("--bin-scale", type=float, default=3.0)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        sys.exit(selftest())
    if not args.csv:
        ap.error("provide a CSV or --selftest")

    import pandas as pd
    df = pd.read_csv(args.csv)
    x = df[args.col].to_numpy(dtype=float)
    sigma = args.noise_sigma
    if sigma is None:
        med = np.median(x)
        sigma = 1.4826 * np.median(np.abs(x - med))  # MAD estimate
    mode, n_valid, occ = mode_estimate(x, noise_sigma=sigma, bin_scale=args.bin_scale)
    print(f"mode={mode:.6g}  n_valid={n_valid}/{x.size}  occlusion={occ:.1%}  sigma_used={sigma:.3g}")


if __name__ == "__main__":
    main()
