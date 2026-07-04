# RED TEAM — V09 Field-hardened White-Rabbit-class timing & synchronization appliance

Date 2026-07-03 · Raw 86.8 · Sources: `REDTEAM_V09_sources.json` (RT-V09-01…17; 5 fetched)

## 1. Novelty verification (G7-NOVEL)

Full-ledger grep for timing/sync/clock/1588/GNSS/PNT/oscillator: zero hits (only false positives
— "synchronous compensator" RID-030, Synchron neural W-entry). Three nearest neighbors:
**C10** (precision magnet/scientific power converters — carries watts, not picoseconds; buyer
overlap is the same facility but a different budget line and product physics), **EXT-21**
(rad-hard in-vessel wireless telemetry — data link in a radiation environment, no clock
distribution), **C34** (ultra-low-noise SMU — analog source-measure bench instrument). No ledger
entry covers time-transfer/sync distribution as a category. Not a re-parameterization.
**Verdict: NOVEL — G7 passes.** The problem is the outside world, not the ledger.

## 2. Strongest bear case

The one-pager's premise — "nothing exists for unattended outdoor/remote nodes" — is factually
dead. LHAASO has run a field-hardened WR network since 2021: >8,000 detectors, 550+ WR switches,
outdoors at 4,410 m, with device temp range already extended to **-20…+70 °C** and automatic
temperature/link-delay compensation, built by Chinese WR vendor SyncTechnology [RT-V09-03].
Safran (Seven Solutions) ships the WR-ZEN TP-FL today: fanless, 1U, holdover option, marketed at
finance/defense/5G/fusion — only -10…+50 °C [RT-V09-01]. So V09's entire residual claim is a
-40 °C corner-case packaging delta on open (CERN OHL) hardware, aimed at a buyer pool
(unattended quantum nodes ex-China) realistically in the low hundreds by 2030, purchased on
grant cycles. By 2029 the WR Collaboration (8→18 members in one year; UNH-IOL testing/trademark
program; GMV commercializing WR Switch v4 under £2M Innovate UK; IQD quantum-clock expansion
board) will have multiple hardened, qualified SKUs [RT-V09-04][RT-V09-02]. A seed startup enters
a standard that incumbents co-own, with no IP moat, after the window shuts.

## 3. Hidden competition (missed by one-pager)

- **Safran**: WR-ZEN TP-FL/TP-32BNC nodes + WRS-LJ switch + VersaSync (MIL-STD-810G rugged
  master clock, mobile/harsh env — the defense-timing certs bench) [RT-V09-01][RT-V09-09][RT-V09-10].
- **SyncTechnology (China)**: WR Collaboration member; built the LHAASO hardened WR fleet
  [RT-V09-02][RT-V09-03]. Kills the "sell timing to CAS programs" China angle.
- **OPNT (NL)**: WR sub-ns time-as-a-service over existing fiber for telecom/finance/datacenters
  [RT-V09-06]. **Quincy Data** already sells WR-based timing service to finance; **Deutsche
  Börse, Jump Trading, Liquid-Markets** (WR NIC) deploy it [RT-V09-04].
- **Nu Quantum (UK)**: first quantum member; embeds WR inside its Quantum Networking Unit — the
  quantum-network timing socket gets absorbed into the network fabric vendor, not sold as a
  separate appliance [RT-V09-05].
- **GMV, Creotech Quantum, Timebeat**: WRS v4 commercialization, WR systems, low-cost open WR
  nodes [RT-V09-04][RT-V09-02][RT-V09-16].
- **From below**: Adtran/Oscilloquartz OSA 5405 rugged outdoor GNSS/STL PTP grandmasters;
  Microchip TimeProvider 4100 (PRTC/ePRTC class, mass-produced) — ns-class covers most "field
  timing" tenders without WR [RT-V09-07][RT-V09-08].
- **China demand side**: QuantumCTek/China Telecom Quantum own the QKD equipment chain
  (京沪干线, 588+ patents) [RT-V09-12]; domestic WR literature (LHAASO, HIAF) is mature
  [RT-V09-14][RT-V09-15].

## 4. Engineering reality check

Sub-ns field WR is hard in exactly one place — temperature-dependent link asymmetry and SFP
calibration drift — and that was solved publicly (LHAASO temp compensation, since 2021)
[RT-V09-03]. The rest is standard telecom hardening (fanless thermal at ~80 W, conformal coat,
redundant PSU, IP-rating, EMC). This is a packaging exercise Safran's Orolia/VersaSync unit
performs routinely on demand. Physics footnote: VLBI/optical-clock links at 10^-15…10^-17 need
optical carrier-phase transfer (Menlo/TimeTech class) or local masers — sub-ns WR is orders too
coarse, so that beachhead segment is a category mismatch.

## 5. WTP skepticism

Who pays $25–80K/node? EuroQCI buys through 26 national consortia and incumbent integrators
(operational target 2027 — before V09 ships) [RT-V09-13]; China buys domestic [RT-V09-12];
finance already buys WR from Quincy/Safran/Timebeat [RT-V09-04][RT-V09-16]; defense PNT demands
certs primes hold [RT-V09-09]. Remaining: DOE testbeds and radio astronomy — real but grant-fed,
tens of units/yr.

## 6. Founder-fit doubts

Not PhD-lane, but C1=5 is inflated: FPGA + big-physics credibility ≠ time-metrology pedigree.
Competitors are the literal WR authors (CERN spinout teams). No calibration-lab, telecom-cert,
or defense-channel experience. Anti-anchoring: "I can build it in 12 months" is true and
irrelevant — so can six collaboration members.

## 7. Score adjustments (±1, reasons)

| C | Raw→Adj | Reason |
|---|---|---|
| 1 | 5→4 | No timing-metrology pedigree; rivals wrote the standard |
| 2 | 4→3 | Hardened WR exists (LHAASO -20…+70 °C since 2021); residual edge = packaging increment |
| 3 | 4→3 | Ex-China unattended-node count low-hundreds by 2030; VLBI/optical segment mis-specced |
| 4 | 4 hold | Timing-as-infrastructure vision legitimate |
| 5 | 4→3 | GMV WRS v4 + WR testing program land 2026-27; window closes pre-launch |
| 6 | 5 hold | Feasible — that is the problem (low barrier) |
| 7 | 4→3 | Open-source base + 18-member industrial collaboration = no moat |
| 8 | 4→3 | China angle inverted (SyncTechnology/QuantumCTek domestic lock) |
| 9 | 4 hold | WR gear currently low export sensitivity — stands |
| 10 | 5 hold | v1 cheap on open hardware |
| 11 | 5 hold | Sells per-unit like a switch |

**Adjusted: 434−64 = 370/5 = 74.0** (−12.8; consistent with Round-1 stress norm −11.4).

## 8. Steelman

WR-standard fluency plus fleet-management/holdover-analytics software could still win the
un-glamorous merchant niche the giants ignore (Safran sells switches, not fleets; OPNT sells
service, not boxes), and the QKD/quantum-testbed wave gives a fresh buyer with no incumbent
habit. If timing-as-managed-infrastructure (hardware + recurring software) closes even 50
national-lab/quantum sites by 2030, it is a fundable wedge — a services-margin business, though,
not a category-defining one.

**Kill-probability: 65% · Biggest objection: hardened field WR already exists at 8,000-node
scale and the open WR Collaboration industrializes the rest before 2029 · Novelty: NOVEL (G7
pass).**
