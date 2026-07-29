# PHD_CORE — PhD research core (FULL)

This is the full-run PHD_CORE artifact for stage `B10_phd`. It extends
`pilot/B10_phd/attempt-1/PHD_CORE.md` (a 10-claim sample) to the full
`sources/phd` corpus sweep. It synthesizes `PHD_FACTS.json`'s 50 claims
(C01-C50); every substantive statement below is claim-ID cross-referenced.
Extraction, not ranking: nothing below scores, ranks, recommends a
portfolio decision, or repeats a corpus scorecard's numbers as this
extraction's own judgment.

## 0. Corpus map swept for this run

- **Folder 06** (`sources/phd/P/01/06/`) — completed PhD-strategy mission,
  31 output files, all read (skim-to-full depth; see RUN_META.md), red-team
  audited (C39), `FINAL STATUS: PASS`.
- **Folder 08** (`sources/phd/P/01/08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/`)
  — the "Opt2" hybrid/radiation continuation mission, 25 output files, all
  read, **pre-redteam/pre-synthesis (10/12 stages, C40)** — every claim
  drawn from it carries that caveat.
- **Raw/project folders characterized**: `01_Publications/` (C11, C12,
  C20, C21, C22), `02_HSX_Hall_Sensor_Readout/` (C03, C04, C13, C15),
  `03_HSX_Vector_Probe_RSI2026/` (C14), `04_Magnetic_Sensor_Review_Sensors2026/`
  (C18), `05_HSX_ChatGPT_Windows_App/` (C19), `07_HSX_august2025_results/`
  (C01, raw campaign data — 230 files characterized at directory level per
  C01/C22's evidence and the pilot's Group-C reading; the full byte-level
  contents were not individually opened beyond what the corpus's own
  stage-00 inventory already established and this run's own Glob
  confirmation of file counts/types).
- **External verification performed this run**: the decision letter PDF
  (C02, C05, C22) and the live IEEE Sensors Letters author-guidance page
  (C36) were opened directly, not relayed through a corpus synthesis
  document.

## 1. Recent/current work, as evidenced by the full claim set

- **Deployment (demonstrated, C01).** A packaged AlGaN/GaN Hall-effect
  sensor module was fabricated, packaged, and deployed in-vessel near the
  HSX stellarator plasma edge during the August 2025 campaign. Raw
  shot-resolved voltage transients and a qualitative correlation with
  diamagnetic-loop stored energy exist in the raw data archive (230 files
  under `sources/phd/P/01/07_HSX_august2025_results/hsx_20250821/`), which
  contains no gain/sensitivity/calibration factor anywhere — it supports
  reproducing existing qualitative figures, not a new absolute-field
  derivation.
- **Publication status (demonstrated, directly re-verified, C02, C22,
  C49; the manuscript's own disputed 1 MHz bandwidth figure remains
  separately tracked as unknown, C05).** The resulting manuscript (IEEE
  Sensors Letters, Manuscript ID SENSL-26-07-RL-1061) was submitted
  2-Jul-2026 and declined 23-Jul-2026, with an invitation to revise and
  resubmit under a new Manuscript ID. This run opened the decision letter
  PDF directly (not through a corpus summary) and confirmed the
  Associate Editor's novelty concern and four specific requests
  (comparison table, repeatability statistics, bench calibration,
  Fig. 5 in field units), Reviewer 1's supportive-but-incomplete
  assessment ("novel and unique... still worth publishing"), and
  Reviewer 2's rejection recommendation. Zero accepted first-author
  publications currently exist across every publication
  track in the corpus (C49): the manuscript above (declined), the
  co-authored TCAD paper (early incomplete draft, C20), the magnetic
  sensor review (planning stage only, C18), and the RSI vector-probe
  paper (not yet written; its campaign has not occurred, C14).
- **A widespread "2023, published" provenance conflict (demonstrated,
  C11, C12).** At least five corpus documents outside the strategy
  missions (parent CLAUDE.md, folder index, project-02 CLAUDE.md, project
  03's RSI plan, and project 04's own paper-plan document) assert or
  assume the manuscript was published in 2023. This is directly
  contradicted by the primary submission bundle and decision letter, and
  the likely mechanical source is an unedited IEEE class-template
  copyright-boilerplate string plus a misleadingly renamed duplicate PDF.
  Notably, project 04's own review-paper pipeline independently caught
  this and refused to auto-insert the citation, flagging it
  `[UNVERIFIED]` for the author to add manually — an internal
  cross-check the corpus performed on itself.
- **Bench readout-architecture validation (demonstrated, C03/C04, with a
  cross-project corroboration found this run, C04's refinement).** On a
  resistor-ring bench emulator (not the real sensor die), current-spinning
  demodulation suppressed a raw offset by >=130x — but the same test also
  produced an unresolved ~109x magnitude anomaly relative to the expected
  bridge output. This anomaly is not a one-off: the independent
  three-board vector-probe packaging design (project 05) lists an
  "X/Y/Z approximately 109-times anomaly root-cause" as one of its own
  unchecked hardware release gates, suggesting this is a standing,
  cross-project blocker. The project's own rule is that no calibration
  work may start until it is closed.
- **Unverified figure (unknown, C05).** The manuscript's stated 1 MHz
  readout bandwidth is asserted twice with no derivation anywhere in the
  manuscript, its references, or the project's own specs. The reviewer
  letter (directly re-verified this run) explicitly disputes it. This
  ledger marks the true bandwidth as unknown rather than accepting the
  manuscript's own unverified figure.
- **Vector-probe successor instrument planned but not built (proposed,
  C14).** A fully specified 2-3-axis ceramic-cube vector probe design
  exists (matrix calibration, phase-locked synchronized spinning, in-situ
  vacuum-field anchor), targeting RSI submission ~March 2027 — but no
  hardware, code, CAD, or data exists in the project-03 folder itself.

## 2. Assets, as evidenced by the full claim set

- **Hardware/firmware.** A packaged, previously-deployed AlGaN/GaN Hall
  sensor module and its readout electronics: cross-checked LTspice/KiCad
  netlists, an ordered gerber package, as-built resistor/gain values, and
  two Pico 2 firmware modes (C13). The packaging *process* itself (LCC,
  Al wedge bonds, EPO-TEK 353ND, 150C vacuum bake, zirconia holder,
  grounded graphite GDC shield) is demonstrated once (the 2025 deployment)
  and planned for reuse, unmodified, on the vector-probe cube (C46) —
  though vertical-face bond yield on the cube is an explicitly
  unresolved, never-before-solved risk.
- **Raw data.** The 2025 HSX campaign archive (C01) — usable for further
  supplied-data analysis without new hardware or campaign time, but
  insufficient by itself for absolute calibration.
- **A second, independent hardware-packaging design track (proposed,
  C19).** A separate ChatGPT-Windows-based mission produced a full
  die/LCC/fanout, three-board isolated-readout, and ceramic-cube
  packaging design with CAD, self-reporting `COMPLETE_WITH_OPEN_GATES`
  after an independent red team found 8 BLOCKER + 14 MAJOR findings (all
  with stated corrections); fabrication/purchase is explicitly on HOLD,
  and this track is not adopted by, or integrated with, folders 06/08.
- **Evidence infrastructure.** Two independently built, DOI-verified
  source ledgers: 231 rows (folder 06, C16) and 219 rows (folder 08, C17,
  pre-redteam), together spanning GaN device physics, Hall-sensor
  metrology, fusion diagnostics, stellarator context, calibration
  traceability, hybrid/coil-fusion, radiation effects, and application
  alternatives. **Provenance caveat (C50):** this ledger-building,
  scoring, and planning work was produced by autonomous AI-agent research
  missions the researcher commissioned and directed, not hand-executed
  literature-review labor — a distinction that matters for how any of
  these assets should be read in a PhD-portfolio or transferable-skills
  context. The bench/hardware work (C01, C03, C04, C13, C46) is a
  separate, directly researcher-attributed category (dated lab-notebook
  entries), not an AI-mission output.
- **A documented, not-yet-executed calibration plan (WP-C, C06) and a
  documented, not-yet-built reusable simulation/estimator package
  specification (C10), refined this run by an integrity gate (FT-02, C31,
  C48) that requires the future estimator to visibly fail (freeze states,
  inflate uncertainty) on cases the theory proves are non-identifiable,
  rather than silently converging on a confident wrong answer.
- **A parallel, separately-scoped literature-review paper project**
  (C18) — outline, title, and a 122-reference registry for an MDPI
  Sensors submission target of 30 Oct 2026 — not integrated into folders
  06/08's roadmap, and itself only self-reported peer-review status for
  most of its rows.
- **A completed IP research screen** (C33, C34) — six candidate
  protectable concepts, a prior-art ledger citing active competitor
  patent families and the advisor group's own 2019 publications, and an
  eight-gate disclosure checklist — concluding that any protectable scope
  is expected to be thin, not a platform claim, and explicitly reaching
  no patentability/ownership/FTO conclusion.

## 3. Evidence quality, as evidenced by the full claim set

- Demonstrated current-work claims (e.g. C01-C04, C11-C13, C20-C22, C41,
  C44, C46, C49; note C05, C15, and C45 are deliberately marked `unknown`
  rather than `demonstrated`, and C14, C18, C19 are deliberately marked
  `proposed` — see PHD_FACTS.json for the exact status of every claim)
  trace to primary artifacts: raw HSX data files, dated
  lab-notebook-style NOTES.md/journal entries, the manuscript source and
  its LaTeX boilerplate, and — for C02/C05/C22, directly re-opened this
  run — the primary decision-letter PDF itself, closing a limitation the
  pilot had explicitly flagged (it had only read a corpus summary of the
  letter).
- The Opt2-related claims trace to two evidence tiers of different
  maturity: folder-06-sourced claims (C06, C33-C39, C41-C42, C44,
  C47, C49) rest on a completed, independently red-team-audited (C39)
  mission with a `FINAL STATUS: PASS`; folder-08-sourced claims (C07-C10,
  C17, C23-C32, C40, C43, C48) rest on a mission that has completed only
  10 of 12 planned stages and has **not** passed its own `70_redteam` or
  `80_synthesis` steps (C40, independently reconfirmed this run by a
  direct Glob returning exactly 25 output files, no redteam/synthesis
  file). Every claim citing folder 08 states this caveat individually.
- One claim in this ledger (C23) upgrades the evidentiary framing found
  for C07: the plain-language "mutual calibration is only partly
  feasible" verdict rests on a formally labeled *Derived* mathematical
  result (Theorem 1, a two-parameter structural non-identifiability
  proof) with a reproducible numerical confirmation, not merely an
  *Inferred* qualitative judgment — though this ledger keeps C07's own
  status label ("inferred") stable per the task's instruction not to
  change kept claims' substance, and records the stronger evidence as an
  explicit refinement note plus the separate claim C23.
- External verification performed directly by this extraction (not
  relayed): the decision letter (C02/C05/C22) and the live IEEE Sensors
  Letters author-guidance page (C36), which matched the corpus's own
  earlier-cited figures exactly as of this run's access date
  (2026-07-28).

## 4. Gaps, as evidenced by the full claim set

- No calibration of the real (non-emulator) Hall die exists (gap behind
  C06, blocked by C04's open anomaly and by C45's unresolved question of
  whether the deployed 2025 module can even be located).
- No hardware demonstration of coil->Hall gain tracking exists in fusion
  conditions; the coil->Hall direction rests on a formal structural proof
  (C23) plus a single non-fusion precedent (C07, C30).
- No GaN/AlGaN Hall-plate radiation dataset exists in the literature
  reviewed by either corpus ledger (C29); the radiation-drift magnitude
  for this device family is Unknown, and cross-species scaling has failed
  by ~14x in one cited comparable case, meaning a wrong-species screening
  campaign would be actively worse than none (C29).
- The broad "hybridize a Hall sensor with a coil" idea is not novel —
  26 years of direct prior art exists — and the corpus's own narrowest
  defensible contribution is four specific, narrower open gaps (C26), not
  the architecture concept itself.
- Six documented application niches exist where a simpler,
  single-technology sensor is stated to outright beat the proposed hybrid
  (C27), and a competing single-channel technology (TMR) already spans
  DC-to-broadband with demonstrated gamma-radiation tolerance, directly
  challenging the hybrid's core value proposition in at least one regime
  (C43).
- No reusable simulation/estimator code has been built yet; only a module
  boundary specification and an integrity-gate design exist (C10, C31,
  C48).
- The deployed 2025 module's post-campaign location, custody, and health
  are undocumented anywhere in the corpus — the single most consequential
  open inventory question, gating both repeatability statistics and the
  retroactive field-unit conversion of the existing 2025 dataset (C45).
- This full run still did not open every one of the 1,145 files in
  `sources/phd`; large supporting CSVs (e.g. folder-06's full
  `01_LITERATURE_REVIEW.md` narrative text and folder-08's
  `01_HYBRID_LITERATURE_REVIEW.md`/`01_RADIATION_LITERATURE_REVIEW.md`
  bodies, `01_EVIDENCE_MAP.csv`, and several application/collaborator
  CSVs) were characterized through their own stage's summary/coverage
  documents and cross-referencing narrative reports rather than read row
  by row — a proportionate skim given the aggregate statistics those
  summary documents independently validate (e.g. `01_SOURCE_COVERAGE.md`
  in both folders).

## 5. Transferable skills, as evidenced by the full claim set

**Demonstrated directly by the researcher (dated bench/lab-notebook
evidence, C01, C03, C04, C13, C46):** in-vessel sensor packaging and
deployment in a live fusion research device (UHV-compatible LCC
packaging, wire bonding, encapsulation, vacuum bake, GDC-survivable
shielding); bench emulator-based readout-chain design; current-spinning
bias/demodulation circuit design and firmware development across two
operating modes; systematic bench-anomaly diagnosis under an explicit
no-calibrate-until-resolved discipline; primary-source manuscript/decision
-letter review and reviewer-response planning.

**Proposed skill areas the Opt2 continuation would exercise, not yet
demonstrated on real hardware (C06, C10, C23-C25, C31, C48):** traceable
absolute calibration methodology (GUM/Monte-Carlo uncertainty budgeting);
formal structural-identifiability analysis of multi-sensor systems;
estimator-honesty/integrity testing before hardware commitment;
multi-channel sensor-fusion estimator design; scientific software
packaging with a frozen interface/regression discipline.

**A distinct provenance category, flagged for portfolio honesty (C50):**
the large-scale literature-ledger construction (450 combined rows across
two missions), direction scoring, IP screening, application scorecarding,
and 24-month roadmap planning visible throughout folders 06/08 were
produced by AI-agent research-strategy missions the researcher
commissioned and directed via detailed prompts and policy files, not
hand-executed by the researcher personally. Commissioning, scoping,
reviewing, and acting on this kind of AI-assisted research-planning
pipeline is itself a real and increasingly relevant skill, but it should
not be conflated with, or presented interchangeably as, personally
performed systematic literature review, direction-setting analysis, or
IP screening in any CV or portfolio document.
