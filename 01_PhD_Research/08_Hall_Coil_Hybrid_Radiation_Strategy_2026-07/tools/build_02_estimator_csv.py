"""Build outputs/02_ESTIMATOR_REQUIREMENTS.csv for stage 20 (one-off; kept
because it documents the exact row content programmatically and re-runs
deterministically)."""
import csv, io, os

HDR = ("case_id,objective,states,unknown_parameters,known_inputs,excitation,"
       "reference,observable_quantities,unobservable_quantities,"
       "estimator_candidate,uncertainty_method,fault_test,evidence_ids,"
       "verdict,notes").split(",")

R = []

R.append(dict(
    case_id="CASE1",
    objective="Track Hall offset drift and integrator drift with both gains pre-calibrated and stable",
    states="B(t); x_I; b_H(t); b_C(t) or m(t)",
    unknown_parameters="b_H0;b_H1;b_C0;b_C1 (or x_I(0);m;tau_L); field coefficients",
    known_inputs="S_H;K_C (pre-calibrated); shot timing",
    excitation="natural field waveform incl. dB/dt variation (ramp+flat-top)",
    reference="pre/post-shot zero-field and zero-dB/dt epochs (ambient/remanent field controlled or known)",
    observable_quantities="b_H;b_C;x_I(0);m;tau_L;B(t) fully (with anchors); quadratic+ field components and b_C1 even without anchors",
    unobservable_quantities="without anchors: LF trio {field DC/ramp, Hall offset drift, coil offset} (rank deficiency 2)",
    estimator_candidate="augmented-state Kalman filter with random-walk bias states (Friedland form); RTS smoother offline",
    uncertainty_method="filter/smoother covariance; innovation whiteness check",
    fault_test="innovation chi-square on each channel; between-shot offset jump test",
    evidence_ids="H004;H005;H015;P003;H025;H026;H027",
    verdict="conditionally_identifiable",
    notes="Fully identifiable ONLY with zero-field anchors; rank test C1 (6/8) vs C2 (8/8). Hardware-proven direction per claim C02. Gain-vs-drift separation needs dB/dt variation (CASE I-ramp counterexample)."))

R.append(dict(
    case_id="CASE2",
    objective="In-situ Hall gain (and offset) estimation with trusted coil chain",
    states="B(t); S_H(t); b_H(t)",
    unknown_parameters="S_H; b_H; B(0); field coefficients",
    known_inputs="K_C;b_C (trusted coil chain)",
    excitation="field excursion dB with SNR: var(S_H_hat) ~ sigma_H^2/sum((dB-mean)^2); S_H,b_H quasi-constant over window",
    reference="coil-derived field increment dB(t); plus B(0) anchor (zero-field start) if offset needed",
    observable_quantities="S_H; lumped intercept S_H*B(0)+b_H; B(t) up to B(0)",
    unobservable_quantities="b_H separately from B(0); absolute B",
    estimator_candidate="recursive least squares / EKF regression of y_H on coil-integrated dB(t)",
    uncertainty_method="Fisher/CRLB from regressor energy; window-length vs coil random-walk error tradeoff",
    fault_test="regression residual runs test; gain-estimate jump detection",
    evidence_ids="H059;H018;H019;H021",
    verdict="conditionally_identifiable",
    notes="THE reverse direction the mission asks about. Rank test B (4/5; S_H identifiable, DC null). Precedent H059 is non-fusion, driven-ramp, abstract-level (claim C11); no fusion/radiation demonstration exists (claim C06)."))

R.append(dict(
    case_id="CASE3",
    objective="Joint estimation with S_H,b_H,K_C,b_C all drifting (unreferenced pair)",
    states="B(t); S_H; b_H; K_C; b_C",
    unknown_parameters="all five",
    known_inputs="none",
    excitation="any (no excitation breaks the gauge group - Theorem 1)",
    reference="none",
    observable_quantities="gain ratio S_H/K_C and its drift; b_C (if dB/dt has no unknown drift-band component); field shape up to affine orbit",
    unobservable_quantities="absolute B; S_H; K_C; b_H; common-mode gain drift (2-dim null space for ALL waveforms)",
    estimator_candidate="none valid for absolute quantities; ratio tracker (cross-channel AC regression) for differential drift alarm",
    uncertainty_method="ratio-estimate CRLB in AC band",
    fault_test="rho-jump alarm detects differential drift WITHOUT attribution",
    evidence_ids="H021;H012;H015;H016;H017;H001;H002",
    verdict="not_identifiable",
    notes="Required counterexample. Rank test A (5/7, both null directions matched analytically). An EKF 'converging' here returns its prior, not information. Consistent with literature absence (claim C03)."))

R.append(dict(
    case_id="CASE4",
    objective="Absolute calibration of all four channel parameters from machine current + field model",
    states="S_H; b_H; K_C; b_C (field known)",
    unknown_parameters="S_H;b_H;K_C;b_C (+ misalignment as gain bias)",
    known_inputs="machine coil currents I(t); validated vacuum field model G(r)",
    excitation=">=2 field levels AND nonzero-dB/dt segments (constant field degenerates to rank 2)",
    reference="B_ref=G(r)I(t); vacuum shots only (plasma invalidates model)",
    observable_quantities="all four parameters; S_H only as S_H*cos(theta_m) with single-axis reference",
    unobservable_quantities="misalignment separately from gain; parameters during plasma (model invalid)",
    estimator_candidate="per-channel linear least squares on [B_ref,1] and [dB_ref/dt,1]",
    uncertainty_method="propagate reference budget: current measurement, model error, position via field gradient, timing skew",
    fault_test="cross-shot calibration repeatability; residual vs model",
    evidence_ids="H040;P003;H004;P013;H046",
    verdict="identifiable",
    notes="The workhorse absolute anchor (HSX context: vacuum shots with logged coil currents). Rank test D (4/4) and D-flat counterexample (2/4). H040 calibrates inductive sensors from known currents; no Hall-channel precedent (claim C08/C32)."))

R.append(dict(
    case_id="CASE5",
    objective="Gain calibration via embedded calibration coil with characterized transfer function",
    states="B(t); S_H; b_H; K_C; b_C",
    unknown_parameters="S_H;K_C;b_H;field coefficients",
    known_inputs="I_cal(t) measured; G_cal characterized",
    excitation="injected AC tone/coded waveform spectrally orthogonal to ambient content (or toggled); DC-capable toggling extends gain cal to DC operating point",
    reference="B_inj=G_cal*I_cal; reference-chain stability budget",
    observable_quantities="S_H*G_cal and K_C (both gains, given orthogonality); Hall dynamics if injected near/above pole",
    unobservable_quantities="b_H (AC injection blind to offset); S_H separately from G_cal drift (common-mode); gains if injection spectrally collides with ambient content",
    estimator_candidate="lock-in/synchronous demodulation at injection frequency; toggled-difference estimator",
    uncertainty_method="lock-in SNR; reference-chain stability budget (I_cal source, G_cal geometry, insulation leakage)",
    fault_test="scheduled self-test toggle; loss-of-injection detection; cal-vs-ambient consistency",
    evidence_ids="H003;H007;H038;H039;R056",
    verdict="conditionally_identifiable",
    notes="Rank tests E (6/7; both gains identifiable) and E-collide (5/7 counterexample). JET RHP 11.5-yr record is the operational precedent but same-die common-mode blind (claim C05). RIEMF risk to cal circuit under radiation is inferred from R056 mechanism (claim C19)."))

R.append(dict(
    case_id="CASE6",
    objective="Drift tracking via repeated reference waveform/shot",
    states="S_H^k;b_H^k;K_C^k;b_C^k across shots k",
    unknown_parameters="per-shot gain ratios and offset lumps",
    known_inputs="waveform identity across shots; machine current logs to verify reproducibility",
    excitation="the repeated waveform itself (>=2 field levels within it)",
    reference="shot-0 (or pre-irradiation) calibrated epoch",
    observable_quantities="S_H^k/S_H^0; K_C^k/K_C^0; offset-drift lumps",
    unobservable_quantities="absolute values (inherited from shot-0 cal); offset decomposition; drift within a shot",
    estimator_candidate="shot-to-shot regression y^k vs y^0 (slope=gain ratio); trend filter across shots",
    uncertainty_method="reproducibility floor from current logs sets minimum detectable drift; regression CI",
    fault_test="slope/intercept jump between adjacent shots",
    evidence_ids="H003;H040",
    verdict="conditionally_identifiable",
    notes="PROPOSED practice (derived algebra; no fusion source demonstrates repeated-shot Hall recal - claims C03/C06). Ideal form for radiation trend monitoring S_H(dose)/S_H(0). Requires waveform reproducibility << drift signal."))

R.append(dict(
    case_id="CASE7",
    objective="Drift attribution via material-diverse redundant Hall + temperature/dose proxies",
    states="B(t); S_1;b_1 (GaN); S_2;b_2 (diverse material); K_C;b_C; kT;kD drift coefficients",
    unknown_parameters="all gains/offsets; kT;kD",
    known_inputs="measured T(t); dose proxy D(t) from species-matched dosimetry; pre-characterized temperature coefficients",
    excitation="shared AC field content; engineered thermal excursions decorrelated from dose accumulation",
    reference="radiation-null reference channel (metallic Hall per R071) as differential anchor; dosimetry",
    observable_quantities="gain ratio S_1/S_2 and its drift; differential radiation term f_1(D)-f_2(D); kT vs kD separately IF T,D histories decorrelated",
    unobservable_quantities="absolute scale (scale null survives redundancy); common-mode drift of all channels; kT vs kD when T proportional to D (rank 1/2)",
    estimator_candidate="joint EKF with per-channel drift states + hypothesis-test bank (GLR) for attribution voting",
    uncertainty_method="FIM conditioning vs T-D decorrelation; Monte Carlo over coefficient priors",
    fault_test="three-channel majority voting; per-channel residual GLR",
    evidence_ids="R071;R042;R024;H020;H044;H050;R072;R075;R076",
    verdict="conditionally_identifiable",
    notes="Rank tests G (7/9; ratio identifiable, scale/DC nulls persist), J-corr (1/2 counterexample), J-decorr (2/2). Radiation-null reference rests on SINGLE source R071 (claim C18); in-situ material-diverse Hall recal unreported anywhere (claim C21). Cross-species dosimetry warning: R042 (~14x, claim C16)."))

R.append(dict(
    case_id="CASE8",
    objective="Any mutual calibration during quasi-static field (little persistent excitation)",
    states="B (constant); S_H;b_H;K_C;b_C",
    unknown_parameters="all five",
    known_inputs="none",
    excitation="none available (defining feature)",
    reference="none (in-pair)",
    observable_quantities="two lumps only: S_H*B+b_H and b_C",
    unobservable_quantities="everything else; K_C entirely invisible; Hall drift vs true field drift indistinguishable",
    estimator_candidate="none from the pair; fall back to injected self-test (CASE5) / scheduled reference (CASE4/6)",
    uncertainty_method="n/a (structural)",
    fault_test="none from the pair - zero fault coverage; schedule injected self-tests",
    evidence_ids="H018;H019;P042;H065",
    verdict="not_identifiable",
    notes="Rank test F (2/5). The long-pulse/steady-state regime that motivates the hybrid is exactly where the pair alone provides nothing - value rests entirely on engineered anchors. GPS/INS no-maneuver analog (claim C04); persistent-magnet NMR precedent (claim C28); steady-state DC-sensing requirement (claim C33)."))

R.append(dict(
    case_id="CASE9",
    objective="Fast transient: Hall bandwidth/delay verification and coil saturation detection",
    states="B(t); Hall pole a; delay dt; S_H;b_H; clip indicator",
    unknown_parameters="a; dt; S_H;b_H (coil chain trusted)",
    known_inputs="K_C;b_C",
    excitation="transient content near/above Hall pole; broadband for delay (phase slope)",
    reference="coil channel as wideband witness (trusted)",
    observable_quantities="Hall pole and delay in overlap band; relative dynamics; saturation events within overlap band",
    unobservable_quantities="content above Hall band (single-channel, no redundancy); pole from near-DC data (singular value collapses ~omega/a); delay vs gain-phase with narrowband excitation",
    estimator_candidate="cross-spectral transfer-function estimate; parametric fit of pole/delay",
    uncertainty_method="coherence-based TF confidence; FIM conditioning vs excitation band",
    fault_test="overlap-band residual burst against rho-consistency detects clipping (CT-saturation analogs)",
    evidence_ids="H045;H051;H052;H053;H048;H049;H050;H066",
    verdict="partially_identifiable",
    notes="Rank tests H-broad (pole s.v. 1.2e-1) vs H-narrow (1.4e-2; ~omega/a scaling). Crossover prior art (H045;H066) is signal combination, NOT identifiability proof, per stage prohibition. Air-core coils linear; clipping risk is in cored designs/readout/integrator rails."))

R.append(dict(
    case_id="CONF1",
    objective="Distinguish field scale from Hall sensitivity (B vs S_H)",
    states="B(t);S_H", unknown_parameters="alpha (scale gauge)",
    known_inputs="none", excitation="irrelevant (holds for all waveforms)",
    reference="required: absolute (current+model / NMR / characterized injection)",
    observable_quantities="none in-pair", unobservable_quantities="alpha direction (Theorem 1)",
    estimator_candidate="n/a", uncertainty_method="n/a",
    fault_test="n/a",
    evidence_ids="H021;H041;H042;H064",
    verdict="not_identifiable",
    notes="Gauge-group proof, CASE A null 1; matched numerically to 1e-15."))

R.append(dict(
    case_id="CONF2",
    objective="Distinguish simultaneous Hall and coil gain drift (common vs differential)",
    states="S_H;K_C", unknown_parameters="common-mode and differential gain factors",
    known_inputs="none", excitation="AC content (for the ratio)",
    reference="differential: none needed; common-mode: absolute reference or mechanism-diverse third channel",
    observable_quantities="differential drift via rho=S_H/K_C",
    unobservable_quantities="common-mode drift (identical to field change)",
    estimator_candidate="rho tracker (AC-band cross-regression)",
    uncertainty_method="rho CRLB",
    fault_test="rho-jump alarm (detection without attribution)",
    evidence_ids="H021;H018;H019",
    verdict="partially_identifiable",
    notes="CASE A: ratio identifiable (1.6e-15 null component), S_H alone not (0.72)."))

R.append(dict(
    case_id="CONF3",
    objective="Distinguish Hall offset drift from slowly changing field",
    states="b_H(t);B_LF(t)", unknown_parameters="drift-band trajectories",
    known_inputs="S_H;K_C (best case)", excitation="none in drift band by definition",
    reference="zero-field epochs; or coil constrains only field drift with |K_C*dB/dt| > sigma(b_C)",
    observable_quantities="field drift above coil noise floor",
    unobservable_quantities="below-floor field drift vs b_H; full LF trio without anchors",
    estimator_candidate="anchored bias-state KF",
    uncertainty_method="coil LF noise floor sets minimum detectable field-drift rate",
    fault_test="between-shot offset check",
    evidence_ids="H034;H035;H004",
    verdict="conditionally_identifiable",
    notes="CASE C1 nulls (c0,bH0),(c1,bH1,bC0) vs C2 full rank with anchors. Spinning-current leaves residual b_H floor (claim C07) so the state cannot be dropped."))

R.append(dict(
    case_id="CONF4",
    objective="Distinguish coil/integrator offset from low-frequency field",
    states="b_C or m; B_LF", unknown_parameters="b_C;m;g;LF field",
    known_inputs="calibrated Hall (for the resolving direction)",
    excitation="dB/dt variation (ramp+flat-top)",
    reference="calibrated Hall channel supplies LF/DC field (claim C02 direction)",
    observable_quantities="b_C;m;g;tau_L given Hall + dB/dt variation",
    unobservable_quantities="steady ramp vs coil offset (exact degeneracy); g vs m under constant dB/dt (g*r+m)",
    estimator_candidate="Kalman integrator-drift corrector (Arpaia form)",
    uncertainty_method="filter covariance; H004 hardware figures as achievable-scale reference (bench, non-fusion)",
    fault_test="flat-top residual (coil should read b_C only)",
    evidence_ids="H004;H005;H025;H026;H027;P003",
    verdict="conditionally_identifiable",
    notes="CASE I (4/4) vs I-ramp (3/4, g*r+m null matched). The hardware-proven mutual-calibration direction."))

R.append(dict(
    case_id="CONF5",
    objective="Distinguish temperature-induced from radiation-induced drift",
    states="kT;kD (drift coefficients)", unknown_parameters="kT;kD",
    known_inputs="measured T(t); dose proxy D(t)",
    excitation="thermal excursions decorrelated from dose accumulation",
    reference="pre-characterized temperature coefficients; species-matched dosimetry",
    observable_quantities="kT;kD separately iff T,D histories decorrelated",
    unobservable_quantities="kT vs kD when T proportional to D (exact collinearity); attribution during annealing-coupled windows",
    estimator_candidate="joint regression with T,D regressors; windowed validity",
    uncertainty_method="FIM conditioning vs T-D correlation; dosimetry uncertainty (C/E ~1.05+/-0.13 for validated foil practice)",
    fault_test="post-anneal recheck against pre-characterized T model",
    evidence_ids="R042;R024;R071;R072;R075;R076",
    verdict="conditionally_identifiable",
    notes="CASE J-corr (rank 1/2) vs J-decorr (2/2). Cross-species proxy warning ~14x (R042, claim C16); annealing hysteresis (R024, claim C22)."))

R.append(dict(
    case_id="CONF6",
    objective="Distinguish sensor failure from model mismatch",
    states="fault indicators per channel; model-error terms",
    unknown_parameters="fault magnitude/time; mismatch terms",
    known_inputs="whatever references are installed (cases 4-7)",
    excitation="as available; injected self-test on demand",
    reference="third channel / injection / reference shot for attribution",
    observable_quantities="that a change occurred (residual/rho jump); attribution ONLY with redundancy exceeding the unidentifiable orbit",
    unobservable_quantities="attribution from the bare pair; abrupt-vs-slow signature is heuristic prior, not proof",
    estimator_candidate="GLR/hypothesis-test filter bank; three-channel voting",
    uncertainty_method="test power vs drift-rate prior; false-alarm budget",
    fault_test="per-channel GLR; voting logic; scheduled self-test",
    evidence_ids="H050;H044;H021;H052",
    verdict="conditionally_identifiable",
    notes="Attribution impossible in CASE3 conditions; requires case-5/7 infrastructure. Precedents are fault DETECTION (H050 BLDC Hall faults; H044 redundant degradation), not Hall+coil attribution."))

path = os.path.join(os.path.dirname(__file__), "..", "outputs",
                    "02_ESTIMATOR_REQUIREMENTS.csv")
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=HDR, quoting=csv.QUOTE_ALL)
    w.writeheader()
    for row in R:
        assert set(row) == set(HDR), sorted(set(HDR) ^ set(row))
        w.writerow(row)
print(f"wrote {len(R)} rows to {os.path.normpath(path)}")
