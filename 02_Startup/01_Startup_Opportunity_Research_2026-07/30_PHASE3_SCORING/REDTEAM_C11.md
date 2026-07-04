# RED TEAM — C11: Fast solid-state HTS quench-protection switch & dump modules

Reviewer stance: adversarial. Current matrix score 86.8, rank 3 — too high.

## Strongest bear case

The product solves the wrong half of the problem. In HTS quench protection the hard, unsolved
problem is *detection* (slow normal-zone propagation makes quenches hard to see), not *dumping*.
Energy extraction itself is deliberately slow: ITER's Fast Discharge Units dump 40+ GJ with
7.5–14 s time constants because coil insulation caps dump voltage at ~10 kV, and V = L·dI/dt
means a "sub-millisecond dump" of any GJ- or even MJ-scale magnet requires physically inadmissible
terminal voltages [RT-C11-04]. Meanwhile the beachhead's actual design trend — no-insulation/
metal-insulation REBCO coils (CFS TFMC, ASIPP's 24.1 T all-REBCO magnet) — is *passively
self-protecting* by construction [RT-C11-09]. By 2031 the likely outcome: NI coils need no active
dump module, and insulated coils buy proven vacuum-breaker+resistor FDUs from incumbents. The
startup is squeezed to zero from both sides.

## Hidden competition

The one-pager names essentially no competitors. There are many:

- **Mitsubishi Electric / Scibreak**: VARC breaker already demonstrated 10 kA / 9 kV interruption
  in ~3 ms; Mitsubishi acquired Scibreak in 2023 explicitly to commercialize fast DC breakers
  [RT-C11-05][RT-C11-06]. ABB, Hitachi Energy, and Eaton all have hybrid DC breaker lines.
- **ASIPP (合肥等离子体所)** builds hybrid 100 kA-class quench-protection breakers in-house for
  EAST/CFETR/BEST and publishes concept designs — China's fusion demand is captive [RT-C11-02][RT-C11-03].
- **Tokamak Energy** holds granted US patents on quench detection *and* protection (e.g.
  US 11,190,006) — magnet builders are patenting this as core IP, not shopping for it [RT-C11-07].
- **Oxford Sigma + STEP Fusion/Strathclyde** already demonstrated a fusion magnet-protection
  "safety valve" aimed at the UK STEP program [S065] — the exact niche, occupied first.
- **HTS-110, American Magnetics, Cryomagnetics, Oxford Instruments** ship magnets with protection
  integrated into coil + power-supply design [RT-C11-08]; Chinese MRI magnet makers (宁波健信,
  辰光医疗) likewise integrate vertically [RT-C11-10].

## Physics/engineering reality check

"Sub-ms kA-class solid-state switching" is real but not scarce — it is a standard IGCT/press-pack
IGBT application; CERN's own 2025 review treats switch hardware as available and names detection,
CLIQ, and current-sharing control as the open problems [RT-C11-01]. The defensible-sounding edge
evaporates at system level: semiconductor on-state loss in a kA DC loop forces a parallel
mechanical bypass anyway (i.e., you rebuild the known hybrid breaker), and the SFCL analogy [S085]
cuts the wrong way — Nexans/AMSC SFCLs are the field's most famous commercial *failure*, a
category that never escaped pilots.

## Market skepticism

No cited source shows a magnet builder wanting to *buy* protection. Protection is safety-critical,
liability-carrying, and inseparably coupled to coil inductance, insulation class, and cryogenics —
exactly what integrators keep in-house (CFS, Tokamak Energy patents, ASIPP all do). The $50–500K
ASP is asserted, not evidenced. Fusion buyers number ~10 worldwide with multi-year qualification
cycles; NI-trending MRI/motor magnets may need no dump at all. Real WTP evidence: none.

## Founder-fit doubts

Solo founder selling a safety-critical subsystem: who signs the liability and functional-safety
case (IEC 61508-style) in 2030? Qualification needs a kA-class cryogenic test stand — $1M+ capex
the plan hand-waves; a "bench prototype without magnets" proves nothing a buyer will accept. No
channel into conservative big-science procurement, and China sales of fusion-adjacent power
switching sit near export-control tripwires both directions.

## Score adjustments (±1)

- **C2 Extreme edge: 5 → 4** — sub-ms dump is voltage-limited physics theater; hybrid breakers already exist.
- **C3 Beachhead: 4 → 3** — no evidence any builder buys rather than builds; NI coils shrink the need.
- **C7 Whitespace/moat: 4 → 3** — Mitsubishi/Scibreak, ASIPP, Tokamak Energy IP, Oxford Sigma un-named in the pager.
- **C6 TRL path: 4 → 3** — qualified safety product needs cryo kA test infrastructure, not 18-month bench work.

## Steelman rebuttal

A believer would say: NI coils don't scale to fast-ramping tokamak CS/PF coils or grid-connected
SMES, so active protection survives; incumbents build 70 kA stadium-sized FDUs, not compact
$100K modules for the coming wave of 5–20 kA commercial HTS systems; and being the neutral,
qualified Tier-2 supplier (as OCEM is for power supplies) is precisely how small firms win in
big science. Detection-to-trip firmware plus switch could still become the "safety PLC" of HTS.

---
**Verdict:** Candidate C11 · kill probability ~70% · biggest objection: magnet integrators treat
quench protection as in-house safety IP while the physics need it claims to serve (sub-ms dump)
is voltage-limited out of existence — and NI coils remove the need entirely.
