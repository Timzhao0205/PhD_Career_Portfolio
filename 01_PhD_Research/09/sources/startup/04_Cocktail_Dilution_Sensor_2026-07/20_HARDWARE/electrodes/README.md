# IDE electrode coupon panel — design spec (KiCad)

Panel of interdigitated-electrode coupons for pitch selection.

Per coupon:
- Pitches: 150 / 200 / 300 um (6 / 8 / 12 mil trace+space — standard
  JLCPCB/OSH Park capability). One coupon per pitch, 2x replicates.
- Active area ~8 x 12 mm, 20-40 finger pairs; finger width = gap.
- GUARD RING: grounded ring surrounding each IDE, separate net,
  stitched to a back-side ground pour — rejects hand/glass parasitics.
- Finish: ENIG (flat, solderable, corrosion-resistant under coating).
- Connector end: 0.1" castellated or SMA-able pads at the TOP of a
  finger-shaped board (dipstick form); sensing area at the bottom.
- One coupon variant: coplanar pad PAIR at ~10 mm pitch for the
  through-glass stretch test.
- Passivation after assembly: parylene-C (SNF) primary; 422B silicone
  backup. Bare ENIG in ethanol-water WILL drift (electrochemistry).

Acceptance: air/DI/IPA discrimination (P0-E0), 30-min DI drift within
FDC noise, guard ring demonstrably kills hand-wave sensitivity.
