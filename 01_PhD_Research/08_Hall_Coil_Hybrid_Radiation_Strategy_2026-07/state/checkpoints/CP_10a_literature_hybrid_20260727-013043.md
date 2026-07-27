# Checkpoint — Stage 10A (`10a_literature_hybrid`)

- Stage and current gate: 10A hybrid-lane literature search. Gate: ≥40
  verified peer-reviewed unique rows in `evidence\10A_HYBRID_SOURCES.csv`.
  **Gate met: 65 verified_peer_reviewed rows (66 total, 1 peer_review_uncertain).**
- Model/effort: Sonnet 5, xhigh (per `MODEL_POLICY.md`; this is not a
  Fable-integrity stage, no model-downgrade event occurred).

## Completed outputs and row counts

- `evidence\10A_HYBRID_SOURCES.csv` — 66 rows, exact shared-ledger header
  (parse-verified via PowerShell `Import-Csv`). 65 `verified_peer_reviewed`,
  1 `peer_review_uncertain` (H006). 0 duplicate DOIs, 0 duplicate
  source_ids, 0 duplicate normalized titles. 15/66 rows exactly duplicate
  folder `06`'s ledger (individually flagged in `notes`); 51/66 are new.
  Topic-tag coverage: direct_hybrid 15, calibration_or_observer 28,
  coil_or_integrator 29, hall_reference 21, enabling_only 22, context_only 12
  (tags overlap by design).
- `evidence\10A_HYBRID_SYNTHESIS.md` — 8 sections: search strategy/domains,
  15-row direct-prior-art timeline (1999–2025), measured/estimated-state
  table, performance/validation-type table, 5 unresolved identifiability
  questions, novelty/sequencing implications, 8 material limitations
  (≥5 gate met), acceptance-gate self-check.

## Searches/analyses completed

- 7 parallel research subagents, one per required search domain (direct
  seeds+citations; observer theory; coil/integrator drift; calibration/
  self-test; Rogowski/fault-detection; non-fusion hybrid applications; Hall
  absolute-reference). Each independently verified candidates against
  Crossref/PMC/publisher pages, not just search snippets.
- Programmatic DOI dedup within this lane's 73 raw candidates (7 within-set
  duplicates removed) and against folder `06`'s full 232-row ledger (15
  cross-mission duplicates found and flagged, not hidden).
- Resolved 2 `LITERATURE_SEEDS.md` metadata errors (wrong title for DOI
  10.3390/s19245455; venue-quality downgrade for the 2007 Sensor Letters
  DOI) and caught/discarded 1 hallucinated DOI from an initial search pass.

## Exact unresolved questions (carried forward, not blocking this gate)

1. No verified source proves joint identifiability of field + Hall gain +
   Hall bias + coil gain + coil bias from a Hall+coil pair (closest proof,
   H021, excludes the gain term).
2. No source establishes an excitation/persistence condition or a
   crossover-frequency design rule specific to a Hall+coil pair (GPS/INS
   analogs, H018/H019, are the closest transferable precedent).
3. No source hardware-validates Hall+coil fusion in a real (not synthetic)
   fusion/plasma environment.
4. Timing/phase misalignment between a Hall channel and a coil channel
   specifically has not been analyzed in any verified source found.
5. 41/66 rows remain `metadata_only` due to publisher access blocks (IEEE
   Xplore, ScienceDirect, MDPI, AIP); several specific performance numbers
   (e.g., H038, H059) should be re-verified with institutional access before
   manuscript use.

## Files safe to reuse

- `evidence\10A_HYBRID_SOURCES.csv` and `evidence\10A_HYBRID_SYNTHESIS.md`
  are complete, gate-passing, and should be treated as durable inputs to
  stage 10D (evidence merge) — do not re-run this lane's searches from
  scratch; extend/append only if new evidence is found in a later stage.

## Next action

Run/resume the parent launcher into `10b_literature_radiation` (radiation
lane, ≥45 verified peer-reviewed rows gate).

## Model/effort and notes

- Requested/reported: Sonnet 5, xhigh. No Fable-downgrade event (not
  applicable to this stage). No security-fallback flag. Auxiliary subagent
  work (7 general-purpose research subagents) logged per `AGENTS.md`
  §"Auxiliary/subagent use of another model is logged and allowed" — all 7
  subagents inherited the session's Sonnet model, no auxiliary-model
  deviation occurred.
