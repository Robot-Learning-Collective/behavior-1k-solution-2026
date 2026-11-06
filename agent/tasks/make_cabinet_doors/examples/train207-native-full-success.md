# TRAIN207 native-reset full-chain practice success

## Result and qualification
`cabinet-train207-full-reversal-003` began with native `admin_reset(..., practice=True, unbounded_practice=True)` through the switching shim, on source `e87cfaa129cc864da45ed45eba1a280277d3ae0a`, cache namespace `cabinet-run-023-p6-d689c6`. No snapshot save/restore in this attempt. Reset returned backend setup approximately497seconds, separate from task wall; this recurring setup value is NOT measured reset-call latency. Earlier wording claiming the reset itself took497wall seconds was incorrect.

- First native feedback, after seating: **attached=true/Q1**, step2737,91.2333sim s. Exact transition tick unknown.
- Canceled measured-joint preload, released left grip, withdrew open hand8cm.
- Native finish: **attached=true/Q1**, **2757ticks /91.9sim s /1893.7295063669953task-wall s**.
- Native meter was **2406ticks/80.2sim s below5163**. This is a completed **seen-instance, studied, unbounded practice full chain**, not held-out success, official-budget-enforced evaluation, wall-time parity or repeatability proof.
- First2075277tickQ0, registration0023782tickQ0 and prior restored4383tickQ1 remain unchanged. Current attachment/finish does not retroactively resolve the historical TRAIN10 attach-joint abort.

Evidence: `../train207-full-reversal-003-seating-feedback.json`, `../train207-full-reversal-003-finish.json`;67 actions in `../control-action-results.jsonl`;68 public endpoints under the own cache attempt directory. Last returned action: `receipt_01792184553440820000_9845deeca1d0408da89dfa4abec2e2ba.json`. Both hands open, no pending motion, attempt closed.

## What changed
Earlier study established that rectangular alignment/handle-face-up could conceal mating-end reversal. Rather than force a difficult opposite horizontal edge-grip IK branch or push harder after false seating, this fresh chain used **temporary broad support and a downward handle-region regrasp** to decouple orientation from the acquisition grip. The earlier checkpoint continuation needed180degrees; this run's current geometry required about57degrees negative yaw after its different navigation/regrasp. Therefore180degrees is NOT a task macro.

The temporary support was the visible ottoman, not an attachment attempt. Public depth measured its uneven top near.36–.37m; the panel settled near.39m. No object pose/contact/attachment-frame truth was used for motor targeting. Native training feedback was queried only once after the first actual cabinet seating, then at finish.

## Inspected phases
| Phase | Endpoint / sim s | Evidence / limitation |
|---|---|---|
|Top-edge acquisition, retention test, carry|obs1–12|Fresh top~.451m; shallow downward pinch then14cm lift; both empty arms unfolded before crouch; right tucked for aisle|
|Far-rim cabinet tipping|obs13–22 /40.73|Closer feasible precontact replaces earlier distant IK misses; bounded backward-diagonal draws, measured-q cancellation; visibly open-face-up after withdrawal|
|Early cabinet relocation|obs23–31 /53.50|Kept door upright at.60m using coupled torso/left pose; wrist RGBD corrected assumed short-rim target to actual visible long rim; right pinch,4cm partial lift, cancel lag; backward.4m then partial.5m draw|
|Guard recovery / heading|obs32–37 /63.30|Second drag stopped after~.28m with base_velocity_tracking_mismatch; released supported cabinet. Initial yaw also stopped with translation drift; changed position15cm away from right obstacle, then two inspected−45degree turns reached. No blind retry at old pose|
|Retained edge-grip reorientation|obs38–45 /70.43|Raised to1m; inspected quarter wrist transitions. Modified old qu wrist target1.0272→1.0, improving measured margin~.034rad. Achieved horizontal handle-up qh, then58cm inspection|
|Temporary support / regrasp|obs46–58 /81.97|Shifted panel over ottoman, bounded descent, canceled lag/released/withdrew. Changed heading−25degrees to make handle reachable without driving into ottoman. Fresh downward grasp,12mm then8cm retention probes; raised to65cm then90cm|
|Mating-end orientation / alignment|obs59–65 /90.23|Handle-grasp yaw−30degrees then~−27degrees; moved back-left20cm each; lowered to60/40cm. Fresh door/rim corner discrepancy led to base+.04fwd/+.045left, then35cm pre-seat|
|Seat / release / withdraw|obs66–68 /91.90|28cm handle TCP caused modest tracking lag; native attached=true at2737. Canceled measured-q preload, opened, withdrew8cm; final native goal true|

All simulator calls were sequential and endpoints inspected. Ordinary controller stops were treated as feedback, not execution uncertainty or permission for pressure escalation. No transport failure, replay, backend repair or peer-world call occurred.

## Reusable lesson, not numeric replay
1. Plan the placement workspace early, but inspect the whole cabinet footprint during relocation: the second backward draw still met an ottoman-side obstruction.
2. Do not confuse a visible long rim with a short end. The corrected public wrist sample `[.593,-.204,.248]` supported a successful right pinch; naming the wrong edge did not justify stale coordinates.
3. A near-corner acquisition grip can carry/tip reliably yet make the desired final horizontal orientation kinematically awkward. If fresh IK candidates fail, this does not prove global unreachability. A measured broad support and downward handle-region regrasp provided a practical alternative.
4. Downward handle grasp here stalled at~.006m finger sum, then visibly lifted the panel. The earlier checkpoint grasp had~.07m aperture; neither aperture alone proves retention or isolated handle contact.
5. Keep mating-end/handle-side relationships through tipping and regrasp. Use fresh corner pairs for final yaw/XY; old odometry is not calibrated world truth.
6. The final held-panel tracking lag was not a force measurement. Native attachment was checked separately; no further downward push was issued.

## Instance-specific pose references
All below require fresh geometry, limits and clearance; FK solutions are not collision checks.

- Upright door held while crouching to relocate cabinet: torso`[1.744,-2.75,-1.3,0]`, left`[-1.90544,.8332,-1.62175,-1.94757,.02823,.34195,-1.5308]`, TCP~`[.501,.249,.600]`, fingers down.
- Right rim pregrasp at32cm: `[-.87115,.1345,-.27448,-.94633,-1.24976,.60422,-1.46792]`. Corrected rim insertion at24.1cm: `[-.92769,.13055,-.1777,-.50324,-1.14202,.3911,-1.08964]`. Partial lift lag canceled before base drag.
- Temporary support approach, deep torso: left`[.10076,-.1345,-.23593,-1.62123,1.41197,-.22577,-.30928]`, TCP`[.52,.15,.46]`, fingers forward/closing down. Requested support endpoint`[-.0229,-.1345,-.19282,-1.19613,1.50872,-.22966,-.62504]` stalled near39.1cm, then measured-q release; no pressure increase.
- Handle pregrasp at50cm: left`[-1.35547,.89879,-1.07197,-1.24321,-.34357,-.89132,-1.5308]`, TCP`[.595,.426,.50]`, Fdown,C`[.4,-.92,0]`. Fresh wrist samples placed bar at~`[.612,.434,.402]`; insertion delta`[+.016,+.010,−.096]`. Wrist margin became~.01rad; no further outward extension.
- Handle-retained90cm: torso`[.6,-.9,-.3,0]`, left`[-.83355,.78455,-1.19484,-1.11011,-.78596,-.78433,-1.03159]`.
- Negative30degree rotation: `[-1.0119,.80848,-1.55612,-1.1083,-1.31188,-.9972,-.38468]`.
- Final orientation at90cm: `[-1.36337,.711,-2.3062,-1.10829,-1.60516,-.69709,.22198]`, Fdown,C`[-.548,-.837,0]`; q3 margin~.04rad.
-60cm: torso`[1.4505,-2.227,-.818,0]`, left`[-1.55915,.89911,-2.3162,-1.23609,-1.76964,-.76018,.34382]`.
-40cm: torso`[1.75,-2.65,-1.2,0]`, left`[-1.67476,1.06669,-2.23829,-1.4655,-1.77644,-.71921,.12068]`.
-35cm: torso`[1.744,-2.75,-1.3,0]`, left`[-1.59224,.96148,-2.23392,-1.3038,-1.76735,-.65539,.17519]`.
-28cm seating: same torso, left`[-1.38628,.8067,-2.2259,-1.03175,-1.74348,-.50298,.2255]`. Native goal true. Final measured-q release then8cm empty withdrawal.

Fresh obs63 far door opposite-handle corner~`[.565,.120,.409]`; exposed cabinet corner~`[.599,.163,.246]`. Wrist rim samples independently showed lateral offset. These drove the small base correction; they are not coordinates for another attempt.
