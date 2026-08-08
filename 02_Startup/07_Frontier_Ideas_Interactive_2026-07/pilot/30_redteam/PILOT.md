# Stage 30_redteam pilot

Run: 2026-07-28 (UTC). Status: **PASS**. Errors: none.

Three survivors with different risk profiles were attacked end-to-end:
P3R2-D-02 (top-ranked instrument play), P3R2-C-01 (platform-absorption risk),
P3R2-F-23 (policy- and science-contingent device).

## Paths exercised

1. **Current competitor verification (live):** THEVA TapeStar was checked
   against vendor/distributor pages. Finding: TapeStar is a merchant
   instrument sold openly (Quantum Design distribution; "many laboratories and
   well-known tape producers" as users) — the P4 frame that only captive
   in-house scanners exist is wrong. D-02's wedge must be restated to the
   delamination/lock-in channel, calibrated acceptance reporting, cable/CICC
   stations, and neutrality against a producer-owned competitor.
2. **Technical kill tests:** C-01's sub-100us/800V/500A interruption with arc
   discrimination; F-23's binding 2,000h A/B degradation-reduction proof;
   D-02's blind Ic correlation plus delamination detection beyond TapeStar.
3. **Commercial kill tests:** OCP-reference-design absorption for C-01;
   lender refusal to price third-party evidence hardware for F-23; tape-vendor
   self-certification acceptance for D-02.
4. **Fact/inference separation:** recorded explicitly per attack (e.g., 5/7
   hub restoration is fact; lender technical requirements are inference).
5. **Decisions:** survive (C-01), repair (D-02, F-23) — previews only; the
   full pass re-decides all 30. No final-24 selection was made.

## Lessons

- Re-verify whitespace claims against live vendor pages; even fresh P4 frames
  can be stale.
- Lead each attack with the idea's own recorded fatal uncertainties.
- Bounded source-retriever batches will verify load-bearing current claims in
  the full pass; the main Fable agent makes every decision.
