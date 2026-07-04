# RED TEAM — C35: Modular solid-state RF amplifier cassettes for compact particle-therapy accelerators

**Verdict: kill-probability ~85%.**

## Strongest bear case

This is not a gap — it is a mature merchant market with a customer base of roughly five to seven
accelerator OEMs worldwide, each of which either already builds solid-state RF in-house or has a
decades-qualified supplier. IBA — the named US-angle beachhead — designed and built its own
its own solid-state power amplifier at 176 MHz for MYRRHA [RT-C35-05]; it is a *seller* of SSA capability, not a buyer.
A solo founder launching a v1 cassette in 2030 enters a 3–5-year OEM design-in cycle against
vendors with 20 years of installed-fleet reliability data. The company dies waiting for its first
qualification, not on technology.

## Hidden competition (the one-pager missed all of it)

- **BTESA (Spain)** already sells exactly this product: hot-pluggable, N+1-redundant, water-cooled
  SSAs from 10 kW to 500 kW for accelerators; CERN awarded it a 350 kW/101 MHz tube-replacement
  system, prototype validated 2021, presenting at IPAC 2026 [RT-C35-01][RT-C35-02].
- **R&K (Japan)** — "gold standard" narrowband accelerator SSAs, 4-year warranty; APS bought a
  commercial 32 kW/352 MHz R&K system off the shelf [RT-C35-03][RT-C35-04].
- **RFHIC (Korea)** — GaN-on-SiC SSPAs to 30 kW/module, active accelerator contracts (POSTECH
  synchrotron, 2025) [RT-C35-06]. It owns the exact "GaN cassette" positioning at chip-to-system scale.
- **China:** 成都沃特塞恩 (Wattsine) sells 5.2 kW accelerator SSPAs domestically [RT-C35-07];
  国睿科技/CETC-14 supplies accelerator power subsystems to SSRF [RT-C35-12]; and 合肥中科离子
  (CAS Hefei) explicitly advertises having broken subsystem "卡脖子" dependencies in its 240 MeV
  superconducting cyclotron [RT-C35-08]. The "41+8 unit" Chinese quota [S204] funds *domestic
  self-supply*, confirming the candidate's own 国产化-exclusion flag.
- Others unexamined: Cryoelectra (Germany, proton-therapy SSAs), DB Elettronica, IFI, Ampegon.

## Physics/engineering reality check

The "extreme edge" evaporates on inspection. Solid-state accelerator RF is 20-year-old practice —
ESRF/SOLEIL ran 40–190 kW SSAs in the 2000s [RT-C35-11]. The cited 68–71% efficiency at 83 MHz
[S192][S193] comes from *published academic work by others* (SKKUCY-10, Korea) — it is prior art,
not a moat. Worse, at VHF (30–100 MHz, where cyclotrons live) cheap LDMOS matches GaN performance;
GaN-on-SiC's advantage is at ≥1 GHz. Wolfspeed exited RF (sold to MACOM, 2023) [RT-C35-10],
so the device supply chain is itself consolidating. Combining, phase-matching, and graceful
degradation are solved and shipping at BTESA/R&K production tolerances today.

## Market skepticism

"Downtime is the metric hospitals pay for" — but hospitals buy uptime from the *OEM service
contract*, never from a component vendor; the cassette maker captures none of that premium. The end
market is financially sick: Maryland Proton Treatment Center defaulted on $267M of bonds; Proton
International Arkansas is distressed [RT-C35-09]. Global installs run ~30–40 systems/year; even at
$1M of RF per system the merchant TAM is <$50M/year, shared among the incumbents above. No cited
source shows any OEM soliciting a second RF source.

## Founder-fit doubts

A seed-scale solo founder cannot afford 100 kW-class test infrastructure (RF dummy loads, water
plant, shielded test cell), cannot generate the thousands of unit-hours of MTBF data OEM
qualification demands, has no channel into IBA/Hitachi/Sumitomo/Varian procurement, and loses
accelerator access on leaving Stanford. RF talent transfer is real; everything else — channel,
capital, reliability dossier — is missing.

## Score adjustments

- **Moat/defensibility −1:** BTESA/R&K/RFHIC ship the identical product; academic prior art is the claimed edge.
- **Beachhead/market −1:** ~5 concentrated OEM buyers, most self-supplying; distressed end market.
- **China angle −1:** 国产化 policy plus domestic suppliers (Wattsine, CETC-14, CAS Hefei) exclude a US solo founder.
- **Capital efficiency −1:** 100 kW test infrastructure and OEM qual timelines are incompatible with seed budget.
- **Founder fit:** hold — skill match is genuine; it is the only criterion that survives.

## Steelman rebuttal

Tetrode/tube supply is genuinely dying, incumbents' SSAs are bulky rack systems rather than true
field-swappable cassettes with LLRF health analytics, and OEMs increasingly want second sources for
supply-chain resilience. A founder who wins one compact-cyclotron design slot (e.g., a national-lab
newbuild) rides a 20-year installed-base annuity, and fusion ICRH plus industrial accelerators
triple the TAM beyond therapy.
