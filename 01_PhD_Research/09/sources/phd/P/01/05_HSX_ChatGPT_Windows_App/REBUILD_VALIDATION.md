# ChatGPT Windows app rebuild validation

Validation date: 2026-07-12

- Clean app-native package constructed independently from the PowerShell automation layer.
- 96 files audited before this validation record was added.
- All seven ordered stage prompts, markers, and acceptance conditions are present.
- Required inputs, annotated LCC image, CAD/reference data, and previous processed results exist.
- Package contains no `.ps1`, `.bat`, `.cmd`, `.claude`, `CLAUDE.md`, project `config.toml`, or old
  runner/kickoff file.
- One-paste `/goal` kickoff and separate restart/resume prompt are present.
- State, work, decision, model/effort, checkpoint-index, and self-contained checkpoint records are
  initialized.
- The checkpoint protocol covers stage boundaries, costly research/CAD, context pressure, restart,
  atomic snapshots, file-only fallback, and optional local Git commits without remotes.
- Prompt coverage checks passed for continuous 250 deg C UHV, 31.75 mm x 27.5 mm envelope, three
  boards/twelve conductors, pad 14/18 conflict, reuse/cost/connection priorities, and zero tapped
  zirconia threads.
- Sol/xhigh critical-work and no-silent-downgrade policies are explicit.

The live app must still verify its actual folder permissions, web access, model selection, and
available local CAD tools. Those checks are part of the baseline and first runtime checkpoint.

