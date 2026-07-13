# Source standards and acceptance schema

The mission must review more than it accepts. Target 720–800 collected records; accept at least
600 unique canonical works after peer-review, quality, duplication, and relevance checks.

## Minimum accepted mix

- 360 peer-reviewed academic/technical works.
- 120 primary demand sources: tenders, procurement notices, buyer specifications, company filings,
  earnings transcripts, official project awards, or direct customer documentation.
- 60 government, national-lab, standards-body, or regulator sources.
- 60 credible market/industry sources; vendor marketing alone cannot establish demand or TAM.
- 80 sources concerning China, Japan, Taiwan, or South Korea, including at least 40 local-language
  primary sources. Within the total atlas, require at least 150 US records, 100 China records,
  and 40 combined Japan/Taiwan/South Korea records so primary-market depth is not diluted.

Categories may overlap, but one canonical work counts once toward 600. The ledger must report
overlap transparently.

## Temporal reuse and 2030 refresh rule

The existing source corpus remains valid as a 2026 baseline. Do not discard older peer-reviewed
technical work merely because the company launches in 2030; foundational physics, validated
mechanisms, standards history, and durable performance data remain usable when still applicable.

Time-sensitive claims must be refreshed during P4/P6: buyer budgets, tenders, project schedules,
prices, incumbent offerings, market capacity, regulations, incentives, export controls, and
supply chains. A final idea needs at least two independent 2030-timing sources, including one
primary/official source that specifies a 2028–2035 procurement, capacity, regulation, roadmap, or
customer investment trigger. Label forecasts as scenarios, not facts, and triangulate them against
present commitments. If a 2026 source's underlying commitment remains active through 2030, record
that explicit date and it may serve as forward evidence without replacement.

## India source-origin exclusion and multinational exception

Every accepted source must contain `india_origin_audit`. Entirely India-origin material—including
Indian labs, universities, governments, companies, media, publishers, consultancies, market
reports, and organizations—is discovery-only. It may suggest a keyword, buyer, or final paper,
but an independent eligible source must confirm the claim before it enters the evidence atlas.

A peer-reviewed academic paper with one or more Indian-affiliated co-authors is allowed only when
at least one co-author has a verified non-Indian institutional affiliation. Record all resolved
institutions and countries and set status `verified_multinational_allowed`. A paper whose resolved
authors are all India-affiliated is rejected. For accepted sources without Indian affiliations,
use status `verified_non_india_origin`. Missing or ambiguous affiliation/origin metadata cannot
pass until publisher pages/PDFs, official organization pages, Crossref, OpenAlex, ROR, or ORCID
evidence resolves it. Do not infer affiliation from a name or nationality.

## Academic peer-review rule

arXiv, SSRN, ResearchGate uploads, theses, posters, slide decks, and unreviewed manuscripts are
discovery-only and cannot enter the accepted ledger as academic support. A journal article or
conference paper is accepted only if the agent records:

1. DOI or stable publisher record;
2. final venue, volume/year or proceedings identity;
3. `peer_review_status: verified`;
4. a publisher, society, indexing, or venue-policy URL supporting final publication/peer review;
5. article page fetched successfully.

IEEE conference papers are not accepted merely because “IEEE” appears in a result. Verify the
final IEEE Xplore record and proceedings. Editorials, standards, magazines, and Spectrum articles
may be useful but must be typed correctly and do not count toward peer-reviewed quota.

## Quality tiers

- T1: peer-reviewed primary technical paper; official law/regulation/standard; government or
  national-lab primary record; buyer tender/procurement/specification; audited company filing.
- T2: respected review article; recognized trade association; credible technical vendor datasheet;
  named-expert interview; high-quality trade press with primary links.
- T3: general news, consultancy estimates, vendor blogs. Context only; <=15% of accepted ledger.
- Discovery-only: preprint, search snippet, aggregator, unsourced repost, Wikipedia.

At least 70% accepted sources must be T1 and at least 90% T1+T2. Each final idea needs at least 12
unique sources: >=5 peer-reviewed technical, >=3 demand/primary commercial, >=1 competitor
primary, and >=1 geography/policy source.

## Canonical ledger fields

Each object in `90_BIBLIOGRAPHY/sources.json` must contain:

`id, title, authors_or_org, year, url, canonical_key, source_type, tier, lane_ids, idea_ids,
accessed_at, fetched, language, geography, peer_review_status, peer_review_evidence_url, doi,
demand_evidence_type, claim_supported, locator, accepted, rejection_reason, notes,
india_origin_audit`.

`lane_ids`, `idea_ids`, and `geography` are arrays. Geography uses ISO-like codes (`US`, `CN`,
`JP`, `TW`, etc.). Technical publications retain objective origin metadata even when their origin
is outside the target markets. `CN`, `JP`, `TW`, and `KR` count toward the Asia-market quota, but
P3 and later must distinguish China from the three optional side markets.
`source_type` uses one of: `academic_peer_reviewed`,
`buyer_procurement`, `company_filing`, `government`, `national_lab`, `standard`, `regulator`,
`market_industry`, `vendor_datasheet`, `trade_press`, `patent`, or `discovery_only`.

Canonical key priority: normalized DOI, then patent/tender/standard ID, then normalized publisher
URL, then normalized title+year. Deduplicate mirrors and preprint/final pairs in favor of the
peer-reviewed final work. Do not invent DOI, authors, venue, quotes, page numbers, or access state.

## Claim discipline

- Search snippets locate sources; they never support final claims.
- Load-bearing claims require `fetched: true`, a locator, and a concise support note.
- Market size requires bottom-up arithmetic plus at least one independent triangulation.
- Vendor claims are labeled vendor claims and never treated as independent validation.
- Conflicts are shown, not averaged away. Inaccessible sources can be logged as rejected but do
  not count toward 600.
