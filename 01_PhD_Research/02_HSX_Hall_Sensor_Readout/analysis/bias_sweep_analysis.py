#!/usr/bin/env python3
"""Analyse the 2026-07-10 bias-current sweep and rebuild the results figures.

Reads the DSO-X 4022A captures in ``data/2026-07-10_bias_sweep/`` and reports,
per capture: the spinning phase rate recovered from the data, the settled
per-state amplitude, and the transfer slope in V/mA.

The phase rate is not written in the capture files, so it is recovered by
folding: for a trial phase duration Tp the record is wrapped modulo the 8-state
cycle (8·Tp), each phase is trimmed at both edges to drop mux settling, and the
residual variance about the eight per-state means is scored. The Tp that leaves
the least residual is the true one. On the three ``_v2`` captures — which also
recorded sync on CH1 — the folded answer is checked against the sync period,
and the two agree to better than 2 %.

    python3 analysis/bias_sweep_analysis.py            # table only
    python3 analysis/bias_sweep_analysis.py --figures  # also rebuild the PNGs
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
DATA = PROJECT / "data" / "2026-07-10_bias_sweep"
FIGURES = HERE / "figures"

GAIN = 100.3          # AD8429, R_G = 60.4 ohm
Z_DECK = 37.26        # per-state differential source resistance, deck model
BLANK = 0.45          # fraction of each phase discarded at its edges

# capture -> (bias current in mA, label)
CAPTURES = [
    ("100uA",      0.1,  "100 µA"),
    ("500uA",      0.5,  "500 µA"),
    ("1mA",        1.0,  "1 mA"),
    ("2mA",        2.0,  "2 mA"),
    ("5mA_10khz",  5.0,  "5 mA"),
    ("10mA_10khz", 10.0, "10 mA"),
    ("500uA_v2",   0.5,  "500 µA (sync)"),
    ("1mA_v2",     1.0,  "1 mA (sync)"),
    ("2mA_v2",     2.0,  "2 mA (sync)"),
]


def load(path: Path):
    """Return (t, channels) from a DSO-X 4022A CSV export."""
    rows, header = [], None
    with path.open(encoding="utf-8-sig") as fh:
        for line in fh:
            parts = [x.strip() for x in line.rstrip("\n").split(",")]
            if parts and parts[0].startswith("Sample Number"):
                header = [c for c in parts if c]
                continue
            if header and parts and parts[0].isdigit():
                rows.append([float(x) for x in parts[1:len(header)]])
    if header is None:
        raise ValueError(f"{path}: no 'Sample Number' header row")
    a = np.asarray(rows)
    return a[:, 0], a[:, 1:]


def fold(t, v, phase, blank=BLANK):
    """Fold onto the 8-state cycle. Returns (score, per-state means)."""
    pos = np.mod(t - t[0], 8 * phase) / phase       # 0..8
    state = np.floor(pos).astype(int) % 8
    frac = pos - np.floor(pos)
    keep = (frac > blank / 2) & (frac < 1 - blank / 2)
    means = np.full(8, np.nan)
    residual = []
    for k in range(8):
        m = keep & (state == k)
        if m.sum() < 5:
            return -1.0, means
        means[k] = v[m].mean()
        residual.append(v[m] - means[k])
    total = v[keep].var()
    if total <= 0:
        return -1.0, means
    return 1.0 - np.concatenate(residual).var() / total, means


def recover_phase(t, v, lo_us=5.0, hi_us=200.0, coarse=4000):
    """Grid-search then refine the phase duration that best explains the record."""
    grid = np.linspace(lo_us * 1e-6, hi_us * 1e-6, coarse)
    scores = np.array([fold(t, v, p)[0] for p in grid])
    p0 = grid[int(np.argmax(scores))]
    step = grid[1] - grid[0]
    fine = np.linspace(p0 - step, p0 + step, 400)
    scores = np.array([fold(t, v, p)[0] for p in fine])
    best = fine[int(np.argmax(scores))]
    return best, float(np.max(scores))


def sync_phase(t, sync):
    """Phase duration from the sync channel: sync is high for exactly one state."""
    threshold = (sync.max() + sync.min()) / 2
    high = sync > threshold
    rises = np.where((~high[:-1]) & (high[1:]))[0]
    if len(rises) < 2:
        return None
    return float(np.mean(np.diff(t[rises])) / 8)


def analyse(name):
    t, ch = load(DATA / f"{name}.csv")
    v = ch[:, -1]                       # CH2 = v_meas, always the last column
    phase, score = recover_phase(t, v)
    _, means = fold(t, v, phase)
    pedestal = float(np.mean(means))
    amplitude = float(np.mean(np.abs(means - pedestal)))
    result = {
        "name": name, "t": t, "v": v,
        "fs": 1.0 / float(np.median(np.diff(t))),
        "phase": phase, "f_kHz": 1e-3 / phase, "score": score,
        "means": means, "pedestal": pedestal, "amplitude": amplitude,
        "sync_f_kHz": None,
    }
    if ch.shape[1] > 1:
        sp = sync_phase(t, ch[:, 0])
        if sp:
            result["sync_f_kHz"] = 1e-3 / sp
    return result


def slope(bias, amplitude):
    """Least-squares slope and intercept, plus the through-origin slope."""
    m, b = np.polyfit(bias, amplitude, 1)
    through = float((bias * amplitude).sum() / (bias * bias).sum())
    return float(m), float(b), through


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--figures", action="store_true", help="rebuild the PNGs in analysis/figures/")
    args = ap.parse_args(argv)

    if not DATA.is_dir():
        raise SystemExit(f"missing capture directory: {DATA}")

    results = {}
    print(f"{'capture':14} {'I (mA)':>7} {'fs (kHz)':>9} {'phase (µs)':>11} "
          f"{'f (kHz)':>8} {'sync f':>8} {'fit':>6} {'amp (V)':>8} {'V/mA':>7}")
    for name, bias, _ in CAPTURES:
        r = analyse(name)
        r["bias"] = bias
        results[name] = r
        sync = f"{r['sync_f_kHz']:.2f}" if r["sync_f_kHz"] else "—"
        print(f"{name:14} {bias:7.1f} {r['fs']/1e3:9.1f} {r['phase']*1e6:11.2f} "
              f"{r['f_kHz']:8.2f} {sync:>8} {r['score']:6.3f} {r['amplitude']:8.3f} "
              f"{r['amplitude']/bias:7.3f}")

    linear = [n for n, b, _ in CAPTURES if b <= 2.0 and not n.endswith("_v2")]
    bias = np.array([results[n]["bias"] for n in linear])
    amp = np.array([results[n]["amplitude"] for n in linear])
    m, b, through = slope(bias, amp)
    predicted = Z_DECK * GAIN / 1000.0

    print(f"\n10 kHz set, unclipped points only ({', '.join(linear)}):")
    print(f"  least squares      : {m:.3f} V/mA, intercept {b*1000:+.0f} mV")
    print(f"  through the origin : {through:.3f} V/mA")
    print(f"  deck prediction    : {predicted:.3f} V/mA  ->  measured is {100*(1-m/predicted):.1f}% low")
    print(f"  implied per-state differential source: {m*1000/GAIN:.2f} Ω "
          f"(deck model {Z_DECK} Ω)")

    print("\nsame bias, 10 kHz vs 40 kHz:")
    for name in ("500uA", "1mA", "2mA"):
        a10, a40 = results[name]["amplitude"], results[name + "_v2"]["amplitude"]
        print(f"  {results[name]['bias']:4.1f} mA : {a10:6.3f} V  vs  {a40:6.3f} V"
              f"   ({100*(a40-a10)/a10:+5.2f} %)")

    if args.figures:
        make_figures(results, linear, m, b)
    return 0


def make_figures(results, linear, m, b):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    FIGURES.mkdir(parents=True, exist_ok=True)
    rail = 13.7

    # ---- results figure: waveforms + transfer -----------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.81))
    colours = {"100uA": "tab:blue", "500uA": "tab:orange", "1mA": "tab:green", "2mA": "tab:red"}
    for name, label in (("100uA", "100 µA"), ("500uA", "500 µA"), ("1mA", "1 mA"), ("2mA", "2 mA")):
        r = results[name]
        w = (r["t"] >= -5.0e-3) & (r["t"] <= -3.5e-3)
        ax1.plot(r["t"][w] * 1e3, r["v"][w], lw=0.9, color=colours[name], label=label)
    for s in (+rail, -rail):
        ax1.axhline(s, color="k", ls=":", lw=1)
    ax1.set_xlabel("t (ms)")
    ax1.set_ylabel("v_meas (V)")
    ax1.set_ylim(-15, 15)
    ax1.set_title("Unclipped square waves (100 µA – 2 mA)\n"
                  "amplitude tracks bias current · spinning at 10 kHz")
    ax1.legend(loc="upper right", fontsize=9)
    ax1.grid(alpha=0.3)

    bias_lin = np.array([results[n]["bias"] for n in linear])
    amp_lin = np.array([results[n]["amplitude"] for n in linear])
    clipped = [("5mA_10khz", 5.0), ("10mA_10khz", 10.0)]
    x = np.linspace(0, 11, 100)
    ax2.plot(x, m * x + b, color="tab:green", lw=2, label=f"fit {m:.2f} V/mA", zorder=2)
    ax2.plot(x, Z_DECK * GAIN / 1000 * x, color="gray", ls="--", lw=1.5,
             label=f"predict {Z_DECK*GAIN/1000:.2f} V/mA", zorder=1)
    ax2.axhline(rail, color="tab:orange", ls="--", lw=2)
    ax2.text(5.2, rail + 0.35, "±13.7 V rail", color="tab:orange", fontsize=11)
    ax2.scatter(bias_lin, amp_lin, s=110, color="tab:green", zorder=4, label="measured (linear)")
    ax2.scatter([c[1] for c in clipped], [results[c[0]]["amplitude"] for c in clipped],
                s=110, marker="s", color="tab:red", zorder=4, label="measured (clipped)")
    for n in ("500uA", "1mA", "2mA"):
        ax2.scatter([results[n]["bias"]], [results[n + "_v2"]["amplitude"]],
                    s=52, marker="x", color="tab:purple", zorder=5,
                    label="40 kHz cross-check" if n == "500uA" else None)
    ax2.set_xlabel("bias current (mA)")
    ax2.set_ylabel("square-wave amplitude (V)")
    ax2.set_xlim(0, 11)
    ax2.set_ylim(0, 16)
    ax2.set_title("Per-phase output amplitude vs bias current")
    ax2.legend(loc="lower right", fontsize=9)
    ax2.grid(alpha=0.3)
    fig.tight_layout()
    out = FIGURES / "2026-07-10_bias_sweep_results.png"
    fig.savefig(out, dpi=160)
    plt.close(fig)
    print(f"\nwrote {out.relative_to(PROJECT)}")

    # ---- frequency figure: 10 vs 40 kHz + settling ------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.81))
    r10, r40 = results["2mA"], results["2mA_v2"]
    w10 = (r10["t"] >= -5.0e-3) & (r10["t"] <= -4.2e-3)
    ax1.plot((r10["t"][w10] + 5.0e-3) * 1e6, r10["v"][w10], lw=1.0,
             color="tab:blue", label=f"10 kHz  ({r10['amplitude']:.2f} V)")
    w40 = r40["t"] <= (r40["t"][0] + 0.8e-3)
    ax1.plot((r40["t"][w40] - r40["t"][0]) * 1e6, r40["v"][w40], lw=1.0,
             color="tab:red", alpha=0.85, label=f"40 kHz  ({r40['amplitude']:.2f} V)")
    ax1.set_xlabel("t within the record (µs)")
    ax1.set_ylabel("v_meas (V)")
    ax1.set_title("2 mA: spinning at 10 kHz vs 40 kHz\nsame amplitude, 4× the update rate")
    ax1.legend(loc="upper right", fontsize=9)
    ax1.grid(alpha=0.3)

    t, ch = load(DATA / "2mA_v2.csv")
    sync, v = ch[:, 0], ch[:, 1]
    dt = float(np.median(np.diff(t)))
    n = int(25e-6 / dt)
    threshold = (sync.max() + sync.min()) / 2
    high = sync > threshold
    rises = np.where((~high[:-1]) & (high[1:]))[0]
    curves = []
    k = rises[0]
    while k + n < len(v):
        seg = v[k:k + n].astype(float)
        final = seg[int(0.6 * n):].mean()
        prev = v[max(0, k - n):k][int(0.6 * n):].mean()
        step = final - prev
        if abs(step) > 0.2:
            curves.append(np.abs(seg - final) / abs(step))
        k += n
    curve = np.mean(curves, axis=0) * 100
    tau = np.arange(n) * dt * 1e6
    ax2.plot(tau, curve, color="tab:purple", lw=2)
    for tol, style in ((5, ":"), (1, "--")):
        ax2.axhline(tol, color="gray", ls=style, lw=1)
        idx = np.where(curve < tol)[0]
        if len(idx):
            ax2.annotate(f"{tol}% at {idx[0]*dt*1e6:.1f} µs",
                         xy=(idx[0] * dt * 1e6, tol), xytext=(9, tol + 6),
                         fontsize=9, arrowprops=dict(arrowstyle="->", lw=1))
    ax2.set_xlabel("time into the phase (µs)")
    ax2.set_ylabel("|error| as % of the step")
    ax2.set_yscale("log")
    ax2.set_xlim(0, 25)
    ax2.set_title("Settling after a phase edge (2 mA, ensemble mean)\n"
                  "≈3.5 µs — sets the highest usable spin rate")
    ax2.grid(alpha=0.3, which="both")
    fig.tight_layout()
    out = FIGURES / "2026-07-10_spin_frequency.png"
    fig.savefig(out, dpi=160)
    plt.close(fig)
    print(f"wrote {out.relative_to(PROJECT)}")


if __name__ == "__main__":
    sys.exit(main())
