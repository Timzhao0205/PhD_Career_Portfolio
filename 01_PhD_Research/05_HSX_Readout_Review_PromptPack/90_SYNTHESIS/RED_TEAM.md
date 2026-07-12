# RED_TEAM — adversarial review of ST1–ST8 deliverables

**WAVE 1 — ST1–ST7 (§§1–7) · WAVE 2 — ST8 3D packaging (§8). Both complete 2026-07-10.**
Reviewer: red-team-critic · 2026-07-10 · effort HIGH.
Method: independent re-derivation of every load-bearing number, end-to-end pin-map trace
against the live netlist (`01_MISSION/REFERENCE/hsx_2026_v2.net`, read directly — not via
ST2's summary), and 9 (wave 1) + 5 (wave 2) fresh fetches of the purchase/bond-critical
citations. Wave 2 additionally read the concept renders as images and re-ran the envelope,
spring, thermal, and matrix arithmetic from first principles.

---

## BLUF (both waves)

**Combined counts: 0 BLOCKER · 5 MAJOR · 14 MINOR · 8 NOTE.**
(Wave 1: 0/2/9/4 · Wave 2: 0/3/5/4.)

**Single most important finding (RT-01, now sharpened by RT-16):** the ST5 primary pick
(9C2-275) is electrically airtight but **mechanically unproven against the locked
Ø31.75 × 27.5 mm probe-head envelope** — and ST8's Concept B quietly inherits the same hole.
B's stack claim (25.8 ≤ 27.5 mm) budgets only **6.5 mm** under the head for the two Sub-C
towers **plus their mated 100040 PEEK connector shells plus the cable exit bend**; tower
protrusion is UNVERIFIED and an axially-mated circular PEEK connector shell almost certainly
does not fit in 6.5 mm. By B's own arithmetic the standoff budget caps at **8.2 mm**, and a
minimum-cube redesign recovers ≤1.5 mm more — so a tower+connector need of >~9.7 mm kills the
2.75″ path outright and forces the ST5 flip. **The Accu-Glass spec-drawing / phone check (tower
protrusion + mated-connector stack height + Ø) must gate BOTH the feedthrough PO and the
ceramics PO** — one call settles it. (The catalog PDF remains unreadable in this environment;
re-attempted and failed again this wave.)

**Wave 2 headline:** ST8's **Concept B (SpringClamp Cube) SURVIVES as the recommendation** —
its contact principle, brittle-body handling, materials chain, matrix arithmetic, and
manufacturability logic all check out, the Concept C (COTS socket) rejection is verified from
the Aries materials block (Au **over Ni** + 150 °C ceiling), and the "replace, don't refine"
verdict on the user's CAD is supported by real STEP measurements. But B is **WEAKENED on three
specifics** before geometry freeze: (i) the envelope pass is overstated while the under-head
clearance is unverified (RT-16); (ii) the **preload tolerance chain is never computed** and the
"±1 % as-sintered is acceptable everywhere" claim has no vendor backing — worst-case stack-up
(~±0.3 mm) exits the springs' 0.2–0.5 mm working band on both sides, so the "optional" pocket-
floor lap must become mandatory or the finger must get longer (RT-17); (iii) the square pocket
plus 4-fold-symmetric contact layout means a **90°/180°-rotated carrier seats and connects
perfectly** — a silent sign flip guarded only by an engraved mark and ST6's D.4 procedure, when
a green-machined corner-chamfer key would cost nothing (RT-18). None of this blocks Aug-2026.

**The wave-1 headline good news stands:** the pin-map chain is **consistent end-to-end**
(die p1/p3/p2/p4 → LCC pads 1/16/11/6 → feedthrough n·1/2/3/4 → J1 pins 1/2/6/7), verified
against the netlist itself; **no deliverable in either wave violated the locked constraints or
leaned on the 2026-07-08 measured amplitudes.** All 14 citation spot-checks across both waves
passed; the new Materion C17200 data (96–97 % stress remaining @100 °C/1000 h, 70–73 %
@200 °C/1000 h) turns ST8's BeCu-relaxation UNVERIFIED into a quantified, survivable margin.

---

## 1. Pin-map chain, traced independently (highest-value check)

Trace performed against `hsx_2026_v2.net` nets 14–17 (read directly this session), ST7 §4,
ST6 §2.1, ST2 §1/§2a, HARDWARE_DATA §3:

| Die terminal (assumed orientation) | LCC pad (ST7, JEDEC-CCW assumed) | FT pin (per axis, ST6) | J1 pin (netlist, verified) | Netlist net → mux nodes (verified) |
|---|---|---|---|---|
| p1 (N) | **1** (mid-N, index side) | n·1 | **1** | `/pin1` → J1.1, U1 S1A/S2A, U2 S3B/S4A ✓ |
| p3 (E) | **16** (mid-E) | n·2 | **2** | `/pin3` → J1.2, U1 S2B/S1B, U2 S4B/S3A ✓ |
| p2 (S) | **11** (mid-S) | n·3 | **6** | `/pin2` → J1.6, U1 S3A/S4A, U2 S2B/S1A ✓ |
| p4 (W) | **6** (mid-W) | n·4 | **7** | `/pin4` → J1.7, U1 S4B/S3B, U2 S1B/S2A ✓ |

- **All three documents agree with each other and with the netlist. No contradiction found.**
- ST2's §2a diagonal analysis re-checked from the raw nets: U1 channels 1/2 identical (bias
  diagonal p1–p3), channels 3/4 identical (p2–p4); U2 channels are the orthogonal diagonal
  with a0 as a pure polarity flip. Consistent with the 8-phase encoding and the demod sign
  rule (+1 if a0==a2). ST2's cross-check is genuine, not decorative.
- ST7's mid-side pad set {1,6,11,16} is internally consistent with CCW numbering N→W→S→E
  (1=N, 6=W, 11=S, 16=E), and the map p1→1, p4→6, p2→11, p3→16 matches it. The alternative
  ±1-pad map (2/7/12/17) is also internally consistent.
- Also verified from the netlist: `/a2` → U3 IN1+IN2 only (closes ST4 assumption 5); `/en` →
  U1.2 + U2.2 only; J1 pins 3/4/5/8/9 are `unconnected-` nets (**closes ST6 assumption A7 —
  the pins-5/9 ID-resistor and shorting-cap schemes are safe**). Neither closure is recorded
  anywhere; synthesis should state both as CONFIRMED.
- **The chain still hinges on two unconfirmed identity facts** (RT-02): LCC numbering
  direction (drawing PB-CA8272-B) and die p1–p4 physical orientation (GDS "C1"). Both are
  honestly flagged with numbering-agnostic mitigations, but three separate printed artifacts
  (ST6 §2.1 table, ST7 §4, ST6 §8 fingerprint) propagate the numbers — they are bond-blocking
  gates, not footnotes.
- **A/B double-swap logic checked and holds:** single AC or VC swap → DSY 1↔2 reads the <2 Ω
  ID loop (pathognomonic); consistent double swap → fingerprint clean, X↔Z exchanged, caught
  only by the §10 D.4 per-axis magnet polarity check — ST6 correctly makes D.4 mandatory.
  One accuracy gap in the swap matrix found (RT-03, below).

---

## 2. Findings table

| ID | Sev | Deliverable | Claim attacked | Finding | Concrete failure scenario | Evidence that settles it | Status |
|---|---|---|---|---|---|---|---|
| RT-01 | **MAJOR** | ST5 (50_FLANGE) + addendum | "Primary: 9C2-275 … conditional on UW confirming the port is 2.75″ CF" | The purchase gate omits the **envelope fit-check**. Two Sub-C towers on 0.750″ centers + 2 mated 100040 PEEK connectors + cable exits occupy the same Ø31.75 × 27.5 mm cylinder the ST8 stand/cube must fill; tower protrusion height is UNVERIFIED (ST5 §7 admits it). The 2023 heritage proves coexistence with ONE Sub-D tower, not two Sub-C towers spanning most of the envelope diameter. | Feedthrough + ~$800 accessories bought; ST8 then finds no landing area for the stand feet and insufficient height under 27.5 mm → rework to 15D-450 path, ~$1.5k stranded + schedule slip to the Nov 2026 campaign | Sub-C spec drawing (tower Ø + protrusion height + mated-connector stack height — the catalog PDF ST6 already parsed pp.8–9, or one call to Accu-Glass) **plus** an ST8 CAD fit-check with mated connectors modeled, **before** the PO | **SUSTAINED** — make it a blocking DECISION_GATE input alongside the port-size question |
| RT-02 | **MAJOR** | ST7 §2/§8 → ST6 §2.1 | Pad numbers 1/16/11/6 and die orientation p1=N/p2=S/p3=E/p4=W | Both are ASSUMPTIONS (flagged), yet the numbers are propagated into ST6's printed harness table and fingerprint procedure. If Spectrum numbers CW, or the die's p-labels sit on different physical sides, every pad number in two documents is wrong (the *physical* mid-side instruction survives; the *paper* doesn't) | Assembler bonds per the printed table without the drawing check → 90° rotation = bias/sense pairs swapped (confusing, detectable), 180° = silent sign flip that survives to calibration | 5-minute read of drawing PB-CA8272-B (shipped with the purchased parts) + the GDS "C1" image; ST7 §9 already requests both. Must be a **bond-blocking gate**, then update ST6 §2.1 numbers | **SUSTAINED** (flagged by authors; severity raised because 3 artifacts carry the numbers) |
| RT-03 | MINOR | ST6 §8 | AC-A↔AC-B swap row: "Y-position ← ID loop + guards … None [hazard]" | Row is **incomplete**: in that swap, Y's real plate wires (tower A pins 6–9) land on JB terminals B6–B9, where B8/B9 carry **removable earth jumpers** — Y's p2/p4 get tied to JB earth (and to each other via the earth bus). Still 100 µA-limited, still no damage, and DSY 1↔2 <2 Ω still detects it — but a troubleshooter trusting the matrix could read Y-to-earth continuity as a chafe fault (F3) instead of a swap | Mis-diagnosis at HSX: hunting a phantom in-vessel chafe (vessel-entry conversation) when the fault is an air-side cable swap | Desk-check only: rewrite the row to include the JB-side consequence; add "DSY 6↔7 to earth <1 Ω" as a swap co-signature | **SUSTAINED** — one-row fix before the table is printed |
| RT-04 | MINOR | ST1 §AD8429 | "Crossover … ≈ 1.6 kΩ per input ≈ 3 kΩ differential" | Arithmetic ignores the 2.2 kΩ return shunt it used everywhere else: per-input impedance = R_s/2 ∥ 2.2 kΩ, which **saturates at 2.2 kΩ** — 1.6 kΩ per input corresponds to ≈ 11.7 kΩ differential source, not 3 kΩ. Error is in the **conservative direction**: the AD8429's win region is ~4× wider than stated | None — a corrected number strengthens KEEP. Reported to keep the synthesis honest | Re-derivation (done here): R_s/2 ∥ 2.2k = 1.6k → R_s ≈ 11.7 kΩ | **RESOLVED by my check** — verdict KEEP AD8429 stands, stronger |
| RT-05 | MINOR | ST1 §7 vs ST4 §5 | Buffer threshold "450 pF ≈ 4–5 m" (ST1) vs "400 pF ≈ 7.4 m" (ST4) | Reconciled — see §3 below. Capacitance thresholds effectively agree (400–450 pF); the meters diverge only because ST1 assumed 100 pF/m (uncited judgment) and ST4 used 50 pF/m (two cable datasheets). Different drive models (12 mA current-limit vs 50 Ω RC) coincidentally converge | If synthesis carried both numbers unreconciled, a future 5 m run would get contradictory advice | Carried number fixed in §3 | **RECONCILED** |
| RT-06 | MINOR | ST3 §3.2 | "Even zeroing both schedule and reuse … C still edges A 275→235 vs 210" | "235" reproduces from nothing; correct zeroed-weight totals are **C 275, A 210, B 215**. The conclusion (C still wins; margin is intrinsic) is right; the sentence contains a garbled number, and it hides that B outranks A in that hypothetical | A reader re-running the sensitivity math distrusts the whole matrix | Recompute (done): weights {15,10,15,5,15}: C=75+40+75+25+60=275, A=45+40+45+20+60=210, B=60+50+30+15+60=215 | **RESOLVED by my check** — recommendation unaffected; fix the sentence |
| RT-07 | MINOR | ST2 §4/F3 + ST6 §4 | ST6: "ST2 to report the [J1] shell net" | ST2 never answered. Netlist J1 has only pins 1–9 — **no shell/board-lock pin exists in the schematic**, so the shell's grounding is decided by the layout footprint (board-lock holes in GND1 copper?) and cannot be verified from the files in the pack. ST6's shield plan already avoids relying on the shell (fold-back, no tie) — robust either way | If the shell happens to land on GND1 copper AND someone later ties a tail shield to the backshell, the earth↔GND1 sneak loop ST6 forbids appears silently | Layout file or first-article ohmmeter check: J1 shell/bracket ↔ GND1. Add to ST6 Stage 0/D checklist | **SUSTAINED** — cheap check, assign it explicitly |
| RT-08 | MINOR | ST5 BLUF | Primary pick presented within Q5's scope | Q5/REFERENCE_DATA scoped the menu to the **Sub-D CF family**; the 9C2-275 is **Sub-C** — outside the given menu, different connector family, different mating hardware/contacts/tooling, and the more expensive system (~$1,572 vs ~$952). The excursion is *defensible* (I verified there is no ≥12-pin Sub-D on 2.75″ CF — family page + 15d-275 404 + Sub-C page "only 9-pin configurations … two on a 2.75″ CF") and it is the only port-preserving option; but the synthesis must present it as a deliberate family change, not a like-for-like swap | User approves "the flange rec" without registering that every mating connector, contact, and spare in the 2023-era Sub-D toolkit becomes obsolete | Already settled by my fetches (§4); present as an explicit trade in DECISION_GATES | **SUSTAINED as a framing fix** — engineering content correct |
| RT-09 | MINOR | ST1 §U1/U2 | "ADG1409 class … ~50–100× the injected charge" | The rejection of the low-R_on alternative rests on an **uncited** Q_inj figure for ADG1409. Plausible (low-R_on switches carry large gate charge) but it is exactly the class of from-memory number SOURCE_STANDARDS forbids | None practical — nobody is advocating the swap; but the pack's quality bar says cite or mark UNVERIFIED | One fetch of the ADG1409 datasheet Q_inj row, or relabel the sentence UNVERIFIED/judgment | **SUSTAINED** (cosmetic; verdict independent of it) |
| RT-10 | MINOR | ST5 §1 vs ST6 §1 | ST5: "Stock/lead time not listed — UNVERIFIED" vs ST6 [S2]: 9C2-275 "ships next business day" | Direct contradiction between two deliverables citing the same page on the same day. ST6's quote is the more specific; either way phone confirmation is still owed for the 2026 schedule | Synthesis copies ST5's "unknown lead time" and schedules a buffer that isn't needed — or vice versa | Re-read the 9C2-275 page shipping note / call Accu-Glass at PO time | **SUSTAINED** — trivial, resolve in synthesis wording |
| RT-11 | MINOR | Mission pack itself (affects ST7) | REFERENCE_DATA §C2: die has "4 **corner** contacts p1–p4" vs PACKAGING_LCC02046 §B: pads at **N/E/S/W mid-sides** | Internal contradiction in the pack's own reference data. ST7 built on the detailed §B description (reasonable), but if the GDS actually has diagonal/corner pads, the radial mid-side map's bond angles and the "no crossing" claim change (likely still fine at 45°, but lengths/geometry shift) | Bond plan drawn for N/E/S/W meets a 45°-rotated die at the bonder | The GDS "C1" image (same evidence as RT-02) | **SUSTAINED** — folded into the RT-02 bond gate |
| RT-12 | NOTE | ST1 §U5 / ground truth | "~1–2 kHz effective demod band" vs locked "10–20 kHz demodulated BW is sufficient" | HARDWARE_DATA itself carries the tension (usable demod BW ~1–2 kHz **at 40 kHz phase rate**; 10–20 kHz demod BW implies running nearer the 100 kHz phase-rate ceiling). Not a deliverable error; ST1's spur-rejection argument and ST4's edge margins were checked at the 100 kHz point and both hold | If synthesis quotes "1–2 kHz" as the system bandwidth, it understates the locked requirement | Note in synthesis: requirement is ≤20 kHz demod; margins verified at the 100 kHz phase-rate point | **RESOLVED** (verified margins cover it) |
| RT-13 | NOTE | ST4 §2 | C_IN = 5 pF/pin "UNVERIFIED" | I verified C_IN from the ADG1209 datasheet mirror: **2 pF typ** (ADG5236: 3 pF per ST1). ST4's 5 pF was conservative by 2.5×; its verdict already survived 2× stress. Closes ST4's biggest UNVERIFIED | None — margin grows | Done (fetch, §4) | **RESOLVED by my check** |
| RT-14 | NOTE | ST1 §Needed-now / ST5 | Parts availability for the ×3 build | RS6-2415D: 701 in stock at Digi-Key but **17-week manufacturer standard lead time** — if the July buy slips and stock drains, the DC/DC becomes the schedule long pole. Order the ×3 (+spares) in the July PO as ST1 says | Late order + stockout = 17-week wait through the Sept assembly gate | Digi-Key page (fetched, §4) | **RESOLVED** — reinforces ST1's "buy in July" |
| RT-15 | NOTE | All seven | Locked-constraint & anomaly discipline | Checked explicitly: no high-temp/wideband readout concerns smuggled in; no radiation scope creep; no conclusion anywhere rests on the 2026-07-08 amplitudes (ST6 D.4 even quarantines amplitude judgment inside the procedure). ST3's fact-fix (replicate **v2**, not the rsi plan's "v1") is correct per HARDWARE_DATA §1 | — | — | **CLEAN PASS** (reported because a zero-findings claim needs evidence: every file was searched for these three failure classes) |

---

## 3. ST1-vs-ST4 buffer-threshold reconciliation (the known inconsistency — settled)

| | ST1 §7 | ST4 §5 |
|---|---|---|
| Timing criterion | edge ≤ 1 % of 12.5 µs half-phase @ 40 kHz = 125 ns | 5τ ≤ 1 % of 10 µs period @ **100 kHz ceiling** = 100 ns |
| Drive model | constant-current 12 mA slew | RC with R_o = 50 Ω (conservative) |
| **C threshold** | **≈ 450 pF** | **≈ 400 pF** |
| Cable assumption | 100 pF/m (uncited judgment) | 50 pF/m (Samtec 44.6 / Weico 50.9 pF/m, cited) |
| **Meters** | 4–5 m | 7.4 m (18 m at 40 kHz) |

**Resolution:** the two capacitance thresholds agree to within 12 % despite independent
models — the number is robust. The entire meters discrepancy is the pF/m assumption, where
ST4 has datasheet backing and ST1 does not. **Synthesis carries: buffer trigger ≈ 400 pF per
shared line (strictest case, 100 kHz phase rate), ≈ 7 m with the quoted 50 pF/m twisted pair,
≈ 3.5–4 m worst-case with 100 pF/m ribbon.** Against ST3's fixed geometry (10–20 cm
baseplate jumpers, ≤1–2 m absolute worst), that is ≥10× margin under every assumption set —
**KEEP direct fan-out is safe under both documents' math; the verdict never disagreed, only
the annotated trigger distance.**

---

## 4. Citation spot-check results (9 fetched this session)

| # | Citation | Claimed by | Fetched result | Verdict |
|---|---|---|---|---|
| 1 | Accu-Glass 9C2-275 page | ST5/ST6: P/N 100012, $685, 18-pin (2×9) Sub-C, 2.75″ CF, 5 A, −200…250 °C, 1×10⁻¹⁰ Torr, male/male | All confirmed verbatim; voltage NOT on product page (as ST5 said) | **PASS** |
| 2 | Accu-Glass Sub-C CF family page | ST5/ST6: family 500 VDC, 5 A (20 % simultaneity), only 9-pin inserts, "two … on a 2.75″ CF" | Confirmed, including the exact dual-9-pin-on-2.75″ wording | **PASS** (closes ST5's family-level-only 500 VDC caveat) |
| 3 | Accu-Glass Sub-D CF family page | ST5: no ≥12-pin Sub-D on 2.75″ CF | Page lists no such option; reducer marketing implies high counts live on 4.5″ | **PASS** (negative claim corroborated; 15d-275 404 check was ST5's) |
| 4 | Digi-Key D09S33E6GX00LF | ST2: female sockets/receptacle, 9 pos, THT right-angle, solder, Active | All confirmed; $2.09 ea | **PASS** |
| 5 | Spectrum LCC page, LCC02046 row | ST7: 20 pads, 0.35″ body, 0.16″ cavity, 0.050″ pitch, S/R 0.314/0.254″, lid CL-30010, "NON-MAGNETIC / NO NI", drawing PB-CA8272-B | Row confirmed verbatim (note full text: "NON-MAGNETIC / NO NI **NOT ZERO TESLA**") | **PASS** |
| 6 | Digi-Key RS6-2415D | ST1: Active, $20.37, 18–36 V, ±15 V/200 mA, 1.6 kV (Digi-Key figure) | All confirmed; +17-wk mfr lead time, 701 in stock (RT-14) | **PASS** |
| 7 | Accu-Glass 100040 | ST5/ST6: $243, 2 A, 250 °C, 1×10⁻¹⁰ Torr, PEEK, 9× 28 AWG Kapton, non-terminated far end, 19″/39″ | All confirmed | **PASS** |
| 8 | AD8429 datasheet (radiolocman mirror, as ST1 cited) | ST1: e_ni 1.0 nV/√Hz, e_no 45 nV/√Hz, i_n 1.5 pA/√Hz @1 kHz, CMRR(G=100) 120 dB DC / 90 dB @5 kHz | All confirmed from the mirror ST1 actually used | **PASS** |
| 9 | ADG1209 datasheet (rlocman mirror, ±15 V table) | ST1: R_on 120 Ω typ, Q_inj 0.4 pC typ, C_IN 2 pF, V_INH 2.0 V, transition 80/130 ns | All confirmed — and the mirror shows the 0.4 pC condition (V_S=0, R_S=0, C_L=1 nF) **explicitly on the dual-supply table**, closing ST1 assumption 6 | **PASS** |

Direct analog.com/PDF fetches failed for me too (ECONNRESET/timeout), matching the subagents'
reports — the mirror-based citation strategy was necessary, and the mirrors check out.
**No UNVERIFIED item was found silently treated as verified downstream**; the one near-miss is
ST5's family-level 500 VDC, which the ST6 catalog read and my fetch #2 both closed.
UNVERIFIED items that remain genuinely open: RS6 switching frequency/ripple, ADG5236 numeric
latch-up mA, RP2350 electrical table (RP2040 precedent used), Sub-C protrusion height (RT-01),
die V-withstand/ESD (drives ST6's 10 V rule — correctly conservative).

---

## 5. Anomaly-sensitivity map (if the ΔV check shows in-operation gain ≠ ~100×)

| Verdict | Survives gain ≠ 100×? | Why |
|---|---|---|
| ST1 all-KEEP + AD8421 reject | **Yes** | Noise ranking and Q_inj/R_on arguments are amplitude-independent (ST1 says so explicitly, and it's true — checked). If the anomaly turns out to be a *board-level* gain fault, the affected artifact is the **layout/wiring**, not the device choices |
| ST1 ADA4898 leave-unplaced | **Yes** | Rejection rests on topology and the ≤20 kHz lens, not on any measured level |
| ST2 PASS-with-flags | **Yes** | Pure topology; and anomaly branch (b) ("2.2 kΩ not unbalancing the emulator bridge") is a bench-emulator artifact, not a board defect |
| ST3 Option C | **Conditionally** — the only anomaly-coupled verdict | ST3's own flip condition: if the anomaly forces a layout respin, heritage evaporates → flip to Option A. Timing is right (anomaly closes before Sept board assembly). **This is the one place the synthesis must keep the anomaly wired to a decision** |
| ST4 no-buffer + star ground | **Yes** | Logic-side only |
| ST5 flange, ST6 wiring, ST7 packaging | **Yes** | Mechanical/harness; no dependence on signal amplitude. ST6 D.4 explicitly defers amplitude judgment until closure |

Every file carries the required anomaly flag. Discipline held.

---

## 6. Verdict summary per recommendation

| Recommendation | Red-team status |
|---|---|
| ST1: keep entire chain; reject AD8421; leave ADA4898-2 unplaced | **SURVIVES** (noise sum reproduced digit-for-digit; RT-04 error is conservative; RT-09 cite gap cosmetic) |
| ST2: PASS-with-flags F1–F5 | **SURVIVES** (independently re-verified from the netlist; add RT-07 shell-net action) |
| ST3: Option C, ×3 replicated boards, side-by-side rack | **SURVIVES** (matrix arithmetic verified: 310/275/475; RT-06 typo to fix; flip condition genuine and correctly timed) |
| ST4: keep direct fan-out, star ground | **SURVIVES / RECONCILED** (carry 400 pF ≈ 3.5–7 m trigger, §3) |
| ST5: 9C2-275 primary | **WEAKENED** (RT-01: add envelope/protrusion fit-check as a blocking gate; RT-08 framing; runner-up 15D/25D-450 path intact) |
| ST6: pin map + FMEA + pre-power procedure | **SURVIVES** (chain verified; RT-03 one-row correction; A7 now CONFIRMED from netlist) |
| ST7: ADJUST — mid-side pads, mount-level one-side routing, no Kovar lid, open cavity | **SURVIVES** (LCC row verified incl. CL-30010 and non-magnetic note; RT-02/RT-11 are bond-blocking evidence gates, not verdict changes) |

**Aug-2026 impact check:** no surviving recommendation touches the single-axis board's
schematic/layout. The only near-term hardware action, ST6 W4 (keyed J2/J5 mating housings),
is a connector-housing change that *protects* the Aug build — do it on the bench setup too.

---

## 7. Assumptions made (this pass)

1. Sub-C 9-pin tower shell diameter ~11–12 mm used in the RT-01 geometry concern —
   ENGINEERING JUDGMENT from typical circular-subminiature shells; the concern stands on the
   verified 19.05 mm tower centers alone and is settled by the spec drawing either way.
2. JEDEC MS-004 CCW numbering arithmetic (pads 1/6/11/16 = mid-sides, order N→W→S→E viewed
   cavity-up) re-derived independently to check ST7's internal consistency — same UNVERIFIED
   status as ST7's; RT-02 gate applies.
3. Zeroed-weight sensitivity recomputation (RT-06) uses ST3's own scores unchanged.
4. Treated the pack-internal files (HARDWARE_DATA, netlist) as authoritative over prose in
   deliverables wherever they disagreed, per SOURCE_STANDARDS §4 — no such disagreement found
   except RT-11 (two pack reference files disagreeing with each other).

## Sources (fetched this session, 2026-07-10)

- Accu-Glass 9C2-275: https://www.accuglassproducts.com/subminiature-c/cf-feedthroughs/9c2-275
- Accu-Glass Sub-C CF family: https://www.accuglassproducts.com/subminiature-c/cf-feedthroughs
- Accu-Glass Sub-D CF family: https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs
- Accu-Glass 100040: https://www.accuglassproducts.com/subminiature-c/uhv-round-cables/9-pin-female-connector-cable
- Digi-Key D09S33E6GX00LF: https://www.digikey.com/en/products/detail/amphenol-cs-fci/D09S33E6GX00LF/1539664
- Digi-Key RS6-2415D: https://www.digikey.com/en/products/detail/recom-power/RS6-2415D/6206497
- Spectrum LCC (LCC02046 row): https://www.spectrum-semi.com/products/leadless-chip-carrier
- AD8429 datasheet mirror (noise/CMRR page): https://www.radiolocman.com/datasheet/pdf.html?di=126283&p=3
- ADG1208/1209 datasheet mirror (±15 V table): https://www.rlocman.cn/datasheet/pdf.html?di=176133&p=2
- Local ground truth read directly: `01_MISSION/REFERENCE/hsx_2026_v2.net` (nets 1–20 incl.
  /pin1–/pin4, /a0–/a2, /en, /ib*, GND/GND1), `01_MISSION/HARDWARE_DATA.md`,
  `01_MISSION/REFERENCE/PACKAGING_LCC02046.md`, `01_MISSION/REFERENCE/PACKAGING_3D_ENVELOPE.md`,
  `01_MISSION/REFERENCE_DATA.md`.
- (Failed fetches, consistent with subagent reports: analog.com AD8429/ADG1208_1209 PDFs —
  ECONNRESET/timeout.)

---
---

## WAVE 2 — ST8 (3D packaging)

Reviewer: red-team-critic wave 2 · 2026-07-10 · effort HIGH.
Target: `80_3D_PACKAGING/PACKAGING_3D_DESIGN.md` + concept folders. Method: re-derived the
envelope, spring (k, force, stress), thermal, vibration, and decision-matrix arithmetic from
first principles; **read the renders as images** (B iso/section/front/top, D iso/top, C top,
user_assembled_iso) and cross-checked against the text; read `concept_B.py` (the envelope
asserts) line-by-line; 5 fresh citation fetches ([PC], [AG-S], [AR], Materion C17200
relaxation, Victrex PEEK) + one re-attempt on the Sub-C catalog PDF (failed again — no PDF
rendering in this environment, matching ST5's report).

**Wave 2 counts: 0 BLOCKER · 3 MAJOR · 5 MINOR · 4 NOTE.**

### Arithmetic independently reproduced (all PASS)

- Envelope: worst corner √(9.8² + 6.7²) = **11.87 mm** ≤ 15.875; stack 6.5+2.0+15.0+1.0+1.3 =
  **25.8 mm** ≤ 27.5; both asserts present and correct in `concept_B.py`. Ears at 15.0 mm ✓.
  D: 13.31/25.5 claims not re-derived to the mm but consistent with the renders (all geometry
  inside the envelope cylinder in `concept_D_top.png`).
- Spring: k = 3EI/L³ with E=131 GPa, 1.5×0.10×3.5 mm → **1.15 N/mm** (deliverable 1.3 — within
  E-value spread); F(0.35 mm) ≈ **0.40–0.46 N** ✓; σ = 6FL/(wt²) ≈ **630 MPa** (deliverable
  ~550) — both below aged-C17200 yield, same conclusion.
- Thermal: Δα(YSZ−alumina) 3.5 ppm/K × 9 mm × 150 K ≈ **4.7 µm** ✓ — genuinely negligible vs
  350 µm travel. Bolt-axis ΔCTE adds ~40 N to an M1.6 Ti bolt at +175 K — fine.
- Vibration: 1.8 N / (0.5 g) = **367 g** unload threshold ✓ (claimed >350 g).
- Decision matrix: A 2.55 / B 4.84 / C 2.94 / D 4.70 — all four weighted totals reproduce
  exactly; C's disqualification-by-gate regardless of score is correctly applied.
- Bearing stress: land annulus (8.4²−7.0²) = 21.6 mm², 2 N → ~0.1 MPa ✓; frame window 7.0 >
  cavity opening 6.10 → the frame never overhangs the open cavity ✓ (bond-wire clearance
  claim holds; wires top out below the carrier surface on the recessed shelf).

### Findings table (continuing the series)

| ID | Sev | Deliverable | Claim attacked | Finding | Concrete failure scenario | Evidence that settles it | Status |
|---|---|---|---|---|---|---|---|
| RT-16 | **MAJOR** | ST8 §2/§5-B/§7 (extends RT-01) | "Passes every hard constraint with margin … stack 25.8 ≤ 27.5 mm" with "6.5 mm nominal, adjustable" reserved under the head (A2) | The stack pass is **overstated**: the 6.5 mm line must contain the UNVERIFIED tower protrusion **plus the mated 100040 PEEK connector shell plus the cable exit bend** — the mated-connector item is absent from the height ledger entirely, and an axially-mated circular PEEK shell almost certainly exceeds 6.5 mm on its own. By B's own arithmetic the standoff caps at **8.2 mm** (27.5 − 19.3); shrinking the cube can't recover more than ~1.5 mm because the 13.4 mm Ti frame sets a ~13.5–14 mm minimum face. ST8's flip trigger "towers >~10 mm" is **more permissive than its own math** (breach begins >8.2 mm). Radially: towers at ±9.525 mm centers with ~Ø11–12 shells put the tower edge at ~15.5 mm ≈ the envelope wall; the mated shell Ø is unknown. Note A2's basis — the 6.64 mm gap measured in the user's CAD — is heritage from the single-tower Sub-D 9D-275, not evidence about Sub-C | Zirconia body + frames + inserts ordered against `concept_B.step`; Accu-Glass drawing then shows tower+connector needs 12–20 mm → head cannot sit inside 27.5 mm → either the ceramics or the $685 feedthrough is scrap; schedule slips past vector-probe integration | One call to Accu-Glass (or the Sub-C spec drawing pp. 8–9 the ST6 run parsed): tower protrusion, tower/shell Ø, **mated 100040 stack height**, and whether a right-angle/low-profile exit exists; then a CAD fit-check **with mated connectors modeled**, all **before both POs**. (Re-attempted the catalog PDF this wave — unreadable here) | **SUSTAINED** — fold into the RT-01 DECISION_GATE as one blocking fit-check; fix the flip-3 threshold to 8.2 mm |
| RT-17 | **MAJOR** | ST8 §5-B/§8 | "As-sintered ±1 % is ACCEPTABLE EVERYWHERE because the spring stack absorbs ±0.15 mm — no post-sinter diamond grinding required"; pocket-floor lap "optional" | The **preload tolerance chain is never computed**, and the fetched [PC] page gives **no as-sintered tolerance figure at all** (it says green machining "prevents tight tolerances") — the ±1 % rule is the deliverable's own, and vendors typically quote ±1 % **or ±0.1 mm, whichever is greater**. Stack-up: pocket depth 2.15 (±0.1 floor) + carrier thickness 1.65 (drawing tol UNVERIFIED, class ±0.13) + PEEK insert 1.0 (±0.05) + spring form height (±0.05) → worst ≈ **±0.3 mm** against a claimed 0.2–0.5 mm working band around δ=0.35. Low tail δ≈0.05 → ~0.06 N/contact, far below A4's own 0.3 N floor → intermittent opens under vibration; high tail δ≈0.65 → σ≈1.1+ GPa > yield → **permanent finger set**, preload lost on every later cycle | Three assembled axes pass bench continuity cold, then one channel goes intermittent at HSX after the first thermal cycle — presents exactly like the in-vessel chafe fault the user fears most, on hardware that was "in spec" | Cheap: (i) make the pocket-floor grind/lap **mandatory** (±0.02 mm), or measure-and-shim each pocket, or lengthen the finger (L 3.5→5 mm halves k and stress, widens the band ~2×); (ii) put a toleranced stack-up in the freeze drawing; (iii) the A5 force-deflection test on photo-etch prototypes, already planned, closes the spring side | **SUSTAINED** — must be resolved in the geometry freeze, before the ceramics RFQ |
| RT-18 | **MAJOR** | ST8 §5-B insert/remove step (1) | "Drop carrier in, chamfer to the engraved pin-1 mark" | **No mechanical anti-rotation keying.** The pocket is square and the 4-contact layout is 4-fold symmetric, so a carrier inserted at 90°/180°/270° seats perfectly, clamps normally, and **makes all four contacts** — 180° is a silent sign flip, 90° swaps bias/sense pairs. The only defenses are an engraved mark + operator care + ST6 §10 D.4 (procedural). Carriers are *designed* to be swapped in ~2 min in the field, multiplying the exposure; this is the same silent-sign-flip class as RT-02 but with a zero-cost hardware fix available in green machining | Field carrier swap between run days, D.4 skipped "because nothing else changed" → one axis reports −B; vector reconstruction is silently wrong for the campaign | Add a **corner key**: chamfered/filled pocket corner mating the LCC's pin-1 index chamfer (green-machinable; zirconia brief explicitly allows chamfers), or an asymmetric notch in the Ti frame + carrier land. Keep D.4 mandatory regardless (defense in depth) | **SUSTAINED** — one-feature ceramic change before freeze |
| RT-19 | MINOR | ST8 §2/A3 (+ user CAD heritage) | Head mounts "via two standoffs on the heritage ±12.5 mm pattern" | The ±12.5 mm pattern is measured from the **user's own CAD**, not from any Accu-Glass drawing; the 9C2-275 has **no documented vacuum-side tapped features**, and at r = 12.5 mm on a 2.75″ CF the landing zone may sit over the bore/ceramic region (stated 1.45″ ID → bore radius ≈ 18.4 mm > 12.5 mm). If a clamp collar or adapter plate is needed, it consumes height (RT-16 budget) and radial margin. A3 flags this but it is not wired into any gate | Ceramics arrive; nothing on the purchased feedthrough to bolt the standoffs into; improvised adapter plate blows the 1.7 mm height margin | Same Accu-Glass call/drawing as RT-16 (one conversation settles both); confirm what the 2023 9D-275 heritage mount actually screwed into | **SUSTAINED** — folded into the RT-16 gate |
| RT-20 | MINOR | ST8 §5-B harness row | Finger tails "crimped or push-on-connected [AG-S] … wires never bend tighter than 5× diameter" | The **12 junctions have no specified home**: face grooves are 2.0 × 1.5 mm, smaller than any crimp splice or Accu-Glass push-on barrel; and my [AG-S] fetch confirms the push-on's **included set screw is stainless steel** — an unvetted (possibly magnetic, work-hardened 18-8) part inches from the Hall plates in a design that elsewhere bans Ni plating. Also unstated: how flat etched tails mate to round push-on/crimp barrels, and how the PEEK insert is retained in a vertical-face pocket when the carrier is out (it can simply fall out during a swap) | Junctions improvised at assembly time end up as solder (banned), or bulk under the base that eats the height budget; SS set screws add a field distortion nobody modeled | Desk fix in the freeze package: junction location (under-base cavity is the natural volume), splice type, set-screw replacement (Ti) or crimp-only, and a captive lip/dot for the insert | **SUSTAINED** — cheap specification work, do before RFQ |
| RT-21 | MINOR | ST8 §5-B ("seal-ring band OD 7.98 mm is a legitimate clamp land") + concept_B.py land 7.0→8.4 mm | Frame bears on the carrier rim — electrically uncharacterized | The Ti frame's land presses directly on the **gold seal-ring metallization** (7.0–7.98 mm of the 7.0–8.4 annulus) — each frame+bolts+nuts becomes a **floating conductor network** capacitively adjacent to its Hall plate, and the seal ring is forced to frame potential. ST7 §4 called seal-ring grounding "optional, coordinate with ST6"; ST8 never states the frames' electrical status. Secondary: repeated clamping burnishes the soft thin Au | Uncontrolled floating electrode next to a 100 µA mV-level sensor; if it intermittently touches a castellation via debris, a phantom leakage path appears and disappears with thermal cycling | One-line design decision, coordinated with ST6: tie frames to the harness drain (a fifth finger in the insert reaching the seal ring, or a drain lug under one frame bolt) **or** document floating-is-acceptable with the coupling estimate | **SUSTAINED** — decide at freeze, zero hardware cost either way |
| RT-22 | MINOR | ST8 §10 + `concept_B_section.png` | "Visuals for every concept (isometric + orthographic + section)" | The B "section" PNG is **not a section** — it is another exterior view; the load-bearing internals (leaf-spring finger, PEEK insert, carrier-in-pocket engagement, land depression 0.35 mm) are **never drawn anywhere**, and per §10 the `concept_B.step` contains only the zirconia body + 3 frames — the insert/springs exist **only as prose numbers**. The single subsystem that decides success is the least-documented artifact in the folder | Photo-etch and PEEK vendors quote from prose; each resolves ambiguity differently; the assembled stack misses the 0.35 mm engagement it was never drawn to hold | Produce a true cutaway + a dimensioned insert/finger detail (2D is fine) before the photo-etch RFQ; re-export the STEP with insert + one formed finger included | **SUSTAINED** — documentation gap, not a design flaw |
| RT-23 | MINOR | ST8 §5-B pocket "9.40 sq … spring compliance absorbs the rest" + A7 | Lateral position of finger tips on 0.64 mm-wide bottom pads | The lateral chain is also uncomputed: pocket 9.40 vs body 8.76–9.14 → up to **0.63 mm slop + ~4° rotation**; a 1.5 mm-wide finger tip on a 0.64 mm pad at 1.27 mm pitch has ~0.2 mm nominal clearance to the adjacent pad — worst-case slop **overlaps the neighbor**. Today the neighbors are unbonded/floating (ST7), so no hard fault — but it silently ties a floating stub to the signal, and if the guard option (pads 3/8/13/18) is ever populated the same slop becomes a signal-to-guard short | Populated-guard variant built later; one axis shows a mysterious few-pF/leakage asymmetry that moves when the carrier is reseated | Narrow the tip to ~1.0 mm and/or add two corner nesting springs that reference the carrier to one pocket corner; state the lateral chain in the freeze drawing (same drawing as RT-17) | **SUSTAINED** — fix rides along with RT-17/RT-18 |
| RT-24 | NOTE | ST8 sources | Citation spot-check (5 fetched this wave) | **[PC]** Precision Ceramics: shrinkage ~20 %, K_IC 8–17 MPa·m½, 10¹² Ω·cm, green-vs-diamond machining — all confirmed; **no tolerance figure** (feeds RT-17). **[AG-S]** Accu-Glass: BeCu push-on 200 °C / in-line 400 °C / 1×10⁻¹⁰ Torr, Au-plated BeCu — confirmed (+ SS set-screw detail, RT-20). **[AR]** Aries: "heat-treated BeCu … 0.75 µ Au over 0.75 µ Ni per SAE AMS-QQ-N-290", −55…150 °C — confirmed verbatim → **Concept C rejection is solid on both counts and P/N-independent**. **Materion C17200 relaxation (searched, task-requested):** ~96–97 % stress remaining @100 °C/1000 h, **70–73 % @200 °C/1000 h** (AT & 1/2HT tempers) — quantifies flip condition 2: at realistic HSX head temperatures (≲150 °C bakes, near-ambient operation) relaxation is negligible; at a true sustained 200 °C, 0.45 N → ~0.31 N, still at the bottom of the 0.3–0.6 N window → the fuzz-button flip is correctly staged, not needed now. **Victrex PEEK:** Tg 143 °C, CUT 260 °C — insert is material-legal at ≤200 °C; it crosses Tg, but clamp stresses (~0.1–0.3 MPa) are far too low for meaningful creep and thickness change is ≪ the 350 µm travel — PEEK choice stands | — | — | **ALL PASS**; BeCu UNVERIFIED now has numbers |
| RT-25 | NOTE | ST8 §3 | "Replace, don't refine" + "his CAD fails the electrical gate" | **Verdict is fair, not overstated.** C1 (no electrical path) is exactly the §F.1 gate and is architectural; C2 (12×12×0.635 mm modeled plate vs the purchased 8.89×8.89×1.65 LCC) is a kernel-measured fact; the render matches the cap-over-plates description; and §3 C10 explicitly preserves everything right about the user's idea, which Concept B then implements. One framing softener for synthesis: the user's CAD **predates** the §F compatibility gate — "fails the gate" reflects requirement evolution, not carelessness; say so at the sign-off | — | — | **SURVIVES as written** (+ framing note) |
| RT-26 | NOTE | ST8 §1/§7 | "Nothing here touches the Aug-2026 single-axis campaign" | Confirmed by inspection: heritage 1D mount untouched, all ST8 hardware is 2026-27 vector-probe scope, no shared parts with the Aug build, and the only coupled action (the RT-16 Accu-Glass call) is a phone call, not bench time. The decision-gate asks (geometry freeze, ceramics PO, tower confirmation) can all slip past August without touching the single-axis schedule | — | — | **CLEAN PASS** |
| RT-27 | NOTE | ST8 all | Locked-constraint & anomaly discipline + self-checks | Checked explicitly: no conclusion rests on the 2026-07-08 amplitudes (pure mechanics); no readout-temperature/bandwidth scope creep; envelope asserts are real executable checks in `concept_B.py` (and correct); matrix, spring, thermal, vibration arithmetic all reproduce (§ above). Orthogonality: B's one-piece as-fired faces beat D's bolted ±0.2–0.5° as claimed; both are calibration-absorbable; ST6 D.4 covers the per-axis sign check — **provided RT-18's keying gap is closed or D.4 is re-run after every carrier swap** | — | — | **CLEAN PASS** (evidence: every failure class from the wave-2 checklist was searched for) |

### Verdict summary — ST8

| Recommendation | Red-team status |
|---|---|
| **Concept B (SpringClamp Cube) — build** | **SURVIVES, WEAKENED on three freeze-blocking specifics**: RT-16 (envelope pass overstated until tower+mated-connector height is read — same gate as RT-01), RT-17 (preload tolerance chain uncomputed; make the pocket-floor lap mandatory or lengthen the finger), RT-18 (add a pocket corner key against silent 180° carrier rotation). All three are cheap, pre-RFQ fixes; none changes the concept ranking |
| Concept D runner-up + "flip on vendor quote" | **SURVIVES** (identical interface inherits the same RT-17/RT-18/RT-23 fixes; flip logic is genuinely procurement-only as claimed) |
| Concept C rejection (COTS sockets) | **SURVIVES — verified** (Aries materials block fetched: Au over 0.75 µm Ni + 150 °C ceiling; envelope violation consistent with the render; rejection is P/N-independent) |
| Concept A as honest baseline, not recommended | **SURVIVES** (its solder-on-castellation cost is exactly what ST7 §5b rejected; correctly kept as fallback S4) |
| User-CAD verdict: replace, don't refine | **SURVIVES** (RT-25: supported by kernel measurements; add the requirement-evolution framing at sign-off) |
| Decision-gate items (i)–(iii) | **ADJUST**: item (iii) "confirm tower protrusion before fixing standoff length" is under-scoped — per RT-16 it must also cover **mated-connector stack height and mounting features (RT-19)**, and it must gate the **ceramics PO and the feedthrough PO**, not just the standoff length; fix flip-condition 3's threshold from "~10 mm" to **8.2 mm** |

**Cheapest evidence that settles the most:** one Accu-Glass phone call (tower protrusion +
mated 100040 stack height + shell Ø + vacuum-side mounting features) closes RT-16 and RT-19
and finally closes wave-1 RT-01; one toleranced stack-up drawing + the already-planned A5
force-deflection bench test closes RT-17 and RT-23; one green-machined chamfer closes RT-18.

### Wave-2 assumptions

1. Vendor as-fired tolerance floor "±1 % or ±0.1 mm, whichever is greater" — ENGINEERING
   JUDGMENT (industry-standard clause); [PC] gives no figure either way, which is itself the
   RT-17 point. A real vendor quote supersedes this.
2. LCC thickness tolerance ±0.13 mm class — ENGINEERING JUDGMENT (drawing tolerance
   UNVERIFIED per ST7 §2); the RT-17 stack-up must use the drawing value once read.
3. Mated 100040 shell axial length > 6.5 mm — ENGINEERING JUDGMENT from circular-subminiature
   connector proportions; settled by the same RT-16 call either way.
4. E(BeCu C17200) = 131 GPa for the spring re-derivation; Materion relaxation data read from a
   datasheet aggregator (lookpolymers) — cite the Materion original in the freeze package.

### Wave-2 sources (fetched 2026-07-10)

- Precision Ceramics zirconia (shrinkage ~20 %, K_IC 8–17, 10¹² Ω·cm, green-vs-diamond, **no
  tolerance figure**): https://precision-ceramics.com/materials/zirconia/
- Accu-Glass specialty connectors (BeCu push-on 200 °C / in-line 400 °C, 1×10⁻¹⁰ Torr, **SS
  set screw**): https://www.accuglassproducts.com/specialty-connectors
- Aries test-socket materials block (Au over 0.75 µm Ni per SAE AMS-QQ-N-290, −55…150 °C):
  https://www.arieselec.com/product/23023-csp-test-socket/
- Materion C17200 stress relaxation (via datasheet aggregator: AT temper 96 % @100 °C/1000 h,
  70 % @200 °C/1000 h; 1/2HT 97 %/73 %):
  https://www.lookpolymers.com/polymer_Materion-Beryllium-Copper-Alloy-25-Strip-AT-TF00-Temper-UNS-C17200.php ,
  https://www.lookpolymers.com/polymer_Materion-Beryllium-Copper-Alloy-25-Strip-12HT-TH02-Temper-UNS-C17200.php
- Victrex PEEK (Tg 143 °C, CUT 260 °C UL 746B): https://www.victrex.com/en/material-properties
  (via search; original FAQ URL 404s)
- Accu-Glass Sub-C specifications catalog PDF — **re-attempted, still unreadable in this
  environment** (no PDF page rendering): https://www.accuglassproducts.com/sites/default/files/catalog/subminiature_c_specifications.pdf
- Local artifacts read directly: `80_3D_PACKAGING/PACKAGING_3D_DESIGN.md`, `concept_B.py`,
  renders `concept_B_{iso,section,front,top}.png`, `concept_D_{iso,top}.png`,
  `user_cad_measured/user_assembled_iso.png`; `70_PACKAGING/PACKAGING_REVIEW.md`;
  `50_FLANGE/FLANGE_SELECTION.md` + addendum; `01_MISSION/REFERENCE/PACKAGING_3D_ENVELOPE.md`;
  `01_MISSION/REFERENCE/PACKAGING_LCC02046.md`.

---

## Post-run note (2026-07-10, not a red-team pass)

The flange pick this wave reviewed (9C2-275, referenced throughout §§ above, e.g. RT-01, RT-16,
RT-19) was **superseded** by a user-directed follow-up: **Accu-Glass 19C-275** (single-shell
MIL-C-26482, 2.75″ CF) is now GATE 2's primary — see `FLANGE_SELECTION.md` §9,
`DECISION_GATES.md` GATE 2. This file's findings are **not re-derived** against the new pick;
every finding above that cites the 9C2-275's dual-tower geometry (RT-01 envelope-vs-towers,
RT-16 height ledger, RT-19 mounting features) should be read as applying to the **fallback** path
only, until a fresh pass re-derives them for a single-shell connector. No new red-team wave has
been run on this change.
