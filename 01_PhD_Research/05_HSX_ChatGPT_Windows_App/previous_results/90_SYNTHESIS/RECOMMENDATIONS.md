# RECOMMENDATIONS — master answer table + 3-axis build order

Run of 2026-07-10. All eight subtasks complete; every deliverable passed a `red-team-critic`
review (two waves, `RED_TEAM.md`: **0 BLOCKER · 5 MAJOR · 14 MINOR · 8 NOTE**; all MAJORs are
pre-purchase/pre-bond verification gates, none overturns a recommendation).

**Global integrity notes**
- No conclusion in this run rests on the 2026-07-08 measured bench amplitudes (open ~109×
  anomaly, ΔV gain check pending). ST1's keep/change calls are datasheet + first-principles;
  if the anomaly resolves to "in-operation gain ≠ ~100×," the component verdicts stand — only
  the *expected output amplitudes* (≈0.5–0.6 V/T system sensitivity) need re-derivation.
- The locked constraints were honored everywhere: readout board outside the vessel at ~ambient,
  ≤20 kHz demodulated bandwidth, only die + LCC + zirconia head in-vessel. Red-team confirmed
  zero locked-constraint violations across all deliverables.
- Nothing recommended blocks the Aug-2026 single-axis HSX campaign.
- **POST-RUN UPDATE (2026-07-10):** Q5's flange pick changed from 9C2-275 to **19C-275** after a
  user-directed follow-up found a better-fitting connector family. See `FLANGE_SELECTION.md` §9
  and `DECISION_GATES.md` GATE 2. Q6 and Q8's mechanical specifics (pin grouping, A/B swap FMEA,
  height ledger) still reflect the superseded 9C2-275 geometry and have not been reconciled.

## Master answer table

| # | Question | Answer (bottom line) | Keep/Change | Confidence | Cost/effort | Deliverable |
|---|---|---|---|---|---|---|
| Q1 | Component selection optimal? | Yes — the whole chain is right under the ambient/≤20 kHz/spun lens. ADG1209 (charge injection is the FOM, 0.4 pC settles in ~90 ns ≪ 12.5 µs half-phase; low-R_on alternatives rejected), ADG5236 (trench latch-up immunity earns its seat next to pulsed coils), AD8429 **beats** AD8421 here (total RTI 3.87 vs 4.81 nV/√Hz at this source impedance), RS6-2415D fine (spurs ≥15× above demod band). **ADA4898-2: leave unplaced** — no role survives ≤20 kHz. Passives keep; 10 kΩ bias returns = +7 % SNR rev-B tweak only. | **KEEP (all)** | High (datasheet-verified; 9/9 red-team citation spot-checks passed) | $0 | `10_COMPONENTS/COMPONENT_REVIEW.md` + `bom_verdict.csv` |
| Q2 | Connections correct? | **PASS-with-flags.** All 36 nets / 40 components traced; J1 (Amphenol D09S33E6GX00LF) confirmed female DSUB-9 with p1=1/p3=2/p2=6/p4=7 preserved; the netlist independently reproduces the 8-phase spin logic (a1 toggles the bias/sense diagonal; a0 flips sense polarity). No v1→v2 regression found. Low flags: `+36V` net name is cosmetic; EN=0 opens the bias loop (use a compliance-limited source); J1 footprint pads need a first-article continuity check; RS6-2415D CTRL pin floating. | **KEEP** (fix flags at leisure) | High | $0 | `20_CONNECTIONS/CONNECTION_CHECK.md` |
| Q3 | Bigger board, 6 layers, or 3 stacked boards? | **Three replicated `hsx_2026_v2` boards, racked side-by-side on one baseplate with standoffs** (not a literal face-to-face tower). Wins 475/500 vs A=310 (large board) and B=275 (6-layer); still wins with schedule+reuse weights zeroed (275 vs 210/215 of 300) — isolation and blown-channel-rework advantages are intrinsic. Runner-up: A as the natural rev-B. Flip: if the anomaly or Campaign #1 forces a layout respin anyway, heritage is void → go A. | **KEEP plan (replicate ×3)** | High (judgment, weights stated) | ~$30/set PCBs + 2× parts sets (~$100s) | `30_3AXIS_ARCH/ARCHITECTURE_TRADE.md` → **GATE 1** |
| Q4 | Does the Pico connection change? | **No buffer, no drive change needed.** 3-board load ≈ 21 pF chip + cable; settle ~5–25 ns vs 12.5 µs half-phase (≥400× margin); DC pulldown load ~4 mA of a ≥50 mA budget. Buffer threshold: **≈400 pF per shared line ≈ 7 m cable at 50 pF/m** (red-team-reconciled number; ~3.5 m worst-case 100 pF/m) — bench runs are <1–2 m. **Change that IS needed: star ground** — Pico → each board's GND1 home-run, each logic line with its own return; optional 33–100 Ω series R at the Pico. | **KEEP fan-out / CHANGE grounding** | High | $0 | `40_PI_FANOUT/PI_FANOUT.md` |
| Q5 | Which flange for 12 conductors? | **REVISED 2026-07-10 — Accu-Glass 19C-275 (P/N 110210)** — 19-pin, single-shell MIL-C-26482 circular, on **2.75″ CF**, $434; meets/exceeds all 9D-275 ratings (500 VDC, 5 A/pin, −200…250 °C, 1×10⁻¹⁰ Torr). Found in a user follow-up after the original run (a third connector family ST5 didn't check); **strictly beats** the original pick (9C2-275, $685, 2× 9-pin Sub-C) on cost, spare-pin count (+7 vs +6), and mis-mate risk (one shell vs. two — removes the A/B swap FMEA the 9C2-275 needed). System ≈ $1,145 (110230 vacuum-side, 110232 air-side). 9C2-275 remains the fallback if the 19C-275 fails a new contact-AWG/protrusion check (§7 below); 15D-450/25D-450 (4.5″ CF) stay the runner-up if the port changes. **Open debt: `WIRING_PLAN.md` and `PACKAGING_3D_DESIGN.md` were built for the 9C2-275's dual-tower geometry and have not been reconciled to the single-shell 19C-275** — see `FLANGE_SELECTION.md` §9. | **CHANGE (9D-275 → 19C-275)** | Medium-high (two purchase gates open, plus unreconciled downstream ST6/ST8) | ≈ $1,145 | `50_FLANGE/FLANGE_SELECTION.md` → **GATE 2** |
| Q6 | Wiring & short-circuit safety? | Per-sensor grouping: connector A = X (pins 1–4) + Y (6–9), B = Z (1–4) + ID-loop (6–7) + grounded spares; identical (p1,p3,p2,p4) order both towers makes an **A/B swap harmless by construction and detectable pre-power** (ID loop + resistance fingerprint + magnet polarity check). Grounding: scope = single signal common; shields earthed only at a flange junction box. **Top risk is not the harness** (pin-to-pin shorts are 100 µA-limited = data-killers): it's **24 V mis-plugged into the J2 bias loop** (identical 1×02 headers, would push ~20 mA through a ~500 µA-class die) → **keyed housings NEEDED NOW**; and **IR-testing >10 V with sensors attached** → hard 10 V/500 µA ceiling + red tag. Full pre-power procedure in the deliverable. | **New plan (adopt)** | High | ~$10s (keyed housings, labels) | `60_WIRING_SHORTS/WIRING_PLAN.md` |
| Q7 | LCC02046 wire-bond strategy sound? | **ADJUST.** (a) "Four corners" is a misconception — LCC-20 has 5 pads/side and *no corner pads* (one corner is the index chamfer); bond the die's N/E/S/W pads radially to the **mid-side pads: p1→pad 1 → DSUB 1, p3→pad 16 → DSUB 2, p2→pad 11 → DSUB 6, p4→pad 6 → DSUB 7** (~2 mm bonds, 90° apart, zero crossings; DSUB convention unchanged). (b) "Route to one side via castellations" is impossible on the carrier (castellations only connect a shelf pad to its own outer pad) — the one-side/downward exit is the **mount's** job (delivered in Q8). (c) Bonus finding: Spectrum's lid (CL-30010) is Kovar/Ni — **ferromagnetic → run open-cavity, no lid**. Bond flat on the bench, then mount; never vertical-face bond. Al wedge on Au OK now with pull-test qual; Au wire is the rev-B upgrade. | **ADJUST** | High on geometry/map (chamfer-datum-relative); 2 bond-blocking verifications open | $0 | `70_PACKAGING/PACKAGING_REVIEW.md` → **GATE 3 preconditions** |
| Q8 | 3D probe-head options + critique? | **Concept B "SpringClamp Cube"** — 15 mm monolithic zirconia cube; per-face drop-in pocket; PEEK insert carrying 4 gold-plated BeCu (no-Ni) leaf springs contacting pads 1/6/11/16; Ti picture-frame clamp with geometry-defined preload; glue-free, ~2-min carrier swap; envelope: corner 11.87 ≤ 15.875 mm, stack 25.8 ≤ 27.5 mm. Score 4.84/5; runner-up **D "TriPlate"** (4.70, same contact interface, 3 flat plates on a core cube — flip if the monolithic cube quotes >2–3× the plates or misses tolerance). **Your slotted cube: replace, don't refine** — measured from your STEP: base plate at 15.87 mm = zero envelope margin, only 2 axes, wrong carrier stand-in, and sensors sealed in 0.5 mm-wall cavities with **no electrical path** (the compatibility-gate failure); your pocket-per-face/no-glue instinct survives inside B. COTS LCC-20 sockets rejected on citation (Ni plating = magnetic, 150 °C limit, oversize). 3 pre-RFQ fixes required (see Gate 3). | **New design (adopt B)** | Medium-high (3 MAJOR pre-RFQ fixes open) | ceramics + inserts RFQ (quote TBD) | `80_3D_PACKAGING/PACKAGING_3D_DESIGN.md` + 4 concept folders (19 renders, STL/STEP) → **GATE 3** |

## Needed-now vs rev-B (rollup)

**Needed now (3-axis build):** keyed J2/J5 power-vs-bias housings; star-ground fan-out wiring;
2× additional board builds (option C); 19C-275 system purchase (after Gate 2 clears; 9C2-275 is
the fallback); LCC
numbering + die-orientation verification, then bonding to pads 1/6/11/16 open-cavity; Concept B
pre-RFQ fixes → geometry freeze → ceramics/insert order; harness build + labels + ID loop;
pre-power test procedure executed and signed.

**Rev-B / nice-to-have (do NOT do before Aug-2026):** 10 kΩ bias returns (+7 % SNR); π-filters
on the ±15 V rails; Au bond wire (Au–Al intermetallic insurance); rename `+36V` net; tie or
document RS6-2415D CTRL; drop ADA4898-2 from the library BOM; option A single-board respin as
the eventual integrated rev.

## 3-axis build order of operations

1. **Now — close the ΔV gain anomaly** (bench, no purchase blocked by it). Until closed,
   measured amplitudes stay untrusted; component conclusions above are independent of it.
2. **Now — one UW-Madison email + one Accu-Glass call** (details in `DECISION_GATES.md`):
   port CF size at the probe location; **19C-275 contact AWG rating + single-shell protrusion
   height** (fallback: 9C2-275 Sub-C tower protrusion height) above the flange face; in-vessel
   temperature at the probe; bakeout plan; whether the Ø31.75 mm envelope derives from the port
   bore. These clear Gates 2 and 3 preconditions.
3. **Order long-lead cheap items:** 2× more `hsx_2026_v2` PCB sets + component sets (all
   confirmed active/orderable); keyed housings; labels/backshells per `WIRING_PLAN.md`.
4. **Bond-blocking verifications (RT-02):** confirm LCC02046 pad-numbering direction on the
   physical carrier vs drawing PB-CA8272-B, and pin die p1–p4 orientation to the GDS labels.
   Then **bond gen-2 dies flat** to pads 1/6/11/16, open-cavity, pull-test qual.
5. **Concept B pre-RFQ fixes (RT-16/17/18):** add mated-connector stack to the height ledger
   (standoff cap 8.2 mm until the tower call answers); compute the preload tolerance chain
   (mandate pocket-floor lap or lengthen finger); add a corner key against 90°/180° rotated
   seating. Then geometry freeze → RFQ zirconia cube + PEEK inserts + Ti frames.
6. **Purchase the 19C-275 system** once Gate 2's two conditions clear (9C2-275 if the 19C-275
   fails its contact/protrusion check). **Before treating Gate 2 as fully closed, reconcile
   `WIRING_PLAN.md` and `PACKAGING_3D_DESIGN.md` to whichever flange is actually ordered** — both
   were written for the 9C2-275's dual-shell geometry (`FLANGE_SELECTION.md` §9).
7. **Build the harness** per `WIRING_PLAN.md` (twisted pairs, shields to junction box only,
   ID loop, bake-compatible labels).
8. **Assemble the 3-board rack** (option C) with star grounding; Pico direct fan-out.
9. **Execute the pre-power procedure** (continuity map → IR at ≤10 V/500 µA with sensors
   attached → one axis at a time, current-limited).
10. **Aug-2026 single-axis campaign proceeds in parallel, untouched by all of the above.**

## Sources
Each claim above is cited in its parent deliverable (one Sources block per file, per
SOURCE_STANDARDS). This rollup introduces no new sources. Red-team citation audit: 14/14
load-bearing spot-checks passed (`90_SYNTHESIS/RED_TEAM.md`).
