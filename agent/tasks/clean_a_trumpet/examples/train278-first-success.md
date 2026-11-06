# TRAIN278 — first-attempt native success

## Result and evidence limits

`trumpet-train278-first-001` finished with native success=true, Q=1 and `not covered(cornet,dust)` satisfied at **4,040 ticks / 134.6666667 simulated seconds / 4708.2659922 wall seconds**. This is 3,920 ticks below the 7,960-tick ceiling and below the 6,600-tick target.

Exact receipts: [`../train278-first-reset.json`](../train278-first-reset.json), [`../train278-first-finish.json`](../train278-first-finish.json). Final public endpoint: obs161, `receipt_01792184305825401000_215a920ede0443df805c5e86de371251.json`, in the TRAIN278 cache. Final administrative result, not visual appearance or joint effort, establishes success.

This was the first zero-shot, NOTES-only attempt on unseen TRAIN278 in the existing learner/session. No demonstration study, snapshot, restore or intermediate native outcome feedback was used. Finish supplied the first native feedback. The exact tick at which the predicate became satisfied is therefore unknown; no particular stroke can be credited as the decisive one. This is **one successful held-out practice instance**, not repeatability, a frozen evaluation, wall-time parity or a controlled comparison with TRAIN10. Wall time was approximately 78.47 minutes, despite the 134.67 simulated seconds.

## Public-observation trajectory

- **Obs1–44:** Fresh navigation/depth-based pickup; initial right brush grasp and lift, optional right→left handover with independent relocation, brush orientation work and supported approaches. RGBD plane fitting required a narrow/eroded region: a broad red mask contaminated the geometry.
- **Obs45–90:** Right cornet acquisition and lift. Left brush worked around neck/valve/rail regions while the cornet was presented in several orientations. Contact-associated bilateral displacement required measured-joint goal replacement and clear separation. Opening the left brush at obs90 alone did not establish placement.
- **Obs91–116:** Left cleared, approached as receiver and closed before the right hand opened. Right withdrew; left independently lifted/relocated the cornet. Right then reacquired and independently lifted the brush. A new right-grasp calibration superseded the old left-grasp transform.
- **Obs117–135:** Right brush approached fresh valve/body surfaces. Several approaches displaced the left arm near its third-joint limit; goals were replaced with legal measured-joint targets and the brush withdrawn. Some orientation searches failed without motor execution. Their failure is not global unreachability proof.
- **Obs136–142:** Cornet presentation initially interfered with the right brush. A short, FK-inspected right-shoulder raise separated the tool; later measured-goal replacement relieved another displacement. Translating the held cornet leftward with approximately preserved orientation brought its bell into a reachable right-arm workspace. This was more useful than persisting with infeasible outside-bell poses.
- **Obs143–152:** Staged right-arm reorientation exposed the bell interior in the wrist camera. Fresh depth and the grasp-specific bristle-patch estimate guided short inward approaches. Bilateral displacement prompted outward/upward withdrawal and measured-joint release, not further pushing. The brush then returned to a clear standoff.
- **Obs153–161:** Public gold-surface point-cloud PCA supplied an approximate long axis for staged inspection rotations. Additional shoulder rotation raised the cornet for another view; subsequent lag led to measured-goal replacement and a partial reversal. Sampled TCP/bell estimates did not certify whole-object clearance. Tools remained retained at the final public endpoint; finish confirmed the native goal.

## Transferable procedure updates

1. Keep calibration **grasp-specific**. After a handover/regrasp, recompute the working-face/visible bristle-patch relation from current RGBD and public FK. A fitted wood plane is not an exact bristle contact or force model.
2. Before forcing an awkward brush approach, **present the retained cornet within the other arm's reachable workspace**, with the brush clear. The successful lateral presentation here improved both reach and bell-interior visibility. Do not replay these coordinates in another instance.
3. Separate **presentation, tool reorientation, short contact and withdrawal**. Command completion, aperture and measured effort do not certify retained objects, safe paths or cleaning.
4. Use ordinary legal measured-joint replacement for persistent preload, verify convergence, and inspect current joint margins. Endpoint IK and sparse TCP samples do not account for the entire forearm, brush or long cornet.
5. Inspect the mouth end, loops, grasp-occluded regions and bell interior, but do not convert their clean appearance into a native outcome claim. In this first attempt success was queried only at finish.

## Preserved local plans

`train278-right-brush-calibration.json`, `train278-left-bell-centering.json`, `train278-right-bell-view-plan.json`, `train278-right-bell-approach.json`, `train278-left-final-inspection-options.json`, `train278-left-inspection65.json`, `train278-left-inspection95.json` preserve the grasp-specific planning evidence. Earlier plans and rejected alternatives remain intact. They are historical examples, not portable execution scripts.

## Handoff

The completed first attempt is ready for Astra's checkpoint freeze/PR integration without a second-success, clean-pair or batch gate. No new same-instance reset, cross-instance restore, simulator lifecycle change or additional native outcome query was made after finish. Further unseen practice requires the operator's next matched READY binding; existing learner context and cap remain unchanged.
