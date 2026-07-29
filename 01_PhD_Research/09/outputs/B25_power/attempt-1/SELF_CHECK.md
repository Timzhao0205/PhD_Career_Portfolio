# SELF_CHECK — B25_power FULL attempt-1

Checklist against the task card, stage specification, and global policies.
Verdicts: PASS / PASS-WITH-DISCLOSURE / FAIL.

| # | Requirement | Verdict | Evidence |
|---|---|---|---|
| 1 | AT LEAST 18 distinct power-relevant ideas with stable IDs as recorded | PASS | POWER_MAP.csv has 31 rows, all unique: 23 P3R2-* IDs verbatim from the A30/B20 universe + 8 startup IDs (ST01-C10/C11/C06P; ST03-ID_08/ID_10/ID_12/ID_13; ST05-CF-4 — corpus prefix + recorded ID verbatim, convention stated in POWER.md §1) |
| 2 | Full 13-column set, exact header, one row per idea | PASS | Header matches the task card's column list exactly, in order, as line 1; every cell in all 31 rows populated with substantive content; no newlines inside cells; comma-bearing cells quoted |
| 3 | All roles represented (products, subsystems, measurement tools, qualification platforms, reference designs) | PASS | 12 full end products, 10 subsystems, 6 measurement/qualification platforms, 3 reference-design/platform rows (counts reconciled in POWER.md §2) |
| 4 | Winners AND killed/cut ideas included | PASS | Winners: C-01 (top consensus), C-05, C-22, D-01, E-14, F-01, ST01-C10. Killed/cut: A-02, C-07 (A30-verified kill), C-14, C-15, D-16, D-19, F-03, F-12, F-23, E-10 (killed canonical), D-09 (OLD kill, NEW revival), CF-5 documented as killed in the sweep account |
| 5 | Startup-corpus serious power-adjacent directions included with record support and recorded IDs | PASS | 8 startup rows spanning startup/01 (audited synthesis), startup/03 (C10 deep dive + 4 red-teamed invention disclosures), startup/05 (CF-4/ID_04); audit status per B00 carried into every row; considered-not-rowed candidates listed with reasons (POWER.md §1) |
| 6 | Inclusion boundary stated; no padding with non-power ideas | PASS-WITH-DISCLOSURE | Boundary stated up front (POWER.md §1) with 4 labeled boundary cases (C-05, D-09, D-10, D-19 — the task card itself names C-05/D-10 in the sweep list); 16 excluded ideas listed with reasons; "A-01" verified absent from B20's universe and said so |
| 7 | Hall/coil sensing concrete across ripple, transients, current sharing, ramp/dump, protection, fault localization, calibration | PASS | POWER.md §3 covers all seven functions across the full set, with honest bandwidth bounds (EV27/EV28) and the trip-path exclusion; ramp/dump now has native hosts (F-02, ST03-ID_10, F-06 magnet leg, CF-4 noted as non-magnetic by design) |
| 8 | Converter-stack reality check; what the PhD does NOT cover | PASS | POWER.md §4: full stack enumerated incl. certification variants (IEC 62477-1 / NRTL / marine class / space), with the explicit finding that B10's ledger covers none of it in any of the 31 rows |
| 9 | Radiation compensation vs bandwidth fusion as separate problems | PASS | POWER.md §5 three-way separation (adding SET/SEB, now covering E-10 AND D-16); BRIDGE_TESTS.md §8 enforces it at ladder level (PB-7 is the only radiation entry) |
| 10 | Traceability discipline: mutual consistency is not absolute calibration | PASS | POWER.md §6 (C23 Theorem-1, C07, EV32, EV04) with the power-domain consequence, extended by the ST03-ID_12 divergence-watchdog convergence and ST05-CF-4's design-around note; PB-1/PB-2 controls repeat the rule inside the experiment designs |
| 11 | End products vs measurement/qualification/reference platforms distinguished | PASS | POWER.md §7 across all 31 rows by role class; reflected in every disposition cell |
| 12 | PREFERRED WEDGES with reasoning, plural if genuine; pilot's F-06-class wedge tested against the full set | PASS | POWER.md §9: pilot wedge retested against C-05/C-22/G-03/E-14-HIL/D-09 and the startup corpus; resolves into TWO wedges (W1 DC-asset qualification authority; W2 magnet-power measurement-chain/detection authority) with reasoning, counter-evidence (C-22's loss, E-14's line), explicit non-wedges, and honesty bounds; no portfolio ranking made |
| 13 | POWER_SKILLS grounded in B10 demonstrated-vs-proposed and B20's five founder-fit corrections, with acquisition paths (time/cost/route) | PASS | POWER_SKILLS.md §1-§2 (B10 only), §3 (all five corrections applied + a sixth documented divergence: startup founder-profile assertions recorded, NOT adopted), §4 (six skill families with HIRE/PARTNER/TRAIN/BUY/COLLABORATE routes, EST or record-cited figures), §5 summary |
| 14 | Never imply sensor expertise suffices for converter design/certification | PASS | Governing-rule statements in POWER.md §4 and POWER_SKILLS.md preamble; every product row's missing_capabilities names converter-stack gaps; the startup corpus's contrary founder-fit assertions explicitly not adopted (§3.6); no cell or paragraph implies sufficiency |
| 15 | BRIDGE_TESTS: RANKED ladder, multiple experiments, PB-1 carried; each with measurand/measurements, controls, success criteria, kill criteria, cost range, safety, PhD value, startup value, ideas de-risked | PASS | Seven ranked entries (PB-1 carried in full; PB-2 through PB-6 new; PB-7 developed from the carried BT-5 pointer); every entry contains all nine required elements; ranking criterion stated; B15 BT linkages cited (BT-6, BT-3/FT-05, BT-8, BT-5); §8 records deliberate non-entries |
| 16 | Bridge tests build on B15's BT-1..BT-6 where applicable | PASS | PB-1=BT-6 extended; PB-5=BT-3/FT-05; PB-6=BT-8; PB-7=BT-5/FT-11; PB-3 uses BT-1/FT-02 honesty discipline; cited to GAPS.md §5 throughout |
| 17 | SOURCES.csv schema exact; B15 paper IDs for literature claims; pilot opens carried with reuse noted; >=3 NEW live opens; honest failures | PASS | Header matches exactly; 19 rows; literature routed through EV rows + paper IDs without restating unverified metadata (S-B25-04..07); pilot opens S-B25-01/02/03 marked `*_reused_open` with reuse noted; FOUR new live opens (S-B25-15/16/17/18); NERC 403 failure disclosed in S-B25-16 and RUN_META |
| 18 | NO pilot labels anywhere | PASS | No file carries "PILOT SAMPLE — NOT FINAL", a PILOT mode header, or any pilot marking; the accepted pilot run is referenced only as provenance where the task card requires carry/refinement disclosure (POWER.md §1; BRIDGE_TESTS PB-1) — disclosure of origin, not a label on these artifacts |
| 19 | Claims mapped (Cxx / EVxx / Pxxxx / G-M-BT / A30:* / S-B25-xx / S-B20-xx / corpus paths); record-vintage vs live separated | PASS | Applied throughout all five stage files; corpus-dated facts flagged record-vintage; live opens dated; startup records' own caveats (tautology, served-model, snippet-level ECCN) carried verbatim where their content is reused |
| 20 | No fabrication (specs, standards, market facts, capabilities, citations, model identity) | PASS-WITH-DISCLOSURE | Standards cited only at scope/record level (no invented standard numbers — rows where records name none say so); patent/NPL chartings attributed to the startup records, not asserted as verified; EV07/EV08 headline figures not reused (BT-8 open, PB-6); all costs EST or record-cited; founder capabilities limited to B10's ledger; model identity recorded as self-identification only |
| 21 | Per-idea record-read list in RUN_META | PASS | RUN_META.md lists the record basis for every one of the 31 ideas, incl. partial reads (ID_13 lines 1-60; RND_STRATEGY 1-120; exec summary 1-160; showdown 1-80) and not-opened records (DD_C11, DD-C06) |
| 22 | RUN_META complete (agent, requested vs observed model/effort, times, sources, web activity, limitations, exposure status) | PASS | All fields present; observed effort NOT_EXPOSED; observed model = system-prompt self-identification, separated; 3 searches + 5 fetch attempts (4 opened, 1 HTTP 403) itemized |
| 23 | Write nothing outside outputs/B25_power/attempt-1/ | PASS | Seven files written, all inside the target; no other file created or modified |
| 24 | No portfolio ranking (disposition is not a B40 rank) | PASS | Stated in POWER_MAP usage, POWER.md preamble and §9; disposition cells give per-idea handling, not ranks |
| 25 | Internal consistency | PASS | Role counts (12/10/6/3=31) reconciled between CSV and POWER.md §2; wedge families in §8/§9 match disposition cells; PB references in CSV cells all exist in BRIDGE_TESTS.md; S-B25-xx references all exist in SOURCES.csv |

## Disclosed shortfalls (none hidden; none judged load-bearing)

1. B20-universe rows other than F-06 rest on B20's accepted row-level
   record reads rather than fresh re-opens of the underlying corpus files
   — permitted by the task card ("judge relevance yourself from B20's
   map") and disclosed per row in RUN_META.
2. ST01-C11 and ST01-C06P rows rest on the audited startup/01 executive
   summary; their underlying deep dives (DD_C11, DD-C06) were not opened.
   Row confidences reflect this.
3. ST03-ID_13 was read to line 60 only; its row is the map's
   lowest-confidence startup entry and says so.
4. The official NERC PRC-028-1 PDF returned HTTP 403; compliance dates
   rest on a secondary page (S-B25-16) consistent with the old06 record's
   NAES citation — flagged for re-verification before any reliance beyond
   demand context.
5. The Pattern Energy page (S-B25-17) confirms the 2029/2032 targets but
   its status narrative appears frozen at ~2023; treated as the
   developer's stated plan, not current construction status.
6. BT-8 primary tracing remains unperformed (PB-6 carries it); no
   conclusion in this stage depends on the untraced figures.
7. CF-7 (current-lead co-qualification) was identified as a possible
   additional power-adjacent startup row but not rowed because its
   disclosure was not read this run — documented in POWER.md §1 rather
   than silently dropped.
8. Runtime effort not exposed; recorded as NOT_EXPOSED per convention.
