# SOURCE_STANDARDS

Tier 1 (evidence-grade, preferred): exchange filings and announcements via cninfo
巨潮资讯 / SSE / SZSE / HKEX; annual & quarterly reports; prospectuses; inquiry
letters (问询函) and replies; official 互动易 / 上证e互动 company answers; government
procurement records (ccgp); Huawei annual reports and official releases; OFAC/Treasury
and BIS official pages.

Tier 2 (reporting-grade): Reuters, FT, Bloomberg, Caixin 财新, Economic Observer
经济观察报, 21jingji, Yicai, CNBC, SCMP, IEEE Spectrum, TrendForce/IDC/Counterpoint
research notes (label as [ESTIMATE] with firm name).

Tier 3 (context only, never sole support): sell-side research (name the broker),
industry blogs, trade press without named sourcing.

Prohibited as evidence (leads/sentiment only, always [RUMOR]): Xueqiu, Guba, Eastmoney
caifuhao promo posts, Weibo/WeChat public accounts, unattributed "channel checks",
anything whose economic incentive is stock promotion.

Every sources.json entry: {id, url, title, publisher, pub_date, access_date, tier,
claims_supported[]}. Dead links: keep entry, mark dead, find replacement. Preprints
and forums may inspire searches but never appear in dossiers as support.
