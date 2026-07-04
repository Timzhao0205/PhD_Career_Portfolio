# SOURCE STANDARDS V2 (binding on every agent)

Identical to Round 1, plus prior-source reuse rules.

## Targets
- Merged bibliography >= 200 unique sources (unique URL after stripping tracking params), of
  which >= 100 gathered FRESH in this mission. Tier 1+2 >= 70% of total; Tier 1 >= 25%.
- Every candidate >= 3 sources; every deep dive >= 14 (fresh-majority); policy delta 10-18.

## Tiers (unchanged)
- Tier 1 - peer-reviewed & primary technical: IEEE Xplore, Nature/Science family, AIP/APS/IOP,
  Elsevier/Springer, PNAS; standards bodies (IEC, IEEE-SA, SEMI, JEDEC); patents as technical
  evidence.
- Tier 2 - official & institutional: .gov / europa.eu / .gov.cn (MIIT, NDRC, MOST), Federal
  Register, BIS, DOE, NIST, national labs, IEA/IRENA, CSIS/Carnegie/Brookings/Peterson/MERICS,
  IEEE Spectrum (user priority), SEC/exchange filings, university engineering news.
- Tier 3 - reputable industry: EE Times, Semiconductor Engineering, Fusion Industry Association,
  S&P/Wood Mackenzie/Yole/TrendForce, McKinsey/BCG, Caixin, Nikkei Asia, 36kr/wandian for China
  business facts. Never sole support for a load-bearing market size - triangulate.
- Not citable as support: preprints (arXiv/SSRN), Wikipedia, forums, SEO farms, anonymous blogs
  (discovery only - then cite the published/primary version).

## Prior-source reuse (new)
- The prior ledgers (00_PRIOR_CORPUS/GEN1_GEN2/source_evidence_ledger*.csv and
  GEN3/sources.json and GEN3 DD_*_sources.json) MAY be reused. Reused entries keep a pointer to
  their original ID, get a fresh entry in 90_BIBLIOGRAPHY/sources.json with
  "reused_from":"<orig id/file>", and count toward the 200 but NOT toward the 100-fresh floor.
- Any reused source supporting a LOAD-BEARING claim (market size, price, spec, date, policy
  provision) must be RE-FETCHED this mission and re-marked verified:"fetched" with today's
  accessed date. Unrefetched reused sources may support color only.

## Citation mechanics (unchanged)
- Ledger: 90_BIBLIOGRAPHY/sources.json - {"id":"V-S001","url","title","publisher","date",
  "tier","lang","accessed","used_in":[],"verified":"fetched|abstract-only|snippet",
  "reused_from":null}. Cite inline [V-S###] (or original IDs for reused). Human-readable
  BIBLIOGRAPHY.md regenerated at Phase 6, tier-grouped, zh titles bilingual.
- Load-bearing claims require verified:"fetched". Quotes <= 25 words. Never invent DOIs,
  quotes, or numbers; conflicting credible sources -> report both.
- Chinese-language searching REQUIRED for China market/competitor/policy questions (gov.cn
  ministries, plan texts, CNKI, SSE/SZSE filings); record lang:"zh".
- Prefer 2024-2026 for market/policy; physics may be older. Short queries first; fetch the best
  1-3 pages; log sources at time of use.
