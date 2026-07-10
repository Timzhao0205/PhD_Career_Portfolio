# ST6 — Multi-sensor wiring & short-circuit safety plan (Q6)

**Date:** 2026-07-10 · **Scope:** 3 sensors × 4 plate terminals = 12 signal conductors, probe
head → LCC02046 carriers → in-vessel harness → **Accu-Glass 9C2-275 (P/N 100012)** feedthrough
(ST5 primary pick) → air harness → 3× `hsx_2026_v2` boards (J1 DSUB-9 each).
**This answers the user's #1 worry: wiring and short circuits across 3 sensors.**
Red-team pass pending per MISSION_BRIEF.

---

## 0. BLUF

1. **Pin-map scheme:** each sensor lives **entirely on one feedthrough connector**, in the
   fixed order (p1, p3, p2, p4) on pins (1, 2, 3, 4) — Connector **A = X on 1–4, Y on 6–9,
   guard on 5**; Connector **B = Z on 1–4, guard on 5, ID-loop on 6–7, grounded spares on
   8–9**. Because A pins 1–4 and B pins 1–4 carry *identically-ordered* plate groups, a
   worst-case **A↔B swap can never drive a bias line into another axis's sense line at a
   different terminal role — it only relabels axes, and it is positively detected before
   power** by the resistance-map fingerprint (§8).
2. **The harness is intrinsically short-tolerant by architecture** — and this should
   recalibrate the fear: the 12 conductors carry *only* floating Hall-plate terminals driven
   by per-board **100 µA current-limited sources**; **no power rail crosses the feedthrough**.
   A pin-to-pin short anywhere in the harness corrupts data but cannot push more than 100 µA
   (= the normal operating current) into any die. The **actual die-killers** are elsewhere:
   (a) a **>10 V insulation tester used with sensors connected**, (b) the **J2/J5 identical
   2-pin headers** letting 24 V power be plugged into the bias loop (~20 mA through the die),
   (c) **plasma current collected by exposed conductor** in-vessel, and (d) **ESD in
   handling**. The FMEA (§9) and procedure (§10) are built around those four.
3. **Grounding:** single signal-ground common at the **scope chassis** (3× SMA shields +
   sync); Pico logic returns **star per ST4** (one return per board, twisted per line);
   harness shields/guards earthed **only at the junction box** on the vessel side; **no
   galvanic tie anywhere between harness shields and any GND1**. No shared signal return
   exists anywhere in the sensor path (fully differential, floating).
4. **Pre-power gate:** printable continuity + isolation procedure (§10) with expected values;
   insulation-resistance testing at **50 V only while sensors and boards are disconnected**,
   and a hard **≤10 V / ≤500 µA** limit for any measurement once carriers are installed
   (justified in §10.0 — the plate is qualified to 500 µA bias, not to megger voltages).

---

## 1. Verified hardware chain (all vendor facts re-fetched 2026-07-10)

```
IN VESSEL (UHV, hot)                         │ FLANGE │            AIR SIDE (~ambient)
                                             │        │
3× Hall die ──Al wedge bonds──> 3× LCC02046  │        │
   p1..p4        (ST7 map)      mid-side pads│        │
      │                                      │        │
   ST8 mount contacts (per-face exit)        │        │
      │  2× twisted pairs per axis           │        │
      ▼                                      │        │
2× Accu-Glass 100040 (9-way Kapton/PEEK, cut │9C2-275 │ 2× Accu-Glass 100020 (9-lead shielded
   to length, female PEEK, 250°C, UHV) ──────┤2× Sub-C├── PVC, foil+drain, Delrin female, 80°C)
   VC-A → tower A     VC-B → tower B         │ towers │  AC-A ← tower A    AC-B ← tower B
                                             │ A ─ B  │      │
                                             │0.750" c│      ▼
                                             │        │  Junction box JB (earthed to flange)
                                             │        │      │ 3× 2-pair shielded tails
                                             │        │      ▼
                                             │        │  DSX / DSY / DSZ (DSUB-9 male plugs)
                                             │        │      → boards BD-X / BD-Y / BD-Z (J1)
```

| Element | Part | Key wiring-relevant facts | Source |
|---|---|---|---|
| Feedthrough | 9C2-275, P/N 100012, $685 | 18 pins = two 9-pin Sub-C towers on **0.750″ centers**, 2.75″ CF; **straight-through pin-to-pin**; male/male; 500 VDC max, 5 A/pin @20 °C (max 20 % of pins at once); −200…250 °C; 1×10⁻¹⁰ Torr; **pin-position surface mark on every connector face** (mark position mirrors vacuum↔air side); **screw-boss = polarizing key** (a connector cannot be mated rotated); towers **not factory-marked A/B** (no marking mentioned anywhere) | Sub-C catalog PDF pp.8–9 [S1]; 9C2-275 page [S2] |
| Vacuum harness | 2× 100040 (CKAP-C9-19SC), $243 ea | 9-pin **female PEEK** connector w/ captured SS locking screws (vented); 19″ of **nine Kapton-insulated 28 AWG silver-plated Cu wires (7×0.005 stranded)** in a **PEEK braid jacket Ø0.14″**; far end non-terminated; 250 °C, UHV, 2 A; wire colors **not specified → assume indistinguishable, identify by continuity** | Catalog p.10 [S1]; 100040 page [S3] |
| Air harness | 2× 100020 (AIR-CP9-48SC), $154 ea | 9-pin **female Delrin** connector; 48″ gray PVC jacket Ø0.23″; **nine 24 AWG tinned-Cu wires (7×0.008)**; **shield = aluminum/Mylar foil + 24 AWG tinned-Cu drain wire**; far end non-terminated; **80 °C max**; 4 A; wire colors not specified | Catalog p.13 [S1]; 100020 page [S4] |
| Board connector | J1 = Amphenol D09S33E6GX00LF, DSUB-9 **socket** → harness needs DSUB-9 **male** plugs | p1=1, p3=2, p2=6, p4=7; pins 3/4/5/8/9 spare (assumed N/C on board — ST2 to confirm) | HARDWARE_DATA §1/§3 [S9] |
| High-mate-cycle option | Female Sub-C contacts 110908 (20–24 AWG) / 110909 (26–30 AWG) | Recommended by vendor where plug-in cycles exceed 3/day | Catalog p.12 [S1] |

Electrical headroom (one-line): worst-case harness current = 100 µA ≪ 2 A (weakest element,
100040) ≪ 5 A/pin (feedthrough); worst-case harness voltage = bias-source compliance
(≤ ~18 V, assumption A5) ≪ 500 VDC. Ratings are a non-issue; everything below is about
**where the wires go and how a fault is detected before it matters**.

---

## 2. End-to-end pinout table (THE artifact — print and keep with the harness)

Naming: `FT-A/B` = feedthrough towers (A = the tower scribed "A" per §7.1), `VC-x` = vacuum
cable 100040, `AC-x` = air cable 100020, `JB` = junction box terminal, `DSX/Y/Z` = DSUB-9
plugs, `BD-X/Y/Z` = boards. Feedthrough is straight-through, so **vacuum pin n = air pin n**
[S1 p.8 "straight through pin-to-pin"]. Wire numbers in VC/AC = the feedthrough pin they
land on (wires are not color-coded — identity is established by continuity at build, §10
Stage 0, then tagged).

**Nominal roles:** pair (p1,p3) = "bias pair", (p2,p4) = "sense pair" **at spin phase 0
only** — under 8-phase spinning the muxes rotate roles, so *every* conductor carries switched
bias current at some phase. Labels on hardware carry terminal names (p1…p4), never "bias"/"sense".

### 2.1 Signals (12)

| Axis | Plate | Nominal role (φ0) | LCC02046 pad | In-vessel pair/tag | FT conn·pin | Air wire | JB term | DSUB tail pair | Board · J1 pin |
|---|---|---|---|---|---|---|---|---|---|
| X | p1 | bias + | **1** (mid-pad, index side — per ST7 map, numbering pending drawing PB-CA8272-B) | VC-A pair **XP-B**, wire 1, tag `X1` | **A·1** | AC-A w1 | A1 | DSX pair 1, wht | **BD-X · 1** |
| X | p3 | bias − | **16** (per ST7) | VC-A pair **XP-B**, wire 2, tag `X3` | **A·2** | AC-A w2 | A2 | DSX pair 1, blk | **BD-X · 2** |
| X | p2 | sense + | **11** (per ST7) | VC-A pair **XP-S**, wire 3, tag `X2` | **A·3** | AC-A w3 | A3 | DSX pair 2, wht | **BD-X · 6** |
| X | p4 | sense − | **6** (per ST7) | VC-A pair **XP-S**, wire 4, tag `X4` | **A·4** | AC-A w4 | A4 | DSX pair 2, blk | **BD-X · 7** |
| Y | p1 | bias + | 1 (per ST7) | VC-A pair **YP-B**, wire 6, tag `Y1` | **A·6** | AC-A w6 | A6 | DSY pair 1, wht | **BD-Y · 1** |
| Y | p3 | bias − | 16 (per ST7) | VC-A pair **YP-B**, wire 7, tag `Y3` | **A·7** | AC-A w7 | A7 | DSY pair 1, blk | **BD-Y · 2** |
| Y | p2 | sense + | 11 (per ST7) | VC-A pair **YP-S**, wire 8, tag `Y2` | **A·8** | AC-A w8 | A8 | DSY pair 2, wht | **BD-Y · 6** |
| Y | p4 | sense − | 6 (per ST7) | VC-A pair **YP-S**, wire 9, tag `Y4` | **A·9** | AC-A w9 | A9 | DSY pair 2, blk | **BD-Y · 7** |
| Z | p1 | bias + | 1 (per ST7) | VC-B pair **ZP-B**, wire 1, tag `Z1` | **B·1** | AC-B w1 | B1 | DSZ pair 1, wht | **BD-Z · 1** |
| Z | p3 | bias − | 16 (per ST7) | VC-B pair **ZP-B**, wire 2, tag `Z3` | **B·2** | AC-B w2 | B2 | DSZ pair 1, blk | **BD-Z · 2** |
| Z | p2 | sense + | 11 (per ST7) | VC-B pair **ZP-S**, wire 3, tag `Z2` | **B·3** | AC-B w3 | B3 | DSZ pair 2, wht | **BD-Z · 6** |
| Z | p4 | sense − | 6 (per ST7) | VC-B pair **ZP-S**, wire 4, tag `Z4` | **B·4** | AC-B w4 | B4 | DSZ pair 2, blk | **BD-Z · 7** |

LCC pad column: the ST7 mapping (p1→pad 1, p3→pad 16, p2→pad 11, p4→pad 6 = the **middle pad
of each carrier side**, chamfer as datum) is identical on all three carriers
[70_PACKAGING/PACKAGING_REVIEW.md §4]. ST7's numbering assumes JEDEC-style CCW numbering —
**confirm against Spectrum drawing PB-CA8272-B before bonding**; the physical instruction
(mid-side pads) and everything downstream of the ST8 mount contacts is unaffected either way.
The mount-contact → VC-x wire termination method (mechanical clamp / crimp / spot-weld — **no
solder, no flux in-vessel**) is an ST8 interface item; this table fixes only *which wire meets
which pad*.

### 2.2 Spares (6) — all six get a defined use; nothing floats

| FT conn·pin | Name | In-vessel end | Air end | Use / justification |
|---|---|---|---|---|
| **A·5** | GUARD-A | insulated, capped (folded back + fiberglass sleeve), laced into VC-A bundle | JB earth bus | Grounded guard conductor physically riding between the X and Y groups' wires the full length of the shared harness; also the per-harness IR-test reference. A floating spare would be an antenna; earthing it (one end only) is free shielding. ENGINEERING JUDGMENT |
| **B·5** | GUARD-B | insulated, capped, laced into VC-B bundle | JB earth bus | Same, for the Z harness |
| **B·6** | ID-a | **crimp-spliced to B·7** ~30 mm from the VC-B connector exit (UHV-clean uninsulated crimp, sleeved) | JB terminal (measure point) | **Connector-identity loop:** B6–B7 reads <2 Ω only when the true B tower/cable chain is in the B position → positively distinguishes an A↔B swap from a broken wire (§8). ENGINEERING JUDGMENT |
| **B·7** | ID-b | (spliced to B·6) | JB terminal (measure point) | — |
| **B·8** | SPARE-1 | insulated, capped, laced | JB earth bus via **removable** jumper | Grounded guard by default; documented replacement conductor if a Z wire fails (re-terminate at JB + at the mount — vacuum end repair still needs a vessel entry, so this mainly protects against air-side/contact faults) |
| **B·9** | SPARE-2 | insulated, capped, laced | JB earth bus via removable jumper | Same |

**Failure mode if the spare plan is wrong:** floating spares capacitively couple spin edges
between axes and confuse IR tests with phantom readings; an *in-vessel-grounded* guard (the
alternative rejected here) would form a shield loop through the vessel wall and the JB earth.

---

## 3. Twisted-pair plan

| Segment | What twists with what | Pitch / practice |
|---|---|---|
| In-vessel (VC-A/B free ends, connector → probe head) | Per axis: (p1,p3) twisted as one pair, (p2,p4) as the second pair. VC-A carries 4 pairs + guard; VC-B carries 2 pairs + guard + ID stub | Hand-twist ~1 turn per 25 mm, consistent direction; keep the factory **PEEK braid jacket intact to within ~20 mm of the connector**, twist only the freed length; secure with bare SS lacing wire (no polymer ties, no adhesives). Kapton wire tolerates gentle twisting; do not nick insulation — every nick is an F3/F5 initiator (§9) |
| Feedthrough | (untwistable — pins) | Pair members on **numerically adjacent pins** (1-2, 3-4, 6-7, 8-9) so the loop area through the feedthrough stays minimal. Geometric pin adjacency of the Sub-C insert is UNVERIFIED (no pin-layout drawing extracted) — the FMEA therefore assumes any-pin-to-any-pin shorts are possible within a tower (§9 F1/F2) |
| Air, feedthrough → JB (100020) | None — the 100020 is a straight 9-wire bundle under one overall foil shield (construction verified [S1 p.13]) | Accept for 48″: overall foil + drain, 100 µA signals, ≤20 kHz demod band. **Residual risk:** X-bias spin edges coupling to Y-sense within the shared AC-A bundle — bounded, and measured explicitly at the October 3-channel rehearsal (§10 D.6). If it proves visible: replace this segment with a DIY 100160 Delrin connector + 4× individually-shielded twisted pairs (needs T1 contacts 100181 + crimp tool 100190, $1,074 — avoid unless proven necessary) |
| JB → boards (tails) | 2-pair **shielded twisted-pair instrumentation cable** per axis, pair 1 = (p1,p3), pair 2 = (p2,p4) | e.g. Belden 8723-class (2 individually foil-shielded pairs, 22 AWG) — example only, **UNVERIFIED** (not fetched); any equivalent works. Tail shields bonded at **JB end only**, folded back + insulated at the DSUB end |
| Pico logic (out of this harness) | Per ST4: 4 twisted pairs per board (a0/ret, a1/ret, a2/ret, EN/ret), returns starred at the Pico, landed on each board's GND1 | 40_PI_FANOUT §6 [S10] |

**Failure mode if wrong (untwisted pairs):** spin-edge capacitive/inductive pickup between
pairs and axes shows up as a demod residual that looks exactly like a sensor offset — the
failure is silent data corruption, not a hard fault.

---

## 4. Shield & drain plan

| Shield element | Grounded at | Floating at | Why |
|---|---|---|---|
| AC-A / AC-B foil + drain (verified foil+drain construction [S1 p.13]) | **JB earth bus only** | Feedthrough end (Delrin shell is insulating, so the shield cannot touch the flange there — verified shell material [S1 p.13]) | Single-point earth → no shield current loop through vessel/mains |
| JB enclosure (die-cast Al or similar) | Bonded to a **flange bolt** via short earth strap (ring lug) = vessel earth | — | The vessel is the local earth; the box is the one shield-earth node of the whole harness |
| DSUB tail shields | JB earth bus | DSUB plug end — folded back under heat-shrink; **do NOT tie to the DSUB shell** (the J1 shell's connection to GND1 is unknown — tying it would risk an earth↔GND1 sneak bond; ST2 to report the shell net) | Prevents the earth→GND1 loop |
| GUARD-A/B, SPARE-1/2 | JB earth bus | In-vessel end (capped) | §2.2 |
| In-vessel | **No shield braid in-vessel.** The 100040's PEEK braid is mechanical protection, not an electrostatic shield; adding conductive braid in UHV invites virtual leaks, particulates, and an un-cleanable outgassing trap, and every UHV harness the vendor sells is unshielded discrete-wire for this reason (catalog construction [S1 pp.10–11]) | — | Electrostatic environment in-vessel is dominated by the grounded vessel itself + the probe-head graphite shield (2023 heritage); twisting provides the differential-mode rejection |
| LCC seal ring / guard pads (3/8/13/18) | Optional per ST7 §4 — only if the ST8 mount provides a contact; if used, land on GUARD-A/B (vessel earth), never on a signal | — | Removes a floating conductor next to the plate; ENGINEERING JUDGMENT |

**Failure mode if wrong (shield grounded both ends):** mains/vessel ground-loop current flows
in the drain, couples into the 9-wire bundle, and appears as line-frequency + switching hash
on all axes simultaneously — misdiagnosed as board noise.

---

## 5. Grounding topology (three boards, one Pico, one scope — the sneak-path map)

```
  vessel earth ══ flange ══ JB box ── shields/guards (single point)
       ║ (facility earth)                     [NO connection to any GND1]
  mains earth ══ scope chassis ──┬── SMA1 shield ── GND1-X ─┐
       ║                         ├── SMA2 shield ── GND1-Y ─┼─ boards' GND1s common
   (laptop/USB, if earthed)      ├── SMA3 shield ── GND1-Z ─┘   ONLY via scope + star
       ║                         └── SMA4 shield ── Pico GND
  Pico GND ──star──> 3× logic-return wires ──> GND1-X, GND1-Y, GND1-Z (ST4)
  bias sources: 3× floating 100 µA — one per board, NO interconnection, CM set by each
                board's R2/R3 (2.2 kΩ) to its own GND1
```

Rules (each is a checklist line in §10):

| # | Rule | Reason / failure mode if violated |
|---|---|---|
| G1 | The **scope chassis is the only signal-ground common point**; GND1-X/Y/Z meet there via SMA shields (and via the ST4 star returns — the resulting small loops are accepted; see G2) | A second deliberate GND1 interconnection elsewhere (e.g., a "helpful" bus bar at the boards **plus** long mismatched SMA runs) enlarges loop area → spin-rate circulating currents |
| G2 | Pico GND: star returns per ST4 (one return per board, twisted per logic line); dress the three SMA cables together and equal-length so the star↔scope loops have minimal area; **verify** GND1↔GND1 < 10 mV rms while all three spin (§10 D.5) | Daisy-chained returns put board 2/3 switching current through board 1's reference → per-board offset/noise that looks like a sensor fault (ST4 §8) |
| G3 | **No connection between JB earth (vessel) and any GND1** anywhere. The only earth↔GND1 path is the unavoidable scope-chassis→mains-earth one | A harness-shield-to-GND1 tie creates a mains/vessel loop through the measurement reference → hum + shot-correlated transients |
| G4 | Bias sources stay **one per board, floating, unconnected to each other, to GND1, and to earth** (their CM is defined by R2/R3 through the plate) | Sharing one source across boards: the three spinning muxes fight over it — garbage data (F13). Grounding a source terminal: defeats the floating-CM design, CM steps at every phase |
| G5 | J3 has **no ground pin** (HARDWARE_DATA §3): the ST4 return wire must land on a GND1 point on each board (SMA shield solder point or a GND1 test point; a dedicated GND1 post is a rev-B nicety — flag to ST3) | A board with a missing return has its logic referenced only through the SMA shield → edge integrity depends on scope cable dressing (F11) |
| G6 | Scope inputs stay grounded (standard); never float the scope with a cheater plug | Floating-scope "fixes" create the biggest loop of all when someone later re-earths it mid-campaign |

---

## 6. Connector genders down the chain (mis-mate physics)

| Interface | Vessel/left side | Air/right side | Cross-mating possible? |
|---|---|---|---|
| Feedthrough towers (both faces) | male pins ×2 (A, B) | male pins ×2 (A, B) | The two towers are **identical** → A↔B swap possible on both faces. Rotation impossible (screw-boss polarizing key + captured locking screws, verified [S1 p.8]) |
| VC-A/VC-B (vacuum) | — | female PEEK ×2 | Identical → covered by §7 + swap-safe map §8 |
| AC-A/AC-B (air) | female Delrin ×2 | — | Identical → same mitigation |
| JB → DSUB tails | fixed wiring (soldered/screwed in box) | DSUB-9 **male** ×3 | Tails are permanently wired to JB terminals — no swap possible upstream of the plugs |
| DSUB plugs → boards | DSX/DSY/DSZ male | J1 female ×3 (identical boards) | Swap possible → §7.3 ID resistors + colors |
| Bias loop / power headers on each board | J2/J7 and J5/J6 are **both bare 1×02 headers** (HARDWARE_DATA §1) | — | **Cross-plug possible today — this is the one genuinely die-killing mis-mate in the system (F8). Fix required (§7.4)** |

---

## 7. Keying, labeling, and mis-mate prevention

### 7.1 The A/B Sub-C ambiguity (ST5 flag — resolved here)
- At receiving inspection, **permanently scribe/engrave "A"** on the flange rim (air face)
  adjacent to one tower, and a matching scribe on the vacuum face rim adjacent to the *same*
  tower (the pin-position mark mirrors between faces [S1 p.9] — do not rely on visual symmetry;
  the scribe is the datum). Photograph both faces; the photo goes in the harness folder.
- **Bundle-level tags:** stamped 304 SS tags tied with bare SS lacing wire on VC-A ("A") and
  VC-B ("B") ~50 mm behind each PEEK connector. No adhesive labels, no polymer markers
  in-vessel (bake + outgassing). Air side: printed heat-shrink labels on AC-A/AC-B at both ends.
- **Cut-length asymmetry (second, glance-visible key):** trim VC-A free length to the routing
  need + 50 mm, VC-B to the routing need + 0 mm — the A harness is *visibly* the longer one.
- Even if every label fails, the pin map is swap-safe and the §8 fingerprint catches the swap
  before power. Three independent layers.

### 7.2 In-vessel labeling constraints
Allowed materials at the harness: Kapton, PEEK, SS, ceramic — i.e., **stamped SS tags + SS
lacing wire only**. Individual wire identity in-vessel is maintained by *position at the
termination* + the continuity check (§10 Stage 0/B), not by per-wire markers (nine unmarked
amber Kapton wires per bundle; per-wire SS tags would add nine metal objects per bundle for
no benefit). ENGINEERING JUDGMENT.

### 7.3 Board-end DSUB swap (three identical boards)
- **Colored backshells/heat-shrink:** X = red, Y = green, Z = blue, matching colored rings on
  each board's J1 and on the scope channels (CH1=X…).
- **Continuity fingerprint (positive ID independent of color):** inside each DSUB backshell,
  an **ID resistor between spare pins 5 and 9**: DSX = 1.00 kΩ, DSY = 10.0 kΩ, DSZ = 100 kΩ
  (1 %). Measurable at the plug face in seconds; pins 5/9 are spares on J1 (HARDWARE_DATA §3)
  so the resistor never touches board circuits — **conditional on ST2 confirming J1 pins
  3/4/5/8/9 are truly N/C on the board** (flagged).
- Note the *severity* here is low by construction: the three boards are identical, so a DSUB
  swap only mislabels axes (data integrity, not hardware). The coil-only calibration shots
  (rsi plan §3.3) would also catch it — but catch it at the bench instead.

### 7.4 The J2/J5 header fix (NEEDED NOW — the one hard mis-mate)
Replace the bare 1×02 headers' mating scheme so **bias loop (J2/J7) and 24 V power (J5/J6)
cannot physically interchange**: use two different polarized latching housing families (e.g.,
power on locking polarized 2-pin housings, bias loop on a different-pitch or different-family
polarized housing), plus red (power) vs yellow (bias) wire colors and labels. Zero board
respin — this is a mating-connector/housing choice on the existing headers (or a swap of one
header type at next assembly). **Failure mode if skipped:** 24 V into the bias loop drives
≈ 24 V / (R9+R10+2·R_on+R_plate ≈ 1.1 kΩ) ≈ **20 mA through the die — 200× operating current;
likely die damage** (ENGINEERING JUDGMENT on the damage threshold; the plate is only
qualified to 500 µA per the rsi plan's bias-linearity range [S11 §3.1]).

### 7.5 Transport / storage
Fit each DSUB tail with a **shorting cap** (DSUB-9 female with all of 1,2,6,7 commoned) during
transport and storage — the plate is a passive resistor network, so commoning all four
terminals is safe and it ESD-protects the dies the same way thermocouple/RTD shorting plugs
do. Remove as the last step of §10 Stage D. ENGINEERING JUDGMENT (standard practice).

---

## 8. Swap-consequence matrix (why the map is safe, and how each swap is caught)

Healthy fingerprint first (measured at DSUB plug faces + JB, sensors installed, boards NOT
connected):

| Measurement | Healthy value |
|---|---|
| DSx 1↔2, 1↔6, 1↔7, 2↔6, 2↔7, 6↔7 (each axis) | ~0.4–1.5 kΩ each (2023 opposite-pair signature ~650 Ω [S11 §2.1]; exact gen-2 values from incoming inspection — ENGINEERING JUDGMENT band) |
| DSx 5↔9 | 1.00 k (X) / 10.0 k (Y) / 100 k (Z) ID resistor |
| JB B6↔B7 | < 2 Ω (ID loop) |
| Any conductor of one axis ↔ any conductor of another | > 20 MΩ |
| Any conductor ↔ JB earth bus | > 20 MΩ |

| Mis-mate | What lands where | Electrical hazard? | Detected by |
|---|---|---|---|
| **AC-A↔AC-B swapped** (air cables on wrong towers) | X-position ← Z plate; Y-position ← ID loop + guards; Z-position ← X plate | None — plate terminals land on plate positions in the same (p1,p3,p2,p4) order; guards/loop see at most one 100 µA source | **DSY 1↔2 reads <2 Ω** (ID loop) instead of ~kΩ; DSY 6↔7 reads open (guards) |
| **VC-A↔VC-B swapped** (vacuum harnesses on wrong towers, caught ideally at install) | Same signature by symmetry (the loop travels with VC-B) | None (same argument) | Same fingerprint, plus the visible cut-length/tag mismatch at install |
| **Both pairs swapped consistently** (VC and AC both swapped) | Everything lines up again except axes X↔Z exchanged end-to-end | None | ID loop reads correctly (both swapped) → **caught by field polarity check** §10 D.4 (known magnet orientation per axis) and by tags. This is the one swap the electrical fingerprint alone cannot see — hence D.4 is mandatory |
| **DSUB plugs swapped at boards** | Axis data relabeled | None (identical boards) | ID resistor 5↔9 vs the board label; colors |
| **Sub-C connector rotated** | — | Impossible — polarizing screw-boss (verified [S1 p.8]) | — |

**Failure mode if the map were built the "obvious" other way** (X split across A and B, or B's
group at pins 6–9 instead of 1–4): an A↔B swap would then put guard/ID conductors onto one
axis's bias pins *and* plate terminals onto mismatched roles across two axes simultaneously —
still not damaging (current-limited), but the fingerprint becomes ambiguous against a
broken-wire fault, and diagnosis at HSX costs a vessel entry.

---

## 9. Short-circuit FMEA

Severity: 1 = nuisance · 2 = data loss on one axis until fixed · 3 = campaign data quality
compromised · 4 = hardware rework / vessel entry · 5 = sensor die or board destroyed.
All "effect" entries assume the locked architecture: floating per-board 100 µA sources, no
rails in the harness, R2/R3 = 2.2 kΩ CM returns, AD8429 inputs behind the sense mux.

| # | Failure mode | Location | Cause | Effect (quantified where derivable) | Sev | Detection | Mitigation |
|---|---|---|---|---|---|---|---|
| F1 | Pin-to-pin short **within one axis** (e.g., bias pin to sense pin) | Feedthrough tower / connector | Bent 0.040″ pin, Au debris, misaligned mate under the locking screws | Bias current partially bypasses the plate; demod output rails or collapses. **I ≤ 100 µA (source limit) → no damage to die or in-amp** | 2 | Pre-power map (§8): the shorted pair reads Ω instead of ~kΩ; in operation: offset step ≫ 5 mV bench signature | Loupe-inspect pins before *every* mate; keep protective caps on unmated connectors; use high-duty-cycle contacts (110908/110909) if mating >3×/day [S1 p.12] |
| F2 | Pin-to-pin short **across axes** (X↔Y inside tower A) | Feedthrough tower A | Same as F1 | The two floating bias domains become galvanically tied; both axes' CM and demod corrupt; currents still ≤ 100 µA each | 3 | Inter-axis isolation test (§10 C.3); correlated garbage on exactly two axes | GUARD-A on pin 5 sits numerically between the groups (geometric adjacency UNVERIFIED — treat as any-to-any); same inspection discipline |
| F3 | **Chafed insulation → one conductor to vessel ground** | In-vessel hot zone: wire against SS stand edge, zirconia cube corner, or graphite shield rim; bake + shot vibration | Plate CM dragged to vessel earth; with GND1 ≈ earth (scope path) the in-amp stays in range → axis reads but with CM disturbance; **single fault is survivable** (floating source) | 3 | Continuity-to-earth check pre/post bake and post-pumpdown (§10 B/C); offset step correlated with mechanical disturbance | Keep the PEEK braid jacket to within 20 mm of terminations; fiberglass sleeve over every edge crossing; bend radius ≥ 6× wire OD; SS lacing (smooth, not sharp); route per ST8 harness channel; photo-document the dressed harness before closeout |
| F4 | **Second** chafe fault (two conductors to vessel, same axis) | In-vessel | As F3 | Bias current returns through the vessel instead of the plate → axis dead; fault currents still µA-class | 4 (vessel entry to fix) | Resistance map via feedthrough air side (no vessel entry to *diagnose*) | As F3; the guards + map make the *first* fault visible so the second never accumulates |
| F5 | **Exposed conductor collects plasma current** | In-vessel: any chafe point, uncapped spare, unsleeved splice | Plasma electron/ion current (µA–mA class, shot-dependent) injected into a plate terminal; local heating + electromigration at the die contact | **5 — this is the realistic in-vessel die-killer** | Cannot be detected electrically pre-shot; prevented, not detected | Hard rule: **every in-vessel conductor insulated end-to-end** — spares capped, ID splice sleeved, no bare crimp exposed; graphite shield per 2023 heritage; post-bake inspection before closeout |
| F6 | A↔B connector swap | Flange, either face | Unmarked identical towers (verified no factory marking [S1, S2]) | None electrically (map §8); axes mislabeled if undetected | 2 | §8 fingerprint (ID loop + open pattern); D.4 polarity check catches the double swap | §7.1 scribe + tags + length asymmetry |
| F7 | DSUB tails swapped across boards | Bench | Identical boards | Axis relabeling only | 2 | ID resistors 5↔9; colors | §7.3 |
| F8 | **24 V power plugged into bias loop** (J5↔J2 confusion) | Board headers | Identical 1×02 headers today | ≈ 20 mA forced through plate (24 V / ~1.1 kΩ) = 200× operating current → probable die damage; also blows past the 500 µA qualified range instantly | **5** | None fast enough — prevention only | §7.4 keyed housings + colors + labels — **NEEDED NOW** |
| F9 | **Insulation tester / megger used on sensor lines** | Any test point after carriers installed | Habit ("500 V megger is how you test harnesses") | 2DEG / contact breakdown; die dead. The die's V-withstand is **UNVERIFIED** — treat as tens of volts at most | **5** | Prevention only | §10.0 hard gate: >10 V testing **only** in Stages 0–B (carriers not installed, boards unplugged); red tag on the flange until Stage C sign-off |
| F10 | Shield/drain strand touches a signal terminal | JB | Frayed foil drain, loose strand | That terminal's axis gets earthed → F3-equivalent at air side | 2 | Signal-to-earth isolation (§10 C.4) | Heat-shrink every drain pigtail; comb-type terminal blocks; box inspection photo |
| F11 | Pico GND return missing on one board | Logic bundle | Build omission (J3 has no ground pin — HARDWARE_DATA §3) | Logic still weakly referenced via SMA shield → edges marginal; R5–R8 pulldowns keep EN low if fully floating (board disabled, safe) | 2 | §10 D.1 logic-level check at TP1–TP4 per board | ST4 star returns; checklist line G5 |
| F12 | Shared-return sneak path (GND1 daisy-chain, or shield tied to GND1) | Bench wiring | "Convenient" extra ground wire | Common-impedance coupling: board-to-board offset/noise at spin rate; hum loop through mains/vessel | 3 | GND1↔GND1 < 10 mV rms check (§10 D.5); noise correlated with cable dressing | §5 rules G1–G6; no ad-hoc grounds — every ground wire appears in this document or doesn't exist |
| F13 | One bias source miswired across two boards | J2/J7 cabling | Identical 2-pin cables | Two spinning muxes fight over one source: both axes garbage; currents ≤ source limit (no damage) | 2 | R9/R10 drop check per board: each must read **10.0 mV ± tol across each 100 Ω** (TP5–TP8) with its own source | Per-axis colored + labeled bias cables; keyed housings (§7.4) |
| F14 | Air cables left on during bake | Flange, air side | Handoff gap | Delrin (80 °C max, verified [S1 p.13]) melts onto feedthrough pins | 4 | Visual — too late | SS tag on flange: "REMOVE AIR CABLES + JB BEFORE BAKE"; bake checklist; vacuum side (PEEK, 250 °C) stays |
| F15 | ESD to die via harness during handling | Anywhere the DSUB/plate wires are open-ended | Handling; winter humidity | Die ESD rating UNVERIFIED — assume sensitive (unprotected 2DEG plate) | 5 | Incoming-inspection R-map delta after any suspect event | Wrist strap + dissipative mat for all carrier/harness handling; **shorting caps on DSUB tails whenever not mated** (§7.5) |
| F16 | Debris/flake short inside an unmated connector cap-off period | Any connector | Open connectors during install | As F1/F2 | 2 | Pre-power map | Caps on every unmated connector, always; final map is run *after* the last mate |

**The honest summary the FMEA supports:** within the harness itself, the design is
short-*tolerant* (everything is 100 µA-limited and floating); the five-severity events are all
**procedural or off-harness** (F5 plasma exposure, F8 power mis-plug, F9 megger, F15 ESD).
That is why §10 is a gate, not a formality.

---

## 10. Pre-power test procedure (printable — run in order; initial each box)

### 10.0 Test-equipment rules (read first)

| Rule | Value | Justification |
|---|---|---|
| Insulation-resistance (IR) test voltage, **harness only** (Stages 0–B: carriers NOT installed, boards NOT connected) | **50 V DC**, 60 s, pass ≥ 1 GΩ | Feedthrough rated 500 VDC [S1 p.8]; 50 V gives margin ≫ any operating voltage (≤ ~18 V) with zero risk to hardware present at that stage. Use an insulation tester with a 50 V range or an SMU (50 V, 1 µA compliance) |
| **Absolute test limits once carriers are installed** (Stage C onward) | **≤ 10 V open-circuit, ≤ 500 µA test current, ever** | The die is qualified only to 500 µA bias (linearity data to 500 µA, rsi plan §3.1 [S11]); its voltage withstand is **UNVERIFIED** — a 500 V (or even 50 V) megger across plate terminals must be assumed lethal to the 2DEG. All post-install checks are DMM-class resistance measurements, which is sufficient: every fault class in §9 changes a ≤ 20 MΩ-scale reading |
| DMM qualification (one-time) | Measure your DMM's ohms-range **short-circuit test current** (second meter in series, µA range) and **open-circuit voltage** on every range you will use; record on the checklist. Require ≤ 500 µA / ≤ 10 V | Typical DMMs source ~0.1–1 mA on low-Ω ranges — *verify, don't assume* (ENGINEERING JUDGMENT) |
| ESD | Wrist strap + dissipative mat for every operation from Stage C on; shorting caps on DSUB tails when unmated | F15 |

### Stage 0 — Receiving & bench prep (parts on the bench, nothing installed)
- [ ] 0.1 Verify P/Ns: 100012, 2× 100040, 2× 100020. Inspect all 18 + 18 feedthrough pins
      (straightness, debris) with a loupe. Photograph both flange faces.
- [ ] 0.2 **Scribe "A"** next to the chosen tower on both faces (§7.1); photograph again.
- [ ] 0.3 Feedthrough alone: IR at 50 V — every pin vs shell, and each pin vs 3 nearby pins
      (sampling): ≥ 1 GΩ. Continuity vacuum-pin-n ↔ air-pin-n: < 0.5 Ω for all 18.
- [ ] 0.4 VC-A/VC-B: identify each unterminated lead against its connector socket by
      continuity (use a proper Sub-C test pin, not an oversized probe — socket damage is an
      F1 initiator); tag leads 1–9 temporarily; fit SS bundle tags A/B. Same for AC-A/AC-B
      with heat-shrink labels.
- [ ] 0.5 Build JB per §2 table; drains → earth bus; guards → earth bus; ID terminals; DSUB
      tails with ID resistors (1k/10k/100k) in backshells; colored shrink. Verify the whole
      JB wiring by continuity against the §2 table (all 18 + tails), then IR 50 V
      terminal-to-terminal (no boards, no cables): ≥ 1 GΩ.
- [ ] 0.6 Cut VC-A/VC-B to routing length (A = need + 50 mm, B = need + 0 mm); twist pairs
      per §3; make the B6–B7 crimp splice + sleeve; cap A5/B5/B8/B9; re-run continuity of
      all 18 vacuum leads connector-socket ↔ wire-end after dressing: < 1 Ω.

### Stage A — Full chain on the bench (feedthrough in a vise, everything mated, **no sensors, no boards**)
- [ ] A.1 Mate VC-A→tower A, VC-B→B (vacuum face), AC-A→A, AC-B→B (air face), lock screws.
- [ ] A.2 End-to-end continuity, all 12 signal paths: in-vessel wire end ↔ DSUB plug pin per
      the §2 table. Expect **< 2 Ω** (derivation: 0.5 m of 28 AWG @ ~0.213 Ω/m + 1.22 m of
      24 AWG @ ~0.084 Ω/m + tails + 4 contact interfaces ≈ 0.4 Ω — standard AWG values,
      engineering knowledge). **Any wrong-pin continuity = stop, fix, restart Stage A.**
- [ ] A.3 IR at 50 V: every signal conductor vs every other (12×11/2 pairs may be sampled as:
      each conductor vs its pair partner, vs its group neighbors, and vs one conductor of
      each other group) and each vs JB earth: ≥ 1 GΩ.
- [ ] A.4 Fingerprint: JB B6↔B7 < 2 Ω; DSx 5↔9 = 1k/10k/100k; guards to earth < 1 Ω;
      guards to every signal ≥ 1 GΩ.

### Stage B — Installed on HSX flange, **carriers not yet inserted**
- [ ] B.1 After flange install + in-vessel routing/dressing (ST8): repeat A.2 (continuity,
      now to the mount contact points) and A.3 (IR 50 V) through the full installed chain.
      **This is the last moment 50 V testing is permitted. Red-tag the flange:** "SENSORS
      NEXT — NO TESTING ABOVE 10 V BEYOND THIS POINT."
- [ ] B.2 If a bake occurs before carrier install: remove AC-A/AC-B + JB first (F14);
      re-run B.1 after bake (chafe faults appear at bake — F3).

### Stage C — Carriers installed (sensors in circuit) — **≤ 10 V / ≤ 500 µA only**
- [ ] C.1 Confirm DMM qualification (§10.0) is on file for the ranges used today.
- [ ] C.2 **Per-axis resistance map** at each DSUB plug face (boards NOT connected): all six
      pin combinations of {1, 2, 6, 7}. Expect ~0.4–1.5 kΩ each; opposite plate pairs
      (1↔6 = p1–p2, 2↔7 = p3–p4) near the incoming-inspection values for that die
      (2023 signature ~650 Ω [S11 §2.1]); axes should match each other within ~±20 %.
      **Record actual values — they are the fingerprint for the rest of the campaign.**
- [ ] C.3 Inter-axis isolation: one pin of each axis vs one pin of each other axis (3 combos
      minimum, all 4×4 if time): ≥ 20 MΩ on the DMM MΩ range.
- [ ] C.4 Each axis (any pin) vs JB earth bus: ≥ 20 MΩ. Guards to earth still < 1 Ω.
- [ ] C.5 Fingerprint: B6↔B7 < 2 Ω; DSx 5↔9 ID values; tags/colors photographed as installed.
- [ ] C.6 Repeat C.2–C.5 **after** any bake, pumpdown, or transport, and at HSX before the
      first shot day.

### Stage D — First power (one axis at a time, current-limited by construction)
- [ ] D.1 Boards powered from 24 V, **harness NOT connected, EN low** (Pico idle or
      disconnected — R5–R8 pulldowns hold the board disabled, HARDWARE_DATA §3). Verify
      ±15 V rails; verify logic levels at TP1–TP4 toggle per board when the Pico runs
      (confirms each star return is landed — F11).
- [ ] D.2 Each bias source into a 1 kΩ dummy load: verify 100 µA (100 mV across the dummy).
      Sources labeled per axis, keyed housings verified (§7.4).
- [ ] D.3 **Axis X only:** connect DSX (remove shorting cap last), bias source on, EN still
      low. Verify **10.0 mV across R9 and across R10** (TP5–TP8; 100 µA × 100 Ω) → the full
      bias loop through feedthrough and plate is live and correct. Verify in-amp input CM
      vs GND1 is small (|CM| < 1 V — ENGINEERING JUDGMENT band, set by R2/R3 symmetry).
- [ ] D.4 EN high, spin at 40 kHz: demod offset should be in the bench class (≤ ~5–10 mV —
      the *offset* behavior is bench-proven; **do not judge amplitudes** until the ΔV gain
      anomaly closes, HARDWARE_DATA §5). Then a **known-orientation magnet/Helmholtz polarity
      check on this axis** — this is what catches the consistent-double-swap (§8) and any
      90°/180° die-rotation surprise from ST7 assumption 2.
- [ ] D.5 Repeat D.3–D.4 for Y, then Z. Then all three spinning: measure GND1↔GND1 (X–Y,
      Y–Z) < 10 mV rms; sync on CH4.
- [ ] D.6 **Crosstalk sniff:** X spinning, Y and Z bias sources disconnected → Y/Z outputs
      must sit at the noise floor (tests AC-A shared-bundle coupling, §3). Rotate roles.
      Record; this is the acceptance evidence for the shared-cable decision.

---

## 11. Fallback pin map — 15D-450 (ST5 runner-up, single 15-pin Sub-D on 4.5″ CF)

If UW offers a 4.5″ port and the runner-up is bought instead: one connector kills the A/B
ambiguity entirely (no ID loop needed), and the map transfers group-wise — **X = pins 1 (p1),
2 (p3), 3 (p2), 4 (p4); pin 5 = GUARD-1; Y = pins 6–9 in the same (p1,p3,p2,p4) order;
pin 10 = GUARD-2; Z = pins 11–14 in the same order; pin 15 = shield/drain to JB earth.**
Guards grounded at the JB only, exactly as §2.2; standard two-row Sub-D geometry places
pins 9–15 in the second row (standard connector knowledge), so Y straddles the rows —
acceptable, since the FMEA already assumes any-adjacent-pin shorts and all conductors are
100 µA-limited. Vacuum side: one 100350 15-way Kapton ribbon assembly (cut to length, twist
freed pairs per §3); air side: one 101050 assembly into the same JB; DSUB tails, ID
resistors, grounding, FMEA, and the §10 procedure carry over unchanged — only Stage A's
"two towers" steps collapse to one connector and §7.1/§8's swap items become moot
(15D-450 accessories per the 15D-450 product page, fetched by ST5 this run [S5]).

---

## 12. Recommendations (each with failure-mode-if-wrong)

| # | Recommendation | Failure mode if wrong |
|---|---|---|
| W1 | Adopt the §2 pin map (per-sensor grouping, identical (p1,p3,p2,p4) order on A1–4 and B1–4, guards on 5, ID loop B6–7) | A map without group symmetry turns an A↔B swap into an ambiguous fault signature → mis-diagnosis at HSX costs shots or a vessel entry |
| W2 | Ground shields/guards at the **JB only**; never tie any shield or JB earth to GND1 | Double-ended shields → mains/vessel loop currents in the harness → hum + shot-correlated artifacts on all axes |
| W3 | Scope chassis = the single signal common; ST4 star for Pico returns; no other ground wires exist | Ad-hoc grounds → common-impedance coupling that mimics sensor offset drift (the exact thing spinning was built to kill) |
| W4 | **Fix J2/J5 header keying now** (§7.4) | 24 V into the bias loop = ~20 mA through a die qualified to 500 µA → dead axis, and it can happen silently during a rushed setup |
| W5 | Hard 10 V / 500 µA test ceiling after carrier install; 50 V IR only in Stages 0–B; red tag on the flange | One habitual 500 V megger sweep = up to three dead dies — the single worst outcome available in this project |
| W6 | Every in-vessel conductor insulated end-to-end (caps, sleeves, sleeved splice); PEEK jacket kept to 20 mm of terminations | Exposed conductor in the plasma environment = F5, the realistic die-killer that no pre-power test can catch |
| W7 | ID resistors in DSUB backshells + colored shrink + shorting caps in transit | Silent axis relabeling survives to publication (calibration matrix assigns data to the wrong physical axis); unprotected open tails invite ESD (F15) |
| W8 | Keep the 100020 shared-bundle air segment, but gate it on the D.6 crosstalk sniff at the October rehearsal | If coupling is visible and unaddressed, X-bias edges appear in Y data as a systematic vector error — subtle, calibration-resistant |
| W9 | Run §10 in full at the bench, after install, after bake, and at HSX before first shot | Skipped re-tests let bake/transport chafe faults (F3/F4) reach shot day undetected |

---

## 13. Assumptions made (for the orchestrator to log; ST6 does not write 05_STATE)

1. **A5 (ST5-A1 inherited):** flange = 9C2-275 primary path; the 15D-450 fallback is §11.
2. **A6:** Bias-source compliance ≤ ±18 V (battery box / REF200-class per rsi plan §2.3);
   sets the "worst-case harness voltage" figure. If a higher-compliance source is ever used,
   re-check the AD8429 input abs-max case in F2's "domains tied" scenario.
3. **A7:** J1 pins 3/4/5/8/9 are N/C on the board (HARDWARE_DATA §3 says "spare") — the ID
   resistor and shorting-cap scheme depends on it. **ST2 to confirm from the netlist.**
4. **A8:** The 100040/100020 wires are not color-coded (pages/catalog silent) — identity by
   continuity + tags. If they arrive color-coded, record the color map into the §2 table.
5. **A9:** Sub-C insert geometric pin adjacency unknown (no pin-layout drawing readable) —
   FMEA treats any-pin-to-any-pin shorts within a tower as possible; the guard-between-groups
   benefit is claimed on numbering only.
6. **A10:** ST8's mount provides the wire-to-pad contact and strain relief; termination is
   mechanical (clamp/crimp/spot-weld), no solder in-vessel; the §2 table's LCC pad column
   follows ST7 §4 including its numbering caveat (confirm PB-CA8272-B before bonding).
7. **A11:** Die damage thresholds: qualified operating range taken as ≤ 500 µA (rsi plan
   §3.1 linearity data); voltage withstand and ESD rating UNVERIFIED → treated as fragile
   (drives W4/W5 and the ≤10 V rule).
8. **A12:** In-vessel run length ≤ ~0.5 m (head sits on this flange, Ø31.75 × 27.5 mm
   envelope) — within the 19″ 100040 standard length.

## 14. UNVERIFIED items

| Item | Needed for | Path to close |
|---|---|---|
| Sub-C 9-pin insert geometric pin arrangement/numbering drawing | Adjacency-aware pin assignment (would upgrade guard placement from numeric to geometric) | Vendor mechanical drawing or measure the delivered part; the map is already robust without it |
| Die voltage-withstand / ESD rating | Test-voltage ceiling (currently conservative 10 V) | Fab runsheet / device team; keep 10 V until known |
| J1 spare pins N/C on board | ID resistors, shorting caps | ST2 netlist check (flagged) |
| 100020 / 100040 wire color coding | Build convenience only | Inspect at receiving (Stage 0.4 covers either way) |
| Belden 8723 (JB→DSUB tail example cable) specs | Tail cable purchase | Fetch datasheet at order time; any 2-pair individually-shielded 22–24 AWG equivalent is acceptable |
| Exact adjacent-terminal plate resistance of gen-2 dies | §10 C.2 pass bands | Incoming inspection (rsi plan §2.1) — enter measured values into the checklist before Stage C |
| HSX bakeout temperature/duration for the campaign port | Whether B.2 applies and PEEK margin (250 °C) | UW email (already a ST5 DECISION_GATE input) |

---

## Sources

- [S1] Accu-Glass **Subminiature-C catalog/specifications PDF** (family electrical specs
  500 VDC / 5 A per pin @20 °C, 20 % simultaneity note; polarizing screw-boss; pin-position
  marks mirroring vacuum↔air; 9C2-275 = two 9-pins on 0.750″ centers; 100040 construction:
  9× 28 AWG SPC 7×0.005, Kapton insulation, PEEK braid Ø0.14″, PEEK connector 250 °C;
  100020 construction: 9× 24 AWG tinned Cu 7×0.008, PVC, **Al/Mylar foil + 24 AWG drain**,
  Delrin 80 °C; contacts/tools P/Ns): https://www.accuglassproducts.com/sites/default/files/catalog/subminiature_c_specifications.pdf (fetched + read 2026-07-10)
- [S2] Accu-Glass 9C2-275 product page (P/N 100012, $685, ratings, accessories, ships next
  business day): https://www.accuglassproducts.com/subminiature-c/cf-feedthroughs/9c2-275 (fetched 2026-07-10)
- [S3] Accu-Glass 100040 product page (CKAP-C9-19SC/39SC, $243, 2 A, 250 °C, UHV, PEEK,
  non-terminated far end): https://www.accuglassproducts.com/subminiature-c/uhv-round-cables/9-pin-female-connector-cable (fetched 2026-07-10)
- [S4] Accu-Glass 100020 product page (AIR-CP9-48SC, $154, 4 A, 80 °C, Delrin, non-terminated
  far end): https://www.accuglassproducts.com/subminiature-c/air-cables-components/air-service-connector-cable-female (fetched 2026-07-10)
- [S5] Accu-Glass 15D-450 product page + accessories (100210/100350/101050) — fetched this
  run by ST5 (2026-07-10): https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/15d-450
- [S6] 50_FLANGE/FLANGE_SELECTION.md (ST5 pick, accessories, A/B flag) — internal, this pack
- [S7] 70_PACKAGING/PACKAGING_REVIEW.md (ST7 die→LCC pad map + numbering caveat) — internal
- [S8] 40_PI_FANOUT/PI_FANOUT.md (ST4 star-ground + per-line return recommendation) — internal
- [S9] 01_MISSION/HARDWARE_DATA.md §1–§5 (J1 convention, J3 no-ground, R9/R10, TPs, locked
  constraints, open anomaly) — internal, authoritative
- [S10] = [S8]
- [S11] 01_MISSION/REFERENCE/rsi_experiment_and_publication_plan.md (§2.1 ~650 Ω plate
  signature + incoming inspection; §2.3 grounding intent + per-board floating sources;
  §3.1 bias range to 500 µA) — internal
