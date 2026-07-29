# RED TEAM — C06: Solid-state DC arc-fault & ground-fault protection for 800 VDC data centers

Reviewer stance: adversarial. Scored 84.0 (rank 5). I think that is 6–10 points too high.

## Strongest bear case

The window closes before the founder can enter. The one-pager's core claim — "sub-ms solid-state
clearing at 800 V/kA class... no incumbent ships as a rack-level product" [S223, a 2016 paper on
380 VDC] — was already false in late 2025. ABB's SACE Infinitus is an IEC-certified SSCB
(1000 V/2500 A) with an announced NVIDIA data-center adaptation [RT-C06-01][RT-C06-08]; Siemens
ships the SENTRON 3QD2 SiC breaker with Infineon CoolSiC modules explicitly targeting DC data
centers [RT-C06-03][RT-C06-02]. NVIDIA's own 800 VDC ecosystem list names ABB, Eaton, Siemens,
Schneider, Vertiv, Hitachi Energy, Mitsubishi — no seat for a 2029 startup [RT-C06-09]. First
Kyber-class 800 VDC halls qualify in 2027; protection vendors are being locked in during
2026–2027 design-ins, two to three years before Tim can ship anything.

## Hidden competition (named)

- **ABB SACE Infinitus** — first IEC-certified SSCB, NVIDIA collaboration [RT-C06-01][RT-C06-08].
- **Siemens SENTRON 3QD2 + Infineon** — SiC SSCB, microsecond interruption, DC-grid/data-center
  positioning [RT-C06-03][RT-C06-02].
- **Atom Power** — first UL-listed digital SSCB, SiC module, million-cycle tested, marketing
  directly at data centers [RT-C06-04].
- **Blixt (Stockholm)** — Infineon-backed AC/DC SSCB startup [RT-C06-05].
- **China:** 良信 (Liangxin/Nader) claims SiC SSCB <100 μs, zero-arc, GB200/GB300 adaptation
  testing, deployed at China Mobile Hohhot and China Unicom sites [RT-C06-06]; 泰永长征 (TYT)
  is described as Delta Electronics' exclusive domestic SSCB supplier entering NVIDIA Rubin and
  Google TPU chains, mass production year 2026 [RT-C06-07] (both are stock-forum claims, Tier 3,
  but the products and deployments are named and checkable). 中熔电气 (Sinofuse) covers the
  fuse-backup layer to 1000 V+ across the HVDC stack [RT-C06-10]. The "China standards-shaping
  opportunity" [S040] is effectively gone — domestic players are already installed.

## Physics/engineering reality check

Sub-ms interruption is not the moat the one-pager thinks: SiC/JFET-based SSCBs interrupting in
microseconds are catalog reality [RT-C06-02][RT-C06-03]. The genuinely hard residual — series
arc-fault *discrimination* on a noisy 800 VDC bus feeding switching converters (avoiding nuisance
trips that drop a $4M rack) — is real, but it is an algorithm/dataset problem where incumbents
with thousands of fielded breakers accumulate training data faster than a startup. At production
tolerances the differentiator collapses to firmware, which incumbents can license or copy, and
the cost floor (SiC conduction losses forcing hybrid designs, galvanic isolation contacts required
by UL 489I) is identical for everyone.

## Market skepticism

No hyperscaler quote supports $5–25K/module willingness-to-pay; NVIDIA's own blog treats
protection as "fuse-and-disconnect combinations or emerging solid-state devices" — fuses remain
the cheap default at rack level [RT-C06-09]. Facility-electrical teams buy life-safety gear from
UL/IEC-listed incumbents with decades of liability track record and installed service networks;
an unlisted seed-stage module is a career risk for the buyer. UL 489I Edition 1 only became an
ANSI standard in October 2025 [RT-C06-11] — certifying against it at 800 V/kA requires high-power
lab campaigns (KEMA/UL) costing seven figures and 18–30 months.

## Founder-fit doubts

Solo founder, seed budget, 2029 launch: he cannot fund kA-class interruption test campaigns, NRTL
listing, and a demo fleet simultaneously. No switchgear-channel relationships, no field-service
organization (mandatory for protection gear), no standards-committee standing. WBG + sensing +
firmware fits the *technology* but not the *certification-and-liability business* this actually is.

## Score adjustments

- Extreme edge 4→3: incumbents already ship 800 V-class SSCBs; edge is firmware only.
- Whitespace/moat 4→3: five named direct competitors incl. two NVIDIA-adapted Chinese lines.
- Beachhead 5→4: hyperscaler protection procurement is closed-list, incumbent-only.
- China+US 4→3: China slot already taken by Liangxin/TYT with domestic-substitution tailwind.
- Why-2029 5→4: the design-in window is 2026–2027, not 2029 — timing works *against* him.
- Net: ~84.0 → ~76, out of the top 5.

## Steelman rebuttal

Incumbent SSCBs are feeder/row-level boxes; nobody yet ships a certified *rack-level*,
field-replaceable module with integrated series-arc discrimination, and NVIDIA itself says fault
detection in VDC systems "is a key area for innovation" [RT-C06-09]. UL 489I is brand-new, so
every player starts the 800 VDC certification clock at roughly the same time. A startup that wins
on arc-signature firmware could be a prime acquisition target for exactly the incumbents listed
above — a good exit even if it never wins hyperscaler prime-vendor status.
