# Saved protocol4/protocol6 hang comparison

## Execution boundary
The requested new literal a07 replay was **not executed**: `restore('p6-before-hang')` failed before remote exec because pod `<worker-pod>` was Failed. Lead subsequently confirmed disk-pressure eviction and STOP on simulator calls. No retry/infrastructure action. Last live drill was already admin-finished.

This comparison instead uses the **saved first protocol6 drill**, which already executed the original prehang joint/torso target, base `[1,.75,20]`, frame1520 joint target and15mm normal seating before later corrections. It is not a newly controlled run.

## Reproduce offline
`/usr/bin/python3 experiments/model-comparison/runs/pictures-run-009/examples/compare_p4_p6_saved.py`

Outputs `p4-p6-saved-comparison.json`, using saved public RGBD/proprio only. No RPCs. Plane fit ROI is head pixels x330:390/y160:250, visually checked inside poster in both endpoints. Plane normal is transformed into each measured TCP frame, separating object-in-hand differences from arm orientation.

| Corresponding stage | p4 a07 obs | p6 first drill obs | max joint difference rad | TCP difference mm (fwd,left,up) | poster-normal difference in TCP frame |
|---|---:|---:|---:|---|---:|
| Prehang |383|10|.010316|1.22,−.38,−7.60|4.629°|
| Approach |443|11|.011066|.06,−.03,−6.81|4.623°|
| Frame1520 before seat |447|12|.000120|.01,.00,−.00|4.624°|
|15mm seat |451|13|.002364|.31,−.34,−.18|14.792°|

The final pre-seat robot endpoint is effectively identical, but the poster-in-hand orientation is not. The difference predates seating. Protocol4 then changed poster orientation at seating/retained; protocol6 did not. This supports investigating acquisition/grasp transform, not simply assuming inadequate arm endpoint accuracy. It **does not prove** which pickup command/controller semantic caused the changed grasp, nor exclude base odometry/contact/transient timing.

## Evidence limits
- Protocol4 trace samples are chunk endpoints, not every physics tick. Protocol6 trace has tick-indexed errors but not full tick-indexed joints, pads or gripper positions. A true tick-by-tick proprio/pad trajectory diff cannot be reconstructed from these receipts. Do not interpolate and label it measured.
- p4 uses simulator pose odometry; p6 uses integrated velocity odometry. Numerically equal base goals do not establish equal physical base position. Wall/nail RGBD must anchor the comparison.
- Original p4 fixed-duration commands and p6 reached/stalled/timeout semantics differ. `seconds/max_steps` are ignored by current p6; an explicit fixed-duration closed hold cannot be reproduced through this client. The a07 post-snap hold was harmful and is not necessary evidence of success: snap already visible at451, before hold455.
- Different pickup histories mean this is not a controller-only causal comparison. Changed gripper gating remains a hypothesis.

## Next after explicit READY
1. Reverify own new SETUP/runtime; assume old process-local snapshots may be gone after eviction. Do not touch stale queue or recreate infrastructure.
2. Reacquire using public RGBD. Before hanging, compare poster-in-TCP plane/top edge with historical a07, not merely robot q.
3. Execute literal prehang/approach/frame1520/15mm-seat sequence without extra plane corrections as baseline; preserve all stage endpoints and command timing.
4. Isolate one compensation: match the **historical poster-in-hand transform**, rather than forcing wall-parallel orientation early. Historical pre-seat poster is oblique; indiscriminate full-plane alignment is not the same policy.
5. Release after observed seating with fresh measured-q target; verify full opening and unsupported retention. Partial grip.55/5.5cm width carried the poster through50mm retreat in the latest drill and is not release proof.
6. Only after snapshot/isolated success, full native-reset proof within3581steps. No protocol6 success is established.
