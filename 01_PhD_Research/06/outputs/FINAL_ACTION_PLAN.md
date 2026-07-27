# FINAL — Action plan (Stage 80 synthesis)

Companion to [`FINAL_EXECUTIVE_STRATEGY.md`](FINAL_EXECUTIVE_STRATEGY.md).
Every item below schedules work already specified by stages 20–60 — no new
direction, invention, or experiment is introduced here. Milestone IDs
`Mxx` resolve in [`06_MILESTONES.csv`](06_MILESTONES.csv); requirement IDs
(`A-##`/`B-##`/`C-##`/`D-##`, gates `I-#`/`U-#`/`G#`/`G-A..G-H`) resolve in
[`04_MEASUREMENT_REQUIREMENTS.csv`](04_MEASUREMENT_REQUIREMENTS.csv),
[`04_HSX_EXPERIMENT_PLAN.md`](04_HSX_EXPERIMENT_PLAN.md), and
[`05_DISCLOSURE_HOLD_CHECKLIST.md`](05_DISCLOSURE_HOLD_CHECKLIST.md).
Owner "Tim" means Yiming Zhao; this mission itself contacts no one and
submits nothing. Base date: 2026-07-25.

---

## 1. Next 72 hours (by ~2026-07-28)

| # | Action | Owner / decision maker | Dependency | Acceptance gate | Fallback |
|---|---|---|---|---|---|
| 1 | Read `FINAL_EXECUTIVE_STRATEGY.md` and `06_ADVISOR_MEETING_BRIEF.md`; request the advisor meeting (M01/M02 kickoff) | Tim | None | Meeting on the calendar | If the advisor is unavailable ≥2 weeks, send the brief's §1 decision list ahead by e-mail so decisions are not serialized behind the meeting |
| 2 | Start the evidence-preservation list (checklist §1): dated snapshots of the manuscript source, decision letter, 2025 archive + checksums, project 02/03 records; collect UW/group e-mail threads that date design decisions | Tim | None | Every §1 checkbox has a dated copy in a known location | If some records can't be located, note what is missing and when it was last seen — absence is itself evidence to record |
| 3 | Locate the deployed 2025 module and any spare packaged die; record custody and visual condition (gate I-4 — the plan's most consequential inventory question) | Tim (+ group members who handled the module) | None | Module location + custody recorded; resistance-map health check scheduled (F-07 protocol) | If the module cannot be found or is dead: C-03 falls back to a same-wafer sibling die with die-to-die spread as transfer uncertainty, clearly labeled (plan §4.3) |
| 4 | Begin the A-group supplied-data analyses (A-01 shot recount first; M04) | Tim | None (immutable 2025 archive only) | Recount of plasma vs coil-only vs unbiased shots reproduced from `test_note.docx` | None needed — desk work, no gate |
| 5 | Walk the bench: close what can be closed of inventory gates I-1, I-2, I-6, I-7, I-8 by physical check; list what must be purchased (~$90 calibration BOM + ~$8 REF200) or borrowed (I-9 electromagnet) | Tim | None | Each I-gate marked in-hand / to-buy / to-ask | Purchases are Tim's own (small); I-9 "no" → rely on F-01 or state the ~185× extrapolation limitation |
| 6 | Correct the "2023, published" framing in parent-project files and any CV/website copy (conflict C1 — outside the mission's write access) | Tim | None | No document under Tim's control describes the manuscript as published | — |

## 2. Next 30 days (by ~2026-08-24)

| # | Action | Owner / decision maker | Dependency | Acceptance gate | Fallback |
|---|---|---|---|---|---|
| 1 | Advisor decision batch #1: the seven items of `06_ADVISOR_MEETING_BRIEF.md` §1 (M02) | Advisor decides; Tim presents | 72-h item 1 | All seven items answered and minuted | Partial answers: proceed on what cleared; die supply (item 3) and UW e-mail (item 4) are the two with the longest shadows — press for those first |
| 2 | Send the UW e-mail (M03, disclosure gate G-A) — feedthrough pins, mount-pose survey, vacuum-field computation, shot list, co-located B-dot records (U-1), archive-scale question (U-7), August window (U-9) | Tim sends; advisor authorizes; advisor decides the confidentiality posture | Advisor item 4; G-A confidentiality check | E-mail sent; answers logged against gates U-1..U-9 | If authorization is delayed, everything bench-side proceeds anyway (Tier 1 needs no UW input) |
| 3 | Open the advisor + OTL pre-disclosure conversation (M13 start; checklist §2–§3) | Tim initiates; advisor owns go/no-go on OTL time; OTL owns evaluate/file/decline | 72-h item 2 (preservation record) | OTL screen concluded and its outcome recorded in writing — including a documented "nothing to file" | If OTL is slow, the hard consequence is only on disclosure events (P1 resubmission, arXiv, UW specifics) — bench work is unaffected |
| 4 | Close G0: finish inventory gates; make the small purchases; build the Helmholtz former/cradle (M05) | Tim | 72-h item 5 | I-1..I-5 closed; calibration bench physically exists | Any missing instrument → borrow/substitute per plan §2.2; A-group work continues regardless |
| 5 | Attempt B-01 anomaly closure (M06, gate G1) — the single highest-priority bench task; then B-02 8-state survey + global sign fix | Tim | G0 partially closed (needs only scope + divider) | Mechanism named, reproduced, written to the project 02 journal; do-not-calibrate flag lifted | G1 fail → board fault-isolation sprint; P1 re-scoped around A-group + WP-A + bandwidth while the chain is fixed (plan §2.4) |
| 6 | Complete A-group analyses (M04) and draft the WP-A comparison table from ledger rows (M07) | Tim | A-group: none; WP-A: primary-PDF re-confirmation for any metadata-only row | Six analyses scripted + written up; table populated with per-cell evidentiary basis | None needed — desk work |
| 7 | Ask the SENSL editorial office whether the resubmission invitation lapses (no-commitment query) | Tim or advisor (their call at the meeting) | Advisor awareness | Written answer on file | If unanswered, plan on the letter's own terms (no stated deadline) |

## 3. Next 90 days (by ~2026-10-23)

| # | Action | Owner / decision maker | Dependency | Acceptance gate | Fallback |
|---|---|---|---|---|---|
| 1 | WP-C calibration core: C-01 coil-constant triangulation, C-02 DC calibration + GUM/MC budget, C-04 bias scaling (M08–M09) | Tim | G1 passed (hard rule) | u(k)/k ≤ 2%; m ± ~2% absolute, <0.5% linearity; written budget | G-cal fail → no tesla claim anywhere; route decision revisited per matrix AE-01 fallback |
| 2 | C-03 voltage-bias S_v on the deployed die (M10) — unlocks the retroactive Fig.-5 field-unit conversion (G-01) | Tim | I-4 answer; ideally I-6 (2023 chain) | S_v ± u at 0.2/0.3/0.4 V bias, assumptions stated | Deployed die unavailable → sibling-die transfer with labeled uncertainty; worst case, Fig. 5 stays voltage-domain with the AE's honest-uncertainty framing |
| 3 | WP-B repeatability: D-01 ≥3 dies + D-02 remount separation (M11) | Tim; die count decided by advisor item 3 | Die supply; wedge-bonder access if packaging needed | Within-die vs between-die variance separated | Single-device fallback §7.3 — operational repeatability + literature statistics, AE-sanctioned |
| 4 | Characterization suite: bandwidth (B-03/B-04), noise, hysteresis, temperature, drift, parasitics (M12) | Tim | C-02 exists | Each quantity reported with basis; 1 MHz assertion retired | C-07/C-08 strengthen but do not gate Tier 1 — drop last if time is short |
| 5 | Campaign #1 execution if gates clear (M15–M16, gates G2/U-9; realistic window September) | Tim on-site; HSX schedule is UW's | U-9 confirmed; C-02 done pre-ship; F-07 health map | Coil-only anchor shots (≥2 settings × ≥3) + shot matrix per plan §10 | Fallback F1: Tier-1 package unaffected; anchor moves to the next window |
| 6 | P1 full draft (M14) integrating A-group + WP-A/B/C + bandwidth + revision map (`03_MANUSCRIPT_DIAGNOSIS.md` §7) | Tim writes; advisor reviews | Bench results as they land | Every P0 matrix row closed in the draft; 4-page fit per R1's concession | If a P0 row is still open, the draft carries the honest fallback wording already specified in the matrix |
| 7 | Conclude the IP screen (M13 end) | Advisor + OTL (+ counsel) | 30-day item 3 | Written outcome; disclosure gates G-B/G-C released or held deliberately | Screen unresolved → P1 resubmission waits (the advisor's own rule); bench/desk work continues |
| 8 | Start reading-committee formation (M32; Stanford EE year-3 norm) | Tim + advisor | None | Committee list agreed | Administrative — start early precisely so it never gates |

## 4. Next six months (by ~2027-01-21)

| # | Action | Owner / decision maker | Dependency | Acceptance gate | Fallback |
|---|---|---|---|---|---|
| 1 | P1 resubmission to IEEE Sensors Letters (M18) with the point-by-point response supplement | Tim submits; advisor approves | M13 closed; M14 complete | Submitted under new Manuscript ID with prior ID declared | If the invitation lapsed: submit as a fresh SENSL letter, or trigger the modified-Route-D fallback |
| 2 | Optional arXiv posting of the revised manuscript (M19, hard gate G-C) | Advisor + OTL sign-off; Tim executes | M18; M13 outcome documented | Documented sign-off precedes posting | Skip the posting — it is an accelerant, never a requirement |
| 3 | Campaign #2 / vector probe window (M21–M25, gates G3/G4; slip limit ~Feb 2027) | Tim + UW | Vector build (≥2 axes), campaign scheduling | Probe operated in-vessel; anchor + dynamics + stability shots | Fallback F2: P3 descopes to single-axis anchor + bench-validated vector module |
| 4 | WP-D development substantially complete on synthetic + available HSX data (M17/M23) | Tim | U-1 answer scopes the data | Estimator runs on real or synthetic data with quantified drift correction | U-1 negative → synthetic + 2025-data floor (degrades gracefully by design) |
| 5 | P2 draft begins (M27, parallel to P1 review) | Tim | M17/M23 | Draft exists by ~Feb 2027 | — |
| 6 | Candidacy/course-requirement confirmation (M33) | Tim + department | None | Confirmed in writing | Administrative |
| 7 | Startup discovery round 1 (M41, ~1 day/month, no confidential content) | Tim | IP-screen boundaries understood | ≥10 conversations logged | Compress rather than cancel — it never competes with critical-path time |

## 5. Next 12 months (by ~2027-07-25)

| # | Action | Owner / decision maker | Dependency | Acceptance gate | Fallback |
|---|---|---|---|---|---|
| 1 | P1 acceptance decision window (M20/M26) | Journal-controlled | M18 | First accepted first-author paper | Second decline → advisor escalation: alternate sensors-class venue or strengthened arXiv route (never the rejected version) |
| 2 | MVG-vs-upside checkpoint (M28, Q1 2027) — explicit joint commitment | Tim + advisor | Campaign-#2 actual status known | Decision minuted | Defaults to MVG if unresolved — the floor never waits on the upside |
| 3 | P2 submission and review (M27→M31) | Tim | M17/M23 | Second paper submitted; acceptance completes the two-paper floor | P2 declined → revise/resubmit; flagged as the plan's highest-consequence review risk (no fully pre-planned fallback if it fails outright) |
| 4 | P3 drafting per branch: upside (M29) or descoped (M30) | Tim | M25 outcome | Draft matching the RSI new-instrument criterion | Descoped branch is pre-designed, not improvised |
| 5 | Direction gate G5 (M34, ~Jul 2027): ≥1 paper accepted/in revision AND real-die calibration achieved | Tim + advisor | Everything above | Both conditions true → continue OPT2 | Either false → pivot to OPT3 on WP-D's pipelines and UW relationship (bounded-cost landing) |
| 6 | Dissertation Ch. 1–4 drafting begins (M36) | Tim | P1 content stable | Chapters drafted (P1 material repackaged — lowest-risk writing) | — |

## 6. Next 24 months (by ~2028-07-25)

| # | Action | Owner / decision maker | Dependency | Acceptance gate | Fallback |
|---|---|---|---|---|---|
| 1 | P2 acceptance (M31); P3 review/acceptance in the upside branch (M35) | Journal-controlled | Prior rows | Two-paper floor complete; third paper is upside | MVG plan defends on P1+P2 with the descoped vector chapter |
| 2 | Dissertation Ch. 5–7 (M37): hybrid architecture, vector-probe chapter in whichever form, conclusions | Tim | M36; P2/P3 content | Full draft to committee | Chapter framing degrades with the fallbacks above — never hides the campaign gap |
| 3 | TGR status (M38) once residency, candidacy, committee are in place | Tim + department | M32/M33 | TGR granted | Administrative buffer exists in the M38→M39 gap |
| 4 | University Oral Exam / defense (M39, Q2 2028 — Stanford EE year-4 norm) | Tim + committee | M37/M38 | Defense passed | ~2-month buffer to submission absorbs formatting/admin delay |
| 5 | Dissertation submission + conferral (M40, Q3 2028) | Tim | M39 | Degree conferred ≈ the two-year target | — |
| 6 | Startup round 2 + technical-validation summary (M43); collaborator-boundary + go/no-go evidence memo before the defense (M44) | Tim; advisor aware | P1/P2 results; IP-screen outcome | Dated go/no-go memo exists before the defense | Absence of market signal is itself recorded evidence, not failure |

## 7. Do-not-do-yet list

1. **No arXiv posting of anything** until the IP screen concludes and the
   advisor + OTL sign off (hard gate G-C) — and **never** the rejected
   version verbatim, at any point.
2. **No UW e-mail** before advisor decision 4 and the G-A confidentiality
   check.
3. **No calibration work** before B-01 closes the ~109× anomaly (the
   project's own do-not-calibrate instruction).
4. **No tesla-denominated claim** anywhere before G-cal passes; no reuse
   of the asserted 1 MHz bandwidth figure.
5. **No conference talk, poster, abstract, public code/firmware repo, or
   demo** before the disclosure gates release (G-D/G-F/G-G); inventory
   any already-given talks first.
6. **No RSI submission** without re-checking the live RSI policy page
   (verification currently rests on an ~8-month-old archived copy).
7. **No description of the manuscript as published (2023 or otherwise)**
   in any document, response letter, or conversation.
8. **No new device topology, epitaxy, or mask work; no cleanroom
   fabrication; no neutron/gamma experiments** (mission scope; radiation
   stays TCAD/literature outlook).
9. **No startup pitching, fundraising, equity, or commitment
   conversations** — discovery rounds are informational only.
10. **No purchase or commitment against campaign #2 hardware** beyond
    what the advisor-approved plan already lists, until M02 decisions
    land.

## 8. Exact materials for the advisor meeting

Bring (in this order of use):

1. [`06_ADVISOR_MEETING_BRIEF.md`](06_ADVISOR_MEETING_BRIEF.md) — the
   agenda; its §1 lists the seven decisions requested.
2. [`FINAL_EXECUTIVE_STRATEGY.md`](FINAL_EXECUTIVE_STRATEGY.md) — the
   one-document synthesis (this stage).
3. `../inputs/Decision_Letter_IEEE_2026-07-23.pdf` — the primary evidence
   for the venue discussion [SF].
4. [`02_RESEARCH_DIRECTION_DECISION.md`](02_RESEARCH_DIRECTION_DECISION.md)
   — open to §2 (scorecard) and §10 (the seven decisions in full).
5. [`03_PUBLICATION_ROUTE_DECISION.md`](03_PUBLICATION_ROUTE_DECISION.md)
   — open to §0 (summary) and §5 (side-by-side table).
6. [`04_HSX_EXPERIMENT_PLAN.md`](04_HSX_EXPERIMENT_PLAN.md) — open to §2
   (inventory/UW gates) and §12 (burden: ≈19–29 bench-days, zero
   cleanroom); plus the must-have table in the advisor brief §3.
7. [`05_DISCLOSURE_HOLD_CHECKLIST.md`](05_DISCLOSURE_HOLD_CHECKLIST.md)
   — §2 (advisor questions) and §5 (gate table), for the IP-screen
   conversation.
8. [`06_MILESTONES.csv`](06_MILESTONES.csv) +
   [`06_24_MONTH_PHD_ROADMAP.md`](06_24_MONTH_PHD_ROADMAP.md) §7–§8 —
   the MVG-vs-upside structure and slip table, for the graduation-target
   confirmation.
9. The conflict-C1 note ([`00_CONFLICT_LEDGER.md`](00_CONFLICT_LEDGER.md)
   §C1) — for decision item 7 (correcting the parent record).
