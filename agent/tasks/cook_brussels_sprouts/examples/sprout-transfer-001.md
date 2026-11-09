# One sprout transferred to chopping board

Single observed success, not repeatability. Attempt `practice-restore-container_at_board-3276306c8581490f9bc016e04426c7ce`, obs21–28. Snapshot `sprout_on_board_first`. Scene had two sprouts spilled onto steel after failed container regrasp; two remained in tipped container. No cutting/cooking implied.

## Failure that made food accessible
Restored upright `container_at_board` after failed left rim retention. Right pads at old placement command[.78,-.12,.997] closed empty. Depth-corrected [.81,-.15,.985] caught only thin rim (fingers~.0027/.0009), then slipped on lift toward[.80,-.15,1.07]. Container tipped and two sprouts spilled onto steel, all four still visible. This was not an intentional/successful pour.

## Successful individual pickup
Torso[.45,-.4,-.22,0] permits vertical fingers at lower worktop; the earlier low torso[1.025,-1.45,-.47,0] had poor vertical-down reach. Base backed .20, right arm folded, shifted right .35. Stage left q[-1.76372,.34414,-1.91702,-.95669,-.30369,-.89001,-1.00049] ->TCP[.709,.220,1.060], fingers down, closing -Y. Advance .20 while above support.

First high pinch atTCP~[.712,.210,.921] closed empty above sprout. Lower target[.72,.205,.889] hit IK reach limit, not observed collision; lifted clear then advanced base another .10, giving fresh usable workspace. Fresh wrist depth top samples around[.6466,.1892,.9110]; steel .8616m.

- Target left[.65,.189,.890] reached[.649,.189,.891], open. Pad plane approximately sprout mid-height rather than top surface.
- Close0: fingers[.0500,.0008], asymmetric pinch[.649,.165,.891]. `stalled` grip alone is not success/failure proof.
- Lift[.65,.189,1.01] reached[.651,.189,1.009]; sprout visibly followed and remained held. Fingers[.05,.0006].
- Base right .35 (`left:-.35`), with sprout bottom clear of board; retained through transport.
- Left[.65,.05,1.01] centers sprout above board; lower[.65,.05,.925], release grip1, withdraw[.65,.10,1.08]. Sprout remains on board at obs28, hand empty.
- Snapshot `sprout_on_board_first` after obs28. Base odom~[.054,1.494], yaw-.382 (integrated/drifting, not world coordinates).

## Transferable observations
Use depth to estimate support and object top, then put the pad plane near the object's midsection; the first attempt at top+.01 closed empty. Short base correction improved low reach without changing torso. Verify asymmetric grasp via lift and subsequent lateral carry, not finger aperture alone. Plan each posture with free-space clearance; endpoint IK does not certify the path.
