# Loaded board acquisition, pour and release — one partial transfer

Scope: obs104–127. Later pan relocation/activation and the native-successful training outcome are recorded in [example009](pan-reposition-switch-009.md) and NOTES. That later outcome does not erase this transfer's spills or establish recovery of every original particle.

Corrected sourcea32648a, same TRAIN10 restored attempt, obs104–127. Public RGBD/self-state evidence only. **One board grasp, retained lift/transport, visible cabbage/chili-material transfer into pan, and empty-board release on microwave top survived withdrawal.** Some material remained outside the pan (earlier spills plus pour scatter); this is NOT complete containment, cooked material, repeatability or full-task success.

## Geometry-adapted edge pinch
The two-episode study in `human-pan-board-comparison-005.md` supplied the edge-pinch/level-transport/pour hypothesis. The live board's front-right corner overhung the counter: initial board edgeBODYx~.809,z.896, cabinet face belowx~.886. This made lower-jaw access possible. Remeasured after base alignment; corner~[.712,−.256,.898].

Prepared an above-board arm branch using static FK and current torso, not replaying human q. Then lowered open jaws OUTSIDE the corner to[.68,−.29,.895], finger[.88,.45,−.15], close[0,.316,.949]; upper pad~z.94/lower~.85, with the lower jaw outside the counter lip. Inserted to[.737,−.245,.895] and closed. Aperture~.03 was not retention proof; board followed the actual .08m lift (obs110), then base withdrawal (obs112).

Three visible wooden-plane points gave a3.63° tilt after acquisition. Applied the minimal rotation mapping this measured plane normal toBODY+Z, rather than assuming the gripper axes define board level. Recheck actual geometry after every such correction.

## Raising without an uncontrolled torso-induced tilt
Backed away before changing posture, leaving forward clearance. Current R1Pro public FK showed chest pitch approximatelyq0+q1−q2. Matched joint increments preserved that pitch through each independent-slew leg:
- [ .97,−1.59998,−.82001,−.0003 ] → [ .97,−.90998,−.13001,−.0003 ] (q1/q2 both+.69): board moved forward and slightly upward.
- Then → [ .45,−.38998,−.13001,−.0003 ] (q0−.52/q1+.52): raised/retracted into carry posture.

Those are historical checks, NOT fresh-world commands. Static pitch preservation does not certify real tracking, swept-link clearance or object retention. Actual images retained the loaded board. Planned forward excursion required the preceding retreat; monitor torso lag and all links, not just final TCP.

## Pour: align the future lowered edge, not the hand
Measured pan rim/interior and board corners in current BODY. Transported laterally with board level; moved the hand slightly backward so the pouring edge's X-span fit the pan. Allowed for that edge moving toward the gripper inY as tilt increased. Saved practice-only `corrected-loaded-board-over-pan-001` before pouring.

Tilted approximately30° towardBODY+Y aboutBODY X. Only~.33simsec elapsed on that call. A no-goal `act(seconds=2)` then advanced ONE tick, not2seconds; seconds/max_steps are caps, not dwell times.

Raised the tilted board before a steeper pour to keep its future lowered edge above the rim. **This fast lift coincided with many cubes becoming airborne; it was not a clean spill-free transfer.** Material subsequently visibly accumulated inside the pan, with scatter on the stove/counter too. Steepened by another12°; board appeared empty byobs121 and after re-leveling obs122. Both pale green and orange diced material were visible in the pan. Their cooked state was not verified.

Prefer establishing adequate edge clearance BEFORE initiating tilt, avoiding a rapid mid-pour lift. Assess settling from actual elapsed ticks and object motion. Lead's confirmed protocol6 guidance: short intentional settling may use a finite awaited series of normal `act(max_steps=1)` calls, count actual executed ticks, preserve every endpoint, and stop on faults/uncertainty/ended/no progress. Omitted commands persist; this is not relaxation. No sleep/observe time advance, fabricated unreachable targets, raw RPC or controller edits.

## Empty board placement
Leveled the empty board from a measured wooden-plane normal (~41° before correction). Chose a clear flat microwave top, measured~z1.18, with board COM over the support and modest front overhang for lower-jaw clearance. Aligned laterally while above support, lowered level toTCP~z1.18, replaced preload with measured arm q and opened. Backed straight out .12 before lifting/folding, so the lower jaw did not hook the board underside. Board remained supported after withdrawal (obs127).

Generic rule: select a clear supported placement, verify footprint/COM and jaw-exit path; release and withdraw in a direction that does not re-engage the object. 'Lift first' is not universal for a vertical board-edge pinch.
