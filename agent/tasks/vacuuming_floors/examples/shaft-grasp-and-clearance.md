# Narrow-shaft fallback, switch clearance and grip-dependent cleaning

## Transferable rule

When a measured motor-body grasp closes empty, do not repeatedly rotate an open hand against the tool. Withdraw into clear space and inspect an alternative **narrow, exposed shaft segment between the motor and switch**. Choose a segment with enough separation from the button for the other hand's complete wrist/forearm envelope, not merely its TCP. A higher grasp can lift successfully yet make the next operation infeasible.

- Start from a bent, clear elbow posture before Cartesian orientation targeting. Initial straight-arm IK can choose the wrong branch; inspect achieved pose, not requested coordinates. Clear the free elbow outward before tucking inward if its body blocks it.
- Use RGBD to measure the shaft at the intended grasp height; a nearby motor-top point is not its center. Orient fingers to approach across the shaft with closing jaws spanning its narrow width. Set orientation in clear space, approach open, close separately.
- Inspect prerequisite failures. A timeout can leave a pending base goal even when velocity is almost zero; a zero-displacement base anchor can clear the old target. Rejected closure is not a grasp attempt. Do not replay earlier travel.
- Require visible nozzle/tool motion on a bounded lift. Asymmetric finger positions may retain a shaft, but aperture alone proves nothing.
- Keep the holding grasp clear of the switch-working envelope. Measure button after presentation; press with feasible free-hand orientation, and stop/withdraw on green instead of forcing convergence.
- Calibrate the cleaning head again after changing grasp. Motor-grip TCP heights cannot be reused for shaft grips. Measure head and neighboring floor, lower by their observed separation, use a short powered sweep, then lift backward/lateral to reveal the patch. Carry raised between patches.

## Evidence and counterevidence

TRAIN256 first001 Q0: two motor-body closures empty, followed by tipping during near-object reorientation. No cleaning tested. Two dense paired human comparisons (13814 left pickup,13815 right pickup; RGB/state/action alignment in NOTES) motivated bent-arm staging, measured centering, separate closure and retained-lift checks. Human motor grasps were not blindly replayed and do not directly establish the shaft fallback.

Restored precontact branch: opposite-side motor staging still blocked. Upper shaftTCPz.80 closure retained on5cm lift, but free-hand switch attempts hit handle/arm obstructions. Release/regrasp destabilized the tool. EndedQ0 at1971ticks/65.7sim s. This branch is not success evidence or an advised route.

Fresh full-reset `vacuum-train256-practice-003` succeeded without any restore:

| Event | Evidence |
|---|---|
| Reach correction | Direct Cartesian initialization failedobs002; bent-arm branch and outward free elbow reachedobs005 |
| Measured lower shaft | Headsampleobs007 atpixel(280,620) BODY`.573,.152,.640`; target`.585,.150,.640`, fingers`[.9,0,-.435]`, close`[0,1,0]` attainedobs008 |
| Separate closure/lift | Pending-base closure rejected at354ticks; zero-displacementanchor thenclose370ticks, asymmetric5cm aperture; lift toz.69 visibly raised tool384ticks |
| Activation | Button`.5546,.1235,.9757`; side-facing closed Rstage`.59,.10,1.02`, back/down`.554,.123,.975`, smallfollow-through`.548,.138,.971`; greenobs016/476ticks; withdraw |
| Grip-specific calibration | CarryTCPz.740/nozzletop.136/floor−.005; lowerTCPz.640; shortforward.10 and reveal shelf patch; nativefalse877 |
| Coverage | Shiftedview found paired starting-floor particles; raisedalign, calibratedlower, forward.12, revealobs030; nativeQ1 at1382ticks/46.0667sim |
| Finish | One already-scripted survey added70ticks. admin_finishQ1 at1452ticks/48.4sim/328.261107202wall. WAIT written/read-verified; no repeat |

All coordinates/joints here are **conditional evidence, not a route or macro**. Different grasp, tool yaw, stance or torso changes the relation to nozzle and switch. No claim of force sensing, universal particle count, repeatability, first-try generalization or wall-time parity.

Cache: `<observation-cache>/vacuuming_floors-train020-p6-f8d4ca/vacuum-train256-practice-003/`. Firsttrueobs030 receipt `receipt_01792197637198665000_12c6c8169ad24a569b1fd3b498144286.json`; finalobs031 `receipt_01792197653351944000_34e83a3411d540d192479ac6603c74c8.json`.
