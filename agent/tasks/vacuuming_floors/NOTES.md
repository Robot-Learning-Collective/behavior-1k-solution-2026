# Vacuuming floors — practice and distinct-instance checkpoints

## EVAL PROCEDURE — current checkpoint

**TRAIN256 learned full-reset PASS/Q1; now WAIT_NEXT_INSTANCE.** `vacuum-train256-practice-003` began with `admin_reset`, no snapshots/restores in this attempt. First native true at1382ticks/46.066666667sim s after shelf plus paired starting-floor treatment; a survey action already queued in the same Python call added70ticks. `admin_finish()` reconfirmedQ1 at **1452ticks/48.4sim s/328.261107202wall s**. Then wrote/read-verified `PRACTICE-HOLD=WAIT_NEXT_INSTANCE`. No active attempt; no further controls/reset. One full-reset success meets lead996/999; no repeat gate. First256Q0 remains unchanged. General pickup upgrade: use an accessible narrow shaft segment between motor and switch when motor-body grasp fails, leave adequate free-hand clearance, set elbow branch before Cartesian targeting, then separate close and visibly verify bounded lift. Recalibrate nozzle height for the new grip. See `examples/shaft-grasp-and-clearance.md` and updated `EVAL-PROCEDURE.md`.

**Latest first-attempt transfer TRAIN256 FAILED/Q0** (`vacuum-train256-first-001`), admin_finished1034ticks/34.466666667sim s/278.597971924wall s. No demos, snapshots/restores or intermediate feedback. Failure was acquisition, before activation/cleaning: measured motor top around`.592,.161,.402`, attemptedTCP`.58,.16,.425` attained`.578,.161,.428`, closureempty; changed base+.055/left−.025 andTCP`.53,.19,.395`, closureempty again. Tool tipped during subsequent open-hand reorientation. Bounded fallen-body recovery used changed approach/low torso/shorter reach, but IK stalls then tracking block; final withdrawal also retained residual. No tool retained or powered, no coverage test in256. Faults were ordinary finite IK/pose limits, not infrastructure errors. Invalid coupledtorso1.75 request rejected before motion; corrected1.69 accepted. Finalobs028`receipt_01792196602920679000_ebfc9a475b9c421cb8aa5dedc08bfbb8.json` in `<observation-cache>/vacuuming_floors-train020-p6-f8d4ca/vacuum-train256-first-001/`. No active attempt after that first finish; subsequent authorized development is recorded below. First188Q0/practice002Q1/abortedrestoredcomparison unchanged.

**Counterevidence to pickup robustness:** visible motor-top depth and separate closure were insufficient here. Do not copy the failed256 grasp heights or recovery as a proven method. A fully closed jaw with stationary tool is empty, never retention. Compare paired human precontact/contact/closure sequences before changed retry; existing coverage correction is not disproven because256 never reached cleaning.

Use `EVAL-PROCEDURE.md` steps1–7 and `examples/coverage-and-forward-sweep.md`: fresh RGBD alignment; clear arms then intermediate crouch; measured vertical motor-body grasp/separate close/visible lift retention; measured button presentation and bounded press, withdraw on green; raised travel and measured nozzle-to-patch alignment; calibrate floor-level posture, short powered forward sweep, lift backward/lateral to REVEAL prior patch; survey ALL floor sectors including starting footprint from a SHIFTED viewpoint; finish-only native feedback on first attempt. Coordinates are conditional references, never universal targets. Use switching `practice_client as s` from tools/python; new-instance first attempt prohibits demo study, restore and intermediate feedback.

**TRAIN188 first attempt completed FAILED/Q0**, 1353ticks/45.1sim s/560.190485716wall s. No new demo study, snapshot/restore or intermediate feedback. This is usable honest checkpoint evidence, not a success qualification. TRAIN20 six successes/two failures remain development results. Latest full-reset development attempt `vacuum-train188-practice-002` SUCCESS/Q1 at2784ticks/92.8sim s/618.780837331wall s. Saved a preclean snapshot but never restored; practice feedbackfalse1488/1800, true2784. Both188attempts admin_finished. Latest HELD-OUT-KICKOFF supersedes old TRAIN20 hold/binding paragraphs below. This is studied improvement, not replacement of first-attempt failure.

### TRAIN188 `vacuum-train188-first-001`

Fresh unseen instance, same scene house_double_floor_upper; shim printed SLOT_SWITCH. Pickup used fresh geometry, vertical lower approximately`.535,.175,.425`, separate closure and5cm lift with visible retained tool (~9cm aperture). First lateral switch press failed; withdrew/released, remeasured button`.59739,.11737,.97441`; changed backward/downpress`.602,.112,.974`, fingers`[-.095,.952,.291]`,close`[-.992,-.115,.055]`,position_tol.002/.7s. Green visible on withdrawal018. Cleared free hand, upright nozzle and raisedcarry.

Turned90° toward bed floor. Three visible patches measured BODY`[1.267,1.097,-.005]`,`[1.239,.782,-.005]`,`[1.234,.237,-.005]`. Raised travelforward.60/left.07, lower`.55,.18,.43`,lift`.50,.26,.50`; left.45,lower`.55,.26,.43`,lift; remeasured final visiblepatch`.683,.592,-.005`,left.34/forward.04,lower/lift. No baseguard returned in these travel actions. FinalTCP`.505,.258,.505`, toolretained/green, no visible remaining dirt in current views, but several relevant floor pixels were occluded by nozzle/hand; **absence was not proven by reveal**. Nativefinishfalse/Q0. Diagnostic candidates are insufficient nozzle-to-floor contact height and incomplete visual coverage; neither is established. Do not claim three removals from occlusion alone. Next change must follow dense aligned cross-demo cleaning/contact and neighboring travel/release study including recorded actions.

Public cache `<observation-cache>/vacuuming_floors-train020-p6-f17939/vacuum-train188-first-001/`; finalreceipt`receipt_01792177530103577000_dc1f594921124a1393ba0bb07b1d5327.json`,obs030. Finish returnedfalse at1353ticks, no later motion. Full-reset first test preserved; no favorable replacement.

## TRAIN256 development results — preserved branches, then fresh success

- Full-reset `vacuum-train256-practice-002`: saved `train256-upright-precontact-002` at197ticks/6.5667sim s. Yaw-aware motor approach and torso-led descent did not establish retention; restored at330ticks/Q0, closing that attempt. Not a full-reset success.
- Restored branch `practice-restore-train256-upright-precontact-002-050989b07d744000ac297d8703978a8e`: opposite-side route did not solve motor access. Upper-shaft grasp atTCPz.80 retained on5cm lift, obs016→017, but grasp too close to switch led to arm/handle obstructions during free-hand pressing. Moving shoulder/press direction did not activate it. Release for lower regrasp left tool unstable; it fell. FinishedQ0 at1971ticks/65.7sim/529.847552066wall. Do not package this route or claim lower motor failure isolated to orientation.
- Fresh `vacuum-train256-practice-003`: no restore. A direct Cartesian command from initial straight-arm branch failed (obs002/60ticks); explicit bent-arm staging corrected it. Free R elbow inward posture initially blocked (obs004/235), changed outward and reached(obs005/263). Measured narrow shaft in head RGBD, used normal torso and near-horizontal fingers, centered jaw below switch and above motor. Base pending blocked first closure without motion(obs008/354); explicit zero-displacement base anchor cleared it, then closure(obs010/370) and5cm lift(obs011/384) visibly retained tool with asymmetric5cm aperture.
- Presented shaft inward. Fresh button`.5546,.1235,.9757`; side-facing R above/forward stage, backward/down contact then small lateral follow-through made greenobs016/476. Withdrew immediately, released L preload. Kept approximately30cm between grasp and button rather than the previous~15cm; coordinates are evidence only.
- New grip required new calibration: carryTCPz.740 had nozzle topz.136, nearbyfloor−.005. LowerTCPz.640 gave near-floor nozzle; shortforward.10m and backward-left lift revealed shelf patch. Feedbackfalse877, no assumption of finished task. Shifted survey found two particles in R wrist atBODY`.695,-.536,-.005` and`.628,-.520,-.005`; raised lateral alignment, calibratedlower, forward.12, reveal. First nativeQ1 at1382ticks, obs030wall303.3; already scripted survey031 then finishQ1 at1452/48.4/328.261107202. No baseguard observed. This is adaptive studied success, not unseen first-try or fixed-policy qualification.

Public cache all256 attempts: `<observation-cache>/vacuuming_floors-train020-p6-f8d4ca/`. Successful003 finalobs031 receipt `receipt_01792197653351944000_34e83a3411d540d192479ac6603c74c8.json`; firsttrue endpointobs030 `receipt_01792197637198665000_12c6c8169ad24a569b1fd3b498144286.json`. Scene/session retained under WAIT.

### Exact first256 failure anchors

First001 motor-depth-only alignment reached pose but not grasp: obs005/269ticks approach, obs007/279 first closureempty; changed base/height, obs010/388 approach, obs012/398 secondclosureempty. Open reorientation obs013/458 tipped the tool. Subsequent recovery obs022/878 and024/910 stalled; finalobs028/1034 still unretained. Grasp failure preceded all activation/cleaning. The missed checks were pad/body alignment beyond a top-surface point, reach margin, and selecting an alternate accessible grasp before repeated nearby reorientation. Orientation as sole cause remains unproved.

## TRAIN256 pickup study after first failure — before changed practice retry

Lead996 authorizes learning on256, stop at ONE full-reset success then writeWAIT_NEXT_INSTANCE. First256Q0 immutable. Reopened13814 sheets2/3/4 (320–550) and13815 sheets2/3/4 (290–520), head/bothwrists at10frame spacing; extracted measuredstateRGB−1 and recordedactionRGB−2, only those columns.

|Phase|13814 left grasp|13815 right grasp|Own256 / change|
|---|---|---|---|
|Approach/precontact|350–420 EEFx.511–.516,y.174; torso1.19→1.37 lowersz.561→.481; armq4~−1.17 stays bent|300–370 EEFx.387→.442,y−.33→−.303; q4−.595→−.79, then stable|Ownlargearmreachx.578 atlowcrouch straightenedq4−.401 andq2nearbound; stage nearer measured body before lowering|
|Contact/descent|430–490 torso1.381→1.512,EEFz.478→.408, q4~−1.17; wrist motor visually centered/symmetric between pads|380–440 torso1.056→1.266,EEFz.511→.413, q4~−.804; wrist motor centered with nozzle nearly horizontal|Ownvacuum/nozzle diagonal inwrist; inherited globalcloseaxis may misalign with tool width. Measure foot/motor orientation, align closing axis, then lower incrementally while retaining centered silhouette. Topheight alone insufficient|
|Closure|500 gripcommand−1 after stableopen precontact; measuredfingers.045/.049 then.044/.049|450 gripcommand−1; measured.043/.050 then.041/.050|Ownzero/zero twice; no retainedliftproof. Do not rotate nearobject after emptyclose; withdraw clearly first|
|Object-changing lift|520–530 EEFz.420 from.409, heldbody moves withhand; theny.177→.074 presentation|480–530 EEFz.417→.455 withsamegrip, torso/armadaptation|Use small lift after asymmetric aperture plus visible motor retention; no genericfinger aperture success claim|
|Release/nextannotation|No griprelease; inward presentation precedes switch|No griprelease; otherhand rises for switch|Do not pursue switch without retainedlift; recovery poses are not established method|

Changed next retry: yaw-align jaw closing direction to observed nozzle lateral axis (not inherited BODYyleft); nearer bent-arm staging and small torso-led descent preserving wrist centering. Save precontact snapshot in practice so failed local alignment can be compared without destroying the upright start. These are hypotheses pending test; not packaged as proven.

## Historical TRAIN188 hold — superseded by matched TRAIN256 READY handoff989

Lead840 accepts substantive coverage upgrade and forbids same-layout repetition. `PRACTICE-HOLD` written/read-verified. Following success handoff838/839 but before hold840 arrived, restored `train188-powered-preclean-002` into `practice-restore-train188-powered-preclean-002-a7a5cc3ffbb4460ca48d39bbc33227cc`. **Zero subsequent motor calls**; admin_finished on hold, inherited721ticks/24.033333sim s/Q0, wall128.741430491. Aborted preclean comparison, not new task failure. Full-reset002 itself never restored and its Q1 result is unchanged. No active attempt; native world retained; same session preserved.

## TRAIN188 practice002 — tested coverage correction and short sweep

[Detailed procedure and public evidence](examples/coverage-and-forward-sweep.md). Fresh full reset, visible retained pickup~9.2cm, measured backward/downpress gavegreen012; savedpoweredpreclean snapshot, no restore. New nozzle calibration: atcarryTCPz.50, headtop.084–.089; lowerdesired.45 attained.455, headtop.040–.046 andfloor−.005. Released slight residual via measuredq, shortbaseforward.08–.12m, liftbackward-left`.43,.30,.54` to reveal swept pixels. Three bed patches treated; nativefalse1488. Crucially, explicit room coverage found **two additional visible dirt particles near the starting footprint**: afterback.35/yaw90 fourth`.590,.135,-.005`, treated thenfalse1800; after changed viewpoint andback.40 fifth`.627,-.350,-.005`, raisedlateralalignment, lower/forward.10/reveal gavetrue2784. No baseguards. Finishsuccess92.8sim/618.780837331wall, within3617ticktarget. Snapshotneverrestored, not first-attempt/no-feedback evidence.

**Strongest supported improvement is coverage, not claimed contact-height causality.** Single-origin rotations and nozzle occlusions hid near-body patches; translating through known clear floor then backing exposed fifth. Neither three nor five is a universal count. First188Q0 remains untouched. Forward sweep matches human measured/recorded pattern but was not isolated in a causal ablation. Finalreceipt`receipt_01792178271374669000_b0af805934a9446ea19425cc53692cbe.json` underpractice002. No active attempt afterfinish.

## Post-TRAIN188 failure: dense cleaning comparison (before retry)

Re-read pinned13814 cleaning sheet2 (860–930) and13815 sheets2–3 (860–1010), head+both wrists every10frames. Extracted measuredstate rowRGB−1 and recorded23Daction rowRGB−2 densely820–1030; only these public columns, no reward/termination. Same cleaning annotation plus neighboring approach and departure; contact labels are not sensors.

|Phase|Human13814|Human13815|Own188 difference / changed retry|
|---|---|---|---|
|Approach/precontact|820–840 rotates at~.30rad/s, stable heldL EEF`.478,.074,.415`; bodyactionyaw.30|820forward.262m/s;830 lateral.256;840–880 mixedbase approach; R EEFz.425–.427|Raised carryz.50 is useful for clearance, but does not calibrate suction-head contact|
|Cleaning/contact interval|850stop;860–870 forward.262m/s with commandedbase.35×.75, armnearconstantz.415; lowerbody retained|910stop;920–980 torso progressively lowers1.42→1.461,EEFz.431→.416; armcommandq4−1.18→−1.21; RGB head/nozzle moves down relativefloor|Own fixed lowerTCPz.430, purely vertical down/up, may not put underside atfloor. Need fresh nozzle/floor height and small forward sweep after actual lowering; no force claim|
|Object-changing movement|860–870 shortforward sweep whilelower, then880–950turn−.30rad/s; retainedgrip−1|1020forward.262m/s (recorded.35),1030forward+turn.262; new lowerposturez.417 retained|Add boundedforward motion with calibrated lowerhead rather than assuming point dip cleans patch|
|Release/departure|No griprelease: armstable, base turns/routes nextpatch|No griprelease: stillclosed, newbase motion|Lift/retract and deliberately reveal original patch pixels; current nozzle occlusion was mistaken for disappearance|

Changes for next practice: measure actual headtop/floor height, lower in small increments until visually floor-level without sustained lag, then short forward sweep. Reveal each patch before leaving; practice feedback allowed but not substitute for public geometry. No pre-segment snapshot exists because first attempt prohibited snapshots; next authorized reset will save one after reacquisition/activation. These are hypotheses, not proven corrections. First188failure remains immutable checkpoint evidence.

## Historical TRAIN20 current state

**HELD after completed008 per lead msg_000741 / Atin: no further same-instance resets.** Original session/world preserved; no worker shutdown. Wait for lead-staged unused-instance NEXT and explicit matching handoff. First next-instance attempt uses frozen NOTES/procedure only, no restore or intermediate feedback; feedback at finish. No infrastructure blocker.

Assigned world only: `vacuuming_floors-train020`, controller26efe4a/protocol6, sourcea32648a. Ordinary `import sim_client as s` uses launch binding; do not override PYTHONPATH or reuse donor bindings/budget wrapper. Donor patio world is historical and untouched after reassignment.

**First native whole-task success: `vacuum-train020-002`, step1256/41.8667sim s**, within3617tick official comparison budget; finish reconfirmed at1338ticks/44.6sim s and633.6728wall s. No restores. Native sole `not covered(floor,dust)` true/Q1. One success, not repeatability; no wall-time parity claim. [Evidence and technique](examples/native-completion.md).

Attempt001 ended incomplete1897ticks/63.2333sim s,1522.3659wall s,false/Q0. Attempt002 used lower-body grip, both arms crouch-clear, human-informed switch presentation, and changed approach after one baseguard. Repeat003 FAILED at507ticks/16.9sim s,416.6929wall s: vacuum tipped during copied lower-body pickup and fallen-tool recovery IK failed. Nativefalse/Q0, admin_finished, no restores. Dense cross-demo pickup comparison below. No runtime hold/blocker. **004 SUCCESS at928ticks/30.9333sim s,429.5059wall s throughfinish**, Q1. Changed measured intermediate-crouch pickup and clearance-first route worked without baseguards. [Exact evidence/technique](examples/measured-pickup-and-cleaning.md). **005 independent repeat SUCCESS at927ticks/30.9sim s,443.924277wall s throughfinish**, Q1; 006 adapted repeat also SUCCESS1026ticks/34.2sim s,468.501967wall s; 007 also SUCCESS922ticks/30.7333sim s,455.247186wall s; 008 SUCCESS933ticks/31.1sim s,321.437315wall s; no active attempt after008finish. Revised measured method succeeded004/005/007, plus006 with changed pickup geometry and switch adaptation; six successes overall002/004/005/006/007/008 with intervening003failure. Ready to freeze as a TRAIN20 development technique, not held-out generalization or a fixed executable policy. Further same-instance practice is now disallowed; use EVAL-PROCEDURE.md for lead-staged distinct-instance test. Latest lead rule: no per-attempt/substep messages unless ready-to-freeze/ship, completed full assigned deliverable/eval or action-needed blocker. Official3617 ticks (~120.567s) remains comparison meter, not a new unbounded-practice termination gate.

Public cache: `<observation-cache>/vacuuming_floors-train020-p6-a98736/`, attempt-qualified001/002. Historical001 details below are not the active world state. Lead reporting: only meaningful whole-task readiness, external/runtime blockers or help decisions; routine findings stay here/examples.

## Attempt008 — final same-instance attempt, then user-directed hold

Already active when leadmsg_000741 arrived; completed without another reset. Original measured pickup, visible retention, same geometry-derived cleaning route. Tested removing intermediateRq620: closeR while rollingL10°, then directRq670 succeeded. Not demonstrably faster: stage ended12.27sim s; wholeattempt31.1sim s. Freshbutton `.577151,.087895,.961119`; beforepress `.573225,.087046,.962973`; greenobs012. Releasedpreload/withdrew. Central/shelf depth matched007; clearanceleft.20 thenforward.58, no baseguards. Final lower/lift, finish-only feedback (no intermediate feedback queried008) true/Q1 at933ticks/31.1sim s,321.437315191wall s. Finalreceipt `receipt_01792174960069608000_1498ef955c09491c872fab96f22fbcb9.json`; endpointwall309.9. Finalact reportsreached but pendingL/q4lag+.017; not zero residual.

Local no-motion API errors preserved: reset keyword `attempt_id` invalid (correct `attempt_name`); arm `tol` invalid and top-level `tol` invalid (correct top-level `position_tol=.002`). Corrected beforedispatch; no successful action replay. Baseline004/005 still preferred freeze reference; direct staging008 is one successful variant, not a speed result. Held now, original world/session intact, no next repeat/restore/shutdown. Cross-instance procedure frozen in EVAL-PROCEDURE.md.

## Attempt007 — measured method repeat success

Original reset, no restores. Initial yaw5scap attained1.538rad; fresh exposed motor geometry matched004/005. Intermediate crouch/vertical lower `.505,.175,.405`, measured-q release, separate close, visible retained lift. Lroll10°, Rq620→close→q670; switch depth `.575521,.088903,.963090`, prestage `.578,.055,.960`, boundedpress `.576,.090,.960`. Green visibly confirmed onwithdrawalobs013; released measuredLq and withdrewR without forcing press convergence. Restoredroll−10° and tucked freearm. Initiallower `.53,.30,.425`, lift `.53,.18,.49`. Fresh central`.986545,-.256224,-.005092`; baseforward.40/right.44, lower/lift; false636. Freshshelf `1.208667,-.368634,-.005058`; yaw−35, postturn `1.218478,.339134,-.005045`; clearanceleft.20 thenforward.58. No baseguards.

Final lower `.55,.16,.425` alone remainedfalse891. Final lift/retract `.50,.26,.50` changed native predicate totrue/Q1 at922ticks/30.733333sim s,obs024wall445.7; finish reconfirmed455.247186188wall s. Act reportedreached but leftpending/trackinglag+.019 atendpoint; no claim of zero residual and no extra forcing. Cache finalreceipt `receipt_01792174580901635000_46c53799f43d43c1af31376709412049.json` under007. This adds observed TRAIN20 repeat evidence, not held-out or executable-policy qualification. Final lift remains necessary in tested sequence; lower-only wasfalse on006/007. No runtimehold, no routineleadmessage.

## Attempt006 — completed success, switch adaptation study

Original reset. Shorter4s initialyaw attained1.508rad; measured pickup adjustedleft2cm, reached lowerTCP`.504,.194,.406`, retained. Different retained presentation put switch~`.544,.110,.981`; previous lateral-only geometry no longer adequate. +4°toolroll and small sidepress did not change red; released preload and withdrew before studying, not runtimehold.

Re-read dense3camera switch RGB13814 frames640–790 and13815 530–680 every10frames, plus alignedproprio at9/10frames respectively. Relevant neighboring approach/release included; human EEF not identical calibratedTCP.

|Segment|13814 right pressing hand|13815 left pressing hand|Own006 / changed retry|
|---|---|---|---|
|Approach|EEF640`.691,.004,.825`→670`.629,.023,.883`,closed|530`.631,-.171,.843`→570`.556,-.202,.963`,open thenclose590|Fresh switch differs from004; right staging q2nearupper; don't replayold coordinates|
|Precontact/contact change|700`.583,.031,.898`→720`.560,.035,.917`; mainlybackward2.3cm+up1.9cm, not lateral-only|590`.514,-.200,.998`→640`.476,-.206,1.004`; mainlybackward3.8cm with small lateral/height|Ownsidepress constrained by shaft andq2; change to forward/high staging then backward/down approach to exposed button face|
|Visible activation|red720→green730,EEF`.562,.029,.919`|red640→green650,EEF`.475,-.208,.997`,slightdown7mm|Ownred persists; lag is not proof ofbuttoncontact|
|Release|740forward2.4cm;750forward/open;780lowered|670forward7.5cm;680forward/open|Withdraw/release measured preload, keepretainedvacuum; newpress finite and inspectcolor|

006 changed retry succeeded: right precontact `[.58,.09,1.01]`, human-informed fingers `[-.095,.952,.291]`,close `[-.992,-.115,.055]`; fresh red`.5462,.1024,.9810`; backward/downpress `[.548,.095,.978]`,tol.002,seconds.7 produced GREENobs017 despite blocked pose. Withdrewforward/right and held measuredLq, then raisedcarry `.53,.18,.49`; tucked freehand. Cleaninglowerz.41 (grip1.5cm lower than004) and lift. Freshcentral`.994,-.223,-.005`, baseforward.4/right.4. Shelf afteryaw−35 `1.245,.373,-.005`; clearanceleft.22 attained~.215 at2scap, thenforward.60. Native lower-onlyfalse991; lift/retract `.50,.26,.49` changed totrue1026 atobs029. Therefore do not delete final lift based on assumption lower alone suffices. No baseguards/no restores. Finalreceipt `receipt_01792174061671330000_ccd5e5fc005d4d8e9f64cce9a2d72b1d.json`, endpointwall451.0, finish468.501966892wall/34.2sim. Finalpose residual/lag remains, not pose-achieved. Original004/005 frozen-candidate evidence unchanged;006 is adaptive variant, not identical-policy repeat.

## Attempt005 — independent repeat of improved method

Original reset, no restore. Fresh wrist motor depth matched004, so used intermediate crouch and vertical descent; released measured-q preload before separate close and verified visible retention on lift. Fresh switch staging depth `[.57557,.08880,.96312]`, prepress `[.57193,.08782,.96346]`; bounded lateral press produced greenobs012 despite pose timeout. Released preload and withdrew. Tucked free arm before travel, raised tool between cleaning contacts, remeasured central/shelf dust. Central feedbackfalse636; shelf clearance-left.20 thenforward.58 reached without baseguards. Final lower/liftobs024 verified native true/Q1 at927, finish reconfirmed30.9sim/443.924276974wall seconds. Final lift did not achieve pose (q4lag−.044, actualTCP`.489,.263,.482`); did not force it. Erroneous `admin_feedback()` raised local AttributeError after successfulobs019 action; corrected to documented `practice_feedback()`, without replaying the action. Cache finalreceipt `receipt_01792173544931351000_0ff08a7bd9724ee581c92c314ad92037.json` under005. Endpointwall433.8s; actual success onset may be earlier. No wall-time parity claim.

## First acquisition

- Obs001 facing desk.002 yaw+90°, both grips explicitly open; vacuum upright ahead.
-003 baseforward.25/right.22 aligns shaft. Public head depth shaft `[.608,.253,.809]`; upper loop `[.545,.248,.919]`; red upper switch~`[.600,.251,.937]` before lift.
-004 left stage `[.44,.255,.82]`, fingersforward `[1,0,0]`,closeleft `[0,1,0]`,open. Measuredq `[.47970,.00670,.00332,-1.53082,.00883,-.56467,-.00424]`.
-005 insert `[.619,.255,.82]` +close. Pose reached1.7mm residual but closure deferred; resultstalled, fingersstillopen. Inspected prerequisite gate; not interpreted as grasp.
-006 separate close issued: aperture.0412m, shaft between fingers.007 lift8cm: shaft/head visibly moved, retained through010. TCP~`[.618,.255,.899]`,q `[.01070,.00895,.00086,-1.55973,.00848,-.06476,.00008]`; current commandedq `[.01049,.00896,.00079,-1.56043,.00901,-.06473,-.00088]`.
-After lift red switch headpixel(193,484) measured `[.6141,.2656,1.0212]`. Candidate geometry only; fresh depth required after changes.

## Switch approach failures / recovery

-008 right `[.55,.02,1.12]`, fingersdown/closeleft, timeout5s. Bad IK branch, target badly missed: actual `[.414,-.724,1.409]`,q4upper/q7lower endpoint limits. Close deferred; right remained open. No repeated goal.
-009 joint-space forward stage mirrored from measured left004 recovered to `[.44,-.255,.819]`: q `[.4797,-.0067,-.00332,-1.53082,-.00883,-.56467,.00424]`. Robot goal reached; close still deferred; no object contact claim.
-010 right forward-facing target `[.62,-.05,1.02]` nearly reached but q2upper.1645 limited inward travel: actual `[.621,-.056,1.016]`, residual~6.9mm; right pending. Measuredq `[-.21367,.16450,.64512,-1.70068,.04470,.37332,-.64913]`, fingersstillopen. No actual switch contact yet. Left vacuum retained, no substantial arm lag; effort is not force proof.
-Hypothesis (untested): upright high shaft grasp leaves switch high and far left for right arm. Human may tilt/lower vacuum, use different grip or presentation. Must compare actual demos rather than keep retrying IK.

## Human study queued

`examples/fetch-human-switch.py` downloads pinned public metadata/frame shards and bounded three-camera spans, cache outside Workbench at `<demo-samples>/vacuuming_floors/`.

-13814/TRAIN20 frames240–810 includes approach, pickup267–570, switch570–780, next movement780–850.
-13815/TRAIN21 frames210–810 includes approach, pickup240–480, switch480–780, next movement780–875.
-Every10frames (~.333s), original head/left/right plus contact sheets. RGBn uses positions/joints rown−1, velocities/actionsn−2. Labels are not contact sensors; EEF geometry is not calibrated live TCP.
-Background job `bg-fbde1fe1` succeeded. Reviewed13814 contact sheets3–7 (pickup400–550, approach560–670, contact candidate680–720, red→green720–730, withdrawal750–790) and13815 sheets3,5–7 (pickup370–440, approach530–580, contact590–640, green650, withdrawal670–760), all three views every10frames. Extracted aligned state at six representative frames in each episode.

### Human-vs-own switch comparison

|Feature|13814/TRAIN20|13815/TRAIN21|Own001 / change|
|---|---|---|---|
|Acquisition|Left grips lower motor-body area, fingers angledforward/down; EEF at570 `[.475,.074,.411]`, aperture~.093m|Right lower body, EEF480 `[.443,-.317,.417]`, aperture~.091m|Left upper shaft `[.618,.255,.899]`, gap.041m. Retained but presents switch higher/fartherleft. EEF definitions differ: not exact calibrated offset comparisons.|
|Torso during switch|`[1.512,-2.339,-.868,0]`|`[1.267,-1.891,-.761,0]`|`[1.025,-1.45,-.47,0]`; more upright.|
|Press approach|Right fingers point left and slightlyup; at720 fingeraxis `[-.095,.952,.291]`, closeaxis `[-.992,-.115,.055]`, closed|Left pointsright/up, at610 `[.047,-.884,.465]`, close `[.772,-.263,-.578]`, closed|Wrong initial downward approach, then forward-only approach hit limits. Change right orientation to left/up side approach, not another downward goal.|
|Presentation and indicator|Vacuum mostlyupright, nearcentre; right EEF720 `[.560,.035,.917]`, red720→green730|Vacuum tilted/laterally oriented; left EEF650 `[.475,-.208,.997]`, green650|Currentred~`[.614,.266,1.021]`; remeasure beforecontact. Can alter presentation if lateral reach remains blocked.|
|Release|Right withdraws andopens whileleft retains|Left withdraws andopens whileright retains|After visiblegreen withdraw without repressing. `observe` adds no dwell.|

These are public human RGB/state, not contact proof or directly replayable robot goals. Next candidate: retain existing vacuum grasp, change right-hand finger/closing axes to the demonstrated side approach, establish precontact geometry, then a bounded finger press. No human reward/termination fields used.

## Powered switch and first cleaning evidence

-011–025: changed right finger approach to human-informed lateral orientation, moved held vacuum nearer centre, tilted left roll20°, released preload with measuredq; final right fingers `[.16,.98,.15]`, close `[-.99,.15,.06]`, target `[.647,.080,.990]`, position_tol.002/seconds.7. Green indicator at025. Withdrew without repressing, returned left tool upright. Right parked/open q=zeros.
-028–030: torso lowered to `[1.25,-1.861,-.75,0]`; initial near-floor travel dragged/tilted nozzle. Do not treat near-floor tool as freely carried.
-031 lift `[.75,.25,.98]`, fingersforward/closeleft. Nozzle top~`.206m`; first dust `[.663,.243,-.005]`.032 lower `[.64,.25,.82]`,033 lift: first patch absent in reveal. Native stillfalse.
-034 diagonal forward.61/right.54 stalled by base velocity mismatch. Changed035 forward-only.4 reached.036 right.4 still guarded.037 yaw−35 achieved only~11.5° then guard (zero commanded translation, accumulated onboard translation error~.0052m). No force/contact proof; did not force through.
-038 inward left `[.85,.05,.82]` hit q2lower;039 retract `[.65,.25,.98]` diverged to q4limit.040 recovered using known033 raised joint configuration below.041 smaller yaw−20 after recovery reached~9° then translation guard; used attained heading instead of further turn retries.
-042 shelf dust freshly~`[.904,.025,-.025]`; lower left `[.82,.15,.82]` reached,043 lifted using known raisedq. Dust visibly absent at prior353,585 location. Native043 false/Q0. Two local removals are not complete-floor success.

### Current useful pose, not an unconditional macro

Torso `[1.25,-1.861,-.75,0]`, rightq=zeros/open. Known raised left commandedq `[-.62075,.25872,-.29116,-1.73146,.41954,.53613,.37497]` gives approximately `[.75,.25,.98]`, but current gravity/oscillation yielded actual `[.750,.246,.965]`, q5lag−.034/q6lag−.046. Retained gap.0411. Nozzle clear enough for reveal; inspect fresh actual clearance before travel. These joints recovered from an IK branch failure, not a universally collision-free path.

Latest base odom `[.694,1.044,0]`, yaw1.162rad is integrated/drifting only. Facing door and white shelf. Last two patches absent; other floor areas remain unsearched. Latest receipt `receipt_01792170853726680000_068adffa9dc743cab0c05de25a1d3e1f.json` in current attempt cache. No reset/finish/restore performed.

## Human cleaning/navigation comparison after base-guard retries

Fetched `--cleaning` spans13814/780:1240 and13815/780:1760, stride10, aligned pose n−1. Reviewed13814 contact sheets1–5 and13815 sheets2,3,5–7 across floor approach/contact/departure, all3RGB views; extracted aligned poses at8frames/episode.

|Feature|13814|13815|Own / change|
|---|---|---|---|
|Carry grip|Lower body, left EEF~`[.475,.073,.414]` stable throughout790–1140|Lower body, right EEF~`[.51,-.23,.425]`850–1600|Upper shaft atTCP.75,.25,.98: longer forward envelope, larger lever. EEF/TCP offsets differ; no exact replay.|
|Torso|`[1.512,-2.339,-.868,0]`, crouched and stable|Progressively lower1.42→1.494, q2−2.17→−2.31|Own1.25/−1.861/−.75; tool held farther forward. Compare compact carry rather than force through guards.|
|Cleaning action|Mostly base approach/short turns with near-constant arm pose; floor patch approached then absent|Several lower/tilt adjustments900–1000, then mostlybase sweeps around bed|Own arm lower→lift effectively removes patches; preserve this while making navigation compact.|
|Evidence limits|RGB patch disappearance, not downloaded reward or termination|Same; another instance layout|No causal claim that posture alone explains native guard. Own guard sometimes trips on~5mm uncommanded translation duringyaw.|

044 open-room turn+65 attained~62°;045 continuation+50 guarded after3°. Bed corner depth in045 is~`[1.31,1.35,.375]`, outside current tool radius; nearby visible floor clear. Change candidate: compact known arm configuration and more upright torso for navigation, not unchanged retries. Human lower-body regrasp remains an alternative for a fresh attempt, not yet attempted.

## Repeat003 acquisition divergence and renewed dense human comparison

Fresh original reset003, native0false. Both arms staged forward before crouch; no torso obstruction. However, the copied002 target `[.55,.185,.39]` closed empty at006. Fresh depth showed motor surface 5–10cm farther forward. Reopened; 008 open insertion to.615 tipped vacuum away, so **do not continue blind coordinate replay**. Tool lay/leaned forward, public head motor samples~`[.90,.21,.187]`; no grasp established.009withdraw Cartesian goal diverged toq6upper,010knownstage recovered plusbaseforward.22.011pure-down and012oblique far-motor targets unreachable;013near-neck goal stillIK_stalled (desiredz.21, achieved.28). Finishedfalse at507ticks. No runtime blocker or hold; preserve failed recovery rather than silently discard it.

Re-read all3RGB contact sheets13814/2–4 and13815/2–3, every10frames, and aligned proprio each10frames across13814/320–570 and13815/290–510. These span approach, precontact, closure, pickup and next-segment presentation. Grip release is intentionally absent during pickup; both retain for switch.

|Phase|Human13814|Human13815|Own003 difference / correction|
|---|---|---|---|
|Approach|Open hands; torso gradually1.075→1.485; EEF.531,.18,.622→.505,.179,.423, x stable|Open right; EEF.387,−.329,.503→.44,−.315,.413|Abrupt final crouch plus forward insertion displaced tool. Need measured motor placement, not inherited coordinates.|
|Precontact|Wrist sees broad black motor bulb centered continuously; q6~.531, q7~.288|Motor bulb centered; q6−.126,q7−.011; different orientation works|At006 wrist sees narrow red cone, not bulb. x.549 TCP vs livebody.60–.65: behind target.|
|Closure|490 open→500 fingers.0447/.0491 atEEF.502,.18,.409|440open→450.0434/.05→460.0406/.05|006closed0/0, decisively empty. No lift/grasp claim.|
|Object-changing lift|500→530 EEFz.409→.420, retained aperture~.093m; then move inward|450→510 z.412→.434, retained~.091m|008 tool tipped ahead during open approach, not a retainedlift. Recover by withdrawing and approaching tilted motor from above, changing orientation to measured tool posture.|

## Transfer boundaries

Patio's short observed tool-to-patch moves and native-completion checks transfer conceptually, not its coordinates, primitive offsets, budget cap18106 or worker. Vacuum requires powered switch interaction and suction head placement; one remaining dust particle keeps native goal false. Preserve all failures; success and budget efficiency are separate claims. Use serial awaited public calls only, current user/STOP/cost guards intact.
