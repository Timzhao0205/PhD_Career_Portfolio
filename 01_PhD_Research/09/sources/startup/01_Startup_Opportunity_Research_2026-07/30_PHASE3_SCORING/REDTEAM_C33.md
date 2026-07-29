# RED TEAM — C33: Cryogenic current-distribution & quench-onset QC instruments for HTS coil production

**Verdict: kill-probability ~75%.**

## Strongest bear case

The addressable market is ~15–25 organizations worldwide by 2030, and the most valuable ones treat coil QC as core process IP they will never outsource. CFS co-developed fiber-optic quench detection with MIT PSFC [RT-C33-01][RT-C33-02]; Tokamak Energy holds granted US patents on quench detection generally (US11101059B2) and — fatally for this concept — on **magnetic-field-based quench detection specifically** (US11749434B2, granted 2023, expires 2038) [RT-C33-05][RT-C33-09]. Even a Chinese fusion startup, Startorus (星环聚能), has filed its own quench-detection-system patent [RT-C33-04]. When your three flagship prospective customers have each patented the thing you plan to sell them, you don't have a product company — you have a thesis chapter. At a $100–300K ASP and optimistically 5 units/year, this is a $1M/year revenue business that can never return venture capital; it collapses into consulting.

## Hidden competition

- **Tokamak Energy Ltd** — US11749434B2 "Strain- or magnetic field-based quench detection" and US11101059B2 (HTS-tape-strip sensing). Direct freedom-to-operate threat, not just competition [RT-C33-05][RT-C33-09].
- **Fiber-optic quench detection (MIT/CFS lineage)** — FBG/Rayleigh sensing demonstrated on VIPER cable at SULTAN with 2–3x better SNR than voltage taps and tens-of-seconds-earlier detection; being co-wound into cables at manufacture, which pre-empts an external Hall instrument [RT-C33-01][RT-C33-02]. Chinese teams are replicating this for CFETR-class conductors [RT-C33-03], and Chinese literature explicitly frames 光纤传感 as the quench-detection path for HTS coils.
- **THEVA TAPESTAR** — the incumbent non-contact Ic-uniformity QC instrument, used by "all well-known tape producers"; it captures the defect-screening value **upstream at the tape level**, shrinking what a coil-level instrument can add [RT-C33-06].
- **Metrolab, Lake Shore Cryotronics, Senis** — established Hall-probe/field-camera vendors already selling cryogenic Hall sensors and mapping systems to magnet manufacturers (Lake Shore HGCA cryogenic Hall sensors are already used per-winding-pack in HTS test stands) [RT-C33-07]. Any of them can package an array + inversion software in a quarter if demand materializes.
- **In-house rigs** — HTS-110, General Atomics, Canyon Magnet Energy all advertise internal winding + conductor-qualification + test capability [RT-C33-08].

## Physics/engineering reality check

The cited edge rests on lab-grade CCCs [S175] and a current-distribution-monitoring paper [S066] — the latter authored within the fusion-magnet community the founder would sell to, i.e., the method is published, unpatented-by-him, and reproducible by every customer. CCCs need SQUID-grade shielding and are notoriously unhappy on a factory floor. Inverting an external Hall-array map to internal current distribution in an NI pancake is an ill-posed problem; screening currents that make QC "hard" also make the inversion non-unique at production tolerances. The defensible residue is software, which customers' magnet-modeling teams already write.

## Market skepticism

No cited source shows any coil maker asking to **buy** such an instrument; [S054] documents fusion magnet QC needs generically, and [S051] is a Sina Finance listicle about Chinese localization — evidence of Chinese in-house capability, not import demand (and an instrument aimed at fusion-magnet QC will face 国产化 substitution anyway). Magnet builders' willingness-to-pay is revealed by behavior: they patent and build detection themselves.

## Founder-fit doubts

This is the founder's PhD lane (diagnostics cap — quota-constrained by design). Solo founder, seed budget: every sale requires cryogenic on-site integration at a customer whose engineers know the physics as well as he does — a services trap. No channel, no cryo-plant capital, and a 2029/2030 launch lands after CFS/Tokamak Energy have frozen their QA stacks for first-of-a-kind machines.

## Score adjustments

- **Market size/beachhead: −1** — ~20 identifiable buyers; strongest ones are DIY-with-patents.
- **Defensibility/moat: −1** — Tokamak Energy's US11749434B2 covers magnetic-field-based quench detection; core method papers are public.
- **Competition intensity: −1** — fiber-optic co-wound sensing is winning the architecture battle inside cables.
- **Feasibility/TRL: +1** — genuinely 18-month buildable; the tech risk is low even if the business isn't.

## Steelman rebuttal

A believer would say: fiber and voltage taps protect operating magnets, but nothing today gives a factory a pass/fail current-distribution signature on an NI coil **before** it ships — that's a QC gap, not a protection gap, and Tokamak Energy's patent covers in-magnet detection, not standalone factory metrology. If 5–10 fusion companies each ramp multi-coil production lines post-2028, a $300K instrument that prevents one $2M coil scrap pays for itself, and the founder is one of perhaps a dozen people alive who has fielded cryogenic Hall arrays on a real stellarator.
