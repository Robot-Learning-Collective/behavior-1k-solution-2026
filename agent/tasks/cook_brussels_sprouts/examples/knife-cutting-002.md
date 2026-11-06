# First verified corrected-source cut — TRAIN10

Source a32648a/PID511218, protocol6; practice only. Attempt `practice-restore-recovery_container_carry-fd61d378358448deba8fd30124c4e475`. No cross-source restore. All positions BODY metres, angles degrees, torso `[.45,-.4,-.22,0]`. These are inspected trajectories, not blind macros or collision certificates.

## Outcome and stroke count
At obs63/sim188.17, two cut faces visibly remain on board; three whole sprouts remain on steel. Dedicated privileged **practice** feedback at step5645 independently reports **2/8 real halves**, zero cooked/inside oven; whole task false, fridge open, oven closed. Snapshot `recovery_first_cut`.

This branch made **two downward cutting approaches**: first level-blade approach stalled without visible split; second tip-down approach produced the verified split. There was no repeated sawing or third stroke. Second RPC ended stalled ~5mm above target, not pose-achieved: successful native slicing does not imply actuator endpoint completion. Cut verified after measured-q release and lift. No simulator fault on either corrected-source contact; old transition-asset failure is not reproduced.

## Knife grasp
- Knife initially swept during descent from TCP `[.679,-.19,1.061]` to `[.698,-.18,.907]`. Did NOT blindly close. Withdrew and remeasured changed handle heading.
- Free-space yaw−45 made fingers down, closing approximately `[-.71,.70,0]`, perpendicular to new handle axis. Stance advanced .06; staged `[.698,-.216,.98]`, then short descent `[.700,-.220,.907]`, measured `[.698,-.220,.908]`.
- Close0 → fingers `[.0363,0]`; lift `[.70,-.22,1.10]`, base retreat .25: retained knife visibly followed throughout.
- Two bounded joint-space waypoints reoriented it while clear:
  1. `[-1.20303,-.31424,1.25087,-1.51985,-1.68747,.34287,-.05138]` → TCP `[.634,.086,1.175]`.
  2. `[-.41691,-.28420,.27541,-1.93872,-1.75043,-.35149,-.44351]` → TCP `[.700,-.250,1.200]`, fingers +X, closing +Z, blade +Y.
- RGB-selected blade depth estimated plane x≈TCP.x+.014, useful span TCP.y+.08..+.20; edge near TCP.z−.005. These are noisy public-image estimates, not hidden rigid-object transforms.

## Contact correction
- Sprout top approximately `[.717,-.219,.929]`, board z≈.883. Base odom around `[-.407,1.228]`, yaw−.022.
- Alignment `[.704,-.35,1.02]` reached; **approach1** target `[.704,-.35,.945]`, seconds1.5 → obs57/sim184.77 TCP `[.708,-.350,.958]`, right q4lag+.027, torso effort~76Nm, stalled. No visible split. Likely low gripper geometry exhausted board clearance; effort/lag alone is not contact identity proof.
- Released with exact measured-q; lifted to1.08. Public depth PCA on visually selected blade gave normal approximately `[-.966,.010,-.260]`: blade face was already near vertical, so rotating face another90deg was not justified.
- Free-space `[.704,-.35,1.12]` plus **roll_deg−30** pitched blade tip down while keeping hand higher. Closing axis≈`[-.03,.49,.87]`, fingers≈+X.
- **Approach2** target `[.704,-.35,1.005]`, seconds1.5 → obs61/sim187.40 TCP `[.704,-.348,1.010]`, fingers~.0364/0, qlag≤.010rad, native no-fault stalled endpoint. Two pieces appeared. Receipt `receipt_01792172306329902000_0321fc4d947842d197b23048e9c64f84.json`.
- Exact measured-q release; lift `[.704,-.35,1.13]` → obs63/sim188.17 TCP `[.705,-.351,1.128]`, retained knife, two visible pieces. Receipt `receipt_01792172336007795000_41d3c45e60bc421e8263ddb6419ce7df.json`.

## Limits
One verified sprout split in same-source restored practice, not repeatability/generalization/full episode. Still need remaining three cuts, eight-half transfers, oven handling/cooking, door closure. Human exact stroke count remains unverified. Do not propagate privileged practice predicate identities into evaluation policy inputs.
