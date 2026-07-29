# SELF_CHECK — B25_power PILOT attempt-1

**PILOT SAMPLE — NOT FINAL**

Checklist against the task card, stage specification, and global policies.
Verdicts: PASS / PASS-WITH-DISCLOSURE / FAIL.

| # | Requirement | Verdict | Evidence |
|---|---|---|---|
| 1 | Exactly FOUR distinct architectures with stable idea IDs | PASS | POWER_MAP.csv: P3R2-C-01, P3R2-C-13, P3R2-F-06, P3R2-E-10 (4 rows, IDs verbatim from the A30/B20 universe) |
| 2 | Rows span >=2 roles among full end product / subsystem / measurement-qualification tool / reference design | PASS | All FOUR roles covered, one per row (exceeds the >=2 minimum) |
| 3 | Full 13-column set exercised per row (idea_id,role,application,phd_leverage,missing_capabilities,buyer,proof_experiment,safety_certification,capital,moat,confidence,falsifier,disposition) | PASS | Every cell populated with substantive content in all 4 rows; header matches the task card's column list exactly, in order |
| 4 | POWER.md: Hall/coil sensing entry analyzed concretely (ripple, transients, current sharing, ramp/dump, protection, fault localization, calibration) per architecture | PASS | POWER.md §2 covers all seven functions for each of the four architectures, with honest bandwidth bounds (EV27/EV28) and per-architecture non-applicability stated (e.g. no ramp/dump native to C-01) |
| 5 | POWER.md: converter-stack realities enumerated AND which the PhD does NOT cover | PASS | §3: full stack list (topology, gate drive, WBG, magnetics, insulation, EMI/EMC, thermal, controls, HIL, safety/cert, manufacturing, reliability, service, supply chain) with the explicit finding that B10's ledger covers none of it |
| 6 | Radiation compensation vs bandwidth fusion treated as SEPARATE problems | PASS | POWER.md §4 (three-way separation incl. SET/SEB as a third distinct problem); BRIDGE_TESTS.md §2 keeps PB-1 strictly on the bandwidth/EMI side |
| 7 | Traceability/uncertainty discipline: mutual Hall/coil consistency ≠ absolute calibration | PASS | POWER.md §5 (C23 Theorem-1, C07, EV32, EV04) with the power-domain consequence stated; BRIDGE_TESTS.md controls repeat the rule inside the experiment design |
| 8 | Full end products vs measurement/qualification/reference platforms distinguished | PASS | POWER.md §6 (structural comparison across the four roles); reflected in every disposition cell |
| 9 | Preliminary preferred-wedge judgment present and labeled preliminary | PASS | POWER.md §7 — measurement/qualification layer wedge, with honesty bounds (rides on proposed C06; F-06 commercial evidence weak) and full-run retest condition |
| 10 | POWER_SKILLS.md: present vs missing skills grounded in B10's demonstrated-vs-proposed ledger and B20's five founder-fit corrections; acquisition paths (time/cost/route) | PASS | §1 (demonstrated with bounds incl. C50 provenance), §2 (proposed-only with gates), §3 (all five B20 corrections applied), §4-5 (per-architecture acquisition paths, EST-labeled) |
| 11 | NEVER imply magnetic-sensor expertise alone suffices to design or certify a converter | PASS | Explicit governing-rule statements in POWER.md §3 and POWER_SKILLS.md preamble; every row's missing_capabilities names the converter-stack gaps; no cell or paragraph implies sufficiency |
| 12 | ONE bridge experiment in full form (measurand+measurements, controls, success criteria, kill criteria, cost range, safety, PhD value, startup value) | PASS | BRIDGE_TESTS.md §1 (PB-1, BT-6-based, all eight elements present); B15 BT-6 cited as the basis with the extension (traceable reference chain) justified |
| 13 | Bridge experiment builds on B15's ranked BT-1..BT-6 where applicable (cite) | PASS | PB-1 = BT-6 (closes G5/M6), cited to GAPS.md §5; BT-5 and BT-8 preserved as undeveloped pointers per B20's handoff and B15's hygiene rule |
| 14 | SOURCES.csv schema exact (claim_id,url,title,publisher,published_date,accessed_date,source_type,stage_file,confidence,limitation) | PASS | Header matches exactly; 11 rows; honest access notes per row |
| 15 | B15 paper IDs used for literature claims; at least one NEW live open for a load-bearing current claim | PASS | S-B25-04..07 route literature through EV rows + paper IDs without restating unverified metadata; THREE live opens (S-B25-01 standard scope page, S-B25-02 manufacturer spec, S-B25-03 vendor architecture blog) |
| 16 | Claims mapped: every material claim carries Cxx / EVxx / Pxxxx / G-M-BT / S-B25-xx / S-B20-xx / corpus-path anchors | PASS | Applied throughout all five stage files; corpus-dated facts flagged as record-vintage |
| 17 | Every artifact labeled "PILOT SAMPLE — NOT FINAL" | PASS | Label present at top of POWER_MAP.csv (line 1 comment), POWER.md, POWER_SKILLS.md, BRIDGE_TESTS.md, SOURCES.csv (line 1 comment), RUN_META.md, SELF_CHECK.md |
| 18 | Write nothing outside pilot/B25_power/attempt-1/ | PASS | Seven files written, all inside the target; no other file touched or modified |
| 19 | No fabrication (specs, standards numbers, market facts, capabilities, citations, model identity) | PASS-WITH-DISCLOSURE | IEC 62477-1 scope verified live at abstract level (not full text); Danisense snippet figures for models other than DQ500ID deliberately NOT reused; EV07/EV08 headline numbers not reused as facts (BT-8 unperformed); all costs labeled EST; no DOI/title metadata invented for B15 papers |
| 20 | Sensor-role honesty inside architectures (trip-grade sensing not claimed for Hall) | PASS | POWER.md §2 bandwidth reality paragraph; C-01/C-13 rows route edge/trip fidelity to shunt/CT/Rogowski class per EV27/P0048/P0056 |
| 21 | RUN_META.md complete (agent, model/effort requested vs observed, times, sources, web activity, limitations, exposure status) | PASS | All fields present; observed effort NOT_EXPOSED; model self-identification separated from requested-model evidence; failed fetches (2x HTTP 403, 1 non-render) disclosed |
| 22 | Pilot-before-full ordering and target conventions respected | PASS | This is the pilot, attempt-1, in `pilot/B25_power/attempt-1/`; full run not attempted |

## Disclosed shortfalls (none load-bearing, none hidden)

1. Two standard-page mirrors (IECEE, ANSI webstore) returned HTTP 403 and
   one (iTeh) did not render scope text; mitigated by the successful IEC
   webstore live open (S-B25-01). No FAIL: the load-bearing claim is
   sourced.
2. The F-06 corpus record was read to line 80 only (its demand, competitor,
   and price sections); the remainder was not read. The row relies on B20's
   full-row adjudication for anything beyond those sections.
3. C-13 and C-01 rows rely on B20's accepted row-level reads of the
   underlying deep dives rather than fresh re-opens — permitted use of an
   accepted prerequisite, disclosed in RUN_META.
4. Runtime effort not exposed; recorded as NOT_EXPOSED per convention.
5. The preferred-wedge judgment covers only the 4 pilot architectures; it
   binds nothing downstream until the full >=18-idea run retests it.
