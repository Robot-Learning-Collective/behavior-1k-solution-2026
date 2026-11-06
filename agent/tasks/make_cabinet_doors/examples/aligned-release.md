# Cabinet attachment via tipped-rim placement — TRAIN10

## Result and limits
Native practice feedback/finish reports success=true, attached=true, Q1 at step3799/sim126.6333; finish wall1696.66s. Attempt `practice-restore-carried-door-near-cabinet-1922672029814f679d44217f6cbd69a6`. This is CHECKPOINT-CONTINUATION practice, not an uninterrupted native-reset episode or generalization evidence. The snapshot already held the acquired/carried door. Existing acquisition has a separate retained repeat. Full sequence before final placement includes failed motions and adjustments; timings are not clean policy performance.

Receipt/result: `../attachment-success.json`; actual release image/receipt own cache `practice-restore-carried-door-near-cabinet-1922672029814f679d44217f6cbd69a6/receipt_01792157913278284000_5e57d7f77752472391e3580fbbc458b5.json`. Native feedback uses explicitly privileged practice-only API; none of its truth supplies pose geometry.

## Observable geometric strategy
Tip cabinet open-face up, rim Z~.2478. Retain top-edge door pinch through wrist reorientation to horizontal, handle face UP. Horizontal gripper finger direction[.74,.67,0] matches cabinet long axis; close direction[0,0,-1]. Panel D→A long edge ~.477m and D→C width~.244m measured from RGBD, not guessed simulator object geometry.

Obs38 samples (head u,v): D(92,591)→[.547,.467,.484], A(76,452)→[.898,.791,.471], B(179,425)→[1.020,.569,.467], C(233,515)→[.707,.283,.466]. Far-edge lower than near edge by~17mm at that moment. Cabinet rim estimated from earlier observed corners plus base relative displacement, then checked visually. Door needed +.195m forward/-.063m left to align; actual base command +.18/-.06 achieved near alignment. This cleared a chair obstruction that had prevented crouching. Do not assume other instances match.

## Verified last placement sequence
Snapshot `door-aligned-above-cabinet`: torso[1.65,-2.423,-.89,0], left TCP[.569,.449,.479], grip0, right preset ready/open, base odom[.575,-.725],yaw-5.989. Native cabinet remains unattached, panel above rim. Snapshot from actual successful trial.

1. Lower to TCP[.569,.451,.352] with coupled torso/arm; reached:
```python
s.act(torso={'q':[1.75,-2.65,-1.2,0]},
      left={'q':[-.41233,-.00659,.33661,-.67196,1.8398,-.30763,-.84616]},seconds=4)
```
2. Deeper crouch attempted. Left reached but torso q1 STALLED at1.744 vs target1.8, 100Nm. This is a FAILED substep, do not perpetually command it:
```python
s.act(torso={'q':[1.8,-2.75,-1.3,0]},
      left={'q':[-.53746,.02106,.35621,-.43899,1.86396,-.25429,-.99538]},seconds=3)
```
Actual TCP[.571,.450,.325], finger[.74,.67,.04]. A future clean replay should test direct measured feasible torso rather than retain failed1.8 target.
3. Cancel torso preload at measured q1 and use slight five-degree far-edge-down door tilt to reach rim. Reached TCP[.569,.451,.299], finger[.74,.67,-.08], close[-.06,-.06,-1]:
```python
s.act(torso={'q':[1.744,-2.75,-1.3,0]},
      left={'q':[-.53207,.0244,.34218,-.44336,1.8552,-.28687,-.86769]},seconds=2)
```
Torso q errors zero but measured effort remained high; no force/contact inference. Saved `door-above-rim-prerelease`.
4. `s.act(left={'grip':1},seconds=1)` released retained panel. It settled visibly flush over opening. Finger opening stalled partially (sum.086m vs requested.10), lower pad atZ.270. No retreat was required for native success. `s.practice_feedback()` then `s.admin_finish()` both confirmed attached=true/Q1. The first script mistakenly called nonexistent `s.feedback()` AFTER release: act succeeded; AttributeError did not invalidate action. No replay occurred.

## Verified repeat
Restored `door-aligned-above-cabinet` into `practice-restore-door-aligned-above-cabinet-90d37d1c3edf4952bcb632452a7d83a6`; practice feedback explicitly false/Q0 atstep3732. Executed steps1,3,4 above (OMITTED failed step2). Native finish true/Q1 atstep3779, 47additional ticks=1.5667sim seconds, restore-to-finish wall68.6175s. `../attachment-repeat.json`; release receipt `receipt_01792158099124812000_ada3f509ae98427aafdc55e03ef9d4ea.json`. First descent terminal had transient q4lag.040 despite statusreached; next pose reached fully. Release partial-opening stall repeated, but attachment succeeded. Thus final aligned descent/release has two same-instance successes; not full chain reliability.

## Recovery / repeat
Named snapshot `door-above-rim-prerelease` tests final release only. `door-aligned-above-cabinet` tests final descent/release. `cabinet-tipped-ready` tests reorientation/approach. `carried-door-near-cabinet` tests tipping onward. `before-panel-grasp` tests acquisition onward. Use only matching source/instance native restore and inspect returned state; no determinism guarantee for attachment/particles. Preserve failures rather than counting snapshot repeats as full episode successes.
