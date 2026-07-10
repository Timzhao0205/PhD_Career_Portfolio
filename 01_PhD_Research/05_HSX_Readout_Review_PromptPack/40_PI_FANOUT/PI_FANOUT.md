# ST4 — Raspberry Pi Pico 2 Fan-Out to 3 Boards (Q4)

**BLUF / verdict:** **KEEP direct fan-out.** One Pico 2 driving a0/a1/a2/EN into 3× `hsx_2026_v2`
boards (6 CMOS logic inputs per shared line, plus 3 on-board pulldowns) needs **no logic
buffer, no series termination, and no drive-strength increase to function** — RC settle time
on each shared line is ~3–4 orders of magnitude shorter than the 25 µs (40 kHz nominal) /
10 µs (100 kHz usable) phase period, and the added DC pulldown sink current is ~4 mA total vs
a ≥50 mA GPIO budget (RP2040 precedent). The one thing that **does** change is **ground
distribution**: J3 has no ground pin, so with 3 boards the logic return must be **home-run
("star") from the Pico to each board's GND1**, not daisy-chained board-to-board. A logic
buffer (74LVC-class) only becomes numerically necessary beyond **~7 m of twisted-pair harness
per line** (conservative bound, see §5) — far beyond the <1–2 m bench/rack run expected here.

---

## 1. Fan-out count (per HARDWARE_DATA §1/§3, authoritative — not re-derived)

| Shared line | Destinations on ONE board | CMOS inputs / board | ×3 boards |
|---|---|---|---|
| a0 | U1 (ADG1209 bias mux) A0, U2 (ADG1209 sense mux) A0 | 2 | **6** |
| a1 | U1.A1, U2.A1 | 2 | **6** |
| a2 | U3 (ADG5236 chopper) IN1, IN2 | 2 (**assumption**, see §6) | **6** |
| EN | U1.EN, U2.EN | 2 | **6** |

Each board also has one on-board pulldown (R5–R8, one per line) — see §4.

Basis: HARDWARE_DATA §2 phase encoding `state=(a2<<2)|(a1<<1)|a0` requires a0/a1 as the 2-bit
mux address (present on both differential muxes U1, U2 — a 4:1 diff mux needs 2 address bits)
and a2 as the chopper polarity bit on U3. EN is stated explicitly in the task scope as "U1+U2
enables" only (ADG5236/U3 has no separate EN pin in this design per the given netlist facts —
not independently re-verified this session, treated as authoritative per CLAUDE.md §4).

## 2. Capacitive load per shared line (×3 boards + harness)

| Element | Value | Basis |
|---|---|---|
| ADG1209/ADG5236 digital-input C_IN, per pin | **UNVERIFIED — engineering judgment 5 pF** | 9 fetch attempts on the ADI ADG1208/1209 (Rev. E) and ADG5236 (Rev. B) PDFs and 6 mirrors (alldatasheet, octopart, digchip, datasheetq, radiolocman, datasheetarchive) all failed (timeout / ECONNRESET / binary-not-renderable — no `pdftoppm` available to this agent to render the saved PDF binaries). Value is a conservative high-side estimate for ADI iCMOS/latch-up-proof switch control pins of this class; used because it does not change the verdict (see §5 margin). |
| CMOS inputs per line ×3 boards | 6 pins | §1 |
| **Total silicon C** | 6 × 5 pF = **30 pF** | calc |
| Cable/harness, line-to-return | **50 pF/m** (assumption, mid-range) | Samtec 100 Ω 28 AWG shielded twisted pair: 13.6 pF/ft ≈ 44.6 pF/m [Samtec TPS-28100-RF datasheet]; Weico 28 AWG multipair low-C: 15.5 pF/ft ≈ 50.9 pF/m [Weico 28 AWG product page] — averaged/rounded to 50 pF/m |
| Assumed harness length, Pico → board stack | **1.0 m** (assumption — bench/rack distance, stated in ASSUMPTIONS) | engineering judgment; realistic range 0.3–1 m |
| Cable C @ 1.0 m | **50 pF** | 50 pF/m × 1.0 m |
| **Total per-line load, base case** | **≈ 80 pF** | 30 pF (ICs) + 50 pF (cable) |

Range if C_IN is 2× the assumed value or harness is 2 m: **~130–180 pF** — still trivial (see §5).

## 3. Edge-rate margin

Phase period at nominal 40 kHz = 1/40 kHz = **25 µs**; at the 100 kHz usable ceiling =
**10 µs** (HARDWARE_DATA §2). Logic edges must settle in a small fraction of this.

- Pico 2 (RP2350) GPIO drive strength is software-selectable **2/4/8/12 mA**, same
  register/SDK scheme as RP2040 (`GPIO_DRIVE_STRENGTH_2MA/4MA/8MA/12MA`;
  `PADS_BANK0_GPIOx_DRIVE_VALUE_12MA` register field confirmed present for RP2350 in SDK
  headers found in search). Exact RP2350 output-impedance table (§14.9.4 "IO Electrical
  Characteristics" per a user's forum citation of the datasheet) **could not be fetched this
  session** (repeated timeout/ECONNRESET on `datasheets.raspberrypi.com` and 3 mirrors) —
  **UNVERIFIED**, RP2040 precedent used instead: drive-strength options "2 mA, 4 mA, 8 mA or
  12 mA" [RP2040 datasheet p.255, reproduced in Raspberry Pi forum thread
  `viewtopic.php?t=300735`] and total IOVDD current budget **≤50 mA** aggregate across all
  GPIOs [Raspberry Pi engineer "jamesh," same forum thread]. RP2350 shares the same GPIO/pad
  architecture per the SDK constants above; treated as ≥ RP2040 capability.
- Output impedance R_o: used a **conservative bound of 50 Ω** (engineering judgment — worst
  case for a 3.3 V CMOS pad even at reduced drive-strength settings; actual R_o at 12 mA
  setting is typically well under this for parts in this class).

**τ = R_o × C = 50 Ω × 100 pF (mid-range load) = 5 ns. Settle to <1% (5τ) = 25 ns.**

| Phase rate | Period | 5τ (settle) | Margin |
|---|---|---|---|
| 40 kHz (nominal) | 25 µs | 25 ns | **~1000×** |
| 100 kHz (usable ceiling) | 10 µs | 25 ns | **~400×** |

Even doubling every conservative input (C→200 pF, R_o→100 Ω → 5τ = 500 ns) still leaves
**20× margin at 100 kHz**. Direct fan-out is not edge-rate-limited at any length relevant to
this build.

## 4. DC pulldown load (R5–R8, ×3 boards)

- R5–R8 value **not given** in HARDWARE_DATA/netlist. **Assumption:** treat as "~10 kΩ class"
  per the task's own fallback instruction (logged to §6).
- 3 boards' pulldowns in parallel per line: R_eff = 10 kΩ/3 = **3.33 kΩ**.
- Sink current when line driven HIGH (3.3 V): I = 3.3 V / 3.33 kΩ = **0.99 mA ≈ 1 mA/line**.
- Worst case, all 4 lines HIGH simultaneously: **~4 mA total** added Pico source current.
- Against a 12 mA single-pin drive-strength rating: **>10× margin per pin**. Against the
  ≤50 mA aggregate IOVDD budget (RP2040 precedent, §3): **>12× margin** even before
  accounting for the rest of the Pico's own load. **No extra "signal power" is needed** — Q4's
  literal question ("need more signal power?") is answered **no**.

## 5. Threshold at which a buffer becomes necessary

Requirement: 5τ ≤ 1% of the fastest usable phase period (100 kHz, T = 10 µs) → 5τ ≤ 100 ns →
τ ≤ 20 ns → **C_max,line = τ / R_o = 20 ns / 50 Ω = 400 pF** (conservative R_o).

- Fixed silicon load (3 boards): 30 pF.
- Cable budget: 400 pF − 30 pF = 370 pF → at 50 pF/m → **L_max ≈ 7.4 m** of twisted-pair
  harness per line before a 74LVC-class buffer/re-clock is numerically required, at the
  strictest (100 kHz) operating point.
- At the nominal 40 kHz operating point the same margin math gives ≈**18 m**.

**Realistic harness (Pico near the 3-board stack, bench/rack setup): <1–2 m ⇒ 3.5–7×
length margin under the conservative case.** Verdict: **buffer not needed now; the numeric
trigger is ~7 m/line (worst case) to ~18 m/line (nominal-rate case) of twisted-pair harness,
or equivalently >≈400 pF on any one shared line.**

If a rev-B packaging decision (ST3/ST8) ever puts the Pico far from the board stack (e.g.
routed through the same long run as the sensor harness), re-check this budget — at that point
a **74LVC1G/74LVC2G-class buffer** (e.g. **74LVC2G34 dual buffer, SOT-363**,
https://www.ti.com/product/SN74LVC2G34 — TI product page, keep-or-add candidate only, not
independently pin/spec-verified this session since it is not needed now) placed at the Pico
end of each line would restore margin.

## 6. Ground / sync distribution — this DOES change with 3 boards

- J3 has **no ground pin** (HARDWARE_DATA §3, authoritative) — logic ground must be bonded to
  each board's GND1 by a separate conductor, same as the single-axis case.
- **Do not daisy-chain GND1 board-to-board.** With 3 boards sharing a0/a1/a2/EN, a daisy-chain
  return puts the 10–100 kHz spin-rate switching current of boards 2 and 3 through board 1's
  ground path (or vice versa), producing a common-impedance IR-drop that appears as a
  common-mode disturbance at another board's in-amp reference — exactly the kind of
  offset/noise coupling current-spinning was adopted to eliminate (HARDWARE_DATA §4 locked
  lens: low-noise, offset-free).
- **Recommended:** home-run ("star") ground — a dedicated return conductor from the Pico to
  each board's GND1 (3 individual returns, not 1 shared bus), and pair each of the 4 logic
  lines with its own return in the harness (twisted pair per line: a0+ret, a1+ret, a2+ret,
  EN+ret — 8 conductors total for logic instead of 4 signal + 1 shared ground) to keep the
  fast edges locally referenced per board and minimize loop area. This is a **harness
  conductor-count change** (mechanical/BOM, not a Pico-side electrical change) — flag for
  ST6 (wiring/harness plan) to carry forward.
- **GP19 sync → scope:** unaffected by the ×3 board fan-out (it does not drive mux/chopper
  logic; it is a single lightly-loaded net to a scope/DAQ input, typically ~1 MΩ ∥ ~10–15 pF).
  No change needed.
- **EN:** fans out the same as a0/a1/a2 (§1–§5, no incremental concern). Note as a **design
  choice, not a requirement**: sharing one EN across all 3 boards means all axes enable/disable
  together. If independent per-axis enable is wanted for bring-up/debug (e.g. isolating one
  channel's chopper during fault-finding), that needs 3 separate Pico GPIOs instead of 1 shared
  EN — this is a **rev-B nice-to-have**, not needed for the Aug 2026 single/first 3-axis build.

## 7. Needed-now vs rev-B

| Item | Needed now | Rev-B / nice-to-have |
|---|---|---|
| Direct fan-out (no buffer) | ✅ keep | — |
| GPIO drive strength 8/12 mA in firmware | ✅ cheap, do it (extra margin, zero cost) | — |
| Star ground (Pico→3×GND1, per-line returns) | ✅ needed to avoid cross-channel coupling | — |
| 74LVC-class buffer per line | — | only if harness later exceeds ~7 m/line |
| Independent per-axis EN (3 GPIOs) | — | optional, for per-channel debug isolation |

## 8. Failure mode if wrong

If the verdict is wrong in the "add buffer" direction (i.e., a buffer is skipped when it was
actually needed): edges on a0/a1/a2/EN slew too slowly relative to the phase period, so the
mux/chopper state hasn't settled before the next phase transition — this shows up as
inter-phase crosstalk/blanking-glitch growth and a demodulated-offset residual that scales with
harness length, not as an outright board fault. If the verdict is wrong in the "ground" call
(daisy-chained instead of star grounds are used): a slow, hard-to-diagnose per-board offset or
noise floor increase appears that correlates with which board is physically farthest from the
Pico — easily mistaken for a sensor or in-amp problem rather than a wiring topology problem.

---

## Assumptions made (this subtask)

1. ADG1209/ADG5236 digital-input capacitance C_IN = 5 pF/pin — **UNVERIFIED**, datasheet fetch
   failed after 9 attempts across primary + 6 mirror sources; engineering-judgment estimate,
   conservative (high) for this device class; does not change the verdict given the >400×
   margin at the base case.
2. RP2350 GPIO output impedance R_o ≤ 50 Ω (conservative bound) and drive-strength scheme
   matching RP2040 (2/4/8/12 mA) — RP2350-specific datasheet electrical table **UNVERIFIED**
   (fetch failed); RP2040 precedent + RP2350 SDK register-name cross-reference used instead.
3. Harness: twisted-pair/ribbon, 50 pF/m line-to-return, 1.0 m Pico-to-board-stack length —
   assumption per task instruction; backed by 2 real 28 AWG twisted-pair cable datasheets
   (44.6–50.9 pF/m) for the pF/m figure, but the exact cable product and length are not yet
   selected (that's a §6/ST6 harness decision).
4. R5–R8 (logic pulldowns) = "~10 kΩ class" — value not given in HARDWARE_DATA/netlist;
   per task fallback instruction.
5. a2 drives both ADG5236 IN1 and IN2 directly (2 CMOS inputs), no on-board inverter — inferred
   from the 8-phase encoding in HARDWARE_DATA §2 and the absence of any logic-inverter IC in
   the BOM (HARDWARE_DATA §1); not independently confirmed against the live netlist file (this
   subtask did not have `hsx_2026_v2.net` access — flagging for ST2 to cross-check).
6. Total IOVDD/GPIO current budget ≤50 mA taken from RP2040 datasheet p.255 (via forum
   reproduction) as a stand-in for RP2350; RP2350's actual figure could not be fetched this
   session but is expected to be ≥ this given the newer/larger die.

## Sources

- HARDWARE_DATA.md §1–§4 (authoritative design facts: BOM, pin maps, phase encoding, V_INH≈2V) — local file, this pack.
- Samtec TPS-28100-RF, 100 Ω 28 AWG shielded twisted pair, 13.6 pF/ft nominal: https://suddendocs.samtec.com/notesandwhitepapers/tps-28100-rf_datasheet.pdf
- Weico 28 AWG multipair, dual shield, low-capacitance cable, 15.5 pF/ft conductor-to-conductor: https://www.weicowire.com/28-awg.html
- Raspberry Pi Forums, "GPIO Current Rating" (RP2040 drive-strength table p.255 citation + Raspberry Pi engineer statement on ≤50 mA IOVDD budget): https://forums.raspberrypi.com/viewtopic.php?t=300735
- Raspberry Pi Forums, "RUN and GPIO electrical specs for RP2350" (points to RP2350 datasheet §14.9.4 IO Electrical Characteristics — table itself not independently fetched this session): https://forums.raspberrypi.com/viewtopic.php?t=383006
- RP2350 datasheet (fetch attempted, failed — timeout/ECONNRESET on all of the following mirrors; electrical-characteristics table content is therefore UNVERIFIED this session):
  - https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf
  - https://pip.raspberrypi.com/documents/RP-008373-DS-rp2350-datasheet.pdf
  - https://pip-assets.raspberrypi.com/categories/1214-rp2350/documents/RP-008373-DS-2-rp2350-datasheet.pdf
  - https://cdn.sparkfun.com/assets/0/7/7/c/4/rp2350-datasheet.pdf
- ADG1208/ADG1209 datasheet (Rev. E) — fetch attempted, failed on all of the following (C_IN therefore UNVERIFIED this session):
  - https://www.analog.com/media/en/technical-documentation/data-sheets/adg1208_1209.pdf
  - https://datasheet.octopart.com/ADG1208YRUZ-Analog-Devices-datasheet-68320185.pdf
  - https://www.alldatasheet.com/datasheet-pdf/pdf/166208/AD/ADG1209.html
  - https://datasheet.datasheetarchive.com/originals/distributors/Datasheets-4/DSA-75735.pdf
  - https://www.digchip.com/datasheets/1084724-adg1209.html
  - https://www.datasheetq.com/ADG1209-doc-ADI
- ADG5236 datasheet (Rev. B) — fetch attempted, failed on all of the following (C_IN therefore UNVERIFIED this session; VINL/VINH ≈0.8 V/2.0 V and off-leakage ~0.1–0.4 nA appeared in a WebSearch tool summary of this page but were NOT independently confirmed by direct fetch, so are not relied on here beyond cross-checking HARDWARE_DATA's own stated V_INH≈2 V):
  - https://www.analog.com/media/en/technical-documentation/data-sheets/adg5236.pdf
  - https://radiolocman.com/datasheet/data.html?%2FADG5236=&di=650593
  - https://studylib.net/doc/11964197/high-voltage-latch-up-proof--dual-spdt-switches-adg5236-d...
- TI SN74LVC2G34 (candidate buffer, not needed now, cited only as the rev-B fallback part): https://www.ti.com/product/SN74LVC2G34
