# RED TEAM — V10: Vendor-agnostic real-time QEC decoder / feedback appliance

Reviewer stance: kill it if possible. Sources: `REDTEAM_V10_sources.json` (RT-V10-01..19). Raw 80.4.

## 1. Novelty verification (G7-NOVEL)

Three nearest ledger neighbors. **CL-24/EXT-17** (cryo-CMOS quantum control/readout — the blocked lane): V10 is a room-temperature digital co-processor downstream of readout; no cryogenics, no analog front end, different buyer function (QEC/software team, not control-hardware team). **C34** (ultra-low-noise SMU): analog bench source-measure, orthogonal axis. **N07** (AI-rack transient load-test rigs): shares only the "real-time FPGA appliance" form factor — different domain, buyer, physics. Swept remaining quantum-adjacent entries (C31, C32, EXT-12): none touch classical decode; V09 (timing) is disjoint. **Verdict: NOVEL vs. the ledger.** Caveat: the one-pager's "unclaimed product category" premise was true mid-2025 and is false now — G7 passes, the whitespace claim does not.

## 2. Strongest bear case

Between Oct 2025 and Apr 2026 the category was claimed from both ends. NVIDIA's NVQLink standardized the controller-GPU interface — all four Western control-stack vendors (Quantum Machines, Zurich Instruments, Qblox, Keysight) and 17 QPU makers signed [RT-V10-02] — and CUDA-Q QEC ships free (`pip install cudaq-qec`): GPU RelayBP, TensorRT AI decoders, sliding-window streaming, real-time NVQLink workflows [RT-V10-03/04/05]. NVIDIA gives decoders away to sell GPUs; the appliance is commoditized as a complement before it exists. From the other end, Riverlane ($75M Series C [RT-V10-01]) already occupies the vendor-agnostic slot: hardware decoder Dec 2025 [RT-V10-09], sub-µs decode-feedback inside Qblox's stack Mar 2026 [RT-V10-07], IQM/Zurich platform [RT-V10-08], 11+ partnerships at 6.5 µs decode-and-feedback [RT-V10-16], and "streaming logic" — V10's headline differentiator — scheduled in Deltaflow 3 late 2026 [RT-V10-19], a year before V10's v1. QPU leaders decode in-house. V10 arrives ~2028 as fourth choice in a dozen-box merchant market.

## 3. Hidden competition the one-pager missed

- **NVIDIA** [RT-V10-02..05]: <4 µs FPGA-GPU-FPGA; Quantinuum Helios real-time qLDPC decode, 67 µs reaction vs. 2 ms budget; free CUDA-QX library; cudaq-realtime logical-QPU layer.
- **Quantum Machines DGX Quantum** [RT-V10-06]: external classical/ML decoders inside QEC cycles — decode embedded in the very control racks V10 must plug into.
- **EdenCode** (San Jose, Jan 2026, $1.3M pre-seed): hardware-agnostic real-time AI decoder, "drop-in layer" [RT-V10-14]; **QpiAI** decoder platform, Mar 2026 [RT-V10-15].
- **In-house**: Google AlphaQubit + open-sourced Tesseract [RT-V10-13]; IBM Relay-BP real-time on AMD FPGAs, a year ahead of schedule [RT-V10-10]; Microsoft/Quantinuum single-shot QEC.
- **Open source**: PyMatching 2/sparse blossom, ~1M errors per core-second [RT-V10-11]; micro-blossom — the FPGA MWPM decoder itself, free on GitHub [RT-V10-12]; Stim ecosystem.
- **China**: 国盾量子/中微达信 ez-Q Engine 2.0 delivered June 2025 at under half foreign price, QEC-capable 万比特 successor in development; 中微达信 is the named domestic third-party 测控 supplier spanning control/readout/纠错 [RT-V10-17/18]. Self-supplied market; BIS scope drift [G06-18] closes the channel regardless.

## 4. Engineering reality check

Sub-µs decode compute at useful distances is real — and already demonstrated by others, partly free. The binding constraint is not FPGA decode latency but syndrome I/O: syndrome bits are born inside the controller's readout FPGA after state discrimination (readout consumes most of a ~1 µs superconducting round). A third-party appliance needs a co-designed low-latency port into each proprietary backplane — exactly what Riverlane-Qblox built and NVQLink standardizes. "Vendor-agnostic sub-µs" is near self-contradictory: sub-µs requires per-vendor integration, and the generic transport now belongs to NVIDIA. Worse, the residual merchant buyers (ion/atom long tail) run ms-class QEC cycles — 67 µs on a GPU met Helios's 2 ms budget — so the sub-µs edge is overkill precisely where demand remains.

## 5. Market/WTP skepticism

No quoted buyer pays $60–250K for a box whose algorithm layer pip-installs. The QICK channel (~500 users) is an explicitly cost-cutting open-source community — PyMatching users, not appliance buyers. The "20+ QPU programs without decoder teams" mostly lack QEC-scale machines and cash; the five organizations with verified logical qubits (Apr 2026) all have decode arrangements [RT-V10-16]. Honest TAM 2028–2031: ~30–50 real-time-QEC systems worldwide, minus in-house, NVQLink's 17, Riverlane's 11+, and China → merchant residual ~10–20 boxes ≈ $2–5M cumulative. Not venture-scale.

## 6. Founder fit

Not PhD-lane, but C1=5 repeats the V01 anchoring error: component-level FPGA match, zero domain capital. Decoder credibility is a publications race (AlphaQubit, Relay-BP, LCD) judged by QEC theorists; the founder has no QIS community standing and must recruit decoder theorists against DeepMind, NVIDIA, and Riverlane. Every channel partner (control vendor) is already paired.

## 7. Score adjustments (raw 80.4)

| Crit | Raw→Adj | Reason |
|---|---|---|
| C1 | 5→4 | No QEC-community standing; theorist hiring race unwinnable (−2.8) |
| C2 | 5→4 | Sub-µs streaming already shipped (Riverlane-Qblox); overkill for residual buyers (−2.4) |
| C3 | 3→2 | Beachhead buyers get decode free (CUDA-Q QEC, PyMatching) or bundled (−2.4) |
| C4 | 5→4 | Expansion targets (rearrangement/shuttling feedback) are control-stack vendors' core features (−2.0) |
| C5 | 4→3 | Timing inverted: interface standard + partnerships locked 2025–26, three years before V10's window (−2.0) |
| C7 | 3→2 | NVQLink + Riverlane cross-stack + EdenCode/QpiAI: whitespace closed (−1.6) |
| C11 | 4→3 | Sub-µs value requires per-vendor co-integration — an attach product in disguise (−0.8) |

**Adjusted total: 66.4** (showdown comparability: 57.5e).

## 8. Steelman

Sovereignty buyers (EU/UK/JP/KR national programs) may refuse NVIDIA lock-in and pay for a neutral, auditable, on-prem decode appliance; superconducting fast-branching feed-forward may still need the last few hundred nanoseconds a GPU roundtrip cannot reach. If fault tolerance proliferates to hundreds of systems post-2030, an appliance-plus-algorithm-library vendor could matter — but every one of those arguments is Riverlane's own pitch, three years and ~$120M ahead.

---
**Candidate:** V10 · **Kill-probability: 85%** · **Biggest objection:** the whitespace closed in 2025–26 — NVIDIA gives decoders away free over NVQLink with all four controller vendors and 17 QPU makers signed, Riverlane already sells cross-stack sub-µs decode, and the residual merchant TAM (~10–20 boxes by 2031) cannot fund a company · **Novelty verdict: NOVEL** (vs. ledger; G7 passes — the kill is competition, not duplication)
