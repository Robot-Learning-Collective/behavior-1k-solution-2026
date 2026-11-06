# Corrected-source four cuts + human-informed final pickup

TRAIN10 practice only; same a32648a source/attempt as knife-cutting-002. No new reset, no cross-source snapshot, no full-task success. Current obs142/sim259.43, feedback step7783 confirms8/8 real halves,0cooked/inside oven, fridge open/oven closed. Snapshot `recovery_four_cut`. Right retains knife; left open. Seven halves on board (two overlapping), one on steel beside back-left board edge. This is one restored practice trajectory, not independent repeatability.

## Stroke accounting
- Whole1: TWO downward approaches; level blade stalled without split, lifted/reoriented roll−30, second tip-down approach split; see knife-cutting-002.
- Whole2: ONE downward pass in TWO increments1.10→1.015→.990; split by obs82/measuredz1.007, release/lift obs84. No lift/restrike between increments.
- Whole3: ONE pass, target[.739,−.16,1.00] at torso[.85,−.85,−.22,0], obs103/sim226.57 reached[.739,−.160,1.001] and split. Lift obs104 to1.10, snapshot `recovery_three_cut`. One half rolled off board onto adjacent steel, not lost off table.
- Whole4: ONE pass target[.7145,−.1597,1.00], obs140/sim258.97 reached[.713,−.157,1.012], native stalled, q4lag+.018/q5−.018; split visible before endpoint. Measured-q release obs141 then lift obs142 to[.739,−.158,1.104]. No additional sawing. Feedback after lift confirms all8 real.

Fourth cut event receipt `receipt_01792174370556749000_e25e83f4de4444058f64eca9e79b6e43.json`; release `receipt_01792174384289040000_82c5c3933df744888eb06d5c054bc4e5.json`; final lift/feedback `receipt_01792174398148792000_8e3eb752c6534102a2ae374f27507b7a.json` under active public cache.

## Human study adaptation: fourth whole pickup, failures preserved
See human-three-episode-study.md for3public episodes' aligned RGB/measured/action evidence. The human oblique approach was useful; blindly adding pitch to our old near-limit branch was not.

1. Free-space left pitch−20 at[.80,.20,1.10] saturated q3/q7, measured[.847,.196,1.094], no useful tilt. Returned inspected prior fore-aft q staging. No forcing through endpoint limit.
2. Bowl still interfered at old whole[.807,.214,.903] even with fore-aft pads. Withdrew. Closed-empty-finger front-wall push[.66,.07,.95]→[.82,.07,.95] moved bowl back but did NOT establish sufficient whole-wrist clearance. Subsequent descent to[.807,.214,.886] tipped bowl around wrist. Closing6.7cm aperture and lifting obs118 **held bowl, NOT food**; food remained on steel. This was a failed food grasp, not a success.
3. Used actual retained empty bowl: lateral carry[.78,.48,1.10], lower.96, release, withdraw. Bowl settled on side at left steel, physically clear of board. It need not be upright for task, but this is not clean upright placement.
4. Old fore-aft pinch at fresh whole[.786,.299,.886] closed fully EMPTY, pushed/rolled whole left. Lifted rather than repeating stale position. Public-depth extent then5/50/95%: x.731/.747/.765, y.419/.431/.459, z.883/.901/.909. Separated XY staging from descent.
5. Adapted HUMAN-STYLE OBLIQUE fingers[.6,−.2,−.775], closing[.2,.96,−.09], using own public IK, NOT copied human joints. Inspected joint interpolation above1.075m, then staged q[-1.99586786,1.22282774,−1.94835254,−1.87137927,2.04931339,.57946722,.48118237]→[.749,.349,1.10]. Native path reached, not a swept-clearance guarantee.
6. Align[.747,.438,1.00], straight descend targetz.892→measured.896. Close obs130 gave fingers.0414/.0203 (~6.2cm), left axes closing[.20,.98,−.09], fingers[.58,−.19,−.79]. Lift obs131[.748,.437,1.080] visibly retained whole. Lateral/back base carry obs132 also retained. This changed palm approach from behind food toward front, avoiding bowl.
7. High inward carry target[.64,.106,1.05] saturated elbow q4 at−2.0844, attained[.715,.135,1.055], still retained. Accepted nearest-valid measured q and moved baseback.10 instead of forcing. Rounded q4−2.0844 was locally rejected against exact float bound without motion; explicit correction from actual bound+1e−5 changed measuredq4 by5.22e−5rad and passed. Lowered whole[.74,.106,.925]→measured[.736,.104,.926], opened obs136, withdrew obs137. Whole remained board, nowtop[.727,.124,.929].
8. Baseleft.15 aligned right knife workspace; new top[.72854,−.00970,.92929]. Aligned knife TCP top−[.014,.15,−.171]≈[.7145,−.1597,1.10] and performed final stroke above.

Base carry timeouts were caller step limits with base_safety.triggered=false, not obstacle/fall proof; residual goals cancelled by zero-displacement replacement. During bowl interference native torso effort was large (−87Nm at descent); not calibrated contact force, no safety fault or uncertain result. Retention/placement assessed from RGB after lift/carry/release, not aperture/achieved alone.

## Current continuation
Stage/retrieve baking sheet next, adjacent to board before eight half transfers. Knife can now be placed on empty steel and released/withdrawn. Bowl is left on its side, outside food workspace; do not count bowl accidentally retained as food. Need independently verify each half placement and oven/cooking/door closure. All8 existence is training feedback only; never evaluation-policy predicate input.
