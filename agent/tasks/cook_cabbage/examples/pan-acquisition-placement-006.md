# Pan acquisition, transport and supported placement — one practice sequence

Sourcea32648a, same restored TRAIN10 attempt, obs079–103. Public RGBD/self-state only. **One retained pan grasp and supported stovetop placement after withdrawal; no repeated mastery, verified heating, transfer or cooking.** The pan is on the right/front stovetop area; exact burner centering and heating effectiveness remain unverified. Numeric poses below are historical BODY evidence, not a fresh-world script.

## Failure and changed approach
The first compact→Cartesian extension displaced the pan and stalled near straight elbow. See [two-episode study/application](human-pan-board-comparison-005.md). Matching8214's forward-down gripper orientation alone did not reproduce its high-arm preparation and torso descent. Remeasured the moved handle rather than chasing the old target.

Established high right branch after withdrawing, while keeping free left elbow/hand clear. Public FK predicted direct independent torso slew would transiently drive right TCP down toz.770 although its endpoint wasz.959. A high-back torso waypoint made the predicted TCP path monotonic, but the actual descent still stalled with torso and free-left-shoulder lag. Raised the unloaded left shoulder, then released remaining torso preload via measured q. This is evidence that endpoint/TCP clearance alone does not certify elbow, forearm, housing or torso clearance; do not replay these waypoints blindly.

Fresh wrist depth identified a closer handle-neck location, avoiding another forced torso extension. At torso[1.06624,−1.59998,−.82001,−.0003], right target[.95,−.385,.94], finger[.79777,−.13375,−.58794], close[.07444,.98947,−.12409] reached[.948,−.385,.941]. Close produced fingers.0003/.0426, but retention was not claimed until lift.

## Retention and transport
- Torso q0 reduced to.97 with other torso joints held, lifting right TCP toapproximately[.875,−.384,1.052]. Pan followed in wrist/head images.
- Base withdrew.20; pan remained retained (obs093). Raised it for counter/grate clearance; Cartesian carry goal hit wrist tracking lag. Replaced that preload with measured arm q, preserving the actual retained pose.
- Turned toward stove, approached with bowl raised, inspected stove/pan depths. Pan followed the turn and translation. No opening until supported placement.

## Level and place using the PAN, not just handle TCP
Initial lower pose left the bowl bottom tilted about13°. Three non-collinear visible points on the flat inner bottom gave normal[−.21336,−.07619,.973998]. A fourth sample was on the forearm and was rejected; do not fit an object plane from an unverified pixel region.

Rotated measured gripper axes by the minimal rotation taking that measured pan normal toBODY+Z, holding the handle TCP. The resulting pan plane was freshly checked: normal[−.01330,−.00303,.999907], tilt~.78°, inner-bottomz~.960. This is object-frame measurement, not assuming a particular wrist sign or that the commanded orientation was achieved.

Measured grate samples were aroundz.904–.905, counter~.882. Lowered the level pan (right TCP target[.866,−.379,.993]) toward support, accounting for bowl-bottom thickness rather than using handle height as contact height. Opened at measured q (obs100), raised right shoulderq0−.15 first (obs101), then backed.20 and folded empty arms along a checked high path (obs102–103). Pan remained on the stovetop after actual hand/base withdrawal.

## Transferable procedure and limits
1. Choose a reachable handle portion and a whole-arm-clear approach; remeasure if the pan moves.
2. Close around handle body, lift and transport to verify retention—not just aperture or apparent contact.
3. Keep the bowl clear of counters, grates and the carrying forearm; release persistent preload after a miss.
4. Align the bowl footprint with the receiving support; level from visible pan geometry if needed.
5. Lower to measured support, release, lift clear before retracting, and verify the pan after withdrawal.
6. Recheck exact burner alignment/heat during cooking. A stable stovetop placement is not proof that the intended burner is active or heating the contents.

Practice snapshot `corrected-pan-on-stove-001` is provenance only, excluded from evaluation operations. No private state or practice feedback belongs in an evaluator procedure.
