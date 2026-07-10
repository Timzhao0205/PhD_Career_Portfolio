#!/usr/bin/env python3
# =============================================================================
# CF-5 STARTER -- Research aid -- not legal advice. SIMULATED / prophetic example.
#
# Aviation-motor context ONLY (Hinetics CRUISE-class conduction-cooled NI field
# coils, aircraft electric-motor rotor). No "stellarator" framing anywhere.
#
# Thesis under test: a spinning conduction-cooled NI winding must reject heat
# across a rotating-to-stationary interface (rotary joint / heat-pipe / thermal
# strap) to a STATIONARY cryocooler cold head. That interface's effective
# thermal resistance is not RPM-invariant: contact-pressure loss, gap growth,
# and vibration/runout at the rotary joint degrade its conductance as RPM
# rises. Under a FIXED cold-head cooling-power budget, this predicts a
# steady-state winding-to-cold-head Delta-T that grows with RPM and can cross
# a current-sharing safety margin at some finite operating speed -- the
# rotor-speed ceiling this candidate's mitigation (compliant/redundant joint
# design) would need to push out.
#
# Cheap model: simple SERIES thermal-resistance chain,
#   winding -> [R_winding_fixed] -> rotary-joint interface -> [R_joint(RPM)]
#            -> stationary cold head (held at T_cold)
# R_joint(RPM) = R_joint0 * exp(RPM / RPM_char)   -- monotonic increase from
# contact/gap effects, a simple order-of-magnitude parametrization, NOT a
# vendor rotary-joint datasheet fit. Steady state: dT(RPM) = Q_budget *
# (R_winding_fixed + R_joint(RPM)), where Q_budget = cooling_budget(T_cold)
# reused from CF-1's thermal_network.py load-line proxy, treated here as the
# heat load the joint+cold-head chain must carry at steady operating point.
# =============================================================================
import json
import os
import numpy as np

from thermal_network import cooling_budget

ASSUMED_PARAMETERS = dict(
    R_winding_fixed_K_per_W=0.15,   # lumped winding-to-joint-interface resistance,
                                     # prophetic order-of-magnitude (NOT vendor data)
    R_joint0_K_per_W=0.30,          # static (RPM=0) rotary-joint interface resistance
    RPM_char=6000.0,                # characteristic RPM scale of joint degradation,
                                     # prophetic -- sets where the exp() growth bites
    margin_K=5.0,                   # illustrative current-sharing safety margin above
                                     # the RPM=0 baseline Delta-T (labeled as such)
    rpm_min=0.0,
    rpm_max=20000.0,
    rpm_steps=201,
    note="illustrative monotonic contact/gap-degradation curve for a rotating "
         "cryo interface, not a measured rotary-joint or heat-pipe test result",
)


def joint_resistance(rpm, p=ASSUMED_PARAMETERS):
    """Rotary-joint interface resistance, monotonic increase with RPM from
    contact-pressure loss / gap growth / runout -- prophetic parametrization."""
    return p["R_joint0_K_per_W"] * np.exp(rpm / p["RPM_char"])


def steady_state_dT(rpm, T_cold, p=ASSUMED_PARAMETERS):
    """dT = Q_budget * R_total(rpm), fixed cold-head cooling-power budget."""
    Q_budget = cooling_budget(T_cold)
    R_total = p["R_winding_fixed_K_per_W"] + joint_resistance(rpm, p)
    return Q_budget * R_total, Q_budget, R_total


def run():
    p = ASSUMED_PARAMETERS
    rpms = np.linspace(p["rpm_min"], p["rpm_max"], p["rpm_steps"])

    cooling_levels = {}
    for T_cold in (20.0, 30.0, 50.0):
        dTs = []
        R_tot = []
        for rpm in rpms:
            dT, Q_budget, R_total = steady_state_dT(rpm, T_cold, p)
            dTs.append(float(dT))
            R_tot.append(float(R_total))
        dTs = np.array(dTs)
        dT0 = float(dTs[0])
        rise = dTs - dT0
        over_idx = np.where(rise > p["margin_K"])[0]
        rpm_limit = float(rpms[over_idx[0]]) if over_idx.size else None

        cooling_levels[str(T_cold)] = dict(
            Q_budget_W=float(cooling_budget(T_cold)),
            dT_baseline_K=dT0,
            dT_max_K=float(dTs.max()),
            rpm_limit_margin_exceeded=rpm_limit,
            rpm=rpms.tolist(),
            dT_K=dTs.tolist(),
            R_total_K_per_W=R_tot,
        )
        print(f"[SIMULATED/prophetic] T_cold={T_cold:.0f} K, Q_budget="
              f"{cooling_budget(T_cold):.2f} W: dT(0 RPM)={dT0:.3f} K, "
              f"dT({p['rpm_max']:.0f} RPM)={dTs[-1]:.3f} K, "
              f"RPM at which +{p['margin_K']:.1f} K margin exceeded="
              f"{rpm_limit}")

    summary = dict(
        SIMULATED_prophetic=True,
        description=("Series thermal-resistance chain (winding -> rotary-joint "
                     "interface -> stationary cold head) with an RPM-dependent "
                     "joint resistance (exponential contact/gap-degradation "
                     "proxy), swept at 3 fixed cooling-power budgets (20/30/50 "
                     "K cold-head load lines). Reports steady-state winding "
                     "Delta-T vs RPM and the RPM at which Delta-T rises past an "
                     "illustrative current-sharing safety margin above the "
                     "RPM=0 baseline."),
        assumed_parameters=p,
        cooling_levels=cooling_levels,
    )

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "cf5_starter.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print(f"[SIMULATED/prophetic] wrote {out}/cf5_starter.json")


if __name__ == "__main__":
    run()
