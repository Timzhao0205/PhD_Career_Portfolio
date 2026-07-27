# Source policy

## Final ledger schema

Every evidence-lane and final ledger CSV uses this exact header:

```text
source_id,citation,title,authors,year,venue,doi,url,source_type,peer_review_status,quality_tier,topic_tags,claims_supported,verification_basis,access_level,notes
```

Allowed peer-review status values:

- `verified_peer_reviewed`
- `not_peer_reviewed`
- `peer_review_uncertain`

Only `verified_peer_reviewed` counts toward numeric gates.

Allowed quality tiers for verified papers:

- `A`: high-quality original evidence, authoritative review, or strong
  high-impact/field-leading work directly relevant to a decision.
- `B`: sound peer-reviewed work with useful direct or enabling relevance.
- `C`: peer-reviewed contextual or narrow evidence that is helpful but less
  decisive.

Allowed access values:

- `full_text`
- `abstract_metadata`
- `metadata_only`

Verification must state exactly what was inspected. Do not write
`full_text` after reading only a snippet or abstract.

## Gates

- Hybrid lane: at least 40 verified peer-reviewed unique rows.
- Radiation lane: at least 45.
- Applications/alternatives lane: at least 40.
- Final ledger: at least 120 after cross-lane deduplication.
- Final new-source delta: at least 75 relative to normalized DOI/title entries
  in folder `06\outputs\01_SOURCE_LEDGER.csv`.
- Final topic quotas:
  - hybrid/coil/integrator/sensor fusion: 25
  - radiation/irradiation: 30
  - applications/alternatives: 25
  - calibration/observability/uncertainty: 20

A source can satisfy multiple topic quotas. It counts only once toward 120.

## Preferred evidence order

1. Original peer-reviewed journal or conference paper.
2. Official publisher metadata/full text.
3. DOI/Crossref or institutional repository metadata.
4. Standards and official facility documents for requirements/context.
5. Review articles for mapping and terminology.
6. Preprints, theses, patents, vendor pages, general webpages, and talks for
   discovery only.

Current group status and facilities should use official institutional pages.
Those pages do not become peer-reviewed evidence.

## Radiation discipline

Record, when available:

- particle/species and spectrum;
- fluence or dose and units;
- dose/fluence rate;
- temperature during and after exposure;
- bias state;
- annealing/time-after-exposure;
- material, heterostructure, geometry, packaging, and readout;
- affected quantity: sensitivity, offset, resistance, mobility, noise,
  linearity, cross-axis response, or failure.

Never silently combine neutron, gamma, proton, electron, or heavy-ion results.
Label mechanism-based extrapolation as inference.

## Deduplication and conflicts

Normalize DOI by lowercasing and removing DOI URL prefixes. Normalize titles
by lowercasing and removing punctuation. DOI or normalized-title duplicates
must be merged.

Conflicting results remain in the ledger. Explain whether the conflict may be
caused by device material, dose/spectrum, bias, temperature, annealing,
packaging, metrology, or sample variation.

No source is excluded solely because of author nationality or affiliation.
