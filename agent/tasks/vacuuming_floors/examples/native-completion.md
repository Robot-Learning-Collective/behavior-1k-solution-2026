# First native whole-task completion — TRAIN20

Attempt `vacuum-train020-002`, original assigned reset, no restores. Controller26efe4a/protocol6/sourcea32648a unchanged. Public RGBD/self-state and authorized native practice feedback only. Human RGB/proprio from pinned demos13814/13815 informed lower-body grip and lateral switch approach; no downloaded human reward/termination values used.

- First verified success: **step1256 /41.8667sim s**, after obs034 lift/reveal. `success=true`, `q_score=1.0`, `satisfied_fraction=1.0`, sole native `(not (covered floor.n.01_1 dust.n.01_1))=true`.
- Previous check step1220 immediately after shelf lowering was false. The following lift/reveal executed36ticks; success first verified afterward. Do not assign exact earlier completion tick.
- Official comparison budget3617ticks; first verified success uses34.725% of budget. Practice unbounded setting was not used to claim a deadline beyond this meter.
- A safe retreat was already in the same Python call after feedback; it executed82additionalticks. Native admin_finish reconfirmed success at**1338ticks/44.6sim s**, **633.6728355wall s throughfinish**. First-success wall endpointobs034~599.9s; not teleoperation-wall parity.
- One successful reset so far, **not repeatability or held-out generalization**. Continue fresh independent practice, no old snapshot restoration.

Evidence cache: `<observation-cache>/vacuuming_floors-train020-p6-a98736/vacuum-train020-002/`.
- obs033: `receipt_01792171885547761000_8b46af397a1e45cda599df32cbeaeb74.json` (false feedback at1220).
- obs034: `receipt_01792171901446803000_a57c44dc7dd9470e96a7bb75f087d8df.json` (1256; subsequent native feedback true).
- obs035: `receipt_01792171920861996000_981f32a5470247d8a3c75cb6bfcc4e5a.json` (1338; finish true).
- Actual feedback/finish responses are in native session tool transcript; action endpoints preserved in control-action-results.jsonl and cache. No video packaging performed.

## Mechanism and critical failures

Lower motor-body grasp, not upper shaft: open stage mirrored human13814 frame300 joints; clear BOTH arms forward while standing before crouch. Lower torso `[1.48,-2.281,-.842,0]`. Closed first behind body (empty0gap), reopened and inserted5cm forward into `[.55,.185,.39]`, fingers `[.62,.02,-.78]`, close `[.02,1,.04]`. Closed gap~.095m;6cm lift visibly retained vacuum.

Switch: right human-derived approach q620→separateclose→q670; leftroll10°, rightstage `[.69,.025,.97]` with finger `[.16,.98,.15]`, close `[-.99,.15,.06]`. Fresh red switch~`[.694,.100,.978]`; directpress hitrightq2limit atactual `[.706,.075,.973]`. Held measured rightq and rolled left+4°: visible green atobs020. Released left preload with measuredq and withdrew right. No force/hidden-toggle claim.

Cleaning: initial foot-adjacent patch lower left `[.55,.31,.39]` thenlift `[.55,.185,.48]`; baseforward.40/right.44, central lower/lift samex/y,z.39↔.48. Shelf approach: yaw−35, free right hand touched visible desk edge; withdrew rightq3+.15. Diagonalforward.60/left.15 tripped trackingguard afterpartial. Changedrouteleft.18 thenforward.32/yaw−10 reached. Shelf lower `[.57,.17,.39]`, liftback/left `[.49,.30,.49]` led to native success. This is a learned observed sequence, **not a blind replay macro**; fresh geometry, clearances, endpoint results and feedback govern every attempt.

The upright high-shaft attempt001 ended incomplete at1897ticks/63.2333s, nativefalse/Q0,1522.3659wall s. Two patches visually removed but repeated navigation guards. Lower-body grip, crouch-clear free arm and changed route improved this second attempt; not an isolated causal experiment.
