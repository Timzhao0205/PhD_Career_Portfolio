# 03 — Publication route decision (Stage 30)

Prepared by: Claude Code, stage `30_manuscript`, requested model Fable 5 /
Extra High. Per conflict C2 in
[`00_CONFLICT_LEDGER.md`](00_CONFLICT_LEDGER.md), this comparison is derived
**from the decision letter's actual terms**
([`../inputs/Decision_Letter_IEEE_2026-07-23.pdf`](../inputs/Decision_Letter_IEEE_2026-07-23.pdf),
read in full this stage), not from project 03's planning narrative (which
assumes one branch of the question). Evidence labels: **[SF]** supplied
fact, **[CONFIRMED POLICY]** current official journal/repository policy
verified this stage (evidence table in §4), **[INF]** inference,
**[REC]** recommendation, **[GATE]** unresolved gate. Manuscript-defect
detail lives in [`03_MANUSCRIPT_DIAGNOSIS.md`](03_MANUSCRIPT_DIAGNOSIS.md);
reviewer-item detail in
[`03_REVIEWER_RESPONSE_MATRIX.csv`](03_REVIEWER_RESPONSE_MATRIX.csv).

**Nothing was submitted, uploaded, or rewritten in this stage.**

---

## 0. Decision summary

- **Primary recommendation [REC]:** Route A — revise and resubmit to IEEE
  Sensors Letters as the invited new submission, but **only after** the
  bench evidence package closes (WP-A comparison table, WP-B multi-die
  statistics, WP-C absolute calibration + uncertainty, bandwidth
  derivation, supplied-data analyses of §4.1 of the diagnosis). Then Route
  C (the RSI vector-probe instrument study) proceeds as the separate,
  substantially new paper it already is in project 03's plan. An arXiv
  posting of the **revised, calibrated** manuscript at resubmission time is
  optional and permitted by IEEE policy, strictly after the Stage-50 IP
  screen and advisor sign-off.
- **Fallback [REC]:** if the bench-calibration path stalls past the
  stage-20 gate windows (anomaly unresolved or no die supply), switch to a
  modified version of the user's Route D: an IP-screened arXiv preprint of
  a **strengthened but explicitly uncalibrated** version (reframed novelty,
  WP-A table, supplied-data analyses; not the rejected version verbatim) to
  timestamp priority, followed by the RSI study after the next campaign.
- The user's Route D as literally proposed (rejected version to arXiv now,
  skip SENSL, everything else into RSI) is **not recommended as primary**:
  it permanently publishes the version that just failed review, leaves zero
  peer-reviewed first-author output until ~mid-2027 against a ~24-month
  graduation plan, and triggers the advisor's pre-disclosure IP gate
  earliest, for the least benefit. §3.4 gives the full accounting,
  including what the proposal gets right (priority timestamping; RSI as the
  natural home for the full study).

---

## 1. What the decision letter actually establishes [SF]

1. Decision: "we must decline the manuscript … we invite you to consider
   submitting a revised manuscript that takes the reviewers' comments into
   consideration. It would be given a **new Manuscript ID** and reviewed
   again."
2. Mechanics: revised main document plus a **supplementary file responding
   to every reviewer remark** ("state how you satisfied (or why you
   declined to satisfy) each suggestion"); declare prior ID
   SENSL-26-07-RL-1061; "it **may** be sent again to reviewers."
3. The AE's substantive bar: "IEEE Sensors Letters requires a fully
   finished study of the intended sensing output" — authoritative for this
   manuscript regardless of where journal policy states it.
4. Tone: "we believe the work has merit"; Reviewer 1: "novel and unique to
   my knowledge … still worth publishing." Only Reviewer 2 recommended
   outright rejection.
5. **No resubmission deadline appears anywhere in the letter.** Whether
   the invitation lapses is NOT ESTABLISHED FROM SUPPLIED FILES [GATE —
   answerable by a no-commitment query to the editorial office; asking a
   question mutates nothing].

## 2. The four routes compared

- **Route A** — new/revised IEEE Sensors Letters submission following the
  invitation.
- **Route B** — arXiv preprint based on the current study, as a standalone
  act.
- **Route C** — full RSI instrument study using the next experiment
  (project 03's plan; C019/C020).
- **Route D** — the user's proposed sequence, quoted from
  [`../inputs/ORIGINAL_REQUEST.txt`](../inputs/ORIGINAL_REQUEST.txt):
  "I am going to initiate another experiment with the HSX and if IEEE
  Sensors letters require too much work (calibration, exact values). I am
  considering to use all that data and methods for Review of Scientific
  Instruments (or higher impact journals) and use the rejected version for
  the preprint only (Arxiv)." The same request records the advisor's
  condition: "if I am going to publish on Arxiv … my advisor would like me
  to find concepts or technologies that are potentially patentable before
  showing it to the publication." [SF]

## 3. Route-by-route analysis

### 3.1 Route A — revised Sensors Letters submission (invited)

- **Minimum evidence to submit credibly [INF, from the matrix]:** all P0
  rows closed: WP-C calibration with uncertainty (AE-01/AE-04/AE-05/R1-01,
  prerequisite: ~109× anomaly closure, C017), WP-B ≥3-die bench statistics
  + single-module explanation (AE-03/R2-02; die supply = advisor gate),
  WP-A table (AE-02), novelty reframing + reference expansion
  (R2-01/R2-03), bandwidth answer (R1-04/AE-07), plus the free
  supplied-data analyses (shot recount, repeatability statistics,
  correlation quantification). Reviewer 1's page-limit concession
  (calibration as text discussion) keeps this inside 4 pages.
- **Time [INF]:** bench package is stage 40's to schedule; stage 20's P1
  window (months 0–7 from Aug 2026) implies resubmission ~Q4 2026.
  Post-submission speed is fast: "Submission-to-ePublication = 4.8 weeks,
  median" [CONFIRMED POLICY §4.1]. Earliest realistic acceptance: late
  2026 / early 2027.
- **Page/scope fit:** 4-page maximum including a reference column
  [CONFIRMED POLICY §4.1]; scope is sensor-centric ("theory, design,
  fabrication, manufacturing and application of devices for sensing…") —
  the revision must foreground the sensor system (AE-06). Fit is good
  *after* the evidence package exists; it was the fit of the *old* framing
  that failed.
- **Novelty risk [INF]:** moderate-low. The two-part re-centered claim
  (first GaN/WBG 2DEG Hall in-vessel in a magnetic-confinement device;
  first Hall of any kind in a QHS stellarator) is a bounded absence
  finding from the 231-source ledger — strong but falsifiable; a new
  R2-type reviewer can still contest granularity. Mitigations: WP-A table
  makes the comparison explicit; prior-art citation of the group's own
  device papers removes the easiest attack; AE and R1 are already on
  record that the work has merit. Residual risk: "new Manuscript ID" means
  review may restart with different reviewers [SF].
- **Duplication/overlap risk:** none — it is the invited resubmission of
  the authors' own unpublished manuscript; declare the prior ID as
  instructed [SF]. It does constrain Route C's writing later (§3.3).
- **Pre-publication IP gate [REC]:** peer-reviewed submission is not a
  public posting, but SENSL's ~5-week ePub median means publication
  follows acceptance almost immediately — so the Stage-50 screen (and any
  filing decision it triggers, which is counsel's call, not this
  mission's) should complete **before resubmission**, not before
  acceptance. This is a research screen sequencing recommendation, not a
  legal conclusion.
- **What not to claim:** "first fusion Hall diagnostic" (false — CASTOR/
  EAST/JET/ITER lineage [S0068](https://doi.org/10.1088/1741-4326/ac8aad),
  [S0113](https://doi.org/10.1063/1.4732077)–[S0115](https://doi.org/10.1063/1.5038812)); "calibrated"/"absolute"
  until WP-C data exists; the loose QHS wording (use
  [S0128](https://doi.org/10.1088/1361-6587/adb179)'s); 1 MHz bandwidth
  until derived; any experimental radiation-hardness plan (scope rule —
  TCAD/literature outlook only); any suggestion the work was previously
  published (conflict C1).

### 3.2 Route B — arXiv preprint of the current study (standalone)

- **Minimum evidence:** none new — that is precisely its weakness: it
  answers no reviewer concern and publishes them unanswered.
- **Time:** days after the IP gate clears (endorsement/moderation
  permitting).
- **Page/scope fit:** no length constraints; physics.ins-det /
  physics.plasm-ph classification subject to arXiv moderation [CONFIRMED
  POLICY §4.4].
- **Novelty risk:** the timestamp *helps* priority against scooping — the
  proposal's genuinely good idea — but a preprint confers no peer-reviewed
  standing, and the posted version becomes the version of record in
  Google-Scholar terms while carrying every defect in the diagnosis.
- **Duplication/overlap risk:** low as policy: IEEE permits prior preprints
  ("Authors may share or post their preprints … On TechRxiv or ArXiv")
  and requires the posted version be updated upon any later IEEE
  acceptance; AIP likewise permits preprints before submission and
  requests "at the minimum a CC BY-NC" license [CONFIRMED POLICY
  §4.2–4.3]. So Route B forecloses neither journal.
- **Pre-publication IP gate — the hard one [SF + CONFIRMED POLICY]:**
  arXiv postings are permanent ("Articles that have been announced and
  made public cannot be completely removed"; withdrawal leaves prior
  versions accessible) and the license grant is irrevocable. Posting is a
  public disclosure; its effect on patentability in any jurisdiction is a
  legal question this mission does not decide. The advisor's instruction
  makes the sequencing unambiguous: **no arXiv posting before the Stage-50
  screen and advisor sign-off.**
- **What not to claim:** everything in Route A's list, plus: do not label
  the preprint "submitted to/under review at" any venue it is not, and do
  not post the rejected version verbatim with the known-false framing
  (QHS wording, unsupported 1 MHz, device-granularity novelty) — a
  permanent record of retracted-in-spirit claims is worse than no
  preprint.

### 3.3 Route C — full RSI instrument study from the next experiment

- **Minimum evidence [INF from C019/C020 + genre norms]:** the calibrated
  multi-axis probe with campaign data — i.e., everything Route A needs
  *plus* the vector hardware, campaign deployment, and
  vacuum-field/conventional-probe validation. RSI's genre
  ([S0143](https://doi.org/10.1063/1.4894209),
  [S0154](https://doi.org/10.1063/5.0002193),
  [S0226](https://doi.org/10.1063/5.0095907)) expects a complete
  instrument characterization.
- **Time [SF/INF]:** campaign #2 is planned for Nov 2026 and has not
  occurred; project 03 targets ~Mar 2027 submission (C019). Realistic
  acceptance mid-to-late 2027. Any campaign slip moves it directly.
- **Page/scope fit:** scope confirmed — "novel advancements in scientific
  instrumentation, apparatuses, techniques of experimental measurement"
  [CONFIRMED POLICY §4.3]. Length limits: NOT ESTABLISHED this stage (the
  journal's article-type length guidance was not retrievable; do not
  assume).
- **Novelty risk [INF]:** low *given* the letter exists or not: the
  instrument-study contribution (calibrated vector probe, uncertainty
  budget, in-situ validation) is differentiated from the feasibility
  letter either way; stage 10C found no HSX-specific Hall
  calibration/comparison literature at all.
- **Duplication/overlap risk [CONFIRMED POLICY §4.3]:** RSI "will consider
  papers … that contain some material previously published, but not yet
  peer-reviewed," but "papers covering material previously published in
  any peer reviewed journal … will be refused." Consequence: if Route A
  publishes first, the RSI paper must be substantially new — which the
  vector probe + campaign-#2 data + full calibration methodology make it
  [INF]. Background overlap is normal letter→full-paper practice; the RSI
  manuscript should cite the letter and confine overlap to introduction
  context. A prior arXiv preprint is expressly tolerated (preprints are
  not peer-reviewed publication under this policy).
- **Pre-publication IP gate:** same sequencing logic as Route A — the
  Stage-50 screen precedes whichever disclosure comes first (preprint or
  publication).
- **What not to claim:** the project-03 thesis wording ("first absolutely
  calibrated, multi-axis…") only becomes claimable when its premises are
  met (C020: calibration achieved, campaign executed); until then it is a
  target, not a result.

### 3.4 Route D — the user's arXiv-plus-RSI sequence

- **What it gets right [INF]:** (a) an arXiv timestamp protects the
  first-in-class claim while the slow RSI study matures — the scooping
  concern is legitimate given the active non-GaN fusion-Hall field
  ([S0112](https://doi.org/10.1088/1361-6587/ae6c59) shows the 2026 state);
  (b) RSI is the right eventual home for the full instrument study; (c) it
  avoids re-review under a 4-page constraint the user found onerous.
- **What it costs [INF]:**
  1. **Timeline exposure:** first peer-reviewed first-author output slips
     to ~mid-2027 and becomes single-point-dependent on campaign #2 —
     exactly the structure stage 20 rejected ("every month P1 slips, the
     zero-accepted-papers risk compounds"; the two-paper floor exists on
     bench + already-collected data only if a bench-based paper is
     actually written).
  2. **Permanent weak disclosure:** "use the rejected version for the
     preprint" would permanently publish (irrevocably licensed,
     non-removable [CONFIRMED POLICY §4.4]) a version whose novelty
     framing, QHS wording, bandwidth claim, and measurand gap are
     documented defects — under the authors' names, citable by the very
     reviewers/competitors who know its history.
  3. **Earliest IP-gate trigger:** it front-loads the public disclosure
     the advisor explicitly gated on a patent screen.
  4. **Foregone invitation:** it abandons a decline-with-merit invitation
     at a venue with a 4.8-week median publication cycle — the cheapest
     available path to an accepted paper — without the SENSL door being
     actually closed by anything in the letter [SF].
- **Minimum evidence / time / fit / risks:** composition of §3.2 and §3.3.
- **What not to claim:** union of Routes B and C lists.

## 4. Official-policy evidence base (all retrieved 2026-07-25)

| # | Policy fact | Source (access basis) |
|---|---|---|
| 4.1 | IEEE Sensors Letters: 4-page maximum including a reference column; sensor-centric scope statement; "Submission-to-ePublication = 4.8 weeks, median" | [ieee-sensorsletters.org/information-for-authors](https://ieee-sensorsletters.org/information-for-authors/) (page fetched and read) |
| 4.2 | IEEE article sharing: preprints may be posted "On TechRxiv or ArXiv" prior to submission; upon acceptance "previously posted versions must be replaced by a full citation with DOI or the accepted version with DOI"; accepted versions require an IEEE copyright notice | [IEEE Article Sharing and Posting Policies (PDF)](https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE-Article-Sharing-and-Posting-Policies.pdf) (PDF fetched and read verbatim) |
| 4.3 | AIP/RSI: preprints allowed "prior to submission and/or acceptance" on noncommercial servers, minimum CC BY-NC license requested; accepted manuscript postable immediately; 12-month embargo on the version of record. RSI scope ("novel advancements in scientific instrumentation…"). RSI refuses "papers covering material previously published in any peer reviewed journal" while considering material previously posted without peer review | [AIP sharing-content-online](https://publishing.aip.org/resources/researchers/rights-and-permissions/sharing-content-online/) (fetched and read); [AIP RSI journal page](https://publishing.aip.org/publications/journals/special-topics/rsi/) (fetched); [RSI Editorial Policies](https://pubs.aip.org/aip/rsi/pages/policies) — **direct fetch blocked (HTTP 403); the previously-published wording was confirmed via search-result extraction of that official page and is quoted only to that confidence level** |
| 4.4 | arXiv: announced articles "cannot be completely removed"; withdrawal leaves prior versions accessible; license choice is irrevocable; submitters directed to check journal policies before choosing a license | [arXiv withdrawal policy](https://info.arxiv.org/help/withdraw.html), [arXiv license help](https://info.arxiv.org/help/license/index.html) (both fetched and read) |

Everything else in §3 is [SF] from the letter/files or labeled [INF].

**Stage-70 re-verification (2026-07-25) of the §4.3 RSI wording:** the
live `pubs.aip.org/aip/rsi/pages/policies` page remained bot-blocked
(Cloudflare challenge/HTTP 403), but an Internet Archive snapshot of the
same official page (2025-11-15,
[web.archive.org/web/20251115144142/https://pubs.aip.org/aip/rsi/pages/policies](https://web.archive.org/web/20251115144142/https://pubs.aip.org/aip/rsi/pages/policies))
contains both quoted sentences **verbatim**, upgrading the confidence
level from search-extraction to archived-official-page (≈8 months old —
re-check the live page before actual submission). The same page adds a
criterion §3.3 should carry explicitly: *"The major criterion for
publication is technical novelty. A previously published instrument is
not considered to be novel."* — i.e., the RSI paper must present the
vector probe as a **new instrument/technique**, not "the same instrument,
more data"; the §3.3/§6 framing (vector hardware + campaign-#2 data +
full calibration methodology) already satisfies this, and this criterion
is the reason a "letter content + minor extensions" RSI submission would
fail even where the duplication rule technically allows it.

## 5. Side-by-side summary

| Criterion | A: revised SENSL | B: arXiv now | C: RSI study | D: arXiv+RSI |
|---|---|---|---|---|
| New evidence needed before acting | Bench package (WP-A/B/C + bandwidth) | None (that is the flaw) | Campaign #2 + everything in A | None now; C's later |
| Earliest peer-reviewed acceptance [INF] | late 2026–early 2027 | never (not peer-reviewed) | mid–late 2027 | mid–late 2027 |
| Page/scope fit | 4 p incl. refs; sensor-centric — fits after evidence exists | unconstrained | instrument-study genre — natural fit | as C |
| Novelty risk | moderate-low with reframing + table | timestamp helps; no standing | low, differentiated | low, but weak version public |
| Duplication risk | none; constrains C's writing | none (policies permit) | must be substantially new vs A — it is | as C |
| IP gate timing | screen before resubmission | screen before posting (hard gate) | screen before first disclosure | earliest trigger |
| Distinctive failure mode | third-party reviewer roulette on new ID | permanent public weak version | campaign slip | zero accepted papers for ~a year + permanent weak version |

## 6. Recommendation with triggers

**Primary [REC]: A → C sequence (equals stage 20's P1 → P3).** Execute the
bench evidence package first (stage 40 specifies it), resubmit to SENSL
with the point-by-point response supplement the letter requires, and build
the RSI study on campaign #2 as the substantially new instrument paper.
Optional accelerant: post the **revised** (calibrated, reframed) manuscript
to arXiv at resubmission time — permitted by IEEE policy [4.2] — after the
Stage-50 screen and advisor sign-off; this captures Route D's timestamp
benefit without publishing the weak version.

**Fallback [REC]: modified Route D.** Trigger: the stage-20 §8 gate windows
fail — the ~109× anomaly stays open past its gate, or no multi-die supply
materializes, or the SENSL editorial office states the invitation has
lapsed [GATE §1.5]. Then: complete the Stage-50 screen; post an arXiv
preprint of a **strengthened, honestly-uncalibrated** version (reframed
novelty, WP-A table, §4.1 supplied-data analyses, explicit limitations
section — not the rejected version verbatim); and direct all experimental
effort at the RSI study. This preserves priority and salvages a
campaign-independent public record even in the worst bench case.

**Explicitly not recommended [REC]:** posting the rejected version
verbatim (Route D as literally worded), and any disclosure of any kind
before Stage 50 completes — the advisor's own stated condition [SF].

## 7. Gates handed onward

| Gate | Owner |
|---|---|
| ~109× anomaly closure; WP-B/WP-C experiment specs; bench bandwidth sweep; UW co-located B-dot data request | Stage 40 (next) |
| Pre-disclosure IP screen (advisor-required before any arXiv posting) | Stage 50 |
| SENSL invitation-lapse question (no-commitment editorial query; asks permission for nothing, mutates nothing) | User/advisor, any time |
| Die supply (gen-2 vs remaining 2023-generation) — advisor question #3 of stage 20 §10 | User/advisor |
| Calendar integration of A→C sequence with campaign dates | Stage 60 |
