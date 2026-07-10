#!/usr/bin/env python3
# =============================================================================
# CF-6 STARTER -- Research aid -- not legal advice. SIMULATED / prophetic example.
#
# Thesis under test: an NI turn-to-turn interface must hold BOTH an electrical
# contact resistance Rc AND a thermal conduction path across repeated
# cooldown/warm-up (thermal-cycling) events. A CTE-MISMATCHED interface
# (dissimilar-material layers with different thermal-contraction coefficients)
# should degrade its thermal contact FASTER with cycle count than a
# CTE-MATCHED interface, because differential contraction/expansion each cycle
# progressively opens micro-gaps / relaxes contact pressure at the interface.
# This predicts a projected peak hot-spot Delta-T that rises faster over N
# thermal cycles for a mismatched interface than a matched one at the SAME
# fixed cooling-power budget -- the reliability/lifetime evidence this
# candidate's CTE-matched-interface claim rests on.
#
# Cheap model: parametric contact-DEGRADATION-vs-cycle-count curve,
#   k_interface(N) = k_floor + (k0 - k_floor) * exp(-N / tau_cycles)
# a simple monotonic decay toward a degraded asymptote k_floor, with a
# FASTER time constant (smaller tau_cycles) and a LOWER floor for the
# CTE-mismatched case -- a prophetic, illustrative parametrization, NOT a
# measured cycling-test result. The degraded k_interface is fed back into
# thermal_network.thermal_solve() (uniform interface across all turns) at a
# fixed cold-head cooling-power budget to project peak hot-spot Delta-T rise
# over N up to 10,000 cycles for matched vs mismatched interfaces.
# =============================================================================
import json
import os
import numpy as np

from thermal_network import thermal_solve, cooling_budget, MATERIALS, GEOM

N_TURNS = GEOM["N"]

ASSUMED_PARAMETERS = dict(
    k0_W_per_mK=400.0,            # pristine (as-built, N=0) interface conductance,
                                    # anchored near the CF-1 "cu" table entry, prophetic
    k_floor_matched_W_per_mK=150.0,   # CTE-matched degraded asymptote, prophetic
    k_floor_mismatched_W_per_mK=15.0,  # CTE-mismatched degraded asymptote (order of
                                        # magnitude worse -- near the CF-1 "hast" entry)
    tau_cycles_matched=3000.0,     # slower degradation time constant, prophetic
    tau_cycles_mismatched=400.0,   # faster degradation time constant, prophetic
    rho_ct_placeholder_Ohm_m2=1e-7,  # placeholder electrical contact resistivity for
                                       # the synthetic MATERIALS entry (not used by
                                       # thermal_solve; kept only for table completeness)
    q_spot_W=0.5,
    spot_turn=20,
    n_cycles_max=10000,
    n_cycles_steps=41,
    note="illustrative exponential contact-degradation-vs-cycling parametrization, "
         "not a measured thermal-cycling test result",
)


def degraded_k(n_cycles, k_floor, tau, p=ASSUMED_PARAMETERS):
    """Monotonic exponential approach from pristine k0 down to k_floor as
    thermal-cycle count grows -- prophetic degradation proxy."""
    return k_floor + (p["k0_W_per_mK"] - k_floor) * np.exp(-n_cycles / tau)


def peak_dT_at_cycles(n_cycles, k_floor, tau, T_cold, G_ch, p=ASSUMED_PARAMETERS):
    """Inject the degraded k as a synthetic uniform-interface material into the
    CF-1 MATERIALS table, then reuse thermal_solve() unmodified."""
    k = float(degraded_k(n_cycles, k_floor, tau, p))
    key = f"_cf6_deg_{n_cycles}_{k_floor}"
    MATERIALS[key] = dict(k=k, rho_ct=p["rho_ct_placeholder_Ohm_m2"])
    th = thermal_solve([key] * N_TURNS, q_spot=p["q_spot_W"],
                       spot_turn=p["spot_turn"], T_cold=T_cold, G_ch=G_ch)
    del MATERIALS[key]
    return th["peak_dT"], k


def run():
    p = ASSUMED_PARAMETERS
    cycles = np.linspace(0, p["n_cycles_max"], p["n_cycles_steps"])

    cooling_levels = {}
    for T_cold in (20.0, 30.0, 50.0):
        G_ch = cooling_budget(T_cold)
        rows_matched = []
        rows_mismatched = []
        for n in cycles:
            dT_m, k_m = peak_dT_at_cycles(n, p["k_floor_matched_W_per_mK"],
                                          p["tau_cycles_matched"], T_cold, G_ch, p)
            dT_mm, k_mm = peak_dT_at_cycles(n, p["k_floor_mismatched_W_per_mK"],
                                            p["tau_cycles_mismatched"], T_cold, G_ch, p)
            rows_matched.append(dict(n_cycles=float(n), k_W_per_mK=k_m,
                                     peak_dT_K=float(dT_m)))
            rows_mismatched.append(dict(n_cycles=float(n), k_W_per_mK=k_mm,
                                        peak_dT_K=float(dT_mm)))

        dT0 = rows_matched[0]["peak_dT_K"]  # both start at same pristine k0
        rise_matched = rows_matched[-1]["peak_dT_K"] - dT0
        rise_mismatched = rows_mismatched[-1]["peak_dT_K"] - dT0

        cooling_levels[str(T_cold)] = dict(
            G_ch_W_per_K=float(G_ch),
            peak_dT_baseline_K=float(dT0),
            matched=rows_matched,
            mismatched=rows_mismatched,
            peak_dT_rise_matched_K=float(rise_matched),
            peak_dT_rise_mismatched_K=float(rise_mismatched),
        )
        print(f"[SIMULATED/prophetic] T_cold={T_cold:.0f} K, G_ch={G_ch:.2f} W/K: "
              f"baseline peak_dT={dT0:.4f} K; after {p['n_cycles_max']} cycles "
              f"matched peak_dT rise={rise_matched:.4f} K, "
              f"mismatched peak_dT rise={rise_mismatched:.4f} K")

    summary = dict(
        SIMULATED_prophetic=True,
        description=("Projected peak hot-spot Delta-T over thermal-cycle count "
                     "(N up to 10,000) for a CTE-matched vs CTE-mismatched NI "
                     "turn-to-turn interface, using an exponential contact-"
                     "degradation-vs-cycling proxy fed back into CF-1's "
                     "thermal_solve() radial conduction network, at 3 fixed "
                     "cold-head cooling-power budgets (20/30/50 K)."),
        assumed_parameters=p,
        cooling_levels=cooling_levels,
    )

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "cf6_starter.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print(f"[SIMULATED/prophetic] wrote {out}/cf6_starter.json")


if __name__ == "__main__":
    run()
