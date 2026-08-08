# 10_refresh — current evidence refresh

## Purpose

Refresh decision-relevant mutable evidence for every frozen longlist idea
without scoring, ranking, adding, or deleting ideas.

## Inputs allowed

- `src/06/30_SCREENING/LONGLIST.json`
- `src/06/30_SCREENING/EVIDENCE`
- `src/06/10_SOURCE_ATLAS`
- `src/06/90_BIBLIOGRAPHY/sources.json`
- `src/06/01_MISSION`

Do not read `src/06/98_RUN_LOGS` or historical P4-P8 judgments.

## Pilot

Test three ideas from different lanes, including at least one power-electronics
or power-supply-adjacent idea when present. Exercise frozen-source reuse, one
current web verification, source normalization, origin eligibility, and JSON
writing. Save the pilot only under `pilot/10_refresh`.

## Full outputs under `outputs/10_refresh`

- `REFRESH.json`: object with `artifact`, `as_of`, and exactly 65 unique
  `items`. Every item has `idea_id`, `refresh_status` (`updated`,
  `no_material_change`, or `insufficient`), `checked_claims`,
  `new_source_ids`, `stale_claims`, and `confidence`.
- `SOURCES.json`: unique array of newly introduced or materially reverified
  sources. Each has `id`, `title`, `url`, `publisher`, `published_at`,
  `accessed_at`, `source_type`, `peer_reviewed`, `primary_demand`,
  `geography`, `claim_supported`, `access_level`, `accepted`,
  `india_origin_status`, and `non_indian_affiliation_evidence`.
- `REFRESH.md`: material changes, no-change findings, and unresolved gaps.
- `RESULT.json`: `stage:"10_refresh"`, `status:"COMPLETE"`, `outputs`, and
  `checks`.

For each idea, check at least one claim likely to change: buyer/procurement
activity, standards or regulatory timing, competitors, capacity, policy,
market access, or technical maturity. Prefer 2025-2026 evidence. Open every new
source; search snippets alone are not evidence.

