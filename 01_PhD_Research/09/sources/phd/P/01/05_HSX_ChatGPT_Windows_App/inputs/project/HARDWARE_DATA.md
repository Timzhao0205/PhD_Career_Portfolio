# HARDWARE_DATA — ground truth for the review (do not re-derive; verify against datasheets)

All of the following is given. Part *specs* still must be datasheet-verified per
SOURCE_STANDARDS; the *design facts* (what is placed, values, pin maps) are authoritative
here. Source of the BOM/netlist below: `hsx_2026_v2` KiCad project (netlist parsed
2026-07-09).

## 1. Board `hsx_2026_v2` — as-built component list (from the v2 netlist)

| Ref | Part | Function |
|---|---|---|
| U1 | ADG1209YRUZ (4:1 diff mux) | **bias**-steering mux |
| U2 | ADG1209YRUZ (4:1 diff mux) | **sense**-steering mux |
| U3 | ADG5236BRUZ (dual SPDT, latch-up-proof) | bias-polarity **chopper** |
| U4 | AD8429ARZ (instrumentation amp) | readout in-amp, **G = 100.3** (R1 = R_G = 60.4 Ω) |
| U5 | RS6-2415D (isolated DC/DC) | **±15 V** rails from a 24 V input |
| J1 | **Amphenol D09S33E6GX00LF** (DSUB-9 socket) | **sensor connector — the v2 update (Digi-Key)** |
| J4 | Molex 73100-0105 (SMA edge jack) | v_meas output to scope |
| J2, J7 | 1×02 headers | external bias-current loop in/out |
| J5, J6 | 1×02 headers | power input (24 V) |
| J3 | 1×04 header | logic: a0/a1/a2/EN from the Pico |
| TP1–TP8 | RCU-0C test points | a2/a1/a0/EN (TP1–4), ib_in/J2.1/ib_out/J2.2 (TP5–8) |
| R1 | 0603 | R_G = **60.4 Ω** (SMD code "76X", DMM-confirmed) → G = 100.3 |
| R2, R3 | 0805 | in-amp bias-return resistors, **2.2 kΩ** each → GND1 |
| R4 | 0805 | output load, **10 kΩ** to GND1 (at J4) |
| R5–R8 | 0805 | logic pulldowns (a0/a1/a2/EN) |
| R9, R10 | 0805 | bias-current **sense resistors, 100 Ω each** (as-built, confirmed) |
| C1–C10 | 0805 | decoupling / rail filtering |

**Note (fact, not a judgment):** the project *libraries* include `ADA4898-2YRDZ` (dual
low-noise op-amp) symbol/footprint, but **no ADA4898 is placed** in the v2 schematic or
netlist. v2 is topologically identical to v1 except J1 was changed to the specific Amphenol
`D09S33E6GX00LF` DSUB-9 part.

## 2. Verified electrical facts (inherited, settled — do not "correct")

- Bias: **100 µA current bias**, external source via J2 (∥ J7) through R9/R10; source must
  float. S_I ≈ 60 V/A/T (AlGaN/GaN, current-scaled; stable with T per Alpert 2020).
- In-amp gain G = 1 + 6 kΩ/R_G = **100.3** (R_G = 60.4 Ω; reads ≈ 59.8 Ω in-circuit).
- Loading factor ≈ **0.83** at RT (≈0.9 kΩ plate+Ron source vs 4.4 kΩ bias-return load).
- System sensitivity ≈ **0.5–0.6 V/T** at output, 100 µA.
- Spinning: **8-phase**, `state = (a2<<2)|(a1<<1)|a0`; demod sign **+1 if a0==a2 else −1**.
  Nominal phase rate f = 40 kHz (10k–100k usable); demod cycle 8/f → update f/8, usable
  demodulated BW ~1–2 kHz at 40 kHz.
- Rails: ±15 V from RS6-2415D (switching spurs in the 100s of kHz on the rails).

## 3. Pin & connector maps (authoritative)

- **J1 (DSUB-9, sensor):** pin 1 = p1, pin 2 = p3, pin 6 = p2, pin 7 = p4. Opposite plate
  pairs (p1,p2) and (p3,p4). Pins 3/4/5/8/9 spare.
- **J3 (logic, 4-pin):** 1 = a2, 2 = a1, 3 = a0, 4 = EN. **No ground pin** — logic ground
  must be bonded to GND1 separately. EN has an on-board pulldown (board dead until EN ≥ 2 V).
- **J2/J7 (bias loop):** external 100 µA source through R9 = R10 = 100 Ω sense resistors.
- **Pico 2 → board (single-axis):** GP16→J3.3 (a0), GP17→J3.2 (a1), GP18→J3.1 (a2),
  GP20→J3.4 (EN), GP19→scope sync, Pico GND→GND1.
- Logic threshold of the ADG1209/ADG5236: V_INH ≈ 2 V (3.3 V Pico logic is sufficient).

## 4. LOCKED CONSTRAINTS for this review (given by the user — do not question)

1. **Bandwidth:** 10–20 kHz *after* current-spinning recombination is sufficient. Do NOT
   optimize for 1 MHz or raw-signal bandwidth.
2. **Physical architecture across the flange (CONFIRMED by the user):** the **CF feedthrough
   flange is the boundary**.
   - **Inside the vessel** (plasma side, hot, UHV): the **zirconia-ceramic 3D package** (the
     cube/mount of ST8) holding the **3× LCC02046 chip carriers** and the **AlGaN/GaN Hall
     sensor dies**. Nothing else electronic is in-vessel.
   - **Outside the vessel** (air side, **~ambient**): the **`hsx_2026_v2` readout board(s)**
     (mux/chopper/in-amp/DC-DC). No high-temperature de-rating of the *readout electronics* —
     out of scope.
   - The **12 signal conductors** cross the boundary through the feedthrough. So ST5/ST6 (flange
     + harness) span the boundary; ST8 (zirconia package) is entirely in-vessel; ST1–ST4/ST7 are
     the air-side board (except ST7's carrier, which is in-vessel).
3. **Vector target:** scale to **3 sensors (3 axes)** = **3 × 4 = 12 signal conductors**
   (plus shields/returns). Three "sets of components" (three readout channels).
4. **Current feedthrough:** Accu-Glass **9D-275** (9-pin sub-D, 2.75″ CF). See REFERENCE_DATA
   for the family menu; must move to a ≥12-conductor option meeting the same ratings.
5. **Primary worry:** multi-sensor **wiring and short-circuit** risk.

## 5. Current bench status (context for trust, not for magnitude)

- Latest run (2026-07-08): emulator bridge (4×680 Ω + 2.2 kΩ across p1–p2), 20 mA, 20 kHz
  spin. Spinning + demod **works** (offset 686 mV → ≤5 mV). But an **open anomaly** remains:
  measured output is ~109× below what 680 Ω + 2.2 kΩ + 20 mA + gain 100.3 predicts (which
  would rail). R9 = R10 = 2.0 V rules out leakage; R_G = 60.4 Ω present. Surviving
  explanations: (a) in-operation gain ≠ ~100×, or (b) the 2.2 kΩ not electrically
  unbalancing the bridge. **Unresolved — the ΔV gain check is pending.**
  ⇒ Do not use measured amplitudes as evidence in this review until resolved.

## 6. Reference documents that belong with this pack (attach if available)

- `SPECS.md` (single-axis quick reference: phase table, pin maps, gains, expected numbers).
- `hsx_readout_bringup_and_calibration_plan.md` (bring-up plan, §2 gotchas, §7 testbench).
- `rsi_experiment_and_publication_plan.md` (the 3-axis vector-probe plan: §2.3 replicate
  board ×3, one Pico fans out shared a0/a1/a2/EN, per-board floating 100 µA sources; §2.4
  harness = 12 conductors, DB-15 or 2×DSUB-9; §2.5 DAQ).
- Alpert et al., RSI 91, 025003 (2020) — S_I(T), µ ∝ (T/300)^−2.35 (sensor side only).
