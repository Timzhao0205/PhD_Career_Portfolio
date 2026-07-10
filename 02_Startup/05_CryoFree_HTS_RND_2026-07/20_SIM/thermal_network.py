#!/usr/bin/env python3
# =============================================================================
# CF-1 STARTER -- coupled electro-thermal network for a CRYOGEN-FREE NI coil.
#
# Research aid -- not legal advice. Outputs are SIMULATIONS (prophetic examples):
# present tense, labeled, never blended with measured data.
#
# Thesis under test: in a conduction-cooled (no bath) NI pancake, the turn-to-turn
# interface material sets BOTH the contact resistance Rc (electrical bypass) AND the
# radial thermal drain to the cold head. These conflict: high-Rc interfaces (good for
# charging/field-quality control) are poor thermal conductors (bad for hot-spot margin
# under limited cooling power). This script quantifies that conflict and searches for a
# SPATIAL interface map that beats any uniform interface on the
# (charging-delay vs peak-hotspot-DeltaT vs cooling-power) trade -- the Pareto evidence
# that anchors non-obviousness.
#
# Model (deliberately cheap, extend as needed):
#   * Electrical: reuse the NI loop-network tau = L/Rc scaling (import if available).
#   * Thermal: 1-D radial nodal network, one node per turn, radial thermal resistors
#     R_th(turn) = pitch / (k_interface(turn) * A_face(turn)); outermost turn tied to a
#     cold-head node held at T_cold via a finite cold-head conductance G_ch limited by
#     the cryocooler load-line (fixed lift budget Q_budget). A local disturbance power
#     q_spot is injected at one turn; steady state gives the hot-spot Delta-T and the
#     total load the cold head must lift.
#
# This is a STARTER: the mission's W2 extends it (axial stack, AC-loss maps, motor
# duty). Keep the coupling honest -- k_interface and Rc are two responses of ONE
# material/pressure choice; a real map cannot set them independently, so the sweep
# ties them through a small material table.
# =============================================================================
import json
import os
import numpy as np

# --- material table: (name, k_th @~30 K [W/m/K], rho_ct [Ohm.m^2]) ----------
# Rc and k move TOGETHER by material: metal-insulation stainless => high Rc, low k;
# copper co-wind => low Rc, high k. This coupling is the whole point.
MATERIALS = {
    "cu":    dict(k=400.0, rho_ct=5e-9),    # copper co-wind: great heat path, low Rc
    "brass": dict(k=120.0, rho_ct=2e-8),
    "hast":  dict(k=9.0,   rho_ct=7e-7),    # bare Hastelloy-ish NI contact
    "ss":    dict(k=3.0,   rho_ct=2e-6),    # stainless MI: high Rc, poor heat path
}

GEOM = dict(N=30, r_in=30e-3, pitch=0.11e-3, tape_t=0.1e-3, w=4e-3)


def geometry(g=GEOM):
    r = g["r_in"] + g["pitch"] * np.arange(g["N"])
    A_face = 2 * np.pi * r * g["tape_t"]          # radial conduction cross-section
    return r, A_face


def thermal_solve(mat_per_turn, q_spot=0.5, spot_turn=20, T_cold=20.0,
                  G_ch=0.5, g=GEOM):
    """Steady 1-D radial heat flow to an OD cold-head node.

    mat_per_turn : list[str] length N of material keys (interface at each turn)
    q_spot [W]   : local disturbance power injected at spot_turn
    G_ch [W/K]   : cold-head conductance (outer turn <-> T_cold sink)
    Returns dict with peak Delta-T above T_cold and the cold-head load.
    """
    r, A_face = geometry(g)
    N = g["N"]
    k = np.array([MATERIALS[m]["k"] for m in mat_per_turn])
    # radial resistor between turn i and i+1 uses the worse-conducting of the pair
    Rth = np.zeros(N - 1)
    for i in range(N - 1):
        ki = min(k[i], k[i + 1])
        Rth[i] = g["pitch"] / (ki * A_face[i])
    # nodal conductance matrix (turns 0..N-1), plus cold head tied to turn N-1
    G = np.zeros((N, N))
    for i in range(N - 1):
        c = 1.0 / Rth[i]
        G[i, i] += c; G[i + 1, i + 1] += c
        G[i, i + 1] -= c; G[i + 1, i] -= c
    G[N - 1, N - 1] += G_ch                    # cold-head link at OD
    q = np.zeros(N); q[spot_turn] = q_spot
    q[N - 1] += G_ch * T_cold                  # sink boundary
    T = np.linalg.solve(G, q)
    load = G_ch * (T[N - 1] - T_cold)          # power delivered to cold head
    return dict(peak_dT=float(T.max() - T_cold), Tprofile=T,
                cold_head_load=float(load))


def electrical_tau(mat_per_turn, g=GEOM):
    """Cheap proxy: whole-coil charging tau ~ L / R_char, R_char = series sum of
    per-interface radial resistances (K parallel sectors folded into rho_ct/area).
    Uses the SAME material choice as the thermal solve -> honest coupling."""
    r, _ = geometry(g)
    r_int = r[:-1] + g["pitch"] / 2
    R_char = 0.0
    for i in range(g["N"] - 1):
        rho = MATERIALS[mat_per_turn[i]]["rho_ct"]
        R_char += rho / (2 * np.pi * r_int[i] * g["w"])
    L = 1.09e-4                                 # from the validated ID_09 pancake
    return L / R_char, R_char


# --- G-PHYS note (W2 fix of the W0/W1-flagged known issue) -----------------
# The W0 starter's demo() print narrative claimed "uniform stainless gives
# LONG tau (high Rc)" while the coupled formula (tau = L/R_char, R_char =
# series sum of rho_ct/(2*pi*r*w)) always computes the OPPOSITE direction:
# higher rho_ct -> higher R_char -> LOWER tau = L/R_char. That printed
# narrative was the inverted tau<->Rc coupling flagged for G-PHYS -- the
# formula direction itself is the textbook NI-coil result (Hahn et al.: raising
# interface resistivity is exactly how metal-insulation (MI) coils SHORTEN
# charging delay relative to bare-copper-contact NI coils), so the fix here is
# to correct the narrative/labels to match the formula, not to flip the
# formula. G-PHYS (W3) must independently confirm this direction against the
# cited NI/MI literature before any filing reliance.
KNOWN_ISSUES = [
    dict(id="tau_rc_narrative_direction",
         status="FIXED_W2",
         description=("W0 demo() print text asserted uniform stainless (high "
                      "rho_ct) gives the LONGEST tau, but the coupled formula "
                      "always produced the shortest tau for stainless and the "
                      "longest for copper -- the narrative contradicted its own "
                      "printed numbers. Fixed: narrative now matches computed "
                      "direction (higher Rc -> shorter charging tau, consistent "
                      "with published metal-insulation/NI charging-delay results). "
                      "G-PHYS must independently verify this direction before "
                      "filing reliance -- a self-consistent fix is not proof of "
                      "correctness."))
]


def cooling_budget(T_cold):
    """Cryocooler load-line: rough two-stage-GM-class lift budget [W] at the
    fixed cold-head temperature operating points the mission specifies.
    Prophetic / order-of-magnitude only -- not a vendor datasheet fit."""
    # coarse monotonic points bracketing common small conduction-cooled HTS
    # magnet cryocoolers; interpolated for anything between the anchors.
    anchors = {20.0: 1.0, 30.0: 4.0, 50.0: 20.0}
    if T_cold in anchors:
        return anchors[T_cold]
    xs = sorted(anchors)
    return float(np.interp(T_cold, xs, [anchors[x] for x in xs]))


def spatial_sweep(g=GEOM, q_spot=0.5, spot_turn=20, T_cold=20.0):
    """Sweep the boundary position of an inner-ss/outer-cu spatial map against
    uniform baselines, at a fixed cold-head cooling-power budget, to search for
    a Pareto improvement over any uniform interface -- the CF-1 non-obviousness
    evidence target (charging-delay vs peak-hotspot-dT vs cooling-W)."""
    N = g["N"]
    G_ch = cooling_budget(T_cold)
    rows = []
    for m in ("cu", "brass", "hast", "ss"):
        th = thermal_solve([m] * N, q_spot=q_spot, spot_turn=spot_turn,
                           T_cold=T_cold, G_ch=G_ch, g=g)
        tau, Rc = electrical_tau([m] * N, g=g)
        rows.append(dict(map=f"uniform:{m}", n_cu_drain=0,
                         tau_s=round(tau, 4), peak_dT_K=round(th["peak_dT"], 4),
                         cold_head_load_W=round(th["cold_head_load"], 4)))
    for n_cu in (2, 4, 6, 8, 10, 12):
        smap = ["ss"] * (N - n_cu) + ["cu"] * n_cu
        th = thermal_solve(smap, q_spot=q_spot, spot_turn=spot_turn,
                           T_cold=T_cold, G_ch=G_ch, g=g)
        tau, Rc = electrical_tau(smap, g=g)
        rows.append(dict(map=f"spatial:ss-core/cu-drain[{n_cu}]", n_cu_drain=n_cu,
                         tau_s=round(tau, 4), peak_dT_K=round(th["peak_dT"], 4),
                         cold_head_load_W=round(th["cold_head_load"], 4)))
    return rows, G_ch


def pareto_front(rows):
    """Non-dominated set on (tau_s, peak_dT_K) -- lower is better on both axes."""
    front = []
    for r in rows:
        dominated = any(
            (o["tau_s"] <= r["tau_s"] and o["peak_dT_K"] <= r["peak_dT_K"]
             and (o["tau_s"] < r["tau_s"] or o["peak_dT_K"] < r["peak_dT_K"]))
            for o in rows if o is not r)
        if not dominated:
            front.append(r["map"])
    return front


def demo():
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out, exist_ok=True)
    N = GEOM["N"]

    print(f"{'interface map':30s} {'tau[s]':>8} {'peakDT[K]':>10} {'coldload[W]':>12}")
    all_cooling_levels = {}
    for T_cold in (20.0, 30.0, 50.0):
        rows, G_ch = spatial_sweep(T_cold=T_cold)
        front = pareto_front(rows)
        for r in rows:
            r["on_pareto_front"] = r["map"] in front
        print(f"\n-- T_cold={T_cold:.0f} K, cold-head budget G_ch={G_ch:.2f} W/K --")
        for r in rows:
            flag = " *" if r["on_pareto_front"] else ""
            print(f"{r['map']:30s} {r['tau_s']:8.4f} {r['peak_dT_K']:10.4f} "
                  f"{r['cold_head_load_W']:12.4f}{flag}")
        all_cooling_levels[str(T_cold)] = dict(G_ch_W_per_K=G_ch, rows=rows,
                                                pareto_front=front)

    print("\n[SIMULATED / prophetic] Read: higher interface resistivity (rho_ct) "
          "SHORTENS charging tau but WORSENS peak hot-spot dT under fixed cooling "
          "power -- the Rc<->thermal conflict. A spatial ss-core/cu-drain map can "
          "sit on the Pareto front between the uniform-ss and uniform-cu extremes "
          "at every tested cold-head budget; '*' marks non-dominated rows. This is "
          "the non-obviousness evidence target for G-NOVEL/G-CLAIM, not a measured "
          "result.")

    with open(os.path.join(out, "cf1_starter.json"), "w") as f:
        json.dump(dict(materials=MATERIALS, geom=GEOM,
                       KNOWN_ISSUES=KNOWN_ISSUES,
                       cooling_levels=all_cooling_levels), f, indent=2)
    print(f"\n[SIMULATED / prophetic] wrote {out}/cf1_starter.json")


if __name__ == "__main__":
    demo()
