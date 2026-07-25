# Stage 00 — Input inventory

Prepared by: Claude Code, stage `00_inventory`, Sonnet 5 / High.
Scope: authoritative baseline only. No literature search performed in this
stage (per stage prompt).

All file-modification timestamps under `01_PhD_Research/` currently read
`2026-07-24` because the whole tree was copied/restored during the
`PHD_FABLE5_FINAL_RESTART...` operation. Filesystem `mtime` is therefore
**not usable evidence of original authoring/acquisition date** anywhere in
this inventory; dates below come from document content, filenames, or the
IEEE portal metadata, not from `mtime`.

---

## Group A — Mission input bundle (`inputs/`)

Authoritative for: what the user actually supplied and asked for; the exact
IEEE decision-letter text; submission timing.

| File | Identity / date | What it establishes | What it cannot establish | Format limitation |
|---|---|---|---|---|
| `inputs/ORIGINAL_REQUEST.txt` / `inputs/ORIGINAL_REQUEST_AND_SETUP.md` | Byte-identical (same SHA-256, verified: `ed0d3b1a...`); user-supplied | Verbatim original request text, including the embedded IEEE decision letter (Reviewer 1, Reviewer 2, Associate Editor comments, decline date "23-Jul-2026"), the Claude/Codex setup manifest, and the eight numbered mission asks in the user's own words | Nothing beyond what the user typed/pasted; the embedded decision-letter text is a copy, not the primary record | Plain text; the decision letter inside it is pasted, not the original PDF |
| `inputs/Decision_Letter_IEEE_2026-07-23.pdf` | IEEE Author Portal export; letter dated **23-Jul-2026**, email "Date sent: 22 July 2026 at 18:13 GMT-7" | Primary-source decision letter: Manuscript ID **SENSL-26-07-RL-1061**, decision = decline-with-invitation-to-revise (not accept, not reject-final), sender `sensl-admin@ieee.org`, AEIC Dr. Giacomo Langfelder, recipient `timzhao@stanford.edu` | Nothing about acceptance elsewhere or prior submission history | PDF is a browser print of the Author Portal page; text extracted cleanly via `pdftotext -layout` |
| `inputs/IEEE_submission_bundle_2026-07-02.pdf` | Atypon ReX submission export; "PDF Generation 02 Jul 2026 18:55:21 EST" | Primary-source proof of the **submission date (2 Jul 2026)**, full author/affiliation list, submission ID `b16111d9-5cc0-4019-a52d-6a06d1bf6edb`, list of submitted files (`regular_lsens.pdf`, `graphical_abstract.pdf`, `cover_letter.pdf`), and the full manuscript text as submitted | Reviewer identity beyond what the decision letter states; whether this is the final revised or only version (none other supplied) | PDF; extracted cleanly via `pdftotext -layout` |
| `inputs/regular_lsens_original.zip` | Preserved unmodified; extracted working copy lives at `../01_Publications/submitted/regular_lsens/` (Group B) | The zip is the authoritative frozen original of the manuscript source; the extracted copy is a working copy that must match it | Whether any post-hoc edits were made to the extracted copy (not diffed in this stage) | Zip archive; not opened directly, relied on the extracted copy |
| `inputs/07_HSX_august2025_results_original.zip` | Preserved unmodified; extracted copy at `../07_HSX_august2025_results/` (Group C) | Same relationship as above for the HSX raw-data archive | Same caveat — extracted copy not diffed against the zip in this stage | Zip archive; not opened directly |
| `inputs/INPUT_NOTES.md` | Mission-authored index of the above | States that the decision letter + submission bundle are authoritative for submission status/reviewer wording, and that parent-project reports are prior work, not automatically verified truth | — | — |
| `inputs/../INPUT_CHECKSUMS.sha256` | SHA-256 manifest at the mission root | All five `inputs/` files verified to match the manifest exactly (recomputed in this stage: `ed0d3b1a...` .txt/.md, `dd72739e...` decision letter PDF, `fa1563a0...` submission bundle PDF, `a4748e8e...` regular_lsens zip, `c4df6a8b...` HSX zip) | — | — |

## Group B — Manuscript source (`../01_Publications/`)

Authoritative for: exact manuscript claims, figures, structure, and the
in-preparation co-authored draft.

| Item | Identity/date | What it establishes | What it cannot establish | Limitation |
|---|---|---|---|---|
| `submitted/regular_lsens/regular_lsens.tex` (+ `.pdf`, `.aux`, `.log`, `graphical_abstract.pdf`, `figures/fig1–5`) | LaTeX source, IEEE Sensors Letters class; matches `IEEE_submission_bundle_2026-07-02.pdf` text | Full manuscript content — title, author list, abstract (both the active 150-word version and a commented-out ~250-word alternate), keywords, section/figure structure, and every calibration/bandwidth/shot-count claim currently made (detailed in `00_CLAIM_BASELINE.csv`) | Whether the manuscript was ever published — DOI and Associate Editor fields are blank in the source | Compiles to the same PDF as the submission bundle; a `1949-307X (c) 2023 IEEE` string at line ~438 is unedited IEEE_lsens.cls **template copyright boilerplate**, not evidence of publication (see `00_CONFLICT_LEDGER.md`) |
| `01_Publications/tim_ieee_sensors_letters_GaN_Hall_sensor_in_HSX_2023.pdf` (top level, outside `submitted/`) | Same byte size (1,838,044 B) as `regular_lsens.pdf`; identical title/abstract via text extraction | This is the **same compiled, unpublished manuscript**, just copied/renamed with a "_2023" suffix in the filename | Does **not** establish an actual 2023 publication — filename year is unverified and contradicted by the submission/decision evidence | Filename is misleading; flagged in `00_CONFLICT_LEDGER.md` |
| `in_preparation/vangorp_dawes_zhao_senesky_radiation_TCAD_sensitivity_modeling_DRAFT.pdf` | Word-exported PDF, author metadata "Thibaut Van Gorp" | Existence and rough scope of the co-authored TCAD radiation-sensitivity paper (Van Gorp, Dawes, Zhao, Senesky) — simulation-only (Sentaurus TCAD), models neutron displacement-damage and gamma total-ionizing-dose effects on AlGaN/GaN 2DEG Hall sensitivity | Any finished result — the Abstract field still contains unedited IEEE Word-template boilerplate ("This document provides a guide for preparing articles...") and body text contains incomplete notes (a stray French comment, "given by times x?? (formula)", "Need to be done for Ga, Al, N") | Early/incomplete draft; not usable as a citable result, only as evidence that this co-authored project exists and is simulation-only (consistent with the mission scope rule of no experimental radiation work) |

## Group C — HSX August 2025 raw data (`../07_HSX_august2025_results/`)

Authoritative for: what the HSX August-2025 bench/field data physically
contains and does not contain.

- Single subtree `hsx_20250821/`, ~23 MB, 230 files: 124 `.png`, 73 `.csv`
  (`scope_0.csv`…`scope_72.csv`, two-column `second,Volt`), 12 `.m` (MATLAB
  analysis scripts), 8 `.dat` (per-shot density/stored-energy diagnostics for
  shots 18/19/20/21), 7 `.fig`, 3 `.txt` (main-coil-current logs for shots 65
  and 68), 1 `.docx` shot log, 1 `.log` (an incidental JVM crash-replay log,
  not scientific metadata), 1 `.svg`, 1 `.eps`.
- **Shot/scope mapping**: no folder-per-shot structure; `scope_N.csv` files
  are numbered by acquisition order, not shot number. The only manifest tying
  scope files to shots, bias voltage, and plasma configuration is
  `hsx_20250821/test_note.docx` (e.g., "Scope 71, after 17:4 pm (0.4 V)
  Magnet shot 68 (no plasma)"). Distinct shots documented range from shot 9
  through shot 68.
- **What it can establish**: relative/qualitative sensor response in the
  bias-voltage domain (amplified `V_out`, time and FFT domain) as a function
  of applied bias voltage (0.2–0.4 V, or 0 V "sensor off") and plasma
  shot/configuration; this matches the manuscript's Fig. 4/5 data.
- **What it cannot establish**: any absolute magnetic-field (Tesla/Gauss)
  value. No gain factor, sensitivity (V/T), sensor part number, or
  calibration curve exists anywhere in the tree — all `.m` scripts operate
  purely in Volts, subtracting only a fixed `amp_offset = 4 mV`. This
  corroborates the user's own framing ("only bias voltage is known, other
  variables were unknown") and the manuscript's explicit statement that
  absolute calibration is future work.
- **Sufficiency for quantitative re-analysis**: sufficient to reproduce the
  manuscript's existing qualitative/relative-comparison figures (signal
  amplitude and FFT vs. bias voltage and shot); **not sufficient** to derive
  a new absolute B-field calibration without external data (a sensor
  sensitivity coefficient, amplifier gain, and a known-field reference) not
  present in this archive.
- Acquisition date inferred from folder/filename content (`hsx_20250821`,
  `25_8_21_#18_*`) and `test_note.docx` timestamps as **2025-08-21**,
  10:33 a.m.–~17:41 p.m.; no independent filesystem corroboration survives
  the archive restore.

## Group D — Project 02, `HSX_Hall_Sensor_Readout` (single-axis, active, Aug 2026 target)

- `CLAUDE.md`, `docs/SPECS.md`, `NOTES.md` (5 entries, all dated 2026-07-06
  or 2026-07-08; **no entries after 2026-07-08** as of today 2026-07-24),
  `circuit/` (LTspice + KiCad netlists, cross-verified pin-by-pin, gerber
  order package), `firmware/pico2/` (two operating modes), `analysis/`
  (`hsx_demod_scope_csv.py`, `spin_verify_nosync.py`), `data/` (one bench
  capture, `2026-07-08_test_spin.csv`), `journal/` (one dated entry).
- **What it establishes as bench-verified fact**: current-spinning readout
  design exists (netlists cross-checked), as-built R9 = R10 = 100 Ω,
  AD8429 gain R_G = 60.4 Ω ("reads ≈59.8 Ω in-circuit"), a 2026-07-08 dynamic
  spin run on a resistor-ring emulator (not the real GaN die) demonstrated
  offset cancellation from 686 mV raw to ≤5 mV (≥130×).
- **What it cannot establish**: any completed absolute calibration (the
  Helmholtz-coil calibration procedure in `SPECS.md` is specified, not run),
  hardware-validated static-bias firmware (Mode 2, "smoke-tested... with the
  Pico hardware stubbed" only), or field-readiness for the August 2026 HSX
  install (no field deployment evidence exists).
- **Open blocker on record**: an unresolved ~109× magnitude discrepancy
  between the measured 0.686 V raw offset and a ~75 V predicted rail value,
  logged as "top priority" with an explicit instruction not to calibrate
  against these magnitudes until closed. This is a live, unresolved
  engineering gap, not a resolved fact.
- **Reuse status**: bench-verified circuit/firmware/offset-cancellation
  results may be cited as prior-project claims once cross-checked against
  `NOTES.md`/`SPECS.md` (done here); the calibration and install-readiness
  claims may **not** be reused as achieved facts.

## Group E — Project 03, `HSX_Vector_Probe_RSI2026` (2–3 axis, planning, RSI ~Mar 2027)

- Only 7 items: `CLAUDE.md`, `NOTES.md` (2 entries, both ≤2026-07-08),
  `.claude/settings.json`, and `docs/rsi_experiment_and_publication_plan.md`
  (+ HTML mirror). **No hardware, code, CAD, or data files exist in this
  folder** — everything built (firmware, netlists) lives in the sibling
  Group D folder and is referenced only by relative path.
- **What it establishes**: a fully committed plan — target journal Review of
  Scientific Instruments, target submission "~March 2027"; thesis statement
  ("first absolutely calibrated, multi-axis... GaN Hall-effect probe operated
  inside a stellarator... upgrading 2023's 'temporal correlation' to numbers
  with uncertainties"); a month-by-month timeline (Jul 2026 bring-up → Aug
  2026 HSX campaign #1 single-axis → Sep/Oct 2026 gen-2 die + 3-channel bench
  work → Nov 2026 HSX campaign #2 → Feb 2027 draft → ~Mar 2027 submit); an
  8-item risk register; a rough BOM (~$120/board + ~$95 misc, cube machining
  cost explicitly "quote needed — the one real unknown").
- **What it cannot establish**: that any of this has happened. Campaign #2
  (Nov 2026, the paper's primary data source) has not occurred; multiple
  design points are explicitly still open ("Design points to settle in
  September," 2-vs-3-axis "commit to... decide," feedthrough connector
  undecided, DAQ/scope-memory strategy undecided).
- **Strategic note for later stages**: this folder already treats the 2023
  Sensors Letters manuscript as a *closed, published* prior work whose
  stated limitations (uncalibrated offset, single axis, temporal-correlation
  only) the RSI paper is designed to resolve — it does **not** treat
  "revise-for-Sensors-Letters vs. arXiv+RSI" as an open question. This
  planning assumption inherits the same publication-status conflict recorded
  in `00_CONFLICT_LEDGER.md` and should not be treated as settled by later
  stages without re-derivation from the decision letter.

## Group F — Project 04, `Magnetic_Sensor_Review_Sensors2026` (prior review-paper pipeline)

- A separately-scoped, already-executed 9-stage review pipeline (`run.ps1`,
  headless `claude -p` stages) targeting MDPI *Sensors*, submission target
  "before 30 Oct 2026." Completed run dated 2026-07-10 (per its own
  `NOTES.md`).
- Ledger: `outputs/reference_registry.csv`, header
  `key,authors,year,title,venue,type,doi,url,peer_reviewed,status,sections_used,confidence,notes`,
  **122 reference rows** (16 seed + 108 retrieved). Its own Stage-70 report
  states DOIs were "left as-is (not re-fetched individually)" for most
  entries and only ~2 entries were independently Crossref-confirmed; status
  breakdown per that report: 80 peer-reviewed journal, 16 vendor-grey, 13
  standards, 4 preprint, 2 market-report-grey, 2 book chapter, 2 peer-reviewed
  conference, 2 non-peer-reviewed conference, 1 monograph.
- **Reuse status**: a **plausible seed list only**. It (a) falls short of the
  150-verified-peer-reviewed-source minimum on its own, (b) has
  self-reported, not independently re-verified, peer-review status for most
  rows, and (c) is scoped to a general sensor-review paper independent of the
  HSX/GaN-fusion projects, so its topic coverage does not automatically match
  `SOURCE_POLICY.md`'s required coverage areas. Any row reused in the
  150-paper ledger (stages `10a`–`10d`) must be independently re-verified
  (DOI resolution / publisher record) before being counted, per
  `SOURCE_POLICY.md`.

## Group G — Project 05, `HSX_ChatGPT_Windows_App` (unrelated prior design package)

- A **self-contained, already-largely-executed engineering-design workspace**
  (packaging/readout decision for the Hall-sensor LCC/wire-bond/harness
  design), explicitly built to be opened in the ChatGPT Windows desktop app,
  not Claude Code (`PACKAGE_MANIFEST.md`: "Explicitly absent: PowerShell
  runners... `.claude`, Claude settings/agents, or `CLAUDE.md`").
  `outputs/FINAL_ACCEPTANCE_CHECKLIST.md` (2026-07-12) declares
  `COMPLETE_WITH_OPEN_GATES` (fabrication/purchase release still `FAIL/HOLD`),
  while `state/PROJECT_STATE.md` (2026-07-13) shows a later, unfinished
  cost-down revision pass (`IN_PROGRESS`) — **the two status files disagree**,
  recorded here as an open item, not resolved by this stage.
- **Important disambiguation**: this folder is *not* the infrastructure
  behind this mission's `MODEL_POLICY.md` "Manual ChatGPT Windows
  continuation" fallback. The actual fallback files
  (`CHATGPT_WINDOWS_START_PROMPT.md`, `CHATGPT_WINDOWS_CONTINUE.md`,
  `AGENTS.md`) live at the `01_PhD_Research/` root, use this mission's own
  `state/` schema (`CHATGPT_HANDOFF_STATE.json`, `OPERATION_LOG.csv`, etc.),
  and are unrelated in content to Group G's packaging design state schema.
  Group G should not be assumed to satisfy or represent the current
  mission's continuation mechanism.
- **Reuse status**: out of scope for the strategy/publication mission's
  content (it is a mechanical/packaging design exercise, not literature,
  manuscript, or PhD-strategy content); noted for completeness per the stage
  prompt's instruction to inspect it, not carried forward as evidence.

## Group H — Parent root memory (`../CLAUDE.md`, `../01_PhD_Research_Folder_Info.md`)

- Both files assert the same trajectory claim: *"2023 — IEEE Sensors Letters
  (1st author, published)"* / *"Demonstrated in-situ (2023 Letters)."* This
  is **parent-project prior-project narrative, not independently verified
  fact**, and it directly conflicts with the primary-source decision letter
  and submission bundle in `inputs/` (submission 02-Jul-2026, decline
  23-Jul-2026, no acceptance record supplied). See `00_CONFLICT_LEDGER.md`
  for the full analysis; this inventory does not resolve the conflict, only
  records where each claim originates.
- Per `INPUT_NOTES.md` and the mission's `SOURCE_POLICY.md`/operating rules,
  parent root memory is background context, not ground truth, when it
  conflicts with supplied primary evidence.

---

## Manuscript section/figure/table map (from Group B)

| Section | Content |
|---|---|
| I. Introduction | Motivation (drift in inductive diagnostics), HSX description, novelty statement (1 MHz readout bandwidth claim, 68 shots) |
| II.A Fabrication | AlGaN/GaN octagonal Hall plate, 200 µm inscribed diameter, 5×5 mm die |
| II.B Packaging | Ceramic leadless chip carrier, epoxy coat, custom flange |
| II.C Experimental Setup | Voltage bias via oscilloscope waveform generator; differential readout chain |
| III.A Sensor Functionality | Biased-vs-unbiased and plasma-vs-coil-only comparisons (shots 63, 65, 68) |
| III.B Real-Time Plasma Energy Tracking | Temporal correlation with diamagnetic-loop stored energy (shots 21, 18, 19) |
| IV. Conclusion | Restates 68-shot functionality claim; lists absolute calibration as future work |
| References | 20 entries (`Ongena2016`, `Degrave2022`, `Anirudh2023`, `ref1`–`ref17`) |

| Figure | Caption subject | Shots shown |
|---|---|---|
| Fig. 1 | Cross-section schematic + optical image of fabricated die | — |
| Fig. 2 | Packaging / in-vessel mounting | — |
| Fig. 3 | Readout configuration (bias + amplifier chain) | — |
| Fig. 4 | Biased vs. unbiased; plasma-discharge vs. coil-only | 63, 65, 68 |
| Fig. 5 | Stored energy vs. sensor output, 3 discharge classes | 21 (high-energy), 18 (late-breakdown), 19 (failed-breakdown) |

No tables are present in the manuscript. Two numbered equations exist:
`V_H = S_v · V_bias · B` and `V_out = A_v · V_H + V_off`.

## Decision-letter editor/reviewer map

| Role | Identity | Position |
|---|---|---|
| Associate Editor-in-Chief (AEIC) | Dr. Giacomo Langfelder | Signed the decline letter; primary concern = novelty ("only showing changes in sensing values, not... magnetic field"); asked for a GaN-sensor comparison table, repeatability statistics across fabrication iterations, bench-top calibration at minimum, and Fig. 5 shown in field units, not just voltage |
| Reviewer 1 | Anonymous | Supportive overall ("device itself is novel and unique to my knowledge... worth publishing"); asks for bench-top calibration or comparison to a conventional field probe (B-dot/Mirnov); minor points on the 1 MHz bandwidth justification and a missing Endler-W7X re-citation |
| Reviewer 2 | Anonymous | Not supportive ("this paper lacks sufficient novelty"); cites insufficient repetitive testing/accuracy calibration and insufficient literature citation of prior GaN Hall-device work; recommends rejection |
| Decision outcome | — | **Decline with invitation to revise and resubmit under a new manuscript ID** (not a final reject, not an accept) |

## HSX data/shot/script map

See Group C above for the full breakdown; summarized shot coverage:
shots 9–68 (magnet-only baseline range per `test_note.docx`), with named
diagnostic sets for shots 18, 19, 20, 21 (density/stored-energy `.dat` +
overview `.png`) and main-coil-current logs for shots 65 and 68. Analysis
scripts (`figure3_in_pub.m`, `figure3b_in_pub.m`, `figure4.m`, `figure5.m`,
`bigfigure.m`, `halfqhs.m`, `figure2d_tomkat.m`, `1T_qhs_backup.m`,
`qhs_1T_fft.m`, `hsx_test_result_matlab.m`) all operate on raw
`scope_N.csv` voltage traces and reproduce the manuscript's Fig. 4/5-style
plots; none contain a Tesla/Gauss conversion.

## Prior-project outputs reusable only after verification

1. Group D (project 02) bench facts: circuit netlist cross-check, as-built
   resistor values, amplifier gain, and the 2026-07-08 offset-cancellation
   result — reusable as prior-project claims once the ~109× open anomaly is
   flagged alongside them (it is, in `00_CLAIM_BASELINE.csv`).
2. Group E (project 03) plan — reusable as the user's stated intended RSI
   route, not as an accomplished result.
3. Group F (project 04) reference registry — reusable only as a candidate
   seed list for stages `10a`–`10d`, subject to full independent
   re-verification per `SOURCE_POLICY.md`; does not by itself satisfy the
   150-verified-source minimum.
4. Group G (project 05) — not reused; out of topical scope for this mission.

## Note on subagent tool behavior during this survey

Two of the six read-only survey subagents used in this stage returned a
harness-generated notice ("subagent output matched instruction-shaped
pattern(s): settings-json") before their findings. Inspection of the
underlying content (`03_HSX_Vector_Probe_RSI2026/.claude/settings.json`:
`{"model": "opusplan", "effortLevel": "medium"}`, and a similar file in
Group D) shows this is ordinary, benign Claude Code settings JSON that
structurally resembles an instruction payload — not an actual prompt-
injection attempt. Recorded here for completeness per the operating
instruction to flag suspected injection; no action beyond this note is
warranted.
