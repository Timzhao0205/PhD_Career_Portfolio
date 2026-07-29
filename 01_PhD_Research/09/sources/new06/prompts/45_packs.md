# 45_packs — verified source packs

## Purpose

Build traceable source packs for the ten deep-dive ideas without changing
selection or rank.

## Inputs allowed

- `outputs/10_refresh`
- `outputs/40_select`
- `src/06/90_BIBLIOGRAPHY/sources.json`
- relevant frozen P0-P3 evidence

## Pilot

Build a miniature pack for two selected ideas. Test source reuse, one new
source, claim mapping, deduplication, Boolean fields, and India-origin
eligibility. Save only under `pilot/45_packs`.

## Full outputs under `outputs/45_packs`

- `SOURCES.json`: unique normalized accepted source array. Every source has
  `id`, `title`, `url`, `publisher`, `published_at`, `accessed_at`,
  `source_type`, `peer_reviewed`, `primary_demand`, `geography`,
  `claim_supported`, `locator`, `access_level`, `accepted`,
  `india_origin_status`, and `non_indian_affiliation_evidence`.
- `PACKS.json`: `artifact` and exactly ten unique `ideas`, matching the top
  ten. Each has `idea_id`, `source_ids`, `peer_reviewed_source_ids`,
  `primary_demand_source_ids`, `claim_source_map`, `coverage_gaps`, and
  `quality_notes`.
- Every pack has at least 20 accepted sources, including at least seven
  peer-reviewed and five primary-demand sources; sets may overlap.
- `PACKS.md`: coverage and remaining gaps.
- `RESULT.json`: `stage:"45_packs"`, `status:"COMPLETE"`, outputs and checks.

Open every new source. Every packed source supports a named claim. Entirely
India-origin sources are excluded; academic eligibility needs affirmative
non-Indian affiliation evidence.

