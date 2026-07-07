# Research notes — HSX vector probe / RSI 2026 paper

Append new entries at the top (newest first). One dated section per
entry. Claude Code reads this file every session (see CLAUDE.md).

---

## 2026-07-06
- Project created. Target: 2–3 axis (vector) AlGaN/GaN Hall probe in a
  ceramic cube package (same LCC per face), second HSX campaign, paper
  aimed at Review of Scientific Instruments (~Mar 2027 submission).
- Full experiment + publication plan drafted in
  `docs/rsi_experiment_and_publication_plan.md`. Headline decisions:
  replicate the 02 readout board ×3 from existing gerbers, one Pico
  fans out shared a0/a1/a2/EN to all boards (synchronized spinning),
  DSOX1204G's 4 channels = v_x, v_y, v_z + sync.
- New sensor dies have larger bond pads; same plate geometry assumed —
  incoming inspection must re-measure plate R and update the 649 Ω
  emulator value + loading factor before trusting old numbers.
- Scope explicitly excludes radiation experiments: plasma + magnetic
  field measurement in HSX only. Radiation stays in the co-authored
  Van Gorp TCAD paper (cite as complementary).
- Open decisions: (1) feedthrough pin count / DB-15 vs 2×DSUB-9 — ask
  Wayne/Thomas; (2) scope memory strategy (300 ms window @ 1 MSa/s vs
  full shot @ lower f); (3) commit to 2 axes vs 3.
