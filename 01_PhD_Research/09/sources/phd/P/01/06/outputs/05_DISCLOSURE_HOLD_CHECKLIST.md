# 05 — Disclosure-hold checklist (Stage 50)

> **RESEARCH SCREEN — NOT LEGAL ADVICE · NO PATENTABILITY CONCLUSION ·
> NO FREEDOM-TO-OPERATE CONCLUSION.**
> This checklist organizes what to preserve, whom to ask, and in what order
> — it does not send anything, contact anyone, or decide any legal question.
> Concepts CC-1…CC-6 are defined in
> [`05_CANDIDATE_PROTECTABLE_CONCEPTS.md`](05_CANDIDATE_PROTECTABLE_CONCEPTS.md);
> prior art in [`05_PRIOR_ART_LEDGER.csv`](05_PRIOR_ART_LEDGER.csv).

## 1. Materials to preserve before any public disclosure

Preserve dated, unaltered copies (the mission's immutability rules already
protect several of these):

- [ ] The declined manuscript source and figures
  (`01_Publications/submitted/regular_lsens/`), the submitted PDF bundle
  (`inputs/IEEE_submission_bundle_2026-07-02.pdf`), and the decision letter
  (`inputs/Decision_Letter_IEEE_2026-07-23.pdf`) — establishes what was
  described, by whom, and when, and that journal submission is not a public
  posting.
- [ ] The 2025 HSX raw data archive with its SHA-256 checksums
  (`inputs/07_HSX_august2025_results_original.zip`,
  `inputs/INPUT_CHECKSUMS.sha256`).
- [ ] Project 02 as a dated snapshot: `docs/SPECS.md`,
  `docs/hsx_readout_bringup_and_calibration_plan.md`,
  `docs/second_test_setup_static_bias.md`, `NOTES.md`, `journal/`
  (esp. `2026-07-08_spinning_emulator_20mA.md`), firmware
  (`firmware/pico2/`), analysis scripts, LTspice/KiCad netlists, and the
  gerber/order package `circuit/hsx_setup_v1_Y23.zip` — the CC-2
  conception/reduction-to-practice record.
- [ ] Project 03 plan (`docs/rsi_experiment_and_publication_plan.md`) with
  its July 8, 2026 revision date — the CC-3/CC-5 conception record.
- [ ] Any lab notebooks, e-mail threads, and design reviews with UW
  (Goodman/Gallenberger/Geiger) and within the Senesky group that date the
  packaging and deployment decisions (CC-1) — whereabouts NOT ESTABLISHED
  FROM SUPPLIED FILES; collect them now.
- [ ] The mission's stage 40/50 outputs, labeled as AI-assisted planning
  documents with their generation dates (relevant to the CC-4/CC-6
  contribution question, §4).
- [ ] A record of the deployed 2025 module's current location and custody
  (stage 40 gate I-4) — the physical artifact itself is evidence.

## 2. Questions for the advisor (Prof. Senesky)

- [ ] Does the group intend to pursue any invention disclosure from this
  work before the P1 resubmission/arXiv step? (The advisor's own
  requirement — IP screen before arXiv — is the trigger for this stage;
  the outcome decision is the advisor's + OTL's, not this document's.)
- [ ] Are there existing Senesky-group invention disclosures or OTL dockets
  touching GaN Hall sensors, spinning readout, or harsh-environment
  packaging that this work builds on? (Bounded public searches found no
  granted Stanford/Senesky GaN-Hall patent, but unpublished applications
  and internal disclosures are invisible to public search.)
- [ ] Which of CC-1…CC-5, if any, does the group consider worth OTL's
  time, given stage 20 §9's thin-claims expectation?
- [ ] Timing: is the group willing to hold the P1 resubmission and the July
  UW e-mail until OTL answers a quick screen, or does the publication
  schedule take priority? (Stage 30/60 scheduling consequence.)
- [ ] Who from the group should be named on any disclosure conversation
  (see §4 contributors), without prejudging inventorship?

## 3. Questions for Stanford OTL

- [ ] Given SU-18 assignments and the funding mix (DOE DE-AC02-76SF00515 /
  SLAC FWP 101264, TomKat, NSF-supported NNCI fabrication ECCS-2026822),
  what disclosure obligations exist regardless of whether anything is
  filed (e.g. federal iEdison reporting)?
- [ ] Does OTL see enough in CC-1/CC-2/CC-3/CC-5 to justify a provisional
  before the P1 resubmission, knowing the prior-art density documented in
  the ledger? (OTL's call with counsel — this screen provides the
  evidence, not the answer.)
- [ ] How does OTL want to handle the UW-Madison joint-contribution fact
  pattern (CC-1 deployment, CC-5 pose survey/vacuum-field computation) —
  is an inter-institutional agreement (e.g. with WARF) needed before
  deeper design sharing?
- [ ] Is there an existing collaboration/facility-use agreement covering the
  HSX deployments that already allocates IP? (NOT ESTABLISHED FROM SUPPLIED
  FILES.)
- [ ] Does the Aug-2025 in-vessel operation at a collaborator facility, or
  the 68-shot dataset's handling, count as a public use/disclosure for any
  jurisdiction OTL cares about? (Counsel question routed via OTL.)

## 4. Authorship / inventorship / ownership / sponsor / collaboration questions

*For OTL + registered patent counsel; listed, not answered.*

- [ ] **Inventorship vs authorship:** the manuscript's six authors (Zhao,
  Goodman, Gallenberger, Cox, Geiger, Senesky) are an authorship list;
  inventorship on any claim set must be determined feature-by-feature by
  counsel. Which features of CC-1 (packaging stack, graphite GDC shield,
  in-vessel integration) trace to which person?
- [ ] **CC-2/CC-3 contribution boundaries:** project 02/03 design records
  sit in Tim's repositories; the die and offset-physics lineage is the
  group's published work (PA-N03–PA-N05, PA-N08). Where is the
  conception boundary?
- [ ] **AI-assisted content:** parts of CC-4's and CC-6's concrete method
  text originate in AI planning outputs (this mission). US law requires
  natural-person inventors; treatment of AI-assisted conception is
  evolving. Counsel must review what was human-conceived vs
  machine-elaborated before any filing that touches those concepts.
- [ ] **Ownership:** SU-18 assignment scope for Tim (grad student) and any
  UW-side obligations of the co-authors to UW-Madison/WARF.
- [ ] **Sponsor rights:** DOE contract and SLAC FWP implications (Bayh-Dole
  election, government license, march-in exposure), NSF NNCI facility
  terms for the fabrication, TomKat gift/grant terms.
- [ ] **Materials terms:** the NTT-AT wafer purchase — any terms limiting
  IP on devices made from purchased epi material? (NOT ESTABLISHED FROM
  SUPPLIED FILES.)
- [ ] **International-student considerations** are a scheduling constraint
  only (MISSION.md); any visa-related question about founding/assigning IP
  goes to counsel, not this document.

## 5. Disclosure gates (each event, its gate, and what it exposes)

| # | Event | Earliest per current plans | What it discloses | Gate before it happens |
|---|---|---|---|---|
| G-A | July UW e-mail (feedthrough, mount survey, vacuum-field computation, shot list) | imminent (advisor decision #4) | CC-3 harness/cube specifics, CC-5 anchor method, to a third-party institution | Advisor confirms whether a confidentiality/collaboration framework covers it (§3); if none, advisor decides knowingly |
| G-B | SENSL resubmission of revised P1 | after WP-A/B/C close (stage 30 route A→C) | CC-1, CC-2 (chain + phase logic), CC-5 method, CC-6 conversion | §2/§3 conversations concluded; journal peer review is generally treated as confidential, but confirm with counsel rather than assume |
| G-C | arXiv posting (optional, of the *revised* version per stage 30) | at resubmission time, if chosen | Same as G-B but **public, permanent, irrevocable license** (stage 30 verified arXiv permanence) | **Hard gate — the advisor's explicit condition.** Only after advisor + OTL sign off; arXiv posting is the single most consequential disclosure event on the board |
| G-D | Conference talk/poster/abstract on the 2025 deployment or the readout | none scheduled in supplied files (verify with advisor) | Whatever the slides show — abstracts are public disclosures too | Same sign-off as G-C; inventory any *already-given* talks (NOT ESTABLISHED FROM SUPPLIED FILES — ask the group) |
| G-E | RSI vector-probe manuscript (P3) | ~Mar 2027 | CC-3 in full, CC-5 executed | Counsel review of CC-3 completed by ~Jan 2027 if any filing is contemplated |
| G-F | Public code/firmware repository (Pico firmware, demod scripts, gerbers) | not currently public per supplied files (verify) | CC-2 implementation detail; stage 40's reproducibility/release plan would publish analysis pipelines | Check repo visibility now; keep private until G-B decisions are made |
| G-G | Public demo, site visit, media, thesis defense/deposit | thesis far out; others unscheduled | Varies; thesis deposit is a publication | Same review path; note defenses can be embargoed — university procedures apply |
| G-H | P2 hybrid-architecture paper (WP-D) | months 6–18 | CC-4 | Counsel look at CC-4 only if WP-D produces something beyond PA-N19/N20's teaching |

## 6. Sequence and decision owner (no contact is made by this mission)

1. **Preserve** (§1) — owner: Tim; immediate; no external contact.
2. **Advisor conversation** (§2) — owner: Tim initiates; the advisor owns
   the go/no-go on spending OTL's time and on G-A timing.
3. **OTL screen** (§3, via Stanford's disclosure process) — owner: advisor +
   Tim jointly submitting, if step 2 says yes; OTL owns the
   evaluate/file/decline decision with registered counsel.
4. **Counsel questions** (§4) — owner: OTL/counsel; Tim supplies the §1
   record and this stage's ledger.
5. **Only then** release the gates in §5, in the stage 30 route's order
   (G-A may proceed earlier if the advisor accepts the third-party-sharing
   posture; that is the advisor's call, flagged here).
6. If steps 2–3 conclude "nothing to file" — a plausible outcome given the
   documented prior-art density — record that decision in writing and
   release G-B/G-C per the stage 30 route. The screen's value is that the
   decision was made deliberately, before disclosure, as the advisor
   required.

## 7. Official policy links (accessed 2026-07-25)

> **Warning: policies, fees, and law change; grace-period rules differ by
> country (many jurisdictions have absolute novelty with no US-style grace
> period). Verify each link and rule with OTL/counsel at decision time; the
> summaries below are pointers, not statements of current law.**

- Stanford OTL — policies on intellectual property (incl. SU-18 patent and
  copyright agreement context):
  <https://otl.stanford.edu/stanford-policies-intellectual-property>
- Stanford Research Policy Handbook — "Inventions, Patents, and Licensing":
  <https://doresearch.stanford.edu/policies/research-policy-handbook/intellectual-property/inventions-patents-and-licensing>
- Stanford — how to disclose an invention (Researcher Portal route):
  <https://doresearch.stanford.edu/how-to/disclose-invention> and
  <https://otl.stanford.edu/inventors/submit-invention>
- Stanford OTL — process overview:
  <https://otl.stanford.edu/researchers/otls-process>
- USPTO MPEP §2152 — AIA 35 U.S.C. 102(a)/(b) (prior art and the one-year
  inventor-grace-period exceptions):
  <https://www.uspto.gov/web/offices/pac/mpep/s2152.html>
- 35 U.S.C. §102 text (Cornell LII mirror of the U.S. Code):
  <https://www.law.cornell.edu/uscode/text/35/102>
- WIPO — Patent Cooperation Treaty portal (international filing route;
  confirmed live 2026-07-25):
  <https://www.wipo.int/pct/en/>

*All links were reached or extracted from official-domain search results on
2026-07-25; none of their content is restated as legal advice.*
