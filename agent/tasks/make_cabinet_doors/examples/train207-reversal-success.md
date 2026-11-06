# Seen TRAIN207 — 180-degree reversal component success

## Result and limits

New practice attempt `practice-restore-train207-postregistration-unattached-d6f4dea269a946d387b350dc2d7cf30d` restored the explicitly saved, unattached end state of `cabinet-train207-registration-002`. It did not reopen either finished full-reset attempt.

- Native seating feedback: **attached=true/Q1**, step4359/145.3sim s, before commanded release.
- Released left gripper and withdrew the open hand7cm.
- Native finish: **attached=true/Q1**, step4383/146.1sim s;687.5777582349983task-wall s in this restored continuation.
- Restore baseline3782ticks/126.06666666666666sim s; continuation601ticks/**20.03333333333333sim s**. First positive feedback was577ticks after restore, not an exact attachment-transition tick.
- This is a **checkpoint-based component success on studied/seen207**, not a native-reset completion, held-out success, within-budget evaluation, or repeatability proof. Absolute meter4383<5163 does not remove those exclusions.
- First207 failure5277ticks/Q0 and registration002 failure3782ticks/Q0 remain unchanged.
- Current sourcee87cfaa129cc864da45ed45eba1a280277d3ae0a/cachecabinet-run-023-p6-d689c6 survived an actual native attachment and normal finish. No crash, uncertain transport, backend change, or opening/closing of the cabinet door. This does not retroactively resolve the old TRAIN10 crash.

Evidence: `../train207-reversal-seating-feedback.json`, `../train207-reversal-component-finish.json`; own cached receipts and `../control-action-results.jsonl`. Pre-seating snapshot `train207-reversed-aligned-above` was saved atstep4340 but never restored in this attempt.

## What changed

Public15602 tip images showed open-front-side pushing, whereas207's cabinet was tipped by a far-rim pull from its closed side. A rectangular outline and handle-face-up condition do not distinguish180-degree mating-end orientation. The earlier postrelease push test failed. This test reacquired the visible handle region, lifted the door, rotated it180degrees with its handle face returning upward, freshly realigned it, and descended. Attachment then succeeded **without postrelease registration pushes**.

This strongly supports mating-end orientation as the missed variable. It is not a strict isolated causal proof: grasp, small final offsets and seating path also changed. Public observations do not reveal private mating frames. The general lesson is to track the asymmetric handle/hinge-side relation through cabinet tipping; do not infer correctness from parallel edges or increase seating pressure.

## Executed phases

All calls were sequential, individually inspected `practice_client.act`; no unattended replay.

1. Restore unattached state; establish both grips open. Base approaches[+.10fwd,+.05left] then[+.036,+.035] positioned the downward open left hand over the bar.
2. Fresh wrist depth, obs4: bar center[.5994,.4527,.27149], panel plane~.256m. TCP pregrasp[.596,.450,.357], closing direction[.56,-.83,~0], fingers down. Lowered.086m; actualTCP.274. Closing stalled at7.4cm aperture, not itself retention proof. Lifted.012m then.08m: panel visibly lifted away from the cabinet while its handle remained stationary in wrist view. Contact region may include panel geometry; do not claim an isolated thin-bar pinch.
3. Lifted retained panel toTCP[.55,.45,.60], then[.45,.40,.90]. Closed aperture remained~6.9cm. Public dresser points were aroundBODYx1.1/y1.0/z.76; the rotation workspace was nearer the robot. FK estimates and images informed clearance, not collision certification.
4. Rotated45deg,90deg, then four inspected joint-space substeps to the alternate180deg branch. The transition temporarily tilted the panel~35deg; it was not a continuously level yaw rotation. Final fingers down/C[-.55,.84,~0], minimum left endpoint margin~.102rad. The rejected negative-yaw and135deg candidates had near-limit/large-branch jumps and were not executed.
5. Lowered toTCP[.60,.35,.60], then[.60,.35,.40]. These inspection poses had wrist margins~.05rad; do not extend them blindly.
6. Obs18 fresh head corners (BODY metres):

|Point|Door|Cabinet|
|---|---|---|
|Near right|[.397374,.202005,.384628]|[.552804,.135367,.245968]|
|Far right|[.768727,.429555,.388729]|[.929701,.376475,.236333]|

Base shift[+.158fwd,-.060left] matched the two corner offsets, with no base guard. Obs19 near corner door[.396078,.199760,.382417] vs cabinet[.399075,.192965,.247715]: within~7mm in XY. Cabinet long axis~31.4deg, door~31.6deg. These are observed corner estimates, not attachment-frame truth.
7. Coupled descent toTCP[.60,.35,.35], snapshot, thenTCP[.60,.35,.28]. Feedback at endpoint21/step4359 returned attached=true/Q1. Release endpoint22/4364; empty-hand withdrawal endpoint23/4383. Finish remainedtrue/Q1.

## Exact reference joint goals — instance-specific, not an evaluation macro

Right remained open at `[-.65,.14,-.08,-1.1,0,.05,-.1]`. Left held grip0 through seating, then grip1. All vectors require fresh public geometry and matching robot bounds in another world.

|Stage|Torso q|Left q|
|---|---|---|
|Lift60cm|[1.4505,-2.227,-.818,0]|[-.96974,.7953,-1.0466,-.9625,-.64394,-.87791,-1.22847]|
|Lift90cm/0deg|[.6,-.9,-.3,0]|[-.7808,.76624,-1.08035,-1.10848,-.72509,-.67643,-1.14745]|
|45deg|same|[-.70981,.73277,-.91807,-1.10828,-.53875,.02542,-1.30975]|
|90deg|same|[-.64038,.68519,-.74188,-1.1082,-.47953,.74502,-1.31409]|
|Transition1/4|same|[-.61521,.65312,-.65692,-1.10823,.17951,.79261,-.62037]|
|Transition1/2|same|[-.59004,.62105,-.57196,-1.10825,.83854,.8402,.07336]|
|Transition3/4|same|[-.56486,.58898,-.487,-1.10828,1.49758,.88779,.76708]|
|180deg|same|[-.53969,.55691,-.40204,-1.1083,2.15661,.93538,1.4608]|
|Inspection60cm|[1.4505,-2.227,-.818,0]|[-.93131,.42253,-.61911,-.82853,2.25409,.88567,1.5108]|
|Inspection40cm|[1.75,-2.65,-1.2,0]|[-.924,.56397,-.61572,-1.2017,2.2962,.73321,1.5108]|
|35cm|[1.744,-2.75,-1.3,0]|[-.9548,.47483,-.58798,-1.00225,2.14433,.82182,1.39737]|
|28cm seating|same|[-.98787,.38195,-.69695,-.65553,1.85018,.83421,.97057]|

After release, reused35cm goal for withdrawal. No deeper force escalation, registration nudge, or door opening/closing was needed.
