# U_B — Unsolved problems from CS-B (China winding/coil equipment & industrial HTS)

Schema: `U-### | lane | problem (<=30 words) | who suffers (archetype, named example) | evidence [refs] | severity 1-5 | why unsolved (1 line) | small-team-exploitable Y/N | linked clusters`
Local ids U-B-n; lane C12 per charter. Evidence ids resolve in `10_COMPETITORS/CS_B_sources.json`. Merge into UNSOLVED_REGISTER.md at Phase-1 close.

U-B-1 | C12 | No merchant vendor sells NI/REBCO-native winding machines to non-affiliated buyers in China; fusion startups build their own — Startorus built two machine generations in-house. | New fusion cos & labs without machine teams (named: 星环聚能 "自主研发两代绕线机"; 能量奇点 in-house line) | [CS-B-13][CS-B-11][CS-B-01] | 4 | Incentive: integrators treat winding as moat; captive shops (聚能) serve only parents; demand too thin for a merchant catalog | Y | P01 P05

U-B-2 | C12 | Winding is the acknowledged hardest core process even in 600-unit/yr MRI magnet production, but the know-how (干式绕线) is trade-secret — not embodied in any purchasable equipment or recipe product. | Industrial magnet producers scaling volume (named: 健信超导 — "绕线是核心生产工序之一，技术难度较高") | [CS-B-07][CS-B-08] | 3 | Incentive: process IP hoarding beats equipment sales at current volumes; no vendor productizes the recipe layer | Y | P02 P01

U-B-3 | C12 | Coil production is fragmented into separate contracts — winding line, 匝间绝缘包绕, VPI, post-impregnation inspection, LN2 test — buyer carries all interface/rework risk; no integrated cell with inline QC exists. | Big-science magnet programs (named: HFIPS/ASIPP 关联业务 contract list; SWIP buying external test systems) | [CS-B-02][CS-B-04] | 3 | Technical: no during-winding QC instrument exists to close the loop, so steps stay separable and QC stays post-hoc | Y | P04 P03

U-B-4 | C12 | Qualified-supplier base for outsourced HTS magnet builds is thin: ASIPP's ¥6.38M D-type HTS magnet system needed a second tender (二次招标); test capability is bought, not integrated. | State institutes outsourcing coils (named: ASIPP D型 re-tender; SWIP test-system award) | [CS-B-18][CS-B-04][CS-B-05] | 3 | Economic: spec ceilings exceed what the few non-captive shops can qualify for at institute price points | N (China channel closed to founder; value = intelligence + analog for Western labs) | P02 P04

U-B-5 | C12 | Industrial HTS OEM ramp is bottlenecked at coil/magnet production: 联创超导 booked ¥45.21M revenue through 2024-10 against a ¥330M target despite ¥432M in-hand orders; buyout terminated. | HTS induction-heater OEMs and their industrial customers (named: 联创超导 / 宁夏旭樱 100+ unit backlog) | [CS-B-09][CS-B-10] | 4 | Technical+economic: coil throughput/yield does not scale like assembly; no bought-in line or QC layer available to de-risk the ramp | Y | P01 P04

U-B-6 | C12 | Tape QC ends at the spool: SSTC ships Ic-mapped tape, but nobody sells coil-level inline QC (during-winding Rc estimation, defect-map-synchronized feed); defects surface only after stacking/VPI/cold test. | Anyone winding NI coils (named: ASIPP 26.8 T team; 能量奇点 32-pancake 经天 stack) | [CS-B-14][CS-B-03][CS-B-11] | 4 | Technical: turn-to-turn Rc during winding is an unsolved commercial measurement; incumbents solved it only as internal recipes, if at all | Y | P04 P02

Note: an incumbent-says-solved counter-read applies to U-B-2/U-B-6 — 健信 markets quench-auto-recovery He-free magnets [CS-B-08] and SSTC markets mapped tape [CS-B-14], yet institutes still buy post-hoc inspection and LN2 test as separate line items [CS-B-02][CS-B-04]: both sides cited.
