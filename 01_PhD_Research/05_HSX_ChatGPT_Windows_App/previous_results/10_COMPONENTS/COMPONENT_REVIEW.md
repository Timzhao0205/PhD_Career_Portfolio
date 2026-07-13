# COMPONENT_REVIEW — ST1 / Q1, board `hsx_2026_v2`

**Date:** 2026-07-10 · **Lens (locked, HARDWARE_DATA §4):** readout OUTSIDE vessel at ~ambient ·
≤20 kHz demodulated BW · 8-phase spinning @ 40 kHz nominal · 100 µA bias · low noise ·
hand-assembled · low cost · nothing may block the Aug-2026 single-axis install.
**Anomaly rule honored:** no conclusion below uses the 2026-07-08 measured amplitudes (open ~100×
anomaly, ΔV gain check pending). Everything is datasheet + first principles.

## Bottom line up front

**Keep the entire signal chain as-built. Zero "change" calls.** The incumbent parts are the
correct choices *under this lens*, and quantitatively so:

- **ADG1209** is the right mux *because of* its 120 Ω R_on: the figure of merit here is charge
  injection (0.4 pC typ), not R_on. A "better" low-R_on mux (e.g. ADG1409, 4 Ω class) buys ~100 Ω
  you don't care about (bias side is a current source; sense side feeds GΩ inputs) and pays with
  ~50–100× the injected charge at every phase step — exactly the glitch the spin/demod must digest
  8× per cycle.
- **AD8429 beats AD8421 at this source impedance.** Full noise sum below: 3.9 vs 4.8 nV/√Hz RTI
  total (≈0.77 vs 0.96 µT/√Hz at 100 µA). The i_n penalty of the AD8429 (1.5 pA/√Hz) costs only
  ~0.8 nV/√Hz against ~370 Ω per input; its 2 nV/√Hz e_n advantage dominates. Crossover is at
  ≈3 kΩ differential source — the plate is ~0.9 kΩ. Keep AD8429.
- **ADA4898-2: leave unplaced.** No function it could serve here survives the ≤20 kHz constraint
  (analysis below).
- **RS6-2415D: keep.** Spurs sit in the 100s of kHz [HARDWARE_DATA §2], 5–25× above the 40 kHz
  spin tone and its demod band (~1–2 kHz effective); the synchronous demod is a narrowband
  lock-in and rejects them. No linear post-regulator needed. One cheap rev-B insurance item noted.
- **Passives: keep all values.** The 2.2 kΩ bias returns are within 0.6 dB of the SNR-optimal
  choice — quantified below.

## Decision table

| Ref | Part | Role | Key spec that matters HERE | Verdict | Alt (if change) | Quantitative reason | Failure mode if wrong |
|---|---|---|---|---|---|---|---|
| U1 | ADG1209YRUZ | bias-steering 4:1 diff mux | Q_inj 0.4 pC typ; I_cont abs-max 30 mA vs 100 µA; V_INH 2.0 V | **KEEP** | — | R_on (120 Ω typ) is in series with a *current source* → zero bias error; Q_inj is the only glitch source at 8×/cycle, and 0.4 pC is near best-in-class for ±15 V muxes | High-Q_inj mux ⇒ pC-scale glitches at every phase step demodulate into a residual offset floor, defeating the spinning |
| U2 | ADG1209YRUZ | sense-steering 4:1 diff mux | Q_inj 0.4 pC; R_on 120 Ω into GΩ in-amp input; leakage ±0.1 nA max 25 °C | **KEEP** | — | 120 Ω R_on into 1.5 GΩ input ⇒ ~10⁻⁷ gain error; its Johnson noise is already inside the given 0.9 kΩ source figure; 0.4 pC/plate-node-C settles in ≪1 µs of the 12.5 µs phase | Same as U1; also leaky mux would unbalance the bridge at nA level (here ≤0.1 nA vs 100 µA ⇒ 10⁻⁶) |
| U3 | ADG5236BRUZ | bias-polarity chopper | Latch-up immune (trench); Q_inj −0.6 pC; I_cont 19 mA (TSSOP, ±15 V, 25 °C) vs 100 µA; V_INH 2.0 V | **KEEP** | — | In series with the floating current source ⇒ 160 Ω R_on and R_flat irrelevant; trench-isolated 5000-series can't latch under bench/plasma-EMI transients; 190× current headroom | Latch-up during a shot shorts a rail into the bias loop → sensor die overcurrent (irreversible, in-vessel) |
| U4 | AD8429ARZ | in-amp, G = 100.3 | e_ni 1.0 nV/√Hz; i_n 1.5 pA/√Hz; total RTI 3.9 nV/√Hz vs 4.8 for AD8421 at this R_s; BW(G=100) 1.2 MHz ≫ needed | **KEEP** (A grade suffices) | — (AD8421 explicitly rejected, sum below) | Noise sum: √(3.5² + 1.10² + 0.79² + 0.99²) = **3.9 nV/√Hz** vs AD8421 √(3.5² + 3.06² + 0.11² + 1.27²) = **4.8 nV/√Hz** → AD8429 ~20 % (1.9 dB) quieter; V_os/drift/1/f all killed by chopping, so B grade buys nothing | Swapping to AD8421 ⇒ noise floor up ~24 %, averaging time up ~1.5× for same field resolution |
| U5 | RS6-2415D | ±15 V isolated rails from 24 V | f_sw spurs in 100s of kHz (≥5× above spin); 18–36 V input; ~1.6–2 kVDC isolation; ±200 mA vs ~8 mA load | **KEEP** | — | Spurs are far out of the ~1–2 kHz demod band and not synchronous with the 40 kHz spin → lock-in rejects; per-board isolated supply is exactly what the 3× floating-channel replication wants; 25× current headroom | If a spur harmonic drifted onto a spin harmonic it would intermodulate into the demod band → false B ripple (see rev-B insurance) |
| R1 | 60.4 Ω 0603 | R_G (G = 1+6 kΩ/R_G = 100.3) | Adds √(4kT·60.4) = 0.99 nV/√Hz RTI (3 % of total) | **KEEP** (0.1 % thin film) | — | Right gain for 6 mV/T input scale on ±15 V rails; its noise contribution is already near-negligible | Wrong/drifty R_G ⇒ gain error directly in calibration; 5 % part = 5 % field error |
| R2, R3 | 2.2 kΩ 0805 | in-amp bias returns → GND1 | Loading 4.4/(4.4+0.9) = 0.830; sets i_n·R and thermal terms | **KEEP** (10 kΩ = optional rev-B, +7 % SNR) | — | SNR figure e_tot/α: 2.2 kΩ → 4.66, 10 kΩ → 4.32, 47 kΩ → 4.24 (nV/√Hz per unit signal): only 0.6–0.8 dB on the table; small R also minimizes CM imbalance and I_B·R offsets (spun away anyway) and EMI pickup | Omitting/oversizing them ⇒ in-amp bias current has no return → inputs drift to rail, output nonsense |
| R4 | 10 kΩ 0805 | output load at J4 | AD8429 specified at R_L = 2 kΩ; 10 kΩ ∥ 1 MΩ scope is lighter still | **KEEP** | — | Defines output DC path when scope disconnected; no drive issue at ≤20 kHz (slew 22 V/µs) | Missing load ⇒ floating SMA reads garbage when unplugged mid-test |
| R5–R8 | 0805 pulldowns | a0/a1/a2/EN defaults | Board dead until EN ≥ V_INH 2.0 V; 3.3 V Pico gives 1.3 V margin | **KEEP** | — | Guarantees safe (disabled) state with harness unplugged; values UNVERIFIED (not in HARDWARE_DATA) — any 10–100 kΩ works against Pico push-pull | No pulldown ⇒ floating EN can enable random mux states at power-up → wrong plates driven |
| R9, R10 | 100 Ω 0805 | bias-loop sense | Burden 2×10 mV at 100 µA — negligible vs floating-source compliance | **KEEP** (1 kΩ = optional rev-B for 100 mV readability) | — | Monitor-only; 10 mV is measurable with any bench DMM; zero noise impact (outside the sense path) | Oversized sense R with a compliance-limited source ⇒ eats headroom; undersized ⇒ can't verify bias |
| (lib) | ADA4898-2YRDZ | **unplaced** dual op-amp | 65 MHz, 0.9 nV/√Hz, 8 mA/amp | **LEAVE UNPLACED** | — | No function survives the lens: SNR is fixed at the in-amp input; AD8429 drives J4 directly; ≤20 kHz needs no post-amp/buffer; placing it costs 16 mA on ±15 V (0.48 W) + $ for zero SNR gain. Even the rev-B ADC-driver role is better served by a slower precision dual (e.g. OPA2210 class) | Placing it "because it's low noise" ⇒ heat + cost + an extra stage that can only add error, never remove input noise |

## Per-part detail

### U1/U2 — ADG1209YRUZ (keep) — the R_on-vs-Q_inj trap, resolved
Verified at ±15 V dual supply [ADG1208/1209 Rev E]: R_on 120 Ω typ / 200 Ω max (25 °C); ΔR_on
3.5 Ω typ; R_flat 20 Ω typ; leakage ±0.003 nA typ / ±0.1 nA max off, ±0.02 nA typ on (25 °C);
**Q_inj 0.4 pC typ**; t_transition 80 ns typ / 130 ns max; V_INH 2.0 V min / V_INL 0.8 V max;
digital C_IN 2 pF typ; C_S/C_D(on) 5 pF typ (ADG1209); off-isolation/crosstalk −85 dB. Abs max:
**continuous S/D current 30 mA**, 100 mA peak (1 ms, 10 %) — 300× above the 100 µA bias.
Supply ±5 to ±16.5 V. Active, in stock, $8.87 [Digi-Key].

Why R_on is a non-issue *here*: the bias path (U1) carries a stiff 100 µA current — series
resistance drops voltage but cannot change the current (compliance loss: 100 µA × ~240 Ω =
24 mV, nothing against ±15 V rails). The sense path (U2) feeds the AD8429's 1.5 GΩ input —
divider error ~120/1.5 G ≈ 10⁻⁷. Its Johnson noise is already inside the 0.9 kΩ "plate+R_on"
source figure given in HARDWARE_DATA §2.

Why Q_inj IS the issue: every phase step (8 per demod cycle, every 25 µs at 40 kHz) both muxes
switch, dumping ±Q_inj onto the plate nodes. 0.4 pC on a ~100 pF harness node = 4 mV spike with
τ ≈ 0.9 kΩ·100 pF ≈ 90 ns — fully settled within <1 % of the 12.5 µs half-phase, so the demod
plateaus are clean. A low-R_on mux (ADG1409 class, ~4 Ω) achieves that R_on with ~50–100× larger
gate charge; those glitches would still be settling when the demod samples. **ADG1209 (the
low-C_on/low-Q_inj member of the family) is the correct pick; keep both.**
Transition-time check: 130 ns max ≪ 12.5 µs half-phase (1 %) — timing budget fine up to the
100 kHz end of the stated 10 k–100 k usable phase-rate range.

### U3 — ADG5236BRUZ (keep) — the 5000-series robustness is earning its seat
Verified [ADG5236 Rev B]: **"latch-up immune under all circumstances"** via dielectric trench
isolation (features page); R_on 160 Ω typ ±15 V (Digi-Key headline concurs: "160 Ω"); at ±20 V
table: R_on 140 Ω typ/230 Ω max, ΔR_on 1.3 Ω, Q_inj −0.6 pC typ (V_S = 0 V, R_S = 0 Ω, C_L =
1 nF), transition 150 ns typ/290 ns max, leakage ≤0.4 nA (source off, 25 °C), V_INH 2.0 V min,
C_IN 3 pF typ. Abs-max **continuous current 19 mA/channel (TSSOP, ±15 V, 25 °C)** — 190× above
100 µA. Supply ±9 to ±22 V dual (board's ±15 V is inside; note it will NOT run on ±5 V — fine,
not asked). Active, in stock, $7.40 [Digi-Key]. A JESD78-class mA figure was not visible in the
pages fetched — the trench-isolation "immune under all circumstances" claim is the datasheet's
own wording; specific mA rating UNVERIFIED.

Chopper sits wholly in the floating-current bias loop → R_on/R_flat drop out entirely; only
Q_inj (−0.6 pC, settles as above) and robustness matter. The latch-up-proof process is the
right conservatism for a box living next to a stellarator's pulsed coils. **Keep.**

### U4 — AD8429ARZ vs AD8421ARZ — the noise sum, not an assertion
Verified [AD8429 Rev A]: e_ni **1.0 nV/√Hz** @1 kHz (RTI, high G), e_no 45 nV/√Hz, i_n
**1.5 pA/√Hz** @1 kHz (100 pA p-p 0.1–10 Hz); CMRR(G=100) 120 dB DC–60 Hz (A grade), 90 dB at
5 kHz; V_OSI ≤150 µV (A), drift ≤0.3 µV/°C; gain G = 1 + 6 kΩ/R_G → 100.33 at 60.4 Ω; gain
error ≤0.3 % (A, G>1); **BW 1.2 MHz at G = 100** (features); slew 22 V/µs; supply ±4–±18 V,
I_q ≈ 6.7 mA; specified −40…+125 °C. I_B ≤300 nA max (A grade); typ value OCR-ambiguous in the
mirror (70 nA vs µA row) — **I_B typ UNVERIFIED**, does not affect the verdict (I_B·2.2 kΩ ≤
0.7 mV static offset, removed by spinning). Active, in stock, $11.00 [Digi-Key].

Verified [AD8421 Rev A]: e_ni 3 nV/√Hz @1 kHz, e_no 60 nV/√Hz, i_n **200 fA/√Hz**; CMRR(G=100)
126 dB DC (A), 100 dB at 20 kHz; V_OSI ≤60 µV (A); I_B ≤8 nA over temp; gain G = 1 + 9.9 kΩ/R_G
(→ R_G ≈ 99.7 Ω for 100.3).

Noise sum, RTI, per √Hz, at 295 K. Source: 0.9 kΩ differential (plate + mux R_on, HARDWARE_DATA
§2) loaded by 2×2.2 kΩ returns → thermal R_eff = 0.9 k ∥ 4.4 k = 747 Ω → **3.5 nV/√Hz**;
per-input impedance for i_n ≈ 0.45 k ∥ 2.2 k = 374 Ω; i_n term = i_n·374 Ω·√2.

| Term | AD8429 | AD8421 |
|---|---|---|
| Source+returns thermal (747 Ω) | 3.49 | 3.49 |
| Amp e_n RTI = √(e_ni² + (e_no/G)²) | √(1.0²+0.45²) = 1.10 | √(3.0²+0.60²) = 3.06 |
| i_n · 374 Ω · √2 | 1.5 pA → 0.79 | 0.2 pA → 0.11 |
| R_G thermal | 60.4 Ω → 0.99 | 99.7 Ω → 1.27 |
| **Total RTI** | **3.87 nV/√Hz** | **4.81 nV/√Hz** |

Field-referred (S_I·I·α = 60 V/A/T × 100 µA × 0.83 ≈ 5 mV/T at the input): **0.77 vs
0.96 µT/√Hz**. AD8429 wins by 24 % in noise (≈1.5× in averaging time). Crossover where AD8421's
low i_n would win: √2·Δi_n·R_perinput ≥ √(3.06²−1.10²) ≈ 2.85 nV → R_perinput ≈ 1.6 kΩ ≈ 3 kΩ
differential — 3× above this plate. The AD8421's better documented AC CMRR (100 dB @20 kHz vs
AD8429's 90 dB @5 kHz spec point) is not decision-flipping: spinning itself converts residual
CM-induced offset into a rejected static term. Chopping also removes V_os/drift/1/f, so the
**A grade is the right money** — B grade's 50 µV/0.1 µV/°C buys nothing post-spin. **Keep
AD8429ARZ (A grade).** ENGINEERING JUDGMENT on grade; all numbers datasheet-verified.
*Anomaly note:* if the pending ΔV check reveals in-operation gain ≠ 100×, the fix will be in
wiring/config, not in this device choice — the noise ranking above is amplitude-independent.

### U5 — RS6-2415D (keep) — spurs vs the lock-in
Verified from vendor pages (RECOM PDF fetched but text-locked — see UNVERIFIED): input
**18–36 V** (24 V nominal), outputs **±15 V / ±200 mA (6 W)**, efficiency 87 %, isolation
listed **2 kVDC** [TME, rutronik] but **1.6 kV** on Digi-Key — discrepancy flagged, exact
figure UNVERIFIED (likely rated-vs-test distinction); −40…+75 °C; SIP-8; Active, in stock,
$20.37 [Digi-Key]. **Switching frequency and ripple mV p-p: UNVERIFIED** (datasheet PDF would
not parse; distributor pages omit them). Design fact from HARDWARE_DATA §2 (authoritative):
spurs land in the **100s of kHz**.

Judgment (ENGINEERING JUDGMENT, from verified architecture): the measurement is a synchronous
detection at 40 kHz with ~1–2 kHz effective demod bandwidth. A free-running spur at 300–500 kHz
is (a) ≥15× above the demod band, (b) asynchronous to the spin clock, and (c) attenuated by the
AD8429's PSRR and the existing C1–C10 rail filtering before it ever reaches the signal. It only
becomes visible if an intermod product of f_sw and a spin harmonic drifts through the ~kHz demod
window — a transient, identifiable artifact, not a floor. **No linear post-regulator, no LC
redesign needed now.** Cheap rev-B insurance: one ferrite-bead + 10 µF π-section per rail
(pennies, no layout risk), and/or logging f_sw during a field-sweep to confirm no folding.
Load check: per board ≈ 8 mA (AD8429 6.7 mA + muxes ≤0.4 mA + chopper ≤0.1 mA) of 200 mA — 25×
headroom; also confirms one RS6 per board trivially supports the ×3 replication with per-channel
galvanic isolation, which is exactly what the floating-bias architecture wants.

### Passives
- **R1 = 60.4 Ω (R_G):** G = 1 + 6 kΩ/60.4 Ω = 100.33 [AD8429 Rev A gain eq.]. Thermal noise
  0.99 nV/√Hz RTI = 3 % of total. Keep; ensure 0.1 %/25 ppm thin film at replication buy.
- **R2/R3 = 2.2 kΩ:** loading α = 4.4/(4.4+0.9) = 0.830 (matches HARDWARE_DATA §2). SNR merit
  (total RTI noise ÷ α, lower = better): 2.2 kΩ → 4.66, 10 kΩ → 4.32, 47 kΩ → 4.24. The as-built
  value is 0.6–0.8 dB off optimum — real but small; higher values worsen CM balance sensitivity
  and EMI pickup on the unshielded input node. **Keep now; 10 kΩ is a legitimate +7 % SNR rev-B
  tweak** (two resistors, re-check loading factor in calibration). ENGINEERING JUDGMENT.
- **R4 = 10 kΩ:** output defined when unplugged; ≥2 kΩ spec load respected. Keep.
- **R5–R8 pulldowns:** function verified against V_INH = 2.0 V min / V_INL = 0.8 V max
  (both switch families) and 3.3 V Pico drive — 1.3 V high margin. Values not stated in
  HARDWARE_DATA (assumption: 10–100 kΩ, any of which works). Keep.
- **R9/R10 = 100 Ω:** 10 mV monitor drop each at 100 µA; negligible burden. Keep. (Rev-B
  option: 1 kΩ → 100 mV for easier DMM checks; still negligible.) ENGINEERING JUDGMENT.
- **C1–C10:** not in ST1 scope beyond noting they exist; connectivity belongs to ST2.

### ADA4898-2YRDZ — leave unplaced (the place-or-leave call)
Verified [ADA4898-1/-2 Rev E, features]: 0.9 nV/√Hz, i_n 2.4 pA/√Hz, 65 MHz (G=+1), 55 V/µs,
±5–±16 V, **8 mA supply current per amplifier**. Candidate roles, each rejected under the lens:
1. *Input pre-amp ahead of the in-amp:* would need to precede the mux/chopper to help, breaking
   the spinning topology; noise floor is already thermal-dominated (3.5 of 3.9 nV/√Hz) — ceiling
   gain <0.5 dB. Reject.
2. *Output buffer/line driver to the scope:* AD8429 is specified driving 2 kΩ; J4 sees 10 kΩ ∥
   1 MΩ at ≤20 kHz. Nothing to buffer. Reject.
3. *Active anti-alias/post filter:* the demod is done in software from the scope capture; a
   passive RC at J4 (if ever needed against DC/DC spur folding) does the same job with two
   parts and zero added noise/power. Reject.
4. *Rev-B ADC driver (if DAQ moves off the scope):* a real role, but a 65 MHz/16 mA dual is the
   wrong tool at 20 kHz — a precision low-power dual (OPA2210-class) would be chosen fresh then.
**Verdict: leave out of v2 and out of the ×3 replication; remove from the rev-B BOM too.**
Placing it costs 0.48 W on the ±15 V rails and BOM $ for zero SNR gain. ENGINEERING JUDGMENT
built on verified numbers.

## Pico fan-out load numbers (handed to ST4)

- Per shared logic line per board: 2 × ADG1209 C_IN (2 pF typ) + 1 × ADG5236 C_IN (3 pF typ,
  worst case if that line also drives the chopper) ≤ **7 pF/board** → **≤21 pF for 3 boards**.
- Cable adds ~50–100 pF/m (generic ribbon/twisted pair, ENGINEERING JUDGMENT). 1 m run:
  C_total ≈ 21 + 100 ≈ **121 pF**.
- RP2350 GPIO drive: programmable **2/4/8/12 mA** [RP2350 datasheet; corroborating product
  brief — primary-PDF page fetch not completed, tier: verified-secondary]. Edge time at 8 mA:
  t ≈ C·ΔV/I = 121 pF × 3.3 V / 8 mA ≈ **50 ns** = 0.4 % of the 12.5 µs half-phase at 40 kHz.
- DC load: CMOS inputs, ±0.1 µA max each → ≤1 µA per line. Zero power delta.
- **Buffer threshold:** allowing edges up to 1 % of a half-phase (125 ns) at 12 mA drive →
  C_max ≈ 12 mA × 125 ns / 3.3 V ≈ **450 pF** ⇒ ≈ **4–5 m of cable** (at 100 pF/m) before a
  74LVC-class buffer is warranted. Below that: keep direct Pico drive, add 33–100 Ω series
  resistors at the Pico end for edge damping, and bond Pico GND to each board GND1 (J3 has no
  ground pin — HARDWARE_DATA §3).

## Needed now (3-axis build) vs nice-to-have (rev-B)

**Needed now (none of these block Aug-2026; the single-axis board is untouched):**
1. Buy 3× of the existing BOM as-is — every part confirmed Active/in-stock at Digi-Key
   (ADG1209YRUZ $8.87, ADG5236BRUZ $7.40, AD8429ARZ $11.00, RS6-2415D $20.37).
2. R_G at 0.1 %/25 ppm grade for channel-to-channel gain matching (same value, better tolerance
   — a purchasing note, not a design change).
3. Series 33–100 Ω on the four shared logic lines at the Pico end (fan-out hygiene; on the Pico
   carrier, not the readout board).
4. Keep one RS6-2415D per board (channel isolation) — do not share rails across channels.

**Nice-to-have (rev-B only):**
1. R2/R3 2.2 kΩ → 10 kΩ: +7 % SNR (0.6 dB), re-verify loading factor in calibration.
2. Ferrite + 10 µF π-filter per ±15 V rail (DC/DC spur insurance).
3. R9/R10 100 Ω → 1 kΩ (100 mV monitor readability).
4. Passive RC at J4 (~200 kHz pole) only if field data ever shows DC/DC spur folding.
5. Drop ADA4898-2 from the project library to prevent accidental placement.

**Explicitly NOT recommended:** AD8421 swap (noise sum above), low-R_on mux swap (Q_inj trap),
linear post-regulators (demod already rejects spurs), B-grade AD8429 (chopping makes its V_os
advantage worthless here).

## Assumptions made
1. R5–R8 pulldown values are 10–100 kΩ (not stated in HARDWARE_DATA); any value in that decade
   satisfies both the V_INL ≤ 0.8 V requirement and Pico drive.
2. Plate source treated as symmetric (≈450 Ω per input) for the i_n calculation.
3. Cable capacitance 50–100 pF/m for the Pico logic harness (generic unshielded pair/ribbon).
4. T = 295 K for Johnson noise (√(4kTR), 1 kΩ → 4.03 nV/√Hz).
5. ADG5236 chopper is driven from one of the J3 logic lines (worst-case fan-out assumption);
   if it is derived on-board, per-board load drops to 4 pF.
6. The ADG1209 Q_inj = 0.4 pC row was read from the dual-supply (±15 V) table of the Rev E
   datasheet mirror; test condition assumed to be the family-standard V_S = 0 V, R_S = 0 Ω,
   C_L = 1 nF (explicit on the single-supply table of the same sheet).

## UNVERIFIED (what was needed and could not be fetched)
- **RS6-2415D switching frequency and ripple (mV p-p):** RECOM RS6 datasheet PDF downloaded but
  text extraction failed; distributor pages omit both. Judged instead from the authoritative
  design fact "spurs in the 100s of kHz" [HARDWARE_DATA §2]. Needed: RS6 datasheet spec table.
- **RS6-2415D isolation:** 2 kVDC [TME/rutronik] vs 1.6 kV [Digi-Key] — either exceeds the need;
  exact figure unresolved.
- **AD8429 I_B typical:** mirror OCR ambiguity (70 nA vs a µA-row artifact); max ≤300 nA (A)
  read from the spec table. Not decision-relevant (offset is spun away).
- **ADG5236 JESD78 latch-up class/mA:** datasheet's qualitative "latch-up immune under all
  circumstances" (trench isolation) verified; a numeric mA rating was not visible.
- **RP2350 drive-strength (2/4/8/12 mA):** taken from Raspberry Pi documentation ecosystem
  (product brief/datasheet references); primary datasheet page not directly parsed.
- Note: analog.com and recom-power.com direct PDF fetches timed out repeatedly from this
  environment; ADI specs were verified from full-text datasheet mirrors (radiolocman/rlocman,
  hosting the actual Rev E/B/A ADI PDFs) — revision letters as cited.

## Sources
- ADG1208/ADG1209 datasheet Rev E (ADI) — mirror pages used: https://www.rlocman.cn/datasheet/pdf.html?di=176133&p=2 (±15 V table), …&p=4 (single-supply table, dual-supply power/caps), …&p=6 (abs max); canonical: https://www.analog.com/media/en/technical-documentation/data-sheets/adg1208_1209.pdf
- ADG5236 datasheet Rev B (ADI) — mirror: https://radiolocman.com/datasheet/data.html?%2FADG5236=&di=650593 (features/summary), https://www.rlocman.cn/datasheet/pdf.html?di=176063&p=3 (±20 V table), …&p=6 (abs max/continuous current); canonical: https://www.analog.com/media/en/technical-documentation/data-sheets/adg5236.pdf
- AD8429 datasheet Rev A (ADI) — mirror: https://www.radiolocman.com/datasheet/pdf.html?di=126283&p=3 (noise/CMRR/offset), …&p=4 (gain eq., slew), https://www.radiolocman.com/datasheet/pdf.html?di=169989 (Rev A copy; settling/THD; 1.2 MHz @G=100 features); canonical: https://www.analog.com/media/en/technical-documentation/data-sheets/AD8429.pdf
- AD8421 datasheet (ADI) — mirror: https://www.radiolocman.com/datasheet/pdf.html?di=126275&p=3 (noise/CMRR/offset/I_B); canonical: https://www.analog.com/media/en/technical-documentation/data-sheets/ad8421.pdf
- ADA4898-1/ADA4898-2 datasheet Rev E (ADI) — mirror: https://www.radiolocman.com/datasheet/data.html?di=349231; canonical: https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4898-1_4898-2.pdf
- RECOM RS6 series datasheet (REV 10/2024): https://recom-power.com/pdf/Econoline/RS6.pdf (fetched, text-locked) / https://g.recomcdn.com/media/Datasheet/pdf/.fVDmoE6Y/.td251280bccaf6240ab3d/Datasheet-62/RS6.pdf
- RS6-2415D product pages: Digi-Key https://www.digikey.com/en/products/detail/recom-power/RS6-2415D/6206497 (Active, $20.37, 1.6 kV, 18–36 V, ±15 V/200 mA); TME https://www.tme.eu/en/details/rs6-2415d/dc-dc-converters/recom/ (2 kV); rutronik24 https://www.rutronik24.com/product/recom/rs62415d/11972948.html
- Digi-Key stock/status: ADG1209YRUZ https://www.digikey.com/en/products/result?keywords=ADG1209YRUZ · ADG5236BRUZ https://www.digikey.com/en/products/result?keywords=ADG5236BRUZ · AD8429ARZ https://www.digikey.com/en/products/result?keywords=AD8429ARZ
- RP2350 datasheet (Raspberry Pi): https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf; product brief: https://www.mouser.com/datasheet/2/635/Raspberry_Pi_05_22_2025_rp2350_product_brief-3600627.pdf
