// concept_C.scad — CONCEPT C "COTS LCC-20 socket per face" (§F seed S3) — REJECTED
// -----------------------------------------------------------------------------
// Screening model: three commercial LCC-20 open-top burn-in/test sockets
// (generic Aries/Plastronics-class geometry: ~16.5 mm sq body, ~7 mm tall,
// requires a carrier PCB ~1.6 mm) mounted on the faces of a 14 mm cube.
// PURPOSE OF THIS MODEL: show the envelope violation quantitatively.
//   socket corner radius = cube/2 + PCB + socket height, out at the socket
//   body corners -> ~17.9 mm > 15.875 mm allowed  => DOES NOT FIT (3 faces).
// Independent kill criteria (see PACKAGING_3D_DESIGN.md §C-C):
//   - contacts are Au OVER NICKEL plated BeCu (ferromagnetic Ni) per Aries
//     materials spec -> disqualified next to a Hall plate
//   - socket plastics (glass-filled PPS/LCP) unrated for UHV outgassing
//   - rated -55..+150 C (burn-in), marginal for in-vessel bake
//   - needs a PCB (FR4/polyimide + ENIG = more Ni) to terminate to
// Render: openscad -o concept_C_iso.png --imgsize=1400,1050 --projection=p \
//         --camera=0,0,0,55,0,25,0 --viewall --autocenter concept_C.scad
// -----------------------------------------------------------------------------

SECTION = 0;

ENV_D = 31.75; ENV_H = 27.5; show_envelope = true;
LCC = 8.89; LCC_T = 1.65;

CUBE   = 14.0;      // even with a minimal cube...
SOCK   = 16.5;      // generic LCC-20 open-top socket body square [mm]
SOCK_H = 7.0;       // body height incl. latch lid (typ. class value)
PCB_T  = 1.6;       // socket must be soldered to a board
STAND_H= 5.0; BASE_T= 2.0; BASE_D = 18.0; EAR_Y = 12.5;
Z0 = STAND_H + BASE_T; ZC = Z0 + CUBE/2;

r_sock = sqrt(pow(CUBE/2+PCB_T+SOCK_H,2)+pow(SOCK/2,2));
echo(str("VIOLATION: side-socket corner radius = ", r_sock,
         " mm  > allowed ", ENV_D/2, " mm"));
echo(str("VIOLATION: socket body corner (radial faces) = ",
         sqrt(2)*SOCK/2 + 0, " mm half-diag on a ", CUBE, " cube"));
echo(str("stack height = ", Z0+CUBE+PCB_T+SOCK_H, " mm (limit ", ENV_H, ")"));

$fn = 48;
module envelope() { color([0.8,0.1,0.1,0.10]) cylinder(h=ENV_H, d=ENV_D); }

module socket_stack() {  // local: face at z=CUBE/2, +z out
  color([0.2,0.5,0.2]) translate([0,0,CUBE/2])                  // PCB
    linear_extrude(PCB_T) square(SOCK+1.5, center=true);
  color([0.15,0.15,0.18]) translate([0,0,CUBE/2+PCB_T]) {       // socket body
    linear_extrude(SOCK_H-2.2) square(SOCK, center=true);
    translate([0,0,SOCK_H-2.2]) linear_extrude(2.2) difference() {
      square(SOCK, center=true); square(SOCK-4, center=true); } // open-top lid
  }
  color([1,0.95,0.72]) translate([0,0,CUBE/2+PCB_T+2.0])        // LCC inside
    linear_extrude(LCC_T) square(LCC, center=true);
}

module on_px() { translate([0,0,ZC]) rotate([0, 90,0]) children(); }
module on_py() { translate([0,0,ZC]) rotate([-90,0,0]) children(); }
module on_pz() { translate([0,0,ZC]) children(); }

module body() color([0.93,0.92,0.86]) {
  translate([0,0,ZC]) cube(CUBE, center=true);
  translate([0,0,STAND_H]) cylinder(h=BASE_T, d=BASE_D);
  for (s=[1,-1]) translate([0,0,STAND_H]) linear_extrude(BASE_T) hull() {
    translate([0, s*EAR_Y]) circle(d=5); translate([0, s*7]) circle(d=5); }
}

module standoffs() color([0.55,0.58,0.62]) for (s=[1,-1])
  translate([0,s*EAR_Y,0]) cylinder(h=STAND_H, d=4.8, $fn=6);

module assembly() {
  standoffs(); body();
  on_px() socket_stack(); on_py() socket_stack(); on_pz() socket_stack();
}

difference() {
  union() { assembly(); if (show_envelope && SECTION==0) envelope(); }
  if (SECTION) translate([-50,-100,-10]) cube([100,100,60]);
}
