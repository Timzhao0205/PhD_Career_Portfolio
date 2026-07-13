# Pre-P3 India source-origin audit directive — 2026-07-12

## Binding interpretation

Material produced by an India-located lab, university, government, company, media outlet,
publisher, consultancy, or organization cannot support the research. It may remain only as a
discovery lead, and an independent eligible source must confirm any useful claim.

Exception: a peer-reviewed academic paper with Indian-affiliated co-authors may be accepted if at
least one co-author has a verified non-Indian institutional affiliation. Papers whose resolved
affiliations are entirely Indian are discovery-only. Never infer affiliation from names.

## Work already performed in this patch

- Screened the 1,125-record checkpoint and identified 39 high-priority origin/affiliation records.
- Quarantined 27 clearly India-origin or India-only records in both canonical and lane ledgers.
- Re-merged/deduplicated the canonical ledger: 1,118 reviewed, 833 provisionally accepted.
- Post-prefilter counts remain above numeric requirements: 474 peer-reviewed, 190 primary demand,
  135 government/standards, 133 market/industry, 301 US, 166 China, 117 JP/TW/KR, 99 Asian local
  language, T1 71.9%, and every lane >=42.
- Existing P3 A-D seeds remain non-authoritative; longlist count is still zero.

## Mandatory automated continuation

The prefilter is not the full audit. Claude Code must audit all remaining accepted records, write
`india_origin_audit`, independently replace any excluded-source claims, repair the atlas, and run
replacement searches if any source gate falls below its threshold. P3 remains blocked until
machine validation and `99_AUDIT/P2A_FABLE_ORIGIN_ADJUDICATION.md` both say PASS.

After P2A, run P3 round 2 exactly as patched: five Fable 5/xhigh generation batches (>=80 new
seeds) followed by the independent Fable 5/xhigh elegance adjudication.
