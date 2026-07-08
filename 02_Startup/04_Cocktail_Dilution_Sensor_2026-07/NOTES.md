# NOTES — running log (newest first)

Append with `/log <note>`. One `## YYYY-MM-DD` section per day,
newest at top, tight bullets, preserve every number and unit.

---

## 2026-07-07
- Project folder created from the strategy conversation: sensing
  architecture locked as capacitive IDE + 10k NTC + IMU gating with
  mode-of-histogram burst estimator (DECISIONS.md D-001/D-002).
- Targets set: ±1.5 % v/v ABV, ≤2 s convergence during stirring,
  whisky+ice (binary) scope for v1; sugar → second modality → later.
- Phase 0 BOM drafted (~$250–400): FDC2214EVM, IDE coupon panel
  (150/200/300 µm), 10k glass-bead NTC, XIAO nRF52840 Sense, 0.01 g
  balance, hydrometer, refractometer.
- Claude Code activity hooks wired (SessionStart/PostToolUse/Stop/...
  → 98_CLAUDE_METRICS/logs/*.jsonl); analyzer tested on synthetic
  events, per-session + per-model summaries working.
