# Independent verification — B10_phd FULL attempt-1

## 0. Scope and inputs

- Stage/mode: `B10_phd`, FULL. Candidate: `outputs/B10_phd/attempt-1/`
  (`PHD_FACTS.json`, `PHD_CORE.md`, `OPT2.md`, `SOURCES.csv`, `RUN_META.md`,
  `SELF_CHECK.md`). Read-only; nothing edited.
- Verification card: `state/CURRENT_VERIFY.md`. Stage spec:
  `workflow/stages/B10_phd.md`. Rules: `.claude/skills/pap06-native/references/ACCEPTANCE.md`,
  `SOURCE_POLICY.md`, `LIT_POLICY.md`, `MODEL_POLICY.md`.
- Ground truth opened independently this run: `sources/phd/**` (folder 06,
  folder 08, projects 01-05, 07 raw archive), the accepted pilot
  `pilot/B10_phd/attempt-1/PHD_FACTS.json`, and one live web fetch of the
  candidate's single external web row.
- Verifier identity record: role `pap06-verifier`; requested model/effort
  `Fable 5 / xhigh`; observed model self-identification this session:
  `claude-fable-5` (from the verifier session's own system context); observed
  effort: `NOT_EXPOSED` (treated as missing observation, not a mismatch).
- Worker record in candidate `RUN_META.md`: named agent `pap06-sonnet-high`,
  requested `Sonnet 5 / high` — matches the card; observed model/effort
  recorded as `NOT_EXPOSED` on both axes, with no inference attempted.
  Correct discipline.

## 1. Check-by-check findings

### Check 1 — Files present; SOURCES.csv schema

All six files present and non-empty. `SOURCES.csv` header is exactly
`claim_id,url,title,publisher,published_date,accessed_date,source_type,stage_file,confidence,limitation`
(10 columns). Three data rows, each parsing to 10 fields (quoted fields
correct; multi-claim IDs use semicolons; row 4 is an explicitly-labeled
comment row with empty leading fields and a quoted limitation — parseable).
PASS.

### Check 2 — PHD_FACTS.json recount

My independent recount (full read of all 511 lines plus Grep tallies):

- `"claim_id"` occurrences: 50; IDs run C01..C50 with no gap and no
  duplicate (verified by extracting every `"claim_id": "Cxx"` value).
- Statuses: demonstrated 24 (C01-C04, C11-C13, C16, C17, C20-C22, C33,
  C34, C36, C37, C39-C42, C44, C46, C49, C50); proposed 17 (C06, C08-C10,
  C14, C18, C19, C24-C26, C28, C31, C32, C35, C38, C47, C48); inferred 4
  (C07, C23, C27, C43); unknown 5 (C05, C15, C29, C30, C45). Total 50.
  Matches the candidate's stated 50 = 24/17/4/5 exactly.
- Required fields: `claim_id`, `claim`, `status`, `opt2_mapping`,
  `source_path`, `page_or_section`, `confidence`, `limitation` each occur
  exactly 50 times; every status value is from the controlled vocabulary.

PASS.

### Check 3 — C01-C10 stability vs accepted pilot

Compared claim-by-claim against `pilot/B10_phd/attempt-1/PHD_FACTS.json`:

- IDs C01-C10 all present once, same order, no renumbering.
- Statuses identical in all ten (C01-C04 demonstrated, C05 unknown,
  C06/C08/C09/C10 proposed, C07 inferred).
- Claim text identical in substance (ASCII normalization of °/×/Ω/§ only;
  C07 drops the pilot's trailing "per the corpus's cited sources" phrase
  without changing meaning).
- Changes are confined to `page_or_section` refinements and `limitation`
  additions, each explicitly labeled ("REFINEMENT (full run)" /
  "Unchanged from pilot" / "Full-run addition"). C02's source upgrade
  (corpus summary -> primary decision-letter PDF) is explicitly labeled
  as closing a pilot-flagged limitation. No silent change, no demotion or
  promotion.

PASS.

### Check 4 — Citation-fidelity spot-checks (~35 claims; required minimum 12)

Demonstrated experimental claims (required >= 3):

- **C01**: all six named raw files exist under
  `sources/phd/P/01/07_HSX_august2025_results/hsx_20250821/`
  (hsxMainCoilCurrent_shot65/68.txt, 25_8_21_#18/#19/#20_stored_energy.dat,
  test_note.docx), confirmed by my own Glob. Voltage-domain/qualitative
  limitation honestly stated.
- **C03**: verbatim match in `02_HSX_Hall_Sensor_Readout/NOTES.md`
  (2026-07-08 entry: 686 mV -> <=5 mV, >=130x, 8-bit/5-cycle limit, 4x680 Ω
  + 2.2 kΩ, 20 mA, 20 kHz, gain 100.3); journal file
  `journal/2026-07-08_spinning_emulator_20mA.md` exists.
- **C04**: verbatim "OPEN ANOMALY" bullet (~75 V expected vs 0.686 V, ~109x;
  leakage and R_G ruled out; "Don't calibrate to these magnitudes yet");
  the full-run refinement's cross-project corroboration verified at
  `05_HSX_ChatGPT_Windows_App/outputs/FINAL_ACCEPTANCE_CHECKLIST.md` line 105
  (unchecked "X/Y/Z approximately 109-times anomaly is root-caused..." gate).
- **C13**: SPECS.md "System at a glance" confirms AD8429 G = 100.3, R_G =
  60.4 Ω "(reads ≈ 59.8 Ω in-circuit)"; NOTES.md 2026-07-06 confirms
  as-built R9 = R10 = 100 Ω, netlist cross-check, firmware/analysis assets.
  The claim's own limitation correctly flags the aspirational calibration
  cell (see C15).

Folder-08 claims (required >= 3, pre-redteam caveat required on each):

- **C07**: `02_MUTUAL_CALIBRATION_FEASIBILITY.md` plain-language verdict
  matches exactly (Hall->coil hardware-proven, CERN bench + ITER OVSS;
  coil->Hall gain-only, never offset; "the sensors calibrate each other"
  explicitly rejected; "no hardware demonstration of the coil->Hall
  direction exists in fusion conditions"; single non-fusion driven-ramp
  precedent). Caveat present.
- **C23**: `02_OBSERVABILITY_AND_IDENTIFIABILITY.md` confirms Theorem 1
  (two-parameter gauge group, labeled Derived), CASE A rank 5/7 with both
  analytic null vectors matched at ~1e-15, `tools\observability_rank_tests.py`,
  the "not experimental validation" self-label, and Case 9 (CASE H-broad
  rank 5/6). Candidate honestly keeps status "inferred" and explains why.
  Caveat present.
- **C24/C26/C27**: `05_LIMITATIONS_AND_FAILURE_MODES.md` confirms the
  FM-01..FM-18 register with the stated per-mode structure, Section 3.6
  verbatim ("The broad hybrid idea is not novel," 26-year prior art chain,
  "no publishable claim can rest on 'we hybridized a Hall sensor with a
  coil'", four gaps (a)-(d)), and Section 4's simpler-sensor-wins
  counterexamples. Caveats present on all three.
- **C25**: `05_FALSIFICATION_TESTS.md` confirms FT-01..FT-12, order = cost,
  FT-01..FT-10 zero radiation, FT-11/FT-12 collaborator-led, and the
  explicitly-good-outcome branches. Caveat present.
- **C29**: folder-08 `01_SOURCE_COVERAGE.md` "Unresolved gaps" item 1
  (no bare GaN/AlGaN Hall-plate neutron study, largest direct-evidence gap)
  and FM-05's ~14x cross-species scaling failure both confirmed. Caveat
  present.
- **C17**: folder-08 `01_SOURCE_COVERAGE.md` confirms 219 rows, 215
  verified + 4 uncertain, 17 reused vs folder 06, 198 new-verified vs the
  >=75 gate, all four quotas met at >=2x (70/25, 79/30, 76/25, 50/20),
  99/215 metadata-only. Caveat present.
- **C31/C48**: "it gates every dollar after it" is genuine —
  `06_ADVISOR_MEETING_BRIEF.md` lines 113-114 (phrase line-wrapped, which
  is why a naive single-line search misses it); FT-04 one-bench-day
  first-hardware framing confirmed adjacent. C32's "~3-6 marginal
  bench-days" confirmed twice in the same brief. Caveats present.
- Per-claim caveat sweep: every folder-08-sourced claim (C07-C10, C17,
  C23-C32, C43, C48) carries the pre-redteam/pre-synthesis caveat in its
  own limitation text; C40 states the underlying fact and I reconfirmed it
  by Glob: exactly 25 files under folder-08 `outputs/`, none matching
  redteam/synthesis. (A `logs/.../70_redteam/` session stream exists in
  folder 08's logs, but no redteam/synthesis OUTPUT file — C40's wording,
  which is specifically about outputs, remains accurate.)

Publication-status claim (required):

- **C02/C22**: I opened `sources/phd/P/01/06/inputs/Decision_Letter_IEEE_2026-07-23.pdf`
  in full (4 pages). Confirmed: decline with invitation to revise under a
  new Manuscript ID; SENSL-26-07-RL-1061; dated 23-Jul-2026 (sent 22 July
  2026, 18:13 GMT-7); sensl-admin@ieee.org; Dr. Giacomo Langfelder, AEIC;
  AE novelty concern with the four specific requests (GaN comparison table,
  repeatability statistics, bench-top calibration, Fig. 5 in field units);
  Reviewer 1 "novel and unique to my knowledge" / "still worth publishing";
  Reviewer 2 "lacks sufficient novelty" / "this version should be
  rejected". All as claimed. C49's zero-accepted-first-author statement
  also matches `FINAL_EXECUTIVE_STRATEGY.md` lines 14-23 verbatim.

Unknown claims (required >= 1):

- **C05**: `03_MANUSCRIPT_DIAGNOSIS.md` row M5 states "no derivation exists
  in the manuscript, its references, or `SPECS.md`"; Section 6 confirms the
  1 MHz figure appears twice (manuscript lines 453, 483) underived; my own
  grep of `SPECS.md` finds only the underived "1 MHz raw" table cell (2023
  column) and no derivation; Reviewer 1 minor point 2 disputes the figure
  verbatim in the decision letter. "Unknown" is the honest status.
- **C15**: SPECS.md line 118 ("absolute, Helmholtz + in-situ") exists and
  conflict C6 ("aspirational, not achieved") exists — correctly not marked
  demonstrated.
- **C45**: gate I-4 confirmed in `04_HSX_EXPERIMENT_PLAN.md` (row I-4 plus
  the "this stage's most consequential *new* inventory question" sentence).

Further checks: **C06** (WP-C parameters u(k)/k <= 2%, m +/- ~2%, <0.5%
linearity, GUM/Monte-Carlo, Allan variance in `FINAL_EXECUTIVE_STRATEGY.md`;
~19-29 bench-days is the stage-70 corrected sum per `07_CORRECTION_LOG.md`
rows 5-6 and plan §12.4); **C09** ("Radiation magnitudes for the user's
device family are Unknown", `03_RADIATION_COMPENSATION_ARCHITECTURE.md`
line 40); **C11** (conflict C1 with the boilerplate string near line 438 and
the "_2023" renamed PDF); **C12** (byte-size figure present in
`00_INPUT_INVENTORY.md` Group B); **C16** (231 rows, 154%, 10/58/32%
access depths in folder-06 `01_SOURCE_COVERAGE.md`); **C18** (122-ref
registry and the "[UNVERIFIED] ... must insert it manually" rule in project
04's paper plan); **C19** (COMPLETE_WITH_OPEN_GATES, FAIL/HOLD, 8 BLOCKER /
14 MAJOR / 3 MINOR / 8 NOTE-PASS, dated 2026-07-12; status disagreement is
corpus conflict C5); **C21** (Publications tree matches the Glob listing
exactly); **C33/C41** ("thin and combination-specific, not platform-level";
sponsor-rights item with DE-AC02-76SF00515 / SLAC FWP 101264 / TomKat /
ECCS-2026822); **C34** (G-C "single most consequential disclosure event on
the board"); **C37/C39** (`07_RED_TEAM.md`: eleven findings — 1 medium,
6 low, 4 informational, hence 0 critical/high; F-1 medium; F-7 RSI-policy
archive-snapshot finding); **C38** (M01-M44; G5 at month 12 with the two
conditions and OPT3 pivot); **C44** (Section 5 items 1-2 verbatim,
including "The claim 'first fusion Hall diagnostic' is **false** and must
never appear" and the exact S0128 QHS wording rule); **C47** (Section 1
verdict, §3.3 OPT3, §10 "Approve the novelty re-centering"); **C50**
(`06/EXECUTION_PLAN.md` and `06/inputs/ORIGINAL_REQUEST.txt` exist; the
AI-mission provenance is corroborated by folder state/log artifacts);
**C36** (see Check 8). No fabricated path, quote, number, or status found
in any sampled claim. PASS.

### Check 5 — Distinct-claims rule

Absolute calibration (C06), mutual consistency (C07 + C23), bandwidth
fusion (C08), radiation compensation (C09 + C29 + C30) are separate claims
with separate citations; OPT2.md Element 2 restates the separation
explicitly. C07 states in its own text that mutual agreement is not
automatic absolute calibration, and OPT2.md repeats "Mutual agreement alone
is not automatic absolute calibration." Nowhere does the candidate assert
mutual agreement = absolute calibration as its own claim. Traceable
excitation/reference discipline is present in OPT2.md (traceable
Helmholtz bench standard; trusted coil chain + real field excursions;
zero-field epochs or external absolute reference; excitation-conditional
identifiability). The coil's dB/dt nature is stated verbatim in
PHD_FACTS C08 ("the coil measures dB/dt and is blind at steady field") and
in substance in OPT2.md ("DC/low-frequency field content the coil
structurally cannot see"); the literal token "dB/dt" does not appear in
OPT2.md itself — substance judged present (see Limitations). PASS.

### Check 6 — OPT2.md completeness

All three elements present with status discipline (Element 1 "proposed,
not demonstrated"; Element 2 "never demonstrated on hardware"; Element 3
"proposed, not built"). Dedicated sections exist for Hypotheses (4, each
with a falsifier), Experiments (FT-01..FT-12 ladder table), Deliverables
(P1/P2/P3/T0/capstone), Dependencies (6-item chain), Kill criteria (6
named stop/pivot conditions, each traced to corpus tests/gates), and
Uncertainties (single-source dependencies, absence-vs-proof, redteam
status, provenance). All claim-ID references resolve (no ID above C50
anywhere in the candidate). PASS.

### Check 7 — No ranking

PHD_FACTS.json, PHD_CORE.md, and OPT2.md contain no corpus scorecard
numbers and no recommendation/choice in the extraction's own voice; C28
and C47 describe the corpus's own scored decisions qualitatively with
explicit attribution and explicit refusal to repeat the numbers.
SELF_CHECK.md §8 does quote the corpus's OPT1-4 weighted scores
(3.45/4.29/3.34/2.58) inside a negative-assurance sentence; I verified
those numbers are real corpus values (`02_DIRECTION_SCORECARD.csv`), they
are attributed to the corpus, and they are used neither as fresh judgment
nor as a recommendation — recorded as a minor blemish, not a gate breach.
PASS.

### Check 8 — Pilot labels; NOT_EXPOSED; web log; no fabrication

- Grep for `PILOT SAMPLE|NOT FINAL` across the candidate directory: the
  only hits are SELF_CHECK.md's own audit sentences describing the search
  string — no artifact is labeled as pilot/sample/non-final. PASS.
- RUN_META records requested model/effort and `NOT_EXPOSED` for both
  observed axes, with explicit no-inference statements. PASS.
- SOURCES.csv vs web activity: row 3 (the single live web row) matches
  RUN_META's enumerated WebFetch. I independently re-fetched
  `https://ieee-sensorsletters.org/information-for-authors/` on 2026-07-28
  and confirmed all three cited facts verbatim (4-page limit including a
  single-column reference minimum; sensor-device scope; "Submission-to-
  ePublication = 4.8 weeks, median"). Row 2's URL is the decision-letter
  PDF's own printed page URL (matches the PDF footer exactly), with an
  honest limitation explaining it was read as a supplied PDF, not fetched.
  The IEEE author-guidance row is honest. Two minor internal wording
  inconsistencies in the web-activity count were found (Defects 1-2).
- No fabricated path, quote, count, or publication status found anywhere
  in the ~35-claim sample, including every quoted phrase I chased to its
  source. PASS with minor defects noted.

### Check 9 — Cross-artifact consistency

The 50 = 24/17/4/5 breakdown is identical in PHD_FACTS.json (recounted),
SELF_CHECK.md, and PHD_CORE.md's usage; PHD_CORE.md and OPT2.md claim-ID
references all resolve to real claims (no out-of-range ID). Folder-06
"31 output files" matches my Glob (31 files + `.gitkeep`); folder-08
"25 output files" matches my Glob. RUN_META's read inventory is consistent
with the cited source_paths (spot-checked). One arithmetic slip found in
RUN_META limitation 2 (Defect 3). PASS with minor defect noted.

## 2. Defects

1. **Minor** — `outputs/B10_phd/attempt-1/RUN_META.md` ("Web activity"):
   states "Two `WebFetch` calls were made this run:" but enumerates exactly
   one. Acceptance test: the stated call count matches the enumerated log.
   Repair (if ever revised): either list both calls or correct the count.
2. **Minor** — `outputs/B10_phd/attempt-1/SELF_CHECK.md` §12 describes
   RUN_META's web section as "(one `WebFetch` call)", contradicting
   RUN_META's own "Two" wording (Defect 1). Acceptance test: SELF_CHECK's
   characterization matches RUN_META verbatim. Same repair as Defect 1.
3. **Minor** — `outputs/B10_phd/attempt-1/RUN_META.md` limitation 2:
   "Fourteen of the fifty claims" precedes a parenthetical list of 18 claim
   IDs (C07-C10, C17, C23-C32, C40, C43, C48). The per-claim caveats
   themselves are correct and complete; only the count word is wrong.
   Acceptance test: stated count equals the number of listed IDs.
4. **Minor** — `outputs/B10_phd/attempt-1/SELF_CHECK.md` §8 reproduces the
   corpus's OPT1-4 weighted score values inside a negative-assurance
   sentence. Not a gate breach as worded (not fresh judgment, no
   recommendation, numbers verified real and attributed), but it places the
   scorecard numbers inside the candidate directory; cleaner practice is to
   describe the check without quoting the values.

No critical defects. No major defects.

## 3. Limitations of this verification

- Sampled, not exhaustive: ~35 of 50 claims were opened against their
  cited sources; the rest were checked for structure, status plausibility,
  caveat presence, and path existence. No sampled claim failed, and the
  sample was chosen adversarially (all four statuses, all source folders,
  every quoted phrase and controlled number I judged consequential).
- I did not re-open the ~450 external literature rows cited inside the
  corpus's own ledgers; the candidate explicitly does not re-assert them
  and carries the corpus's own access-level limitations per claim, which
  matches SOURCE_POLICY.
- The literal token "dB/dt" appears in PHD_FACTS C08 but not in OPT2.md;
  I judged the dB/dt discipline present in OPT2.md in substance
  (coil blind to DC/static content, integrator drift, excitation
  conditions). Recorded here for transparency rather than as a defect.
- Observed worker model/effort are `NOT_EXPOSED` in RUN_META; per
  MODEL_POLICY this is missing observation, neither a mismatch nor proof.
  My own effort setting is likewise not exposed to me.
- Folder 08 contains a `70_redteam` log stream (session artifacts) but no
  redteam output file; C40's outputs-scoped wording remains accurate, and
  any future rerun should re-check whether folder-08 redteam outputs have
  since appeared (the candidate itself says the same).

VERDICT: PASS
