"""Stage 70 red-team: INDEPENDENT identifiability verification.

Deliberately different from tools/observability_rank_tests.py:
- central finite differences (not complex step);
- different field basis, sample count, and nominal parameter values;
- adds an exact output-equivalence test of the Theorem-1 gauge orbit
  (global, not just local rank);
- adds a NEW case the stage-20 suite did not run: zero-field anchor with
  UNKNOWN remanent field at the anchor epoch (attack on CASE C2 / RR-24).

Deterministic, no RNG. Model (direct readout, constant parameters):
    y_H(t) = S_H * B(t) + b_H
    y_C(t) = K_C * dB/dt(t) + b_C
"""
import numpy as np

N = 800
t = np.linspace(0.0, 2.0, N)
W1, W2 = 2 * np.pi * 3.0, 2 * np.pi * 11.0   # ambient tones
WINJ = 2 * np.pi * 23.0                       # injection tone (case E)

# nominals (different from stage-20 script's values)
TH0 = dict(c0=0.37, c1=0.81, c2=0.29, S=2.3, bH=0.13, K=1.7, bC=-0.21,
           Brem=0.05)

def field(c0, c1, c2, w2=W2):
    B = c0 + c1 * np.sin(W1 * t) + c2 * np.sin(w2 * t + 0.7)
    Bd = c1 * W1 * np.cos(W1 * t) + c2 * w2 * np.cos(w2 * t + 0.7)
    return B, Bd

def outputs_caseA(p, w2=W2, inject=False):
    B, Bd = field(p[0], p[1], p[2], w2)
    if inject:
        B = B + 0.15 * np.sin(WINJ * t)
        Bd = Bd + 0.15 * WINJ * np.cos(WINJ * t)
    yH = p[3] * B + p[4]
    yC = p[5] * Bd + p[6]
    return np.concatenate([yH, yC])

def outputs_anchor(p, brem_known=None):
    """Operating epoch + anchor epoch (machine field off).
    p = [c0,c1,c2,S,bH,K,bC,(Brem)] ; if brem_known given, Brem fixed."""
    op = outputs_caseA(p[:7])
    Brem = brem_known if brem_known is not None else p[7]
    yH_a = p[3] * Brem + p[4] * np.ones(50)
    yC_a = p[6] * np.ones(50)
    return np.concatenate([op, yH_a, yC_a])

def jac(f, p, scale=1e-6):
    p = np.asarray(p, float)
    cols = []
    for i in range(len(p)):
        h = scale * max(1.0, abs(p[i]))
        pp, pm = p.copy(), p.copy()
        pp[i] += h; pm[i] -= h
        cols.append((f(pp) - f(pm)) / (2 * h))
    return np.column_stack(cols)

def rank_and_null(J, tol=1e-8):
    U, s, Vt = np.linalg.svd(J, full_matrices=False)
    r = int(np.sum(s > tol * s[0]))
    return r, s, Vt[r:].T   # null-space basis (columns)

def proj_onto_null(v, Nmat):
    if Nmat.shape[1] == 0:
        return 0.0
    v = v / np.linalg.norm(v)
    return float(np.linalg.norm(Nmat @ (Nmat.T @ v)))

ok = True
def check(name, cond, detail=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name + ("  | " + detail if detail else ""))
    ok = ok and cond

print("=== 1. Theorem 1: exact global output equivalence on the gauge orbit ===")
c0, c1, c2, S, bH, K, bC = (TH0[k] for k in ("c0", "c1", "c2", "S", "bH", "K", "bC"))
alpha, beta = 1.73, -0.41
p_true = [c0, c1, c2, S, bH, K, bC]
p_gauge = [alpha * c0 + beta, alpha * c1, alpha * c2,
           S / alpha, bH - beta * S / alpha, K / alpha, bC]
d = np.max(np.abs(outputs_caseA(p_true) - outputs_caseA(p_gauge)))
check("gauge-transformed config gives IDENTICAL outputs", d < 1e-12,
      f"max|dy| = {d:.2e} (alpha={alpha}, beta={beta})")

print("\n=== 2. CASE A analog: all 7 unknown, independent FD Jacobian ===")
J = jac(outputs_caseA, p_true)
r, s, Nn = rank_and_null(J)
check("rank deficiency exactly 2 (rank 5/7)", r == 5,
      f"rank={r}, sv={['%.1e' % x for x in s]}")
null_alpha = np.array([c0, c1, c2, -S, 0.0, -K, 0.0])
null_beta = np.array([1.0, 0, 0, 0, -S, 0, 0])
pa = proj_onto_null(null_alpha, Nn)
pb = proj_onto_null(null_beta, Nn)
check("analytic alpha-null lies in numerical null space", pa > 0.999999, f"proj={pa:.8f}")
check("analytic beta-null lies in numerical null space", pb > 0.999999, f"proj={pb:.8f}")
g_ratio = np.array([0, 0, 0, 1 / K, 0, -S / K**2, 0])   # grad of S/K
g_S = np.array([0, 0, 0, 1.0, 0, 0, 0])                 # grad of S alone
check("gain ratio S_H/K_C is identifiable (grad orthogonal to null)",
      proj_onto_null(g_ratio, Nn) < 1e-6, f"proj={proj_onto_null(g_ratio, Nn):.2e}")
check("S_H alone is NOT identifiable (grad has null component)",
      proj_onto_null(g_S, Nn) > 0.5, f"proj={proj_onto_null(g_S, Nn):.3f}")

print("\n=== 3. CASE E analog: known spectrally-disjoint injection ===")
J = jac(lambda p: outputs_caseA(p, inject=True), p_true)
r, s, Nn = rank_and_null(J)
check("rank 6/7 with injection (only DC null left)", r == 6, f"rank={r}")
check("surviving null is the DC/offset direction", proj_onto_null(null_beta, Nn) > 0.999999,
      f"proj={proj_onto_null(null_beta, Nn):.8f}")
check("S_H becomes identifiable under injection", proj_onto_null(g_S, Nn) < 1e-6,
      f"proj={proj_onto_null(g_S, Nn):.2e}")

print("\n=== 4. CASE E-collide analog: ambient tone at the injection frequency ===")
# Phase subtlety found during this red team: a single fixed-phase ambient
# tone at f_inj is NOT phase-coherent with the injection, so no exact null
# appears (rank stays 6). The honest collision model gives the unknown
# ambient a full 2-parameter (sin+cos) component at f_inj:
def outputs_collide(p):
    """p = [c0,c1,c2s,c2c,S,bH,K,bC]; ambient has sin+cos at WINJ."""
    B = p[0] + p[1] * np.sin(W1 * t) + p[2] * np.sin(WINJ * t) + p[3] * np.cos(WINJ * t)
    Bd = (p[1] * W1 * np.cos(W1 * t) + p[2] * WINJ * np.cos(WINJ * t)
          - p[3] * WINJ * np.sin(WINJ * t))
    Binj = 0.15 * np.sin(WINJ * t)
    Bdinj = 0.15 * WINJ * np.cos(WINJ * t)
    yH = p[4] * (B + Binj) + p[5]
    yC = p[6] * (Bd + Bdinj) + p[7]
    return np.concatenate([yH, yC])

p8c = [TH0["c0"], TH0["c1"], 0.2, 0.11, S, bH, K, bC]
J = jac(lambda p: outputs_caseA(p, w2=WINJ, inject=True), p_true)
r_fixedphase, _, _ = rank_and_null(J)
check("fixed-phase collide tone alone does NOT create the null (phase-coherence subtlety)",
      r_fixedphase == 6, f"rank={r_fixedphase} (deficiency 1: DC only)")
J = jac(outputs_collide, p8c)
r, s, Nn = rank_and_null(J)
check("2-parameter (sin+cos) unknown ambient at f_inj restores deficiency 2 (rank 6/8)",
      r == 6, f"rank={r}")

print("\n=== 5. NEW ATTACK - CASE C2 with unknown remanent field at the 'zero-field' anchor ===")
p8 = p_true + [TH0["Brem"]]
J = jac(outputs_anchor, p8)
r, s, Nn = rank_and_null(J)
check("unknown remanent field: rank 6/8 - BOTH nulls survive, anchor buys nothing structural",
      r == 6, f"rank={r}")
null_beta8 = np.array([1.0, 0, 0, 0, -S, 0, 0, 1.0])       # c0 & Brem shift vs b_H
null_alpha8 = np.array([c0, c1, c2, -S, 0, -K, 0, TH0["Brem"]])
check("beta-null extends through B_rem (b_H trades against remanent field)",
      proj_onto_null(null_beta8, Nn) > 0.999999, f"proj={proj_onto_null(null_beta8, Nn):.8f}")
check("alpha-null extends through B_rem",
      proj_onto_null(null_alpha8, Nn) > 0.999999, f"proj={proj_onto_null(null_alpha8, Nn):.8f}")

# With the anchor field KNOWN but at a single value, and BOTH gains also
# unknown (case-3-like), the single anchor level breaks only one of the two
# nulls -- the independent rediscovery of stage-20's D-flat condition
# ("a trusted reference still needs field variation"):
J = jac(lambda p: outputs_anchor(p, brem_known=TH0["Brem"]), p_true)
r, s, Nn = rank_and_null(J)
check("KNOWN single-level anchor + unknown gains: rank 6/7 (one null survives; D-flat condition)",
      r == 6, f"rank={r}")

def outputs_anchor2(p):
    """Two anchor epochs at two KNOWN field values (0 and Brem)."""
    op = outputs_caseA(p[:7])
    a1H = p[3] * 0.0 + p[4] * np.ones(50)
    a2H = p[3] * TH0["Brem"] + p[4] * np.ones(50)
    aC = p[6] * np.ones(100)
    return np.concatenate([op, a1H, a2H, aC])

J = jac(outputs_anchor2, p_true)
r, s, Nn = rank_and_null(J)
check("TWO known anchor field levels: full rank 7/7 (matches CASE D >=2-level requirement)",
      r == 7, f"rank={r}")

print("\n=== VERDICT ===")
print("ALL CHECKS PASS" if ok else "AT LEAST ONE CHECK FAILED - see above")
