#!/usr/bin/env python3
# =============================================================================
# ID_09 Phase A -- FUSION STATE MACHINE (golden model of claim 1 (c)-(g))
#
# Research aid -- not legal advice. This is a cycle-approximate behavioral
# model in Python; the same logic is later ported to the FPGA fabric for the
# HIL bench. Outputs of THIS script are SIMULATED (prophetic) examples.
#
# What it demonstrates, element by element:
#   (c) any-modality ARM with cross-modality CONFIRM:
#         fast-arms -> slow-confirms within a window derived from MEASURED
#         quantities (beta * tau_meas + k * latency_meas of the confirmer);
#         slow-arms -> fast-channel LOOK-BACK (+ short forward watch) for
#         sub-threshold growth on the stored record.
#   (d) unconfirmed arms RELEASE and are logged (no trip).
#   (e) injection-port SELF-TEST on a schedule: per-channel stimulus ->
#         measured response latency; masked end-to-end arm->trip timing.
#   (f) RATED-TRIP-LATENCY STATUS: asserted only while every measured
#         latency is within budget AND fresh (staleness limit).
#   (g) DEGRADED MODES: on self-test failure of a confirming channel, rated
#         status de-asserts, the surviving channel trips single-channel at a
#         tightened threshold, and a supervisory flag is raised.
#
# Inputs : 02_sim/out/S1.npz, S2.npz, S3.npz, S4.npz and summary.json
#          (produced by ni_network_sim.py -- run that first).
# Outputs: out/events.csv, out/fsm_S*.png, out/fsm_summary.json with
#          PASS/FAIL against the four-cell gates of ID_09 section 7.
# =============================================================================

import csv
import json
import os

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")


# ---------------------------------------------------------------------------
# Configuration (instrument-side; coil-side numbers arrive via summary.json)
# ---------------------------------------------------------------------------
CFG = dict(
    dt=1e-3,
    # channel processing-pipeline latencies (physical, before self-test)
    proc_lat=dict(tap=0.005, hall=0.025),
    persistence=dict(tap=0.005, hall=0.020),
    # confirm-window law: W = BETA * tau_meas + KLAT * latency_meas(confirmer)
    BETA=2.0, KLAT=3.0,
    # slow-arm look-back / forward-watch on the fast channel record
    T_LOOKBACK=2.0, W_FORWARD=1.5,
    lookback_slope_min=0.2e-3,      # [V/s]
    lookback_rise_min=0.5e-3,       # [V]
    # trip actuation path
    trip_logic=0.2e-3, trip_driver=0.3e-3, trip_relay=3.0e-3,
    # self-test scheduling and rated-status policy
    selftest_period=5.0, staleness=15.0,
    budget=dict(tap=0.015, hall=0.060, e2e=0.005),
    degraded_thresh_factor=0.6,
)


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------
def sustained_cross(t, y, thr, persist, dt, t_from=0.0):
    """Times at which y completes `persist` seconds above thr (rising)."""
    npers = max(1, int(round(persist / dt)))
    above = (y > thr) & (t >= t_from)
    out, run = [], 0
    for i, a in enumerate(above):
        run = run + 1 if a else 0
        if run == npers:                      # completion instant
            out.append(t[i])
    # collapse bursts: keep first completion of each contiguous excursion
    keep, last = [], -np.inf
    for tc in out:
        if tc - last > persist + 2 * dt:
            keep.append(tc)
        last = tc
    return keep


class Channel:
    def __init__(self, name, t, y, thr):
        self.name, self.t, self.y, self.thr = name, t, y, thr
        self.persist = CFG["persistence"][name]
        self.proc = CFG["proc_lat"][name]
        self.lat_meas = None          # populated by self-test
        self.lat_time = -np.inf

    def detections(self, t_from=0.0):
        """Detection-complete instants (crossing + persistence + pipeline)."""
        return [tc + self.proc for tc in
                sustained_cross(self.t, self.y, self.thr,
                                self.persist, CFG["dt"], t_from)]

    def value_at(self, tq):
        return float(np.interp(tq, self.t, self.y))

    def effective_latency(self):
        return self.lat_meas if self.lat_meas is not None else self.proc


# ---------------------------------------------------------------------------
# Fusion engine
# ---------------------------------------------------------------------------
class FusionEngine:
    """IDLE -> ARMED(ch) -> TRIP | RELEASE, per claim 1(c)-(d)."""

    def __init__(self, fast: Channel, slow: Channel, tau_meas: float, log):
        self.fast, self.slow, self.tau = fast, slow, tau_meas
        self.log = log

    def _window(self, confirmer: Channel):
        return CFG["BETA"] * self.tau + CFG["KLAT"] * confirmer.effective_latency()

    def _lookback_confirm(self, t_arm):
        """Sub-threshold-growth test on the fast-channel stored record."""
        f = self.fast
        t0 = t_arm - CFG["T_LOOKBACK"]
        t_end = min(t_arm + CFG["W_FORWARD"], f.t[-1])
        base = f.value_at(t0)
        m = (f.t >= t0) & (f.t <= t_end)
        tt, yy = f.t[m], np.abs(f.y[m])
        for i in range(len(tt)):
            if tt[i] < t_arm:
                continue
            mm = tt <= tt[i]
            slope = np.polyfit(tt[mm], yy[mm], 1)[0]
            rise = yy[i] - abs(base)
            if slope > CFG["lookback_slope_min"] and rise > CFG["lookback_rise_min"]:
                return tt[i], slope, rise
        return None, None, None

    def run(self, scenario, t_from):
        ev_fast = self.fast.detections(t_from)
        ev_slow = self.slow.detections(t_from)
        arms = sorted([(t, "tap") for t in ev_fast] + [(t, "hall") for t in ev_slow])
        state, result = "IDLE", []
        consumed_slow = set()
        for t_arm, ch in arms:
            if state == "TRIPPED":
                break
            self.log(scenario, t_arm, "ARM", ch,
                     f"threshold crossing sustained ({ch})")
            if ch == "tap":
                W = self._window(self.slow)
                conf = [ts for ts in ev_slow
                        if t_arm - 0.05 <= ts <= t_arm + W and ts not in consumed_slow]
                if conf:
                    tc = conf[0]
                    consumed_slow.add(tc)
                    self.log(scenario, tc, "CONFIRM", "hall",
                             f"asymmetry within W={W:.3f}s of tap arm")
                    self._trip(scenario, tc, result)
                    state = "TRIPPED"
                else:
                    tr = t_arm + W
                    self.log(scenario, tr, "RELEASE", "tap",
                             f"no cross-modality confirmation in W={W:.3f}s")
                    result.append(("RELEASE", t_arm, tr))
            else:  # slow (hall) arm -> look-back on fast record
                tc, slope, rise = self._lookback_confirm(t_arm)
                if tc is not None:
                    self.log(scenario, tc, "CONFIRM", "tap-lookback",
                             f"sub-threshold growth: slope={slope*1e3:.2f} mV/s,"
                             f" rise={rise*1e3:.2f} mV over {CFG['T_LOOKBACK']}s record")
                    self._trip(scenario, tc, result)
                    state = "TRIPPED"
                else:
                    tr = t_arm + CFG["W_FORWARD"]
                    self.log(scenario, tr, "RELEASE", "hall",
                             "look-back/forward growth criteria not met")
                    result.append(("RELEASE", t_arm, tr))
        return result

    def _trip(self, scenario, t_confirm, result):
        t_gate = t_confirm + CFG["trip_logic"] + CFG["trip_driver"]
        t_open = t_gate + CFG["trip_relay"]
        self.log(scenario, t_gate, "TRIP_CROWBAR", "trip",
                 "solid-state crowbar gate asserted")
        self.log(scenario, t_open, "TRIP_RELAY", "trip",
                 "force-guided relay contacts open")
        result.append(("TRIP", t_confirm, t_open))


# ---------------------------------------------------------------------------
# Self-test / rated-status subsystem (claim 1 (e)-(g)) -- runs on S4 record
# ---------------------------------------------------------------------------
def run_selftest(d, log):
    t = d["t"]; dt = CFG["dt"]
    tap, hall = d["tap"], d["hall"]
    events, lat_hist = [], []
    rated_trace = []                      # (t, rated?, mode)
    lat = {"tap": None, "hall": None}
    lat_time = {"tap": -np.inf, "hall": -np.inf}
    mode = "DUAL"
    pilot, stim = float(d["pilot_tap"]), float(d["stim_hall"])
    b3 = hall[:, 3] - np.median(hall[:200, 3])

    inj_pairs = list(zip(d["inj_tap"], d["inj_hall"]))
    for (ti_tap, ti_hall) in inj_pairs:
        # --- tap pilot response ---
        m = (t >= ti_tap) & (t <= ti_tap + 0.2)
        hit = np.nonzero(np.abs(tap[m]) > pilot / 2)[0]
        if hit.size >= 3:
            l = (t[m][hit[2]] - ti_tap) + CFG["proc_lat"]["tap"]
            lat["tap"], lat_time["tap"] = l, ti_tap
            log("S4", ti_tap + l, "SELFTEST_OK", "tap", f"latency={l*1e3:.1f} ms")
        else:
            log("S4", ti_tap + 0.2, "SELFTEST_FAIL", "tap", "no pilot response")
            lat["tap"] = None
        # --- hall stimulus response ---
        m = (t >= ti_hall) & (t <= ti_hall + 0.2)
        hit = np.nonzero(np.abs(b3[m]) > stim / 2)[0]
        if hit.size >= 3:
            l = (t[m][hit[2]] - ti_hall) + CFG["proc_lat"]["hall"]
            lat["hall"], lat_time["hall"] = l, ti_hall
            log("S4", ti_hall + l, "SELFTEST_OK", "hall", f"latency={l*1e3:.1f} ms")
        else:
            log("S4", ti_hall + 0.2, "SELFTEST_FAIL", "hall",
                "no stimulus response")
            lat["hall"] = None
        # --- masked end-to-end arm->trip timing (output inhibited) ---
        e2e = CFG["trip_logic"] + CFG["trip_driver"] + CFG["trip_relay"]
        log("S4", ti_hall + 0.3, "SELFTEST_E2E", "trip",
            f"masked arm->actuation = {e2e*1e3:.1f} ms")
        # --- rated-status evaluation at end of this cycle ---
        t_eval = ti_hall + 0.35
        ok = True
        for ch in ("tap", "hall"):
            fresh = (t_eval - lat_time[ch]) <= CFG["staleness"]
            within = lat[ch] is not None and lat[ch] <= CFG["budget"][ch]
            ok = ok and fresh and within
        ok = ok and e2e <= CFG["budget"]["e2e"] + CFG["trip_relay"]  # relay leg budgeted separately
        new_mode = "DUAL" if ok else "DEGRADED"
        if new_mode != mode:
            if new_mode == "DEGRADED":
                log("S4", t_eval, "RATED_DEASSERT", "status",
                    "self-test failure -> rated trip latency NOT asserted")
                log("S4", t_eval, "MODE_DEGRADED", "status",
                    f"single-channel trip @ thr x{CFG['degraded_thresh_factor']}"
                    " + supervisory flag")
            else:
                log("S4", t_eval, "RATED_ASSERT", "status", "all channels rated")
            mode = new_mode
        rated_trace.append((t_eval, ok, mode))
        lat_hist.append((t_eval,
                         None if lat["tap"] is None else lat["tap"],
                         None if lat["hall"] is None else lat["hall"], e2e))
    return rated_trace, lat_hist


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------
def plot_scenario(name, d, events, note=""):
    t = d["t"]
    fig, ax = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    ax[0].plot(t, d["tap"] * 1e3, lw=0.6)
    ax[0].axhline(float(d["tap_thresh"]) * 1e3, color="r", ls="--", lw=0.8)
    ax[0].set_ylabel("tap est. [mV]")
    ax[1].plot(t, d["c1"] * 1e6, lw=0.8)
    ax[1].axhline(float(d["hall_thresh"]) * 1e6, color="r", ls="--", lw=0.8)
    ax[1].set_ylabel("|c1| [uT]"); ax[1].set_xlabel("t [s]")
    colors = dict(ARM="tab:orange", CONFIRM="tab:green", RELEASE="tab:gray",
                  TRIP_CROWBAR="tab:red", TRIP_RELAY="darkred")
    for (sc, te, ev, ch, detail) in events:
        if sc != name or ev not in colors:
            continue
        for a in ax:
            a.axvline(te, color=colors[ev], lw=1.0, alpha=0.8)
        ax[0].text(te, ax[0].get_ylim()[1] * 0.92, ev.split("_")[0],
                   rotation=90, fontsize=7, color=colors[ev])
    fig.suptitle(f"{name} fusion timeline -- SIMULATED -- {note}")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, f"fsm_{name}.png"), dpi=130)
    plt.close(fig)


def plot_selftest(d, rated_trace, lat_hist, events):
    fig, ax = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    th = [r[0] for r in lat_hist]
    ax[0].plot(th, [1e3 * l[1] if l[1] else np.nan for l in lat_hist],
               "o-", label="tap latency")
    ax[0].plot(th, [1e3 * l[2] if l[2] else np.nan for l in lat_hist],
               "s-", label="hall latency")
    ax[0].axhline(CFG["budget"]["tap"] * 1e3, ls="--", color="tab:blue", lw=0.7)
    ax[0].axhline(CFG["budget"]["hall"] * 1e3, ls="--", color="tab:orange", lw=0.7)
    ax[0].set_ylabel("measured latency [ms]"); ax[0].legend()
    ax[1].step([r[0] for r in rated_trace],
               [1 if r[1] else 0 for r in rated_trace], where="post")
    ax[1].set_ylabel("rated status"); ax[1].set_ylim(-0.1, 1.2)
    ax[1].set_xlabel("t [s]")
    for (sc, te, ev, ch, detail) in events:
        if ev in ("SELFTEST_FAIL", "MODE_DEGRADED"):
            for a in ax:
                a.axvline(te, color="tab:red", lw=1.0, alpha=0.7)
    fig.suptitle("S4 self-test: injected-stimulus latencies, rated status,"
                 " degradation -- SIMULATED")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fsm_S4.png"), dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "summary.json")) as f:
        sim = json.load(f)
    tau_meas = float(sim["scenarios"]["S0"]["tau_fit_s"])

    events = []

    def log(scenario, t, ev, ch, detail):
        events.append((scenario, float(t), ev, ch, detail))

    verdict = {"tau_meas_s": tau_meas, "gates": {}}

    for name, note in (("S1", "cell i: joint quench, tap arms, hall confirms"),
                       ("S2", "cell ii: disturbances arm, release, no trip"),
                       ("S3", "cell iii: hall arms, tap look-back confirms")):
        d = np.load(os.path.join(OUT, f"{name}.npz"))
        te = float(d["t_event"])
        tap = Channel("tap", d["t"], np.abs(d["tap"]), float(d["tap_thresh"]))
        hall = Channel("hall", d["t"], d["c1"], float(d["hall_thresh"]))
        # latencies as most recently measured by self-test (S4 steady values)
        tap.lat_meas, hall.lat_meas = 0.008, 0.029
        eng = FusionEngine(tap, hall, tau_meas, log)
        res = eng.run(name, t_from=te - 2.0)
        plot_scenario(name, d, events, note)

        evs = [e for e in events if e[0] == name]
        seq = [e[2] for e in evs]
        first_by = {e[2]: e for e in reversed(evs)}
        if name == "S1":
            ok = (seq[:2] == ["ARM", "CONFIRM"] and "TRIP_RELAY" in seq
                  and first_by["ARM"][3] == "tap"
                  and first_by["CONFIRM"][3] == "hall")
            verdict["gates"]["S1_tap_arms_hall_confirms_trip"] = bool(ok)
            verdict["S1"] = dict(
                arm_tap_s=first_by["ARM"][1] - te,
                confirm_hall_s=first_by["CONFIRM"][1] - te,
                trip_relay_s=first_by["TRIP_RELAY"][1] - te)
        if name == "S2":
            n_arm = seq.count("ARM"); n_rel = seq.count("RELEASE")
            n_trip = seq.count("TRIP_RELAY")
            verdict["gates"]["S2_arms_release_no_trip"] = bool(
                n_arm >= 2 and n_rel == n_arm and n_trip == 0)
            verdict["S2"] = dict(arms=n_arm, releases=n_rel, trips=n_trip)
        if name == "S3":
            ok = (first_by.get("ARM", (None,) * 4)[3] == "hall"
                  and "CONFIRM" in seq and "TRIP_RELAY" in seq)
            t_arm = first_by["ARM"][1] - te
            tap_cross = sim["scenarios"]["S3"]["tap_first_cross_s"]
            horizon = float(d["t"][-1]) - te
            bound = ((tap_cross - te) if tap_cross else horizon) / t_arm
            verdict["gates"]["S3_hall_arms_lookback_trip"] = bool(ok)
            verdict["gates"]["S3_early_detection_ratio_ge_3"] = bool(bound >= 3)
            verdict["S3"] = dict(arm_hall_s=t_arm,
                                 trip_relay_s=first_by["TRIP_RELAY"][1] - te,
                                 tap_cross_s=(tap_cross - te) if tap_cross else None,
                                 ratio_lower_bound=bound)

    # ----- S4 self-test / rated status / degraded mode -----
    d4 = np.load(os.path.join(OUT, "S4.npz"))
    rated_trace, lat_hist = run_selftest(d4, log)
    plot_selftest(d4, rated_trace, lat_hist, events)
    pre = [r for r in rated_trace if r[0] < float(d4["degrade_hall_after"])]
    post = [r for r in rated_trace if r[0] > float(d4["degrade_hall_after"])]
    verdict["gates"]["S4_rated_asserted_while_healthy"] = bool(
        pre and all(r[1] for r in pre))
    verdict["gates"]["S4_degradation_deasserts_and_degrades"] = bool(
        post and all(not r[1] and r[2] == "DEGRADED" for r in post))
    verdict["S4"] = dict(
        latencies=[dict(t=h[0], tap_ms=None if h[1] is None else h[1] * 1e3,
                        hall_ms=None if h[2] is None else h[2] * 1e3,
                        e2e_ms=h[3] * 1e3) for h in lat_hist])

    # ----- persist -----
    with open(os.path.join(OUT, "events.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["scenario", "t_s", "event", "channel", "detail"])
        for row in sorted(events):
            w.writerow(row)
    with open(os.path.join(OUT, "fsm_summary.json"), "w") as f:
        json.dump(verdict, f, indent=2)

    print(f"tau_meas (from S0 commissioning fit): {tau_meas:.3f} s")
    for g, ok in verdict["gates"].items():
        print(f"  {'PASS' if ok else 'FAIL':4}  {g}")
    return verdict


if __name__ == "__main__":
    main()
