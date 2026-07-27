# Stage 10A synthesis — GaN/WBG/Hall-sensor evidence batch

Stage: `10a_literature_gan`. Global attempt 4 (user-authorized retry cycle 1,
cycle_attempt 2). Companion ledger: `evidence/10A_GAN_WBG_SOURCES.csv`
(86 rows, `A0001`-`A0086`).

## 0. Attempt-history note (why this synthesis differs from any earlier draft)

This is the fourth global attempt at this stage. Attempts 1, 2, and 3 each
self-reported `COMPLETE` with a fully-verified ledger (68, 68, and 86 rows
respectively), but the launcher's own model-integrity telemetry
(`state/OPERATION_LOG.csv`, `state/MODEL_EFFORT_LOG.csv`,
`state/attempts/10a_literature_gan.json`) shows all three actually downgraded
mid-session to `claude-haiku-4-5-20251001` and were rejected `model_mismatch`;
their outputs were quarantined under `logs/run_.../10a_literature_gan/
rejected_attempt_{1,2,3}_outputs/` and were never accepted stage outputs.
`state/PROJECT_STATE.md` had briefly (and, as it turned out, incorrectly)
recorded attempt 3 as `COMPLETE`; this was corrected at the start of this
attempt — see that file's own correction note.

Per the retry instructions ("independently verify anything consulted from
rejected-attempt quarantine before accepting it"), this attempt treated the
quarantined attempt-3 CSV (the largest, most recent prior candidate pool, 86
DOIs) **strictly as an unverified lead list** — none of its verification
claims, access-level claims, or abstract-derived notes were accepted on
trust. Every row in the accepted ledger below was independently re-verified
this session from scratch (Section 1).

## 1. Search and verification method (this session)

1. **Lead extraction.** The 86 candidate DOIs, titles, authors, years, and
   venues were extracted directly from the quarantined attempt-3 CSV as a
   plain candidate list — no other field (topic tags, quality tier, claims,
   notes) from that file was copied without independent review.
2. **Bibliographic re-verification.** The 86 candidates were split into six
   batches of ~14-15 and dispatched to six parallel subagents, each launched
   with `model: sonnet` pinned explicitly (per `MODEL_POLICY.md`'s
   requirement that "main-agent and subagent work must remain on that
   requested Claude family"). Each subagent independently fetched the live
   Crossref API record at `https://api.crossref.org/works/<DOI>` for every
   DOI in its batch and compared the returned title, full author list,
   container-title (venue), year, volume/issue/pages, and Crossref `type`
   field against the candidate claim, reporting `VERIFIED_EXACT`,
   `VERIFIED_MINOR_DISCREPANCY`, or `NOT_FOUND_OR_MISMATCH` for each.
   **Result: 86/86 DOIs resolved to a real Crossref record this session; 0
   `NOT_FOUND_OR_MISMATCH`.** ~76 rows were `VERIFIED_EXACT`; ~10 carried
   trivial `VERIFIED_MINOR_DISCREPANCY` notes (author-count/"et al." framing
   corrected for `A0011`/`A0009`/`A0010`; a title-casing difference for
   `A0012`/`A0048`; an online-first-vs-print year nuance for `A0031`; a
   container-title metadata idiosyncrasy for `A0047`, where Crossref's own
   record omits the words "Sensors" and "(Hilton Head)" from the well-known
   Hilton Head Workshop's name) — none were disqualifying, and all
   discrepancies are stated explicitly in the affected rows' `notes` column
   rather than silently reconciled.
3. **Abstract-level spot-check.** 12 rows whose intended `notes`/
   `claims_supported` content depended on specific abstract-derived claims
   (not just bibliographic metadata) were independently re-fetched by the
   lead researcher directly (not delegated) this session, reading the
   Crossref `abstract` JSON field or, for one DOI with no machine-readable
   abstract (`A0083`), a corroborating institutional-repository listing via
   web search. These 12 rows are marked `access_level = abstract_metadata`;
   all other rows are honestly marked `access_level = metadata_only` (no
   abstract or full text was independently read this session for those rows,
   even where the quarantined draft had claimed otherwise).
4. **Headline finding re-confirmation.** `A0014` (Dowling, Alpert,
   Yalamarthy, Satterthwaite, Kumar, Kock, Ausserlechner, **Senesky**, *IEEE
   Sensors Letters*, 2019) and its two related Senesky-group rows (`A0045`,
   `A0047`) were re-verified via the same live-Crossref process in Section 1,
   not carried over from any earlier attempt's claim (see Section 4).
5. **Curation.** No candidate was dropped for verification failure — all 86
   independently resolved. None were cut for redundancy either, since 86 is
   within a reasonable range above the 65-source aim.

## 2. Venue and year distribution

- **86 rows, 50 unique venues, years 1979-2025** (a 46-year span).
- Decade distribution: 1970s: 1: 1980s: 3: 1990s: 6: 2000s: 12: 2010s: 33:
  2020s: 31. Over 70% of rows (64/86) are from 2010 onward, i.e. this is a
  current, active literature, not a stagnant one — directly relevant to
  rebutting a "the field has moved on / this isn't novel" framing with "the
  field is still actively publishing, including very recently."
- Top venues by count: IEEE Sensors Journal (9), Sensors [MDPI] (8), Sensors
  and Actuators A: Physical (6), Journal of Applied Physics (4),
  Solid-State Electronics (4), IEEE Transactions on Electron Devices (3),
  Nuclear Fusion (2), Review of Scientific Instruments (2), IEEE Sensors
  Letters (2 — the same venue as the manuscript under review), IEEE
  Transactions on Magnetics (2), IEEE Transactions on Instrumentation and
  Measurement (2), IEEE Access (2), Electronics (2), Applied Physics Letters
  (2), Proceedings of the IEEE (1), plus 36 further venues appearing once.
- Source type: 65 `journal_article`, 11 `review_article`, 10
  `conference_paper` (all conference rows are from IEEE-sponsored or
  equivalently peer-reviewed archival proceedings — IEEE Sensors, PRIME,
  SBMicro, CSTIC, IRPS, Hilton Head/TRF, IEEE SENSORS — per
  `SOURCE_POLICY.md`'s rule that peer-reviewed conference proceedings count).
- Quality tier: 16 tier-A (foundational/seminal — e.g. Ambacher 1999, Mishra
  2002, the three Versnel geometry papers, Popovic/Haelg 1988, Bilotti/
  Monreal/Vig 1997, Lenz/Edelstein 2006, Ripka/Janosek 2010, Schaefer et al.
  2020, Pearton reviews), 48 tier-B, 22 tier-C.
- Access level: 74 `metadata_only`, 12 `abstract_metadata`, 0 `full_text` —
  see Section 5 for what this limits.

## 3. Performance/novelty comparison dimensions suitable for a manuscript table

The ledger supports a cross-material, cross-technique comparison table along
these dimensions (source IDs are anchors, not an exhaustive list per
dimension):

| Dimension | AlGaN/GaN 2DEG anchor rows | Comparable-platform anchor rows |
|---|---|---|
| Current-related sensitivity (S_I) vs. temperature | `A0006`, `A0007`, `A0016`, `A0017`, `A0062` | `A0022` (InGaAs), `A0025` (GaAs/InGaAs/AlGaAs), `A0082` (AlSb/InAs) |
| Offset magnitude, as-fabricated | `A0006`, `A0008`, `A0014`, `A0019` | `A0026` (InSb), `A0085` (review, Si/GaAs/InSb/InAs) |
| Offset-cancellation technique (spinning current / dynamic quadrature / CDS) | `A0014`, `A0045`, `A0047`, `A0053` | `A0012` (Munter, foundational), `A0050` (Bilotti/Monreal/Vig, foundational), `A0052` (randomized spinning, 2022), `A0054` (nanotesla-range, 2017) |
| Residual-offset mechanism after cancellation | `A0043`, `A0045` | `A0028` (3-vs-5-terminal), `A0030` (thermomagnetic), `A0055` (nonlinearity) |
| Bandwidth / notch behavior of spinning-current readout | (no AlGaN/GaN-specific row found — Gap, see Section 4) | `A0052` (820 kHz notch-free, Si CMOS), `A0056` (few-hundred-kHz practical limit, general theory) |
| Noise floor / detectivity | `A0057`, `A0058` (non-GaN 2DEG/AHE comparators) | — |
| Hall-plate geometry factor / aspect ratio optimization | `A0006`, `A0043` | `A0031`, `A0032`, `A0033`-`A0035` (Versnel trilogy, foundational), `A0037`, `A0039`, `A0044` (planar Hall/cross-axis) |
| High-temperature survivability (device, not just Hall function) | `A0004`, `A0074`, `A0075` | `A0071`-`A0073` (SiC), `A0084` (4H-SiC Hall) |
| Radiation tolerance | `A0067`-`A0070`, `A0075` | `A0015` (AlGaN/GaN vs. InSb/InAs), `A0076`-`A0078` (SiC), `A0086` (ceramic-chromium, fusion-relevant) |
| Ohmic contacts / packaging / wire-bond reliability | `A0059`, `A0064`, `A0074` | `A0060`, `A0066` (wire-bond/packaging, GaN and general power devices) |
| Fusion/plasma-diagnostic deployment precedent (non-GaN) | — | `A0001`, `A0002` (radiation-hard Hall probes, DEMO-scale), `A0077` (SiC, IBIC/fusion), `A0086` (ceramic-chromium, COMPASS tokamak) |
| Cross-technology review baseline (Hall vs. fluxgate/AMR/GMR/SQUID) | — | `A0009`, `A0080`, `A0081` |

## 4. Established results versus unresolved questions

**Established from this ledger (independently verified this session):**
- The AlGaN/GaN 2DEG Hall-sensor literature is active and recent (31/86 rows
  from the 2020s alone), spanning device physics, offset-cancellation
  circuitry, and harsh-environment survivability.
- **Headline finding, re-confirmed this session via live Crossref fetch (not
  carried over from any earlier attempt's claim):** `A0014` (Dowling,
  Alpert, Yalamarthy, Satterthwaite, Kumar, Kock, Ausserlechner, **Debbie G.
  Senesky** as confirmed final/senior author), *IEEE Sensors Letters*, 2019,
  demonstrates four-phase current-spinning offset cancellation on AlGaN/GaN
  2DEG Hall plates — the identical material system, the identical offset-
  cancellation technique family, and the identical venue as the manuscript
  under review, published seven years earlier, by the mission subject's own
  PhD advisor's research group. Two further Senesky-group rows corroborate a
  sustained group research line on this exact topic: `A0045` (J.
  Microelectromechanical Systems, 2020, explaining the residual-offset
  mechanism via infrared microscopy) and `A0047` (Hilton Head Workshop,
  2018, an earlier bias-condition study by the same core author cluster).
  This is independently-verified external literature evidence — not merely
  Reviewer 2's own assertion (supplied fact `C010`, `outputs/
  00_CLAIM_BASELINE.csv`) — directly relevant to Stage 20's direction
  decision and any Stage 30 manuscript-revision strategy. **This stage does
  not decide how the manuscript or PhD direction should respond to this
  finding; that determination is explicitly deferred to Stage 20/30.**
- A 2025 paper (`A0083`, Marsic et al., *IEEE Access*) independently confirms
  the AlGaN/GaN Hall-sensor field remains active into the current year, with
  a three-terminal GaN Hall sensor aimed at on-chip condition monitoring of
  GaN power transistors — a different application (on-chip monitoring, not
  fusion in-vessel deployment) and different topology (three-terminal, not
  current-spinning offset-cancelled) from the manuscript, so it does not
  itself anticipate the manuscript's specific technique.

**Unresolved / explicitly flagged as gaps (`NOT ESTABLISHED FROM SUPPLIED
FILES OR THIS LEDGER`):**
1. No row in this ledger combines current-spinning AlGaN/GaN offset
   cancellation with in-vessel/plasma-relevant deployment in a single paper
   — the closest analogues split across `A0014`/`A0045`/`A0047` (offset
   cancellation, not fusion-deployed) versus `A0001`/`A0002`/`A0077`/`A0086`
   (fusion-deployed Hall sensing, not AlGaN/GaN current-spinning). Relevant
   to Stage 20/30's novelty-framing decision.
2. No row in this ledger independently confirms a directly comparable
   AlGaN/GaN MHz-class bandwidth figure resolving the manuscript's disputed
   ~1 MHz claim versus the ~1-2 kHz figure in project 02 (Conflict 3, per
   `state/PROJECT_STATE.md` and `outputs/00_CONFLICT_LEDGER.md`). The
   closest general (non-AlGaN/GaN) spinning-current bandwidth data points
   are `A0052` (820 kHz notch-free, silicon CMOS) and `A0056` (practical
   limit "a few hundred kHz," general theory) — useful context, not a
   resolution. Relevant to Stage 30/40.
3. This ledger does not itself establish whether the manuscript's specific
   *combination* of current-spinning + absolute calibration + in-vessel
   fusion deployment is unclaimed elsewhere in the literature; it only
   establishes that the individual component techniques (current spinning,
   AlGaN/GaN 2DEG Hall sensing, fusion-relevant Hall deployment) each
   individually pre-date the manuscript. Whether the *combination* is
   defensibly novel is a Stage 20/30 judgment call, not a Stage 10A finding.

## 5. Implications for the submitted GaN Hall sensor (inference only — not a decision)

The following are flagged explicitly as **inference**, not established fact,
and are offered only as input to Stage 20/30's decision, which this stage
does not make:
- The `A0014`/`A0045`/`A0047` cluster is the single most novelty-relevant
  finding in this ledger: it shows the manuscript's core offset-cancellation
  technique on the identical device platform, in the identical venue, from
  the same PI's own group, predating the manuscript by up to seven years.
  Any revised manuscript or direction strategy will likely need to
  explicitly distinguish the submitted work from this specific prior art
  (e.g., by application context, absolute calibration, in-vessel deployment,
  or vector/multi-axis extension) rather than treat current-spinning
  AlGaN/GaN offset cancellation itself as the novel contribution.
- The gaps in Section 4 (no single paper combining current-spinning +
  fusion deployment; no independent AlGaN/GaN MHz-bandwidth confirmation)
  suggest that *application-level* novelty (in-vessel fusion deployment,
  absolute calibration, multi-axis vector probing) is comparatively less
  contested in this ledger than *device-level* novelty (current-spinning
  AlGaN/GaN offset cancellation itself) — consistent with the mission's own
  preference (per `MISSION.md`) for "defensible novelty in application,
  calibration, measurement architecture ... rather than new cleanroom work."

## 6. Limitations caused by abstract-only / metadata-only access

- **0 of 86 rows are `full_text`.** No paywalled full-text PDF was
  independently read this session for any row.
- **12 of 86 rows are `abstract_metadata`** (`A0017`, `A0028`, `A0031`,
  `A0032`, `A0051`, `A0052`, `A0056`, `A0057`, `A0058`, `A0065`, `A0067`,
  `A0083`) — for these, a specific claim in the `notes` column was
  independently confirmed this session against the paper's own abstract
  text (fetched live via the Crossref `abstract` field, or via a
  corroborating secondary listing for the one DOI with no Crossref abstract
  field). Any *other*, more specific numeric claim about these papers not
  stated in their `notes` column has not been verified and should not be
  assumed.
- **The remaining 74 of 86 rows are `metadata_only`** — bibliographic
  identity (title/authors/venue/year/DOI) is independently confirmed, but no
  claim about the paper's internal results beyond its title and the
  `claims_supported` topical framing should be treated as verified. Any
  later stage that needs a specific quantitative result from a
  `metadata_only` row (e.g. a specific noise floor, offset value, or
  bandwidth figure) must independently re-confirm it against the primary
  source before citing it as an established fact.
- Two rows (`A0009`, `A0031`) surfaced a trivial online-first-vs-print-year
  ambiguity in Crossref's own metadata; the print/issue year was used and
  the ambiguity stated honestly in `notes` rather than silently resolved.

## 7. Row count

**86 unique, `verified_peer_reviewed` rows (`A0001`-`A0086`)** — above the
65-source aim and the 55-row floor. Structural validation
(`state/validate_10a_csv.py`) passed with 0 errors: exact 16-column header
matching `SOURCE_POLICY.md`; 0 duplicate `source_id`/`doi`/title; sequential
IDs `A0001`-`A0086`; 0 blank required fields; all `peer_review_status =
verified_peer_reviewed`; all `url` values `https://doi.org/<doi>` with
lowercase DOI matching exactly; all `quality_tier`/`access_level` values in
their controlled vocabularies; all `year` values numeric and in
[1900, 2026].
