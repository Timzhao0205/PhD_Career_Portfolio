# Stage 70 adversarial audit report

Audit posture: every upstream conclusion was treated as a claim to test.
The audit re-derived arithmetic from raw criterion scores, re-measured
deep dives with the validator's own regex, re-resolved every cited
source ID against its authoritative ledger, re-counted every quota, and
hash-verified every canonical copy. Historical P4-P8 conclusions under
src/06 were not used; frozen P0-P3 evidence (atlas bibliography,
P3R2 session evidence ledgers) was used only for source-ID resolution.

## Verdict

**PASS.** Zero unresolved critical issues, zero unresolved major
issues, four minor open items — every one already disclosed inside the
deliverables themselves (see below). The canonical release under
FINAL/ validates.

## What was tested and what was found

### 1. Cardinality (65 / 30 / 24 / 10)

SCORES.json holds 65 unique scored ideas covering the frozen longlist;
SURVIVORS.json holds 30 unique survivors, identical as a set to the 30
red-teamed ideas; SELECTION.json holds 24 unique final ideas and 10
deep-dive IDs, all subsets in the required directions; INDEX.json holds
exactly the 10, in the exact top-10 order. PASS.

### 2. Score arithmetic (all 65, re-derived)

For every idea, every criterion's weighted points re-derive as
score × weight / 5 against the 16/15/10/9/9/11/7/10/8/3/2 weight
table, and the 11-criterion sum reproduces the recorded total_100 —
zero discrepancies across 65 ideas × 11 criteria. (The one historical
slip, P3R2-D-18's 66.7-vs-67.5, was caught and corrected at stage-20
assembly and is recorded in P4_REPORT.md; the audit confirms the
corrected value is the one on file.) PASS.

### 3. Hard-gate compliance for the final 24

Twenty-two of twenty-four members pass all seven gates as recorded.
Two members — P3R2-A-10 and P3R2-F-01 — carry G6 (compliance)
recorded as **fail as-frozen** with disposition `advance_with_repair`:
their frozen texts named Entity-Listed CN counterparties, so a truthful
G6 could not pass as-frozen. The audit verified the repairs were
actually executed downstream: stage-30 repair requirements, stage-40
selection notes, stage-50 deep dives (D08) and stage-60 cards all
carry the restructured US-primary/gated-CN base cases, and no
deliverable presents the blocked structures as live. C-13's G6 passes
with a binding retarget condition, likewise carried through. Finding
documented; not a defect. PASS with finding.

### 4. Cross-file identity, order, and numeric consistency

Final-24 IDs and order are identical across SELECTION.json,
60_synth/PORTFOLIO.json, the 24-row matrix CSV, and the idea cards;
top-10 IDs and order identical across SELECTION, INDEX, and PORTFOLIO;
SELECTION score_total equals SCORES total_100 for all 24. PASS.

### 5. Deep-dive quotas and word counts

All ten reports re-measure inside 2,500-4,000 words with the
validator's regex; INDEX recorded counts match observed within
tolerance; source lists clear 20/7/5 with peer/demand lists strict
subsets of source lists; every INDEX ID resolves in the 45_packs pool;
each report's body citations, appendix, and INDEX lists are the same
set (verified per report during stage 50 and re-verified here). PASS.

### 6. Source eligibility and claim support (231-record pool)

All 231 pool records: accepted = true, non-empty claim_supported,
verified_non_india_origin, full-page access (zero snippet-level records
in the pool — snippet-grade findings upstream were either upgraded by
direct fetch or honestly excluded from the pool). Unique IDs
throughout. The stage-10 R10 ledger (79 records) is unique and intact.
PASS.

### 7. Citation resolution across the release

Every source ID cited in FINAL/SELECTION.json and FINAL/DEEP resolves:
231 to the normalized pool, 50 additional atlas IDs to the frozen
P0-P3 bibliography, zero orphans. FINAL/SOURCES.json holds the
deduplicated union — 281 unique records, each tagged with its
record_origin. PASS.

### 8. Portfolio quotas and constraints

experiment_by_2028, engagement_by_2029, and g7_pass hold for all 24.
Counts re-derived: 23 US beachheads, 14 CN beachheads, 13 dual-market,
14 ideas at or under the $300k adjudicated budget ceiling — matching
PORTFOLIO_CHECKS.json exactly, including its two recorded
unsatisfiable-by-construction constraints (no sub-$100k experiment
exists in the frozen pool; CN beachhead target 18 vs achievable 14).
The audit confirms those records state original targets, observed
values, and reasons — the honest form required. PASS.

### 9. Excluded markets and geography claims

No idea's markets array contains India or Singapore; GEOGRAPHY.md
covers all 24 with per-idea US/CN paths, side markets, and export
boundaries. Sampled US/China claims verified against underlying
records: C-01's CN-leg premise (missing 800 V certification standard)
against P3R2-C-01-S03; D-02's incumbent-capability claim (Ic-only, no
delamination channel) against the NP45-001 datasheet record; A-10's
blocked-counterparty facts against P3R2-A-10-S01. All supported. PASS.

### 10. Timing and experiments

Launch discipline (2030; prep 2026-2029; windows 2030-2034) holds
across cards, deep dives, and roadmap; every experiment carries budget,
pass thresholds, and a kill rule; the roadmap's tier budgets re-add to
$3.47M / $2.08M / $2.75M = $8.30M. PASS.

### 11. Canonical release integrity

All 20 copied files in FINAL/ (8 portfolio, 10 deep dives, geography,
selection) are SHA-256-identical to their accepted upstream originals
— zero silent edits, zero repairs required in the canonical copies.
FINAL/SOURCES.json is newly assembled per its stage contract. PASS.

## Minor open items (unresolved_minor; all pre-disclosed)

1. IEC 61788 standard text remains unfetched across all sessions —
   carried explicitly as an open item in D01.md §12.
2. L05-028 (IBA FY2025) and L05-035 (CGN H1-2025) headline figures
   unverified pending text-extractable re-fetch — flagged verbatim in
   the pool records and in D09.md.
3. P3R2-G-03's legacy HVDC penetration figures (~12%/78%) must be
   re-sourced or dropped — flagged in GEOGRAPHY.md and the idea card;
   not load-bearing anywhere.
4. The EU JRC electrolyzer-AST harmonization source is 2024-vintage;
   annual refresh scheduled in the C-22 plan (D10.md).

None blocks the release; each is documented at its point of use.

## Audit-process note

One audit-script defect was found and fixed during the audit itself
(the first survivors extraction read a wrong JSON key); it affected the
audit tooling only, never the audited data, and the corrected check
passes. Recorded here for completeness.
