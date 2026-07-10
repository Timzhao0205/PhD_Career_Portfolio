#!/usr/bin/env python3
# =============================================================================
# CF-2 STARTER -- Research aid -- not legal advice. SIMULATED / prophetic example.
#
# Thesis under test: a quench-detection trip threshold referenced to a
# conduction-model temperature map (per-turn margin above that turn's own
# no-fault baseline) catches faults that a FIXED global threshold (calibrated
# once, e.g. at the coldest/best-cooled turn) either misses (threshold too
# loose for inner, worse-cooled turns) or false-trips (threshold too tight
# once cooling budget or turn position shifts the no-fault baseline).
#
# Cheap model: reuse the CF-1 radial conduction network (thermal_network.py).
# Build a no-fault BASELINE profile from a small uniform background loss
# (AC/resistive loss during normal operation) via linear superposition of
# thermal_solve() calls (the network is linear, so superposition is exact
# for this model). Then inject a fault-precursor heat pulse at each turn in
# turn and compare a fixed vs a locally-referenced trip rule.
# =============================================================================
import json
import os
import numpy as np

from thermal_network import thermal_solve, cooling_budget, GEOM

N = GEOM["N"]
MAT_UNIFORM = ["ss"] * N          # fixed uniform interface for this test (isolates
                                    # the detection-threshold question from CF-1's
                                    # interface-material question)

# --- assumed / parametrized (NOT measured) inputs --------------------------
ASSUMED_PARAMETERS = dict(
    q_background_W_per_turn=0.01,   # steady AC/resistive loss per turn, prophetic
    q_fault_W=0.30,                 # local quench-precursor heat pulse, prophetic
    margin_K=3.0,                   # design safety margin above local baseline
    calibration_T_cold_K=20.0,      # cooling level the FIXED threshold is set at
    note="illustrative order-of-magnitude values, not measured hardware data",
)


def baseline_profile(T_cold, G_ch, q_bg):
    """Superpose N single-turn thermal_solve() calls to get the steady
    no-fault profile under uniform background loss (linear network)."""
    T = np.full(N, T_cold)
    for turn in range(N):
        r = thermal_solve(MAT_UNIFORM, q_spot=q_bg, spot_turn=turn,
                          T_cold=T_cold, G_ch=G_ch)
        T += (r["Tprofile"] - T_cold)
    return T


def fault_profile(T_cold, G_ch, q_bg, spot_turn, q_fault):
    """Baseline + one extra fault pulse at spot_turn (superposition)."""
    base = baseline_profile(T_cold, G_ch, q_bg)
    extra = thermal_solve(MAT_UNIFORM, q_spot=q_fault, spot_turn=spot_turn,
                          T_cold=T_cold, G_ch=G_ch)
    return base + (extra["Tprofile"] - T_cold)


def run():
    q_bg = ASSUMED_PARAMETERS["q_background_W_per_turn"]
    q_fault = ASSUMED_PARAMETERS["q_fault_W"]
    margin = ASSUMED_PARAMETERS["margin_K"]
    T_cal = ASSUMED_PARAMETERS["calibration_T_cold_K"]

    # calibrate the FIXED global threshold once, at the design cooling point
    G_ch_cal = cooling_budget(T_cal)
    base_cal = baseline_profile(T_cal, G_ch_cal, q_bg)
    fixed_threshold_K = float((base_cal - T_cal).max() + margin)

    results = []
    false_trips = 0
    missed = 0
    correct = 0
    total = 0
    for T_cold in (20.0, 30.0, 50.0):
        G_ch = cooling_budget(T_cold)
        base = baseline_profile(T_cold, G_ch, q_bg)

        # false-trip check: does the FIXED threshold trip on the no-fault
        # baseline itself, once cooling level / geometry shift the gradient?
        base_dT = base - T_cold
        baseline_false_trip_turns = [int(i) for i in np.where(
            base_dT > fixed_threshold_K)[0]]
        false_trips += len(baseline_false_trip_turns)

        for spot_turn in range(N):
            total += 1
            Tf = fault_profile(T_cold, G_ch, q_bg, spot_turn, q_fault)
            fault_dT_abs = float(Tf[spot_turn] - T_cold)
            fault_dT_local = float(Tf[spot_turn] - base[spot_turn])

            fixed_trips = fault_dT_abs > fixed_threshold_K
            local_trips = fault_dT_local > margin

            if fixed_trips and not local_trips:
                verdict = "fixed_only"
            elif local_trips and not fixed_trips:
                verdict = "local_only"
                missed += 1  # fixed threshold missed a real precursor
            elif fixed_trips and local_trips:
                verdict = "both_detect"
                correct += 1
            else:
                verdict = "neither"

            results.append(dict(T_cold_K=T_cold, spot_turn=spot_turn,
                                fault_dT_abs_K=round(fault_dT_abs, 4),
                                fault_dT_local_K=round(fault_dT_local, 4),
                                fixed_trips=bool(fixed_trips),
                                local_trips=bool(local_trips),
                                verdict=verdict))

    summary = dict(
        SIMULATED_prophetic=True,
        description=("Fixed global QD threshold (calibrated once at "
                     f"{T_cal:.0f} K, value={fixed_threshold_K:.3f} K) vs a "
                     "conduction-model-local threshold (turn's own baseline + "
                     f"{margin:.1f} K margin), swept over all {N} turn "
                     "positions x 3 cooling budgets (20/30/50 K)."),
        assumed_parameters=ASSUMED_PARAMETERS,
        fixed_threshold_K=fixed_threshold_K,
        n_cases=total,
        n_baseline_false_trips_fixed=false_trips,
        n_missed_by_fixed_caught_by_local=missed,
        n_both_detect=correct,
        results=results,
    )

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "cf2_starter.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print(f"[SIMULATED/prophetic] fixed_threshold={fixed_threshold_K:.3f} K "
         f"(calibrated at {T_cal:.0f} K)")
    print(f"[SIMULATED/prophetic] baseline false-trips (fixed rule): {false_trips}")
    print(f"[SIMULATED/prophetic] fault cases missed by fixed but caught by "
         f"local-margin rule: {missed} / {total}")
    print(f"[SIMULATED/prophetic] wrote {out}/cf2_starter.json")


if __name__ == "__main__":
    run()
