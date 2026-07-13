Perform the irreversible Hall die -> LCC02046 -> one-side harness review for continuous 250 deg C
UHV. Read all prior stage outputs, annotated image, LCC drawing, die-related inputs, netlist pin
convention, and historical packaging result. Inspect images directly.

Analyze the user's proposal exactly:

- inner shelf bonds: 8, 3, 19, 14;
- external routes: 8->4, 3->9, 19->13, 18->14;
- desire: four conductors exit one side, with electrically tied pads considered for strength.

Resolve the 14/18 inconsistency and numbering/orientation gates before issuing a fixed map. If die
p1-p4 orientation remains unverified, give an orientation-parametric map plus a mandatory
microscope sign-off; never guess.

Compare at minimum:

A. the user's four-corner/four-jumper concept;
B. shortest non-crossing die-to-nearest-shelf bonds plus a separate one-side breakout/contact;
C. qualified welded/crimped/flying-lead transition at selected castellations;
D. a reusable high-temperature socket/spring/contact concept;
E. any stronger evidence-backed hybrid.

Do not count a parallel electrical pad as mechanical strain relief. Decide whether solder has
adequate continuous-temperature margin and UHV cleanliness; otherwise name the process and coupon
validation needed. Address thermoelectric EMF, loops, Hall symmetry, parasitics, bond length/loop/
crossing, thermal cycling, handling, repair, and reuse.

Write:

- `outputs/10_LCC_WIREBOND_AND_EXTERNAL_JOIN.md`;
- `outputs/drawings/10_lcc_recommended_top.svg` with chamfer, numbered pads, die terminals, bonds,
  keep-outs, and orientation datum;
- `outputs/drawings/11_lcc_external_exit.svg` with transition joints, one-side exit, and separate
  strain relief;
- `outputs/10_BOND_AND_JOIN_QUALIFICATION.csv` with coupon lots, thermal/vacuum exposure,
  pull/shear, contact resistance, microscopy, cleaning/outgassing, acceptance limit, and basis.

Any unsupported numerical acceptance limit must say `ENGINEERING PROPOSAL - VALIDATE`. Update the
source ledger and open gates. Do not edit previous results.
