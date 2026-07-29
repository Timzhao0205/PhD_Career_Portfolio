# NOTES — 04_Magnetic_Sensor_Review_Sensors2026 (newest first)

## 2026-07-10 — full pipeline run completed (stages 00–80; stage 90 digest written)
- All 9 stages executed successfully on Fable 5 (titles, outlines, sensor taxonomy, future methods, assembly), Opus (applications, standards), and Sonnet (journal brief, bibliography). Total cost USD 27.44, ~66 minutes.
- 122 references in registry (16 seed + 108 retrieved across stages); 124 total sources logged; ~80 peer-reviewed journal/conference, ~20% grey/preprint/vendor, all flagged. DOIs verified per Stage 70 audit.
- Deliverable: recommended title, A+B-hybrid outline, coverage matrix (15 families × 5 dimensions), gap analysis, journal-fit checklist (all structural requirements met; figures/tables/abstract/keywords remain). Section-by-section annotated brief ready for drafting.
- Critical gaps: performance-number full-text extractions (Stage 30 re-run with existing sources closes most Thin cells), preprint-to-VoR hunts (Stage 50 re-run for ISO26262+ML and MagNav sources), bibliography author-field cleanup (Stage 70). No blockers to manuscript drafting.
- Next patch sequence in `outputs/PATCH_NOTES.md`: Stage 30 extraction → Stage 50 VoR hunt → Stage 70 hygiene → (manual author self-citation insert) → manuscript drafting from templates.

## 2026-07-08 — pipeline scaffolded (not yet run)
- Automated review-paper pipeline built for MDPI *Sensors* (submission < 30 Oct).
  One command: `powershell -ExecutionPolicy Bypass -File .\run.ps1`.
- 10 staged headless `claude -p` calls (prompts/00–90), per-stage model + effort
  set from PowerShell. Fable 5 on the critical parts: titles (10), outlines (20),
  sensor taxonomy (30), future-methods (50), final assembly (80). Opus on
  applications (40) + standards (60); Sonnet on journal brief (00) + bibliography
  (70); Haiku on patch notes (90).
- Source integrity enforced in `prompts/_shared_system.md`: no fabricated cites,
  peer-reviewed preferred, preprints for discovery only, every source logged to
  `refs_raw/*.jsonl`, DOIs verified in Stage 70.
- Verified seed of ~16 real anchor refs in `refs_raw/00_seed.jsonl`.
- Logs + cost/model/effort table land in `logs/run_<stamp>/`; deliverables in
  `outputs/`. Nothing has been run yet — first `run.ps1` will populate both.
- Next: run `.\run.ps1 -OnlyStage 10,20` first for the Friday title+outline
  deadline, review, then run the full pipeline.
