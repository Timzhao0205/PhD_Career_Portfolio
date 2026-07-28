# Stage 70_audit pilot

Run: 2026-07-28 (UTC). Status: **PASS**. Errors: none.

## Paths exercised

- **Two-idea audit** (P3R2-C-01 top-tier, P3R2-F-23 low-confidence
  repair-verdict): re-derived every criterion's weighted points
  (score × weight / 5) and the 11-criterion sum against the recorded
  totals — 80.5 and 63.4 both reproduce exactly; all seven hard gates
  read pass for both final-24 members.
- **One deep-dive audit** (D03.md): validator-regex word count 2,545
  equals INDEX.json recorded value; 24/9/7 source quotas clear the
  20/7/5 floors; every INDEX source ID resolves in the 45_packs pool.
- **Five source records** (NP45-001, L02-043, P3R2-C-05-S01, R10-036,
  L11-049 — spanning all four namespaces): accepted=true, non-empty
  claim_supported, full metadata, verified_non_india_origin, full_page
  access on all five.
- **One portfolio quota** re-derived: experiment_by_2028 holds for all
  24 (zero violations).
- **One US/China claim**: C-01's CN-leg premise (missing 800 V
  safety-certification standard) verified against the
  P3R2-C-01-S03 record's claim text.
- **Repair logging**: prototype repair record written
  (REPAIR_PROTO.json) with id/severity/location/action/evidence shape.
- **Canonical copy layout**: FINAL_PROTO/DEEP tree created; copied
  D03.md is SHA-256-identical to the stage-50 original.

## Lessons for the full audit

- Copies into FINAL must be hash-verified against upstream; any
  divergence is either a logged, evidence-supported repair in the
  canonical copy or a defect — never a silent edit of upstream.
- The weighted-points re-derivation must run across all 65 scored ideas
  (assembly-time audit caught one historical slip at D-18; the full
  audit re-proves the invariant).
- Source-eligibility sweep runs over the full 231-record pool plus every
  additional ID cited in FINAL/SELECTION.json, resolving R10 IDs to the
  stage-10 ledger and atlas IDs to the frozen P0-P3 bibliography.
- AUDIT.json needs ≥10 named checks with Boolean pass values,
  empty unresolved critical/major lists for a PASS verdict, and
  final_24_count/deep_dive_count/source_count integers.
