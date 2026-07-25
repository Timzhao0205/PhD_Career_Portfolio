# FINAL — Executive strategy (Stage 80 synthesis)

Prepared by: Claude Code, stage `80_synthesis`, requested model Fable 5 /
Extra High. This document synthesizes the accepted, red-team-corrected
work of stages 00–70. **It introduces no new direction, invention,
experiment, or source-dependent claim** — every position below traces to a
prior validated output, cited by file. Source IDs `[S####]` resolve in
[`01_SOURCE_LEDGER.csv`](01_SOURCE_LEDGER.csv) (231 verified peer-reviewed
rows) with a `https://doi.org/...` link on first use. Epistemic labels
follow the mission convention: **[SF]** supplied fact, **[EE]** external
evidence, **[INF]** inference, **[REC]** recommendation, **[PX]** proposed
experiment, **[GATE]** unresolved gate.

**Standing corrections this document honors (conflicts C1/C6,
[`00_CONFLICT_LEDGER.md`](00_CONFLICT_LEDGER.md)):** the manuscript is an
**unpublished** submission — submitted 2-Jul-2026, declined 23-Jul-2026
with an invitation to revise and resubmit under a new Manuscript ID [SF].
It was never published in 2023; any CV, website, or committee document
saying otherwise should be corrected by Tim directly. Project 02's
"calibrated" language is **aspirational**: the demonstrated bench result is
≥130× offset cancellation on a resistor-ring emulator with an open ~109×
magnitude anomaly [SF]. Tim currently has zero accepted first-author
publications [SF] — the risk posture below follows from that.

---

## 1. Direct answer: continue, adjust, or change?

**CONTINUE the GaN Hall-effect magnetic-diagnostics direction, with a
substantial adjustment in where novelty is claimed and how the output
portfolio is structured. Decision class: ADJUST (option OPT2 of
[`02_RESEARCH_DIRECTION_DECISION.md`](02_RESEARCH_DIRECTION_DECISION.md)).
Do not change direction.** [REC]

The quantitative basis (stage 20, arithmetic re-verified exactly by the
stage-70 red team): on a 9-criterion, mission-anchored weighted scorecard
(1–5 beneficial-direction scale), the adjusted continuation **OPT2 scores
4.29**, against 3.45 for the unmodified continuation (OPT1), 3.34 for a
genuine software-only change of direction (OPT3), and 2.58 for
device-novelty escalation (OPT4). OPT2's margin (0.84 ≈ 1.7× the ±0.50
difference uncertainty) survives ±1-point per-cell score uncertainty and
two deliberately adversarial re-weightings; only the #2/#3 ordering is
weight-sensitive. OPT3 is retained as the named fallback, not the plan.

What "adjust" means concretely [REC, stage 20 §3.2]:

- The **finished, absolutely calibrated sensing output** becomes the
  non-negotiable centerpiece — exactly what the decline letter demands.
- Novelty is re-centered from device granularity (where Reviewer 2's
  objection is the literature's own verdict) to **application +
  calibrated measurement + measurement architecture** granularity.
- Four campaign-uncoupled work packages are added: **WP-A**
  GaN-vs-competitor comparison table, **WP-B** multi-die bench
  repeatability, **WP-C** absolute calibration + GUM/Monte-Carlo
  uncertainty budget, **WP-D** hybrid Hall+inductive drift-corrected
  fusion — so no single paper depends on both HSX campaigns happening on
  schedule.
- This is also, verbatim, the user's own original research interest: GaN
  Hall diagnostics *"with or without conventional coils sensors, together,
  to resolve the drift problem"* [SF, `../inputs/ORIGINAL_REQUEST.txt`].
  The original interest was never device novelty; the first manuscript
  claimed the wrong axis.

## 2. The research thesis and why the evidence supports it

**Thesis (stage 20 §3.2):** *absolutely calibrated GaN Hall-effect
magnetic sensing in the HSX stellarator, plus a drift-corrected hybrid
measurement architecture fusing direct (Hall) and inductive (pickup-coil)
sensing — upgrading the 2025 uncalibrated single-axis demonstration into a
traceable, uncertainty-quantified, vector-capable diagnostic and
quantifying what direct sensing adds to a stellarator's existing
magnetics.*

Three evidence pillars, each re-audited by stage 70:

1. **The concept is field-validated; the specific combination is
   unclaimed.** Hall sensing is the fusion field's own chosen answer to
   integrator drift: JET's InSb probes ran 11+ years at ±0.07% stability
   [S0068](https://doi.org/10.1088/1741-4326/ac8aad), and ITER's
   steady-state magnetic diagnostic is a 60-unit bismuth Hall array
   [S0113](https://doi.org/10.1063/1.4732077),
   [S0114](https://doi.org/10.1063/1.5038871) [EE]. Across three
   independent literature lanes (231 verified sources), **no peer-reviewed
   GaN/AlGaN Hall sensor was found deployed in-vessel in any tokamak or
   stellarator, and no Hall sensor of any kind was found in a
   quasi-helically symmetric stellarator** — a bounded absence finding,
   independently reached by each lane and spot-re-searched by the red
   team [EE/INF]. The claim "first fusion Hall diagnostic" is **false**
   (CASTOR/EAST/JET/ITER lineage) and is prohibited in every output.
2. **The asset is real.** A packaged AlGaN/GaN Hall module survived
   in-vessel deployment in HSX across the Aug-2025 campaign with
   shot-resolved transients and diamagnetic-loop correlation [SF,
   manuscript + raw archive]. No competitor holds an equivalent
   deployment record in this device class.
3. **The failure mode of the old framing is understood and correctable.**
   GaN Hall device physics, spinning-current offset cancellation, and
   temperature behavior are already published — largely by the advisor's
   own group [S0004](https://doi.org/10.1109/JSEN.2019.2895546),
   [S0005](https://doi.org/10.1109/LSENS.2019.2898157),
   [S0006](https://doi.org/10.1063/1.5139911),
   [S0012](https://doi.org/10.1063/5.0305414); spinning current dates to
   1990 [S0033](https://doi.org/10.1016/0924-4247%2889%2980069-X) [EE].
   The adjustment cites that record as prior art and claims the finished
   calibrated application and architecture — the granularity at which the
   first-deployment publication genre operates
   [S0143](https://doi.org/10.1063/1.4894209),
   [S0226](https://doi.org/10.1063/5.0095907) [EE].

## 3. Paper diagnosis and publication route

**Diagnosis (full detail:
[`03_MANUSCRIPT_DIAGNOSIS.md`](03_MANUSCRIPT_DIAGNOSIS.md)):** the decline
letter's operative bar is the AE's sentence "IEEE Sensors Letters requires
a fully finished study of the intended sensing output" [SF]. The
manuscript's core defects, claim-by-claim:

- **Measurand gap (the blocking one):** the title promises magnetic-field
  monitoring; the delivered output is voltage-domain only — no tesla
  value, no calibration coefficient, no V_off exists anywhere in the
  study or archive [SF].
- **Unsupported figures:** the 1 MHz bandwidth is asserted twice with no
  derivation; the "68 consecutive plasma discharge shots" count does not
  match the supplied shot log (60 distinct documented shots incl.
  coil-only) [SF].
- **Wording exposures:** the QHS facility claim must match
  [S0128](https://doi.org/10.1088/1361-6587/adb179)'s exact sentence; the
  "cannot be deployed" claim about conventional Hall devices is
  over-general against the deployed non-GaN lineage; the conclusion
  promises neutron-facility experiments that are out of scope by the
  mission's own rule [SF/EE].
- **Single module, no repeatability statistics** — the AE explicitly
  accepts bench repetition (≥3 dies) as the answer [SF].
- What survives intact: deployment, survival, Hall-origin controls,
  transient data, and Reviewer 1's "novel and unique … still worth
  publishing" assessment [SF].

**Route (full comparison:
[`03_PUBLICATION_ROUTE_DECISION.md`](03_PUBLICATION_ROUTE_DECISION.md)):**

- **Primary [REC]: A → C.** Close the bench evidence package first
  (§4 below), then revise and resubmit to IEEE Sensors Letters under the
  standing invitation (new Manuscript ID, point-by-point response
  supplement, prior ID SENSL-26-07-RL-1061 declared). Then build the RSI
  vector-probe instrument study on campaign #2 as the substantially new
  paper (= stage 20's P1 → P3). Optional accelerant: an arXiv posting of
  the **revised, calibrated** manuscript at resubmission time — permitted
  by IEEE policy — strictly after the IP screen and advisor sign-off.
- **Fallback [REC]: modified Route D.** If the anomaly stays open past
  its gate, die supply fails, or the SENSL invitation is confirmed
  lapsed: IP-screened arXiv preprint of a **strengthened,
  honestly-uncalibrated** version (never the rejected version verbatim),
  with all experimental effort directed at the RSI study.
- **Not recommended:** the literal user route (rejected version to arXiv
  now, skip SENSL). It permanently publishes a version with documented
  defects, leaves zero peer-reviewed output until ~mid-2027, and triggers
  the IP gate earliest for the least benefit.
- **RSI-specific criterion (stage-70 verified from the archived official
  policy page):** *"A previously published instrument is not considered
  to be novel"* — the RSI paper must present the vector probe as a new
  instrument/technique, which the vector hardware + campaign-#2 data +
  full calibration methodology framing already does. Re-check the live
  RSI policy page before actual submission [GATE].
- The SENSL invitation has **no stated deadline**; whether it lapses is a
  costless editorial query for Tim/advisor [GATE].

## 4. Minimum next experiment

All from [`04_HSX_EXPERIMENT_PLAN.md`](04_HSX_EXPERIMENT_PLAN.md) — bench
only, zero cleanroom, ≈19–29 bench/desk-days total (+2–3 if die packaging
is needed), campaign-independent by design [PX throughout]:

1. **B-01 anomaly closure first — hard rule.** The ~109× emulator
   magnitude anomaly carries the project's own "don't calibrate yet"
   instruction [SF]. A ΔV gain check (known ~1 mV differential injection;
   ΔV_out/ΔV_in = G, target 100.3 ± 1%) closes it. **No calibration work
   starts before this.**
2. **A-group supplied-data analyses (start immediately, need nothing):**
   exact shot recount, operational-repeatability statistics, quantified
   diamagnetic-loop correlation + measured DAQ offset, bias-scaling
   check, in-situ noise floor, figure regeneration — the cheapest
   credibility wins available, and the G1-fail hedge.
3. **WP-C calibration core:** Helmholtz build with triangulated coil
   constant (u(k)/k ≤ 2%,
   [S0051](https://doi.org/10.5194/jsss-9-391-2020) as the traceable-
   calibration norm); bipolar DC calibration (m ± ~2% absolute, <0.5%
   linearity); GUM/Monte-Carlo budget
   [S0220](https://doi.org/10.3390/s25051633); Allan-variance drift
   [S0168](https://doi.org/10.1109/TIM.2007.908635) [EE].
4. **C-03 voltage-bias S_v on the deployed die** — the 2025 data was
   taken with the 2023 voltage-bias G=200 chain, so the retroactive
   tesla conversion of Fig. 5 needs a distinct voltage-bias-mode
   calibration of the same physical die. This makes **I-4 (where is the
   deployed 2025 module, and is it functional?) the single most
   consequential open inventory question** [GATE].
5. **WP-B repeatability:** ≥3 packaged dies (the AE's own number) with
   within-die/between-die variance separation
   [S0218](https://doi.org/10.3390/jsan2010085); if only one die exists,
   the honest, AE-sanctioned single-device fallback with literature
   statistics [S0004].
6. **B-03/B-04 bandwidth with stated evidentiary basis** (measured /
   derived — the asserted 1 MHz figure is retired)
   [S0076](https://doi.org/10.1063/1.3246785).
7. **Upside, not required:** campaign #1 coil-only absolute anchor
   against the computed vacuum field at a surveyed pose (the [S0143]
   paradigm); the ~185× bench-to-machine field extrapolation is a named
   limitation until an in-machine anchor or borrowed electromagnet closes
   it.

## 5. 24-month graduation strategy

Full detail: [`06_24_MONTH_PHD_ROADMAP.md`](06_24_MONTH_PHD_ROADMAP.md)
and [`06_MILESTONES.csv`](06_MILESTONES.csv) (44 dated milestones with
owners, dependencies, slip triggers, and fallbacks).

- **The critical path never requires HSX campaign success:** inventory →
  anomaly closure → calibration → P1 draft → IP screen → P1 resubmission
  (~Nov 2026) → P1 acceptance (~Jan 2027 window) → P2 (hybrid
  architecture, drafted in parallel with P1 review) → dissertation
  chapters → reading committee (year 3) → oral exam/defense (Q2 2028) →
  submission (Q3 2028). Committee timing is anchored to Stanford EE's
  official pages (reading committee in year 3; University Oral Exam in
  year 4 — verified 2026-07-25) [EE].
- **Minimum viable graduation = P1 + P2 accepted** — a two-paper floor
  that exists entirely on bench work + already-collected data. The
  vector-probe chapter degrades honestly to a bench-validated module
  with the campaign gap stated as a limitation.
- **Upside plan = P1 + P2 + P3 (RSI)** with campaigns #1 (realistic:
  Sep 2026) and #2 (Nov 2026, slip limit ~Feb 2027) succeeding; P3
  upside submission ~Mar 2027, realistic window extending into 2027–28.
- **Dated decision points, not drift:** M28 (MVG-vs-upside checkpoint,
  Q1 2027) and G5 (direction gate, month 12 ≈ Jul 2027: ≥1 first-author
  paper accepted/in revision AND real-die absolute calibration achieved,
  else pivot to OPT3).
- **Honesty flags the roadmap itself carries:** the stated Aug-2026
  campaign-#1 target is very tight (~3 weeks from the mission date);
  fallback F1 absorbs the slip. The one scenario without a fully
  pre-planned fallback is a second P1 decline **plus** a P2 failure —
  named in roadmap §8, not hidden.

## 6. Startup preparation

Full detail: [`06_STARTUP_READINESS.md`](06_STARTUP_READINESS.md). Scope
per MISSION.md: research-strategy framing only — no investment,
incorporation, fundraising, or immigration advice.

- **The PhD itself is the primary preparation:** OPT2 graduates Tim with
  the complete system-competence stack of an instrumentation founder —
  device handling, packaged-sensor qualification, precision analog
  readout, calibration/traceability methodology, estimation software
  (stage 20 §9). Durable ownable assets: calibration infrastructure,
  firmware, demod/fusion codebase, qualification datasets.
  Harsh-environment magnetometry demand outside fusion is documented in
  the ledger (e.g. the AMR flight-qualification lineage
  [S0227](https://doi.org/10.1007/s11214-025-01170-w)) [EE].
- **Two discovery rounds** (~1 day/month, never competing with the
  critical path): open discovery Sep–Dec 2026 (M41); evidence-informed
  discovery + written technical-validation summary Jun–Dec 2027 (M43),
  after P1/P2 exist so the conversation is concrete.
- **Plan around thin IP** as the realistic case (stage 50's screen), with
  any narrow filing as upside. Sponsor-rights and ownership questions
  (DOE/SLAC, NSF NNCI, TomKat, SU-18, UW/WARF) are OTL/counsel questions,
  deliberately left open.
- **Go/no-go evidence memo before the defense (M44):** market signal,
  technical status, IP status, personnel question, funding path — a dated
  record, not a decision.

## 7. Pre-publication IP hold and professional-review gates

Full detail: [`05_DISCLOSURE_HOLD_CHECKLIST.md`](05_DISCLOSURE_HOLD_CHECKLIST.md)
and [`05_CANDIDATE_PROTECTABLE_CONCEPTS.md`](05_CANDIDATE_PROTECTABLE_CONCEPTS.md)
(research screen — not legal advice, no patentability conclusion).

- **Hard gate G-C [SF, advisor's own condition]:** no arXiv posting —
  and by extension no talk, poster, public repo, or demo (G-D/G-F/G-G) —
  before the advisor + Stanford OTL pre-disclosure screen concludes.
  arXiv is permanent and irrevocably licensed; it is the single most
  consequential disclosure event on the board.
- **Sequence:** preserve the dated record (checklist §1, including the
  deployed module's custody, I-4) → advisor conversation (checklist §2)
  → OTL screen (§3) → counsel questions (§4) → only then release the
  disclosure gates in order. The July UW e-mail (G-A) is the earliest
  third-party disclosure and needs an advisor confidentiality decision
  first.
- **Six screened concepts (CC-1..CC-6)**, ranked by maturity × urgency:
  the P1 revision itself discloses CC-1/CC-2/CC-5/CC-6 nearly completely,
  so whatever review happens must happen before resubmission. Expected
  outcome, stated in advance: prior-art density is high (the group's own
  2019 papers, active Infineon/TI spinning-current families, fresh 2025
  Kalman-fusion art [S0118](https://doi.org/10.1088/1741-4326/adb599),
  [S0122](https://doi.org/10.1016/j.fusengdes.2025.115180)), so **any
  protectable scope is likely thin and combination-specific; "nothing to
  file" is a legitimate, plausible outcome** — the screen's value is that
  the decision is made deliberately before disclosure.
- **Flag for counsel:** parts of CC-4/CC-6 method text are AI-assisted
  planning output; inventorship treatment is an evolving legal question
  the screen lists, not answers.

## 8. Key uncertainties, reversal triggers, and contingency plan

**Standing limitations (carried verbatim-in-substance from the red team,
[`07_RED_TEAM.md`](07_RED_TEAM.md) §3):**

1. The novelty anchor is an **absence finding** from bounded searches —
   strong, three-lane-independent, still not proof of priority.
2. **32% of ledger rows are metadata-only:** no specific number from a
   non-full-text row enters any manuscript without primary-PDF
   confirmation.
3. **Provider-level independence was not achieved** (Claude-only
   package; the red team was method-independent, not
   provider-independent).
4. **Live-page gaps:** RSI policy verified via an ~8-month-old archived
   copy of the official page; the SENSL invitation-lapse question is
   open.
5. **The open technical gates are bench/human work, not analysis:**
   ~109× anomaly (C017/G1), deployed-module custody (I-4), die supply
   (advisor decision 3), UW co-located records (U-1), campaign windows
   (U-9/G4).

**Named reversal conditions (stage 20 §11 — each falsifies part of the
verdict):**

| # | Trigger | Response |
|---|---|---|
| 1 | A peer-reviewed GaN/AlGaN Hall deployment in any confinement device predating Tim's surfaces | First-in-class claims die; P1 reframes as qualification/architecture work; re-run the scorecard |
| 2 | The real die cannot be absolutely calibrated to a stable coefficient by G5 | The finished-calibration premise fails; pivot to OPT3 per G5 |
| 3 | HSX access is lost entirely | OPT3 (software/methods on whatever archive exists) becomes the rational thesis |
| 4 | The advisor declines WP-D/system scope | Revert to OPT1 as scored (rank 2, viable but schedule-concentrated) |
| 5 | A stellarator Hall+coil fusion study surfaces | WP-D loses "first," retains HSX-specific value; P2 reframes as comparative/validation |

**Contingency ladder (operational):** G1 fail → P1 re-scoped around
A-group + WP-A + bandwidth while the chain is fixed; G2/campaign-#1 slip →
fallback F1 (P1 unaffected); G3 bond-yield fail → 2-axis probe (still
publishable); G4/campaign-#2 slip past ~Feb 2027 → fallback F2 (P3
descopes, P2 is the second paper); G5 fail at month 12 → pivot to OPT3 on
the data pipelines and UW relationship WP-D builds anyway; P1 declined
again → alternate sensors-class venue or the strengthened (never
rejected-version) arXiv route.

**Operational observations for the user (not research findings):**

- Two launcher-telemetry artifacts documented by the red team: stage-era
  timestamps written as UTC with a −07:00 label (F-10), and a
  packed-notes `security_fallback_flag=True` on stage 30 that primary
  stream evidence refutes (F-11). This stage verified the same
  notes-string pattern appears on the stage-70 row and re-checked the
  stage-70 raw stream directly: Fable init, Fable final main message —
  no fallback occurred. The launcher's notes-string derivation is worth
  a look if its telemetry is ever relied on alone.
- The original request's automatic Codex/MCP fallback and 20-minute
  auto-switch were **deliberately not implemented** (documented
  deviations C3/C4; manual ChatGPT continuation only). Surfaced here per
  the conflict ledger, not silently absorbed.
- The parent-project memory's "2023, published" framing (C1) is outside
  this mission's write access and should be corrected by Tim.

## 9. Where to go next

The concrete sequence, owners, gates, and dates are in
[`FINAL_ACTION_PLAN.md`](FINAL_ACTION_PLAN.md). The advisor meeting is the
single highest-leverage next act: its seven decision items
([`06_ADVISOR_MEETING_BRIEF.md`](06_ADVISOR_MEETING_BRIEF.md) §1) unblock
the die supply, the UW e-mail, the IP screen, and the venue route — every
long-shadow dependency in the plan.
