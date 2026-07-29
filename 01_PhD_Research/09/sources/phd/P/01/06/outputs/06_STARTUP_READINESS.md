# 06 — Startup-readiness preparation compatible with the PhD plan (Stage 60)

> **Scope note.** This document covers only preparation that fits inside
> the PhD plan in [`06_24_MONTH_PHD_ROADMAP.md`](06_24_MONTH_PHD_ROADMAP.md)
> and the STARTUP-tagged rows of [`06_MILESTONES.csv`](06_MILESTONES.csv)
> (M41–M44). It contains **no investment, fundraising, incorporation,
> valuation, term-sheet, or transaction instructions of any kind** — those
> are out of scope for this mission and are not research-strategy
> questions. It also contains no immigration or legal advice, consistent
> with `MISSION.md`'s treatment of international-student status as a
> scheduling constraint only. The user's stated goal is a startup around
> **2029/2030** [SF, `../inputs/ORIGINAL_REQUEST.txt`] — i.e., after the
> PhD, not during it; everything below is framed as pre-work that does not
> compete with the graduation-critical path (`06_24_MONTH_PHD_ROADMAP.md`
> §2.2).

---

## 1. Why this workstream is structured the way it is

Stage 20 found that the OPT2 research direction graduates Tim with a
**complete system-competence stack** — device handling, packaged-sensor
qualification, precision analog readout, calibration/traceability
methodology, and estimation software — which is the skill shape of an
instrumentation-company founder, achieved without betting the PhD on any
single market thesis [SF, `02_RESEARCH_DIRECTION_DECISION.md` §9]. That
finding sets this document's default posture: **the PhD itself is the
primary startup-preparation activity**; the items below are the
supplementary, low-time-cost pieces that make the post-PhD decision an
informed one rather than a cold start.

Every item below is tagged with its `06_MILESTONES.csv` row (M41–M44) and
its effort budget, all of which are deliberately small (~1 day/month or
less) so this workstream never competes with the critical path
(`06_24_MONTH_PHD_ROADMAP.md` §2.2 table).

---

## 2. Problem and customer discovery

**What [REC]:** informational conversations — not sales pitches, not
fundraising conversations — with people who work on harsh-environment or
fusion-adjacent magnetic sensing: national-lab and private fusion-company
instrumentation groups, industrial harsh-environment sensor users,
space-adjacent magnetometry teams (the AMR flight-qualification lineage
already in the source ledger, [S0227](https://doi.org/10.1007/s11214-025-01170-w),
is a documented existence proof that this demand class exists outside
fusion — evaluating the market itself is out of scope for this mission,
but the literature anchor is not invented).

**Two rounds, timed to have something real to discuss [REC]:**

1. **Round 1 (M41, Sep–Dec 2026): open discovery.** ≥10 conversations
   before any paper is out — the goal here is calibrating what problems
   this class of instrumentation actually solves for someone else, not
   validating a specific product. No confidential information is shared
   in either direction; no funding is discussed.
2. **Round 2 (M43, Jun–Dec 2027): evidence-informed discovery +
   technical-validation summary.** By this point P1 (and likely P2) have
   real results — the conversations can be concrete ("here is a
   calibrated GaN Hall sensor with a written uncertainty budget that
   survived in-vessel plasma exposure — is that useful to you and why or
   why not") instead of hypothetical.

**What this explicitly is not [REC]:** pitching, fundraising, discussing
equity, or making any commitment to a counterparty. If a conversation
partner wants to move toward any of those, that is outside this
workstream and outside this mission's scope — it becomes a personal
decision for Tim to make with appropriate counsel at the time, not
something this document plans for.

---

## 3. Technical validation

**What "technical validation" means here [REC]:** a written summary,
produced once real results exist (M43), of what the research has actually
demonstrated versus what remains aspirational — the same
supplied-fact/inference discipline this whole mission uses, applied to a
startup lens instead of a publication lens. Concretely, it should state,
with citations back to the dated evidence:

- What was measured (calibration coefficient + uncertainty budget from
  WP-C, repeatability statistics from WP-B, bandwidth/noise/drift
  characterization) versus what is still a target.
- What survived real deployment conditions (68 shots in-vessel, Aug 2025
  [SF]) versus what has only been bench-demonstrated.
- What the hybrid Hall+inductive architecture (WP-D/P2) actually adds,
  quantified — not asserted.
- Explicitly labeled gaps (e.g., the ~185× bench-to-machine field
  extrapolation, `04_HSX_EXPERIMENT_PLAN.md` §8) — a technical-validation
  summary that hides its own gaps is worse than none, for exactly the
  reason the AEIC's decline letter identified in the first manuscript.

**Why this is scheduled after P1/P2 land, not before [REC]:** doing this
exercise on pre-calibration data would just reproduce the AEIC's novelty
and evidence objections in startup form. The PhD's own bench-package
timeline (`06_24_MONTH_PHD_ROADMAP.md` §3) is what makes this summary
credible when it is finally written.

---

## 4. IP and public-disclosure coordination

This section does not create new IP policy — it points to the governing
one already produced by stage 50 and schedules startup-relevant work
around it.

- **The hard gate stands:** no public disclosure (arXiv, conference talk,
  public code repository, demo) happens before the advisor + OTL
  pre-disclosure screen concludes (gate G-C and its siblings G-D/G-F/G-G,
  [`05_DISCLOSURE_HOLD_CHECKLIST.md`](05_DISCLOSURE_HOLD_CHECKLIST.md)
  §5). Startup preparation does not get an exception to this — if
  anything, it raises the stakes of getting the sequencing right, since a
  premature disclosure could foreclose IP options before anyone has
  evaluated whether they matter.
- **Six candidate concepts already screened (CC-1..CC-6):** stage 50's
  finding was that any protectable scope is likely **thin and
  combination-specific**, not platform-level, because of dense prior art
  (the group's own 2019 GaN publications, active Infineon/TI spinning-
  current patents, 2025 Kalman-fusion journal art)
  [SF, `05_CANDIDATE_PROTECTABLE_CONCEPTS.md` §7]. **This document does
  not revisit that screen or draw a stronger conclusion from it** — a
  startup built on this technology area should plan around thin IP
  protection as the realistic case, with any narrower patent scope as
  upside, not as the plan.
- **Sponsor-rights and ownership questions are OTL's and counsel's, not
  this document's:** DOE/SLAC contract terms, NSF NNCI facility terms,
  TomKat terms, and SU-18 assignment scope all bear on what Tim could
  ever independently commercialize versus what would need a license from
  Stanford [SF, `05_DISCLOSURE_HOLD_CHECKLIST.md` §3–§4]. **Startup
  planning should treat this as an open question to ask OTL directly
  when the time comes, not as settled either way.**
- **Timing relative to the PhD roadmap:** the nonconfidential
  portfolio-artifact review (M42, §5 below) is scheduled *after* the IP
  screen (M13/`06_MILESTONES.csv`) concludes, precisely so it never
  second-guesses that screen's timing.

---

## 5. Nonconfidential portfolio artifacts

**What [REC]:** once the IP screen concludes and P1 is accepted (M42,
target Jan–Jun 2027), produce a written list of which project deliverables
are already publication-cleared (because they are in an accepted paper,
an advisor-approved arXiv posting, or explicitly released code/data) and
therefore safe to describe in a portfolio, talk, or future venture
context without re-clearing them each time. Candidates, **pending that
clearance process — none are cleared as of this stage**:

- The calibration methodology and written GUM/Monte-Carlo uncertainty
  budget (WP-C) — a generically valuable metrology competence, largely
  method-level rather than device-specific.
- The demodulation/fusion codebase (WP-D) — software artifacts are
  explicitly the kind of novelty the user's original request asked to
  emphasize (`../inputs/ORIGINAL_REQUEST.txt`), and stage 20 flagged the
  firmware/demod/fusion codebase as a durable, ownable asset
  [SF, `02_RESEARCH_DIRECTION_DECISION.md` §9].
- Qualification datasets (bench characterization, repeatability
  statistics) — valuable as a demonstrated-competence artifact
  independent of any specific device claim.
- **Explicitly not a portfolio artifact until counsel says otherwise:**
  anything touching CC-1/CC-2/CC-3/CC-5's specific technical
  combinations while the IP screen is open, and anything derived from
  UW-Madison collaboration specifics without UW's own sign-off (a
  joint-contribution fact pattern stage 50 flagged, not resolved
  [`05_DISCLOSURE_HOLD_CHECKLIST.md` §3]).

---

## 6. Collaborator boundaries

**What [REC]:** a short, written statement — reviewed with the advisor,
not unilaterally decided — of what boundaries apply while Tim is still a
Stanford graduate student and a Senesky-group / UW-Madison collaborator:

- No startup-facing conversation shares unpublished data, unreleased
  code, or specifics of CC-1..CC-6 before the disclosure gates in
  §4 clear them.
- Any UW-Madison-originated content (mount-pose surveys, vacuum-field
  computations, co-located coil data) is UW's contribution as much as
  Tim's; a startup discovery conversation should not represent it as
  solely Tim's own work without the same care the mission's own
  inventorship questions already flag [SF,
  `05_DISCLOSURE_HOLD_CHECKLIST.md` §4].
- Advisor awareness of startup-discovery activity (M41/M43) should be
  ongoing, not a surprise revealed at defense time — this is a
  relationship-management recommendation, not a legal requirement this
  mission can state.
- Funding-source obligations (DOE/SLAC, NSF NNCI, TomKat) constrain what
  can be discussed or committed to outside Stanford while those funds
  support the work; the exact boundary is an OTL/counsel question (§4),
  not something this document resolves.

---

## 7. Go/no-go evidence

**What "go/no-go evidence" means here [REC]:** the dated record, produced
before the defense (M44, target Jan–Jun 2028), of what would actually need
to be true for a 2029/2030 startup decision to make sense — not a
decision itself, and not a business plan. A defensible evidence memo
would state, plainly:

1. **Market signal** — what the two discovery rounds (M41, M43) actually
   found: real, expressed demand from named categories of potential
   users, or the absence of it. Absence of a clear signal is itself
   useful, decision-relevant evidence, not a failure to hide.
2. **Technical status** — the §3 technical-validation summary's honest
   accounting of what was demonstrated versus targeted, as of defense
   time.
3. **IP status** — whatever the OTL/counsel process (§4) actually
   concluded: nothing to file, a narrow provisional filed, or still
   undecided. Given stage 50's thin-claims expectation, "nothing
   protectable beyond thin, specific claims" is the base-rate outcome to
   plan around, not a worst case to avoid mentioning.
4. **Personnel/co-founder question** — explicitly out of scope for this
   mission to plan (it depends on people and relationships this mission
   has no visibility into); flagged here only so the go/no-go memo does
   not silently omit it.
5. **Funding path** — explicitly **not** addressed by this document
   (scope boundary, §0) beyond noting that it is a question for after
   this evidence exists, not before.

**Why this is scheduled at M44, right before the defense, rather than
earlier or later [REC]:** earlier, the evidence base (P1/P2 results, IP
screen outcome) does not exist yet; later, it risks becoming an
after-the-fact rationalization rather than a deliberate checkpoint. Tying
it to the defense date keeps it evidence-driven and dated.

---

## 8. Cross-references

- Scheduling and effort for every item above:
  [`06_MILESTONES.csv`](06_MILESTONES.csv) rows M41–M44.
- The disclosure gates this document defers to entirely:
  [`05_DISCLOSURE_HOLD_CHECKLIST.md`](05_DISCLOSURE_HOLD_CHECKLIST.md).
- The candidate-concept screen this document does not revisit:
  [`05_CANDIDATE_PROTECTABLE_CONCEPTS.md`](05_CANDIDATE_PROTECTABLE_CONCEPTS.md).
- The system-competence-stack finding this whole workstream is built on:
  [`02_RESEARCH_DIRECTION_DECISION.md`](02_RESEARCH_DIRECTION_DECISION.md)
  §9.
