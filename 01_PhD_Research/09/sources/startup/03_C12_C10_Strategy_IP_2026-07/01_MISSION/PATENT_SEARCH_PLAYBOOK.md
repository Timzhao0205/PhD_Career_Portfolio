# PATENT SEARCH PLAYBOOK (binding on patent-scout and ip-redteam)

Free/public sources only (user budget rule). This file defines the tool ladder, the search
recipe, the record schema, and the verification protocol. The PATENT TRUTH RULE (CLAUDE.md §3)
governs everything here.

## 1. Tool ladder (in fetch-reliability order)

1. **Google Patents — PRIMARY for both US and CN.**
   - Document page: `https://patents.google.com/patent/<NUMBER>/en`
     (e.g., `/patent/US11581133B2/en`, `/patent/CN110136916A/en`). CN documents include
     machine translations; capture the original zh title too when shown.
   - Search page: `https://patents.google.com/?q=(<terms>)&country=US,CN` — supports
     `assignee=`, `before=priority:YYYYMMDD`, `after=priority:YYYYMMDD`, CPC codes in `q`
     (e.g., `q=(H01F41/06)`). If a search URL fetch returns thin/JS-only content, run the
     same query through WebSearch as `site:patents.google.com <terms>` and fetch the
     individual document pages from the hits.
   - On each document page also harvest: CPC list, priority/filing/publication dates, legal
     status line ("Active/Expired/Abandoned" — record as displayed, mark indicative),
     family ("Also published as"), Cited-By and Similar links (citation-chase fuel).
2. **Espacenet** `https://worldwide.espacenet.com/patent/search?q=<query>` — secondary;
   JS-heavy, fetches may fail. Use for family verification when Google Patents is ambiguous.
   If fetch fails twice, fall back to Google Patents and note it.
3. **WIPO PATENTSCOPE** `https://patentscope.wipo.int/search/en/result.jsf?query=<q>` —
   secondary for WO documents; session-based, may fail → fallback ladder as above.
4. **FreePatentsOnline** — server-rendered US full texts; tertiary fallback for US docs.
5. **USPTO / CNIPA official:** USPTO Patent Public Search and CNIPA's search system are
   JS/login-walled — do NOT depend on them for retrieval. DO fetch the official **fee
   schedule pages** (uspto.gov fees page; cnipa.gov.cn / official fee notices; WIPO PCT fee
   tables) in Phase 5 for the roadmap cost table.
6. **Discovery-only aids** (never cite as the record): Google Scholar patent hits, vendor
   pages bragging about patents, litigation/news mentions — always resolve to a fetched
   Google Patents record or drop.

## 2. Per-cluster search recipe (run all five passes)

1. **EN keyword pass:** 6-10 short queries from the cluster charter (2-5 words each);
   open the 10-20 most relevant documents.
2. **Assignee pass:** for every competitor named in the Phase-1 cards for this cluster's
   lane, `assignee:"<name>"` sweeps — include zh name variants (爱科赛博 AND "Xi'an
   Actionpower"), university/institute assignees (MIT, NHMFL/FSU, KIT, CAS institutes
   中国科学院合肥物质科学研究院, 中国科学院等离子体物理研究所, ASIPP), and the founder-known
   seed US11581133B2 (CAS winding-line, from the prior corpus — re-fetch before citing).
3. **CPC pass:** browse the cluster's candidate CPC entry points (TECH_CLUSTERS.md). FIRST
   fetch the class definition (Google Patents links it, or `https://www.uspto.gov/web/patents/classification/cpc/html/cpc-<class>.html`-style pages via search) — candidate codes in
   TECH_CLUSTERS are seeds, not gospel; correct them in your PL file if the definition says
   otherwise.
4. **ZH keyword pass (mandatory):** run the charter's zh seed terms on Google Patents with
   `country=CN`; also WebSearch `site:patents.google.com` with zh terms. Capture CN utility
   models (numbers containing "U") as well as invention applications (A) and grants (B/C).
5. **Citation chase:** from the 3-5 most on-point documents, walk Cited-By / Similar /
   family links one hop.

Stop condition per cluster: >= 15 verified records AND the last 5 fetched documents added no
new assignee or claim theme (note saturation in the PL file).

## 3. Record schema — `PL_<Pnn>_patents.json` fragment (orchestrator merges to patent_ledger.json)

```json
{"id":"P-XXX assigned at merge","number":"US11581133B2","kind":"B2",
 "title":"...","title_zh":"... or null","assignee":"...","priority_date":"YYYY-MM-DD",
 "pub_date":"YYYY-MM-DD","status_note":"as displayed on GP; indicative",
 "family":["CN...A","WO..."],"cpc":["H01F41/06","..."],"jurisdiction":"US|CN|WO|EP|JP|KR",
 "url":"https://patents.google.com/patent/.../en","accessed":"YYYY-MM-DD",
 "verified":"fetched","cluster":"P03","claim_theme":"<=15 words",
 "indep_claim_gist":"<=40 words for the 3-8 most blocking per cluster, else null",
 "blocking_risk":"high|med|low|none","notes":"expiry est., design-around angle, U-### links"}
```

Dedupe at merge on family: one ledger row per family, `family` array carries siblings,
jurisdiction = the fetched member. Citation style in prose: [P-###].

## 4. Reading depth & honesty

- **Landscape ≠ FTO.** For the 3-8 most blocking-looking documents per cluster, read and gist
  the independent claim(s); for the rest, title/abstract/CPC depth is enough — say which
  depth each record got (`indep_claim_gist` null = abstract-depth).
- Expiry: estimate 20y from earliest non-provisional priority for inventions (10y for CN
  utility models), then note the displayed legal status; both are indicative — fee-event
  lapses and terminal disclaimers are invisible at this depth. Never write "expired, free to
  use"; write "displays as expired — verify before reliance".
- Pending applications (A publications) matter: claims can still grow. Mark
  `blocking_risk` accordingly.
- A whitespace hypothesis must name what was searched and NOT found ("no US/CN family found
  claiming in-situ turn-to-turn Rc estimation during winding; nearest is [P-0xx] which claims
  post-wind measurement") — absence claims are bounded by the passes actually run.

## 5. Quotas

Per cluster: 15-25 verified records, >= 4 CN-family, >= 1 WO/EP/JP/KR family noted where
surfaced, 3-6 whitespace hypotheses. Ledger totals: >= 150 records, >= 50 CN-family.
