# SOURCE STANDARDS V3 (binding on every agent)

Inherits Round-2 V2 verbatim except as amended below. Two ledgers this round:
non-patent sources in `90_BIBLIOGRAPHY/sources.json`, patents in
`30_PATENTS/patent_ledger.json` (schema in PATENT_SEARCH_PLAYBOOK.md §3).

## Targets
- Patent ledger: >= 150 fetch-verified records, >= 50 CN-family, family-deduped.
- Non-patent bibliography: >= 120 fresh unique sources; Tier 1+2 >= 65% of total; every
  competitor segment >= 12 fresh; every strategy/roadmap load-bearing number fetched THIS
  mission (incl. all fee figures).
- Prior-corpus reuse allowed with `"reused_from"` pointers (Round-2 rule); reused sources
  supporting load-bearing claims must be re-fetched this mission.

## Tiers (unchanged from V2, one addition)
- Tier 1 — peer-reviewed & primary technical, standards bodies, **and patents as technical
  evidence** (patents cite as [P-###] from the patent ledger, not the bibliography).
- Tier 2 — official & institutional: .gov/.gov.cn/europa.eu, USPTO/CNIPA/WIPO/EPO official
  pages (fee schedules, rule notices), Federal Register, BIS, DOE, national labs, SEC/SSE/SZSE
  filings, tender platforms (中国政府采购网, 招标 announcements), FIA, university news.
- Tier 3 — reputable industry/trade press; never sole support for a load-bearing number.
- Not citable as support: preprints, Wikipedia, forums, SEO farms, anonymous blogs
  (discovery only). Vendor marketing pages ARE citable for that vendor's own specs/prices
  (primary for self-claims), Tier 3 for anything else.

## Citation mechanics
- Non-patent: [S-###] (or segment/cluster-local ids like [CS-A-07], merged at Phase 5).
  Schema identical to Round 2: {"id","url","title","publisher","date","tier","lang",
  "accessed","used_in":[],"verified":"fetched|abstract-only|snippet","reused_from":null}.
- Patents: [P-###]; PATENT TRUTH RULE applies — no unfetched numbers, ever.
- Load-bearing claims require verified:"fetched". Quotes <= 25 words. Conflicting credible
  sources → report both. zh sources record lang:"zh" with bilingual titles in BIBLIOGRAPHY.md.
- Chinese-language searching REQUIRED for: CS-B, CS-G segments; CN pass of every patent
  cluster; CN fee/procedure facts; tender/price evidence.
- Prefer 2024-2026 for market/competitor/price facts; patents and physics may be any age
  (age is data — expiry matters).
