# Independent verification — B25_power FULL attempt-1

- Verifier: `pap06-verifier` (independent; did not produce the candidate)
- Requested verifier model/effort: Fable 5 / xhigh. Runtime self-identification:
  Fable 5 (`claude-fable-5`) per system prompt; effort `NOT_EXPOSED` — recorded
  as observation status, not proof.
- Date: 2026-07-28
- Candidate: `outputs/B25_power/attempt-1/` (read-only; nothing edited)
- Report: this file only; no other file written or modified.

## 1. Scope and inputs

Verified against: `state/CURRENT_VERIFY.md` (verification card),
`workflow/stages/B25_power.md`, `.claude/skills/pap06-native/references/ACCEPTANCE.md`,
`SOURCE_POLICY.md`, `MODEL_POLICY.md`. Ground truth opened independently this run:
`outputs/B20_align/attempt-1/ALIGNMENT.csv` (header + 10 full rows: E-04, C-04,
A-10, C-07, C-12, E-10, C-14, C-15, F-06, plus header comment) and `ALIGNMENT.md`
(§9-§11); `outputs/B15_lit_synth/attempt-1/EVIDENCE_MAP.csv` (ID census EV01-EV35;
full rows EV16, EV17, EV27, EV28, EV30, EV31, EV32) and `GAPS.md` (G5/M1/M6/BT-1..BT-8
structure); `outputs/B10_phd/attempt-1/PHD_FACTS.json` (C01, C03, C04, C06, C13,
C23, C29, C31, C42, C43, C46, C49, C50 — statuses and full text for C03/C04/C06/
C23/C29/C42/C46/C49/C50); `outputs/B00_inventory/attempt-2/INVENTORY.md`
(startup audit-status lines); startup corpus records (detail in §3.3);
`sources/old06/30_SCREENING/EVIDENCE/P3R2-F-06.md` (targeted passages);
`pilot/B25_power/attempt-1/` (file census + SOURCES.csv header); live web
(4 fetch attempts, §3.9). All seven candidate files read in full.

## 2. Summary of verdict basis

All hard gates pass. Two minor defects (§4); no critical or major defect found.

## 3. Check-by-check findings

### 3.1 Files and schemas (gate 1) — PASS

All seven required files present and non-empty; the candidate directory contains
exactly those seven files. `POWER_MAP.csv` line 1 is the exact 13-column header
`idea_id,role,application,phd_leverage,missing_capabilities,buyer,proof_experiment,safety_certification,capital,moat,confidence,falsifier,disposition`;
31 data rows, one line per row, every cell populated. `SOURCES.csv` header is the
exact 10-column schema
`claim_id,url,title,publisher,published_date,accessed_date,source_type,stage_file,confidence,limitation`,
byte-identical to the accepted pilot's header; 19 rows S-B25-01..S-B25-19.

### 3.2 Recounts (gate 2) — PASS

- **Unique IDs:** 31, all distinct, recounted from the CSV: 23 `P3R2-*` +
  8 startup (ST01-C10/C11/C06P; ST03-ID_08/ID_10/ID_12/ID_13; ST05-CF-4).
  Gate >=18 met; claimed 31 = recounted 31.
- **Role distribution:** recounted from the role cells with POWER.md §2's stated
  reconciliation (dual-role rows E-14 -> end product, F-02 -> subsystem,
  C-09 -> reference-design/platform): 12 end products (C-01, A-02, C-07, C-14,
  C-15, D-16, D-19, E-14, F-03, F-12, ST01-C10, ST03-ID_10), 10 subsystems
  (C-13, D-01, D-10, F-01, F-02, F-23, ST01-C11, ST01-C06P, ST03-ID_13,
  ST05-CF-4), 6 measurement/qualification platforms (F-06, C-22, C-05, D-09,
  G-03, ST03-ID_12), 3 reference designs (E-10, C-09, ST03-ID_08). 12+10+6+3=31.
  Matches the claim exactly; reproducible.
- **Winners and killed both present:** winners C-01/C-05/C-22/D-01/E-14/F-01/
  ST01-C10; killed/cut A-02, C-07, C-14, C-15, D-16, D-19, F-03, F-12, F-23,
  E-10 (canonical A-13), D-09 (OLD kill). Dispositions checked against opened
  B20 rows for C-07 (A30 DIS-C07: PL 119-21 45V deadline; Ingeteam INGECON H2
  <3% THD — verbatim in B20), E-10 (SEM-03 duplicate of A-13, killed by both
  baselines; BT-5 handoff note honored by PB-7), C-14 (A30 NON-MATCH-C14,
  elegance REJECT duplicate_of null), C-15 (SEM-04 duplicate of A-21). Faithful.
- **The 16 universe exclusions:** B20's ALIGNMENT.csv has exactly 39 rows;
  included 23 + excluded 16 (D-02, A-10, A-14, E-04, G-01, A-05, A-22, F-16,
  C-04, C-08, D-12, F-19, P5-USSCI2-S01, P5R2-CN-01, P5R2-CN-03, C-12) = 39
  reconciles exactly. "A-01" is genuinely absent from B20's universe, as stated.
  Sampled six exclusions against opened B20 rows: E-04 (cryogenic readout
  front-end — instrumentation, not power conversion), C-04 (two-phase
  thermal/fluids), C-12 (turbo-Brayton; B20 confirms decisive risk is
  gas-bearing rotordynamics), A-10 (phase-1 core is plasma metrology; its
  power-adjacent bias engine disclosed and the same-lane power idea F-01
  included instead), A-14 (instrumentation ICs), D-02 (measurand is tape
  Ic/defects). All defensible; no power-relevant idea wrongly excluded; the
  closest calls (A-10, E-04) are transparently reasoned in POWER.md §1.

### 3.3 Startup-corpus fidelity (gate 3) — PASS

Opened the actual records for 6+ of the 8 startup rows this run:

- **ST03-ID_08** (`50_INVENTIONS/ID_08_fastcoil_4q_ppm.md`, read in full):
  slot W-11 22/25 INVENT Pass 2 verbatim; alias-to-false-DC mechanism, PWM-locked
  clock domain + ripple-null apertures, RTP ~$19.3K / ~270 h / STRETCH $25-60K,
  >20 dB and <=20 ppm/8 h relative gates, U-014/U-015/U-033, Danfysik 9700
  2-100 Hz loop concession, ABB US10978948B2 fence, 4-prong wall test with
  counsel gate — all as carried. The row's caveat that the alias mechanism is
  asserted-by-record, undemonstrated, is correct (the record's own
  non-obviousness rests on planned locked-vs-free data). PB-4's $800
  nanocrystalline-toroid head is the record's own BOM line.
- **ST03-ID_10** (read §1-§7): W-12 20/25 INVENT rev 2; DTT FDU EUR 8M/1-year;
  ASIPP 2025 productized 100 kA QPS tender (U-024); U-023 latency-ownership gap;
  RTP ~$14.7K; >=1,000 trips / <=100 us clamp / >=50 dumps 0.1-0.4 kJ /
  interlock matrix / single-module kill; Lake Shore 625 / AMI 601+430 /
  Cryomagnetics 4G residue chart; NI pancake at 77 K; scale-up enablement
  flagged by the record itself — all faithful.
- **ST03-ID_12** (read §1-§7): W-17 20/25 INVENT rev 2; Element 1 L-aware
  bounded-deviation states; Element 2 dissimilar-physics divergence watchdog
  with the record's own phrase "a self-correcting chain can self-corrupt";
  honest metrology split (relative ppm vs referee DCCT; absolute 10-20 ppm via
  DMM+shunt) — exactly as POWER.md §6 quotes it; 8.5-digit DMM $7.5K BOM line;
  90-day campaign; CERN circulating-calibration practice — all faithful.
- **ST03-ID_13** (read lines 1-60, matching the worker's disclosed partial
  read): W-15 19/25 INVENT rev 2; U-017 Canis nine supplies + mechanical relay
  H-bridges as documented fault hazard; claim 5 (DCCT-class vs shunt-grade
  socket) and claim 6 (common-clock <=1 us timestamping) exist as cited;
  corrected Princeton/Thea patent reading present; 6-channel demonstrator +
  140 A dwell rig; BOM total indeed not visible in the read range — the row's
  "total not captured — disclosed" is accurate and its medium-low confidence
  appropriate.
- **ST01-C10 / ST01-C11 / ST01-C06P** (startup/01 exec summary lines 1-160;
  Round-2 showdown lines 1-80; DD_C10 targeted passages): C10 rank 2 at 76.8
  Medium; C06-pivot rank 3 at 74.8 (ABB SACE Infinitus + Siemens SENTRON 3QD2
  "ship today"; NVIDIA open-innovation layer; OCP/NVIDIA embed kill end-2027;
  ~$1.5-3M to v1; first revenue ~2031); C11-rescope rank 4 at 71.2 Med-Low,
  "a product line, not a company", sub-ms dump renounced with ITER 41 GJ /
  ~30 s / <=10 kV, detection the unsolved layer, ASIPP tender, <$150M/yr
  ceiling, ~$0.75-1.5M, 2 non-fusion LOIs by end-2027, detection-latency
  benchmark "cheapest validation experiment" — all verbatim-faithful. DD_C10
  confirms the row's record-cited figures word-for-word: $300-700K test
  infrastructure, NRTL/CE/EMC UL 61010 $150-300K and 6-9 months, "3-5 person
  company by first shipment, not solo", seed $2.5-4M / burn to A ~$3.5M, kill
  gates (all four), WTP question ("what premium for 12-week delivery"),
  WHAM/HSX <$15K reference deployment, no nuclear licensing, ECCN 3A226 with
  the record's own snippet-level caveat carried intact. V01 plasma-PSU "NO-GO
  standalone... no reachable merchant buyer pool" confirmed in the showdown
  (used by the C-14 row). DD_C10's "exceptional founder fit (power electronics
  x precision instrumentation...)" quote in POWER_SKILLS §3.6 is verbatim.
- **ST05-CF-4** (`70_DISCLOSURES/ID_04_cold_head_ramp_governor.md` in full;
  RND_STRATEGY greps): G-PHYS REVISE / G-NOVEL NARROW-NOVEL; alpha<1 estimator
  + per-cycle inversion; Jensen argument; 21.5% margin+lag probe SIMULATED/
  prophetic with exogenous headroom; the tautology caveat ("must NOT be cited
  as safety evidence") carried verbatim; Hall/field sensing deliberately
  excluded from the independent claim (funded-lane avoidance + FSU/NHMFL FTO);
  expired Sumitomo US6094333A / Toshiba JP2000012326A genus art; active
  FSU/NHMFL watch; NARROW-NOVEL provisional pending CN/JP/KR harvest;
  served-model caveat — all present in the record exactly as carried.
  "Strongest second bet" (line 49) and "Sub-$1.5K prototype validation (only
  after Phase 0 sims are fixed" (line 91) confirmed inside the disclosed
  RND_STRATEGY read range.

Audit-status carriage verified against B00 INVENTORY: startup/01 audited
(PASS-WITH-EXCEPTIONS), startup/03 unaudited (99_AUDIT contains no audit file),
startup/05 self-reported complete with no audit folder + gate-model-service gap
— each carried into the corresponding rows, RUN_META, and S-B25-12/13/14
limitations.

### 3.4 Required technical coverage (gate 4) — PASS

POWER.md §3 addresses all seven functions concretely with named host rows and
honest bandwidth bounds (EV27's ~50 MHz WBG need, Hall <~100 kHz, TMR filtered
<~50 kHz — verified verbatim against EV27/EV28); trip-grade sensing correctly
excluded to shunt/CT/Rogowski per P0048/P0056. §4 enumerates the full converter
stack including certification variants and states the ledger covers none of it;
EV30/EV31 adjudications verified against B15. §5 separates radiation
compensation, bandwidth fusion, and SET/SEB three ways and the ladder enforces
it (PB-7 sole radiation entry). §6 states and formally grounds mutual
consistency != absolute calibration (C23 Theorem 1 verified in PHD_FACTS;
EV32 gap row verified verbatim) and the rule is repeated inside PB-1/PB-2/PB-5
controls. §7 distinguishes the four role classes across all 31 rows. §9's W1/W2
wedges are reasoned from the rows (including counter-evidence: C-22's loss,
E-14's HIL boundary), list explicit non-wedges and honesty bounds, and make no
B40-style portfolio ranking.

### 3.5 Sensor-suffices prohibition (gate 5) — PASS

Scanned all seven artifacts. Explicit governing prohibitions in POWER.md §4 and
POWER_SKILLS preamble. Every converter/protection/PSU-class row's
missing_capabilities cell is non-empty and names the real stack gaps; every
phd_leverage cell for converter work is marked speculative/outside B10's
ledger. The startup corpus's contrary founder-capability assertions are
recorded and not adopted (§3.6). No cell, paragraph, or bridge test implies
sufficiency; PB-1's safety paragraph even flags elevated-bus bench practice as
a non-evidenced competence requiring supervision.

### 3.6 Founder-fit corrections (gate 6) — PASS

B20's five corrections verified in ALIGNMENT.md §9 (D01 §14/D-02; D04/D-10;
D02 §14/C-01; D03/C-05; D08 §14/A-10) and correctly carried in POWER_SKILLS §3
items 1-5. The NEW §3.6 correction is justified: FOUNDER_PROFILE_V3.md asserts
"finishing ~2029", "high-power-density power electronics", undergrad applied
superconductivity ("fully automated laser-aligned NI-HTS coil winding
machine"), battery-cell current imaging, full-stack breadth (opened, lines
4-12); DD_C10 asserts "exceptional founder fit" verbatim (line 102). B10's
accepted ground truth conflicts: C42 graduation target ~summer 2028, C49 zero
accepted first-author publications, and no power-conversion, cryogenic, or
battery-imaging hardware anywhere in C01-C50. Recording-without-adopting is
the correct treatment and is applied consistently in the ST01/ST03 rows.

### 3.7 BRIDGE_TESTS ladder (gate 7) — PASS with one minor defect

PB-1..PB-7 present and ranked with a stated criterion. PB-1, PB-2, PB-3, PB-4,
PB-5, PB-7 each contain all nine elements (measurements, controls, success,
kill, cost EST, safety, PhD value, startup value, ideas de-risked — the last
in both the summary table and per-entry text). PB-6 (desk audit) contains
measurements-equivalent method, success, kill, cost, safety, PhD value,
startup value, and de-risked ideas, but no explicitly labeled controls element
(minor defect 1). B15 linkages all resolve against GAPS.md §5: PB-1=BT-6
(closes G5/M6), PB-3 uses BT-1/FT-02 discipline, PB-5=BT-3/FT-05, PB-6=BT-8,
PB-7=BT-5/FT-11 (closes M1); FT-02/FT-05/FT-11 appear verbatim in B15's BT
entries. §8's deliberate non-entries (startup RTPs excluded as
capability-presuming builds) is consistent with the sensor-suffices rule.

### 3.8 Evidence-chain spot-checks (gate 8) — PASS

More than 10 rows checked across strata: winners C-01 (SEM-01 consolidation
verified in B20 header; D02 §14 correction; ST01-C06P triangulation), D-01,
F-06 (B20 row opened: old rank 23/NEW cut, medium boundary, BT-6-class
falsifier — all carried; old06 record confirms Southern Spirit +-525 kV,
NERC PRC-028 via NAES, LEM 12.5A-24kA ppm-class HVDC-targeted line, State
Grid/Xuji domestic-only tender), ST01-C10; killed C-07, E-10, C-14, C-15
(B20 rows opened — all kill facts faithful); startup rows per §3.3; boundary
G-03/F-02 via B20-attributed claims. Every sampled Cxx/EVxx/G-M-BT/A30
reference exists and supports the stated point. B10 status vocabulary
respected throughout (C06/C23/C31 consistently marked proposed/inferred/
pre-redteam; C03/C13/C46 demonstrated with their bounds; C04 gate honored —
PB-1 explicitly not gated by C04 only for commercial sensors, correct).
Record-vintage vs live separation consistently flagged.

### 3.9 Live source spot-checks (gate 9) — PASS

Opened this verification run:
- **Danfysik SYSTEM 9700** (S-B25-15): page states "ultra-high long-term
  stability of 10ppm", 0.75-100 kW, water/air-cooled, accelerator/magnet
  applications, and NO control-bandwidth/dynamics figures — matching the
  candidate's claim and its limitation note exactly (the slow-dynamics
  characterization is correctly attributed to the startup record, not the page).
- **FIA 2026 supply-chain report page** (S-B25-18): published 2026-06-23;
  $538M 2025 (+24%); $681M projected 2026 (+27%); power systems/components
  cited by 48%; 25 fusion companies + 67 suppliers. All recorded figures
  confirmed. One nuance: the page describes the 48% category as tied with
  fusion fuel-cycle systems for most-cited constraint; the candidate says
  "top-cited... at 48%" without the tie (minor defect 2 — literally true,
  incomplete).
- **HSI PRC-028-1 page** (S-B25-16): effective 2025-04-01; 50% by 2028-04-01;
  100% by 2030-01-01 for pre-existing BES IBRs — exactly as recorded, correctly
  labeled secondary with a re-verification instruction.
- **NERC official PDF**: my own fetch of a nerc.com PRC-028-1 PDF URL also
  returned HTTP 403, corroborating the honestly-recorded failure in
  RUN_META/S-B25-16.
Reuse notations verified: S-B25-01/02/03 marked `*_reused_open` with pilot
provenance; S-B25-19 reuse-by-reference of B20 opens correctly labeled.

### 3.10 Labels, model discipline, self-check, consistency (gate 10) — PASS

No pilot label in any candidate file (the only occurrence of the label string
is SELF_CHECK item 18 quoting it to assert its absence — not a label; the
pilot's own files carry it, confirming the convention). RUN_META names
`pap06-fable-xhigh`, requested Fable 5/xhigh (matches the card), observed model
recorded only as system-prompt self-identification and kept separate, observed
effort `NOT_EXPOSED` — correct MODEL_POLICY discipline; treated here as missing
observation, not mismatch. SELF_CHECK recounts all reproduced (31 rows;
12/10/6/3; 19 source rows; 4 new opens; 16 exclusions; disclosed shortfalls
match RUN_META). Cross-artifact consistency: W1/W2 identical across POWER.md
§9, POWER_SKILLS §4f/§5, and BRIDGE_TESTS; every PB-x cited in POWER_MAP cells
exists; every S-B25-xx cited exists in SOURCES.csv; disposition cells are
per-idea handling, not a B40 ranking. Candidate wrote exactly the seven target
files; immutable areas show no sign of modification.

## 4. Defects

1. **Minor — BRIDGE_TESTS.md PB-6 / SELF_CHECK.md item 15.** PB-6 (desk audit)
   has no explicitly labeled controls element, so SELF_CHECK's "every entry
   contains all nine required elements" is slightly overstated for that entry.
   Substance is present (match/mismatch recording, strike rule, honest-failure
   rule) and a desk audit has no natural control condition; no conclusion is
   affected. Acceptance test: PB-6 either gains an explicit controls line
   (e.g., dual-sourcing/independent re-derivation of traced figures) or
   SELF_CHECK item 15 is qualified for desk-only entries.
2. **Minor — SOURCES.csv S-B25-18 / POWER_MAP ST01-C10 application cell.** The
   FIA page reports power systems/components tied with fusion fuel-cycle
   systems as the most-cited bottleneck at 48%; the candidate's "top-cited
   bottleneck at 48%" is literally true but omits the tie. No count, wedge, or
   disposition depends on the margin. Acceptance test: note the tie wherever
   the 48% figure is characterized as "top".

No critical or major defects.

## 5. Limitations of this verification

- B20-universe rows other than F-06 were verified against B20's accepted rows
  (a sample of 10 opened in full), not by re-opening the underlying old06/new06
  corpus files — mirroring the accepted-prerequisite structure the task card
  permits the worker; the worker disclosed the same limitation per row.
- Startup/01 deep dives DD_C11 and DD-C06 were not opened (by the worker or by
  me); both rows rest on the audited executive summary, disclosed, with
  confidences reduced accordingly — verified as appropriately handled rather
  than independently re-derived.
- IEC 62477-1 (S-B25-01) and the NVIDIA blog (S-B25-03) are pilot reused opens;
  I did not re-open them. Their content as carried matches the pilot-accepted
  records and scope-level-only limitations are intact.
- The FIA underlying report PDF and the full IEC standard text were not opened
  by anyone; both are flagged as such in the candidate.
- ID_12 was read to §7 and ID_10 to §7 this run; their §8-§11 (wall/counsel
  sections) were not re-read, so counsel-question attributions in those rows
  (e.g., 112(f)/divided infringement) were checked only for plausibility
  against the read portions and ID_08's parallel structure.
- Observed model/effort for the worker and for this verifier rest on
  self-identification and `NOT_EXPOSED` respectively; per MODEL_POLICY these
  are neither mismatches nor proof.

VERDICT: PASS
