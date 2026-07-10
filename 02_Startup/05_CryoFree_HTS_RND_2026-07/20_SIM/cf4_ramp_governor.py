#!/usr/bin/env python3
# =============================================================================
# CF-4 STARTER -- Research aid -- not legal advice. SIMULATED / prophetic example.
#
# Thesis under test: bounding coil ramp rate to a STATIC worst-case cooling
# headroom (set once, for the worst instant of a time-varying cryocooler
# headroom curve) is always safe but needlessly slow; a governor that
# throttles to the INSTANTANEOUS measured headroom recovers most of that lost
# time while remaining safe, whereas a naive FIXED-nominal rate (picked from
# average/typical headroom, not the worst case) risks headroom violations.
#
# Cheap model: q_ramp(rate) ~ k_ramp * rate^2 (AC/eddy ramp-loss scaling with
# dI/dt, a standard quadratic proxy -- prophetic/order-of-magnitude, not a
# vendor-fit). headroom(t) is a duty-cycling cryocooler recovering from a
# prior transient dip (exponential recovery + small sinusoidal ripple).
# Compare total time to reach a normalized ramp target D_target=1.0 for:
#   (a) static worst-case rate  r_wc  = sqrt(min(headroom)/k_ramp)   [safe]
#   (b) naive fixed-nominal rate r_nom = sqrt(mean(headroom)/k_ramp) [risky]
#   (c) dynamic governor: r(t) = sqrt(headroom(t)/k_ramp) each step   [safe, fast]
# =============================================================================
import json
import os
import numpy as np

ASSUMED_PARAMETERS = dict(
    k_ramp_W_per_rate2=1.2,      # ramp-loss coefficient, q=k*rate^2, prophetic
                                  # (rate in normalized A/s units; chosen so
                                  # static ramp time spans several recovery
                                  # time-constants below, not physically fit)
    headroom_nominal_W=4.0,      # nominal cold-head lift budget (~30 K anchor)
    headroom_dip_W=2.5,          # depth of prior-transient headroom dip, prophetic
    recover_tau_s=40.0,          # exponential recovery time constant, prophetic
    ripple_amp_W=0.3,            # small duty-cycle ripple amplitude, prophetic
    ripple_period_s=12.0,        # duty-cycle ripple period, prophetic
    D_target=150.0,              # normalized ramp distance (rate integrated over time)
    dt_s=0.1,
    horizon_s=400.0,
    note="illustrative headroom curve shape (transient-recovery + duty ripple), "
         "not a vendor load-line measurement",
)


def headroom(t, p=ASSUMED_PARAMETERS):
    base = p["headroom_nominal_W"] - p["headroom_dip_W"] * np.exp(-t / p["recover_tau_s"])
    ripple = p["ripple_amp_W"] * np.sin(2 * np.pi * t / p["ripple_period_s"])
    return np.maximum(base + ripple, 0.05)


def run():
    p = ASSUMED_PARAMETERS
    ts = np.arange(0.0, p["horizon_s"], p["dt_s"])
    hd = headroom(ts, p)
    k = p["k_ramp_W_per_rate2"]

    r_wc = np.sqrt(hd.min() / k)          # static, calibrated to worst instant
    r_nom = np.sqrt(hd.mean() / k)        # naive fixed-nominal (NOT worst-case)

    def integrate_static(rate):
        progress = np.cumsum(np.full_like(ts, rate) * p["dt_s"])
        idx = np.searchsorted(progress, p["D_target"])
        if idx >= len(ts):
            return None, 0
        req_power = k * rate ** 2
        violations = int(np.sum(req_power > hd[:idx + 1] * 1.0000001))
        return float(ts[idx]), violations

    t_wc, viol_wc = integrate_static(r_wc)
    t_nom, viol_nom = integrate_static(r_nom)

    # dynamic governor: throttle to instantaneous headroom each step
    progress = 0.0
    viol_dyn = 0
    t_dyn = None
    for i, t in enumerate(ts):
        r_dyn = np.sqrt(hd[i] / k)
        progress += r_dyn * p["dt_s"]
        # by construction q_ramp == hd[i] exactly -> zero violation margin;
        # count only true overshoot from discretization noise
        if k * r_dyn ** 2 > hd[i] * 1.0000001:
            viol_dyn += 1
        if progress >= p["D_target"]:
            t_dyn = float(t)
            break

    summary = dict(
        SIMULATED_prophetic=True,
        description=("Static worst-case-limited ramp rate vs a naive fixed-"
                     "nominal rate vs a dynamic instantaneous-headroom "
                     "governor, over a duty-cycling/recovering cryocooler "
                     "headroom curve. Reports total ramp time and headroom-"
                     "violation counts for each strategy."),
        assumed_parameters=p,
        headroom_min_W=float(hd.min()),
        headroom_mean_W=float(hd.mean()),
        static_worst_case=dict(rate=float(r_wc), ramp_time_s=t_wc,
                               violations=viol_wc),
        naive_fixed_nominal=dict(rate=float(r_nom), ramp_time_s=t_nom,
                                 violations=viol_nom),
        dynamic_governor=dict(ramp_time_s=t_dyn, violations=viol_dyn),
        time_saved_vs_static_pct=(
            round(100.0 * (t_wc - t_dyn) / t_wc, 2)
            if (t_wc and t_dyn) else None),
    )

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "cf4_starter.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print(f"[SIMULATED/prophetic] static worst-case: rate={r_wc:.4f}, "
         f"ramp_time={t_wc}, violations={viol_wc}")
    print(f"[SIMULATED/prophetic] naive fixed-nominal: rate={r_nom:.4f}, "
         f"ramp_time={t_nom}, violations={viol_nom}")
    print(f"[SIMULATED/prophetic] dynamic governor: ramp_time={t_dyn}, "
         f"violations={viol_dyn}")
    print(f"[SIMULATED/prophetic] wrote {out}/cf4_starter.json")


if __name__ == "__main__":
    run()
