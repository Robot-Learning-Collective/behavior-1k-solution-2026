# Upright panel top-edge grasp — TRAIN10, twice at same approach

Evidence: first `cabinet-practice-002` obs12–15, repeat `practice-restore-before-panel-grasp-033fa2c5c0524f51b986bfddb3e29d0a` obs2–5. One native reset acquisition, then one snapshot repeat. Not held-out generalization or full goal success. Repeat took3.90sim seconds from snapshot;42.2wall including inspection/model time.

## Setup
Unfold BOTH arms with `preset='ready'` BEFORE crouching. Hanging right hand obstructed torso in failed001 and caused panel toppling. Torso q=[1.4505,-2.227,-.818,0]. Base odom[-2.473,-.707],yaw-2.862rad at this same-instance approach. Left start TCP[.52,.27,.65], finger_dir[0,0,-1], close_dir[.71,-.70,0], grip1. Right ready TCP[.685,-.281,.621],grip1. Snapshot `before-panel-grasp` holds this practice setup.

Measure, don't transfer coordinates blindly: top visible in left camera around native[245,220], BODY[.5611,.1796,.4513]. Panel face normal approximately[.712,-.702,0]. Near-corner rather than center grasp avoids extended-elbow IK stall. Native-depth near-corner top sample and observed outline support target choice; no object truth used.

## Exact successful repeat commands
Use assigned run-local sim_client only, with both environment variables exported as in kickoff. Inspect endpoints; stop on failed pose commands. Closure can report stalled because panel blocks finger closure; verify by test lift, not closure status.

```python
s.act(left={'to':[.565,.185,.50]}, intent='Repeat efficient near-corner pregrasp from saved approach', seconds=3)
s.act(left={'to':[.565,.185,.43]}, intent='Repeat vertical insertion to top minus21mm', seconds=3)
s.act(left={'grip':0}, intent='Repeat near-corner pinch', seconds=2)
s.act(left={'to':[.55,.185,.57]}, intent='Repeat test lift and verify retained panel displacement', seconds=4)
```

## Key measured state
Base/torso remained as above. Right remained ready.
- Precontact obs2: TCP[.563,.183,.502], pads[.596,.149,.502]/[.529,.216,.501], q[-1.00455,.21401,-1.47648,-.76412,-.47651,-.15389,-1.11406], fingers[.05,.05].
- Insertion obs3: TCP[.561,.186,.433], pads[.595,.152,.433]/[.528,.219,.433], q[-.92589,-.032,-1.49612,-.18567,-.57237,-.39869,-.84677], fingers[.05,.05].
- Close obs4: TCP[.561,.186,.433], pads[.565,.182,.433]/[.563,.184,.433], fingers[.0088,0], grip0. Asymmetry is not failure: visible panel between pads.
- Lift obs5: TCP[.551,.185,.569], pads[.555,.181,.569]/[.553,.183,.569], q[-1.08972,.35958,-1.46264,-1.11136,-.40542,.00549,-1.28301], fingers[.0089,0]. Panel top moved .4513→.5875 (+.1362m), retained relative to hand and moved against fixed bookshelf/floor; first trial top .5877.

## Images/state
Cache root `<observation-cache>/cabinet-run-023-p6-8027c5/`. Under repeat attempt above, `obs_0002*`=precontact, `obs_0003*`=insertion, `obs_0004*`=pinch, `obs_0005*`=airborne verification. Full public receipts carry all joints/pad geometry/image paths. First acquired snapshot `panel-lifted-first` remains available (practice-only).
