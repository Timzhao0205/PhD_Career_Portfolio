#!/usr/bin/env python3
"""eps(T, ABV) calibration surface — fit + inversion (v0).

Workflow (CALIBRATION_PROTOCOL.md):
  1. Gravimetric standards -> true % v/v via abv_from_masses().
  2. Per-standard temperature-sweep CSVs (columns: T_C, cap) -> fit a
     low-order 2-D polynomial cap(T, ABV).
  3. Invert numerically to ABV(cap, T) for the estimator.
Coefficients are versioned artifacts (cal_coeffs.json) — never edit,
refit.

Usage:
    python 50_ANALYSIS/calibration_fit.py --selftest
    python 50_ANALYSIS/calibration_fit.py --fit data/cal_*.csv --out 10_SENSING_DESIGN/cal_coeffs.json
    python 50_ANALYSIS/calibration_fit.py --invert cal_coeffs.json --cap 1.234e-12 --temp 5.0
"""
import argparse
import glob
import json
import re
import sys
from pathlib import Path

import numpy as np

# Densities at 20 °C (g/mL), pure components.
RHO_ETH = 0.7893
RHO_WAT = 0.9982

# ABW (wt%) <-> ABV (% v/v) anchor table at 20 °C (OIML-consistent).
# Ethanol-water mixing contracts up to ~3 %, so volumes are NOT
# additive — never compute ABV from ideal component volumes. Sanity
# anchors: 33.3 wt% <-> 40.0 % v/v (standard whisky), 42.4 wt% <-> 50 % v/v.
_ABW = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], float)
_ABV = np.array([0, 12.4, 24.5, 36.2, 47.4, 57.8, 67.4, 76.4, 84.5, 91.8, 100], float)


def abw_from_masses(m_spirit_g: float, m_water_g: float,
                    source_abw: float = 0.924) -> float:
    """EXACT alcohol-by-weight (wt%) of a gravimetric standard.

    m_spirit_g : grams of source spirit added (190-proof Everclear:
                 95 % v/v = 92.4 wt% -> source_abw = 0.924)
    m_water_g  : grams of DI water added
    Mass balance only — no density assumptions, no approximation.
    Prefer parameterizing the calibration surface in ABW; it is the
    quantity the balance gives you exactly.
    """
    return 100.0 * (m_spirit_g * source_abw) / (m_spirit_g + m_water_g)


def abv_from_abw(abw_pct: float) -> float:
    """Convert wt% -> % v/v via the 20 °C anchor table (interp)."""
    return float(np.interp(abw_pct, _ABW, _ABV))


def abv_from_masses(m_spirit_g: float, m_water_g: float,
                    source_abw: float = 0.924) -> float:
    """% v/v label for a gravimetric standard (exact ABW -> table)."""
    return abv_from_abw(abw_from_masses(m_spirit_g, m_water_g, source_abw))


def design_matrix(T, A, order_t=2, order_a=3):
    """Polynomial features T^i * A^j, i<=order_t, j<=order_a."""
    cols = []
    names = []
    for i in range(order_t + 1):
        for j in range(order_a + 1):
            cols.append((T ** i) * (A ** j))
            names.append(f"T^{i}A^{j}")
    return np.column_stack(cols), names


def fit_surface(T, A, C, order_t=2, order_a=3):
    X, names = design_matrix(np.asarray(T, float), np.asarray(A, float),
                             order_t, order_a)
    coef, *_ = np.linalg.lstsq(X, np.asarray(C, float), rcond=None)
    resid = X @ coef - C
    return {"order_t": order_t, "order_a": order_a,
            "coef": coef.tolist(), "names": names,
            "rms_resid": float(np.sqrt(np.mean(resid ** 2))),
            "max_resid": float(np.max(np.abs(resid)))}


def predict_cap(model, T, A):
    X, _ = design_matrix(np.atleast_1d(np.asarray(T, float)),
                         np.atleast_1d(np.asarray(A, float)),
                         model["order_t"], model["order_a"])
    return X @ np.asarray(model["coef"])


def invert_abv(model, cap, T, lo=0.0, hi=60.0):
    """Numeric inversion cap -> ABV at fixed T (bisection; cap(A) must
    be monotone over [lo, hi] at fixed T — verify on the fitted
    surface, it is for eps-like data)."""
    f = lambda a: float(np.ravel(predict_cap(model, T, a))[0]) - cap
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        raise ValueError("cap outside calibrated range at this T")
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def _synthetic_truth(T, A):
    """Plausible eps-like surface for the selftest: linear mix of
    water(T) and ethanol permittivities + mild curvature."""
    eps_w = 78.4 * (1 - 0.0037 * (T - 25.0))
    eps_e = 24.3 * (1 - 0.0020 * (T - 25.0))
    f = A / 100.0
    return eps_w * (1 - f) + eps_e * f - 6.0 * f * (1 - f)  # excess term


def selftest():
    rng = np.random.default_rng(1)
    T = rng.uniform(-8, 30, 400)
    A = rng.uniform(0, 60, 400)
    C = _synthetic_truth(T, A) + 0.05 * rng.standard_normal(400)
    model = fit_surface(T, A, C)
    # round-trip: invert at 200 random points
    errs = []
    for _ in range(200):
        t = rng.uniform(-5, 25)
        a = rng.uniform(5, 55)
        cap = _synthetic_truth(t, a)
        errs.append(invert_abv(model, cap, t) - a)
    errs = np.abs(errs)
    ok = errs.max() < 1.0
    print(f"fit rms={model['rms_resid']:.3f}  max={model['max_resid']:.3f} (eps units)")
    print(f"round-trip ABV error: mean={errs.mean():.3f}  max={errs.max():.3f} %ABV")
    print("SELFTEST", "PASS" if ok else "FAIL", "- inversion within 1 %ABV on synthetic surface")
    # gravimetric sanity: 100 g 190-proof + 100 g DI = 46.2 wt% -> ~53.8 % v/v;
    # and the standard-whisky anchor 33.3 wt% -> 40.0 % v/v.
    abw = abw_from_masses(100.0, 100.0)
    abv = abv_from_abw(abw)
    anchor = abv_from_abw(33.3)
    print(f"gravimetric check: 100 g 190-proof + 100 g DI -> {abw:.1f} wt% -> {abv:.1f} % v/v (expect ~53-54)")
    print(f"anchor check: 33.3 wt% -> {anchor:.1f} % v/v (expect 40.0)")
    return 0 if ok and 53.0 < abv < 55.0 and 39.5 < anchor < 40.5 else 1


def load_cal_csvs(patterns):
    import pandas as pd
    T, A, C = [], [], []
    for pat in patterns:
        for path in sorted(glob.glob(pat)):
            m = re.search(r"cal_(\d+(?:\.\d+)?)pct", Path(path).name)
            if not m:
                print(f"skip (no ABV in name): {path}")
                continue
            abv = float(m.group(1))
            df = pd.read_csv(path)
            T.extend(df["T_C"].tolist())
            C.extend(df["cap"].tolist())
            A.extend([abv] * len(df))
    return np.array(T), np.array(A), np.array(C)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--fit", nargs="+", metavar="CSV_GLOB")
    ap.add_argument("--out", default="cal_coeffs.json")
    ap.add_argument("--invert", metavar="COEFFS_JSON")
    ap.add_argument("--cap", type=float)
    ap.add_argument("--temp", type=float)
    args = ap.parse_args()

    if args.selftest:
        sys.exit(selftest())
    if args.fit:
        T, A, C = load_cal_csvs(args.fit)
        if len(T) == 0:
            sys.exit("no calibration data loaded")
        model = fit_surface(T, A, C)
        Path(args.out).write_text(json.dumps(model, indent=2), encoding="utf-8")
        print(f"wrote {args.out}: rms={model['rms_resid']:.4g} max={model['max_resid']:.4g} over {len(T)} pts")
        return
    if args.invert:
        model = json.loads(Path(args.invert).read_text(encoding="utf-8"))
        print(f"ABV = {invert_abv(model, args.cap, args.temp):.2f} % v/v")
        return
    ap.print_help()


if __name__ == "__main__":
    main()
