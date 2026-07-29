// concept_D.scad — CONCEPT D "TriPlate corner" (runner-up)
// -----------------------------------------------------------------------------
// Same carrier interface as Concept B (drop-in pocket + PEEK insert with 4
// gold BeCu springs + Ti clamp frame), but the pockets live in THREE IDENTICAL
// FLAT ZIRCONIA SEAT PLATES (13.4 sq x 3.2) bolted onto a featureless 12 mm
// zirconia core cube. Manufacturing rationale: small flat plates are the
// easiest possible zirconia parts (green-machine or even grind from standard
// plate stock; make 10, keep spares); the core cube has only through-holes.
// The +Z plate's two M2 bolts continue through the core cube AND the Ti base
// flange -> one bolt pair clamps plate + cube + base. +X/+Y plates bolt
// through to hex nuts recessed against the bare -X/-Y faces.
// Render: openscad -o concept_D_iso.png --imgsize=1400,1050 --projection=p \
//         --camera=0,0,0,55,0,25,0 --viewall --autocenter concept_D.scad
// -----------------------------------------------------------------------------

SECTION = 0;

ENV_D = 31.75; ENV_H = 27.5; show_envelope = true;
LCC = 8.89; LCC_T = 1.65; SEAL_OD = 7.98; CAV_OP = 6.10;

CORE   = 12.0;      // plain zirconia core cube
PLATE  = 13.4;      // zirconia seat plate square
PLATE_T= 3.2;
POCKET = 9.40; POCK_D = 2.15; PEEK_T = 1.0;
PROUD  = LCC_T - (POCK_D - PEEK_T);   // 0.50 mm
DEFLECT= 0.35;
FRAME  = 13.4; FRAME_T = 1.0; WIN = 7.0;
STAND_H= 6.5; BASE_T = 1.5; BASE_D = 18.0; EAR_Y = 12.5;
Z0 = STAND_H + BASE_T; ZC = Z0 + CORE/2;

SX = [[ 5.00,-5.00],[-5.00, 5.00]];
SY = [[ 5.20, 4.80],[-5.20,-4.80]];
SZ = [[ 4.90,-5.15],[-4.90, 5.15]];

r_corner = sqrt(pow(CORE/2+PLATE_T+FRAME_T+1.3,2)+pow(FRAME/2,2));
echo(str("corner radius, side plate+frame+head = ", r_corner, " mm (<= ", ENV_D/2, ")"));
echo(str("stack height = ", Z0+CORE+PLATE_T+FRAME_T+1.3, " mm (<= ", ENV_H, ")"));
echo(str("carrier proud of plate = ", PROUD, " mm; spring deflection = ", DEFLECT));

$fn = 48;
module envelope() { color([0.8,0.1,0.1,0.10]) cylinder(h=ENV_H, d=ENV_D); }

// ---- local coords: core face at z=CORE/2, +z outward ----
module seat_plate(scr) color([0.93,0.92,0.86]) translate([0,0,CORE/2])
  linear_extrude(PLATE_T) difference() {
    square(PLATE, center=true);
    square(POCKET, center=true);          // pocket is a through-window in the
    for (p=scr) translate(p) circle(d=2.2);   // plate; floor = PEEK on core face
    translate([0,-PLATE/2+1.2]) square([2.0,2.6], center=true);  // wire exit
  }

module peek_insert() color([0.82,0.71,0.55]) translate([0,0,CORE/2+PLATE_T-POCK_D]) {
  linear_extrude(PEEK_T) difference() {
    square(POCKET-0.1, center=true); square(3.0, center=true); }
  for (a=[0:90:270]) rotate([0,0,a]) translate([3.55,0,PEEK_T])
    color([1.0,0.84,0.2]) scale([1.4,2.2,1]) sphere(d=0.9);
}

module carrier() {
  zc = CORE/2+PLATE_T-POCK_D+PEEK_T+DEFLECT;
  color([1,0.95,0.72]) translate([0,0,zc]) difference() {
    linear_extrude(LCC_T) square(LCC, center=true);
    translate([0,0,LCC_T-0.75]) linear_extrude(1) square(CAV_OP, center=true);
    translate([0,0,LCC_T-1.15]) linear_extrude(1) square(4.06, center=true);
  }
  color([0.25,0.28,0.32]) translate([0,0,zc+0.6]) linear_extrude(0.35) square(2.5, center=true);
}

module ti_frame(scr, through=CORE+PLATE_T, nut_drop=0) {
  zf = CORE/2 + PLATE_T;
  color([0.62,0.65,0.68]) translate([0,0,zf]) linear_extrude(FRAME_T) difference() {
    square(FRAME, center=true); square(WIN, center=true);
    for (p=scr) translate(p) circle(d=2.2); }
  color([0.62,0.65,0.68]) translate([0,0,zf-PROUD+DEFLECT])
    linear_extrude(PROUD-DEFLECT+0.01) difference() {
      square(WIN+1.4, center=true); square(WIN, center=true); }
  for (p=scr) {
    color([0.55,0.58,0.62]) translate([p[0],p[1],zf+FRAME_T]) cylinder(h=1.3, d=3.6);
    color([0.55,0.58,0.62]) translate([p[0],p[1],-CORE/2-1.5-nut_drop]) cylinder(h=1.5, d=4.0, $fn=6);
  }
}

module face_pack(scr, nut_drop=0) { seat_plate(scr); peek_insert(); carrier(); ti_frame(scr, nut_drop=nut_drop); }

module on_px() { translate([0,0,ZC]) rotate([0, 90,0]) children(); }
module on_py() { translate([0,0,ZC]) rotate([-90,0,0]) children(); }
module on_pz() { translate([0,0,ZC]) children(); }

module core_cube() color([0.90,0.89,0.83]) difference() {
  translate([0,0,ZC]) cube(CORE, center=true);
  on_px() for (p=SX) translate([p[0],p[1],0]) cylinder(h=CORE+12, d=2.2, center=true);
  on_py() for (p=SY) translate([p[0],p[1],0]) cylinder(h=CORE+12, d=2.2, center=true);
  on_pz() for (p=SZ) translate([p[0],p[1],0]) cylinder(h=CORE+12, d=2.2, center=true);
  // vertical wire grooves on the bare faces
  translate([-CORE/2+0.74,0,ZC]) cube([1.5,2.0,CORE+0.1], center=true);
  translate([0,-CORE/2+0.74,ZC]) cube([2.0,1.5,CORE+0.1], center=true);
}

module ti_base() color([0.62,0.65,0.68]) difference() {
  union() {
    translate([0,0,STAND_H]) cylinder(h=BASE_T, d=BASE_D);
    for (s=[1,-1]) translate([0,0,STAND_H]) linear_extrude(BASE_T) hull() {
      translate([0,s*EAR_Y]) circle(d=5); translate([0,s*7]) circle(d=5); }
  }
  translate([0,0,STAND_H-1]) cylinder(h=BASE_T+2, d=5.0);          // harness hole
  for (s=[1,-1]) translate([0,s*EAR_Y,STAND_H-1]) cylinder(h=BASE_T+2, d=2.2);
  on_pz() for (p=SZ) translate([p[0],p[1],-CORE/2-BASE_T-6]) cylinder(h=12, d=2.2);
}

module standoffs() color([0.55,0.58,0.62]) for (s=[1,-1])
  translate([0,s*EAR_Y,0]) { cylinder(h=STAND_H, d=4.8, $fn=6);
    translate([0,0,STAND_H]) cylinder(h=BASE_T+1.0, d=2.0); }

module assembly() {
  standoffs(); ti_base(); core_cube();
  on_px() face_pack(SX);
  on_py() face_pack(SY);
  on_pz() face_pack(SZ, nut_drop=BASE_T);
}

difference() {
  union() { assembly(); if (show_envelope && SECTION==0) envelope(); }
  if (SECTION) translate([-50,-100,-10]) cube([100,100,60]);
}
