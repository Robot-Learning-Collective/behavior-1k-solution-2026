# Inner bell cleaning — first native goal success

TRAIN10, attempt `trumpet-practice-001`, obs342 / step12602: native `not covered(cornet,dust)` true, Q1, satisfied_fraction1. `practice-001-finish.json` independently records successful admin_finish. This is one long training attempt, not repeatability/mastery or evaluation evidence. Goal first reached at420.07sim s /6503.8wall s. Saved public snapshot name `task-cleaned-001`.

## Decisive finding
The last visible dust was **inside the bell**, not on the outer crown or tube faces. Atobs333, after a centrally grasped cornet lift, right-camera pixels68:85,407:435 showed a black cluster, median RGBD `[.87997,-.13319,.92982]`. Atobs338 pixels354:376,425:450 reconfirmed `[.88034,-.13332,.92963]`. Earlier clean-looking outer faces did not satisfy goal.

Right brush needed its bristles pointing **body +Y (left)** into the right-facing bell, not down. Two +45° body-X rolls with an intervening descent achieved this without wrist-limit failure. The left hand then moved the cornet toward the fixed brush because further right-arm leftward insertion was locally unreachable. A final2.5cm cornet translation changed native success false→true.

## Preconditions
Torso `[.734,-.755,-.4,0]`; uncalibrated base odometry `[1.823,-.485,0]`, yaw1.612. Left central tube/valve grasp, acquired obs321–324 (see central-grasp example), fingers~[.039,.049]. Right brush retained from initial handover, grip0, fingers~[.0002,.038]. Atobs331 leftTCP `[.781,.361,.904]`, rightTCP `[.803,-.189,1.080]`. No cross-run/reset replay implied.

The run-local `local_ik.translate()` returns joints only from public measured robot FK/Jacobian, not collision truth. Every motion below is still `s.act()`. Re-measure before adapting; endpoint and swept-object clearance remain separate requirements.

## Executed sequence (obs332–342)
```python
import sim_client as s
from local_ik import translate
s.act(right={'q':translate('right',[.05,-.10,0])}, timeout_seconds=2)
s.act(left={'q':translate('left',[0,0,.12])}, timeout_seconds=2)
# obs333: retained cornet lifted; inner-bell dust first clearly visible.
s.act(right={'q':translate('right',[0,-.10,.03])}, timeout_seconds=2)
s.act(right={'roll_deg':45}, timeout_seconds=2)
# Wrist5 now near upper bound; lower before next roll.
s.act(right={'q':translate('right',[0,0,-.12])}, timeout_seconds=2)
s.act(right={'roll_deg':45}, timeout_seconds=2)
s.act(right={'q':translate('right',[-.01,.10,-.04])}, timeout_seconds=2)
# obs338: dust localized again. An attempted +.08 left translation was
# rejected by local solver before act; no motion occurred.
s.act(right={'q':translate('right',[0,.04,0])}, timeout_seconds=1)
q=s.last_obs()['robot']['left']['joints'];q[2]=-2.33
s.act(left={'q':q},accept_partial=True,seconds=.2)
s.act(left={'q':translate('left',[0,-.05,0])},timeout_seconds=1)
s.practice_feedback()  # obs341, step12599 false
s.act(left={'q':translate('left',[0,-.025,0])},timeout_seconds=1)
s.practice_feedback()  # obs342, step12602 TRUE
```
Final left q `[-2.14303,.59011,-2.26644,-1.24348,.9027,.56043,-.91911]`, TCP `[.783,.286,1.024]`, measured pinch `[.778,.284,1.024]`, close `[.97,.23,-.04]`, fingers `[-.01,-.13,-.99]`. Right q `[-.693,.10624,-.61169,-.8807,-1.06632,.76616,.70346]`, TCP `[.841,-.252,.952]`, pinch `[.844,-.247,.934]`, close `[-.15,-.24,.96]`, fingers `[.93,.29,.22]`.

## Evidence
Images/depth: `<observation-cache>/trumpet-run-026-p6-509a09/trumpet-practice-001/obs_0333.jpg` (patch visible), `obs_0338.jpg` (localized approach), `obs_0341.jpg` (before success), `obs_0342.jpg` (success endpoint). Exact motor receipts and failed local solve outputs remain in session/control logs. Final motor receipt `receipt_01792163070180454000_1c912d4b7dc14ce7a5a44878c0006d8c.json`.

Avoid repeating unsupported exterior strokes: they moved the cornet toward the desk edge and did not remove this interior patch. Stabilization plus a correctly oriented brush face was decisive here; the full earlier cleaning sequence was not isolated for causal ablation.
