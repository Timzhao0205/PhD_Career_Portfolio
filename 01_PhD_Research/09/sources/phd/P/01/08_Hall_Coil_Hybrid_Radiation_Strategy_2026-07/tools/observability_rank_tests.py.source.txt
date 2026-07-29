"""Numerical structural-identifiability rank tests for the Hall + coil pair.

Stage 20 (observability), Hall+coil hybrid mission, 2026-07-27.

METHOD (finite-basis Fisher-information rank test)
--------------------------------------------------
The unknown field B(t) is restricted to a finite KNOWN basis with unknown
coefficients, e.g. B(t) = c0 + c1*f1(t) + c2*f2(t). This is a BEST CASE for
identifiability: restricting the unknown function to a low-dimensional known
basis can only add information. If the Fisher information matrix (FIM) is
rank-deficient even under this restriction, the infinite-dimensional problem
is a fortiori non-identifiable along the same directions.

Outputs are sampled on a uniform grid t in [0,1] (N samples). Measurement
noise is unit white noise on every channel, so FIM = J^T J with J the
Jacobian of the stacked outputs w.r.t. the unknown parameter vector,
evaluated at the nominal parameter values below. Jacobians are computed by
complex-step differentiation (machine precision; no finite-difference
truncation error). Rank is the number of singular values of J above
RTOL * s_max. Near-null right-singular vectors are matched against the
analytically predicted invariance directions by projection residual.

An "identifiable function" check projects the gradient of a scalar parameter
function phi(p) onto the numerical null space: if the projection is ~0, phi
is locally identifiable even though individual parameters are not.

This is a numerical demonstration on synthetic, stated assumptions ONLY.
It is NOT experimental validation and must never be cited as such.

Reproducibility: deterministic (no random numbers). numpy >= 1.20.
Run:  python tools/observability_rank_tests.py
"""

import numpy as np

N = 1500
T = np.linspace(0.0, 1.0, N)
DT = T[1] - T[0]
RTOL = 1e-9          # rank threshold relative to largest singular value
HSTEP = 1e-20        # complex-step size

# Nominal parameter values (arbitrary but generic; units normalized).
NOM = dict(c0=1.0, c1=0.3, c2=0.2, c3=0.15,
           S=1.2, bH=0.05, K=0.8, bC=0.02,
           S2=0.9, b2=-0.03,
           bH0=0.05, bH1=0.02, bC0=0.02, bC1=0.01,
           x0=0.1, g=0.8, m=0.05, tauL=2.0,
           a=2*np.pi*4.0, kT=0.01, kD=0.03)


def jac(model, p0):
    """Complex-step Jacobian of stacked model outputs w.r.t. parameters."""
    p0 = np.asarray(p0, dtype=complex)
    y0 = model(p0)
    J = np.empty((y0.size, p0.size))
    for k in range(p0.size):
        p = p0.copy()
        p[k] += 1j * HSTEP
        J[:, k] = np.imag(model(p)) / HSTEP
    return J


def analyze(name, model, p0, pnames, analytic_nulls=None, funcs=None,
            note=""):
    J = jac(model, p0)
    U, s, Vt = np.linalg.svd(J, full_matrices=False)
    smax = s[0]
    rank = int(np.sum(s > RTOL * smax))
    ndef = len(p0) - rank
    print(f"\n=== {name} ===")
    if note:
        print(f"    {note}")
    print(f"    params ({len(p0)}): {pnames}")
    print(f"    singular values: " +
          " ".join(f"{v:.3e}" for v in s))
    print(f"    rank = {rank} / {len(p0)}   null-space dim = {ndef}")
    Vnull = Vt[rank:, :]          # rows span the numerical null space
    if analytic_nulls:
        for label, v in analytic_nulls:
            v = np.asarray(v, dtype=float)
            v = v / np.linalg.norm(v)
            if Vnull.size:
                proj = Vnull.T @ (Vnull @ v)
                resid = np.linalg.norm(v - proj)
            else:
                resid = 1.0
            ok = "MATCHED" if resid < 1e-6 else "NOT in null space"
            print(f"    analytic direction [{label}]: residual "
                  f"{resid:.2e} -> {ok}")
    if funcs:
        for label, gradv in funcs:
            gradv = np.asarray(gradv, dtype=float)
            gradv = gradv / np.linalg.norm(gradv)
            if Vnull.size:
                comp = np.linalg.norm(Vnull @ gradv)
            else:
                comp = 0.0
            verdict = "IDENTIFIABLE" if comp < 1e-6 else "NOT identifiable"
            print(f"    function [{label}]: null-space component "
                  f"{comp:.2e} -> {verdict}")
    return rank, ndef, s


# ---------------------------------------------------------------- bases ----
F1 = np.sin(2*np.pi*3*T)          # generic AC content
F2 = np.cos(2*np.pi*7*T)          # second, independent AC component
dF1 = 2*np.pi*3*np.cos(2*np.pi*3*T)
dF2 = -2*np.pi*7*np.sin(2*np.pi*7*T)

# slow/LF basis for the drift-confusion case
S5 = np.sin(2*np.pi*5*T)
dS5 = 2*np.pi*5*np.cos(2*np.pi*5*T)


def leaky_lpf(u, a):
    """First-order low-pass  x' = a (u - x), x(0)=u(0), explicit Euler.

    Complex-step safe (linear recursion)."""
    x = np.empty(len(u), dtype=complex)
    x[0] = u[0]
    for k in range(len(u) - 1):
        x[k+1] = x[k] + DT * a * (u[k] - x[k])
    return x


def leaky_integrator(dB, x0, g, m, tauL):
    """x' = -x/tauL + g*dB + m, x(0)=x0, explicit Euler (complex-safe)."""
    x = np.empty(len(dB), dtype=complex)
    x[0] = x0
    for k in range(len(dB) - 1):
        x[k+1] = x[k] + DT * (-x[k]/tauL + g*dB[k] + m)
    return x


results = {}

# --- CASE A (stage case 3): everything unknown -----------------------------
def model_A(p):
    c0, c1, c2, S, bH, K, bC = p
    B = c0 + c1*F1 + c2*F2
    dB = c1*dF1 + c2*dF2
    return np.concatenate([S*B + bH, K*dB + bC])

nom = [NOM['c0'], NOM['c1'], NOM['c2'], NOM['S'], NOM['bH'],
       NOM['K'], NOM['bC']]
results['A'] = analyze(
    "CASE A | stage case 3: B, S_H, b_H, K_C, b_C all unknown",
    model_A, nom, "c0,c1,c2,S,bH,K,bC",
    analytic_nulls=[
        ("scale: (B,S,K)->(aB,S/a,K/a)",
         [NOM['c0'], NOM['c1'], NOM['c2'], -NOM['S'], 0.0, -NOM['K'], 0.0]),
        ("DC shift: (B,bH)->(B+e, bH-S*e)",
         [1.0, 0.0, 0.0, 0.0, -NOM['S'], 0.0, 0.0]),
    ],
    funcs=[
        ("S_H alone", [0, 0, 0, 1, 0, 0, 0]),
        ("ratio S_H/K_C  (grad at nominal)",
         [0, 0, 0, 1/NOM['K'], 0, -NOM['S']/NOM['K']**2, 0]),
    ],
    note="Expected: rank 5/7; two-dimensional null space (scale + DC).")

# --- CASE B (stage case 2): coil chain known -------------------------------
def model_B(p):
    c0, c1, c2, S, bH = p
    B = c0 + c1*F1 + c2*F2
    dB = c1*dF1 + c2*dF2
    return np.concatenate([S*B + bH, NOM['K']*dB + NOM['bC']])

results['B'] = analyze(
    "CASE B | stage case 2: K_C, b_C known; B, S_H, b_H unknown",
    model_B, [NOM['c0'], NOM['c1'], NOM['c2'], NOM['S'], NOM['bH']],
    "c0,c1,c2,S,bH",
    analytic_nulls=[("DC shift only",
                     [1.0, 0.0, 0.0, 0.0, -NOM['S']])],
    funcs=[("S_H alone", [0, 0, 0, 1, 0])],
    note="Expected: rank 4/5. S_H becomes identifiable (coil pins the AC "
         "field); only the DC/offset direction survives.")

# --- CASE C1 (stage case 1, no anchors): known gains, drifting offsets -----
def model_C(p, anchors):
    c0, c1, c2, c3, bH0, bH1, bC0, bC1 = p
    B = c0 + c1*T + c2*S5 + c3*T**2
    dB = c1 + c2*dS5 + 2*c3*T
    yH = NOM['S']*B + bH0 + bH1*T
    yC = NOM['K']*dB + bC0 + bC1*T
    out = [yH, yC]
    if anchors:
        # pre/post-shot zero-field, zero-dB/dt epochs: Hall reads bH0 (t=0)
        # and bH0+bH1 (t=1); coil reads bC0 and bC0+bC1. 50 samples each.
        z = np.ones(50, dtype=complex)
        out += [bH0*z, (bH0 + bH1)*z, bC0*z, (bC0 + bC1)*z]
    return np.concatenate(out)

pC = [NOM['c0'], NOM['c1'], NOM['c2'], NOM['c3'],
      NOM['bH0'], NOM['bH1'], NOM['bC0'], NOM['bC1']]
results['C1'] = analyze(
    "CASE C1 | stage case 1, in-shot only: S_H,K_C known; offsets drift; "
    "field has DC+ramp+quadratic+AC",
    lambda p: model_C(p, anchors=False), pC,
    "c0,c1,c2,c3,bH0,bH1,bC0,bC1",
    analytic_nulls=[
        ("field DC vs Hall offset: (c0,bH0)",
         [1.0, 0, 0, 0, -NOM['S'], 0, 0, 0]),
        ("field ramp vs offsets: (c1,bH1,bC0)",
         [0, 1.0, 0, 0, 0, -NOM['S'], -NOM['K'], 0]),
    ],
    funcs=[("bC1 (coil linear drift)", [0, 0, 0, 0, 0, 0, 0, 1]),
           ("c3 (quadratic field)", [0, 0, 0, 1, 0, 0, 0, 0])],
    note="Expected: rank 6/8. LF field confounds with both channels' "
         "offsets; but c3 (via Hall t^2) and then bC1 are identifiable -> "
         "cross-channel disambiguation works for components with "
         "distinguishable time signatures.")

# --- CASE C2 (stage case 1 with zero-field anchors) ------------------------
results['C2'] = analyze(
    "CASE C2 | stage case 1 + pre/post-shot zero-field & zero-dB/dt anchor "
    "epochs",
    lambda p: model_C(p, anchors=True), pC,
    "c0,c1,c2,c3,bH0,bH1,bC0,bC1",
    note="Expected: full rank 8/8. Known-field (B=0) epochs pin both "
         "offset polynomials; everything else follows.")

# --- CASE D (stage case 4): trusted field model ----------------------------
Bref = NOM['c0'] + NOM['c1']*F1 + NOM['c2']*F2      # known reference field
dBref = NOM['c1']*dF1 + NOM['c2']*dF2

def model_D(p):
    S, bH, K, bC = p
    return np.concatenate([S*Bref + bH, K*dBref + bC])

results['D'] = analyze(
    "CASE D | stage case 4: B(t) known from machine current + field model",
    model_D, [NOM['S'], NOM['bH'], NOM['K'], NOM['bC']], "S,bH,K,bC",
    note="Expected: full rank 4/4 with a waveform having >=2 field levels "
         "and nonzero dB/dt.")

def model_Dflat(p):
    S, bH, K, bC = p
    Bf = NOM['c0'] * np.ones(N)
    return np.concatenate([S*Bf + bH, K*0*Bf + bC])

results['Dflat'] = analyze(
    "CASE D-flat | stage case 4 degenerate: known but CONSTANT field",
    model_Dflat, [NOM['S'], NOM['bH'], NOM['K'], NOM['bC']], "S,bH,K,bC",
    note="Expected: rank 2/4 (only S*B0+bH and bC observable): a trusted "
         "reference still needs field variation to separate gain from "
         "offset.")

# --- CASE E (stage case 5): known injected calibration field ---------------
Binj = 0.1*np.sin(2*np.pi*11*T)          # known injected tone (AC)
dBinj = 0.1*2*np.pi*11*np.cos(2*np.pi*11*T)

def model_E(p):
    c0, c1, c2, S, bH, K, bC = p
    B = c0 + c1*F1 + c2*F2 + Binj
    dB = c1*dF1 + c2*dF2 + dBinj
    return np.concatenate([S*B + bH, K*dB + bC])

results['E'] = analyze(
    "CASE E | stage case 5: embedded calibration coil, known AC injection "
    "at 11 Hz (distinct from field content at 3 and 7 Hz)",
    model_E, nom, "c0,c1,c2,S,bH,K,bC",
    analytic_nulls=[("DC shift (survives AC injection)",
                     [1.0, 0.0, 0.0, 0.0, -NOM['S'], 0.0, 0.0])],
    funcs=[("S_H alone", [0, 0, 0, 1, 0, 0, 0]),
           ("K_C alone", [0, 0, 0, 0, 0, 1, 0])],
    note="Expected: rank 6/7. Known injection removes the scale null "
         "(both gains identifiable); the DC direction (b_H vs static "
         "field) survives AC-only injection.")

def model_Ecollide(p):
    c0, c1, c2, S, bH, K, bC = p
    B = c0 + c1*F1 + c2*F2 + 0.1*F1      # injection waveform == F1 content
    dB = c1*dF1 + c2*dF2 + 0.1*dF1
    return np.concatenate([S*B + bH, K*dB + bC])

results['Ecollide'] = analyze(
    "CASE E-collide | stage case 5 degenerate: injection waveform "
    "spectrally identical to unknown ambient field content",
    model_Ecollide, nom, "c0,c1,c2,S,bH,K,bC",
    note="Expected: rank 5/7 again. If the plasma/machine field can contain "
         "an unknown component with the same signature as the injection, "
         "the gain information is lost -> injection must be orthogonal "
         "(frequency, coding, or toggling) to ambient content.")

# --- CASE F (stage case 8): quasi-static field, no excitation --------------
def model_F(p):
    c0, S, bH, K, bC = p
    B = c0 * np.ones(N)
    return np.concatenate([S*B + bH, K*0*B + bC])

results['F'] = analyze(
    "CASE F | stage case 8: quasi-static field, all params unknown",
    model_F, [NOM['c0'], NOM['S'], NOM['bH'], NOM['K'], NOM['bC']],
    "c0,S,bH,K,bC",
    note="Expected: rank 2/5 (lumps S*c0+bH and bC only). No mutual "
         "calibration content at all; K_C entirely invisible.")

# --- CASE G (stage case 7): material-diverse second Hall channel -----------
def model_G(p):
    c0, c1, c2, S1, b1, S2, b2, K, bC = p
    B = c0 + c1*F1 + c2*F2
    dB = c1*dF1 + c2*dF2
    return np.concatenate([S1*B + b1, S2*B + b2, K*dB + bC])

pG = [NOM['c0'], NOM['c1'], NOM['c2'], NOM['S'], NOM['bH'],
      NOM['S2'], NOM['b2'], NOM['K'], NOM['bC']]
results['G'] = analyze(
    "CASE G | stage case 7: two Hall channels (diverse materials) + coil, "
    "all gains/offsets unknown",
    model_G, pG, "c0,c1,c2,S1,b1,S2,b2,K,bC",
    analytic_nulls=[
        ("scale: (B,S1,S2,K)->(aB,S1/a,S2/a,K/a)",
         [NOM['c0'], NOM['c1'], NOM['c2'], -NOM['S'], 0.0,
          -NOM['S2'], 0.0, -NOM['K'], 0.0]),
        ("DC shift: b1,b2 absorb",
         [1.0, 0, 0, 0, -NOM['S'], 0, -NOM['S2'], 0, 0]),
    ],
    funcs=[
        ("gain ratio S1/S2 (grad at nominal)",
         [0, 0, 0, 1/NOM['S2'], 0, -NOM['S']/NOM['S2']**2, 0, 0, 0]),
        ("S1 alone", [0, 0, 0, 1, 0, 0, 0, 0, 0]),
    ],
    note="Expected: rank 7/9; the SAME two null directions survive "
         "(redundancy does not fix absolute scale/DC), but the gain ratio "
         "S1/S2 is identifiable -> differential drift attribution.")

# --- CASE H (stage case 9): unknown Hall bandwidth -------------------------
def model_H(p, f1, df1, f2, df2):
    c0, c1, c2, S, bH, a = p
    B = c0 + c1*f1 + c2*f2
    dB = c1*df1 + c2*df2
    yH = S*leaky_lpf(B, a) + bH
    yC = NOM['K']*dB + NOM['bC']
    return np.concatenate([yH, yC])

F1fast = np.sin(2*np.pi*8*T)
dF1fast = 2*np.pi*8*np.cos(2*np.pi*8*T)
# genuinely narrowband variant: BOTH basis components far below the pole
F1slow = np.sin(2*np.pi*0.3*T)
dF1slow = 2*np.pi*0.3*np.cos(2*np.pi*0.3*T)
F2slow = np.cos(2*np.pi*0.5*T)
dF2slow = -2*np.pi*0.5*np.sin(2*np.pi*0.5*T)

pH = [NOM['c0'], NOM['c1'], NOM['c2'], NOM['S'], NOM['bH'], NOM['a']]
results['Hbroad'] = analyze(
    "CASE H-broad | stage case 9: unknown Hall pole a=2*pi*4, excitation "
    "at 8 Hz (above pole), coil chain known",
    lambda p: model_H(p, F1fast, dF1fast, F2, dF2), pH, "c0,c1,c2,S,bH,a",
    note="Expected: rank 5/6 with a WELL-conditioned 'a' direction (only "
         "the DC null survives): the coil characterizes Hall dynamics in "
         "the overlap band.")

results['Hnarrow'] = analyze(
    "CASE H-narrow | stage case 9 degenerate: same unknown pole, ALL "
    "excitation at 0.3 and 0.5 Hz (far below the 4 Hz pole)",
    lambda p: model_H(p, F1slow, dF1slow, F2slow, dF2slow), pH,
    "c0,c1,c2,S,bH,a",
    note="Expected: rank may stay 5/6 numerically but the singular value "
         "carrying 'a' collapses by orders of magnitude -> practically "
         "unidentifiable without near/above-pole excitation.")

# --- CASE I: integrated-coil implementation, Hall as reference -------------
Bwave = NOM['c0'] + NOM['c1']*F1 + NOM['c2']*F2   # known (Hall-calibrated)
dBwave = NOM['c1']*dF1 + NOM['c2']*dF2

def model_I(p):
    x0, g, m, tauL = p
    return leaky_integrator(dBwave, x0, g, m, tauL)

pI = [NOM['x0'], NOM['g'], NOM['m'], NOM['tauL']]
results['I'] = analyze(
    "CASE I | integrated coil vs calibrated Hall: unknown IC x0, gain g, "
    "drift rate m, leak tauL; rich known dB/dt",
    model_I, pI, "x0,g,m,tauL",
    note="Expected: full rank 4/4 -> a calibrated Hall channel identifies "
         "integrator IC, gain, drift, and leak, GIVEN dB/dt variation.")

def model_Iramp(p):
    x0, g, m, tauL = p
    dBr = 0.5*np.ones(N)                 # constant-slope ramp only
    return leaky_integrator(dBr, x0, g, m, tauL)

results['Iramp'] = analyze(
    "CASE I-ramp | integrated coil, constant dB/dt ramp only",
    model_Iramp, pI, "x0,g,m,tauL",
    analytic_nulls=[
        ("gain/drift trade: g*r+m invariant (r=0.5)",
         [0.0, 1.0, -0.5, 0.0]),
    ],
    note="Expected: rank 3/4. Under constant dB/dt, coil gain and "
         "integrator drift rate are structurally confounded (only g*r+m "
         "observable) -> distinguishing them REQUIRES dB/dt variation.")

# --- CASE J: temperature vs radiation drift attribution --------------------
def model_J(p, dT):
    kT, kD = p
    D = T.copy()                          # normalized dose ramp
    S = NOM['S']*(1 + kT*dT + kD*D)
    return S*Bref + NOM['bH']

dT_corr = T.copy()                        # temperature ramps with dose
dT_decorr = np.sin(2*np.pi*1.5*T)         # engineered thermal excursions

pJ = [NOM['kT'], NOM['kD']]
rJ1 = analyze(
    "CASE J-corr | S_H(T,D): temperature history proportional to dose "
    "history (both slow ramps), T measured",
    lambda p: model_J(p, dT_corr), pJ, "kT,kD",
    note="Expected: rank 1/2 -> exactly collinear columns; temperature and "
         "radiation coefficients unidentifiable when T and D co-evolve.")
rJ2 = analyze(
    "CASE J-decorr | same, but engineered thermal excursions decorrelate "
    "T(t) from D(t)",
    lambda p: model_J(p, dT_decorr), pJ, "kT,kD",
    note="Expected: full rank 2/2 -> measured, decorrelated temperature "
         "excursions make the two drift channels separable.")

print("\nAll cases executed. Interpret ranks with the analytic arguments in"
      "\noutputs/02_OBSERVABILITY_AND_IDENTIFIABILITY.md; this script is a"
      "\nnumerical demonstration, not experimental validation.")
