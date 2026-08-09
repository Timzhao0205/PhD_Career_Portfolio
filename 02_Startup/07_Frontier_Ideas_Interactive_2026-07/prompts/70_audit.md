# 70_audit — independent adjudication and release

## Purpose

Adversarially audit the full rerun and create the canonical release. Treat
upstream conclusions as claims to test.

## Inputs allowed

- all accepted outputs from Stages 10-60
- frozen mission, rubric, source policy, and P0-P3 evidence

Do not use historical P4-P8 conclusions under `src/06`.

## Pilot

Audit two ideas, one deep dive, five source records, score arithmetic, one
portfolio quota, and one US/China claim. Test repair logging and canonical
copy layout. Save only under `pilot/70_audit`.

## Full outputs under `outputs/70_audit`

- `FINAL/PORTFOLIO`: complete P7 publication set.
- `FINAL/DEEP`: exactly ten final deep dives.
- `FINAL/GEOGRAPHY.md`.
- `FINAL/SELECTION.json`.
- `FINAL/SOURCES.json`: deduplicated authoritative final source subset.
- `AUDIT.json` with `verdict`, `checks`, `repairs`,
  `unresolved_critical`, `unresolved_major`, `unresolved_minor`,
  `final_24_count`, `deep_dive_count`, and `source_count`.
- `checks` contains at least ten named checks. Each is a Boolean or an object
  with Boolean `pass`.
- `AUDIT.md`: readable adversarial report.
- `CHANGELOG.md`: every repair, or explicit no-change statement.
- `RESULT.json`: `stage:"70_audit"`, `status:"COMPLETE"`, outputs and
  `audit_verdict`.

Audit 65/30/24/10 cardinality; gate and quota compliance; score arithmetic;
source-ID resolution, quality, origin eligibility, and claim support; deep-dive
word/source quotas; cross-file IDs and numbers; US/China claims; excluded
markets; 2030 timing; experiments; and competitors.

PASS is allowed only when unresolved critical and major issues are empty and
the canonical package validates. Do not edit upstream outputs; record
evidence-supported repairs only in the canonical release.

