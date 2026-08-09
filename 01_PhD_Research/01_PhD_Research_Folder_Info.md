# 01_PhD_Research — folder index

Research arc: GaN Hall-effect magnetic sensing for fusion diagnostics
(HSX stellarator). Demonstrated in-situ (2023 Letters) → calibrated
spinning-current readout (02, HSX install Aug 2026) → calibrated 2–3
axis vector probe + second HSX campaign (03, RSI paper, ~Mar 2027).

Folders `01`–`03` are the experimental line. `04`–`10` are analysis and
strategy packages built around it — each is a self-contained Claude Code
project with its own `CLAUDE.md`, run scripts, and durable state.

## The experimental line

- `01_Publications/` — `tim_ieee_sensors_letters_GaN_Hall_sensor_in_HSX_2023.pdf`
  is the published Letters paper. `submitted/regular_lsens/` holds the full
  LaTeX project for the manuscript submitted 2026-07-02 (sources, figures,
  class file, compiled PDF). `in_preparation/` holds co-authored drafts —
  currently Van Gorp et al., radiation TCAD modeling, simulation only.
- `02_HSX_Hall_Sensor_Readout/` — single-axis spinning-current readout:
  bring-up + calibration plan and second-test-setup doc (`docs/`),
  one-page quick reference (`docs/SPECS.md`), Pico 2 firmware in two
  operating modes — spin+scope and static-bias-p2/p4 — (`firmware/
  pico2/`), scope demod CLI (`analysis/`), netlists/schematics/gerbers
  (`circuit/`), running log (`NOTES.md`).
- `03_HSX_Vector_Probe_RSI2026/` — vector-probe experiment and RSI
  publication plan (`docs/`), running log (`NOTES.md`).
- `07_HSX_august2025_results/` — raw and reduced data from the August 2025
  HSX campaign: 1 T QHS shots, FFT products, plots.

## Analysis and strategy packages

- `04_Magnetic_Sensor_Review_Sensors2026/` — review-paper pipeline for
  *Sensors*. Staged prompts (`prompts/`) → per-stage results (`outputs/`,
  `logs/`), bibliography in `outputs/references.bib` +
  `reference_registry.csv`. `advisor_review/` holds the advisor's marked-up
  abstract and the accepted-changes render.
- `05_HSX_ChatGPT_Windows_App/` — UHV/250 °C package and three-board readout
  architecture study: LCC wirebond qualification, pin/cable maps, CAD concepts
  (`outputs/cad/`), drawings (`outputs/drawings/`), red-team and final
  recommendation. Earlier iteration kept in `previous_results/`.
- `06_PhD_Strategy_and_HSX_Publication_2026-07/` — PhD direction, literature,
  manuscript, experiment, patent and timeline analysis. Current run in
  `outputs/`/`logs/`/`state/`; the earlier attempt is preserved under
  `_history/r0/`.
- `08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/` — Hall + pickup-coil hybrid
  sensing under radiation: estimator, risk register, application scorecard,
  technology comparison and collaborator candidates, all Crossref-audited
  (`tools/redteam_*`).
- `09_PAP06_Career_Portfolio_Synthesis_2026-07/` — the PAP06 native package.
  Operation A reconstructs the score-free 126-idea blind pool; Operation B runs
  PhD core → literature → alignment → power → skills → portfolio → execution
  over the combined PhD and startup corpora. Paused at stage B50; see
  `state/PROGRESS.md`. Its `sources/` input snapshot is deduplicated against the
  rest of this repository — see `sources/README.md`.
- `10_HSX_IP_and_arXiv_Screen_2026-08/` — publication-only IP triage for the
  submitted manuscript: disclosure map, prior-art search, claim chart, UHV/GDC
  package verdict, arXiv posting risk, OTL intake brief. Verdict:
  `NO_PUBLICATION_SPECIFIC_FILING_CASE_IDENTIFIED`, with a pre-posting
  ownership/sponsor checkpoint still recommended. Start at
  `outputs/70_EXEC_SUMMARY.md`.

## Conventions

- Reader-friendly `.html` mirrors sit next to each plan/report `.md`
  (open in any browser; `reports_index.html` at this level links them).
  Regenerate the mirror whenever its markdown changes: `python3 tools/md2html.py`.
- `CLAUDE.md` + `.claude/` — Claude Code memory, budget defaults
  (opusplan + medium effort), slash commands (`/log`, `/specs`,
  `/deep`), and the `rsi-editor` review agent. Launch `claude` from
  THIS folder so the commands and agent are picked up.
- Packages `04`–`10` each carry their own `CLAUDE.md` that is binding inside
  that folder. Launch `claude` from the package folder when working in one.
- `UPDATES_2026-07-08.md` records the 2026-07-08 firmware/docs drop.
  `../REORGANIZATION_2026-08.md` records the 2026-08-08 cleanup.
