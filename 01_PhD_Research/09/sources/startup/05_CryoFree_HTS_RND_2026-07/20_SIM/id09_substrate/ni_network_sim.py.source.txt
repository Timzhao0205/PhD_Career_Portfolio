#!/usr/bin/env python3
# =============================================================================
# ID_09 Phase A -- SIMULATION PACKAGE (prophetic examples for the provisional)
#
# Research aid -- not legal advice. All results produced by this script are
# SIMULATIONS. In the provisional they must be written in PRESENT/FUTURE tense
# and explicitly identified as simulated (prophetic) examples. Never blend
# with measured HIL-bench data in a single figure or example.
#
# Evidence protocol: run on personal hardware only; commit to the private
# personal repo with dated messages; no Stanford compute, storage, or email.
# Sensor model is generic Hall (GaAs-datasheet-class behavioral parameters).
# Binding constraints honored: no GaN anywhere; single coil only (no
# inter-coil comparison); no in-winding fiber; no transformer language.
# =============================================================================
#
# WHAT THIS MODELS
# ----------------
# A no-insulation (NI) REBCO pancake coil as a 2-D resistive-inductive network:
#   * N_TURNS concentric turns x K_SECTORS azimuthal sectors.
#   * Azimuthal branches: mutually coupled inductances (Maxwell coaxial-loop
#     formula, uniformly partitioned per sector) in series with a
#     time-varying superconductor/normal-zone resistance R_sc(t).
#   * Radial branches: turn-to-turn contact resistors R_r derived from the
#     contact resistivity rho_ct (default 70 uOhm.cm^2, MIT-canonical class).
#   * Fundamental-loop (chord) formulation: the spiral is the spanning tree;
#     each radial resistor closes exactly one loop spanning K consecutive
#     azimuthal segments. KVL gives
#         (L_loop/dt + C_az^T R_sc C_az + diag(R_r)) x+ =
#              (L_loop/dt) x  -  C_az^T (R_sc*1) I_t+  -  W dI_t/dt
#     solved by implicit (backward) Euler; the factorization is refreshed
#     only when R_sc changes (rank-K updates make that cheap).
#
# OUTPUTS (per scenario, into ./out/):
#   S*.npz   time series: terminal V, compensated tap estimate, per-sensor Bz,
#            azimuthal harmonic magnitudes |c1|,|c2|, normal-zone resistance.
#   S*.png   summary plots (labeled SIMULATED).
#   summary.json  headline numbers: tau validation, per-scenario first-crossing
#            times for the tap channel and the Hall-asymmetry channel.
#
# SCENARIOS (mirror ID_09 section 7 test matrix)
#   S0  charging-delay validation: fitted tau vs L_coil / R_char.
#   S1  cell (i)   fast local quench      -> tap crosses first, Hall confirms.
#   S2  cell (ii)  false-positive battery -> tap crossings w/o redistribution.
#   S3  cell (iii) slow bypass-dominated  -> Hall asymmetry arms while the tap
#                  stays below threshold ("tap-quiet window"); look-back data.
#   S4  cell (iv)  self-test stimuli      -> known injections for the fusion
#                  state machine to measure per-channel latency against.
#
# The fusion logic itself (arm/confirm, look-back, rated latency, degraded
# modes) lives in fusion_state_machine.py, which consumes these NPZ files.
# =============================================================================

import json
import os
from dataclasses import dataclass, field

import numpy as np
from scipy.linalg import lu_factor, lu_solve
from scipy.special import ellipe, ellipk

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

MU0 = 4e-7 * np.pi
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------
@dataclass
class Config:
    # --- coil geometry (small single NI pancake, E1-class) ---
    n_turns: int = 30
    k_sectors: int = 16
    r_in: float = 30e-3            # innermost turn radius [m]
    pitch: float = 0.11e-3         # radial build per turn (tape+contact) [m]
    tape_w: float = 4e-3           # tape width [m]
    gmd: float = 0.2235 * (4e-3 + 0.1e-3)   # rect. cross-section GMD [m]

    # --- electrical ---
    rho_ct: float = 70e-6 * 1e-4   # contact resistivity [Ohm.m^2] (70 uOhm.cm^2)
    r_prime_normal: float = 15e-3  # normal-zone resistance per length @77K [Ohm/m]
    leak_L_per_seg: float = 5e-9   # per-segment leakage self-L regularizer [H]

    # --- operation ---
    i_op: float = 120.0            # operating current [A]
    ramp_rate: float = 20.0        # [A/s]
    dt: float = 1e-3               # solver step [s]
    dt_nz: float = 10e-3           # normal-zone update / refactor interval [s]

    # --- tap channel model ---
    comp_err: float = 0.01         # residual inductive-compensation error
    tap_noise: float = 3e-6        # tap-channel noise, rms [V]
    tap_thresh: float = 5e-3       # instrument tap trip threshold [V]
    #   5 mV = generous margin over the chopper-AFE noise floor while still
    #   realistic against mV-class ramp/flux-jump artifacts (S2 exercises
    #   25-30 mV disturbances). Threshold is a per-deployment configurable;
    #   the "tap-quiet window" in S3 is a network effect (radial bypass),
    #   not an artifact of a deaf threshold.

    # --- Hall array model (generic Hall dies, GaAs-datasheet-class) ---
    n_sensors: int = 16
    sensor_r: float = 37e-3        # ring radius [m] (3.7 mm off outer turn)
    sensor_z: float = 3e-3         # above midplane [m] (1 mm over tape edge)
    sensor_phi0: float = np.deg2rad(11.25)  # offset from sector boundaries
    hall_noise: float = 5e-6       # per-sample Bz noise, rms [T] @ 1 kS/s
    hall_sigma_mult: float = 6.0   # arm threshold = baseline + 6 sigma on |c1|

    # --- self-test stimulus levels (S4) ---
    pilot_tap: float = 15e-6       # injected tap pilot amplitude [V]
    stim_hall: float = 50e-6       # stimulus-conductor field step at one die [T]

    seed: int = 20260705


# ----------------------------------------------------------------------------
# Inductance helpers
# ----------------------------------------------------------------------------
def mutual_coaxial(a: float, b: float, d: float = 0.0) -> float:
    """Maxwell mutual inductance of coaxial circular filaments [H]."""
    m = 4.0 * a * b / ((a + b) ** 2 + d ** 2)
    k = np.sqrt(m)
    return MU0 * np.sqrt(a * b) * ((2.0 / k - k) * ellipk(m) - (2.0 / k) * ellipe(m))


def self_loop(r: float, gmd: float) -> float:
    """Self-inductance of a circular loop of tape (GMD approximation) [H]."""
    return MU0 * r * (np.log(8.0 * r / gmd) - 2.0)


# ----------------------------------------------------------------------------
# Network model
# ----------------------------------------------------------------------------
class NIPancake:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        N, K = cfg.n_turns, cfg.k_sectors
        self.N, self.K = N, K
        self.n_az = N * K
        self.n_loop = (N - 1) * K

        # turn radii and per-segment arc geometry
        self.r_turn = cfg.r_in + cfg.pitch * np.arange(N)
        self.seg_len = np.repeat(self.r_turn, K) * (2 * np.pi / K)   # [n_az]
        self.s_end = np.cumsum(self.seg_len)          # spiral coordinate, seg end
        self.s_start = self.s_end - self.seg_len
        self.tape_len = self.s_end[-1]

        # ---- turn-level inductance matrix (Maxwell, filament-averaged) ----
        # Each 4 mm-wide tape turn is subdivided into n_f axial filaments at
        # fixed radius; mutuals use the coaxial-loop formula with axial
        # offset, and same-filament terms use the loop self-inductance with
        # the filament GMD. This keeps self and mutual terms mutually
        # consistent (naive GMD-self + zero-offset filament mutuals is
        # indefinite at 0.11 mm spacing under a 4 mm width).
        n_f = 7
        z_f = (np.arange(n_f) - (n_f - 1) / 2) * (cfg.tape_w / n_f)
        gmd_f = 0.2235 * (cfg.tape_w / n_f + 0.1e-3)
        M_turn = np.empty((N, N))
        for i in range(N):
            for j in range(i, N):
                acc = 0.0
                for za in z_f:
                    for zb in z_f:
                        if i == j and za == zb:
                            acc += self_loop(self.r_turn[i], gmd_f)
                        else:
                            acc += mutual_coaxial(self.r_turn[i],
                                                  self.r_turn[j], za - zb)
                M_turn[i, j] = M_turn[j, i] = acc / n_f ** 2
        self.M_turn = M_turn
        self.L_coil = M_turn.sum()

        # segment-level: uniform partition + leakage regularizer.
        # M_az[(n,k),(n',k')] = M_turn[n,n'] / K^2 reproduces turn-level
        # energetics for azimuthally uniform currents (the dominant NI
        # physics); leak_L restores a small, physical self-term so purely
        # azimuthal redistribution modes are not inductance-free.
        self.M_az = np.kron(M_turn, np.ones((K, K))) / K ** 2
        self.M_az[np.diag_indices(self.n_az)] += cfg.leak_L_per_seg

        # ---- fundamental loops: loop l=(n,k) covers az segments
        #      s in [n*K+k, (n+1)*K+k-1] and radial resistor (n,k) ----
        C = np.zeros((self.n_az, self.n_loop))
        for n in range(N - 1):
            for k in range(K):
                l = n * K + k
                C[n * K + k: (n + 1) * K + k, l] = 1.0
        self.C = C

        # radial contact resistor per loop (interface between turn n, n+1)
        r_int = cfg.r_in + cfg.pitch * (np.arange(N - 1) + 1.0)
        area = cfg.tape_w * (np.repeat(r_int, K) * (2 * np.pi / K))
        self.R_rl = cfg.rho_ct / area                 # [n_loop]
        # characteristic (whole-coil) radial resistance: series sum over
        # interfaces of the K parallel sector resistors
        self.R_char = float(np.sum(cfg.rho_ct / (2 * np.pi * r_int * cfg.tape_w)))

        # loop inductance and ramp-coupling vector
        self.L_loop = C.T @ self.M_az @ C
        self.W = C.T @ (self.M_az @ np.ones(self.n_az))

        # cache of loops touching each segment (for rank-1 A updates)
        self._seg_loops = [np.nonzero(C[s, :])[0] for s in range(self.n_az)]

        # ---- Biot-Savart geometry matrix G: Bz at sensors per unit segment
        #      current (8 sub-elements per arc) ----
        self.sensors = self._sensor_positions()
        self.G = self._field_matrix(self.sensors)          # [n_sens, n_az]
        self.G_center = self._field_matrix(np.array([[0.0, 0.0, 0.0]]))[0]

    # -- geometry --------------------------------------------------------
    def _sensor_positions(self):
        c = self.cfg
        phi = c.sensor_phi0 + 2 * np.pi * np.arange(c.n_sensors) / c.n_sensors
        return np.stack([c.sensor_r * np.cos(phi),
                         c.sensor_r * np.sin(phi),
                         np.full(c.n_sensors, c.sensor_z)], axis=1)

    def _field_matrix(self, pts, nsub: int = 8):
        K = self.K
        G = np.zeros((len(pts), self.n_az))
        for s in range(self.n_az):
            n, k = divmod(s, K)
            r = self.r_turn[n]
            ph = 2 * np.pi * (k + (np.arange(nsub) + 0.5) / nsub) / K
            dphi = 2 * np.pi / (K * nsub)
            xyz = np.stack([r * np.cos(ph), r * np.sin(ph),
                            np.zeros(nsub)], axis=1)
            dl = np.stack([-np.sin(ph), np.cos(ph),
                           np.zeros(nsub)], axis=1) * (r * dphi)
            for p in range(len(pts)):
                rv = pts[p][None, :] - xyz
                d3 = (np.einsum("ij,ij->i", rv, rv)) ** 1.5
                cross_z = dl[:, 0] * rv[:, 1] - dl[:, 1] * rv[:, 0]
                G[p, s] += 1e-7 * np.sum(cross_z / d3)
        return G

    # -- normal zone ------------------------------------------------------
    def nz_resistance(self, t, ignite_t, s0, v, r_prime, l0=0.0):
        """Per-segment normal resistance for a zone growing at +-v from s0.

        l0 = initial hotspot length at ignition [m] (defect/hotspot class).
        """
        R = np.zeros(self.n_az)
        if ignite_t is None or t < ignite_t:
            return R, 0.0
        half = 0.5 * l0 + v * (t - ignite_t)
        lo, hi = max(0.0, s0 - half), min(self.tape_len, s0 + half)
        if hi <= lo:
            return R, 0.0
        ov = np.clip(np.minimum(self.s_end, hi) - np.maximum(self.s_start, lo),
                     0.0, None)
        R = r_prime * ov
        return R, float(R.sum())

    # -- solver -----------------------------------------------------------
    def run(self, T, i_of_t, di_of_t, nz=None, lead=None, label=""):
        """Backward-Euler transient.

        nz   = dict(ignite_t, s0, v, r_prime[, l0]) -- winding normal zone
               (inside the radial-bypass network).
        lead = dict(ignite_t, v, r_prime[, l0])     -- joint/lead normal zone
               in SERIES with the winding, outside the bypass network; its
               resistance appears directly at the terminals.
        """
        c = self.cfg
        nt = int(round(T / c.dt))
        x = np.zeros(self.n_loop)
        R_sc = np.zeros(self.n_az)

        A_base = (self.L_loop / c.dt) + np.diag(self.R_rl)
        A = A_base.copy()
        lu = lu_factor(A)
        next_nz_update = 0.0

        rec = {k: np.empty(nt) for k in
               ("t", "I", "V_term", "R_nz", "R_lead")}
        rec["Bz"] = np.empty((nt, c.n_sensors))
        rec["B_center"] = np.empty(nt)

        for it in range(nt):
            t = (it + 1) * c.dt
            I, dI = i_of_t(t), di_of_t(t)

            if nz is not None and t >= next_nz_update:
                R_new, _ = self.nz_resistance(t, nz["ignite_t"], nz["s0"],
                                              nz["v"], nz["r_prime"],
                                              nz.get("l0", 0.0))
                dRs = R_new - R_sc
                changed = np.nonzero(np.abs(dRs) > 0)[0]
                if changed.size:
                    for s in changed:                 # cheap rank-1 updates
                        idx = self._seg_loops[s]
                        A[np.ix_(idx, idx)] += dRs[s]
                    R_sc = R_new
                    lu = lu_factor(A)
                next_nz_update = t + c.dt_nz

            R_ld = 0.0
            if lead is not None and t >= lead["ignite_t"]:
                R_ld = lead["r_prime"] * (lead.get("l0", 0.0)
                                          + lead["v"] * (t - lead["ignite_t"]))

            b = (self.L_loop @ x) / c.dt - (self.C.T @ R_sc) * I - self.W * dI
            x_new = lu_solve(lu, b)
            dx = (x_new - x) / c.dt
            x = x_new

            I_az = I + self.C @ x
            dI_az = dI + self.C @ dx
            v_az = self.M_az @ dI_az + R_sc * I_az

            rec["t"][it] = t
            rec["I"][it] = I
            rec["V_term"][it] = v_az.sum() + R_ld * I
            rec["R_nz"][it] = R_sc.sum()
            rec["R_lead"][it] = R_ld
            rec["Bz"][it] = self.G @ I_az
            rec["B_center"][it] = self.G_center @ I_az
        rec["label"] = label
        return rec


# ----------------------------------------------------------------------------
# Channel post-processing (what the instrument front-ends would see)
# ----------------------------------------------------------------------------
def add_channels(rec, cfg: Config, rng, ext_tap=None, ext_field=None):
    """Attach noisy tap estimate and Hall harmonic channels to a run record."""
    t = rec["t"]
    dI = np.gradient(rec["I"], t)
    # commanded-current inductive compensation with residual error; the NI
    # magnetization transient during ramp shows up here on purpose.
    v_comp = rec["V_term"] - (1 + cfg.comp_err) * rec["L_coil"] * dI
    if ext_tap is not None:
        v_comp = v_comp + ext_tap(t)
    rec["tap"] = v_comp + rng.normal(0, cfg.tap_noise, t.size)

    Bz = rec["Bz"].copy()
    if ext_field is not None:
        Bz = Bz + ext_field(t)[:, None]           # common-mode by design
    Bz = Bz + rng.normal(0, cfg.hall_noise, Bz.shape)
    rec["Bz_meas"] = Bz

    # baseline window: the last second before any event (caller passes idx)
    i0, i1 = rec["baseline_idx"]
    base = Bz[i0:i1].mean(axis=0)
    spec = np.fft.rfft(Bz - base, axis=1) / cfg.n_sensors
    rec["c1"] = np.abs(spec[:, 1])
    rec["c2"] = np.abs(spec[:, 2])
    quiet = np.abs(np.fft.rfft(Bz[i0:i1] - base, axis=1) / cfg.n_sensors)
    rec["c1_mu"], rec["c1_sig"] = float(quiet[:, 1].mean()), float(quiet[:, 1].std())
    rec["hall_thresh"] = rec["c1_mu"] + cfg.hall_sigma_mult * rec["c1_sig"]
    return rec


def first_crossing(t, y, thr, t_from=0.0, persist=0.0, dt=1e-3):
    """First time y stays above thr for `persist` seconds, after t_from."""
    npers = max(1, int(round(persist / dt)))
    above = (y > thr) & (t >= t_from)
    run = 0
    for i, a in enumerate(above):
        run = run + 1 if a else 0
        if run >= npers:
            return float(t[i - npers + 1])
    return None


# ----------------------------------------------------------------------------
# Scenario battery
# ----------------------------------------------------------------------------
def make_profiles(cfg, t_hold_end):
    t_ramp = cfg.i_op / cfg.ramp_rate

    def i_of_t(t):
        return cfg.i_op * min(t / t_ramp, 1.0)

    def di_of_t(t):
        return cfg.ramp_rate if t < t_ramp else 0.0

    return i_of_t, di_of_t, t_ramp


def run_all():
    cfg = Config()
    os.makedirs(OUT, exist_ok=True)
    rng = np.random.default_rng(cfg.seed)
    net = NIPancake(cfg)
    print(f"[geom] N={cfg.n_turns} K={cfg.k_sectors}  L_coil={net.L_coil*1e3:.3f} mH"
          f"  R_char={net.R_char*1e3:.3f} mOhm"
          f"  tau_pred={net.L_coil/net.R_char:.3f} s  tape={net.tape_len:.1f} m")
    summary = {"L_coil_H": net.L_coil, "R_char_Ohm": net.R_char,
               "tau_pred_s": net.L_coil / net.R_char,
               "tap_thresh_V": cfg.tap_thresh, "scenarios": {}}

    i_of_t, di_of_t, t_ramp = make_profiles(cfg, None)
    t_settle = t_ramp + 3.0            # event time for S1-S3

    # ---------------- S0: charging-delay validation --------------------
    rec = net.run(t_ramp + 4.0, i_of_t, di_of_t, label="S0")
    rec["L_coil"] = net.L_coil
    t, Bc = rec["t"], rec["B_center"]
    hold = t > t_ramp + 0.05
    Binf = Bc[-1]
    y = Binf - Bc[hold]
    ok = y > Binf * 1e-4
    tau_fit = -1.0 / np.polyfit(t[hold][ok], np.log(y[ok]), 1)[0]
    summary["scenarios"]["S0"] = {
        "tau_fit_s": float(tau_fit),
        "tau_pred_s": net.L_coil / net.R_char,
        "rel_err": float(abs(tau_fit - net.L_coil / net.R_char)
                         / (net.L_coil / net.R_char))}
    print(f"[S0] tau_fit={tau_fit:.3f} s vs tau_pred="
          f"{net.L_coil/net.R_char:.3f} s")

    # ---------------- S1: joint-initiated fast quench (cell i) ----------
    # Classic failure mode: a normal zone starts at the terminal joint/lead
    # (series with the winding, OUTSIDE the radial-bypass network -> the tap
    # sees it immediately) and propagates into the outermost turns 150 ms
    # later, driving redistribution the Hall ring confirms.
    s_outer = float(net.s_start[27 * cfg.k_sectors + 4])
    lead1 = dict(ignite_t=t_settle, v=1.0, r_prime=cfg.r_prime_normal, l0=0.0)
    nz1 = dict(ignite_t=t_settle + 0.15, s0=s_outer, v=1.0,
               r_prime=cfg.r_prime_normal, l0=0.0)
    rec1 = net.run(t_settle + 1.5, i_of_t, di_of_t, nz=nz1, lead=lead1,
                   label="S1")
    rec1["L_coil"] = net.L_coil
    rec1["baseline_idx"] = (int((t_settle - 1.2) / cfg.dt),
                            int((t_settle - 0.2) / cfg.dt))
    add_channels(rec1, cfg, rng)
    save_scenario(rec1, cfg, net, summary, "S1", t_settle,
                  note="joint-initiated quench propagating into winding")

    # ---------------- S2: false-positive battery (cell ii) --------------
    def ext_tap(t):    # (a) flux-jump-like spike, (b) external-pulse pickup
        v = np.zeros_like(t)
        v += np.where((t >= t_settle) & (t < t_settle + 0.005), 30e-3, 0.0)
        tp = t_settle + 1.0
        v += np.where((t >= tp) & (t < tp + 0.010), 25e-3, 0.0)
        return v

    def ext_field(t):  # common-mode external Bz step-and-decay, 5 mT
        tp = t_settle + 1.0
        out = np.zeros_like(t)
        m = t >= tp
        out[m] = 5e-3 * np.exp(-(t[m] - tp) / 0.1)
        return out

    rec2 = net.run(t_settle + 2.0, i_of_t, di_of_t, label="S2")
    rec2["L_coil"] = net.L_coil
    rec2["baseline_idx"] = (int((t_settle - 1.2) / cfg.dt),
                            int((t_settle - 0.2) / cfg.dt))
    add_channels(rec2, cfg, rng, ext_tap=ext_tap, ext_field=ext_field)
    save_scenario(rec2, cfg, net, summary, "S2", t_settle,
                  note="flux-jump spike + external field pulse; no quench")

    # ---------------- S3: slow bypass-dominated (cell iii) --------------
    # Finite hotspot (3 cm, defect class) in an outer turn; slow growth in
    # the current-sharing regime. Radial bypass keeps the tap far below
    # threshold while the redistribution asymmetry is visible at the ring.
    nz3 = dict(ignite_t=t_settle, s0=s_outer, v=0.03, r_prime=5e-3, l0=0.05)
    rec3 = net.run(t_settle + 6.0, i_of_t, di_of_t, nz=nz3, label="S3")
    rec3["L_coil"] = net.L_coil
    rec3["baseline_idx"] = (int((t_settle - 1.2) / cfg.dt),
                            int((t_settle - 0.2) / cfg.dt))
    add_channels(rec3, cfg, rng)
    save_scenario(rec3, cfg, net, summary, "S3", t_settle,
                  note="slow NI bypass event: 5 cm hotspot, v=3 cm/s")

    # ---------------- S4: self-test stimuli (cell iv) --------------------
    T4, dt = 20.0, cfg.dt
    t4 = np.arange(1, int(T4 / dt) + 1) * dt
    tap4 = rng.normal(0, cfg.tap_noise, t4.size)
    hall4 = rng.normal(0, cfg.hall_noise, (t4.size, cfg.n_sensors))
    inj = dict(tap=[], hall=[], degrade_hall_after=12.0)
    for tinj in np.arange(2.5, T4, 5.0):
        m = (t4 >= tinj) & (t4 < tinj + 0.020)
        tap4[m] += cfg.pilot_tap
        inj["tap"].append(float(tinj))
        if tinj < inj["degrade_hall_after"]:
            mh = (t4 >= tinj + 0.5) & (t4 < tinj + 0.5 + 0.010)
            hall4[mh, 3] += cfg.stim_hall
        inj["hall"].append(float(tinj + 0.5))
    np.savez(os.path.join(OUT, "S4.npz"), t=t4, tap=tap4, hall=hall4,
             inj_tap=inj["tap"], inj_hall=inj["hall"],
             degrade_hall_after=inj["degrade_hall_after"],
             pilot_tap=cfg.pilot_tap, stim_hall=cfg.stim_hall)
    summary["scenarios"]["S4"] = {"tap_injections": inj["tap"],
                                  "hall_injections": inj["hall"],
                                  "degrade_hall_after_s": 12.0}
    print("[S4] self-test stimulus record written")

    with open(os.path.join(OUT, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print(f"[done] outputs in {OUT}")
    return summary


def save_scenario(rec, cfg, net, summary, name, t_event, note=""):
    t = rec["t"]
    tap_t = first_crossing(t, np.abs(rec["tap"]), cfg.tap_thresh,
                           t_from=t_event, persist=0.005, dt=cfg.dt)
    hall_t = first_crossing(t, rec["c1"], rec["hall_thresh"],
                            t_from=t_event, persist=0.020, dt=cfg.dt)
    entry = {"note": note, "t_event_s": t_event,
             "tap_first_cross_s": tap_t, "hall_first_cross_s": hall_t,
             "hall_thresh_T": rec["hall_thresh"]}
    if tap_t and hall_t:
        entry["tap_delay_s"] = tap_t - t_event
        entry["hall_delay_s"] = hall_t - t_event
        if hall_t < tap_t:
            entry["tap_over_hall_ratio"] = (tap_t - t_event) / (hall_t - t_event)
    summary["scenarios"][name] = entry
    print(f"[{name}] tap cross: {tap_t}  hall cross: {hall_t}  ({note})")

    np.savez(os.path.join(OUT, f"{name}.npz"),
             t=t, I=rec["I"], V_term=rec["V_term"], tap=rec["tap"],
             Bz=rec["Bz_meas"], c1=rec["c1"], c2=rec["c2"],
             R_nz=rec["R_nz"], R_lead=rec.get("R_lead", np.zeros_like(t)),
             t_event=t_event,
             tap_thresh=cfg.tap_thresh, hall_thresh=rec["hall_thresh"],
             c1_mu=rec["c1_mu"], c1_sig=rec["c1_sig"])

    fig, ax = plt.subplots(3, 1, figsize=(8, 8), sharex=True)
    ax[0].plot(t, rec["I"]); ax[0].set_ylabel("I_t [A]")
    ax[1].plot(t, rec["tap"] * 1e3, lw=0.6)
    ax[1].axhline(cfg.tap_thresh * 1e3, color="r", ls="--", label="tap thr")
    ax[1].set_ylabel("tap est. [mV]"); ax[1].legend(loc="upper left")
    ax[2].plot(t, rec["c1"] * 1e6, lw=0.8, label="|c1|")
    ax[2].plot(t, rec["c2"] * 1e6, lw=0.6, alpha=0.6, label="|c2|")
    ax[2].axhline(rec["hall_thresh"] * 1e6, color="r", ls="--",
                  label="6-sigma thr")
    ax[2].set_ylabel("harmonic [uT]"); ax[2].set_xlabel("t [s]")
    ax[2].legend(loc="upper left")
    fig.suptitle(f"{name} -- SIMULATED (prophetic example) -- {note}")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, f"{name}.png"), dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    run_all()
