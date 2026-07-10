# 04_Magnetic_Sensor_Review_Sensors2026 - Claude Code memory

Standalone review paper. **This subproject is independent of the sibling HSX /
GaN-fusion projects (02, 03) in `01_PhD_Research/`.** Ignore that context except
the author bio below; do not pull the paper toward one lab's probe.

Owner: Yiming "Tim" Zhao, Stanford EE PhD (Senesky group). Author bio for voice
and tasteful self-citation only: works on GaN Hall-effect magnetic sensing for
fusion diagnostics; first-authored *IEEE Sensors Letters* (2023) on an AlGaN/GaN
Hall sensor in the HSX stellarator. The review itself is a broad, vendor-neutral
survey - not about his device.

## Goal
A rigorous review titled (working) "magnetic-field sensors and their
applications in energy, transportation, industrial & manufacturing, and
biomedicine," targeting **MDPI *Sensors*** (https://www.mdpi.com/journal/sensors),
submission target **before 30 Oct 2026**. Full spec in `docs/PROJECT_BRIEF.md`.

Paper skeleton the author wants (three roughly equal middle thirds):
1. Introduction
2. Sensor types (commercial + pioneering), strengths/weaknesses, and current
   applications across the four domains  [middle third #1]
3. Future applications: data-driven modeling, ML control, multi-modality /
   digital twin  [middle third #2]
4. Potential + industry standards for business, companies, investors  [middle third #3]
5. Conclusion

## How this folder runs
`run.ps1` orchestrates the whole thing as staged headless `claude -p` calls, one
per file in `prompts/`, each with its own model + effort (set from PowerShell).
Outputs land in `outputs/`; every source used is logged to `refs_raw/*.jsonl`;
logs and per-stage cost/model/effort go to `logs/run_<stamp>/`. You normally do
not run stages by hand - `run.ps1` does. Editing this file or the prompts is how
you change behavior for the next run/patch.

## Model & effort budget (mirrors the parent repo's philosophy)
Cheapest-capable per task; the most reasoning-critical, hallucination-prone parts
get **Fable 5**. Defaults in `run.ps1`:
- **Fable 5, high** - the intellectual core: sensor taxonomy & strengths/weakness
  judgments (30), future-methods synthesis (50), the paper architecture (titles
  10, outlines 20), and final integration/gap analysis (80). These prompts also
  say `think hard`/`ultrathink` so reasoning depth holds even if the effort knob
  is a no-op for a given model.
- **Opus, high** - broad-but-bounded enumeration: applications (40), standards &
  business (60).
- **Sonnet, medium** - careful mechanical work: journal-requirements brief (00),
  bibliography verification/formatting (70).
- **Haiku, low** - the run digest / patch notes (90).
Note: some Fable 5 requests may be served by Opus 4.8 via Anthropic's safeguards
routing; if a log shows that, it's expected, not an error.

## Hard rules (full version in `prompts/_shared_system.md`)
- Never invent a citation, DOI, or quote. Peer-reviewed sources preferred;
  preprints for discovery only, then cite the version of record.
- Log every source used to `refs_raw/<stage>.jsonl` (schema in the shared prompt).
- *Sensors* style: bracketed numeric citations before punctuation; MDPI/ACS
  reference format; structured abstract; paraphrase (quotes <15 words).
- Unattended: never ask the user a question; decide, note it, finish by writing
  the named file.
