# First unseen TRAIN291 — native attachment success

`cabinet-train291-first-001` finished **attached=true/Q1,3676ticks/122.53333333333333sim s/1921.196430128999task-wall s**. Independently measured reset RPC1.994817791s. The5163tick practice meter had1487ticks remaining; this was unbounded practice, not evaluator-enforced-budget qualification. One unseen layout success is not a reliability estimate. First207 false5277ticks remains unchanged.

## Integrity and evidence

- Operator msg976 matched handoff: sourceff37d40, client next-fast-1792194461408122000, cachecabinet-run-023-p6-4982d6. Same session/context/NOTES; old207 retired.
- No demos, snapshots/restores or intermediate privileged feedback. Sole native feedback was terminal `admin_finish`.
- `../heldout-train291-first-001-reset.json`, `../heldout-train291-first-001-finish.json`, current-attempt rows in `../control-action-results.jsonl` and own cached RGBD/receipts.
-82action-log rows:81motor calls(63reached,13bounded timeouts,5ordinary stalls), all execution-certain/fault-null; one local zero-tick base-key rejection (`forward` instead of `fwd`). Total3676ticks,82public endpoints including initial observation.
- No backend/worker changes, transport uncertainty or reset retry. Finish closes291. `PRACTICE-HOLD=WAIT_NEXT_INSTANCE` written/read-verified; no further291 control/reset.

## Actual chain

1. **Exposed-edge acquisition:** initial positive wrist limit and shallow insertion miss were canceled. Open-hand withdrawal then8cm base advance shortened reach; fresh edge~[.5543,.1745,.4513]. Achieved TCP~[.551,.175,.443], closed, then independent14cm lift visibly retained the panel. Canceled/inset shoulder/wrist limits after lift, raised torso for carry.
2. **Tipping correction:** early far-rim backward/downward draws did not tip the cabinet; depth-plane slopes remained~zero. Canceled preload instead of stronger retries. Own saved wrist crops showed the actual shelf opening. Changed side/workspace and tucked/raised the panel. Deep torso plus inward open-right-pad engagement of the upper opening, then bounded diagonal arm/base pushes produced real tilt. Atobs056 fitted top-plane slope[-.188,-.219]; withdrawal atobs059 left cabinet visibly open-face-up. Earlier assumed right joint bounds were corrected from live endpoint metadata; failed IK candidates were not treated as global unreachability.
3. **Retained-panel reorientation:** raised torso and four freshly solved joint stages brought fingers forward/closing axis up, with panel handle face upper. No support/handle regrasp ultimately occurred. TCP-only sweep samples were not collision certification.
4. **Placement-path recovery:** online coupled torso/Cartesian60cm descent developed large wrist lag and panel/cabinet interference. Canceled with measured q; the first.3s cancellation only slewed partway, so a subsequent bounded cancellation completed unloading. Recovered previously solved75cm horizontal pose. Offline IK at matched crouched torsos then provided feasible60/35/26cm placement without the bad straight-elbow path. The final torso1.8 target stalled near measured1.736; accepted measured torso and solved arm-only descent rather than forcing it.
5. **Fresh registration:**402 public-depth rim samples fit cabinet long-axis49.5degrees. Base yaw and measured corner XY correction aligned the rectangular outlines; compensation of observed panel roll flattened it. Right-arm withdrawal displaced the neighboring chair, so this was not collision-free navigation. Final panel held level over broad support atobs076/3554ticks.
6. **Release and terminal decision:** opened atobs077/3569ticks. Up/back edge withdrawal shifted the panel/cabinet; lower/back recovery then stalled near-body and was canceled. Sideways open-pad escape atobs082/3676ticks showed panel and cabinet moving together. Rather than execute the previously conjectured handle regrasp/180-degree reversal, finished for native verification: **attached=true**. Exact attachment-transition tick is unknown; there was no intermediate feedback.

## Corrections to carry forward

- **Do not prescribe180degrees from an assumed top/bottom mapping.** I initially inferred a reversal was needed and planned a temporary support/handle regrasp. That inference was wrong for this successful direct-edge trajectory. No180 reversal or handle regrasp was executed. Track actual geometry; preserve terminal success rather than applying unnecessary manipulation. Studied207's required reversal is not universal.
- **Supported release can be decisive; held appearance is not terminal proof.** Native result verifies final attachment, not the exact transition or necessity of subsequent withdrawal motions.
- **Open-pad withdrawal can still disturb the assembly.** An upward component under an edge can lift/drag it; broad opening and command acknowledgment do not guarantee collision-free separation. These contacts are inferred from motion, not force/held truth.
- **A cancellation needs enough slew time.** For a.68rad command/measured lag at.025rad/tick, a.3s cap cannot complete unloading. Inspect returned command and measured q, not only a `reached` per-arm label.
- **Use actual opening and a measured plane change to evaluate tipping.** Several earlier draws merely held a flat cabinet. Repositioning solved that; stronger pressure was not the successful change.
- **Workspace and torso solve matter.** Correct live bounds, medial placement, matched torso/arm endpoint solves and measured torso acceptance avoided infeasible limits. Offline IK remains collision-blind.

No further291 reset. Await unused-instance operator handoff with this same context and notes; preserve all older failures and the unresolved TRAIN10 crash history.
