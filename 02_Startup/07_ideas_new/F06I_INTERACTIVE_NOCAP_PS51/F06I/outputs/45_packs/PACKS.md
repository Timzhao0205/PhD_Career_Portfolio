# P6 source packs (2026-07-28)

Traceable source packs were built for the ten deep-dive ideas from four
verified pools: the frozen per-lane atlas ledgers, the frozen P4-session
ledgers (P4-G01..G13), the stage-10 refresh ledger (R10-001..R10-079), and one
new source opened this stage (NP45-001, the TAPESTAR XL-HF datasheet, fetched
and read in full — datasheet-grade confirmation that the incumbent HTS-tape
instrument measures critical current only). Selection and ranks were not
changed.

## Coverage

231 unique normalized accepted sources across ten packs. Every pack exceeds
the 20/7/5 floors:

| Idea | Total | Peer-reviewed | Primary-demand |
|---|---|---|---|
| P3R2-D-02 | 21 | 8 | 7 |
| P3R2-C-01 | 30 | 9 | 10 |
| P3R2-C-05 | 24 | 9 | 7 |
| P3R2-D-10 | 23 | 8 | 11 |
| P3R2-E-14 | 25 | 10 | 9 |
| P3R2-A-14 | 24 | 7 | 11 |
| P3R2-D-01 | 20 | 10 | 9 |
| P3R2-A-10 | 27 | 13 | 5 |
| P3R2-C-09 | 29 | 11 | 11 |
| P3R2-C-22 | 24 | 8 | 9 |

Booleans were mapped conservatively: `peer_reviewed` only where the atlas
records affirmative verification (`peer_review_status: verified`);
`primary_demand` only for buyer_procurement/company_filing types or primary
demand-evidence classes (official awards, tenders, buyer specifications,
earnings transcripts, direct customer documentation). India-origin statuses
carry the atlas audit results (230 verified_non_india_origin; 1
non_india_no_indicators — a corroborating-only newsletter flagged for P6
re-verification). Seven L03 academic records whose atlas claim text lived in
the locator field were given explicit claim statements; all 231 sources now
support named claims.

## Remaining gaps (carried into 50_deep)

- IEC 61788 (superconductor Ic test methods) text remains unfetched across
  all sessions (D-02, D-01 packs).
- DG Matrix primary pages resist automated fetch — its certification status
  stays snippet-flagged inside the C-01 pack narrative.
- OCP primary qualification documents intermittently blocked (403/429) —
  C-05's method-status rests on one opened secondary plus refresh checks.
- No unit-price anchors exist anywhere for: protection shelves (C-01),
  qualification benches (C-05, C-22), reel-to-reel scanners (D-02), 300C
  modules (A-14), phase-control stacks (D-10), or DC relay bays (E-14) —
  deep dives must carry bottom-up arithmetic with labeled assumptions.
- WST/ASIPP and CGN Dasheng screening remain inconclusive-negative and
  counsel-gated respectively (D-02, C-09 packs).
