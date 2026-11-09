# TRAIN43 first-attempt checkpoint — incomplete

Attempt `patio-speed-train43-zero001`, original Pi35445/session936e562a. First authorized reset on TRAIN43 through `practice_client`; handoff `reset-handoff-1792177262850661000.json`. No demo study, snapshot/restore, or intermediate native feedback during this first attempt. Public RGBD/proprioception only, NOTES-derived methods and fresh geometry. No controller/operator changes in this continuation.

## Native result

`speed-train43-zero001-finish.json`: success=false, Q=0, sole not-covered-floor-mud predicate unsatisfied. **8433 native30Hz ticks /281.10sim seconds**, finish wall2019.5780264810019s. Nominal budget18106ticks. It stopped early after a public survey incorrectly suggested no further bright orange; NOT budget exhaustion, task success, wall-speed parity or official evaluation. Binary Q does not quantify remaining mud. No next reset dispatched as part of this checkpoint.

103 dispatched action records in `control-action-results.jsonl` sum exactly8433ticks. Each has `0 < steps <= requested.max_steps`, finite positive remaining-budget cap. Last action `53e2fa47-689c-4b48-8209-930d98788a02`, obs105. Receipt cache `<observation-cache>/patio-run-027-p6-cabfd1/patio-speed-train43-zero001/`; last receipt `receipt_01792179273409585000_3a4a7f4064a1422d96c9f5f808f70403.json`.

## Public sequence and limitations

-009–015: current-depth shaft acquisition, separate open insertion/closure, retained whole-broom lift, surveyed at46.43s. Finger sum approximately3.3cm persisted through finish; visible retained tool corroborates it.
-016–034: stepping-stone/lamp border and chair-front orange strokes. Improved stance after a height miss rather than increased force. Visual disappearance is local evidence only.
-035–043: grill lateral reach blocked. Three-tick measured release did not fully replace old commands; longer slew, retreat and torso raise were required. Known branch was not sufficient clearance.
-044–052: occluded under-chair stroke used an earlier public point transformed through base motion; removal not subsequently verified. This area must remain unverified in a coverage checklist.
-053–068: upright torso restored view around grill; rotation-induced arm lag released. Final grill-leg stroke066 measured TCP[.726,.385,.001] versus requested approximately[.800,.395,.005]; measured release067 then withdrawal068 cleared lag. Local orange absent in exposed view, not entire-task proof.
-069–083: outer bench survey found TWO orange patches behind bench after an earlier survey showed none. Fresh-depth strokes080/082, with stance changes and withdrawal083, removed visible patches. This reinforces multi-view coverage rather than fixed-route recall.
-084–090: attempted outer lamp/tree bypass stalled086; changed route after inspecting current bench endpoints. Public depth, not drifting odometry, guided a1.5m lateral/end-around route. Bench seat brushed broom at090 with modest wrist lag; released/raised091.
-092–097: **unintended bench tilt at093 during lowering near its front**, despite low-safe arm staging. No deliberate bench grasp/relocation. Measured release/retreat094 did not immediately disengage it. Inward right-hand retraction095, attempted low tool retraction096 (IK height miss, not success), then measured hold/backward097 cleared broom from the bench leg. Bench remained tilted. Do not claim furniture was untouched.
-098–105: re-surveyed grill/chair gap with unused hand held inward; no bright orange observed in exposed floor. Incomplete lateral099 and diagonal104 motions prompted changed routes, not repeated pushing. Shaded tan mark under a chair remained uncertain. Final raised retreat105 followed by admin_finish returned failure. Thus stopping based on these exposed views was not a reliable completion policy.

## Next learning axis (not yet demonstrated)

Coverage/occlusion and collision-free whole-tool navigation, not stronger sweeping. Human study must compare matching sweep/approach/release and furniture-neighbor segments across different episodes with synchronized RGB, measured state and recorded actions. Preserve first-attempt failure before adaptation. Top NOTES now explicitly marks occluded strokes unverified, requires each chair/bench side and endpoint inspection, and warns that unused-hand clearance can tip furniture even when joints track closely. These are procedural corrections, not a proven TRAIN43 success.
