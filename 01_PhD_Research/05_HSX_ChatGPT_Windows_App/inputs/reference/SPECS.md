# SPECS — HSX Hall-sensor readout quick reference

One page, every key number. If a value here disagrees with the bench,
the bench wins — measure, then fix this file. Derivations and procedures
live in `hsx_readout_bringup_and_calibration_plan.md`; this file is for
looking things up fast (or via `/specs` in Claude Code).

## System at a glance

| Parameter | Value | Notes |
|---|---|---|
| Bias | 100 µA current bias, external source | via J2/J7 loop; NOT on the board |
| Sensor sensitivity S_I | ≈ 60 V/A/T | current-scaled; 2DEG, weak T-dependence |
| Amplifier | AD8429, G = 100.3 | R_G = 60.4 Ω (reads ≈ 59.8 Ω in-circuit) |
| System sensitivity | ≈ 0.5–0.6 V/T at output | S_I · I · loading (≈0.83) · G |
| Spinning rate f | 40 kHz nominal (10k–100k usable) | f = phase rate |
| Timing @ 40 kHz | 25 µs/phase · 8 = 200 µs cycle | 5 kHz update, ~1–2 kHz usable BW |
| Rails | ±15 V from RS6-2415D DC/DC | input 24 V on J5; expect switching spurs |
| Output | J4 (SMA), R4 = 10 kΩ shunt to GND1 | 2-ch capture: v_meas + sync only |
| Logic | 3.3 V from Pico 2 is sufficient | mux V_INH ≈ 2 V |

## Sensor & package

| Item | 2023 die (Letters) | Gen-2 die (2026, for vector probe) |
|---|---|---|
| Plate | regular octagon, 200 µm inscribed dia. | same geometry assumed |
| Bond pads | as fabricated 2023 | **enlarged** — re-verify before reuse of old numbers |
| Stack | NTT AlGaN/GaN: 22 nm Al₀.₂₈Ga₀.₇₂N / 1 nm AlN / 300 nm GaN / 3.7 µm buffer | same wafer family |
| Plate resistance | ≈ 650 Ω terminal-to-terminal (model 645–655) | **re-measure**; sets emulator + loading |
| Package | ceramic LCC (Spectrum), Al wire, EPO-TEK 353ND, 150 °C vacuum bake 1 h | same LCC; cube mounts 2–3 of them |
| TCAD calibration (Van Gorp draft) | S_i = 54.67 V/A/T, S_v = 93.74 V/V/T, n_s = 8.38×10¹² cm⁻², µ = 1807 cm²/V·s | 100 µm octagon model |

## Spinning phase table

`state = (a2<<2) | (a1<<1) | a0`, advancing 0→7 each phase. Demod sign:
**+1 if a0 == a2 else −1** (a1 is irrelevant to the sign). Raw per-cycle
sign pattern: `+ − − + − + + −`. Plate offset cancels across a1 pairs,
amplifier offset across a0 pairs, and the a2 (chopper) reversal removes
second-order residuals. Global sign is fixed empirically with a known
magnet — never from the netlist.

| state | a2 a1 a0 | demod sign |
|---|---|---|
| 0 | 0 0 0 | + |
| 1 | 0 0 1 | − |
| 2 | 0 1 0 | + (a1 flip: plate-offset pair with 0) |
| 3 | 0 1 1 | − |
| 4 | 1 0 0 | − (a2 flip: chopper reversal) |
| 5 | 1 0 1 | + |
| 6 | 1 1 0 | − |
| 7 | 1 1 1 | + |

Sync (scope CH-b) is high only during state 0. Demod uses 30 % blanking
per phase and discards runt segments (see `analysis/`).

## Pin & connector maps

**J1 (DSUB-9, sensor):** pin 1 = p1, pin 2 = p3, pin 6 = p2, pin 7 = p4.
Opposite plate pairs are (p1,p2) and (p3,p4).

**J3 (logic, 4-pin):** 1 = a2, 2 = a1, 3 = a0, 4 = en. **No ground pin**
— bond logic ground to GND1 separately. EN has an on-board pulldown:
board is dead until EN is driven ≥ 2 V.

**J2 / J7 (bias current loop):** external 100 µA source enters here
through R9 = R10 = 100 Ω sense resistors (10 mV each at 100 µA; DC even
while spinning, since the chopper is downstream). Measure with a
floating DMM: TP6→TP5 and TP8→TP7. Grounded scope probes here short the
loop. V(R9)/R9 = V(R10)/R10 is the leakage check.

**Test points:** TP1 = a2, TP2 = a1, TP3 = a0, TP4 = en, TP5 = ibin,
TP6 = J2.1, TP7 = ibout, TP8 = J2.2.

**Pico 2 (GPIO / physical pin):** a0 = GP16/21, a1 = GP17/22,
a2 = GP18/24, sync = GP19/25, en = GP20/26, GND = pin 23 → GND1. One
contiguous header strip, pins 21–26. Full table:
`firmware/pico2/README.md`.

## Bring-up plug (bridge emulator)

Four 649 Ω resistors in a ring across DSUB pins 1→6→2→7→1, with 33 kΩ
**in parallel** across one arm (pins 1–6) → that arm 636.5 Ω (Δ −12.5 Ω).
Raw bridge signal ≈ 0.315 mV at 100 µA; × 0.83 loading (≈0.9 k source vs
≈4.4 k load) × 100.3 gain → **±26 mV output steps** (not 31 mV — loading
matters). Never put the 33 k in series: that unbalances ~50× and rails
the amplifier.

Pre-plug DMM signature: opposite pairs (1–2, 6–7) ≈ 646 Ω; the tagged
adjacent pair (1–6) ≈ 480 Ω; other adjacents ≈ 486 Ω.

## Expected numbers

| Quantity | Value |
|---|---|
| HSX field at probe (~0.5 T) | ≈ 0.25–0.3 V at output |
| Earth's field (~50 µT) | ≈ 30 µV — below casual bench resolution |
| Noise floor | ≈ 25–30 µT rms at 1 kHz ENBW, 100 µA bias |
| Emulator step | ±26 mV, pattern `+ − − + − + + −` per cycle |
| Helmholtz drive | ±2.7 mT at ±1.5 A |

## Calibration constants & targets

Helmholtz pair: R = 50 mm, N = 100 turns/coil (AWG 20–22),
B = 0.7155·µ₀·N·I/R → k ≈ 1.8 mT/A. Budget ≈ $90. Traceability:
geometry + 0.1 % shunt, cross-checked by AC pickup coil and a
DRV5055A1 / TLE493D / MLX90393 reference on the Pico I²C bus; absolute
in-situ anchor = HSX coil-only shots. Targets: ~2 % absolute, < 0.5 %
linearity over ±2.5 mT, sensitivity vs I linear at 50/100/200/500 µA.

## 2023 system vs this system

| | 2023 (Letters) | 2026 (this readout) |
|---|---|---|
| Bias | 0.4 V voltage bias | 100 µA current bias |
| Offset handling | none (V_off uncalibrated) | 4-phase spinning + chopper |
| Amplifier chain | INA849 + 2×OPA814, G = 200 | AD8429, G = 100.3 |
| Bandwidth | 1 MHz raw | ~1–2 kHz demodulated (raw capture available) |
| Calibration | none (temporal correlation only) | absolute, Helmholtz + in-situ |
| Axes | 1 | 1 (→ 2–3 in project 03) |

## Gotchas (one-liners)

EN pulldown (drive it or the board is dead) · no GND on J3 (bond it) ·
current source is external (sim's ideal source doesn't exist) · DC/DC
spurs on the ±15 V rails · demod BW ≈ 1–2 kHz at f = 40 kHz — record raw
v_meas for fast transients. Details: `CLAUDE.md` §gotchas and plan §2.

## Vector-probe deltas (project 03)

×3 replicated boards from existing gerbers · one Pico fans out shared
a0/a1/a2/EN (synchronized spinning) · per-board floating 100 µA sources ·
12-conductor harness (DB-15 or 2×DSUB-9 — feedthrough TBD with UW) ·
DSOX1204G 4 ch = v_x, v_y, v_z + sync. Plan:
`../03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md`.
