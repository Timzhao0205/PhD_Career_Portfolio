// concept_A.scad — CONCEPT A "Refined slotted cube + flying leads" (baseline, §F seed S4)
// -----------------------------------------------------------------------------
// The user's slotted-cube idea made buildable:
//   - 15 mm zirconia cube; per face an OPEN-FRONT vertical slot (not an enclosed
//     internal cavity like his CAD): carrier slides DOWN from the top edge,
//     riding on two edge rails that touch ONLY the outer 0.4 mm rim of the
//     carrier back face -- die/bond wires face OUT through a 7.0 mm window
//   - BeCu bow spring at the slot back preloads the carrier against the rails
//   - Ti keeper strip across the top of each slot (1 screw) stops back-out
//   - ELECTRICAL: no contacts in the mount -- four 34 AWG Kapton-insulated
//     flying leads are pre-attached (vacuum-grade solder or parallel-gap weld)
//     to castellations 1/6/11/16 of each carrier BEFORE insertion and exit
//     through the top slot mouth. Carrier is mechanically reusable; the lead
//     attachment is semi-permanent -> fails the strict reusability gate.
// Render: openscad -o concept_A_iso.png --imgsize=1400,1050 --projection=p \
//         --camera=0,0,0,55,0,25,0 --viewall --autocenter concept_A.scad
// -----------------------------------------------------------------------------

SECTION = 0;

ENV_D = 31.75; ENV_H = 27.5; show_envelope = true;
LCC = 8.89; LCC_T = 1.65; CAV_OP = 6.10;

CUBE   = 15.0;
SLOT_W = 9.30;      // slot width across carrier (LCC max 9.14 + clearance)
SLOT_T = 2.60;      // slot depth into face: carrier 1.65 + bow spring 0.95
WIN    = 7.0;       // front window (die + bond wires look out through this)
RAIL   = 0.9;       // rail overlap on the carrier front rim (outside seal ring)
STAND_H= 6.5; BASE_T= 2.0; BASE_D = 18.0; EAR_Y = 12.5;
Z0 = STAND_H + BASE_T; ZC = Z0 + CUBE/2;

echo(str("cube corner radius = ", CUBE*sqrt(2)/2, " mm (<= ", ENV_D/2, ")"));
echo(str("stack height = ", Z0 + CUBE + 1.5, " mm (<= ", ENV_H, ")"));

$fn = 48;
module envelope() { color([0.8,0.1,0.1,0.10]) cylinder(h=ENV_H, d=ENV_D); }

// local coords: face at z=CUBE/2, +z out; slot opens toward +y (local "up")
module slot_cuts() {
  // slot body: from just behind the window rails to depth SLOT_T
  translate([0,1,CUBE/2-SLOT_T/2-RAIL/2+0.01])
    cube([SLOT_W, CUBE/2+SLOT_W/2-2, SLOT_T+0.02], center=true);
  // front window (rails remain each side, width (SLOT_W-WIN)/2)
  translate([0,0,CUBE/2-RAIL/2+0.01]) cube([WIN, WIN, RAIL+0.04], center=true);
  // slot mouth at the top edge (insertion + lead exit)
  translate([0,CUBE/2-1.5,CUBE/2-SLOT_T/2-RAIL/2])
    cube([SLOT_W, 3.2, SLOT_T+0.02], center=true);
  // keeper screw hole
  translate([0,CUBE/2-2.2,CUBE/2-RAIL-SLOT_T]) cylinder(h=6, d=1.8);
}

module carrier_in_slot() {
  // carrier sits behind the rails, cavity facing OUT (local +z)
  translate([0,0,CUBE/2-RAIL-LCC_T]) {
    color([1,0.95,0.72]) difference() {
      linear_extrude(LCC_T) square(LCC, center=true);
      translate([0,0,LCC_T-0.75]) linear_extrude(1) square(CAV_OP, center=true);
      translate([0,0,LCC_T-1.15]) linear_extrude(1) square(4.06, center=true);
    }
    color([0.25,0.28,0.32]) translate([0,0,0.6]) linear_extrude(0.35) square(2.5, center=true);
  }
  // bow spring behind the carrier
  color([1.0,0.84,0.2]) translate([0,0,CUBE/2-RAIL-LCC_T-0.5])
    linear_extrude(0.4) square([2.5, LCC-1], center=true);
  // 4 flying leads out the slot mouth (schematic)
  color([0.85,0.55,0.25]) for (i=[-1.5:1:1.5])
    translate([i*1.2, LCC/2+0.2, CUBE/2-RAIL-LCC_T+0.6])
      rotate([-90,0,0]) cylinder(h=CUBE/2-LCC/2+2, d=0.4);
  // Ti keeper strip
  color([0.62,0.65,0.68]) translate([0,CUBE/2-2.2,CUBE/2-0.01])
    linear_extrude(0.8) difference() { square([SLOT_W+2,2.6], center=true); circle(d=1.8); }
  color([0.55,0.58,0.62]) translate([0,CUBE/2-2.2,CUBE/2+0.79]) cylinder(h=1.0, d=3.0);
}

module on_px() { translate([0,0,ZC]) rotate([0, 90,0]) rotate([0,0,90]) children(); }
module on_py() { translate([0,0,ZC]) rotate([-90,0,0]) rotate([0,0,180]) children(); }
module on_pz() { translate([0,0,ZC]) children(); }

module zirconia_body() color([0.93,0.92,0.86]) difference() {
  union() {
    translate([0,0,ZC]) cube(CUBE, center=true);
    translate([0,0,STAND_H]) cylinder(h=BASE_T, d=BASE_D);
    for (s=[1,-1]) translate([0,0,STAND_H]) linear_extrude(BASE_T) hull() {
      translate([0, s*EAR_Y]) circle(d=5); translate([0, s*7]) circle(d=5); }
  }
  on_px() slot_cuts();
  on_py() slot_cuts();
  on_pz() slot_cuts();
  for (s=[1,-1]) translate([0,s*EAR_Y,STAND_H-1]) cylinder(h=BASE_T+2, d=2.2);
}

module standoffs() color([0.55,0.58,0.62]) for (s=[1,-1])
  translate([0,s*EAR_Y,0]) { cylinder(h=STAND_H, d=4.8, $fn=6);
    translate([0,0,STAND_H]) cylinder(h=BASE_T+1.0, d=2.0); }

module assembly() {
  standoffs(); zirconia_body();
  on_px() carrier_in_slot();
  on_py() carrier_in_slot();
  on_pz() carrier_in_slot();
}

difference() {
  union() { assembly(); if (show_envelope && SECTION==0) envelope(); }
  if (SECTION) translate([-50,-100,-10]) cube([100,100,60]);
}
