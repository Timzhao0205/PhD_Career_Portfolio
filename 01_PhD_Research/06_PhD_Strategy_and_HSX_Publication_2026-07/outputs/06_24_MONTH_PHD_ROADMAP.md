# 06 — 24-month PhD roadmap: late July 2026 → summer 2028 (Stage 60)

Prepared by: Claude Code, stage `60_timeline`, requested model Sonnet 5 /
High (non-Fable stage; no downgrade-enforcement applies). Basis: the
validated stage 20 direction decision
([`02_RESEARCH_DIRECTION_DECISION.md`](02_RESEARCH_DIRECTION_DECISION.md),
OPT2, work packages WP-A/B/C/D, P1/P2/P3 windows, gates G1–G5), the stage
30 publication-route decision
([`03_PUBLICATION_ROUTE_DECISION.md`](03_PUBLICATION_ROUTE_DECISION.md),
route A→C), the stage 40 experiment plan
([`04_HSX_EXPERIMENT_PLAN.md`](04_HSX_EXPERIMENT_PLAN.md), gates
G0/G1/G-cal/G-die/G2/G3/G4, inventory gates I-1..I-9, UW gates U-1..U-9),
the stage 50 disclosure gates
([`05_DISCLOSURE_HOLD_CHECKLIST.md`](05_DISCLOSURE_HOLD_CHECKLIST.md),
G-A..G-H), the stage 00 conflict ledger
([`00_CONFLICT_LEDGER.md`](00_CONFLICT_LEDGER.md), standing corrections
C1/C6), and the milestone register built alongside this document
([`06_MILESTONES.csv`](06_MILESTONES.csv), rows M01–M44, cited below as
`Mxx`). Two external web lookups (WebSearch + WebFetch, Stanford EE
"Graduate Degree Progress" pages, accessed 2026-07-25) ground the
committee/defense timing; every other date is derived from the mission's
own gate logic, not invented. *[Stage-70 correction: the lookup URLs were
omitted here originally; the claims were independently re-verified
2026-07-25 against the official pages — reading committee in year 3:
[ee.stanford.edu/academics/graduate-degree-progress](https://ee.stanford.edu/academics/graduate-degree-progress);
University Oral Examination in year 4:
[ee.stanford.edu/academics/graduate-degree-progress/oral-exam](https://ee.stanford.edu/academics/graduate-degree-progress/oral-exam).]* Epistemic labels follow the mission
convention: **[SF]** supplied fact, **[EE]** external evidence, **[INF]**
inference, **[REC]** recommendation, **[PX]** proposed experiment,
**[GATE]** unresolved gate.

**Standing corrections honored (conflicts C1/C6):** the manuscript is a
**declined, unpublished** 2026 submission with an invitation to revise and
resubmit — not "the 2023 published paper." The 2026 readout's "calibrated"
language is **aspirational**; the only demonstrated result is
emulator-based offset cancellation with the ~109× anomaly open. No date
below assumes either correction away.

**No immigration or legal claims appear anywhere in this document.**
International-student status is treated, per `MISSION.md`, as a scheduling
and career constraint only: it favors the on-schedule two-paper floor and
transferable system-competence skills (stage 20 §9), and nothing here
offers visa, work-authorization, or legal guidance. Any question of that
kind belongs with Stanford's international-student office and immigration
counsel, not this mission.

---

## 1. Ground truth this roadmap starts from

- **Today:** 2026-07-25 [SF]. Tim begins his third PhD year in Fall 2026
  and wants to graduate in about two years — i.e., by roughly **summer
  2028** [SF, `../inputs/ORIGINAL_REQUEST.txt`].
- **Zero accepted first-author papers exist today** [SF, stage 20 §0]. The
  single manuscript in hand was declined 2026-07-23 with an invitation to
  revise and resubmit under a new Manuscript ID [SF, decision letter].
- **The direction verdict (stage 20):** continue the GaN Hall
  magnetic-diagnostics direction with the OPT2 adjustment — a finished,
  absolutely calibrated sensing output as the non-negotiable centerpiece,
  plus four campaign-uncoupled work packages (WP-A comparison table, WP-B
  multi-die repeatability, WP-C calibration + uncertainty budget, WP-D
  hybrid Hall+inductive fusion) [SF, `02_RESEARCH_DIRECTION_DECISION.md`
  §1–§3].
- **The venue route (stage 30):** revise-and-resubmit to IEEE Sensors
  Letters (**Route A**) once the bench package closes, then the RSI
  vector-probe instrument study (**Route C**) on the next campaign; an
  optional arXiv posting of the *revised* manuscript is permitted at
  resubmission time, strictly after the IP screen [SF,
  `03_PUBLICATION_ROUTE_DECISION.md` §0, §6].
- **The experiment plan (stage 40):** every P0 reviewer item is
  bench-satisfiable; the HSX campaign is upside, not a single point of
  failure; total bench/desk effort to a submittable Tier-1 (SENSL) package
  is **≈19–29 bench-days** (stage-70 corrected sum; +2–3 more if die
  packaging is needed), with zero cleanroom work anywhere in the plan
  [SF, `04_HSX_EXPERIMENT_PLAN.md` §1, §12].
- **The disclosure gates (stage 50):** the advisor's own condition — an IP
  screen before any arXiv posting — is a hard gate (G-C); six candidate
  concepts (CC-1..CC-6) are ranked by evidence maturity and disclosure
  urgency, with CC-2 (readout chain) and CC-1 (packaging stack) most
  urgent because the P1 manuscript discloses them first [SF,
  `05_CANDIDATE_PROTECTABLE_CONCEPTS.md` §0].
- **A schedule reconciliation this stage performs [REC]:** stage 20's P3
  window (months 12–24 ≈ Aug 2027–Aug 2028) and project 03's own "~March
  2027" RSI-submission target both derive from the same Nov-2026
  campaign-#2 date with a ~Feb-2027 slip limit for "P3-as-planned." This
  roadmap shows both: **Mar 2027 as the upside case** (M29) if campaign #2
  lands near its stated Nov-2026 target, and **a later, realistic/MVG
  window extending into 2027–2028** (M30, M35) if it does not — exactly
  the ambiguity stage 30 handed forward for stage 60 to resolve
  (`03_PUBLICATION_ROUTE_DECISION.md` §7).
- **A schedule-honesty flag [REC]:** the stage-40 target for HSX campaign
  #1 is **August 2026** [SF, U-9/C018] — about three weeks from today. The
  pre-ship dependency chain (anomaly closure → calibration →
  module-health check) makes that target very tight; §3 below shows both
  the stated target and a realistic case sliding into September 2026. The
  existing fallback (F1: "P1 is bench-only and unaffected") absorbs this
  slip without damaging the graduation-critical path.

---

## 2. Critical path and parallel workstreams

### 2.1 The single critical path to graduation

The shortest chain of dependencies that **must** all succeed for an
on-schedule defense is:

```
G0 inventory (M05) -> B-01 anomaly closure / G1 (M06) -> WP-C calibration
(M08-M10) -> P1 draft (M14) -> IP screen (M13) -> P1 resubmission (M18)
-> P1 review (M20) -> P1 acceptance (M26) -> P2 draft/submit (M27) ->
P2 acceptance (M31) -> dissertation Ch.1-4 (M36) + Ch.5,7 (from M37) ->
reading committee (M32) + candidacy (M33) -> TGR (M38) -> oral exam/
defense (M39) -> dissertation submitted (M40)
```

This path **never requires the HSX campaign to succeed** [REC — this is
the structural improvement OPT2 buys over OPT1, stage 20 §3.2].
*[Stage-70 clarification: the `M26 -> M27` arrow above shows the
acceptance sequence of the two-paper floor, not a work dependency —
in `06_MILESTONES.csv` M27 (P2 drafting) depends only on M17/M23 and
proceeds in parallel with P1's review, exactly as §3's January-2027
entry describes.]* Campaign
#1 (M16), the vector probe (M21–M22), campaign #2 (M25), and the RSI paper
(M29/M30/M35) are all **parallel upside workstreams** that feed a stronger
dissertation and a third paper, but a slip in any of them degrades the
*upside* plan (§7.2), not the minimum-viable one (§7.1).

### 2.2 Parallel workstreams and their relationship to the critical path

| Workstream (CSV tag) | Feeds the critical path? | Role |
|---|---|---|
| BENCH-CAL (WP-C) | **Yes** | On the critical path — P1 cannot claim calibration without it |
| REPEAT (WP-B) | **Yes** | On the critical path — AE explicitly required repeatability evidence |
| ANALYSIS (A-group, WP-A) | **Yes**, but lowest-risk | Needs nothing but the immutable 2025 archive; start immediately |
| P1-MANUSCRIPT | **Yes** | The critical-path spine |
| IP-DISCLOSURE | **Yes** (as a gate) | Blocks P1 resubmission and any arXiv posting — cannot be skipped |
| CAMPAIGN-1 | No (upside) | Feeds WP-D data and the in-situ anchor; P1 does not depend on it |
| WPD-ARCH (P2) | **Yes** (for the MVG floor) | The second paper of the stage-20 two-paper floor; degrades gracefully without campaign data |
| VECTOR-HW / CAMPAIGN-2 / P3-MANUSCRIPT | No (upside) | The RSI capstone; genuinely optional for graduation, core to the "stronger upside" plan |
| DISSERTATION | **Yes** | Committee/registration process runs in parallel with research from month 1 |
| STARTUP | No | Explicitly designed to never gate a research milestone (06_STARTUP_READINESS.md) |

**Implication [REC]:** if time or resources become scarce, cut from
CAMPAIGN-2/VECTOR-HW/P3 first (§7.1's minimum-viable-graduation plan), not
from BENCH-CAL/REPEAT/ANALYSIS/P1/P2/DISSERTATION.

---

## 3. Month-by-month detail — first six months (Aug 2026 – Jan 2027)

### August 2026 — inventory, anomaly closure, analysis kickoff

- Advisor decision batch #1 (M02) and the UW e-mail (M03, gate G-A) open
  the month — both are prerequisites for almost everything downstream
  (die supply, UW data access, campaign authorization).
- A-group supplied-data analyses (M04) and the WP-A comparison table
  (M07) start immediately — they need nothing but files already in hand
  and are the cheapest credibility wins in the entire plan [SF,
  `04_HSX_EXPERIMENT_PLAN.md` §4.0].
- G0 inventory gates close (M05); the ~109× anomaly closure (M06, gate
  G1) is the month's single highest-priority bench task — **no
  calibration work starts before it** [REC — hard rule inherited from
  stage 40 §1].
- Advisor + OTL pre-disclosure conversation opens (M13) — it must
  conclude before the P1 draft (M14) can be resubmitted, so starting it
  in parallel with bench work, not after, is what keeps it off the
  critical path's tail.
- Campaign-#1 pre-ship work begins (M15); the stated Aug-2026 target
  (U-9/C018) is tight against this chain — realistic execution slides
  into September (§1's honesty flag).

### September 2026 — calibration core, repeatability, campaign #1, vector build starts

- WP-C calibration core: field-source build (M08), DC calibration +
  uncertainty budget (M09), voltage-bias S_v for the retroactive 2025
  conversion (M10) — this is the month's spine.
- WP-B repeatability (M11) runs in parallel — it needs the die-supply
  decision (M02) but not the calibration bench.
- Characterization suite — bandwidth, noise, hysteresis, temperature,
  drift, parasitics (M12) — starts once C-02 exists.
- Campaign #1 executes (M16, realistic window) — coil-only anchor +
  shot matrix, if the UW gates (U-1..U-9) and pre-ship health check
  clear.
- Vector-probe cube build starts (M21, gate G3) — this is on the
  campaign-#2 critical path (not the graduation critical path), so
  starting it now rather than after P1 ships keeps the RSI upside alive
  without slowing P1.
- Dissertation reading committee formation opens (M32) — pure
  administrative parallel track; start it now because Stanford EE's own
  guidance places it in year 3, which is exactly this quarter [EE].

### October 2026 — P1 drafting, vector calibration, WP-D development

- P1 full draft (M14) — the month's central task, integrating every
  bench result from August–September.
- Vector-probe matrix calibration (M22) continues; WP-D algorithm
  development on synthetic + 2025 data (M17, started September) continues
  in parallel — this is software-heavy, desk-based work that does not
  compete for bench time with M08–M12.
- IP screen (M13) should conclude by month's end — it is the hard gate
  on both P1 resubmission and any UW-facing disclosure of CC-3/CC-5
  specifics.

### November 2026 — P1 resubmission, optional arXiv, campaign #2 window opens

- P1 resubmission to IEEE Sensors Letters (M18) — contingent on the IP
  screen (M13) being closed; if it is not, this slips, not the reverse
  (advisor's explicit condition, §1).
- Optional arXiv posting of the revised manuscript (M19, gate G-C) — only
  with documented advisor + OTL sign-off.
- Campaign #2 pre-ship (M24) and the HSX deployment itself (M25, gate G4)
  open their window — stated target is Nov 2026, hard slip limit ~Feb
  2027 for "P3-as-planned" (§1's reconciliation).
- WP-D validation against campaign-#1 data (M23) begins, contingent on
  what U-1 revealed about co-located coil records.

### December 2026 — review cycle, campaign-#2 continuation, committee filing

- SENSL review cycle (M20) is now underway — timeline is journal-
  controlled, not something this plan can accelerate.
- Campaign #2 continues through its Nov-2026–Feb-2027 window (M25).
- Dissertation reading committee (M32) target-completes this month.
- Startup discovery round 1 (M41) runs quietly in the background — ~1
  day/month, never competing with the above for bench or writing time.

### January 2027 — P1 acceptance track, P2 drafting begins, candidacy opens

- P1 acceptance decision expected in this window (M26) — first
  first-author accepted paper, if the review cycle is consistent with the
  journal's stated "Submission-to-ePublication = 4.8 weeks, median"
  statistic [EE, `03_PUBLICATION_ROUTE_DECISION.md` §4.1; stage-70
  correction: this figure is the journal's submission-to-ePublication
  median, not a post-acceptance interval — the M18→M26 window already
  budgets ~2–4× that median for re-review].
- P2 (hybrid-architecture) draft begins (M27), building on M17/M23.
- Candidacy/course-requirement confirmation opens (M33) — parallel
  administrative track.
- If campaign #2 landed near its stated target, P3 upside drafting (M29)
  begins this month too.

---

## 4. Quarterly detail — months 7–24 (Feb 2027 – Jul 2028)

### Q1 2027 (Feb–Apr 2027)

- MVG-vs-upside checkpoint (M28) — an explicit, dated decision, not a
  drift: once campaign #2's actual status (on schedule, slipped, or
  failed) is known, Tim and the advisor jointly commit to either the
  minimum-viable-graduation plan (§7.1) or continue chasing the 3-paper
  upside (§7.2).
- P2 submission (M27 target) and, in the upside case, P3 draft/submission
  (M29) both land in this window — this is the plan's busiest writing
  quarter; the buffer described in §8 exists precisely because of this
  clustering.
- Direction gate G5 approaches (M34, targeted ~Jul 2027) — begin
  assembling its two required conditions (an accepted/in-revision
  first-author paper, and real-die absolute calibration) now rather than
  scrambling in June.

### Q2–Q3 2027 (Apr–Sep 2027)

- P2 review/acceptance (M31) — completes the stage-20 minimum-viable
  two-paper floor if it lands.
- In the realistic/fallback case, P3's descoped draft (M30) is written
  here instead of the upside-case M29 draft.
- Direction gate G5 (M34) executes at month 12 (~Jul 2027) — the
  stage-20-mandated checkpoint on whether to continue OPT2 or pivot
  toward OPT3 (stage 20 §8/§11).
- Dissertation chapters 1–4 drafting begins (M36) — these chapters are
  largely P1-paper content repackaged, so they are the lowest-risk
  writing and should not wait for P2/P3 to finish.
- Startup discovery round 2 + technical-validation summary (M43) starts,
  informed by P1/P2's actual results rather than speculation.

### Q4 2027 – Q1 2028 (Oct 2027 – Mar 2028)

- P3 review/acceptance, upside case (M35) — the third first-author paper,
  if the earlier upside branch was taken.
- Dissertation chapters 5–7 (M37) — hybrid architecture, vector-probe/
  campaign-2 chapter (in whichever form — full instrument study or
  bench-validated-module-plus-future-work), conclusions and outlook.
- TGR status requested (M38) once residency, candidacy, and the reading
  committee are all in place.

### Q2 2028 (Apr–Jun 2028)

- University Oral Examination / defense (M39) — Stanford EE's own stated
  norm places this in year 4, which for a Fall-2026 year-3 start lands
  exactly in this window [EE].
- Collaborator-boundary and go/no-go startup review (M44) — completed
  before the defense, not after, so it reflects the actual (not
  aspirational) IP and publication status.

### Q3 2028 (Jun–Jul 2028)

- Dissertation submission and degree conferral (M40) — administrative
  buffer already built into the M39→M40 gap.
- **This is the ~2-year-from-now graduation target the user asked for**,
  and it is also, per the external evidence in §1, close to Stanford EE's
  own typical year-4 defense timing — i.e., the accelerated-sounding ask
  is actually close to the department's normal cadence for a student who
  is not behind on committee milestones, not a compression relative to
  it [EE + INF].

---

## 5. HSX/bench campaign preparation, data analysis, manuscript sequence, dissertation chapters, committee gates, and buffer — cross-reference table

| Category | Milestones (CSV IDs) | Buffer built in |
|---|---|---|
| Bench campaign prep | M05, M06, M08–M12, M15, M24 | ~2–3 bench-days of slack per block per stage-40 §12.1 estimates |
| Data analysis | M04, M07, M17, M23 | None needed — desk-only, lowest risk |
| Manuscript sequence | M14, M18–M20, M26 (P1); M27, M31 (P2); M29/M30, M35 (P3) | Review-cycle duration is journal-controlled (M20); the Q1 2027 clustering (§4) is the plan's tightest point |
| Dissertation chapters | M36 (Ch.1–4), M37 (Ch.5–7) | ~1 month slack in each chapter block before the M38 TGR gate |
| Committee/advisor gates | M02, M28, M32, M33, M34, M38, M39 | Reading committee (M32) deliberately starts in month 1–4, far ahead of the M38 TGR need |
| Explicit buffer | Q3 2028 (M39→M40 gap, §4) | ~2 months between defense and submission for formatting/administrative delay |

---

## 6. Low-cleanroom allocation and what to avoid

Per the stage-20 direction decision (§7) and stage-40 experiment plan
(§12.2), **zero cleanroom steps appear anywhere in this roadmap** [SF]:

- The die is the established AlGaN/GaN Hall cross from the group's
  published lineage; gen-2's larger bond pads are a packaging-layout
  change, not a device innovation.
- Everything device-adjacent in M11/M21 (packaging, wedge bonding, EPO-TEK
  encapsulation, vacuum bake, ceramic-cube machining) is **assembly-lab**
  work, reusing the proven 2023 process verbatim — not cleanroom
  fabrication.
- **What to avoid [REC]:** any new epitaxy, new mask sets beyond the
  pad-size change, any device-topology escalation (the rejected OPT4
  path, stage 20 §3.4), and — per the mission's fixed scope rule — any
  neutron/gamma radiation experiment. Radiation stays literature/TCAD
  outlook only, cited at most as a sentence, never as Tim's own
  experimental work (parent `CLAUDE.md` scope rule; M37's dissertation
  guidance restates this explicitly).
- The heaviest hardware task in the whole 24 months is hand-assembling
  vector-probe board copies (M21) — and that is upside/RSI scope (§7.2),
  not required for the minimum-viable plan (§7.1).

---

## 7. Minimum viable graduation plan and stronger upside plan

### 7.1 Minimum viable graduation (MVG) plan

**Structure:** P1 (SENSL, accepted) + P2 (hybrid-architecture paper,
accepted) = the stage-20-defined **minimum-viable two-paper floor**
[SF, `02_RESEARCH_DIRECTION_DECISION.md` §6]. Neither depends on the HSX
campaign succeeding. The dissertation's vector-probe chapter (Ch.6, M37)
is written around the **bench-validated vector module and design** rather
than a completed in-vessel instrument study, with the campaign-#2 gap
stated as an explicit limitation and future-work item — never hidden.

**What triggers committing to this plan [REC]:** the MVG-vs-upside
checkpoint (M28) is the formal decision point; the concrete trigger is
campaign #2 (M25) slipping past its ~Feb-2027 hard limit (fallback F2,
stage 20 §8), or the direction gate G5 (M34) failing one of its two
conditions.

**What it requires that is not yet guaranteed:**
- The anomaly (M06/G1) must close — without it, no calibration claim
  exists and P1 cannot make the finished-study claim the AE demanded.
- The die-supply decision (M02, advisor decision #3) must yield at least
  the honest single-device fallback path (§7.3 of
  `04_HSX_EXPERIMENT_PLAN.md`) for WP-B.
- P2 must clear its own novelty risk — fresh 2025 Kalman-fusion
  literature (PA-N19/N20) is the field's own answer to "has this been
  done," and stage 20 §11 already names this as a reversal condition to
  watch.

**Defense readiness under MVG:** M39 explicitly allows defending on
P1+P2 with a bench-validated-module framing for the vector-probe
material — this is a **defensible thesis**, not a degraded one; it is
exactly the two-paper floor stage 20 scored as achievable "entirely on
bench + already-collected data."

### 7.2 Stronger upside plan

**Structure:** P1 + P2 + P3, all accepted, with campaign #1 and campaign
#2 both succeeding close to their stated targets (M16, M25). The
dissertation gains a full instrument-study chapter (RSI genre: calibrated
vector probe, uncertainty budget, in-situ validation) rather than a
descoped one. IP screening (M13, M24) may surface something OTL considers
worth a provisional filing — stage 50 found the prior-art density high
enough that any protectable scope is expected to be thin, so this is
described as possible, not likely [SF, `05_CANDIDATE_PROTECTABLE_CONCEPTS.md`
§0, §7]. Startup readiness work (M41–M44) has a materially stronger
evidence base to draw on: a completed calibrated instrument, a quantified
hybrid-architecture result, and (if campaign #2 lands) a full vector-probe
demonstration — see `06_STARTUP_READINESS.md` §5 for what "stronger
evidence base" means concretely.

**What it requires beyond the MVG plan:** everything in §7.1, plus
campaign #2 landing within its window (M25), the vector-probe hardware
build succeeding at ≥2 axes (M21, gate G3 — the 2-axis fallback is itself
still publishable), and P3 clearing RSI's "not previously peer-reviewed"
duplication rule against P1/P2 content (M35).

**Relationship between the two plans [REC]:** they are not a fork taken
once — they are the *same* critical path (§2.1) with the upside plan
adding parallel workstreams on top. Nothing in §7.2 competes for the
critical-path resources that §7.1 needs; the only real trade-off is Tim's
personal time and attention, which M28's explicit checkpoint exists to
manage deliberately rather than by drift.

---

## 8. Decision points if HSX access, hardware, calibration, repeatability, or publication review slips

| Slip scenario | Detection point | Decision | Fallback already defined | Effect on graduation date |
|---|---|---|---|---|
| **HSX access** (campaign #1 or #2 cannot happen at all) | U-9 unconfirmed by ~Sep 2026 (campaign 1) or M25 fails entirely (campaign 2) | Advisor + Tim (M28-style checkpoint) | Fallback F1 (campaign 1): P1 unaffected, bench-only by design. Fallback F2 (campaign 2): P3 descopes to bench-validated module (04_HSX_EXPERIMENT_PLAN.md §8) | **None** if only campaign 2 is lost (MVG plan, §7.1); **material risk** if HSX access is lost entirely — this is stage-20's named reversal condition 3 (§11), which would push the whole direction toward the OPT3 fallback |
| **Hardware** (die supply insufficient, bond yield fails, board fault) | M02 (die-supply decision) or M05/M21 (inventory/build gates) | Tim + advisor | Single-device WP-B fallback (§7.3 of the experiment plan); 2-axis vector-probe fallback (gate G3) | None for MVG; upside plan's vector-probe chapter becomes 2-axis instead of 3-axis |
| **Calibration** (the ~109× anomaly does not resolve) | M06 (gate G1) | Tim + advisor — board fault-isolation sprint | P1 re-scoped around A-group + WP-A + bandwidth only, calibration claim dropped (04_HSX_EXPERIMENT_PLAN.md G1-fail branch) | **Material risk to the critical path** — this is the single highest-leverage failure mode in the whole plan, because P1, P2's WP-D validation, and the entire tesla-denominated claim set all sit downstream of it |
| **Repeatability** (only 1 die, no packaging path) | M02/M05 (I-5) | Tim + advisor | Honest single-device fallback: report remount repeatability as operational, cite literature (S0004/S0218) for population statistics — the AE explicitly allows this route | None — this is a pre-planned, AE-sanctioned degradation, not an improvised one |
| **Publication review** (P1 or P2 declined a second time) | M20/M26 (P1); M27/M31 (P2) | Advisor escalation | P1: another Sensors-class venue, or a strengthened Route-D-style arXiv posting (03_PUBLICATION_ROUTE_DECISION.md §3.4/§6). P2: revise and resubmit; a P2 decline is flagged as a graduation-risk trigger because it is the MVG plan's second required paper | **Direct risk to the MVG floor** if P2 fails and no revision succeeds in time — the one scenario in this table with no fully pre-planned fallback, because it removes the plan's second paper rather than degrading a chapter |

---

## 9. Weekly operating rhythm and measurable progress indicators

### 9.1 Weekly operating rhythm [REC]

- **One fixed weekly checkpoint** (day/time chosen by Tim) reviewing: what
  closed this week against the active milestone(s) in
  `06_MILESTONES.csv`, what is blocked and on whom, and whether any
  `slip_trigger` condition has been hit.
- **Bench/desk time protected in blocks**, not interleaved hour-by-hour —
  the stage-40 burden estimates (§12.1) assume single-operator, serial
  bench work; context-switching between bench calibration and manuscript
  writing in the same day is a documented efficiency loss in that plan.
- **Advisor sync cadence:** at minimum, once per the gates in
  `06_ADVISOR_MEETING_BRIEF.md` (M02, M13, M28, M34) — not necessarily
  weekly, but never less often than monthly during the Aug–Dec 2026
  bench-and-campaign-dense period.
- **Startup workstream check-in:** monthly, ~1 day, deliberately
  lightweight (M41/M43) so it never competes with critical-path time.

### 9.2 Measurable progress indicators [REC]

| Indicator | How measured | Where tracked |
|---|---|---|
| Milestones closed vs. planned | Count of `status=complete` rows in `06_MILESTONES.csv` vs. rows whose `target_date` has passed | Weekly checkpoint |
| Bench-days consumed vs. the ~19–29 day Tier-1 estimate | Logged bench-days per session | Project 02 journal (existing practice) |
| Open gates | Count of unresolved I-/U-/G- gates from stage 40, and G-A..G-H from stage 50 | This roadmap's §1 + `05_DISCLOSURE_HOLD_CHECKLIST.md` |
| Papers in each state (drafting / submitted / in review / accepted) | P1/P2/P3 status | `06_MILESTONES.csv` P1-MANUSCRIPT / WPD-ARCH / P3-MANUSCRIPT rows |
| Dissertation chapters drafted vs. 7 planned | Chapter count | M36/M37 |
| Committee/registration milestones met on schedule | M32/M33/M38/M39 dates vs. actual | Weekly checkpoint |
| Direction-gate conditions (G5, M34) | Binary: accepted/in-revision paper? real-die calibration achieved? | Advisor sync |

---

## 10. Cross-references

- Milestone-level detail, dates, dependencies, owners, and fallbacks for
  every item named above: [`06_MILESTONES.csv`](06_MILESTONES.csv).
- Advisor-facing summary of the decisions this roadmap assumes get made
  early (M01–M03, M13, M28, M34): [`06_ADVISOR_MEETING_BRIEF.md`](06_ADVISOR_MEETING_BRIEF.md).
- Startup-preparation detail for the STARTUP workstream (M41–M44):
  [`06_STARTUP_READINESS.md`](06_STARTUP_READINESS.md).
- This document deliberately does not re-derive the direction, venue
  route, experiment design, or IP screen — it schedules them. Any
  disagreement between this roadmap's dates and the underlying technical
  content of stages 20/30/40/50 should be resolved in favor of those
  stages' technical content, with this document's dates adjusted
  accordingly.
