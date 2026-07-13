# HSX Hall-Effect Readout Board — Bring-Up, Verification & Calibration Plan
**Board:** `hsx_2026_v1` (4-layer, assembled) · **Sim:** `hall_sensor_measurement_system_v1.asc` · **Target:** sensor install at HSX, August 2026
**Prepared:** July 6, 2026 · **Revised:** July 8, 2026 — firmware reorganized into two operating modes (spin + scope / static bias p2/p4); second test setup added as §6.3 with its own doc, `second_test_setup_static_bias.md`. Reader-friendly HTML versions of all docs now sit next to their markdown.

---

## 1. LTspice ↔ KiCad correspondence (verified from netlists)

Both netlists were parsed pin-by-pin. The functional topology **matches**. Reference designators differ between the two files — use this map:

| Function | LTspice | KiCad | Match |
|---|---|---|---|
| Bias-steering mux (4:1 dual) | U1 ADG1209 | **U1** ADG1209YRUZ | ✅ identical S-pin wiring |
| Sense-steering mux (4:1 dual) | U2 ADG1209 | **U2** ADG1209YRUZ | ✅ identical S-pin wiring |
| Bias-polarity chopper (dual SPDT) | U4 + U5 (two halves) | **U3** ADG5236BRUZ (one dual chip) | ✅ cross-wired identically |
| Instrumentation amp | U3 AD8429, RG = R5 = 60.4 Ω | **U4** AD8429ARZ, RG = **R1** (0603) | ✅ topology; **value unverified** |
| In-amp bias-return resistors (2.2 k in sim) | R6, R7 → GND | **R2** (in+), **R3** (in−) → GND1 | ✅ topology; values unverified |
| Output load (10 k in sim) | R8 | **R4** (out → GND1), out → **J4** SMA | ✅ |
| ±15 V rails | V1, V2 (ideal) | **U5** RS6-2415D isolated DC/DC from 9–36 V in (J5/J6) | ⚠ switching converter, not ideal — see §2.5 |
| +5 V logic / clocks a0, a1, a2, EN | V3–V6 (ideal, EN tied high) | **J3** header (1=a2, 2=a1, 3=a0, 4=en) + pulldowns R5–R8 | ⚠ external, EN defaults LOW — see §2.1/2.2 |
| 100 µA bias source | I1 (ideal, internal) | **External** via J2 (∥ J7) through series **R9/R10**; monitored at TP5–TP8 | ⚠ you must supply it — see §2.3 |
| Hall plate | R1–R4 + B1–B4 macromodel | **J1** DSUB-9 → sensor (1=p1, 2=p3, 6=p2, 7=p4) | ✅ |
| Sim-only ammeter | V7 (0 V) | (none needed; use R9/R10 drop) | — |

### Verified spinning phase table (identical in sim and PCB)

Bias mux: S1A,S2A→p1 · S3A,S4A→p2 · S1B,S2B→p3 · S3B,S4B→p4, DA=ib_p, DB=ib_n.
Sense mux: DA=in+, DB=in−, with channels arranged so:

| a2 | a1 a0 | Bias current | in+ | in− | Amp input (ideal) |
|---|---|---|---|---|---|
| 0 | 0 0 | p1 → p3 | p2 | p4 | +s + o |
| 0 | 0 1 | p1 → p3 | p4 | p2 | −s − o |
| 0 | 1 0 | p2 → p4 | p3 | p1 | +s − o |
| 0 | 1 1 | p2 → p4 | p1 | p3 | −s + o |
| 1 | 0 0 | p3 → p1 | p2 | p4 | −s − o |
| 1 | 0 1 | p3 → p1 | p4 | p2 | +s + o |
| 1 | 1 0 | p4 → p2 | p3 | p1 | −s + o |
| 1 | 1 1 | p4 → p2 | p1 | p3 | +s − o |

where s = (loading factor)·S_I·I·B is the Hall term and o is the plate resistive offset for the p1–p3 bias axis (o flips sign when the bias axis rotates 90°; both s and o flip when a2 reverses the current). The amplifier's own input offset e is constant across all 8 states.

**Demodulation rule (falls out of the table):**
`sign = +1 if (a0 == a2) else −1` — a1 does not enter the sign.
Multiply the output by `sign`, blank the start of each phase, average over 8 states →
- Hall term s survives with full weight,
- sensor offset o cancels (spinning),
- amplifier offset/drift e cancels (chopping via sense-swap + current reversal).

Caveat: the *absolute* polarity conventions of the physical ADG5236 truth table and of your die's terminal order aren't guaranteed to match the sim symbols — determine the global sign empirically with a magnet of known polarity, then freeze the sign map.

### Timing (from sim, replicate on bench)
- a0 = square wave, period 2/f (toggles every phase, 25 µs at f = 40 kHz)
- a1 = a0 ÷ 2 (period 4/f) · a2 = a0 ÷ 4 (period 8/f)
- Full demod cycle = 8/f = 200 µs → **update rate 5 kHz, usable bandwidth ≈ 1–2 kHz** after averaging.
- These are exactly the outputs of a binary counter clocked at f, or three GPIO lines from a microcontroller.

---

## 2. Discrepancies & gotchas found (fix/verify before first power)

1. **EN is not tied high on the PCB.** In sim EN = +5 V permanently; on the board EN comes from J3.4 with a pulldown. **All switches are OFF by default.** Drive EN high (≥2 V) or nothing works. This is safe-by-default but a classic "board looks dead" trap.
2. **J3 has no ground pin.** The logic source (Pico/counter/function-gen) return must be bonded to board analog ground GND1 separately — use the J4 SMA shell, a capacitor ground pad, or solder a dedicated ground wire. Without it, logic levels float and mux switching will be erratic.
3. **Component values are not in the KiCad schematic/netlist** (all read generic "R"/"C"). The as-built values exist only in your BOM/assembly. Before power, audit with a DMM against the sim: R1 ≈ 60.4 Ω (in-circuit reads ≈ 59.8 Ω because the AD8429's internal 6 kΩ is in parallel), R2 = R3 = 2.2 k, R4 = 10 k, R5–R8 pulldowns (10 k-ish), and **record R9/R10** — you'll use them as current-sense resistors. Then back-annotate values into KiCad so the files are the single source of truth.
4. **External current source required.** Options in order of preference: (a) SMU (Keithley 24xx) at 100 µA, compliance ±2 V; (b) REF200 (two 100 µA sources in one DIP/SOIC, ±0.5 %, 25 ppm/°C) powered from a 9 V battery — beautifully floating and quiet; (c) bench supply + large series resistor (crude; tempco of R dominates). The source **must float** (both terminals swing and get polarity-reversed by the a2 chopper — the chopper reverses the *connection*, so even a unipolar source works). Compliance needed is small: plate ≈ 650 Ω + two mux channels ≈ few hundred Ω → < 0.2 V at 100 µA.
5. **RS6-2415D is a switching converter** (isolated, 9–36 V in, ±15 V out). Expect ripple/spurs in the 100s-of-kHz range on the rails. AD8429 PSRR is high but falls with frequency; spurs can alias into your sampled demod band. Verify the output spectrum in Week 1; mitigations if needed: ferrite + electrolytic bodge on the rails, battery input, or accept (demod rejects out-of-band well). Note there is **no header to inject clean bench ±15 V** — the DC/DC is the only rail path, so characterize it early.
6. **The 2.2 k bias-return resistors load the plate.** Differential source impedance ≈ plate (~650 Ω) + 2× ADG1209 Ron (~120 Ω each) ≈ 0.9 kΩ against a 4.4 kΩ differential load → the amp sees only ≈ 83 % of the open-circuit Hall voltage. This is *identical in sim and hardware* and is absorbed by end-to-end calibration — but remember it when comparing your bench slope to wafer-level S_I ≈ 60 V/A/T. Per-channel Ron mismatch also converts a small fraction of offset into residual after demod; you'll measure that in the sensorless test.
7. **Output drives coax directly** (AD8429 → J4 SMA, 10 k shunt). Watch for ringing with long cables/high C-load; keep the bench cable short, and if you see peaking, add an inline attenuator or a short series-R adapter at the SMA.
8. **Bandwidth trade vs. the 2023 deployment.** The published voltage-bias chain had 1 MHz bandwidth; the spun chain is ~1–2 kHz. Fine for coil ramp (800 ms) and stored-energy tracking (ms), not for fast MHD. Options if you want both in August: record the *raw* v_meas continuously and demodulate offline (keeps everything), and/or use the static-phase "fast mode" — now implemented as the mode-2 firmware (`pico2_static_bias_p2p4.py`, §6.3), which freezes a0/a1/a2 on the p2/p4 axis; for fast events record v_meas on the scope rather than the Pico ADC.
9. **DSUB harness pairing:** make the cable with twisted pairs DSUB(1,2) = sensor p1&p3 (bias pair) and DSUB(6,7) = p2&p4 (sense pair). That pairing minimizes pickup loop area; pins 3,4,5,8,9 are spare (consider grounding one to GND1 as a shield/drain later).

---

## 3. Expected numbers (sanity targets for every test)

With S_I = 60 V/A/T, I = 100 µA, G = 1 + 6 kΩ/60.4 Ω = **100.3**, loading ≈ 0.83–0.87:

| Quantity | At the plate | At v_meas (×100.3) |
|---|---|---|
| Sensitivity (system) | ≈ 6 mV/T → ~5 mV/T after loading | **≈ 0.5–0.6 V/T** |
| Sim plate offset (655/645 bridge) | 0.5 mV | 50 mV raw, alternating per phase table |
| Earth field 50 µT | 0.25–0.3 µV | ~30 µV |
| Helmholtz ±3 mT | ±15–18 µV | ±1.5–1.8 mV |
| HSX ~0.5 T local | ~2.5–3 mV | ~0.25–0.3 V |
| Noise floor (AD8429 1 nV/√Hz + ~0.9 k source ≈ 4–5 nV/√Hz, 1 kHz ENBW) | ~150 nV rms | ~15 µV rms → **~25–30 µT rms resolution** |

Bias current is a free knob: raising I to 0.5–1 mA (the 2023 paper's 0.4 V bias ≈ 0.6 mA) gives 5–10× signal at negligible self-heating (0.65 mW at 1 mA). Characterize S vs I and noise vs I in Week 3 and pick the HSX operating point deliberately.

---

## 4. THIS WEEK (Jul 6–12): power-up + full sensorless verification

**Day 1 — cold checks (no power).**
- Microscope inspection of U1–U4 (TSSOP/SOIC bridges), connector solder.
- DMM value audit per §2.3; record actuals in a board log. Resistance from +15/−15/GND1 to each other (no shorts; expect >10 kΩ-ish through loads).
- Confirm J3 pin order on the physical board silk: 1=a2, 2=a1, 3=a0, 4=en.

**Day 1–2 — first power.**
- Bench supply 24 V into J5, current-limit 100 mA. Verify ±15 V at C-pads/U4.8/U4.5, measure quiescent current, IR/finger thermal check.
- Scope the ±15 V rails AC-coupled: note DC/DC ripple amplitude and frequency (feeds §2.5 decision).

**Day 2 — logic bring-up.**
- Clock source: Raspberry Pi Pico 2, running `firmware/pico2/pico2_spin_scope.py` — **mode 1** of the two-mode firmware (PIO-generated a0/a1/a2 + sync, atomic single-edge updates; 3.3 V logic is fine — ADG1209/ADG5236 V_INH ≈ 2 V). Wiring: GP16/17/18→J3 pins 3/2/1 (a0/a1/a2), GP20→J3 pin 4 (en), GP19→scope sync/trigger, Pico GND→GND1. From the REPL: `start(40000)` raises EN then spins; `hold_state(n)` freezes any of the 8 codes and `survey()` walks all 8 with prompts for the manual survey; `stop()` drops EN before touching the DSUB; `scope_notes()` prints the DSOX1204G capture checklist. The companion **mode 2**, `pico2_static_bias_p2p4.py`, is the scope-free static setup of §6.3. (Zero-code alternative: one wavegen at 40 kHz into a 74HC4040; Q0/Q1/Q2 = a0/a1/a2.)
- **Bond logic ground to GND1** (§2.2). Verify clean 0→3.3 V edges at TP3(a0), TP2(a1), TP1(a2), TP4(en).

**Day 3 — Hall-plate emulator + current source.**
- Build the emulator into a DSUB-9 plug: four 649 Ω (0.1 % if you have them, 1 % fine) wired as the electrical ring p1–p2–p3–p4–p1, which on the DSUB pins is **1 → 6 → 2 → 7 → back to 1** (J1 map: pin1=p1, pin6=p2, pin2=p3, pin7=p4). Solder one 33 kΩ **in parallel** across a single arm (e.g. across pins 1–6, the p1–p2 arm). That pulls the arm from 649 → 636.5 Ω (Δ ≈ −12.5 Ω) and creates a known offset o = I·(R₁₄R₂₃ − R₁₂R₃₄)/ΣR ≈ I·ΔR/4 ≈ **0.31 mV at 100 µA**. Never in series — 33 k in series unbalances the bridge by ~50× and slams the amp into the rail. This is a physical copy of the LTspice model.
- Expected at J4: the amp sees o × loading ≈ 0.315 mV × 0.83 (≈0.9 k bridge+Ron source vs 4.4 k bias-return load) → **steps of ≈ ±26 mV** at the output (0.31 × 100.3 ≈ 31 mV only if you ignore loading). With 1 % resistors the random bridge mismatch (±6.5 Ω/arm) is comparable to the intentional 12.5 Ω — so either use 0.1 % parts, or DMM-measure all four resistors before soldering and predict o exactly with the formula above (turns the emulator into a quantitative gain check).
- Pre-plug DMM signature (with 33 k on p1–p2): opposite pairs pins 1–2 and 6–7 ≈ **646 Ω**; the tagged adjacent pair 1–6 ≈ **480 Ω**; the other three adjacent pairs ≈ **486 Ω**. Caution: solder-cup side of a DSUB is a mirror image of the mating face — go by the numbers molded next to the cups.
- Hook up the current source through J2; verify 100 µA by the drop across R9 at TP6→TP5. **As-built: R9 = R10 = 100 Ω** (confirmed) → expect **10.0 mV per resistor at 100 µA**; 4-wire-measure each resistor's actual value first and divide by that, so current accuracy = DMM voltage accuracy. Measure with a floating DMM across the test points — not a grounded scope probe (the bias loop is referenced to GND1 through the 2.2 k returns; a probe ground clip diverts current). The drop is DC even while spinning (the chopper is downstream of R9/R10); brief spikes at phase edges are the source hitting compliance during break-before-make and are normal. Cross-check V(R9)/R9 = V(R10)/R10 — any mismatch means leakage. Confirm the a2 chopper actually reverses sensor-current direction (watch TP5/TP7 vs a2).
- Static-state survey: hold (a0,a1,a2) at each of the 8 codes by hand (`survey()` in mode 1 steps through them with prompts); record v_meas each state → must reproduce the sign pattern in the §1 table with amplitude G·o. The four p2/p4-axis states (2/3/6/7) can additionally be taken scope-free with the mode-2 firmware and its ADC tap — a useful cross-check that the two acquisition paths agree (§6.3).

**Day 3–4 — gain verification (ΔV method).**
- With phases static, superimpose a known small differential on the selected sense pair (e.g., a 1.000 V source through a 10 kΩ:10 Ω divider across the correct DSUB pins → ~1 mV). Toggle it on/off; ΔV_out/ΔV_in = G. Target 100.3 ± ~1 %. This isolates gain from all offsets.

**Day 4–5 — dynamic spinning + demod.**
- Run f = 40 kHz spinning; single deep capture on the DSOX1204G with **CH-a = v_meas (J4/BNC)** and **CH-b = sync (Pico GP19)** — that's the entire channel budget, leaving 2 channels free for a reference sensor later. Export CSV.
- Run `hsx_demod_scope_csv.py capture.csv --f 40000` (check `--tcol/--vcol/--synccol` and `--skip-header` against your actual export format first). Success criteria with the emulator: raw trace shows the 8-state ±G·o pattern; **demodulated output ≈ 0**, residual ≪ o (quantify — this is your offset-cancellation figure of merit, in volts and in equivalent tesla).
- Characterize switching glitches/settling at phase edges (mux charge injection + AD8429 settling at G=100 is a few µs) → choose a blanking fraction (start at 30 % of each 25 µs phase). Repeat at f = 10 k / 40 k / 100 kHz; residual offset typically grows with f — pick the sweet spot.
- Noise floor: emulator attached, zero field by definition → PSD of demodulated output; express in µT/√Hz.

**Week-1 deliverables:** board log with as-built values; "sensorless verification" memo (gain, 8-state table confirmed, residual offset, noise, chosen f and blanking); working demod script.

### Demod reference implementation
Only 2 scope channels are used — v_meas (J4) and sync (Pico GP19). a0/a1/a2 are never wired to the scope; the phase index at each sample is reconstructed from the sync pulse (high only during state 0) plus the known phase rate f. This is implemented in `hsx_demod_scope_csv.py` (run it directly on your CSV export); the core logic:
```python
import numpy as np

def reconstruct_phase(t, sync, f, thresh=1.65):
    above = sync > thresh
    rising = np.flatnonzero(np.diff(above.astype(int)) == 1) + 1
    t0 = t[rising[0]]                                   # first state-0 edge
    phase = np.floor((t - t0) * f).astype(np.int64) % 8
    phase[t < t0] = -1                                   # unknown before first edge
    return phase

def demodulate(t, v, sync, f, blank_frac=0.3):
    phase = reconstruct_phase(t, sync, f)
    valid = phase >= 0
    v, phase = v[valid], phase[valid]
    sign = np.where((phase & 1) == ((phase >> 2) & 1), 1.0, -1.0)   # a0==a2 rule
    edges = np.flatnonzero(np.diff(phase)) + 1                      # phase boundaries
    segs = np.split(np.arange(len(v)), edges)
    vals, sgns = [], []
    for idx in segs:
        if len(idx) < 10:                                           # runt segment
            continue
        keep = idx[int(blank_frac * len(idx)):]                     # blanking
        vals.append(v[keep].mean()); sgns.append(sign[keep[0]])
    vals, sgns = np.array(vals), np.array(sgns)
    demod = np.convolve(vals * sgns, np.ones(8) / 8, mode='valid')   # rolling 8-phase average
    return vals, sgns, demod
```
Determine the global sign once with a magnet of known polarity, then never touch it again.

---

## 5. THIS MONTH (through early August)

### Week 2 (Jul 13–19): sensor in the loop + Helmholtz build
- Harness: LCC breakout → DSUB per §2.9 pairing. Before connecting: 4-point resistance map of the packaged sensor (p1–p3, p2–p4, adjacents) — log it; this is your incoming-inspection record and your health check at HSX.
- Static magnet sanity: static phase, wave/flip a NdFeB magnet → deflection and sign flip. Fix the global demod sign here.
- Zero-field spun measurement: demodulated residual offset with the real sensor (do a 180° sensor flip and average pairs to remove ambient/Earth field). Compare against the emulator residual — the difference is sensor-specific (contact effects, plate asymmetry).
- Build the Helmholtz pair (§7): print former, wind, measure coil constant three independent ways.

### Week 3 (Jul 20–26): calibration + environment
- DC calibration: bipolar sweep (e.g., 11 points, ±full scale), fit demod output vs B → slope m [V/T], intercept, linearity residuals, up/down hysteresis. The bipolar *slope* is immune to Earth field and any residual offset.
- Repeat at I = 50/100/200/500 µA → confirm m ∝ I (current-scaled sensitivity assumption), pick HSX bias point.
- AC response: sine-drive the coil 10 Hz → 3 kHz → measure the spun chain's transfer function; confirm usable BW and phase lag (matters for correlating with the diamagnetic loop).
- Temperature: sensor (+ emulator as control) on hotplate/oven 25 → 100 °C: demod offset vs T (should now be flat — the headline improvement over the 2023 uncalibrated V_off) and m vs T (expect small; prior work shows S_I stable to 576 °C).
- Overnight drift log at zero field: Allan-deviation-style plot; this is the "long-pulse credibility" figure for the next paper. (The mode-2 firmware's `log_csv` gives a cheap parallel drift record of the un-spun (s − o) channel — log both; the difference is what spinning buys, in one figure.)

### Week 4 (Jul 27–Aug 2): HSX integration rehearsal
- Long-cable test: insert 10–20 m of the actual harness type + feedthrough-equivalent capacitance; re-check settling/blanking; drop f if needed.
- EMI: board in a grounded metal enclosure; re-check DC/DC spurs and demod noise; plan grounding at HSX (single-point to vessel ground; scope/DAQ isolation).
- **Shot rehearsal:** program the wavegen to replay an HSX-like profile into the Helmholtz coil (scaled: 800 ms ramp → 50 ms flat-top → transient) and run the *entire* pipeline end-to-end, including whatever DAQ + trigger scheme UW-Madison will use. Confirm you record v_meas + sync with enough memory for a full shot.
- Coordinate with Wayne/Thomas: DAQ channel count (v_meas + sync minimum; ideally a0/a1/a2 too), trigger timing (remember the ~30 ms diamagnetic-loop offset from last time), where the box sits, and whether coil-only shots can be scheduled for in-situ high-field calibration (§7.4).
- Docs + spares: runbook (power-on sequence, EN reminder, expected voltages at every TP), packed spares (second emulator plug, spare sensor, spare Pico, spare cables), and the written calibration certificate for this sensor S/N.

### Week 5 (Aug 3–9): buffer before travel/install.

---

## 6. How to test — condensed procedures

### 6.1 Without a Hall sensor
1. **Rails & quiescent** — current-limited power-up, ±15 V present, ripple noted.
2. **Logic** — all four lines toggling at TPs; EN high; correct ÷2/÷4/÷8 relationship.
3. **Bridge emulator** (the LTspice plate model made physical) — verifies the entire signal path: current source → chopper → bias mux → "plate" → sense mux → in-amp. Static 8-state survey must match the §1 sign table.
4. **ΔV gain check** — static phase, known 1 mV differential toggled → G = 100.3.
5. **Spinning + demod** — raw pattern amplitude = G·o; demod residual ≈ 0. Quantify residual in µV and equivalent µT.
6. **Glitch/blanking/frequency study** — pick f and blanking fraction.
7. **Noise floor** — PSD of demod output, µT/√Hz.

### 6.2 With the Hall sensor
1. **Resistance map** (incoming inspection, repeated at HSX before/after bake, GDC, and the run).
2. **Static magnet sanity + global sign.**
3. **Zero-field residual offset** (with 180° flip pairs).
4. **Helmholtz DC calibration**: slope, linearity, hysteresis, multi-bias-current.
5. **AC bandwidth** of the spun chain.
6. **Temperature run**: offset(T), sensitivity(T).
7. **Drift log** overnight.
8. **Shot rehearsal** end-to-end.

### 6.3 Second test setup — static DC bias (p2 → p4), sense p1/p3, scope-free

Full definition, wiring, theory and expected numbers:
`second_test_setup_static_bias.md` (this is the summary). Firmware:
`firmware/pico2/pico2_static_bias_p2p4.py` (mode 2).

- The muxes are **parked** in the a1 = 1 states (2/3/6/7): external
  100 µA source biases **p2 → p4**, the AD8429 reads the **p1/p3
  difference**, and the **Pico's ADC** (GP26 ← J4) digitizes — no scope,
  no spinning.
- `measure_chopped()` averages the four states with signs {+, −, −, +}:
  amplifier offset e cancels exactly; the result is (s − o)·loading·G.
  The **plate offset o does not cancel** (single bias axis — that's the
  physics; separating s from o is what the full 8-state spin is for).
  At zero field the result *is* the raw plate offset — the incoming-
  inspection number for the gen-2 dies (RSI plan §2.1).
- Uses: 30-second sensor health checks without the scope cart; raw-offset
  surveys; drift logging (`log_csv`) as a cheap complement to the Week-3
  overnight run; continuity checks against the 2023 static-bias style;
  and the "fast mode" fallback of §2.8 (static phase = full amplifier
  bandwidth).
- Limits: unipolar 0–3.3 V ADC (negative states clamp — firmware warns;
  level-shift network documented in the setup doc) and ~0.8 mV/LSB
  resolution (≈ sub-mV effective with 256× oversampling) — health-check
  grade, never calibration grade.

---

## 7. Low-budget calibration testbench (target < $100 in parts)

### 7.1 Helmholtz pair (the field source *and* your primary standard)
A Helmholtz coil is a *calculable* standard: B = (4/5)^{3/2}·µ0·N·I / R = 0.7155·µ0·N·I/R, uniform to <0.1 % within ±0.1 R of center (your 200 µm die + LCC alignment is trivially inside this).

**Recipe:** mean radius R = 50 mm, spacing = R, N = 100 turns/coil of AWG 20–22 magnet wire, series-connected (fields aiding), on a 3D-printed former with a printed cradle that registers the LCC/DSUB fixture at center, sensor plane ⊥ axis.
- k = B/I ≈ **1.8 mT/A** → ±1.5 A gives ±2.7 mT (plenty to fit a slope; output ≈ ±1.6 mV — well above the ~15 µV noise floor after demod averaging).
- Winding resistance ≈ 3.3 Ω (AWG 22) → ~5 V, ~7 W at 1.5 A: fine for sweeps, duty-cycle for long runs (or use AWG 20).
- Drive: bench supply in current mode for DC points; scope wavegen (possibly through a small audio amp) for AC and shot-replay.

### 7.2 Traceability — triangulate the coil constant three ways
1. **Geometry** (primary): measure mean winding radius and spacing with calipers → k from the formula. Dominant uncertainty is the finite winding-bundle cross-section; ~1–2 % achievable. Measure current with a 4-wire 0.1 % shunt (e.g., 1 Ω) + DMM.
2. **AC pickup coil** (independent physics): wind N_p ≈ 50 turns on a printed 10 mm form of known area; drive the Helmholtz at 1 kHz; V_rms = 2π f N_p A B_rms → k to ~2–3 %.
3. **Commercial sensor cross-check** (your original idea — good, use it as the *check*, not the primary): DRV5055A1 breakout (analog, 100 mV/mT, ±21 mT) and/or TLE493D-W2B6 or MLX90393 (digital I²C via the Pico, sub-µT resolution). These are ±2–5 % class parts; agreement of all three methods within a few % validates the bench.
4. **High-field extension (free/borrowed):** the Helmholtz can't reach HSX's ~0.5 T. Two paths: (a) borrow electromagnet + gaussmeter time (the lab's prior high-T Hall characterization implies access); (b) **use HSX coil-only shots as the in-situ high-field reference** — the vacuum field at your sensor location is computable from coil currents via the HSX field model, and this directly delivers the "in-situ cross-reference with established HSX diagnostics" flagged as future work in the Letters paper. Ask the UW team for the modeled |B| at your mounting location vs. coil current.

### 7.3 "Accuracy of calibration" protocol
1. **Calibrate:** bipolar sweep, fit V_demod = m·B + b on a training subset of field points.
2. **Verify:** apply held-out field values (interleaved, both polarities, plus a few AC amplitudes and one elevated temperature); predict B from m and compare to the coil-constant reference → report % error vs field, worst-case and RMS.
3. **Close the loop on first principles:** compare m to G·S_I·I·(loading) — should agree within the loading-factor uncertainty; a large gap means a wiring/value surprise.
4. **Uncertainty budget** (expected): coil constant 1.5–2 %, current 0.1 %, alignment cos-error (<3°) 0.15 %, temperature 0.1–0.5 %, noise ≪ 0.1 % after averaging → **~2 % absolute, <0.5 % relative/linearity** — a major step from "uncalibrated," and honest to quote in the next paper.

### 7.4 Shopping list (approx.)
| Item | ~Cost |
|---|---|
| Magnet wire AWG 20–22, ~150 m | $20 |
| 3D-printed former + sensor cradle | ~$5 filament |
| RP2040 Pico (clocks + I²C reference readout) | $5 |
| REF200 current source + 9 V battery clip | $8 |
| DRV5055A1 + TLE493D/MLX90393 breakouts | $15 |
| 1 Ω 0.1 % 4-wire shunt | $6 |
| 649 Ω 0.1 % ×8 + assorted (emulator ×2) | $8 |
| DSUB-9 plugs/hoods ×3, SMA cable | $15 |
| NdFeB magnets (sign checks) | $8 |
| **Total** | **≈ $90** |

Assumes existing: DSOX1204G scope/wavegen, bench supply, DMM.

---

## 8. Risk register (August-facing)
| Risk | Mitigation |
|---|---|
| EN not driven → dead board at HSX | Runbook step 1; LED or scope check on TP4 |
| Logic ground unbonded | Dedicated ground wire in harness; document it |
| Demod BW (~1–2 kHz) hides ignition transient detail | Record raw v_meas at ≥1 MS/s and demod offline; static-phase fast mode (mode-2 firmware, §6.3) |
| DC/DC spurs alias into data | Week-1 spectrum check; ferrite/battery fallback |
| Current source drift over a run day | REF200/SMU + log R9 drop each shot block |
| Charge-injection residual at chosen f | Week-1 frequency study; freeze f + blanking before Week 3 calibration |
| Cable capacitance breaks settling at HSX lengths | Week-4 long-cable rehearsal |
| Sensor damage during bake/GDC | Resistance map before/after every environment step |

---

*Cross-check summary: bias mux, sense mux, chopper cross-wiring, in-amp pinout (−IN/+IN/RG/REF/OUT/rails), bias-return resistors, and output network all correspond one-to-one between `hall_sensor_measurement_system_v1.net` and `hsx_2026_v1.net`. The three intentional differences (external current source, external logic with pulled-down EN, DC/DC-generated rails) are integration items, not design errors.*
