# Independent verification — B30_skills FULL attempt-1

- Verifier: `pap06-verifier` (fresh, independent; did not produce the candidate)
- Requested verifier model/effort: Fable 5 / xhigh. Observed model: the runtime
  system prompt self-identifies as `claude-fable-5` (system-prompt
  self-identification, not independent telemetry). Observed effort: NOT_EXPOSED.
- Candidate: `outputs/B30_skills/attempt-1/` (read-only; nothing edited)
- Verification card: `state/CURRENT_VERIFY.md`; stage spec
  `workflow/stages/B30_skills.md`; acceptance rules
  `.claude/skills/pap06-native/references/ACCEPTANCE.md`; `MODEL_POLICY.md`
- Ground truth opened this run: `outputs/B10_phd/attempt-1/PHD_FACTS.json`
  (all 50 claims, both pages) and `OPT2.md` (full);
  `outputs/B20_align/attempt-1/ALIGNMENT.md` (§6-§11) and `ALIGNMENT.csv`
  (A-14 and E-04 rows); `outputs/B25_power/attempt-1/POWER_SKILLS.md` (full),
  `BRIDGE_TESTS.md` (ladder summary + PB-1/PB-2/PB-3/PB-4/PB-5 sections),
  `POWER.md` §9 region; `outputs/B15_lit_synth/attempt-1/GAPS.md` §5-§6,
  `LIT_REVIEW.md` and `EVIDENCE_MAP.csv` spot rows (EV06, EV23),
  `SOURCES.csv` spot row; `pilot/B30_skills/attempt-1/` (SKILLS.csv full,
  BRIDGES.json BR-A/BR-B full, SKILLS.md §6); `workflow/ROUTE.json` (B30 entry).

## Check 1 — Files, structure, JSON/CSV validity

- All six files present and non-empty: SKILLS.csv, SKILLS.md, BRIDGES.json,
  PREP_PLAN.md, RUN_META.md, SELF_CHECK.md. ROUTE.json's four required
  filenames for B30 all present. PASS.
- SKILLS.csv header row is exactly the 12 stage-spec columns in order
  (`skill,category,current_level,evidence,target_level,needed_for,
  acquisition_path,validation_artifact,time,cost,priority,owner`); every data
  row parses to 12 fields (comma-bearing cells quoted; spot-parsed S1, S2,
  S3, S4, S8, S20 field-by-field). One preamble comment line precedes the
  header — same convention as the accepted pilot, disclosed in SELF_CHECK
  item 3 (minor observation, see defect 1). PASS.
- BRIDGES.json: read in full (372 lines); well-formed JSON structure
  (balanced, quoted keys, single top-level object with `bridges` array of 9).
  PASS.

## Check 2 — Recounts

- Rows: 20 data rows, S1..S20 in file order, unique. My independent recount
  of `current_level` values: current_demonstrated = 5 (S1, S6, S13, S15,
  S16); literature_backed_near_transfer = 7 (S2, S5, S7, S10, S11, S12,
  S14); missing = 3 (S3, S8, S9); collaborator_or_vendor = 5 (S4, S17, S18,
  S19, S20). Matches the claimed 5/7/3/5 and SKILLS.md §4 exactly.
- Only the four controlled tokens appear in the current_level column. PASS.

## Check 3 — SKILL-INFLATION AUDIT (critical)

Every cited B10 claim for all five current_demonstrated rows was opened in
PHD_FACTS.json and its status and bounds compared to the row:

| Row | Cited B10 claims | B10 status | Scope-bound fidelity | Verdict |
|---|---|---|---|---|
| S1 (Hall readout/EMI bench) | C03, C13, C01 (+C04, C15 as bounds) | C03/C13/C01 all `demonstrated` | Emulator-only bound stated verbatim ("resistor-ring EMULATOR, not the real die"); C01 qualitative/voltage-domain bound stated; open C04 anomaly and C15 aspirational-calibration flag carried in-cell | NO INFLATION |
| S6 (UHV packaging/deployment) | C46, C01 (+C14, C45, C19, B20 A-14 as bounds) | C46/C01 `demonstrated` | Single-execution bound stated; multi-die cube reuse correctly labeled proposed (C14) with bond-pad-yield risk (C46 limitation); C45 module-location unknown carried; "150C bake is not 300C qualification" verified against B20 ALIGNMENT.csv A-14 row ("a demonstrated 150C bake is not a 300C/1000h qualification") | NO INFLATION |
| S13 (manuscript writing) | C02, C21, C22, C49 (+C44, C35) | All `demonstrated` | "Submission grade ONLY" bound explicit; zero accepted first-author (C49) stated; revision-to-acceptance never completed stated; C44 wording prohibitions carried | NO INFLATION |
| S15 (AI-mission direction) | C16, C17, C50 (+C40) | All `demonstrated` | C50's direction-vs-research-labor distinction carried verbatim ("NOT the underlying research labor"); folder-08 10/12-stage audit gap (C40) stated as the unevenly-exercised part | NO INFLATION |
| S16 (collaboration practice) | C01 (+C28) | C01 `demonstrated` | "Demonstrated NARROWLY" within the established HSX collaboration; initiating new engagements explicitly NOT demonstrated, matching C28's limitation ("No outreach, contact, or collaboration has actually occurred"); vocabulary-edge judgment disclosed in SELF_CHECK item 4 | NO INFLATION |

Nothing proposed/inferred/unknown is promoted: C06 (proposed), C10
(proposed), C14 (proposed), C23 (inferred), C05/C15/C45/C29/C30 (unknown)
are all used only on non-demonstrated rows or as bounds.

Spot-checks across the other three levels (7 rows, exceeding the required 5):

- **S2** (lbnt): opens "NOT demonstrated"; C06 proposed-only and C15
  no-calibration-exists both verified; ~19-29 bench-days / zero-cleanroom
  figure verified in C06's limitation ("stage-70 corrected sum"); correction
  4 applied. Faithful.
- **S3** (missing): POWER_SKILLS §1 verified verbatim ("no converter,
  gate-drive, magnetics, HV, protection... entry of any kind — for any of
  the 31 rows"); PB-1's safety note verified verbatim in BRIDGE_TESTS.md;
  §4(a) "EST 1-2 years dedicated practice" verified; corrections 3 and 6
  applied. Faithful.
- **S5** (lbnt): C10 "specification, not a deliverable" verified; C23
  inferred/pre-redteam (C40) and C50 provenance caveats carried; correction
  5 applied. Faithful.
- **S7** (lbnt): C14 "no hardware, code, CAD" verified; correction 1
  (array/DAQ not demonstrated) verified in ALIGNMENT.md; P0024 field-evidence
  refusal present. Faithful.
- **S9** (missing): no cryogenic entry anywhere in C01-C50 (confirmed by my
  full read); §4(e) months-scale EST verified; correction 6 refusal of the
  startup-corpus HTS assertions verified in POWER_SKILLS §3.6. Faithful.
- **S12** (lbnt): C05 status `unknown` with Reviewer-1 dispute verified;
  C08/C23 Case-9 near-DC-cannot-verify-bandwidth verified in OPT2.md.
  Faithful.
- **S19** (collaborator_or_vendor): C09 collaborator-led/never-critical-path/
  never-first-author verified; C29 ~14x cross-species failure and C30
  single-source witness dependency verified. Justified.

Also checked S8 (missing — no thermal/optical entry exists in B10; lock-in
thermography named non-demonstrated in ALIGNMENT.md §6), S14 (lbnt — C33/C34
demonstrated as artifacts, correctly NOT converted into a demonstrated
personal skill; M13 not_started verified), S17 (C19's FAIL/HOLD + 8 BLOCKER
verified), S4 (§4(b)-(c) figures verified: 2-4 senior engineers/12-24
months/multi-$M; $150-300K and 6-9 months NRTL).

Six corrections: the binding table in SKILLS.md §1 matches ALIGNMENT.md §9's
five (D-02, D-10, C-01, C-05, A-10) plus POWER_SKILLS §3.6 exactly; bindings
verified on S7/S8 (corr. 1), S3/S4 (corr. 3), S2/S10 (corr. 4), S5/S11
(corr. 5), S9/S20 (corr. 6/2) — more than the required 3.

**Inflation-audit verdict: CLEAN. No skill inflation found.**

## Check 4 — Family coverage vs B25 §4

POWER_SKILLS §4 families (a)-(f) all mapped in SKILLS.md §3:
(a) converter design core → S3 (front-slice TRAIN)/S4; (b) protection/
interruption → S4; (c) certification → S4 + BR-F; (d) field commissioning →
S18; (e) application-domain (electrochemistry, laser/photonics, plasma/RF,
space power, cryo/HTS, rotating machines) → S9/S19/S20 incl. retire calls;
(f) precision metrology at acceptance grade → S2/S10 (+S1). §1 present
families → S1/S12, S6, S15; §2 conversions → S2/S10, S5/S11. All 20 rows
appear in the mapping; no needed family lacks a row. PASS.

## Check 5 — BRIDGES.json

- 9 entries, IDs BR-A..BR-I, ranks 1-9 unique (file order BR-A, BR-B, BR-C,
  BR-D, BR-E, BR-G, BR-F, BR-H, BR-I).
- 19 required fields enumerated (id, rank, name, lineage, rank_rationale,
  hypothesis, protocol, metrics, controls, success_gate, kill_gate,
  dependencies, time, cost_range, safety, phd_value, startup_value,
  dual_use_rationale, stop_continue_gate): my grep of exactly these key
  patterns returns 171 = 9 × 19 matches, and all 19 were visually confirmed
  in every entry during the full read. PASS.
- **Lineage recount.** B15 GAPS.md §5 defines EIGHT bridge tests, BT-1..BT-8
  (independently counted this run) — the task card's "BT-1..BT-6" was indeed
  short, and the candidate's disclosed extension is correct (the accepted
  pilot's own §6 scope list already required "all eight BT-x placed").
  Home assignments, each ID exactly once, no orphans, semantically verified
  against the BT/PB definitions:

  | ID | Home | Content match |
  |---|---|---|
  | BT-1 (FT-02 honesty test) | BR-A | yes (Phase 0) |
  | BT-2 (real-data replay) | BR-C | yes |
  | BT-3 (coil-referenced gain recovery) | BR-A | yes (Phase 1) |
  | BT-4 (traceable tesla-scale calibration) | BR-D | yes |
  | BT-5 (species-correct irradiation) | BR-H | yes |
  | BT-6 (Hall-vs-TMR under switching EMI) | BR-B | yes |
  | BT-7 (NI-coil quench redistribution) | BR-I | yes |
  | BT-8 (headline-figure primary tracing) | BR-F | yes |
  | PB-1, PB-2 | BR-B | yes (benchmark + dossier) |
  | PB-3 | BR-G | yes |
  | PB-4 | BR-E | yes |
  | PB-5 | BR-A | yes (Phase 1) |
  | PB-6 | BR-F | yes |
  | PB-7 | BR-H | yes |

  FT-02/04/05/08-09/11/12 also mapped; FT-01 deliberately a precondition in
  publication-facing gates, disclosed in the note — acceptable.
- **Pilot fidelity.** BR-A and BR-B compared field-by-field against
  `pilot/B30_skills/attempt-1/BRIDGES.json`: hypotheses, protocols, metrics,
  controls, success/kill gates carried essentially verbatim. Diffs are
  exactly the disclosed ones (BT-8 pointer discharged to BR-F; pilot's
  "both bridges'" generalized to "every other entry's"; BR-C/BR-G named in
  BR-A's gates; startup-stop consequences added; P2-content line added).
  Substance preserved. PASS.
- **Ranking.** The summary rationale addresses all eight stage-spec criteria
  (information gain, reusability, time, cost, safety, publication value,
  commercial evidence, dependency); BR-A's entry-level rationale enumerates
  all eight explicitly. Ordering is coherent: $0 dependency-free desk gate
  first; BR-C ($0) below BR-B with the dependency/commercial-evidence reason
  stated; BR-D's rank-by-dependency and BR-F's rank-7-despite-$0 (calendar
  compensation, matching B25's own PB-6 placement) both explained;
  deviations from source orderings disclosed rather than smoothed. PASS.
- **Carried figures spot-verified** (risk-stratified): PB-1 safety note
  (verbatim), PB-4's ~$800 BOM line and >20 dB gate, PB-3's cost/time,
  EV06/EV23's ≤9 mV / >100 mV figures (LIT_REVIEW.md 173-176, EVIDENCE_MAP
  EV06/EV23), BR-I's 70 vs ~27 µΩ·cm² and P0043 ≥350 A / 4.2 K (GAPS.md
  61, 91), BR-D's u(k)/k ≤ 2% / ±~2% / <0.5% targets (OPT2.md Element-1
  hypothesis, C06). All genuine record figures; none invented.

## Check 6 — PREP_PLAN.md

- Gate summary table independently recounted: 14 named gates (G-BR-A-0,
  G-30/C04, G-30/BR-F, G-90/C04, G-90/S3, G-90/chain, G-90/M13, G-BR-B-mid,
  G-BR-A-1, G-BR-C, G-BR-D/FT-04, G-365/W1, G-365/W2, G-365/G5) — matches
  the claim. Every horizon has explicit stop/continue gates (G-30: 3;
  G-90: 4; G-180: 5 bullets; G-365: 4).
- PhD critical path verified against B10 records: P1 publication lane
  (C02/C22 decline-with-invite, C22's itemized asks, C35 Route A then C,
  C44 wording rules) staged across horizons; C04 as a day-0 block matching
  B10's own "no calibration work before closure" rule; G5 at ~month 12
  requiring ≥1 accepted/in-revision first-author paper AND real-die absolute
  calibration (C38, confirmed in OPT2.md kill criteria); C45 first-30-days
  module location (the corpus's next-72-hours item); campaign #2 Nov 2026
  (C14); C32's ~3-6 marginal bench-days and piggyback-only rule; M13
  not_started (C34). All accurate.
- Startup-preparation stop points are stated separately from PhD stops at
  every horizon and in the closing paragraph. PASS.
- Budget arithmetic: numeric low ends 0+1+8+3+0+1+2 = 15; high ends
  5+25+10+4+8 = 52 → "~$15-52K plus unsized low-$K items" is consistent;
  BR-D honestly "not estimable in dollars" (C06 gives bench-days only);
  borrow-branch reduction (up to $5-15K) consistent with BR-B's breakdown.
- No startup-idea ranking anywhere in the four artifacts (wedges appear as
  families with upgrade/kill conditions; customer-conversation option
  explicitly "a B40 decision"). PASS.

## Check 7 — Honesty and consistency

- "Not estimable" used where records give no figure — verified instances:
  S1 C04-closure time, S8 time and cost, S9 cost, S18 time, S19 time, BR-D
  cost_range, BR-H/BR-I time (≥2 required; 8 found). No invented numbers
  found anywhere; every cost/time carries an EST label with a record source.
- No literature-prevalence-as-skill reasoning: §8 anti-inference guard plus
  per-row refusals (P0008/S2, P0003/S5, P0024/S7, EV05-EV21/S9, C50/S15)
  all honored in the level assignments.
- No pilot labels in any of the six files (all references to the pilot are
  provenance statements, not banners). PASS.
- NOT_EXPOSED discipline: RUN_META separates requested (Fable 5 / xhigh,
  agent `pap06-fable-xhigh` — matches CURRENT_VERIFY and ROUTE.json) from
  observed (model: system-prompt self-identification, labeled as such;
  effort: NOT_EXPOSED). Treated here as honest recording; missing
  observation is neither mismatch nor proof. PASS.
- SELF_CHECK recounts reproduced independently: 20 rows, 5/7/3/5, 171
  field-instances, 14 gates, lineage map — all match my counts.
- Cross-artifact consistency: S-row references in SKILLS.md §3/§7 and
  PREP_PLAN resolve to the correct CSV rows; BR references resolve; S3↔BR-B
  pre-flight = G-90/S3; S2's C04/C45 gating identical across CSV, BR-D, and
  PREP_PLAN §0; BT-8 ownership consistent across BR-B lineage, BR-F, and
  SKILLS.md §9; level distribution identical in CSV and SKILLS.md §4. PASS.
- Web: candidate made zero new external claims (all S-B2x-xx identifiers
  carried as record-vintage, so labeled); no consequential web source
  required re-opening under the card's rule. No fabricated citation, DOI,
  count, quote, measurement, or provenance claim found.

## Defects

1. **Minor** — `outputs/B30_skills/attempt-1/SKILLS.csv` line 1 is a long
   comma-bearing comment line before the header; a strict CSV parser reads
   it as a malformed record. Acceptance test: SKILLS.csv exact-12-column
   schema. Mitigated: identical convention in the accepted pilot, disclosed
   in SELF_CHECK item 3; header and all 20 data rows are exactly 12 fields.
2. **Minor** — SELF_CHECK item 13 says the horizon tables place "all 20
   rows," but S8 and S20 appear in the horizon tables only via the
   "Skill re-audit | all" row (both are deliberate $0/defer-to-B40 rows,
   consistent with their CSV cells and the owner map). Slight overstatement
   in the self-check wording, not an artifact inconsistency. Affected file:
   SELF_CHECK.md; acceptance test: SELF_CHECK recounts reproducible.
3. **Minor** — SKILLS.csv S13 evidence says the venue route is "decided but
   unexecuted (C35)"; C35 is a `proposed` recommendation (the corpus's own
   stage-30 route-decision document, unexecuted). The row and PREP_PLAN
   treat it correctly as unexecuted; the word "decided" slightly overstates
   the record's status. Affected file: SKILLS.csv (S13); acceptance test:
   grounding fidelity.

No critical defects. No major defects.

## Limitations

- JSON validity confirmed by complete manual read, not by executing a
  parser (native contract: no code execution).
- EVxx/Pxxxx/S-B2x-xx identifiers were verified against the accepted
  B15/B20/B25 stage outputs (the prescribed grounding), not re-traced to
  `sources/` primaries; that tracing was the prior stages' verified scope.
- Verifier observed-model evidence is system-prompt self-identification
  (`claude-fable-5`); observed effort NOT_EXPOSED — recorded, not claimed
  as telemetry.

VERDICT: PASS
