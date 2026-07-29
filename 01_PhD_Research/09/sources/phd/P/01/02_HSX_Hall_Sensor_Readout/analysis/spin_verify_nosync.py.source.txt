#!/usr/bin/env python3
"""
spin_verify_nosync.py
---------------------
Verify a spinning-current emulator capture when only v_meas was recorded
(NO sync channel). Phase is reconstructed purely by folding at the known
phase rate f, so this complements hsx_demod_scope_csv.py (which needs
sync). Written for the 2026-07-08 20 kHz / 20 mA emulator run on the
Keysight DSO-X 4022A; column layout is configurable for other exports.

WHAT IT REPORTS
  - samples, sample rate, folded-cycle count
  - per-state settled medians (blanked), pedestal (amp offset * G)
  - offset staircase amplitude A (raw per-state offset at the output)
  - demodulated residual at the best phase alignment + suppression ratio
  - OPTIONAL (--arm/--par/--ibias): exact bridge nodal sim of what the
    output *should* be for the given bridge + current + gain, to flag the
    absolute-magnitude consistency (this is what surfaced the 2026-07-08
    ~100x anomaly).

USAGE
  python3 spin_verify_nosync.py data/2026-07-08_test_spin.csv --f 20000 \
      --skip-header 6 --tcol 1 --vcol 2 --arm 680 --par 2200 --ibias 0.020
"""
import argparse
import numpy as np


def load(path, skip, tcol, vcol):
    d = np.genfromtxt(path, delimiter=",", skip_header=skip, usecols=(tcol, vcol))
    t, v = d[:, 0], d[:, 1]
    m = np.isfinite(t) & np.isfinite(v)
    return t[m], v[m]


def fold_states(t, v, f, blank=0.45):
    """Fold at the 8-phase cycle (8/f) and return per-state settled medians."""
    Tp = 1.0 / f
    Tc = 8 * Tp
    tt = t - t[0]
    frac = (tt % Tp) / Tp
    cyc = np.floor(tt / Tc).astype(int)
    ph = (np.floor((tt % Tc) / Tp).astype(int)) % 8
    keep = frac > blank
    sm = np.array([np.median(v[keep & (ph == s)]) for s in range(8)])
    return sm, cyc, ph, keep, cyc.max() + 1


def analyze(t, v, f, blank=0.45):
    sm, cyc, ph, keep, ncyc = fold_states(t, v, f, blank)
    ped = sm.mean()
    # demod sign (a0==a2) and emulator offset-pattern sign, per absolute state
    dsg = np.array([1 if ((k & 1) == ((k >> 2) & 1)) else -1 for k in range(8)])
    osg = np.array([+1, -1, -1, +1, -1, +1, +1, -1])
    best = None
    for o in range(8):
        demod = np.mean(np.roll(dsg, o) * (sm - ped))
        amp = np.mean(np.roll(osg, o) * (sm - ped))
        if best is None or abs(demod) < abs(best[1]):
            best = (o, demod, amp)
    # realistic residual: per-cycle scatter (noise/quantization floor)
    per = []
    for c in range(ncyc):
        vals = np.array([np.median(v[keep & (cyc == c) & (ph == s)]) for s in range(8)])
        if np.all(np.isfinite(vals)):
            per.append(np.mean(dsg * (vals - vals.mean())))
    per = np.array(per)
    resid = max(abs(per.mean()) if len(per) else 0, per.std() if len(per) else 0)
    return dict(sm=sm, ped=ped, A=abs(best[2]), demod=best[1],
                resid=resid, ncyc=ncyc)


def bridge_out(Rarm, Rp, I, Rl=2200.0, G=100.3):
    """Exact nodal sim: bias p2->p4, sense p1/p3, 2.2k returns on p1/p3."""
    R12 = Rarm * Rp / (Rarm + Rp)
    g12, g23, g34, g41 = 1 / R12, 1 / Rarm, 1 / Rarm, 1 / Rarm
    gL = 1 / Rl
    M = np.array([[g12 + g41 + gL, -g12, 0, -g41],
                  [-g12, g12 + g23, -g23, 0],
                  [0, -g23, g23 + g34 + gL, -g34],
                  [-g41, 0, -g34, g34 + g41]])
    V = np.linalg.solve(M, np.array([0.0, I, 0.0, -I]))
    return (V[0] - V[2]) * G


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv")
    p.add_argument("--f", type=float, default=20000.0)
    p.add_argument("--skip-header", type=int, default=6)
    p.add_argument("--tcol", type=int, default=1)
    p.add_argument("--vcol", type=int, default=2)
    p.add_argument("--blank", type=float, default=0.45)
    p.add_argument("--arm", type=float, default=None, help="ring-arm ohms (enables consistency sim)")
    p.add_argument("--par", type=float, default=2200.0, help="parallel R ohms on p1-p2")
    p.add_argument("--ibias", type=float, default=0.020, help="bias current A")
    p.add_argument("--gain", type=float, default=100.3)
    a = p.parse_args()

    t, v = load(a.csv, a.skip_header, a.tcol, a.vcol)
    dt = np.median(np.diff(t))
    r = analyze(t, v, a.f, a.blank)
    print("samples %d  fs %.1f kSa/s  folded cycles %d" % (len(v), 1 / dt / 1e3, r["ncyc"]))
    print("per-state settled medians:", np.round(r["sm"], 3))
    print("pedestal (amp offset * G)      : %+.3f V" % r["ped"])
    print("offset staircase amplitude A   : %.4f V  -> plate o ~ %.2f mV" %
          (r["A"], r["A"] / (a.gain * 0.83) * 1e3))
    print("demod residual (best align)    : %.4f V mean, ~%.1f mV noise floor" %
          (r["demod"], r["resid"] * 1e3))
    supp = r["A"] / r["resid"] if r["resid"] else float("inf")
    print("offset suppression             : >=%.0fx (measurement-limited)" % supp)

    if a.arm:
        out = bridge_out(a.arm, a.par, a.ibias, G=a.gain)
        print("\n-- absolute-magnitude consistency --")
        print("predicted output for %g ohm arms + %g par + %g mA + gain %g:"
              % (a.arm, a.par, a.ibias * 1e3, a.gain))
        print("  = %.2f V  (rail is ~+/-13.5 V)" % out)
        print("measured A = %.3f V  ->  ratio %.0fx" % (r["A"], out / r["A"]))
        if out > 13.5 and r["A"] < 5:
            print("  ANOMALY: predicted would RAIL but capture is clean+small.")
            print("  With R9==R10 (no leak) & RG connected, run the dV gain check:")
            print("  static-hold one state, DMM the amp-input differential ->")
            print("    ~0.75 V => gain not ~100x ;  ~7 mV => 2.2k imbalance ineffective.")


if __name__ == "__main__":
    main()
