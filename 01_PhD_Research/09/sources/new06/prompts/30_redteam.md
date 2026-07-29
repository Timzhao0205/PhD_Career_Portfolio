# 30_redteam — adversarial review

## Purpose

Try to falsify every one of the 30 P4 survivor theses before portfolio
selection.

## Inputs allowed

- `outputs/10_refresh`
- `outputs/20_p4`
- frozen P0-P3 evidence needed to verify claims

Do not read historical P5-P8 judgments under `src/06`.

## Pilot

Attack three survivors with different risk profiles. Exercise current
competitor verification, technical and commercial kill tests, and
fact/inference separation. Save only under `pilot/30_redteam`.

## Full outputs under `outputs/30_redteam`

- `REDTEAM.json`: `artifact`, `method`, and exactly 30 unique `ideas`.
  Each has `idea_id`, `decision` (`survive`, `repair`, or `reject`),
  `failure_modes`, `strongest_counterargument`, `demand_separability`,
  `competition_test`, `technical_kill_test`, `commercial_kill_test`,
  `geography_findings`, `source_defects`, `repair_requirements`,
  `residual_risk`, `confidence`, and `source_ids`.
- `REDTEAM.md`: cross-candidate patterns, strongest survivors, rejected
  theses, and repairs.
- `RESULT.json`: `stage:"30_redteam"`, `status:"COMPLETE"`, `outputs`, and
  checks.

Attack buyer willingness to outsource, closest substitutes, measurable 10x
edge, experiment realism, capital path, timing, US/China beachheads,
regulation/export control, safety, and source quality. Do not choose the final
24 in this stage.

