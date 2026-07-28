# Stage 45_packs pilot

Run: 2026-07-28 (UTC). Status: **PASS**. Errors: none.

Mini-packs were built for P3R2-D-02 and P3R2-C-01, exercising every full-stage
path.

## Paths exercised

1. **Source reuse:** atlas records, P4-session ledger records (P4-G05/G06),
   and stage-10 refresh records resolved and normalized into the 45_packs
   schema with locators.
2. **One new source opened in full:** the THEVA TAPESTAR XL-HF datasheet PDF
   (July 2017) — a datasheet-grade confirmation that the incumbent instrument
   measures critical current only (21 Hall sensors across 12 mm, 1 mm axial
   resolution at 200 m/h, 0-1 T, 50-1000 A) with no delamination or thermal
   channel. Normalized as NP45-001.
3. **Claim mapping, dedup, Booleans, origin:** every source attached to a
   named claim; canonical-identity dedup (EurekAlert release vs journal
   article; duplicate copies of the NVIDIA 800VDC page); peer_reviewed and
   primary_demand mapping rules defined; India-origin statuses carried
   through with the new source adjudicated from its own imprint.
4. **Threshold arithmetic:** programmatic pack counts with lane-atlas top-up
   where longlist citations fall short of the 7-peer-reviewed floor.

Lesson of note: DG Matrix primary pages resist automated fetch — their pack
entries stay honestly snippet-flagged. Pilot mini-packs are not reused.
