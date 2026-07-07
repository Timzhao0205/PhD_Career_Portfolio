# SOURCE STANDARDS (binding — finance flavor, adapted from 02_Startup conventions)

## Tiers

- **Tier 1 — primary filings & regulatory:** company annual/interim reports and exchange
  announcements (SEC EDGAR, HKEXnews, cninfo 巨潮资讯, SSE/SZSE), official investor-Q&A
  replies (互动易, 上证e互动), prospectuses, auditor-signed statements, central bank /
  regulator publications. The only tier that can settle a disputed fact.
- **Tier 2 — official-but-unaudited-scope:** Huawei annual reports & official newsroom
  (private co., KPMG-audited but self-published), government stats (MIIT, NBS), exchange
  data feeds, standards bodies, court/tender records.
- **Tier 3 — reputable financial media & research:** Reuters, Caixin, 财经, 21世纪经济报道,
  证券时报/科创板日报, CNBC, Nikkei, TrendForce, IEEE Spectrum (designated priority),
  named sell-side research (note: sell-side has structural long bias — use for facts and
  frameworks, discount the ratings). Fine for company facts and market color; a
  load-bearing market size needs two independent Tier ≤3 sources or one Tier ≤2.
- **Tier 4 — leads only, never citable as support:** 雪球, 股吧, Weibo/Sina finance rolls,
  Zhihu columns, Telegram/WeChat groups, YouTube/抖音 finance, anonymous "产业链梳理"
  posts. These surface tickers and rumors fast (that's their use) and are wrong or
  self-interested often enough that nothing rests on them. Map to evidence tier C in
  research files.

## Rules

1. Ledger: `sources.json` — array of objects
   `{"id":"S001","url":"…","title":"…","publisher":"…","date":"YYYY-MM(-DD)","tier":1-4,
     "lang":"en|zh","accessed":"YYYY-MM-DD","used_in":["RB_01"],
     "verified":"fetched|snippet"}`. Cite inline as [S###].
2. **Load-bearing claims** (revenue, prices, market sizes, customer relationships, policy
   provisions) require Tier ≤3 AND `verified:"fetched"`. Snippet-grade support is color only.
3. **NUMBER TRUTH RULE** (mirror of CLAUDE.md rule 2): no figure enters a file without a
   ledger id. AI output is never a source; it must cite one.
4. Chinese-language searching REQUIRED for A-share / Huawei / China-policy questions.
5. Conflicts: record both values + both ids; do not average; prefer the more primary tier;
   open an OPEN_QUESTIONS entry if unresolved.
6. Dates matter in markets: every cited figure carries its as-of date. A true-in-March
   number can be a false-in-July claim.
