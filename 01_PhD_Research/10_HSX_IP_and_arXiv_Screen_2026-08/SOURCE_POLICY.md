# Evidence and prior-art policy

## Source order

1. Patent publications and official patent-office records.
2. Official Stanford OTL/policy, USPTO, WIPO, arXiv, journal, facility, and
   manufacturer pages.
3. Peer-reviewed articles and publisher abstracts/metadata.
4. University or national-laboratory repositories.
5. Search snippets and secondary summaries only as leads.

Use primary sources for technical and legal propositions whenever accessible.
Do not treat Google Patents legal-status labels as a legal opinion. Consolidate
patent-family duplicates and identify the earliest priority date.

## Required prior-art coverage

- Hall sensors and arrays used as fusion/plasma magnetic diagnostics before the
  likely invention date, including JET, ITER, DEMO, tokamak, and edge probes.
- AlGaN/GaN or group-III-nitride Hall devices, high-temperature/harsh-environment
  uses, device geometry, biasing, offset, and temperature measurement patents.
- UHV sensor encapsulation, ceramic carriers/holders, epoxy qualification,
  vacuum bake practice, grounded conductive/graphite shields, and GDC/plasma
  protection of in-vessel diagnostics.
- Deployment/validation methods using biased/unbiased controls, coil-only
  controls, independent diagnostics, or correlations.
- Patentability of a new use of a known device and combination claims.
- Stanford disclosure, sponsorship, and preprint procedure.

## Verification record

Every row in `outputs/20_PRIOR_ART.csv` must contain:

`source_id,kind,title,authority,year,priority_date,publication_date,identifier,url,accessed_date,coverage_area,claim_supported,verification_status,quality_tier,closest_feature,delta,notes`

Allowed verification values:

- `verified_full` — relevant claims or full technical text examined.
- `verified_abstract` — abstract plus reliable metadata examined.
- `verified_metadata` — identity/date/status only.
- `lead_only` — unverified search lead; cannot carry a material conclusion.

Quality tiers: A (primary/official), B (peer-reviewed or authoritative
repository), C (reliable secondary lead). A material conclusion requires an A
or B source, or an explicit evidence limitation.

## Coverage gate, not a count gate

There is deliberately no minimum number such as 30 verified sources. A stage
passes when all coverage areas above have been searched, the closest material
references are identified, material claims are traceable, duplicates are
consolidated, and remaining gaps are explicit. Search saturation is documented
in `outputs/20_SEARCH_LOG.md`.

## Time and legal boundaries

- Establish an evidence timeline; do not assume a filing or invention date.
- A reference published after the relevant date is not silently treated as
  novelty-destroying prior art, though it may inform terminology or risk.
- Separate U.S. grace-period discussion from foreign absolute-novelty risk.
- Separate patentability triage from freedom-to-operate and validity.
- This research package is not a substitute for Stanford OTL or patent counsel.
