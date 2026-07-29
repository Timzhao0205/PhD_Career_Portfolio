# Stage 10C — Applications, Alternatives, and Group Landscape: Synthesis

Status: complete. Ledger: `evidence\10C_APPLICATION_SOURCES.csv` (76 unique rows,
75 `verified_peer_reviewed` / 1 `peer_review_uncertain`, 0 duplicate DOIs/titles,
0 overlap with `..\06`'s 231-row baseline or this mission's 10A/10B ledgers after
one internal correction — see §0). Gate (≥40 verified peer-reviewed unique rows)
is met with margin. Source IDs P001–P076.

## 0. Method and corrections

Eight parallel research subagents each covered one evidence domain (tokamak,
stellarator, z-pinch/pulsed-power, plasma-jet/MIF, superconducting/HTS
machinery, accelerator magnets, alternative sensor technologies, and current
group/facility landscape), each independently instructed to deduplicate
against a combined baseline of `..\06`'s 231-row ledger plus this mission's own
10A (66-row) and 10B (79-row) ledgers (357 normalized DOIs total, written to
`tools\dedup_baseline_dois.txt`). Raw candidates were compiled (77 rows),
internally deduplicated (0 exact-DOI collisions across domains), and every DOI
was independently re-verified against the Crossref API in this compilation
step — not merely trusted from subagent search snippets — confirming
resolution and a ≥50%-word-overlap title match for all 77. One row (Morisaki
et al., "Flux Surface Mapping in LHD," DOI `10.13182/fst10-a10832`) was caught
as a genuine duplicate of `06`'s S0130 (the domain-B subagent had mistaken it
for a companion sequential-DOI paper, `...-a10833`, which is the actually-new
item already in `06`) and was removed, leaving **76 final rows**. No
hallucinated DOI was found in this batch; two rows flagged by their source
subagent with placeholder-looking URL fragments (JT-60SA/Takechi 2017 and
ITER/Chitarin 2007) were corrected to canonical `https://doi.org/<doi>` URLs
and their DOIs independently confirmed via Crossref rather than trusted from
the original search-engine-derived permalink guess.

One source (P063, TMR radiation-tolerance paper, *Science China Physics,
Mechanics & Astronomy* 2025) is recorded as `peer_review_uncertain` rather than
`verified_peer_reviewed` because its full author list could not be
independently confirmed in this pass — the DOI, venue, and journal-level peer
review are not in doubt, only the author-list completeness. This does not
count toward the 40-row gate.

Access-level honesty: most rows are `abstract_metadata` or `metadata_only`
because publisher full-text pages (AIP, IEEE Xplore, ScienceDirect, Wiley,
Taylor & Francis) consistently returned HTTP 403/402/418 to automated fetch in
this environment. 12 rows (all in the superconducting/HTS domain, where
IOPscience pages were reachable) are `full_text`. No row claims `full_text`
where only a search-engine abstract summary or Crossref bibliographic record
was actually inspected.

## 1. Application requirement matrix

| Lane | Field magnitude | DC/AC content | Bandwidth/pulse duration | Spatial/installation constraint | Temp/rad/EMI/survivability |
|---|---|---|---|---|---|
| **Tokamak long-pulse (ITER/WEST/JT-60SA/EAST/ASDEX-U)** | ~0.01–1 T poloidal | Dominant DC/quasi-DC + MHz-range AC (MHD/disruption) | Pulses now to ~1000 s (WEST); ITER/DEMO target quasi-steady-state (hours) | Vacuum-vessel in-vessel mounting, remote-handling-only maintenance, restricted access (P001, P002, P007) | High heat load, EM loads, neutron/gamma radiation; DEMO-class coils qualified to ≥500 °C and "intense neutron radiation" (P009); JT-60SA figures of 200 °C/9 MGy reported but **unconfirmed at full-text** (P006) |
| **Stellarator field mapping (W7-X/LHD/TJ-II/HSX-class)** | Sub-0.1 T (small devices, commissioning) to 2.75 T (LHD) | Essentially DC/quasi-static (vacuum flux mapping) | Infrequent commissioning campaigns, not continuous shot diagnostics | Tight, non-planar 3-D vacuum vessels; helical in-vessel probe-array routing (P017); ~1e-4 relative coil-accuracy design criterion (P016) | Not addressed by commissioning-era/small-device sources found here — an evidence gap, not a favorable or unfavorable finding |
| **Z-pinch/pulsed power (Sandia Z/MAGPIE/gas-puff)** | Sub-T (bias fields) to >100 T (auto-magnetizing liners) | Essentially single fast pulse; 100–240 ns rise time; dI/dt to ~200 kA/ns (P023) | ns–µs single-shot; no persistent DC baseline within a shot | Near-load B-dot arrays in extreme EMI/blast/debris environment (P021) | Brief, intense burst radiation (not cumulative fluence); severe EMI is the defining stressor, not slow drift |
| **Plasma-jet/magneto-inertial fusion (PLX/HyperV/ZaP/MagLIF)** | Sub-T (jet self-field) to tens of T (MagLIF load) | Mixed: microsecond pinch dynamics to ns liner implosion | Single-shot, low-repetition (Zap Energy's Century platform is the counter-example at 0.2 Hz, P037) | Severe: 36-gun quasi-spherical chamber access (P034); probes physically excluded from the hot dense pinch core (P032) | MagLIF documents significant DD/DT neutron yield (~1e12, P030); PLX/ZaP are low-yield/non-fusion — must not be merged |
| **Superconducting/HTS magnets, trapped-field rotors, motors/generators** | T-class to record 17.7 T (P040) | Persistent-mode DC dominant; brief high-dB/dt pulse only during (de)magnetization (P039) | Static/persistent for magnet lifetime; magnetization pulse itself is ms-scale | Cryostat/cold-bore access (4–77 K); fixed-point Hall arrays (5–18 sensors) rather than scanning benches (P043, P045) | Temperature (not radiation) is the dominant stressor; documented cryogenic Hall temperature-coefficient behavior down to 0.001%/K achievable by doping (P050, P051) |
| **Accelerator magnets (CERN/FNAL/HIAF)** | Multi-T, ppm-level precision (P054: 100 ppm field, 0.1 mrad angle) | Ramped/quasi-static, not fast-pulsed | Long, controlled measurement cycles during dedicated test campaigns | Narrow magnet bores (small-bore rotating-coil scanners, P053); mapping benches typically operate outside the beamline | Radiation present mainly as beamline background context, not a mapping-bench qualification driver — a material scope contrast with in-vessel fusion use |

## 2. Incumbent diagnostic / limitation matrix

| Lane | Incumbent | Documented limitation | Hall+coil hybrid literature found? |
|---|---|---|---|
| Tokamak long-pulse | Mirnov/pickup coils, Rogowski coils, flux/diamagnetic loops (well established in `06` baseline) | Long-pulse integrator drift (established in baseline); ITER already runs a **system-level** DC-Hall-corrects-coil-drift architecture in its outer-vessel steady-state sensor (OVSS) system (P003) | **Yes — the strongest real-machine precedent in the entire mission.** ITER's OVSS pairs bismuth Hall sensors explicitly to correct inductive-sensor drift. This is a system-level pairing of separate sensor heads with downstream fusion, not a co-located single-package hybrid as implied by the user's hypothesis — an important distinction for the identifiability analysis. No source found demonstrates the reverse direction (coil dB/dt identifying Hall gain/offset drift) as a tested capability on a tokamak. |
| Stellarator field mapping | Vacuum flux-surface mapping (electron-beam/fluorescent-screen or probe-array), compared against a Biot-Savart/filament model from known coil currents | Electron beam cannot survive in the presence of plasma — characterizes vacuum topology only, at reduced field, during infrequent commissioning windows | **No.** Despite targeted searching, no literature discusses a Hall+coil hybrid specifically for stellarator field mapping. Recorded as Unknown/unaddressed, not inferred favorably or unfavorably. |
| Z-pinch/pulsed power | B-dot probes and Rogowski coils, cross-calibrated against a current-viewing resistor (CVR) on a dedicated test stand (P022) | Calibration-transfer accuracy per geometry; near-load blast/debris/EMP survivability; well-known Rogowski bandwidth/E-field-pickup weaknesses | **Argues against.** The domain's own "sensor fusion" precedent (P025, B-dot + Rogowski, ±13–15% error) deliberately fuses two *inductive* sensors and bypasses Hall sensors entirely. Hall devices are independently documented as EMI-susceptible, especially to tangential RF E-fields (P028) — an extrapolation from power-electronics testing, not a z-pinch-specific measurement, flagged explicitly as an inference. |
| Plasma-jet/MIF | Multi-axis B-dot (Mirnov-style) coil arrays at boundary/electrode locations; spectroscopic Zeeman splitting where probes cannot physically survive inside the plasma column (P032) | Where fields/EMI/thermal stress are most extreme (MagLIF load region), practitioners abandon magnetic sensing for optical (PDV) current inference (P031) — neither gap is naturally closed by adding a Hall element | **No demonstrated result; a plausible but undemonstrated niche.** Hybrid sensing could plausibly help at boundary/wall locations in lower-field, single-shot devices if a stable pre-shot calibration reference is available, but no source proposes or tests this. |
| Superconducting/HTS magnets, motors/generators | Scanning or fixed-array Hall-probe mapping (P047, P048) for the static/persistent state; pick-up/search coils only during the transient magnetization pulse itself (P049) | **A coil is structurally blind to a persistent-mode trapped field** — no dB/dt to sense once magnetization is complete. NMR, not a coil, is the field's own choice of precision cross-check for the static state (P042). | **Poor fit for the core value proposition.** The coil channel contributes nothing during the dominant (persistent/DC) operating mode; plausible only as a transient/pulse-capture add-on during magnetization, where NMR remains the accepted absolute reference, not the coil. |
| Accelerator magnets | Rotating-coil magnetometers (harmonic-content precision) + Hall probes (local/end-field mapping) + NMR (absolute reference) — **already routinely combined** (P052, P057, P058) | Hall probes need frequent NMR recalibration; rotating coils need precise mechanical rotation reference and cannot resolve local point fields; NMR is DC/quasi-static only | **Yes — mature prior art, a real novelty concern.** Combined Hall+coil(+NMR) mapping is decades-old, routine, production-scale practice at CERN/FNAL/HIAF. Any mission novelty claim needs to rest on the radiation/in-situ/embedded-calibration angle, not on the sensor-fusion architecture itself. |

## 3. Alternative-technology map

At least 7 alternative-technology families are evidenced (gate: ≥6):

1. **Fluxgate** (P060, P061): DC-to-few-kHz bandwidth, sub-mT to few-mT range; thermal *gradients* (not just bulk temperature) corrupt offset stability (P060) — directly analogous to the Hall offset-drift problem this mission studies. No new radiation-tolerance source found in this pass (gap).
2. **AMR/GMR/TMR/planar Hall** (P062–P065): best-evidenced family. AMR tolerates gamma to 200 krad(Si) with front-end electronics as the more vulnerable link (P062); TMR shows no measurable degradation to 0–5 Mrad(Si) γ/X-ray when biased during irradiation (P063, `peer_review_uncertain`) — an order of magnitude beyond the AMR figure. TMR is genuinely DC-through-broadband in one channel (P064) — a direct competitive challenge to the Hall+coil architecture's core value proposition. Gamma/X-ray only in both radiation sources; must not be extrapolated to neutron displacement damage per `SOURCE_POLICY.md`.
3. **Fiber-optic/Faraday-effect current sensors** (P066, P067): DC-to-tens-of-GHz, EMI-immune — the strongest single differentiator against both Hall and coil. Dominant *practical* limitation is Faraday-mirror imperfection/detuning (P066), not radiation per se (radiation-induced fiber darkening is covered separately in the 10B lane). Now evidenced at three tokamaks (ITER, T-15MD here; EAST/JET already in 06/10B).
4. **NMR probes** (P058, P059, P068): DC/quasi-static-only, but the field's own gold-standard absolute reference — used explicitly in place of a coil for persistent-mode HTS magnet cross-checking (P042) and in place of a coil for accelerator-magnet calibration (P058). Cryogenic 3He NMR reaches ~1e-12 relative precision (P068) but only under cryogenic, quasi-static conditions.
5. **SQUID** (P069, P070): fT/√Hz-class sensitivity, but mandatory cryogenic cooling and narrow dynamic range. **No new peer-reviewed source found that directly documents SQUID unsuitability in fusion/radiation environments specifically** — this remains an inference from general operating-envelope evidence plus the already-baselined HTS radiation literature, not an observed claim, and is recorded honestly as a gap rather than papered over.
6. **NV-center/quantum magnetometry** (P071, P072): fT/√Hz-class in ensemble configurations; **weakest-evidenced family**. No peer-reviewed source (only an unverifiable 2026 arXiv preprint, excluded per `SOURCE_POLICY.md`) addresses radiation tolerance or high-field tokamak deployment. TRL for fusion-relevant NV magnetometry is low.
7. **Standalone Hall / inductive coil baseline** (P073 review; P052 as a standalone rotating-coil application case): `06`'s ledger already carries extensive standalone Hall/Mirnov/Rogowski coverage; this lane adds only cross-technology-anchor and diversification sources.

## 4. Current group landscape (official pages + supporting publications; discovery only, no outreach)

| Group/lab | Institution | Status |
|---|---|---|
| Intelligent Diagnostics Group, KSTAR Research Center | KFE (Korea) | Active — 2025 Kalman-filter Hall+coil sensor-fusion paper (already in 10A baseline); official KFE org chart confirms the group exists but does not itself name the paper |
| ITER Organization magnetic diagnostics / ITPA Diagnostics Topical Group | ITER Organization | Active, multi-Domestic-Agency program; OVSS Hall-sensor architecture (P003) is the mission's strongest real-machine precedent |
| Wendelstein 7-X magnetic diagnostics team | Max Planck IPP Greifswald | Active — >300 sensors on W7-X; 2024 synthetic-Mirnov validation paper credited to the "Wendelstein 7-X Team," not a single named lab |
| Z Pulsed Power / MIF program (Mykonos) | Sandia National Laboratories | Active — B-dot probes fielded on Z/Mykonos (P074); no single named PI, credited to Sandia's power-flow/MIF program broadly |
| B-field Mapping and Magnet Support (EP-DT) | CERN | Active, currently listed magnet field-mapping service; NA62 solenoid mapping (P075) used as representative methodology evidence, not page-cited |
| Bulk Superconductivity Group | University of Cambridge | Active — trapped-field HTS magnet characterization; 2023 stack-optimization paper (P076) explicitly uses an 18-probe rotating Hall array |
| Radiation-hard Hall probe (RHP) collaboration (JET) | Consorzio CREATE/RFX (Italy), Lviv Polytechnic National University (Ukraine), IPP CAS (Czechia) | Active, multi-institution — the 2022 Quercia et al. paper (already 10A/10B-seeded) is this mission's own literature seed; no single institutional homepage covers the whole collaboration |
| Fusion Plasma Division, steady-state magnetic diagnostics | IPP CAS Prague | Active — 2026 antimony-Hall-sensor paper for ITER/DEMO successor work (already dedup-baseline'd) |
| Magnetic Sensor Laboratory (LSE) | Lviv Polytechnic National University | Active per secondary sources; **official page could not be live-fetched in this session (HTTP 403)** — status not independently confirmed, flagged for re-check |

**Pattern:** radiation-hard Hall sensing for fusion is concentrated in a tight,
collaborating EU network (Czech Republic, Italy, Ukraine) plus a Korea/Germany
cluster on general magnetic diagnostics — a small, mature, well-documented
community rather than a thin one. Pulsed-power (Sandia) and accelerator/HTS
field-mapping (CERN, Cambridge) groups are active but their best supporting
publications are program overviews or different-domain metrology, not papers
specifically about Hall+coil hybrid sensing under radiation.

## 5. Promising and poor-fit cases

**Promising:**
- **Tokamak long-pulse (ITER-class and beyond):** real-machine precedent already exists (P003) for the DC-Hall-corrects-coil-drift half of the hybrid; the reverse direction (coil identifies Hall drift) is untested and could be a genuine contribution. Calibration reference (known PF-coil currents, repeatable shots, cross-machine algorithm validation, P010) is realistically accessible.
- **Fiber-optic/Faraday current sensing on tokamaks** is a credible *competing* incumbent-upgrade path, not a Hall+coil target — worth naming explicitly as the technology a Hall+coil hybrid must out-perform on EMI immunity and bandwidth, not just radiation tolerance.

**Poor fit (documented, not inferred):**
- **Z-pinch/pulsed power:** the domain's own literature shows the community already solved its redundancy need by fusing two *inductive* sensors (P025), explicitly bypassing Hall sensors; timescales (ns–µs) leave no persistent DC baseline for a Hall channel to anchor.
- **Persistent-mode superconducting/HTS magnets and motor/generator field poles:** a coil is structurally blind to a static trapped field — there is no dB/dt in the dominant operating mode. NMR, not a coil, is the field's accepted precision reference (P042).
- **Accelerator magnets:** combined Hall+coil(+NMR) mapping is mature, decades-old, production-scale prior art (P052, P057, P058) — a novelty risk, not an application opportunity, unless the mission's contribution is narrowly the radiation/in-situ-calibration angle.
- **In-plasma-core sensing (any lane):** wherever the incumbent already had to abandon magnetic probes entirely for optical (P031) or spectroscopic (P032) methods because probes cannot physically survive there, a Hall+coil hybrid adds no new survivability and is out of scope.

## 6. Unresolved gaps (labeled, not inferred away)

- No literature found on Hall+coil hybrid for stellarator field mapping (§2).
- No new radiation-tolerance source for fluxgate sensors in this pass.
- No peer-reviewed source (only an excluded 2026 preprint) on NV-center radiation tolerance or high-field tokamak deployment.
- No peer-reviewed source directly documents SQUID unsuitability in fusion/radiation environments specifically; the mission's reasoning here remains an inference from general operating-envelope evidence.
- JT-60SA's cited 200 °C/9 MGy figures (P006) and the Rogacki et al. ppm/mrad precision figures (P054) rest on search-engine-surfaced abstract paraphrase, not independently re-read full text — flagged for confirmation before being quoted as hard numbers downstream.
- Lviv Polytechnic LSE's official page could not be live-fetched (§4) — group-status claim is weaker than for single-institution labs.

## 7. Acceptance-gate status

- ≥40 verified peer-reviewed unique sources: **met** (75 verified_peer_reviewed of 76 total rows).
- All named applications addressed (tokamak, stellarator, z-pinch/pulsed power, plasma-jet/MIF, superconducting magnets/HTS/motors/generators, accelerator magnets): **met**, §1–2.
- ≥6 diagnostic alternatives evidenced: **met** — 7 families in §3.
- Group status from current official pages; scientific claims from peer-reviewed sources: **met**, with one explicit fetch-failure flagged (§4, LSE) rather than silently asserted.
- No outreach performed: **confirmed** — all group-discovery work was documentation-only per the subagent's explicit instructions and self-report.
