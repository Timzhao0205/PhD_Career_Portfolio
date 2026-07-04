# SOURCE STANDARDS (binding on every agent)

## Targets

- **≥ 200 unique sources** in `90_BIBLIOGRAPHY/sources.json` at mission end (unique = unique URL
  after stripping tracking params; the same publication cited by 3 ideas counts once).
- Tier 1 + Tier 2 together must be **≥ 70%** of all sources; Tier 1 alone ≥ 25%.
- Every candidate idea: ≥ 3 sources. Every deep dive: ≥ 14. Policy brief: ≥ 25.

## Tiers

- **Tier 1 — peer-reviewed & primary technical:** IEEE Xplore journals/conferences, Nature/
  Science family, AIP/APS, IOP (incl. *Nuclear Fusion*, *Superconductor Science & Technology*),
  Elsevier/Springer journals, PNAS; standards bodies (IEC, IEEE-SA, SEMI, JEDEC); patents (as
  technical evidence, not market evidence).
- **Tier 2 — official & institutional:** government (.gov, europa.eu, .gov.cn, MIIT, NDRC,
  Federal Register, BIS, DOE, NIST, CBO, USITC, SEC filings/annual reports of public companies),
  national labs, IEA/IRENA, top policy institutes (CSIS, Carnegie, Brookings, Peterson, MERICS),
  **IEEE Spectrum** (user-designated priority), university engineering news.
- **Tier 3 — reputable industry:** established trade press (EE Times, Semiconductor Engineering,
  PV Magazine, Fusion Industry Association reports, S&P/Wood Mackenzie/Yole/TrendForce summaries,
  McKinsey/BCG), major-company technical blogs/whitepapers, Caixin, Nikkei Asia, 36kr/晚点 for
  China business facts. Fine for market color and company facts; never the sole support for a
  load-bearing market size — triangulate with a second independent source.
- **Not citable as support:** preprints (arXiv/SSRN/bioRxiv), Wikipedia, Reddit/forums, SEO
  content farms, anonymous blogs. Preprints and Wikipedia MAY be used to *discover* leads —
  then cite the published/primary version.

## Citation mechanics

- Ledger: `90_BIBLIOGRAPHY/sources.json` — array of objects:
  `{"id":"S001","url":"…","title":"…","publisher":"…","date":"YYYY-MM(-DD) or n.d.",
    "tier":1,"lang":"en|zh","accessed":"YYYY-MM-DD","used_in":["D03","C17","DD_C17"],
    "verified":"fetched|abstract-only|snippet"}`
- Cite inline as `[S###]` everywhere. Also render a human-readable
  `90_BIBLIOGRAPHY/BIBLIOGRAPHY.md` grouped by tier at Phase 6.
- **Load-bearing claims** (market sizes, prices, dates, policy provisions, performance specs)
  require `verified:"fetched"` — you actually opened the page with WebFetch and the claim is on
  it. Search-snippet-only support is allowed solely for peripheral color and must be marked
  `"snippet"`. Paywalled journals: cite from the abstract and mark `"abstract-only"`.
- Never invent DOIs, quotes, or numbers. Direct quotes ≤ 25 words. If two credible sources
  conflict, report both with the discrepancy noted — do not average silently.
- Prefer 2023–2026 sources for anything market- or policy-related; older is fine for physics.

## Chinese-language research (required, not optional)

For China market/competitor/policy questions, search in Chinese as well as English (the founder
reads Chinese natively). Good Tier 1–2 Chinese sources: gov.cn ministries (MIIT 工信部, NDRC
发改委, MOST 科技部), official plan documents (十五五 / Five-Year Plan texts), CNKI-indexed
journals, exchange filings (SSE/SZSE annual reports), CAS institutes. Record `lang:"zh"` and give
titles bilingually in BIBLIOGRAPHY.md.

## Search hygiene

- Short queries first (2–5 words), then refine. Fetch the best 1–3 results rather than skimming
  ten snippets. Log the source at the moment you use it — no end-of-phase citation archaeology.
- No prior-session knowledge: every factual claim in the deliverables must trace to a source
  gathered during THIS mission.
