# Research Journal — 2026-07-08

## HSX Hall-sensor readout — first dynamic spinning run on the bridge emulator (20 kHz, 20 mA)

**Owner:** Y. "Tim" Zhao · **Project:** 02_HSX_Hall_Sensor_Readout ·
**Session type:** sensorless (emulator) bring-up, plan §4 / §6.1.

Today was the first end-to-end current-spinning run: Pico 2 clock →
board → bridge emulator → AD8429 → oscilloscope capture → offline
demodulation. Headline: **the spinning-current offset cancellation works**;
**one absolute-magnitude anomaly remains open** and is the first task next
session.

---

## 1. Configuration (as-run)

| Parameter | Value |
|---|---|
| Bias current | **20 mA**, external source |
| Spinning phase rate f | **20 kHz** (8 × 50 µs = 400 µs full cycle; 2.5 kHz update) |
| Emulator bridge | 4 × **680 Ω** ring, p1–p2–p3–p4 |
| Parallel resistor | **2.2 kΩ** across the p1–p2 arm (DMM-confirmed 2.2 kΩ) |
| Amplifier gain resistor R_G | **60.4 Ω** — SMD code "76X" (EIA-96: 76→604, X→×0.1), DMM-confirmed connected → nominal G = 1 + 6000/60.4 = **100.3** |
| Current-sense resistors | R9 = R10 = 100 Ω; **both read 2.0 Vdc at 20 mA** |
| Oscilloscope | Keysight **DSO-X 4022A**, CH2 = v_meas (J4), ~971 kSa/s, 8-bit (~33 mV LSB) |
| Firmware | `firmware/pico2/main.py` single-file build, MODE 1 (spin + scope), `DEFAULT_FREQ = 20 kHz` |
| Raw data | `data/2026-07-08_test_spin.csv` — **v_meas only; sync (CH-b) NOT captured** |

---

## 2. Observations

- **Clean 8-state staircase**, period exactly 400 µs → the ADG1209/ADG5236
  muxes are stepping through all eight states correctly at 20 kHz.
- Settled per-state levels: lows ≈ −0.40 V, highs ≈ +0.85 … +1.07 V,
  about a **+0.27 V pedestal** (the amplifier offset × G, constant across
  states). Offset staircase amplitude **A ≈ 0.686 V**. Raw per-state sign
  pattern **+ − − + − + + −** — matches the spec emulator offset pattern.
- Phase-edge **settling spikes to ~+4.8 V** — normal mux charge injection;
  blanked 45 % before averaging.
- **R9 = R10 = 2.0 V** → 20 mA in = 20 mA out. **Leakage check PASSED**
  (plan §4 Day 3: V(R9)/R9 = V(R10)/R10) — the bias current genuinely
  flows through the bridge; no bias-loop leak.

Figure: `analysis/figures/2026-07-08_spin_verify.png`.
Reproduce: `python3 analysis/spin_verify_nosync.py data/2026-07-08_test_spin.csv --f 20000 --arm 680 --par 2200 --ibias 0.020`.

---

## 3. Analysis

**Offset cancellation — PASS.** Sync wasn't captured, so phase was
reconstructed by folding at the known 20 kHz. Demodulating (sign = +1 if
a0 == a2 else −1) collapses the **686 mV** raw offset swing to a residual
**≤ 5 mV** — and that 5 mV is just the DSO-X's 8-bit quantization
(≈33 mV LSB) over only ~5 captured cycles, i.e. the measurement floor,
not circuit error. So the spinning suppresses the offset by **≥ ~130×**
(measurement-limited). This is the core Week-1 §6.1-step-5 result.

**Absolute-magnitude anomaly — OPEN.** With every parameter above taken
as confirmed — 680 Ω arms, an effective 2.2 kΩ imbalance, 20 mA through
the bridge, gain 100.3 — the exact bridge model predicts a per-state
amplifier output of **~75 V**, i.e. pinned hard at the ±13.5 V rail. The
scope shows a clean, unclipped **0.686 V**. The measured offset is
**~109× smaller** than the confirmed components predict. This is a real
inconsistency, not a rounding issue.

What today's data already rules in/out:
- **Current leakage — ruled OUT.** R9 = R10 = 2.0 V ⇒ 20 mA reaches the
  bridge.
- **R_G value — ruled OUT as the cause by resistance alone.** 60.4 Ω
  present and connected (measured).

Remaining candidates (either would explain a ~100× shortfall):
1. **In-operation differential gain is not actually ~100×** — e.g. an
   in-amp / R_G contact issue a static Ω check wouldn't catch, or the amp
   not settling at G=100 under this common-mode. Static resistance ≠
   dynamic gain.
2. **The 2.2 kΩ is not electrically unbalancing the bridge** — an open
   solder joint on it, or it bridges the wrong node (a diagonal instead
   of the p1–p2 arm), leaving four matched 680 Ω arms whose residual
   tolerance offset happens to land near 0.686 V.

**Decisive next test (NOT yet run): the ΔV gain check (plan §4 Day 3–4).**
Static-hold one state and either (a) inject a known ~1 mV differential on
the sense pair and read ΔV_out/ΔV_in, or (b) DMM the differential right
at the amp inputs (IN+ − IN−):
- differential ≈ **0.75 V** ⇒ candidate 1 (gain is not ~100× in operation);
- differential ≈ **7 mV** ⇒ candidate 2 (2.2 kΩ imbalance ineffective).

---

## 4. Verdict

The **method and the signal chain are working**: firmware/clocking, mux
stepping, sync-less demod, and bias-loop integrity (R9 = R10) are all
good, and current-spinning demonstrably cancels the bridge offset. The
**absolute offset magnitude is unexplained (~100× low)** versus the
confirmed component values — this is a consistency/measurement question
to resolve with the ΔV gain check, not a demonstrated failure of the
readout concept. Do not calibrate against these magnitudes until the
anomaly is closed.

Side note: 20 mA is fine for the resistor emulator (~7 mW/arm) but is
~20× above the ≤ 1 mA operating point intended for the real GaN die
(self-heating) — keep the real sensor ≤ 1 mA.

---

## 5. Plan comparison — This Week (Jul 6–12), §4 / §6.1 sensorless verification

| Plan item | Status | Note |
|---|---|---|
| Cold checks / DMM value audit / J3 pin order (Day 1) | ◑ partial | as-built values being captured; not a full board log yet |
| First power: ±15 V rails, quiescent I, thermal (Day 1–2) | ◑ implied | board operating normally; not formally logged |
| DC/DC rail ripple spectrum (§2.5) | ✗ not done | |
| Logic bring-up: a0/a1/a2/sync/EN edges, ground bond (Day 2) | ✓ done | 20 kHz spin + clean staircase confirms clocks; EN verified earlier |
| Emulator build + install (Day 3) | ✓ done | 680 Ω ring + 2.2 kΩ on p1–p2 |
| Current source + R9/R10 leakage check (Day 3) | ✓ done | 20 mA; **R9 = R10 = 2.0 V** (passed) |
| Static 8-state survey, DMM per state (Day 3) | ✗ not done | do next session |
| **ΔV gain verification, G = 100.3 ±1% (Day 3–4)** | ✗ **not done** | **TOP PRIORITY — resolves the §3 anomaly** |
| Dynamic spinning + demod; residual ≈ 0 (Day 4–5) | ✓ core done | offset 686 mV → ≤ 5 mV; ◑ absolute magnitude anomaly open |
| Glitch / blanking / frequency study (Day 4–5) | ◑ partial | 45 % blanking at 20 kHz only; no 10k/40k/100k sweep |
| Noise floor PSD, µT/√Hz (Day 4–5) | ✗ not done | capture too short + quantization-limited |
| Sync-channel capture for the standard demod | ✗ not done | v_meas only; phase reconstructed offline |
| Week-1 deliverables (board log, sensorless memo, demod script) | ◑ in progress | this journal + `spin_verify_nosync.py`; board log + gain/noise pending |

Legend: ✓ done · ◑ partial · ✗ not done.

---

## 6. Next session — priorities

1. **ΔV gain check** — static-hold a state, DMM the amp-input differential
   (or inject a known ~1 mV). Resolves the magnitude anomaly (gain vs
   imbalance). *Everything else waits on this.*
2. Static 8-state survey with a DMM per state (record v_meas vs the §1
   sign table).
3. Re-capture **with the sync channel (CH-b = GP19)** and a **longer
   window / finer vertical scale** — then `hsx_demod_scope_csv.py` runs
   directly and the noise floor isn't quantization-limited.
4. Blanking + frequency study: repeat at f = 10 k / 40 k / 100 k.
5. Log rails/quiescent + DC-DC ripple spectrum if not already.
6. Once the magnitude is understood, set the deliberate emulator operating
   point and (for the real sensor) drop bias to ≤ 1 mA.

---

## 7. Artifacts (this session)

- `data/2026-07-08_test_spin.csv` — DSO-X 4022A capture (v_meas, 20 kHz, 20 mA)
- `analysis/figures/2026-07-08_spin_verify.png` — verification figure (raw, folded staircase, cancellation, verdict)
- `analysis/spin_verify_nosync.py` — reusable no-sync fold/demod/consistency analyzer
