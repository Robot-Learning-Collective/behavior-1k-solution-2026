# TRAIN43 seen-instance chair-exposure test

Attempt `patio-train43-coverage002`, same native Pi session936e562a. One fresh world reset after required cross-demo7217/7218 RGB/state/action study (NOTES comparison table); no restore used in this prefix. First-attempt `patio-speed-train43-zero001` Q0/8433ticks and unintended bench tilt remain separate.

## Demonstrated local capability, not whole-task success

Public RGB obs021–026 shows near chair rotate and then translate away, remaining upright in sampled endpoints. The empty right hand was open; broom retained left. After withdrawal026 a previously chair-occluded orange patch appears to the chair's right. Fresh depth localized it; stroke037 then withdrawal038 visibly removed that orange patch while adjacent tan marks remained. Native practice feedback at039/3484ticks/116.133s is **success=false/Q0**; other visible orange remains elsewhere. No native count/location of remaining mud, whole-task completion, independent repeat or generalization claim.

### Reconstructable sequence

- Preapproach snapshot `train43-chair-preapproach-002` at017. Pickup001–014 used fresh shaft depth, separate open approach/insertion/closure/lift.
- At018 approached chair from front, torso initially upright.019 mid-torso change produced left q6 lag~.587.020 measured release/backoff cleared it. This is NOT a clean collision-free approach.
-021 requested right TCP[.5,−.35,.39], fingers forward; actual[.451,−.321,.602], q6 limit.022 downward fingers requested[.60,−.35,.40], actual[.494,−.326,.550]. Chair visibly rotated during this arm path. Neither Cartesian request reached; do not replay them as reliable push poses.
-023 replaced right request with measured joints and moved broom aside left TCP≈[.404,.449,.799]. Torso fixed[1.025,−1.45,−.47,0].
-024/025 **bounded base advances .3m then .4m**, measured open right TCP≈[.493,−.326,.550] throughout, no significant arm lag. Chair moves with robot relative to background; stays upright. Do not infer precise chair displacement from odometry.
-026 measured right release and.7m retreat. Right grip remained open; left finger sum~32.8mm and broom visible. Newly exposed orange at head(u529,v489), BODY[1.6114,−.9987,−.0050]. This is a changed-view exposure, not scored cleanliness.
-027–032 clearance/recovery detour: diagonal approach toward boundary plus inward-hand staging caused right q6 lag~−.617 and visibly tilted view. Measured release/inward retreat reduced it; alternate right posture still q3 lag~−.461. Low torso relieved arm lag, but boundary turn031 stalled with torso q1~1.833. Measured torso reseed rejected pre-dispatch as outside limits.032 valid raised torso + measured arms + inward retreat reached. Preserve these failures; no claim the overall route is efficient/safe/universal.
-033–036 recovered from interior stance: raised compaction, rightward20deg turn, .4m advance, separately stage arms at **raised** torso, then lower. No stale blocked command carried into the stroke.
-037 orange freshly sampled at head(u216,v330), BODY[1.0593,.3971,−.0466]. Requested left TCP[.6993,.4971,.005], downward fingers/close[.31,.95,0]. Actual[.684,.491,.027], q6 lag~−.063; not achieved-height proof.038 lifted/withdrew to low-reveal joints; orange is absent in its now-exposed footprint, adjacent tan unchanged.039 raised and backed.3m, preserving local visual result from changed view.
- Feedback039: native Q0/false at3484ticks. Postsegment snapshot `train43-chair-exposed-cleared-002`; active attempt continues, no restore and no finish at this checkpoint.

## Transferable procedure vs brittle details

1. Viewpoint-only inspection first. If chair hides a needed floor region, use the empty open hand to expose it while keeping held broom spatially separate.
2. Establish an **achieved** mid-height hand pose; do not demand unreachable low/forward orientations. Fixed torso during short horizontal pushes, inspect after each, stop before another chair/boundary.
3. Release preload, withdraw, acquire current RGBD of vacated footprint. Only then target newly visible orange; after stroke lift/withdraw and verify footprint.
4. Raised-stage→lower transition is distinct from the mid push torso: the same inward-hand preset collided at mid torso, but reached at raised torso and then lowered normally. Presets are not universal clearance guarantees.
5. Avoid outer-boundary lateral shortcuts. This test recovered them, not validated them. Whole-body/tool clearance remains a major limitation.

## Evidence locations

Cache `<observation-cache>/patio-run-027-p6-cabfd1/patio-train43-coverage002/`: `obs_0021_raw.jpg` through `obs_0039_raw.jpg` plus original depth/state receipts. Per-action records: run `control-action-results.jsonl` filtered by exact attempt ID. Native partial receipt: `train43-coverage002-chair-feedback.json`. Public human measures: `human-chair-measurements.md`, `human-sweep-measurements.md`; NOTES records provenance/lag caveats.
