# P5 independent red team — US scientific supplement

Scope: exactly `P5-USSCI-S01` and `P5-USSCI-S02` from
`30_SCREENING/P5_US_SCIENTIFIC_SUPPLEMENT_PROPOSAL.json`. This is an adversarial
P5 recommendation, not a ledger, P4, selection, routing, or state edit. The literal G1 test does
not require a future startup purchase order, but it does require two independent sources for the
exact necessary product job, including a primary buyer/procurement/filing record. A funded host
facility is not by itself demand for a separable merchant daughtercard.

## Executive disposition

| Idea | Proposal score | Revised score | Kill probability | Current blockers | Disposition | US countable now? |
|---|---:|---:|---:|---|---|---|
| `P5-USSCI-S01` | 77.5 | **55.1** | **85%** | G4, G7; G3 experiment-access condition | **KILL** | **No** |
| `P5-USSCI-S02` | 75.0 | **55.8** | **70%** | G1, G7; G3 access condition | **HOLD** | **No; conditional on repair** |

Both classifications are substantively correct: each is a `scientific_big_physics` product sold
to accelerator/detector laboratories, each directly stabilizes or preserves scientific process
output rather than merely testing it, and the proposed lane/role mappings are reasonable
(`S01`: L13, `process_output`; `S02`: L05, `process_output`). Neither has a China beachhead. The
archetype and US geography are therefore countable only if the commercial gates pass; a killed or
held idea cannot be used to satisfy portfolio arithmetic.

## `P5-USSCI-S01` — radiation-aware 5 ps timing-integrity endpoint

### Strongest bear case

**Factual evidence.** The exact detector-edge job is real. The ePIC requirements call for 20 ps
phase stability persisting across power cycles, possibly below 5 ps jitter for time-of-flight,
fine-delay monitoring, drift/phase/frequency information, a 64-bit bunch identity, and automated
power-cycle recovery
([ePIC timing requirements, pp. 3 and 17](https://indico.bnl.gov/event/20010/contributions/82901/attachments/51356/87818/ePIC_Timing_SRO_XI.pdf)).
But the same buyer collaboration is already building the proposed category. Its ppRDO program had
produced six working boards by June 2024; the boards use TClink-compatible FPGAs, SFP+, clock-cleaner
PLLs, a direct-clock alternative, loopback, voltage/temperature telemetry, radiation testing, and
SEU handling. It was already measuring 2–5 ps recovered-clock jitter
([ppRDO review, pp. 2–6](https://indico.bnl.gov/event/23529/contributions/91986/attachments/54930/94039/ppRDO%20Electronics%20Review%20Final%2010Jun2024.pdf)).
The official 2025 schedule places RDO schematics in 2025, PCB layout in early 2026, engineering-test
article procurement/award in 2026–27, then production and DAQ/timing integration—not an unfrozen
endpoint architecture waiting for a 2030 entrant
([ePIC detailed schedule, pp. 73–74](https://indico.bnl.gov/event/26584/attachments/62174/106780/ePIC_28May2025_Full%20Detail.pdf)).

The proposal also omits a closer global incumbent than Safran or Libera. A final 2026 journal
article reports SHINE's commissioned network of about 750 embedded FMC slave nodes. Those nodes
use Artix FPGAs, dual SFPs, fine delay, bunch ID, temperature/lock/round-trip-latency/fixed-delay
monitoring through SNMP/EPICS, achieve below 10 ps jitter, and specify reboot phase change below
120 ps
([SHINE design and commissioning](https://link.springer.com/article/10.1007/s41365-025-01809-x)).
Safran's WR-Z16 independently adds multi-source monitoring and seamless failover, although at a
less demanding sub-nanosecond timing layer
([WR-Z16 product page](https://safran-navigation-timing.com/product/white-rabbit-z16)).

**Inference/judgment.** The proposed card is therefore not a new unbundled category. It is a
harder specification and integration of functions already present in ePIC's ppRDO plan and in
SHINE's embedded FMC nodes. Against the exact SHINE reference, 20 ps reboot repeatability is 6x,
not 10x; 5 ps jitter is about 2x, not 10x. Radiation qualification and silent-slip localization
are useful, non-cosmetic engineering, but no primary buyer source says it will replace its own
board with a merchant endpoint for those increments. By 2030 the highest-value design-in decisions
are likely to be frozen; commissioning spares do not reopen a custom architecture automatically.

### Hard gates

| Gate | Verdict | Independent rationale |
|---|---|---|
| G1 | **PASS_MARGINAL** | Multiple primary ePIC documents specify the exact timing job. They are documentarily distinct, but all are correlated to one EIC/ePIC program; this proves category need, not replicated merchant demand. |
| G2 | **PASS** | The five claimed peer works are final journal records with stable DOI/publisher evidence. Standards and CERN records are correctly not counted as peer review. |
| G3 | **PASS_CONDITIONAL** | The 12-month metrics and silent-slip/buyer-interface kills are falsifiable. The $98k arithmetic sums exactly, but no radiation-facility access letter or quote supports the $14k line; it cannot count as a decisive <$100k experiment today. |
| G4 | **FAIL** | The proposal names broad timing incumbents but omits the closest exact implementations: ePIC ppRDO and SHINE's commissioned embedded FMC endpoint. The claimed 10x edge disappears against them, and the residual merchant difference lacks buyer validation. |
| G5 | **PASS** | All constituent physics and electronics are demonstrated; product economics and architecture access are the killers. |
| G6 | **PASS** | A US civilian DOE route is credible; configuration control, EMC, radiation assurance, provenance, and later export screening are acknowledged. |
| G7 | **FAIL** | The official schedule is a valid 2028–35 trigger for the facility, but it also shows the endpoint design/procurement locking in before the 2030 company launch. No 2030–34 primary record identifies a third-party replacement, second-source qualification, or spares socket for this card. |

### Revised scoring and arithmetic

| Criterion | Raw | Weighted | Reason |
|---|---:|---:|---|
| Demonstrated demand | 4 | 12.8 | Exceptional exact buyer requirements, albeit one program. |
| Frontier/coolness | 3 | 9.0 | Auditable timing is compelling, but commissioned precedents exist. |
| High-end niche | 3 | 6.0 | Valuable endpoint count, very few reachable buyers. |
| Competition whitespace | 0.5 | 0.9 | Exact in-house and SHINE implementations bracket the product. |
| Reachable validation budget | 3 | 5.4 | Buildable, but radiation access and independent benchmark are unpriced. |
| Elegance/controllability | 4 | 8.8 | Phase, delay, restart, fault, and identity are measurable. |
| 10x technical edge | 1 | 1.4 | Exact incumbent comparisons are approximately 2x–6x, not 10x. |
| US–China leverage | 3 | 6.0 | Credible US-only job; no China claim. |
| 2030 launch window | 1 | 1.6 | Buyer design-in closes materially before launch. |
| Expansion economics | 2 | 1.2 | FEL/quantum/telescope use is plausible but facility-specific. |
| Founder transfer | 5 | 2.0 | Correctly capped at 2% and not used to rescue a gate. |

Total: **55.1/100**; the 11 weighted terms sum exactly.

**Exact regeneration conditions.** Do not reinstate this version. A materially new thesis could be
red-teamed only if, by end-2028, a named US detector group (1) issues a written requirement that
the ppRDO/TCLink implementation does not meet, (2) accepts a third-party FMC/AMC interface, and
(3) funds or signs a non-cancellable evaluation that includes incumbent-blind benchmarking and
radiation access. The experiment counts under $100k only with a facility letter/quote keeping the
complete four-card, environmental, metrology, and radiation campaign at or below $99,999. Kill on
no paid interface, any silent unlocalized phase slip, or failure to beat the exact in-house board—not
a generic sub-nanosecond switch—on a buyer-valued metric.

**Final verdict: KILL.** Exact demand validates ePIC's internal engineering program more strongly
than it validates an open 2030 merchant socket.

## `P5-USSCI-S02` — adaptive SRF field-stability daughtercard

### Strongest bear case

**Factual evidence.** Fermilab's 2022 report is an exact historical pain record: large Lorentz-force
detuning, fast-piezo feedback problems, suspected ponderomotive instability, and further
calibration before full-gradient operation
([PIP-II Director report, p. 3](https://pip2.fnal.gov/wp-content/uploads/2022/09/PIPII-DirectorsReport-AUG22-Final.pdf)).
It is not current proof that the problem remains unfilled. Fermilab had already developed piezo-to-
cavity transfer-function measurement/estimation, system identification, controller simulation,
inverse-model control, and resonance-control validation for multiple PIP-II cavity types in 2019
([Fermilab resonance-control program, pp. 7–20](https://indico.fnal.gov/event/21836/contributions/64922/attachments/40806/49407/STC650ResonanceControl_Talk.pdf)).

Brookhaven's present program further narrows the wedge. The 2025 CD-3B review calls RF-controls
integration “very mature,” says ten Common Platform chassis were ordered, and records JLab
up/down-converter development
([EIC CD-3B review, pp. 12–13](https://indico.bnl.gov/event/26584/attachments/62175/106795/EIC%20CD-3B%20Director%27s%20Review%20Final%20Report.pdf)).
BNL's November 2025 FPGA simulator already includes validated cavity electrical and mechanical
models, Lorentz-force detuning, microphonics, amplifier nonlinearity, and beam behavior
([BNL cavity simulator](https://technotes.bnl.gov/PDF?publicationId=229149)).
Its June 2026 real-cavity test used the lab's own modular carrier/daughtercard platform and FPGA
feedback algorithms; the team fixed hardware/algorithm bugs in-house and is refining it for the
next integration cycle
([BNL real-world test](https://www.bnl.gov/newsroom/news.php?a=222988)).
A separate 2026 BNL note demonstrates an in-house digital network analyzer, model-based tuner,
one-turn feedback, and adaptive feed-forward, with the remaining algorithm explicitly planned for
the Common Platform
([BNL EIC RF algorithms](https://technotes.bnl.gov/PDF?publicationId=229314)).
Libera LLRF is the commercial full-stack incumbent with MTCA modularity, cavity tuning, machine
protection, EPICS, commissioning, training, and lifecycle support
([Libera LLRF](https://www.i-tech.si/products/libera-llrf/)).

**Inference/judgment.** Online, continuously updated electromechanical identification plus hard
safety constraints is a real architectural delta from fixed or campaign-based tuning. But the
buyer teams already own the FPGA platform, simulator, identification methods, adaptive algorithms,
and safety integration. The proposal has not shown that portability across cavity families is a
purchased product rather than expert collaboration/software work. Current BNL evidence concerns
beam-loading and broad LLRF control, not a request for a merchant piezo-predistortion daughtercard;
the only exact PIP-II failure record is four years old.

### Hard gates

| Gate | Verdict | Independent rationale |
|---|---|---|
| G1 | **FAIL on current evidence** | Fermilab supplies one exact but stale pain record. Current BNL records prove active LLRF spending and a modular socket, but not the exact adaptive electromechanical/piezo job. Two current, independent exact-job sources including a primary buyer specification are not yet present. |
| G2 | **PASS** | All six claimed academic sources are final journal articles. The 2026 PRAB record, 2024 real-cavity ADRC experiment, 2023 PRAB RLS paper, 2018 PRAB simulator, 2021 NIM A identification paper, and 2017 IEEE controller paper have stable final-publication evidence. |
| G3 | **PASS_CONDITIONAL** | The $145k sum and 12-month transfer/safety kills are coherent, but the decisive real-cavity leg depends on an uncommitted $36k test-stand-access line. Emulator-only work is not decisive. |
| G4 | **PASS_MARGINAL** | Continuous online, constrained, cross-cavity adaptation is non-cosmetic. However, exact in-house system-identification/control programs were underweighted, leaving little demonstrated whitespace. |
| G5 | **PASS** | Technical literature demonstrates identification and active detuning control. Portability, independent safety, and willingness to buy remain unproven. |
| G6 | **PASS** | Independent interlocks, hard output bounds, watchdog fallback, signatures, operator override, and a US civilian base case form a credible path. |
| G7 | **FAIL on current evidence** | PIP-II commissioning and EIC construction are real timing anchors, but the control hardware and algorithms are being selected and built before 2030. No primary 2030–34 record identifies a merchant adaptive daughtercard, retrofit, or spares procurement trigger. |

### Revised scoring and arithmetic

| Criterion | Raw | Weighted | Reason |
|---|---:|---:|---|
| Demonstrated demand | 3 | 9.6 | Exact historical pain plus current category spending; product-specific current demand missing. |
| Frontier/coolness | 3 | 9.0 | Self-characterizing cavities are compelling but not a new research direction. |
| High-end niche | 3 | 6.0 | High-value systems, tiny and expert-dominated buyer set. |
| Competition whitespace | 1 | 1.8 | In-house teams own most enabling blocks; Libera covers the commercial stack. |
| Reachable validation budget | 3 | 5.4 | Bounded only with written SRF access. |
| Elegance/controllability | 4 | 8.8 | Identification, modes, guards, and detuning are measurable. |
| 10x technical edge | 2 | 2.8 | 10x versus no compensation is plausible; 5x versus current fixed feed-forward is unproved. |
| US–China leverage | 3 | 6.0 | Credible US-only context; no China claim. |
| 2030 launch window | 2 | 3.2 | Commissioning continues, but design-in and incumbent convergence precede launch. |
| Expansion economics | 2 | 1.2 | Adjacent facilities need substantial applications engineering. |
| Founder transfer | 5 | 2.0 | Correctly capped at 2% and not gate-rescuing. |

Total: **55.8/100**; the 11 weighted terms sum exactly.

**Exact hold-release conditions.** Reinstate and count US/scientific/process-output only if all of
the following occur by end-2028: (1) a named Fermilab, BNL, JLab, or other US lab issues a written
requirement for online electromechanical identification and constrained adaptive piezo control;
(2) the lab supplies a frozen Common Platform/MTCA.4 interface and a signed paid evaluation,
CRADA/SBIR work package, or procurement path; (3) written test-stand access and a priced cryogenic
run close the $145k budget; and (4) an independent retest across two cavity families achieves at
least 5x peak-detuning reduction versus the buyer's current fixed feed-forward, at least 20% RF-
overhead reduction, no escaped injected unsafe mode, and no manual code fork between cavity classes.
Kill on any missing condition or if the lab requires source-code collaboration without a repeatable
commercial license/support path.

**Final verdict: HOLD.** This is the only repairable candidate of the two, but it is not eligible
for the final 24 or US/scientific counts until the exact buyer and interface events occur.

## Cross-candidate source and experiment audit

- `S01`'s 14-source quota is mechanically credible if the proposed new records are accepted: five
  final peer-reviewed works, multiple primary ePIC documents, competitor-primary pages, and
  geography/timing records. The demand documents are highly program-correlated; do not describe
  them as independent market replication. The SHINE paper is both technical validation and adverse
  exact-incumbent evidence.
- `S02`'s six claimed peer works are valid final publications and independent across CN, European,
  Japanese/Indonesian, and multinational research groups. BNL and Fermilab provide independent
  buyer organizations, but only Fermilab currently documents the exact piezo/electromechanical job.
- Both proposal score totals and both budget breakdowns add correctly. Arithmetic was not the
  failure mode.
- **Decisive <$100k count: zero.** `S01`'s nominal $98k campaign lacks a radiation-access quote or
  commitment and benchmarks a generic metrology reference rather than the exact in-house endpoint.
  `S02` is $145k and also lacks committed SRF access. Commercial interviews alone may test the
  merchant socket, but an inexpensive hardware demo must not be relabeled decisive.

