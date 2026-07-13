# CP_50COST_024_STAGE_START

- Timestamp: `2026-07-13T11:45:48-07:00`.
- Mission/status: `IN_PROGRESS`; Stage-50D cost-down corrected synthesis `IN_PROGRESS`.
- Actual model/effort: GPT-5 reported by system; active high-reasoning parent session; Sol/xhigh selector unavailable; `MODEL_CONTROL_UNAVAILABLE`; no delegation and no known downgrade.
- Git recovery point: accepted Stage-40D commit `627bbe6a0d66c74410c9ed187155cf75400f77ce`.

## Objective

Produce the controlling, lower-cost final mechanical package and revalidate the complete engineering package. Preserve the independently removable bonded LCC cartridges, continuous 250 deg C UHV scope, zero ceramic threads, and the installed diameter 31.75 mm by height 27.5 mm envelope.

## Accepted inputs

- `outputs/30D_COST_DOWN_FLAT_PACKAGE_250C_UHV.md` and its frozen CAD/ledgers/drawings.
- `outputs/40D_COST_DOWN_INDEPENDENT_RED_TEAM.md` and its 48-row requirements trace.
- Existing accepted electrical, LCC, feedthrough, board and final-package artifacts.
- Primary source ledger S001-S060.

## Required corrections

1. True open U-slots and at least 1.4 mm nominal hook-release motion.
2. One identical rotation-only flat guard with pigtail notch and screw-edge relief.
3. A formed CP-Ti perimeter caddy that captures the guard/LCC/fanout without adhesive and carries all clamp load.
4. Nine explicit bracket lands and three caddy/land reactions per cartridge.
5. Three complete strain clips with adjacent solid lugs, screws and open nuts.
6. Four explicit top post fasteners.
7. Positive no-drop face-nut lances/pockets outside the clamp load path.
8. Correct the lowest face-hardware datum to 11.50 mm and recompute bounds/margins.
9. Add driver, 1.4-mm slide and cartridge-withdrawal service keepouts.
10. Include caddies and all retained hardware in the 1/3/10-set cost basis.
11. Keep the guard material selection neutral between quoted 99.6% alumina and flat ZTA/zirconia until coupon/UHV/hot results.
12. Retain a two-screw-per-face fallback until the one-screw/two-hook load case passes analysis and hot-cycle coupons.
13. Require measured lands/planes, full 3x3 calibration at 20/250 deg C, post-bake/hot/service repeats, and a complete-head magnetic field map.

## Validation required

- OpenCascade export and independent STEP reimport.
- Conservative radial/height bounds and proposed tolerance margins.
- Complete pairwise unintended-overlap check plus required zero-distance reactions.
- Exact guard identity by one reference solid and rotations only; binary STL triangle count.
- Installed cable corridors plus driver/slide/withdrawal swept-volume checks.
- CSV/XML/source/final-index/history checks and whole-package consistency audit.
- Final visual QA of the controlling mechanical drawing and CAD render.

## Open gates

All prior G50/G30D/G40D purchase/fabrication/qualification gates remain open until objectively closed. This synthesis may reach `COMPLETE_WITH_OPEN_GATES`; it does not authorize fabrication, ordering, bonding, hot operation or experimental release.

## Deterministic next action

Create `outputs/cad/50B_cost_down_corrected_package.py`, release the corrected assembly/part/service STEP and guard STL, generate dimension/fastener/cost ledgers and the controlling drawing, then update all four final reports and execute the whole-package audit.
