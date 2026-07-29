# Stage 10A — Hybrid/Coil Literature Synthesis

Source IDs in this document (`H001`–`H066`) refer to
`evidence\10A_HYBRID_SOURCES.csv`, which uses the shared ledger header. IDs of
the form `S0xxx` refer to `..\06\outputs\01_SOURCE_LEDGER.csv` (read-only
prior-mission evidence). Per `CLAUDE.md`, every claim below is labeled
**Observed**, **Derived**, **Inferred**, **Proposed**, or **Unknown**.

## 1. Search strategy and databases/domains

Seven parallel search passes were run, each independently verifying
candidates against Crossref DOI metadata (and, where reachable, PMC/publisher
abstract or full-text pages) rather than accepting search-engine snippets as
evidence. Databases/tools used: Crossref API, Semantic Scholar metadata
aggregation, PubMed/PMC, IOPscience, ScienceDirect, MDPI, IEEE Xplore
(metadata only — full-text access was blocked by the publisher in nearly all
cases), AIP Publishing, and general web search for discovery.

Search domains, mapped to the stage's required search list:

1. **Direct seeds + citation network** (`H001`–`H011`) — verified all six
   `LITERATURE_SEEDS.md` direct papers and chased their author/citation
   network (JET RHP group: Bolshakova, Ďuran, Quercia, Pironti, Murari;
   KSTAR/EAST integrator lineage).
2. **Observer theory** (`H012`–`H023`) — Kalman/complementary-filter
   equivalence, Luenberger/unknown-input observers, GPS/INS and
   attitude-estimation observability literature as a structurally analogous
   (absolute-sensor + rate-sensor) problem outside fusion.
3. **Coil/integrator drift** (`H024`–`H033`) — additional tokamak long-pulse
   integrators (ASDEX Upgrade, DIII-D, second-generation KSTAR), non-Rogowski
   alternatives (fiber-optic current sensors), and non-fusion (accelerator,
   geophysical) integrator-drift literature.
4. **Calibration/self-test** (`H034`–`H044`) — Hall spinning-current/chopping
   offset cancellation, embedded calibration windings, in-situ
   "artificial-plasma" coil calibration, Hall-vs-NMR traceability, redundant
   sensor fault detection.
5. **Rogowski/fault detection** (`H045`–`H054`) — bandwidth-crossover design,
   cross-axis sensitivity, CT/coil saturation detection and correction,
   timing/phase-delay fusion theory.
6. **Non-fusion hybrid applications** (`H055`–`H063`) — power electronics,
   space/geophysical magnetometry, rotating machinery, superconducting
   accelerator magnets.
7. **Hall absolute-reference** (`H064`–`H066`, cross-confirming `H001`–`H004`,
   `H006`) — NMR/fluxgate-anchored DC references paired with AC coil
   channels, including a non-fusion (heliophysics) material-diverse analog.

**Cross-check against folder 06.** All 66 unique candidate DOIs were checked
programmatically against `..\06\outputs\01_SOURCE_LEDGER.csv` (232 rows).
**15 of 66 exactly duplicate existing `06` rows** (`H001`≈S0118, `H002`≈S0122,
`H003`≈S0068, `H004`≈S0179, `H005`≈S0180, `H008`≈S0173, `H009`≈S0105,
`H010`≈S0069, `H011`≈S0111, `H034`≈S0033, `H035`≈S0041, `H042`≈S0051,
`H048`≈S0074, `H049`≈S0076, `H065`≈S0067 — each flagged individually in the
CSV `notes` column). **51 of 66 are genuinely new relative to `06`**, which
alone exceeds this lane's 40-verified-source gate. This satisfies the
mission's "extend, not relabel" instruction: the direct seeds are re-verified
here (with corrections — see §7) because the synthesis requires them, not
because they are being presented as new.

**Methodological transparency note (Observed):** one subagent's initial search
pass returned a hallucinated DOI for a paper titled "A generic method for
real time detection of magnetic sensor failure on tokamaks" — the DOI
resolved via Crossref to an unrelated ITER busbar-safety paper. This was
caught during verification and the fabricated-DOI candidate was dropped
entirely (it does not appear in the CSV). This is recorded per `AGENTS.md`'s
requirement to never invent a DOI and to record failed search leads.

**Access-level honesty (Observed).** IEEE Xplore, ScienceDirect, MDPI, AIP,
and Wiley/AGU publisher pages returned HTTP 402/403/429 on the large majority
of direct-fetch attempts across all seven search passes. Consequently 41/66
rows are `metadata_only` (Crossref-confirmed bibliographic identity, content
description from secondary synthesis, not independently read), 20/66 are
`abstract_metadata` (abstract actually read), and 5/66 are `full_text`
(open-access PMC copies: `H004`, `H005`, `H021`, `H032`, `H052`). No row
claims `full_text` without an open-access copy actually having been read.
This access limitation is itself a material constraint on this lane's
confidence — see §7.

## 2. Direct prior-art timeline

"Direct hybrid" = a source that combines a Hall (or Hall-adjacent DC/absolute)
channel and an inductive/coil (or coil-adjacent AC/rate) channel in the same
measurement or calibration architecture, tagged `direct_hybrid` in the CSV.

| Year | Source | System | What is combined | Domain |
|---|---|---|---|---|
| 1999 | `H055` | HOKA current probe | Hall (DC) + air coil (di/dt), summed | Power electronics |
| 2002 | `H038` | Hall array + on-chip coil | Hall array + embedded calibration-winding actuator | Semiconductor sensor R&D |
| 2007 | `H006` (peer-review status **uncertain**) | — | Reported Hall sensing + actuation/self-test concept | Fusion (conceptual) |
| 2008 | `H056` | AC/DC space magnetometer | Hall element inside search-coil core (flux-concentrated) | Space/geophysics |
| 2012 | `H007` | JET RHP system | Hall probe + embedded microsolenoid (dual-use: self-cal actuator and pickup coil) | Fusion (JET, operational) |
| 2013 | `H057` | AC motor instrumentation | Coil + Hall flux sensors, parallel fault signatures | Rotating machinery |
| 2013 | `H040` | HBT-EP tokamak | In-situ calibration coils energize a known "artificial plasma" to calibrate 216 Mirnov coils + a Rogowski coil | Fusion (tokamak) |
| 2018 | `H059` | HTS dipole magnet | Cryogenic Hall sensors cross-calibrated in situ against induction coils | Superconducting accelerator magnet |
| 2018 | `H008` | FAT-CM FRC experiment | Hall sensor (low-f) + coil probe (high-f) | Fusion-relevant (FRC) |
| 2022 | `H045` | Composite current sensor | TMR (Hall-adjacent) + Rogowski coil, crossover design | Power electronics |
| 2022 | `H003` | JET RHP, 11.5-yr record | **Observed:** same-die self-cal preserves Hall sensitivity. **Proposed** (not built): Hall+coil Luenberger–Kalman hybrid probe | Fusion (JET) |
| 2022 | `H004` | CERN accelerator-magnet bench | Kalman filter: coil-integrated field state, Hall (or magnet current) measurement update | Accelerator (non-fusion) |
| 2022 | `H022` | Contactless current sensor | Coil geometry + Hall device for "dynamic precision adjustment" | Power electronics |
| 2025 | `H001` | Synthetic tokamak data | Kalman filter jointly estimates B, dB/dt, coil bias, using Hall as DC anchor | Fusion (simulation) |
| 2025 | `H002` | Tokamak (validation basis unconfirmed) | Kalman filter fuses broadband coil + narrowband Hall | Fusion |

**Derived observation:** the user's "hybridize Hall+coil" concept has **direct
prior art spanning 26 years (1999–2025)**, with the closest fusion-specific
analogs (`H001`, `H002`, `H003`, `H004`) concentrated in 2022–2025 and
produced by two overlapping author clusters (CERN/Arpaia group: `H004`,
`H005`, `H028`; JET/IEAP-Prague/KAERI group: `H003`, `H006`, `H007`, `H011`,
`H040`-adjacent, `H001`, `H002`). This is the single most important finding
of this lane for the novelty question (§6).

## 3. What each source actually estimates or corrects

Per the stage's required discrimination, the table below states the specific
state/parameter each direct/calibration-relevant source targets, using the
mission's model `y_H = S_H B + b_H + n_H`, `y_C = K_C dB/dt + b_C + n_C`.

| Estimated/corrected quantity | Sources | Notes |
|---|---|---|
| Coil/integrator bias `b_C` (drift), using Hall or current-model as reference | `H001`, `H002`, `H004`, `H005`, `H024`, `H025`, `H026` | None of these estimate Hall gain `S_H`; conflating "coil-drift correction" with "Hall-sensitivity calibration" would be a scope error the stage explicitly warns against. |
| Hall sensitivity `S_H` (gain), via same-technology in-situ test field | `H003`, `H007` | JET RHP microsolenoid injects a *known* field on the *same* Hall die — validates gain stability, not a cross-technology check (Limitation 2, §7). |
| Hall sensitivity `S_H`, via external absolute reference (NMR) | `H041`, `H042`, `H064` | Bench/lab technique; NMR needs a reasonably homogeneous field, so not usable in situ during a plasma shot without a dedicated calibration coil. |
| Hall offset `b_H` only | `H034`, `H035`, `H036`, `H037` | Spinning-current/chopping and redundant-plate techniques; `H035` shows a **residual, non-zero offset floor survives** even with current spinning — offset is reduced, not eliminated. |
| Coil sensor geometric/position response + wall eddy-current model (not `S_H`, `b_H`, or `K_C`) | `H040` | Calibrates *inductive* sensors against a driven reference; does not touch a Hall channel at all. |
| Joint state + sensor bias + unknown common input (no gain term) | `H021` | The single strongest identifiability *proof* found (explicit rank condition) but explicitly does **not** include an unknown sensor-gain unknown — see §5. |
| State + rate-sensor bias jointly, assuming known absolute-sensor gain | `H013`, `H014` | Structurally close (accelerometer/gyro) but assumes the DC-type sensor's gain is already known — the Hall case cannot assume this. |
| Conditional (excitation-dependent) bias/state observability | `H018`, `H019` | GPS/INS: bias and state are confounded under straight-line/no-excitation conditions and resolve only with maneuvering — the closest real precedent for "mutual calibration is not automatic." |

**Derived conclusion:** across all 66 sources, **no verified peer-reviewed
source jointly estimates true field `B(t)`, Hall gain `S_H`, Hall bias `b_H`,
coil gain `K_C`, and coil/integrator bias `b_C` simultaneously from a Hall+coil
pair with a stated identifiability proof.** The closest approaches each solve
a strict subset of this problem (see §5).

## 4. Achieved performance and validation type

| Source | Performance claimed | Validation type |
|---|---|---|
| `H004` | Drift 59.9–120 ppm/s → 0.02–0.08 ppm/s | **Hardware**, real CERN accelerator-magnet bench (Observed, full text read) |
| `H005` | ~3 orders-of-magnitude drift reduction, 1 µT/120 s | **Hardware**, real CERN bench, NMR reference (Observed, full text read) |
| `H021` | Rank-condition proof; simulated target-tracking scenario | **Simulation only** (Observed, full text read) |
| `H001` | ~3 orders-of-magnitude drift reduction (per abstract) | **Synthetic data**, explicitly "more extreme than typical fusion diagnostics" per the paper's own abstract — **not** real tokamak discharge data (Observed from abstract) |
| `H002` | Not independently confirmed | Validation basis (real vs. synthetic) **could not be confirmed** — publisher page blocked (Unknown) |
| `H003` | Hall sensitivity SD ≈0.07% over 11 yr / >19,000 pulses | **Hardware, 11.5-year JET operational record** for the *self-cal* claim (Observed). The coil+Hall hybrid probe itself is **Proposed**, not built or tested, per the same abstract. |
| `H038` | 392 mT/A per coil (up to ~2000 mT/A with 4 coils + concentrator) | Hardware demonstration (content not independently read beyond snippet — Inferred confidence, flagged for full-text follow-up) |
| `H059` | Not independently confirmed (abstract inaccessible) | Likely hardware (HTS demonstrator magnet), **not independently confirmed** (Unknown) |

**Derived pattern:** the two most architecturally relevant fusion-specific
Kalman-fusion papers for the user's exact proposal (`H001`, `H002`) are the
*weakest*-validated in this table — one explicitly simulation-only, the other
unconfirmed. The two *strongest*-validated hardware demonstrations of
"non-integrating reference removes coil-integrator drift" (`H004`, `H005`)
are from a non-fusion (CERN accelerator) context and do not touch Hall gain
at all. **No source in this lane provides hardware-validated evidence that a
Hall channel and a coil channel, fused together in a fusion/plasma
environment, jointly resolve both coil drift and Hall gain drift.** This is
an internally consistent gap across every fusion-specific source found and
should be treated as an unresolved evidence gap (Unknown), not papered over.

## 5. Unresolved identifiability questions

Per `DECISION_FRAMEWORK.md`, the central question is whether the augmented
state `[B, S_H, b_H, K_C, b_C]` is jointly observable from `y_H, y_C`. This
lane's evidence bears on that question as follows:

1. **Additive-bias identifiability is provable (given a rank condition), gain
   identifiability is not addressed by any source found.** `H021` (Zhou et
   al. 2016) proves a necessary-and-sufficient rank condition for jointly
   estimating state + per-sensor bias + a common unknown input from
   heterogeneous sensors — but its model has **no unknown sensor-gain term**.
   Applying it to Hall+coil would require first establishing (Proposed, not
   found in any source) an analogous rank condition that also carries `S_H`
   and `K_C` as unknowns. **Unknown / open problem** per this lane's search.

2. **Even simpler two-sensor analogs show observability is conditional, not
   automatic.** `H018`/`H019` (GPS/INS) prove that bias and state remain
   confounded absent specific excitation (vehicle maneuvering); full
   observability requires persistent excitation conditions that must be
   engineered or naturally occur. **Derived implication:** a Hall+coil system
   should not be assumed mutually self-calibrating during steady, unexcited
   operation (e.g., a quiescent plasma state or DC standby) — an analogous
   excitation requirement (time-varying `B(t)`, or an injected calibration
   pulse per `H038`/`H040`) is likely necessary but has not been proven for
   this specific sensor pair in any source found.

3. **The only fusion-specific in-situ self-calibration architecture found
   (`H003`/`H007`) is same-technology, not cross-technology.** The JET RHP
   microsolenoid recalibrates the Hall sensitivity using a *known field on the
   same physical die*. This validates against systematic Hall-die gain drift
   assuming the injection-coil's own gain/geometry is stable — it does **not**
   provide an independent check against a *correlated* failure mode (e.g., a
   radiation or thermal event that shifts both the Hall element and its
   co-located microsolenoid reference together). A true "material-diverse"
   cross-check (Hall vs. an independently-supported coil channel, or vs. an
   independently-sourced current-model reference) is architecturally distinct
   from same-die self-test and is not demonstrated together with a coil
   channel in any fusion source found.

4. **No source establishes the crossover-frequency design rule for a
   Hall+coil (specifically) pair.** `H045` demonstrates a bandwidth-overlap
   design but for TMR+coil, not Hall+coil (flagged explicitly in the CSV).
   The crossover frequency at which the coil's higher-bandwidth AC signal
   should hand off to the Hall channel's DC/low-frequency signal — and how
   errors near that crossover propagate into the fused estimate — is
   **Unknown** from verified evidence for this specific sensor pair.

5. **Timing/phase misalignment between a Hall and a coil channel specifically
   has not been analyzed in any verified source.** `H053` is generic
   (non-magnetic) control theory on delay-uncertain fusion; no Hall-vs-coil
   instance was found despite a dedicated search pass (Domain E). **Unknown.**

## 6. Implications for novelty and the user's proposed sequence

**Observed:** the user's working hypothesis (Hall-first validation →
Hall+coil hybridization → reusable module/simulation package) assumes
hybridization is a comparatively fresh contribution once Hall validation is
complete. This lane's evidence complicates that assumption at the
architecture level:

- The *general* concept of "Hall (DC/absolute) channel + coil (AC/rate)
  channel, fused via a Kalman-type observer, to jointly correct coil
  integrator drift" is **not novel** — it is directly demonstrated or
  proposed in `H001`, `H002`, `H003`, `H004` (2022–2025, fusion and
  accelerator contexts) and has non-fusion precedent back to 1999 (`H055`).
- The specific fusion-facility Kalman-fusion papers (`H001`, `H002`) are recent
  (2025), from active JET/KSTAR-adjacent groups, and target exactly the
  "long-duration plasma operation" drift problem the user's HSX work would
  eventually need to address at longer pulse lengths. Any future publication
  claiming a "Hall+coil hybrid for fusion diagnostics" as its primary
  contribution **must** distinguish itself from this specific prior art by
  source ID, not merely assert novelty (per `MISSION.md`'s prior-art
  requirement).
- **Where a credible novelty gap remains (Inferred, bounded by §5's unresolved
  questions):**
  (a) no source jointly proves gain+bias+state identifiability for a
  Hall+coil pair (§5.1) — a rigorous identifiability analysis specific to
  this sensor pair, or a bench demonstration of its practical limits, is not
  preempted by any source found;
  (b) no source hardware-validates Hall+coil fusion *in a real plasma/fusion
  environment* — `H001`/`H002` are simulation/unconfirmed, `H003`'s hybrid
  probe is proposed-only, and `H004`/`H005`'s hardware validation is
  non-fusion (§4);
  (c) no source packages a reusable, general-purpose Hall+coil calibration
  simulation/module as a distributable research product — the closest
  analog is the CERN/Arpaia group's drift-free-integration methodology
  (`H004`, `H005`, `H028`), which is bench-integrator-specific, not a general
  Hall+coil module.
- **Sequencing implication (Derived):** "hybridization second" is defensible
  as an engineering sequencing choice (a working single-axis Hall channel is
  a prerequisite for building a fused system at all) but should not be
  marketed as the primary novelty claim. The identifiability gap (§5) and the
  real-environment/hardware-validation gap (§4) are better candidates for
  where the user's specific contribution could be novel, if the "reusable
  module/simulation package" phase is scoped around (a) an explicit
  gain+bias+state observability analysis and (b) real (not synthetic) HSX
  data. This is a **Proposed** framing, not a finding — it requires the
  user's/advisor's judgment on scope and is explicitly flagged as such.

## 7. Material limitations of prior hybrid work (counterevidence)

1. **Validation-strength inversion (§4).** The papers architecturally closest
   to the user's proposal (`H001`, `H002`) are simulation-only or
   validation-unconfirmed; the papers with the strongest hardware validation
   (`H004`, `H005`) are non-fusion and do not address Hall gain. No single
   source combines "fusion-relevant" and "hardware-validated" and "resolves
   both coil drift and Hall gain."
2. **Same-technology self-calibration is not a material-diverse cross-check
   (§5.3).** The only proven fusion in-situ self-cal architecture (`H003`/
   `H007`) cannot, by construction, detect a correlated failure mode that
   shifts both the Hall die and its co-located reference coil together
   (e.g., a shared radiation or thermal event) — a genuine and material gap
   given this project's radiation-reliability framing.
3. **No proof of joint gain+bias+state identifiability exists for any
   heterogeneous two-sensor architecture in the literature found, let alone
   Hall+coil specifically (§5.1).** The strongest identifiability result
   (`H021`) explicitly excludes an unknown-gain term. Extrapolating its rank
   condition to include Hall gain is an unverified, non-trivial extension.
4. **Access/verification ceiling.** 41 of 66 rows (62%) in this lane are
   `metadata_only` because IEEE Xplore, ScienceDirect, MDPI, and AIP blocked
   automated full-text/abstract retrieval across every search pass. Several
   specific technical claims used above (e.g., `H038`'s 392 mT/A figure,
   `H059`'s cross-calibration description, `H057`'s redundancy-vs-fusion
   framing) rest on secondary search-engine synthesis, not a directly
   inspected abstract or full text, and are flagged accordingly in the CSV.
   This ceiling should be revisited with institutional library access before
   any of these specific numbers are used in a manuscript.
5. **Excitation/persistence requirements are unestablished for this sensor
   pair (§5.2, §5.4).** The best available analog (GPS/INS, `H018`/`H019`)
   shows observability is conditional on maneuvering-type excitation; no
   source establishes the analogous condition (or the crossover-frequency
   design rule) for Hall+coil specifically. A calibration/observability
   argument built by directly translating `H001`–`H004`'s Kalman
   architecture to HSX would be **importing an untested assumption**, not
   applying a proven result.
6. **The 2007 "self-diagnostic" prior art is weaker than the seed list
   implied.** `H006` could not be full-text verified by any of three
   independent search passes (three different subagents, plus this
   synthesis pass, all hit the same access wall), and its venue (Sensor
   Letters / American Scientific Publishers) has documented quality
   concerns independent of DOI legitimacy. It is downgraded to
   `peer_review_uncertain` and should not by itself support a strong
   "prior art precisely anticipated the proposed self-test concept" claim;
   `H007` (IEEE TNS, 2012, unambiguously rigorous, same author group) is the
   defensible citation for that claim instead.
7. **In two mature, well-resourced adjacent fields, Hall-only and coil-only
   approaches remain parallel, unfused research lines.** Superconducting
   magnet quench detection (`H060` Hall-array-only vs. `H061` coil-only
   "quench antenna") and, to a lesser extent, accelerator field mapping
   (`H062`, Hall+NMR but coil-combination unconfirmed) show that even where
   both sensor types are individually mature and well-funded, fusing them is
   evidently not a default/easy step — a relevant counter-signal against
   assuming hybridization is straightforward engineering.
8. **A seed-list metadata error was found and required independent
   correction.** `LITERATURE_SEEDS.md`'s title for DOI `10.3390/s19245455`
   ("...by Extended Kalman Filtering") does not match the actual
   Crossref/PMC record (`H005`, "...by Feed-Forward Correction" — a
   non-Kalman method using an NMR, not Hall, reference). Folder `06`'s
   ledger (S0180) already had the correct title; this lane's independent
   verification concurs with `06` and flags the seed document as the error
   source, per `CLAUDE.md`'s "never invent or correct a measured value... if
   something disagrees, flag it."

## 8. Acceptance-gate check

- Rows in `evidence\10A_HYBRID_SOURCES.csv`: **66**, header matches the exact
  shared schema (parse-verified).
- `verified_peer_reviewed` unique rows: **65** (≥ 40 required). One row
  (`H006`) is honestly labeled `peer_review_uncertain` and does not count
  toward the gate but is retained as a flagged discovery record per
  `SOURCE_POLICY.md`.
- Duplicate DOIs/source_ids within this lane's CSV: **0** (parse-verified).
- Rows exactly duplicating folder `06`: **15**, individually flagged in CSV
  `notes`; **51 rows are new relative to `06`**.
- Direct evidence (`direct_hybrid`, 15 rows) is separated from
  `calibration_or_observer` (28), `coil_or_integrator` (29), `hall_reference`
  (21), `enabling_only` (22), and `context_only` (12) — tags overlap by
  design (a source may carry more than one).
- Claims based only on abstracts/metadata are bounded in every row's `notes`
  field and are not treated as full-text-confirmed anywhere in this document.
- Counterevidence and eight material limitations are recorded in §7 (≥ 5
  required).
