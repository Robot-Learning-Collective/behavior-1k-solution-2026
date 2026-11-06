# Cook a brisket — shortest evidence-supported procedure

## Status and limits
TRAIN20 / house_double_floor_lower; one same-world training completion, **14813 native ticks / 493.7667 simulated seconds**, versus official11002 ticks. Success/all3 predicates true at obs304. Terminal admin_finish preserves the same step count; wall through endpoint9181.5708s, through finish9366.7275s. No post-start reset/restore. Not within-budget mastery, a fresh-world repeat, or a generalization result.

`PRACTICE-HOLD=WAIT_NEXT_INSTANCE` is active by lead msg_000817. This document is a future evaluation procedure, not permission to act/reset/rebind. Use the next assigned matching client only after lead release. Native worker/session/context/cap remain alive.

## Procedure (geometry-conditioned, not a trajectory replay)
1. **Identify the pan handle, burner, refrigerator and board from RGBD.** Navigate with tucked arms, heading before translation. Preserve a wider aisle near the L-shaped counter; straight backward/left motion from its tight corner caused tracking stops. Changed diagonal escape267 worked; never force/replay a guard-stopped translation.
2. **Move pan to burner by its wooden handle**, not rim. Unfold to a negative-elbow ready branch before reorientation. Align body to the measured handle and lower torso to seat slanted/downward jaws; close separately. Verify visible lift and retained pan through retreat before turning. Support bowl, open, withdraw vertically, then retreat. First successful transfer16–26; later reliable downward branch272–277 used fresh geometry, not copied pixel coordinates.
3. **Open refrigerator sufficiently for extraction.** Initial handle pull opens partially; release and reposition for an open-hand inner-panel push rather than extending a constrained wrist arc into limits. Compare approach to door geometry; do not copy human coordinates. Closing fridge is not a final predicate.
4. **Acquire brisket with fresh depth across the pinch**, not finger-aperture inference. Successful fridge acquisition144–149 followed fresh centering, separate measured-q close145, lift/withdrawal and body retreat; shelf visibly empty. Avoid six earlier empty acquisitions. Floor233 is recovery evidence, not the planned route.
5. **Carry brisket above the pan and release without disturbing it.** Align over pan interior using current depth, not edge/rim. Final successful placement243–247 lowered to TCP≈.958 while pan floor≈.915 in that body pose; open at support, lift fingers vertically, then retreat. The earlier160→161 combined placement/withdrawal lost BOTH pan and meat; exact cause unresolved. Do not replay it.
6. **Operate burner intentionally using a closed empty hand and bent right elbow.** Dense demos10212/10213 show forward/down hand and changing vertical/forward contact, not open nearly-straight cross-body reach. Successful OFF262 corrected TCP to the fresh switch center, then withdrew up/back263; red/off remained. **Clean planned ON was not demonstrated**: this run cooked after incidental blocked-tuck contact248. The closed-hand technique is a candidate for ON, not verified end-to-end behavior. Visually confirm each toggle; training predicate feedback is not an evaluation tool or geometric sensor.
7. **Reacquire pan, carry cooked meat to board, and pour with gripper CLOSED.** Fresh handle geometry→seat274→close275→retained lift276; wider-aisle retreat277 and carry278–280. Position board below the intended low rim. Incremental BODY-axis tilt around approximately[.8,−.6,0] moved meat toward rim. Joint limits required outward/upward elbow extension, not fixed-TCP insistence:281–284 reached and released meat onto board. Lift empty pan vertically285. Human10212/10213 show the same retained-handle tilt/reposition/release sequence; own joints differ. Static IK only supports feasibility, not collision safety.
8. **Return empty pan to the ORIGINAL left/sink-side countertop run near the L-corner**, not any visually similar slab. Restore near-level carry, align full bowl behind edge, lower to measured surface, open, withdraw vertically, retreat. First stove-side placement292–294 looked supported but final target remained false. Corrected original-side placement299–304 satisfied it. This supports a target/support-location distinction; hidden object ownership was not inspected.

No fixed joint list is a general macro. Fresh RGBD, full goal feedback and visible retention govern every stage. Replace persistent blocked arm targets with measured legal q before recovery. Small motor caps bound calls; a no-op `seconds=1` is not a one-second dwell. Do not expose training scorer feedback during evaluation.

## Recovery costs to avoid (observed, not guaranteed savings)
|Interval|Native ticks|Sim seconds|Wall seconds|Scope|
|---|---:|---:|---:|---|
|161→220|2984|99.4667|1428.6409|Search and physical floor-pan recovery after pan/meat displacement; several empty closes, cabinet interference and branch recovery|
|220→240|1121|37.3667|516.2580|Locate/approach floor brisket, first retained floor closure233 and high carry240; wall includes pause/study|
|161→240 combined|4105|136.8333|1944.8989|Spill aftermath through restored high meat carry; not all motion removable from a corrected route|
|294→304|297|9.9000|177.7013|Reacquire and relocate pan from unsuccessful stove-side support to required left-side location|

Official excess3811 ticks is smaller than the4105-tick spill-recovery interval, **but subtracting it is not a measured within-budget result**: corrected placement still needs travel, control and elapsed cooking. Repeated fridge failures, studies and the cleared historical hold also consumed substantial wall time; do not label their whole interval as motor inefficiency. No causal runtime/controller defect established.

## Evidence
- `NOTES.md`: complete chronology, human-vs-own tables and failures.
- `examples/same-world-completion.json`: actual feedback at304 and limitations; records state before terminal admin call.
- `examples/terminal-finish.json`: actual admin_finish reply, finished=true, all3 predicates=true, step14813.
- `examples/pan-pour-and-final-return-first-actions.json`: all35 received actions270–304, including failed target placement.
- `examples/floor-pan-recovery-first-actions.json` and `examples/floor-brisket-to-cooked-first-actions.json`: preserved recovery actions and incidental activation.
- Public reference images/proprio: pinned dataset10212/TRAIN20 and10213/TRAIN22 in `<demo-samples>/cook_a_brisket/`; six `*-pour-dense-*.jpg` sheets plus switch and acquisition studies. RGB n→state n−1 alignment.
