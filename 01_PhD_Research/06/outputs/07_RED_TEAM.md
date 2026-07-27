# 07 — Red-team audit of all completed mission outputs (Stage 70)

Prepared by: Claude Code, stage `70_redteam`, requested model Fable 5 /
Extra High. Committee lenses applied: fusion-diagnostic instrumentation
reviewer, Hall-sensor/metrology reviewer, PhD-program scheduler,
reproducibility auditor, startup-translation skeptic, cautious
pre-publication IP reviewer.

**Independence statement.** This audit used freshly written deterministic
checks (`state/tools/70_audit_ledger.py`, `70_audit_crossrefs.py`), a
sampling rule deliberately different from stage 10D's re-verification
sample (`70_sample_verify.py`: deterministic md5-rank stratification over
lane × access × year-band × tier, vs 10D's 10C/2025-26/unusual-venue
weighting), and verification channels the earlier stages did not use
(Semantic Scholar API, Internet Archive snapshots, secondary press
corroboration, direct extraction of the manuscript `.tex` from the
immutable input zip). **Provider-level independence is not claimed:** the
same Claude family (and in most stages the same Fable 5 model) produced
the audited outputs and this audit. Per `EXECUTION_PLAN.md`, a
cross-provider review remains the manual ChatGPT continuation's job if
the user wants one.

Companions: [`07_SOURCE_AUDIT.csv`](07_SOURCE_AUDIT.csv) (46 audit rows),
[`07_CORRECTION_LOG.md`](07_CORRECTION_LOG.md) (every file patched).

---

## 0. Verdict

**No critical or high-severity defects were found.** The source count
(231 verified ≥ 150), the recommendation logic (stages 20/30 arithmetic
and derivations re-verified exactly), and the safety/legal wording
(stage 50 disclaimers, no-radiation scope, no immigration/investment
advice) all survive adversarial re-examination. Eleven findings —
1 medium, 6 low, 4 informational — were identified; the nine that are
correctable were corrected in place (see the correction log), and the two
launcher-telemetry items are documented here as observations that no
mission file can fix.

Stage-pass condition ("no unresolved critical defects in the source
count, recommendation logic, or safety/legal wording"): **met**.

---

## 1. Findings, ordered by severity

### F-1 (MEDIUM, corrected) — Milestone M15's dependency contradicted its own dates

- **Evidence:** `06_MILESTONES.csv` M15 (campaign-#1 pre-ship gate,
  target 2026-09-08) listed dependencies `M09; M10`, whose targets are
  2026-09-20 and 2026-09-25 — a dependent milestone dated 12–17 days
  *before* its dependencies complete. Found by a deterministic
  dependency-chronology check the stage-60 validator did not include.
- **Impact:** a reader executing the CSV literally would conclude
  campaign #1 cannot ship before ~Sep 25, contradicting M16's stated
  Sep 8–20 realistic window and muddying the roadmap's own
  "August target is tight" honesty flag — the exact place schedule
  credibility matters most.
- **Root cause:** M15's deliverable ("calibration status **frozen**
  before shipment") describes a status-freeze dependency, not a
  completion dependency; the dependency cell over-stated it.
- **Disposition: corrected.** Dependency cell now reads "M09; M10
  (pre-ship freeze: the gate freezes whatever calibration status exists
  at ship date; full completion of M09/M10 is not required — see
  deliverable)". Stage-60 validator re-run: PASS.

### F-2 (LOW, corrected) — Roadmap critical-path diagram overstated a dependency

- **Evidence:** `06_24_MONTH_PHD_ROADMAP.md` §2.1 draws
  `P1 acceptance (M26) -> P2 draft/submit (M27)`, but the CSV correctly
  has M27 depending only on M17/M23, and §3's January-2027 entry runs P2
  drafting in parallel with P1 review.
- **Impact:** taken literally, the diagram adds ~2 months of false
  serialization to the plan's tightest stretch.
- **Disposition: corrected** with a clarifying note in §2.1 (the CSV was
  already right; the diagram shows the acceptance sequence of the
  two-paper floor).

### F-3 (LOW, corrected) — "4.8-week post-acceptance median" mislabel

- **Evidence:** roadmap §3 (January 2027) called SENSL's statistic a
  "post-acceptance median"; the journal's own page (re-fetched live this
  stage) states "Submission-to-ePublication = 4.8 weeks, median" —
  stage 30 quoted it correctly; stage 60 relabeled it in passing.
- **Impact:** minor, and actually conservative — the true statistic makes
  the Jan-2027 acceptance window *more* plausible, and the M18→M26 window
  already budgets ~2–4× the median.
- **Disposition: corrected** to the accurate label.

### F-4 (LOW, corrected) — Stage 60's two web-sourced claims cited no URL

- **Evidence:** the roadmap's [EE] claims (Stanford EE reading committee
  in year 3; University Oral Exam in year 4) appeared with no recorded
  link anywhere in the stage-60 outputs, violating the mission's
  every-material-claim-needs-a-stable-link rule. `PROJECT_STATE.md`
  explicitly asked stage 70 to re-verify them.
- **Verification:** both claims verify against the official pages
  ([Graduate Degree Progress](https://ee.stanford.edu/academics/graduate-degree-progress),
  [PhD Oral Exam](https://ee.stanford.edu/academics/graduate-degree-progress/oral-exam),
  accessed 2026-07-25). Content was right; provenance was missing.
- **Disposition: corrected** — verified URLs added to the roadmap header.

### F-5 (LOW, corrected) — Tier-1 burden total off by one at the top of the range

- **Evidence:** `04_HSX_EXPERIMENT_PLAN.md` §12.1's Tier-1 blocks sum to
  19 (minima) and 29 (maxima: 6+3+3+6+7+4), not the stated "≈ 19–28";
  the optional packaging add (+2–3) pushes the honest ceiling to ~32.
- **Impact:** trivial arithmetic, but the number is quoted twice in the
  roadmap and drives a progress indicator.
- **Disposition: corrected** in the plan and both roadmap quotes
  (≈19–29, packaging add stated).

### F-6 (LOW, corrected) — Off-by-one advisor-question cross-reference, twice

- **Evidence:** stage 20 §10 lists gen-2 die status as advisor decision
  **#3** (the UW email is #4). `03_REVIEWER_RESPONSE_MATRIX.csv` (AE-03)
  and `03_PUBLICATION_ROUTE_DECISION.md` §7 both said "#4" for die
  supply. (`04_HSX_EXPERIMENT_PLAN.md` §13 has it right.)
- **Impact:** an advisor working from the gate table could chase the
  wrong decision item.
- **Disposition: corrected** in both stage-30 files.

### F-7 (LOW, resolved gate + strengthening annotation) — RSI policy wording was search-extraction confidence

- **Evidence:** stage 30 honestly flagged that the RSI
  previously-published wording came from search extraction because
  `pubs.aip.org` returned HTTP 403. This stage verified both quoted
  sentences **verbatim** in an Internet Archive snapshot (2025-11-15) of
  the same official page (live page still Cloudflare-blocked). The
  snapshot also contains a criterion stage 30 did not quote: *"The major
  criterion for publication is technical novelty. A previously published
  instrument is not considered to be novel."*
- **Impact:** the open gate handed to stage 80 is closed (to
  archived-official-page confidence, ~8 months old — re-check live
  before actual submission). The extra criterion *sharpens* Route C:
  the RSI paper must be a new instrument/technique, not "same
  instrument, more data" — the existing vector-probe framing already
  satisfies this, so the recommendation stands unchanged.
- **Disposition:** annotation added to
  `03_PUBLICATION_ROUTE_DECISION.md` §4.

### F-8 (INFO, corrected) — One patent-note phrase brushed a legal conclusion

- **Evidence:** `05_PRIOR_ART_LEDGER.csv` PA-P03 said the abandoned
  application "remains 102 prior art" — a flat statutory
  characterization in an otherwise scrupulously disclaimed screen.
- **Disposition: corrected** to "remains citable prior art as a published
  application; whether and how it qualifies under 35 USC 102 in any
  analysis is a counsel determination." No other legal/ownership/
  patentability overstatement found anywhere in stage 50 (the triple
  disclaimer, counsel-routing, and no-filing-recommendation posture are
  consistently maintained).

### F-9 (INFO, corrected) — Rounding nit in the sensitivity analysis

- **Evidence:** doubling u(k) in the §3.1 placeholder budget gives
  u(m)/m = 4.05% → "≈4.0%", not "4.1%" as
  `04_UNCERTAINTY_AND_STATISTICS_PLAN.md` §5 stated. All other stage-40
  statistics re-verified exactly (see §2.5 below).
- **Disposition: corrected.**

### F-10 (INFO, documented only) — Stage-written timestamps are UTC mislabeled as -07:00

- **Evidence:** launcher logs place stages 50/60 at 01:55–02:29 (-07:00),
  but stage-session-written records say "started 09:35:00-07:00" and the
  checkpoint names embed 09:30/10:30 — those are UTC clock values
  carrying a -07:00 suffix.
- **Impact:** none on content; confusing for forensic timeline reading.
- **Disposition:** documented here and in the correction log; checkpoint
  files are not renamed (names are referenced elsewhere; the launcher's
  event log remains the authoritative clock). Stage-70 entries use true
  local time.

### F-11 (INFO, documented only) — Contradictory security-fallback telemetry on stage 30

- **Evidence:** `state/OPERATION_LOG.csv` stage-30 rows carry
  `security_fallback_flag=True` inside the packed notes string while the
  same rows' structured column says `False`; exactly one event in
  `state/CLAUDE_EVENT_LOG.jsonl` (stage 30's result event) shows the
  flag true. Primary evidence refutes an actual fallback: stage 30's raw
  `stream.jsonl` shows `init.model = claude-fable-5`, the **final
  main-session assistant message from claude-fable-5**, and Haiku only in
  aggregate `modelUsage` (consistent with WebFetch's internal model);
  no Opus (the documented fallback target) appears anywhere.
- **Impact:** none under `MODEL_POLICY.md` (final result model is Fable);
  the launcher's notes-string derivation has a latching/derivation bug
  worth the user's attention if telemetry is ever relied on alone.
- **Disposition:** documented; state logs are launcher-owned evidence and
  were not rewritten.

---

## 2. Checks that passed without findings

### 2.1 Source ledger (deterministic)
231 rows; exact 16-column header; IDs S0001–S0231 sequential, no gaps or
duplicates; 0 duplicate normalized DOIs/titles; 231/231
`verified_peer_reviewed` (≥150 met, margin 81); source types only
journal_article/review_article/conference_paper; tiers/access/years all
in-enum; all URLs are doi.org resolver links matching the DOI column.

### 2.2 Stratified manual verification (36 rows ≥ 30 required)
Deterministic md5-rank sample covering all 9 lane×access cells, all 7
year bands (1971–2026), all 3 tiers (A21/B12/C3), and all 7
SOURCE_POLICY topic categories. Crossref identity: **36/36 match** (4
flags adjudicated as dash/abbreviation artifacts). Deep content checks:
S0068 full-text numbers verified from the CC-BY primary text; S0128's
load-bearing QHS sentence verified verbatim from the publisher page;
S0002's numbers corroborated by two independent secondary reports,
consistent with its honestly-recorded snippet-level basis; PA-P01 patent
status/expiration verified on Google Patents. Row detail:
[`07_SOURCE_AUDIT.csv`](07_SOURCE_AUDIT.csv).

### 2.3 Inline-claim spot checks
276/276 inline `[S####](doi)` links across all reports match the cited
row's ledger DOI. Numeric claims traced to rows and verified: 60-sensor
ITER bismuth array (S0114), 1,118 KSTAR training discharges (S0181),
Munter-1990 spinning-current origin (S0033), CTH GaAs/Biot–Savart
validation (S0143), JET ±0.07%/11+yr/19,000+ pulses (S0068). The
stage-20 verbatim quote from `ORIGINAL_REQUEST.txt` ("with or without
conventional coils sensors, together, to resolve the drift problem")
appears verbatim in the input file.

### 2.4 Novelty and "first" claims
Every "first" claim in every output is granularity-bounded (first
GaN/WBG 2DEG Hall in-vessel in a confinement device; first Hall of any
kind in a QHS stellarator), explicitly labeled a bounded absence finding,
and paired with named bounding prior art; the false claim "first fusion
Hall diagnostic" is prohibited in three separate places. The QHS facility
wording is pinned to S0128's exact sentence (re-verified this stage). No
unsupported "first" claim found anywhere.

### 2.5 Recommendation logic and arithmetic
Stage 20: all four baseline weighted scores (3.45/4.29/3.34/2.58), both
adversarial re-weightings (W_B 3.75/4.20/2.90/3.15; W_C
3.30/4.30/3.35/2.30), and the uncertainty propagation (±0.35 score,
±0.50 difference) recomputed exactly; scorecard CSV consistent with the
report and with recomputation; the OPT2 margin (0.84 ≈ 1.7× the
difference uncertainty) supports the stated robustness; falsifiability
register present and specific. Stage 40 statistics: 1/√(2(n−1)) values,
t-based CI factors, 2.8·s·√(2/n) detectable-effect values, the 2.1%
worked budget, the 92% variance share, and the ~185× extrapolation ratio
all recomputed exactly (single rounding nit = F-9).

### 2.6 Manuscript/reviewer coverage (ground-truth re-read)
The decision-letter PDF was re-read in full and the manuscript `.tex`
extracted from the immutable input zip. All 16 matrix rows map 1:1 onto
every substantive AE/R1/R2 point — no reviewer concern is uncovered, and
no matrix row invents a concern. Checkable manuscript facts verified
against the source: 20 references; exactly 4 GaN-Hall-specific refs
(ref10/ref11/ref12/ref15); S0005 absent as claimed; title/abstract/
setup/figure/conclusion line references accurate; G=200 INA849+2×OPA814
chain; underived 1 MHz figure; abstract's loose QHS wording vs the
intro's more careful variant; the conclusion's neutron-facility
future-work sentence (correctly flagged against the mission scope rule).

### 2.7 Experiment feasibility, traceability, data availability, cleanroom
The plan assumes nothing in-hand (inventory gates I-1..I-9), separates
bench from machine references, refuses to claim any B-dot bound before
U-1 answers, carries the voltage-bias/current-bias chain distinction
(C-03) needed for the retroactive conversion, and pre-drafts honest
limitations language for every degraded case. Calibration traceability
is triangulated (geometry+shunt / pickup coil / commercial references)
with the coil constant correctly identified as the dominant term.
Cleanroom claim ("zero cleanroom steps") is accurate at
fabrication-content level; the assembly-lab burden (wedge bonding, LCC
packaging, encapsulation, cube machining) is carried honestly with yield
risk (G3) and burden estimates. *Skeptic's note, no correction needed:*
if Stanford's wedge bonder physically resides in a shared
cleanroom-class facility, facility-access overhead should be budgeted in
practice even though no cleanroom *fabrication* occurs — the schedule's
per-block slack covers this.

### 2.8 Schedule critical-path realism
The graduation-critical path never requires HSX success; P1 is
bench-only by design; buffers exist at every layer (per-block bench
slack, ~1 month per chapter block, 2-month defense→submission gap);
slip-decision table names detection points, owners, and pre-planned
fallbacks; the two schedule reconciliations stage 60 performed (P3
Mar-2027-upside vs 2027–28 realistic; campaign-#1 August tightness) are
consistent with stages 20/30/40/50 content. The one real defect was F-1.
Residual honest risk, correctly flagged by the roadmap itself: a second
P1 decline plus a P2 failure is the only scenario without a fully
pre-planned fallback — it is named in §8 of the roadmap, not hidden.

### 2.9 Cross-report contradiction sweep
IP-gate ordering (screen before any disclosure) is identical in stages
20 §9, 30 §3.2/§6, 50 G-C, and 60 M13→M18/M19. Campaign-#2 window
(Nov 2026, ~Feb 2027 slip limit) is identical in 20 §8, 30 §3.3, 60 §1.
P1's campaign-independence is identical in 20 §6, 30 §3.1, 40 §11.1,
60 §2. The startup file makes no claim that contradicts the IP screen
(it defers wholly to stage 50) and contains no investment/funding/
immigration advice. No contradiction survives except the two corrected
representation slips (F-2, F-6).

### 2.10 Model/effort and checkpoint audit
All 10 completed stages ran attempt 1 on the EXECUTION_PLAN-assigned
model/effort; all 10 completion markers and checkpoints exist; the five
Fable-assigned completed stages have Fable-produced final results
verified from raw streams (init model + final main-session assistant
message), with Haiku appearing only as logged auxiliary usage
(WebFetch-consistent), which `MODEL_POLICY.md` expressly allows. No
quarantine, no downgrade, no handoff trigger. Telemetry nits: F-10, F-11.

---

## 3. Standing limitations this audit re-affirms (no correction possible)

1. **The novelty anchor is an absence finding.** Three independent
   bounded searches (now plus this stage's spot re-searches) found no
   GaN/AlGaN Hall deployment in any confinement device — still not proof
   of priority. Stage 20 §11's reversal conditions remain the governing
   safeguard.
2. **32% of ledger rows are metadata_only.** The stage-10D rule stands:
   no specific number from a non-full-text row goes into a manuscript
   without primary-PDF confirmation (S0002 is the worked example).
3. **Provider-level independence not achieved** (by design of the
   Claude-only package) — see the independence statement above.
4. **Live-page verification gaps:** RSI policy verified via an ~8-month
   old archived copy of the official page; SENSL invitation-lapse
   question remains open (a costless editorial query, owner: user/
   advisor).
5. **Open technical gates unchanged:** ~109× anomaly (C017/G1), deployed
   module custody (I-4), die supply (advisor decision 3), UW co-located
   records (U-1), campaign windows (U-9/G4). This audit found them
   consistently carried, not resolved — resolving them is bench/human
   work, not analysis.

---

## 4. What stage 80 may rely on

- The 231-source ledger, as re-validated here (schema, count,
  identity, citation integrity).
- Stage 20's OPT2 verdict and scorecard arithmetic, as re-verified.
- Stage 30's route A→C with the RSI policy now at
  archived-official-page confidence and the new-instrument criterion
  annotated.
- Stage 40's plans as corrected (burden 19–29).
- Stage 50's screen as corrected (PA-P03 wording).
- Stage 60's register as corrected (M15, §2.1 note, 4.8-week label,
  Stanford URLs).
- This file's §3 as the honest-limitations base for the final synthesis.
