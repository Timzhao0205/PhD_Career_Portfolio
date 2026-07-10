#!/usr/bin/env python3
# =============================================================================
# CF-3 STARTER -- Research aid -- not legal advice. SIMULATED / prophetic example.
#
# Thesis under test: for a FIXED total copper-bypass budget (same count of
# cu-interface turns), placing that copper preferentially at the turns with
# worse conduction access to the OD cold head (the inner turns, farther from
# the sink) beats a naive uniform/evenly-spaced placement on peak hot-spot
# Delta-T, under a fixed cryocooler cooling-power budget.
#
# Cheap model: reuse the CF-1 radial network (thermal_network.thermal_solve).
# Only the mat_per_turn placement pattern changes between "naive" and
# "steered" -- everything else (geometry, cooling budget, fault load) is held
# identical, isolating the placement effect.
# =============================================================================
import json
import os
import numpy as np

from thermal_network import thermal_solve, cooling_budget, GEOM

N = GEOM["N"]

ASSUMED_PARAMETERS = dict(
    q_spot_W=0.5,           # local disturbance power, same order as CF-1 (prophetic)
    spot_turn=2,            # fault near the INNER turns (worst native cooling access)
    background_material="ss",  # baseline (worst thermal) interface elsewhere
    bypass_material="cu",      # copper bypass material placed at n_cu turns
    note="illustrative, not measured; q_spot/spot_turn chosen to stress the "
         "inner/worst-cooled region where placement should matter most",
)


def naive_placement(n_cu):
    """Evenly spaced copper turns across the full radial span."""
    mat = [ASSUMED_PARAMETERS["background_material"]] * N
    if n_cu > 0:
        idx = np.linspace(0, N - 1, n_cu).round().astype(int)
        for i in set(idx.tolist()):
            mat[i] = ASSUMED_PARAMETERS["bypass_material"]
    return mat


def steered_placement(n_cu):
    """All copper budget concentrated at the innermost (worst-cooled) turns."""
    mat = [ASSUMED_PARAMETERS["background_material"]] * N
    for i in range(min(n_cu, N)):
        mat[i] = ASSUMED_PARAMETERS["bypass_material"]
    return mat


def run():
    q_spot = ASSUMED_PARAMETERS["q_spot_W"]
    spot_turn = ASSUMED_PARAMETERS["spot_turn"]

    rows = []
    for T_cold in (20.0, 30.0, 50.0):
        G_ch = cooling_budget(T_cold)
        for n_cu in (2, 4, 6, 8, 10, 12):
            naive_mat = naive_placement(n_cu)
            steer_mat = steered_placement(n_cu)

            r_naive = thermal_solve(naive_mat, q_spot=q_spot,
                                    spot_turn=spot_turn, T_cold=T_cold, G_ch=G_ch)
            r_steer = thermal_solve(steer_mat, q_spot=q_spot,
                                    spot_turn=spot_turn, T_cold=T_cold, G_ch=G_ch)

            reduction_pct = 100.0 * (r_naive["peak_dT"] - r_steer["peak_dT"]) / \
                r_naive["peak_dT"]

            rows.append(dict(
                T_cold_K=T_cold, n_cu=n_cu,
                naive_peak_dT_K=round(r_naive["peak_dT"], 4),
                steered_peak_dT_K=round(r_steer["peak_dT"], 4),
                peak_dT_reduction_pct=round(reduction_pct, 2),
                naive_cold_head_load_W=round(r_naive["cold_head_load"], 4),
                steered_cold_head_load_W=round(r_steer["cold_head_load"], 4),
            ))

    summary = dict(
        SIMULATED_prophetic=True,
        description=("Same total copper-bypass budget (n_cu turns), naive "
                     "evenly-spaced placement vs thermally-steered placement "
                     "concentrated at the inner (worst cooling-access) turns, "
                     f"fault injected at turn {spot_turn}, swept over n_cu and "
                     "cooling budget (20/30/50 K)."),
        assumed_parameters=ASSUMED_PARAMETERS,
        rows=rows,
    )

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "cf3_starter.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print(f"{'T_cold':>7} {'n_cu':>5} {'naive_dT':>10} {'steer_dT':>10} {'reduc%':>8}")
    for r in rows:
        print(f"{r['T_cold_K']:7.0f} {r['n_cu']:5d} {r['naive_peak_dT_K']:10.4f} "
             f"{r['steered_peak_dT_K']:10.4f} {r['peak_dT_reduction_pct']:8.2f}")
    print(f"\n[SIMULATED/prophetic] wrote {out}/cf3_starter.json")


if __name__ == "__main__":
    run()
