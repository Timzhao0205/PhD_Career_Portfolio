# B60 — adversarial independent review

Treat every prior conclusion as a claim to attack. Look for provenance
overreach, stale or weak sources, selection leakage, circular founder-fit logic,
semantic duplicate inflation, hidden capital/time requirements, buyer
nonexistence, certification and safety barriers, PhD scope damage, false
calibration claims, power-electronics skill gaps, geography assumptions, and
roadmap fantasy. Specifically attack B12/B15 for fabricated or duplicate DOIs,
unverified peer review, retracted/corrected work, review-on-review circularity,
study-condition mismatch, citation-count reasoning, and unsupported novelty
claims.

Recheck a risk-stratified source sample. For every issue, cite exact affected
files/rows and propose the smallest corrective action. Do not directly rewrite
earlier outputs; record issues for B70.

Required outputs:

- `ISSUES.csv`: issue_id,severity,claim,affected_file,evidence,why_it_matters,
  correction,owner,status.
- `REDTEAM.json`: counts by severity/category, sampled claims, unresolved
  issues, and release blockers.
- `REDTEAM.md`: adversarial narrative and what survived.
- `SOURCES.csv`: independent sources used.

Pilot: attack at least six claims spanning provenance, literature quality,
alignment, power, portfolio, roadmap, and sources.
