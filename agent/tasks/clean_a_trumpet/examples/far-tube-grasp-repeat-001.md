# Far-tube grasp after top-cleaned restore — verified retention, not mastery

Attempt `practice-restore-top-cleaned-001-6108899b5ebf409a843f04c5601d21f3`, obs9–19. This asymmetric grasp is different from the completed first episode's wide central grasp. Native task completion remained false later.

## Preconditions and failures
Restored `top-cleaned-001`. Raised both tools; base back.18, right.20 twice. Torso[.734,-.755,-.4,0]. Forward.08 triggered velocity mismatch atobs7; backward.06 recovered (guard false); no forward retry. Odom[2.234,-.591,0], yaw1.597, uncalibrated.

Left local delta[.06,-.03,-.03] obs9, then[.012,-.007,-.07] obs10 reached[.799,.234,.863], but closure11 was empty. Reopen/lift.09 obs12, shift[.06,.02,0] obs13. Far tube RGBD left[120,240]→[.90346,.27210,.87045]. A further-forward local move was rejected before action. Torso q0=.8 extended reach; closure15 was still empty because measured torso had not settled and pads remained above tube. Reopen and settle obs16.

## Successful correction
Fresh left RGBD:
- [u120,v250]→[.92372,.24650,.86981]
- [u120,v330]→[.92465,.27151,.86736]

```python
# From settled obs16, torso [.8,-.755,-.4,0], left open.
s.act(left={'q':translate('left',[0,0,-.035])}, timeout_seconds=2) # obs17
# Descent reached TCP [.902,.253,.869] with ~.023rad joint lag.
q=s.last_obs()['robot']['left']['joints']
s.act(left={'q':q,'grip':0}, accept_partial=True, timeout_seconds=1) # obs18
s.act(left={'q':translate('left',[0,0,.06])}, timeout_seconds=2) # obs19
```

Obs18 fingers[.0416,0], pinch[.921,.256,.869]. Obs19 cornet visibly followed the lift: TCP[.904,.254,.927], fingers[.0418,0]. Closure aperture alone was not evidence; object-following lift was. The requested measured hold is slew-limited, not an instantaneous preload reset.

Obs22 after brush withdrawal: left q[-1.94249,.22802,-2.30905,-.60712,.81854,.29790,-1.14090], pads[.943,.258,.924]/[.906,.255,.927], measured pinch[.924,.257,.925], close[.99,.10,-.07], finger[-.07,-.04,-1]. Retention continued through later axial presentation atobs54.

## Evidence
Current attempt cache under `<observation-cache>/trumpet-run-026-p6-509a09/`: `obs_0016.jpg`, `obs_0017.jpg`, `obs_0018.jpg`, `obs_0019.jpg`, associated depth/receipts. Exact emitted commands are preserved in run `control-action-results.jsonl`; the code above is the concise operation sequence, not a universal blind replay. Remeasure object height, torso settling, jaw insertion and the full tool/object swept path on any reset.
