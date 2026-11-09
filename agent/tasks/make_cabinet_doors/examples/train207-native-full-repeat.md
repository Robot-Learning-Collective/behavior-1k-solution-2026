# TRAIN207 native-reset repeat — attached, released, withdrawn

`cabinet-train207-full-repeat-004` finished **attached=true/Q1, 2817 ticks / 93.9 simulated seconds / 1470.1196528680011 task-wall seconds**. Reset returned backend `setup_seconds=497.0953081710031`; this identical value recurs across resets and is **not independently measured reset-call latency**. Earlier wording that reset itself took497s was incorrect. Native task-wall above is unchanged. No snapshots/restores. This is the second consecutive studied, seen207, unbounded native-reset full-chain success after003; **not unseen generalization, budget-enforced evaluation, or a statistically established success rate**. Native meter5163 leaves2346ticks/78.2sim s. Opening/closing was neither needed nor attempted.

Evidence: [finish](../train207-full-repeat-004-finish.json), [first training feedback after seating](../train207-full-repeat-004-seating-feedback.json), all69 sequential action records in `../control-action-results.jsonl`,70 endpoints in own cache namespace `cabinet-run-023-p6-d689c6`. Sum of action steps2817; every action has execution_uncertain=false/fault=null.63 reached and6 ordinary stalled returns; no base-guard stop in this repeat. Both hands open; no pending motion at endpoint70; lifecycle closed. First native true was sampled at2797ticks, exact transition unknown.

## Adapted full chain

|Endpoint|Ticks / sim s|Observed phase|
|---|---:|---|
|14|873 /29.1|Near-edge acquisition, verified lift, retained carry to cabinet|
|23|1266 /42.2|Far-rim bounded draws tipped cabinet; empty pads withdrew to let it settle|
|32|1670 /55.6667|Fresh long-rim pinch, partial4cm lift, measured-q cancellation; backward40cm then20cm draw, supported release|
|42|2051 /68.3667|Left clearance15cm and two−45° turns; staged raised alternate-wrist path toward handle-face-up|
|47|2194 /73.1333|Broad ottoman support, canceled descent preload, released for regrasp|
|53|2359 /78.6333|Fresh downward handle insertion; inset near-limit wrist before closing|
|56|2399 /79.9667|12mm then8cm retention probes visibly carried panel|
|60|2535 /84.5|Raised65/90cm, staged negative yaw toward tracked mating-end relation|
|63|2680 /89.3333|Back-left20cm each, lowered60/40cm for current rim/corner measurements|
|68|2797 /93.2333|Corrected yaw/translation,35cm pre-seat then bounded28cm target; native true/Q1|
|70|2817 /93.9|Canceled measured preload, opened, withdrew8cm; native finish still true/Q1|

## Substantive differences and corrections

- Shortened second cabinet draw to20cm instead of requesting50cm into the prior obstruction. Total requested relocation60cm, then released while floor-supported before turning. Partial rim lift did not establish a whole-object airborne carry. This repeat had no base guard stop, not proof the route is collision-free.
- Used updated wrist transition target1.0 instead of1.0272. For temporary support, rejected an offline candidate with only.01rad margin and used another with.03rad. FK/IK remains not collision checking.
- Downward handle insertion left wrist joint6 at−1.03645rad, only.001rad margin. Changed that command to−1.0 BEFORE grasp; achieved.038rad minimum margin, with TCP still at fresh visible bar. Then closed and verified visible lift. Aperture~.006m alone was not retention evidence.
- Retained handle-grasp rotation began with the prior~57° staged clearance poses, but **fresh RGBD showed an additional~7° negative yaw was needed**. Relational mating-end tracking, not a universal180° or57° macro.
- Initial apparent far corner in left camera was only a partially occluded rim point. An initial+[.012fwd,.12left] base adjustment exposed the actual short-end corners in head camera; those independently required+[.067fwd,−.07left]. Corrected while panel was still at40cm, rather than trying to seat a mislabeled feature.
- After new yaw correction, measured head panel far corner(.674,.292,.389), opposite corner(.509,.113,.398); actual exposed corresponding rim points approximately(.745,.222,.243),(.572,.045,.248). Their similar XY differences motivated the correction. All these are instance/endpoint-specific BODY coordinates, not future targets.
-35cm pre-seat and28cm seating were recomputed for new closing axis[-.645638,−.763643,0], fingers down. At native true, modest joint lag was canceled at measured q; no pressure escalation or postrelease registration push.

## Exact changed seating poses and endpoint provenance

These commands describe this completed practice only; do not execute against the finished lifecycle or substitute them for new-world geometry. All69 exact sequential `requested` commands, their before/after endpoint IDs and actual robot states remain in `../control-action-results.jsonl`, filtered by `attempt_id == cabinet-train207-full-repeat-004`.

```python
# obs064: seven-degree fresh yaw correction, torso held at [1.75,-2.65,-1.2,0]
s.act(left={'q':[-1.70053,1.05618,-2.2826,-1.46476,-1.91106,-.67936,.21587]},seconds=1)
# obs065: initially misidentified partial-rim point; NOT a recommended final alignment
s.act(base={'fwd':.012,'left':.12},seconds=2)
# obs066: newly exposed actual short-end corner pairs corrected the above
s.act(base={'fwd':.067,'left':-.07},seconds=2)
# obs067: current orientation, pre-seat
s.act(torso={'q':[1.744,-2.75,-1.3,0]},left={'q':[-1.6121,.95214,-2.27261,-1.3038,-1.89189,-.61188,.25731]},seconds=2)
# obs068: current orientation, bounded seating; native training feedback then true
s.act(left={'q':[-1.39744,.80177,-2.25313,-1.03512,-1.85718,-.46038,.28196]},seconds=1.5)
# obs069: measured-q cancellation + release, not deeper pushing
s.act(left={'q':[-1.40242,.80038,-2.25595,-1.03335,-1.87641,-.48324,.28031],'grip':1},seconds=1)
# obs070: free withdrawal
s.act(left={'up':.08},seconds=1)
```

Cache root: `<observation-cache>/cabinet-run-023-p6-d689c6/cabinet-train207-full-repeat-004/`. Each endpoint's `obs_NNNN_depth.npz` and paired public observation/receipt artifacts preserve RGBD/state. Key endpoints:051 pre-handle,052 insertion,053 wrist inset,054 close,055/056 retention probes;063 prealignment,065 exposed actual corners,067 pre-seat,068 attachment,069 release,070 withdrawal. Final receipt `receipt_01792186178449941000_75ca80ca1a5b405ba4e39cdffd989f74.json`. Integrated base odometry is uncalibrated, not absolute scene pose.

## Immutable boundaries

First207 remains false/Q0,5277ticks, over5163 by114. Registration002 remains false/Q0,3782ticks. Restored reversal4383true remains a601-tick continuation, not a fresh full chain.0032757true remains the first native-reset full-chain success;0042817true is a separate repeat. Neither success retrospectively repairs or diagnoses the retired TRAIN10 attach-joint crash. No old worker, backend or private object/mating-frame truth was used.

Astra already reported shipping003 as `bc399239984a68642f1a24e24834512cd4f0ea7b` with22forks/16CPU tests/1147-file keyscan passing. That packaging report is separate from native004 evidence; packaging was not held on this repeat. No requirement for another trial is inferred from this document.
