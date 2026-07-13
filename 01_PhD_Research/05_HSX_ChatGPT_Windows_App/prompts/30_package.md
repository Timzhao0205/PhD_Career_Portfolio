Design a reusable, low-cost CNC ceramic 3-axis head for continuous 250 deg C UHV. Read all current
outputs, previous CAD/reports, envelope, LCC interface, harness map, and sources. Load STEP with a
real CAD kernel when available. Treat prior PEEK/BeCu concepts as unqualified until current
evidence clears continuous 250 deg C.

Hard gates: UHV/250 deg C, non-magnetic/material compatibility, 31.75 mm diameter x 27.5 mm
envelope, three orthogonal faces, protected exposed bond wires, removable bonded LCCs, no adhesive,
and **zero tapped/internal zirconia threads in the recommended baseline**.

Develop at least three manufacturable concepts:

1. cost-focused modular trihedral cage with three identical flat zirconia seats/cartridges;
2. simplified monolithic zirconia core with removable external face clamps;
3. split-clamshell or cartridge design with rear contacts and bond-wire protection.

Prefer simple green/near-net-machined flat parts, open pockets, relaxed tolerances, radii, smooth
through-holes, straight tools, external Ti frames, transverse pins, and accessible replaceable Ti
nuts/nut plates. Reject bonded inserts, hidden nuts, undercuts, blind nut traps, cross-bolt
collisions, and service that requires removing another sensor.

For each concept calculate and document:

- bounding cylinder/height and installed harness/fastener envelope;
- carrier tolerance and seat clearance;
- contact/preload stack at 20 and 250 deg C, worst-case tolerance, creep/relaxation;
- minimum wall, edge distance, radius, and ceramic stress mode;
- every screw axis, head, nut, tool path, and collision/assembly sequence;
- wire bend and bond-wire keep-out;
- independent carrier replacement and electrical remating procedure;
- part count, unique ceramic geometries, post-fire operations, NRE/per-unit cost drivers, and
  budgetary 1/3/10-set RFQ ranges when available.

After hard-gate filtering, score: fabrication cost/simplicity 30; bonded LCC reuse/damage risk 25;
connection reliability/serviceability 25; thermal/tolerance/calibration 10; assembly/tool access 10.

Write:

- `outputs/30_REUSABLE_3D_PACKAGE_250C_UHV.md`;
- `outputs/30_DIMENSION_AND_COLLISION_LEDGER.csv`;
- `outputs/30_FASTENER_AND_THREAD_SCHEDULE.csv` (ceramic thread count target zero);
- conceptual isometric/exploded, top-envelope, section, contact detail, and fastener-axis SVGs for
  every concept under `outputs/drawings/`;
- parametric CAD and STEP/STL only where dimensional validation is possible, clearly marked
  `NOT FOR FABRICATION` until red-team closure.

Update sources and gates. Do not edit previous results.
