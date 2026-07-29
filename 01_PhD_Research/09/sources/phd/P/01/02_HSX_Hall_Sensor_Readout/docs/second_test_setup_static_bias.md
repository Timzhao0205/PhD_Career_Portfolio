# Second test setup — static DC bias (p2 → p4), sense p1/p3

**Prepared:** July 8, 2026 · **Firmware:** `firmware/pico2/pico2_static_bias_p2p4.py` (mode 2)
**Companion (first) setup:** full current-spinning + oscilloscope DAQ — `firmware/pico2/pico2_spin_scope.py` (mode 1), plan §4.

This document defines the project's second bench setup: the **classic
direct DC Hall measurement**, run through the existing readout board.
The external current source biases plate ports **p2 and p4**; the
voltage difference between ports **p1 and p3** is measured through the
AD8429 (G = 100.3) and digitized by the **Pico 2's own ADC** at J4 — no
oscilloscope, no spinning. It complements, and never replaces, the spun
setup: it trades offset cancellation for simplicity, portability, and
full amplifier bandwidth.

## 1. What it is for

| Use | Why this setup |
|---|---|
| Sensor health check (bench or at HSX) | one Pico + one battery current source; 30-second answer, no scope cart |
| **Raw plate-offset measurement at 100 µA** | at zero applied field the chopped result *is* the plate offset — the gen-2 die incoming-inspection number (project 03, plan §2.1) |
| Continuity with the 2023 measurement style | the Letters deployment was static-biased; this reproduces that mode on the new hardware for apples-to-apples checks |
| "Fast mode" fallback | static phases = no demod bandwidth limit (~1–2 kHz in the spun setup); the chain runs at full amplifier bandwidth, and the recording instrument becomes the bottleneck |

## 2. Configuration

The board's muxes are parked in the four spinning states whose bias axis
is p2/p4 and whose sense pair is p1/p3 — the a1 = 1 subset of the
verified phase table (`docs/SPECS.md`):

| state | a2 a1 a0 | bias | in+ | in− | amp input (ideal) | chop sign |
|---|---|---|---|---|---|---|
| 2 | 0 1 0 | p2 → p4 | p3 | p1 | +(s − o) + e | + |
| 3 | 0 1 1 | p2 → p4 | p1 | p3 | −(s − o) + e | − |
| 6 | 1 1 0 | p4 → p2 | p3 | p1 | −(s − o) + e | − |
| 7 | 1 1 1 | p4 → p2 | p1 | p3 | +(s − o) + e | + |

s = Hall term, o = plate resistive offset (p2/p4 bias axis), e =
amplifier input offset; v_meas = G × loading × (amp input), with
G = 100.3 and loading ≈ 0.83 (SPECS). The primary state is **2**; the
firmware's `measure_chopped()` steps through all four.

**What cancels, what doesn't.** Averaging the four states with signs
{+, −, −, +} (the a0 == a2 rule) cancels the **amplifier offset e
exactly** — sense swap plus current reversal, the same chopper physics
as the spun system — and the plain mean of the four states measures e
itself. The **plate offset o does not cancel**: with a single bias axis,
s and o are inseparable in principle; the chopped result is
x = (s − o) · loading · G. Rotating the bias axis 90° (the a1 flip, i.e.
the full 8-state spin of the first setup) is precisely what separates
them. At zero applied field, x reduces to the raw plate offset — which
is exactly the number incoming inspection wants.

## 3. Wiring

Identical to the spun setup on J3, plus the ADC tap; the scope is not
connected (sync GP19 is driven low).

| Connection | Detail |
|---|---|
| Pico GP16/17/18 → J3 pins 3/2/1 | a0/a1/a2 (same as mode 1) |
| Pico GP20 → J3 pin 4 | EN — board is dead until ≥ 2 V (on-board pulldown) |
| Pico GND (pin 23) → GND1 | **mandatory** — J3 has no ground pin |
| Pico GP26/ADC0 (pin 31) ← J4 SMA center | v_meas tap; the on-board 10 k shunt (R4) stays |
| Pico AGND (pin 33) → J4 shell / GND1 | short ADC return |
| External 100 µA source → J2 (∥ J7) | must float; the a2 chopper reverses the *connection*, so a unipolar source works |
| Current verification | R9 = R10 = 100 Ω sense drops: 10.0 mV each at 100 µA, TP6→TP5 and TP8→TP7, **floating DMM only** (a grounded probe shorts the loop) |

**ADC limits — read before trusting numbers.**
- The RP2350 ADC is unipolar 0–3.3 V; the AD8429 output is bipolar. Any
  state that drives v_meas negative clamps to ~0 V (the firmware warns).
  Since the chop sequence flips the signal's sign between states, a
  large-offset sensor will clamp in roughly half the states.
- 12-bit on 3.3 V = 0.8 mV/LSB; ~few-hundred µV effective after the
  firmware's 256× oversampling. Resolves the ±26 mV emulator step at the
  percent level; does **not** resolve Earth's field (~30 µV at v_meas)
  or Helmholtz-scale signals (±1.5–1.8 mV). Calibration-grade numbers
  always come from the spun setup + scope.
- Optional level-shift network for bipolar readings: 100 kΩ from Pico
  3V3 to the ADC node, 100 kΩ from the node to J4 center, 100 nF from
  the node to AGND (the RC is fine for DC work). This centers 0 V at
  ~1.65 V with a ×0.5 scale — then set `ADC_OFFSET_V ≈ 1.65` (measure
  it: short J4 to GND1 and read) and `ADC_SCALE = 0.5` in the firmware.
- No network and a negative-reading state? Use the states that read
  positive and infer the rest by symmetry, or take that state on a
  floating DMM at J4 (the firmware's mux parking works for DMM
  measurements too).

## 4. Procedure

1. Cold checks done (plan §4 Day 1); board powered, ±15 V verified;
   Pico GND bonded to GND1.
2. External source connected at J2, verified via the R9/R10 drops
   (10.0 mV each at 100 µA); cross-check V(R9)/R9 = V(R10)/R10 — a
   mismatch means leakage.
3. Boot the Pico → mode `2` → `on` (EN high, state 010).
   Confirm EN at TP4, a1 high at TP2, a0/a2 low at TP3/TP1.
4. Connect the emulator plug (first time) or sensor. **Always `off`
   before touching the DSUB.**
5. `read` — single-state sanity number. `chop` — the amplifier-offset-
   free measurement; record x and e. `log 600 2` — ten-minute drift log
   as CSV over USB serial (capture on the host, plot).
6. Done: `off`, then disconnect.

## 5. Expected numbers

| Condition | Expectation |
|---|---|
| Emulator plug, zero field | per-state ±≈ 26 mV around e; chopped \|x\| ≈ **26 mV** (same magnitude as the p1/p3-axis states, opposite sign — the emulator's ΔR arm produces equal-magnitude o on both axes) |
| Real sensor, zero field | x = raw plate offset × 0.83 × 100.3 — **record it; that is the measurement.** Repeat 180°-flipped and average pairs to reject ambient field |
| Sensor + NdFeB magnet waved close | tens of mV swing, clearly visible in `log` output — the quick sanity/sign check |
| Sensor + Earth's field | ~30 µV at v_meas — below this setup's ADC resolution; don't chase it here |
| Amplifier offset e | ≲ few mV at v_meas (AD8429 V_os ≤ 50 µV typ × G ≈ 5 mV worst-case-ish); should be stable session-to-session |

Sign convention: as everywhere in this project, the global sign is fixed
empirically with a magnet of known polarity — never from the netlist.

## 6. Relationship to the two projects

- **Project 02 (this project):** steps 3–5 slot into the bring-up plan
  as the scope-free variant of the Day-3 static-state survey, and the
  drift log complements the Week-3 overnight run. See plan §6.3.
- **Project 03 (vector probe / RSI):** this is the standard tool for the
  gen-2 die **raw-offset distribution at 100 µA** (RSI plan §2.1) — one
  packaged die at a time in the LCC breakout, `chop` per die, log the
  distribution, pick matched dies for the cube.
