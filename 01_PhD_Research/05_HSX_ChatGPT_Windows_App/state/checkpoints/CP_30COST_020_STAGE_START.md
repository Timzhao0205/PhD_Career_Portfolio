# CP_30COST_020_STAGE_START

- Timestamp: `2026-07-13T11:00:23-07:00`.
- Mission/status: `IN_PROGRESS`.
- Current stage: `30 package / cost-down revision`.
- Objective: simplify the 250 deg C UHV three-axis head so custom ceramic is limited to flat, repeatable, reusable cartridge parts and the structural package is inexpensive flat/formed CP-Ti, while preserving independent sensor/LCC service and the diameter 31.75 mm by height 27.5 mm installed envelope.
- User design-changing input: the accepted corrected Concept A remains too costly as a CNC ceramic package.
- Actual model/effort: GPT-5 reported by system; active high-reasoning parent session; Sol/xhigh selector unavailable; `MODEL_CONTROL_UNAVAILABLE`; no delegation and no known downgrade.
- Git baseline: clean worktree at `c38d8ffec60aa72d1736cd2edcb6f2bab1d03ebe`; local repository only.

## Recovery snapshot

- Accepted stages 00, 05, 10 and 20 remain controlling and are not reopened.
- Stage 30, its Stage-40 mechanical review and the mechanical portion of Stage 50 are reopened.
- The previous physical package used three 9.60 x 9.60 x 1.00 mm fixed zirconia seats, three separate guarded cartridges, three 15.60 mm clamps, six face screws, six nut plates and six keepers in a 39-solid assembly.
- Its verified kernel bounds were radius 14.354 mm and height 26.750 mm with zero unintended overlap; these are the comparison baseline, not the cost-down target.
- Binding constraints retained: 250 deg C continuous UHV; three mutually orthogonal isolated four-terminal sensors; all installed parts within the cylinder; no adhesive in the reusable head; each bonded sensor/LCC independently removable, reusable and protected; zero tapped/internal ceramic threads; external accessible nonmagnetic hardware; no load through electrical joints.

## Cost-down hypothesis to test

1. Delete the three fixed ceramic seats entirely.
2. Make each protected sensor/LCC/fanout assembly a single reusable flat ceramic cartridge plate manufactured from stock substrate by straight outline/window/notch operations, not a pocketed 3-D CNC body.
3. Replace the machined structural cage/backframes with flat-cut and formed CP-Ti members.
4. Use one broad externally accessible clamp screw plus a positive open hook/rail and three-point hard stops per face, reducing face screws/nuts/keepers from six to three without preventing single-axis service.
5. Preserve three independent 3.80-mm cable corridors and remote keyed four-circuit disconnects.

All dimensions, contact/preload values, material substitutions and production processes remain `ENGINEERING PROPOSAL - VALIDATE` until supported and checked. Fabrication and ordering remain on hold.

## Deterministic next action

Capture primary vendor/process evidence for flat alumina/zirconia substrate cutting and CP-Ti sheet forming; model at least three cost-down concepts; select the hard-gate survivor; export/reimport real-kernel CAD; produce dimension, collision, fastener, service and 1/3/10 RFQ ledgers; visually inspect the drawings; save the Stage-30 revision checkpoint; then run independent Stage 40 and final Stage 50 revision audits.
