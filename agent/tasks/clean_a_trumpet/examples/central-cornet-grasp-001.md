# Central cornet grasp — first success, not repeated mastery

Attempt trumpet-practice-001, obs320–324. Cornet desk-supported after prior manipulation; mouthpiece extended left. Brush retained right, lifted clear. Torso `[.734,-.755,-.4,0]`. Base forward.10 obs320 was reached with base_safety.triggered=false; odometry `[1.823,-.486,0]`, yaw1.611, uncalibrated.

Left RGBD pixel[300,250] on thin upper tube adjacent to valves: `[.79293,.34499,.87126]`. Initial leftTCP `[.831,.329,1.010]`, open fingers[.05,.05], q `[-2.04325,.55706,-2.26459,-.91876,.87034,.34704,-1.01864]`, close `[.97,.26,0]`, fingers `[.04,-.16,-.99]`.

```python
import sim_client as s
from local_ik import translate
s.act(left={'q':translate('left',[-.04,.016,-.07])}, timeout_seconds=2)
s.act(left={'q':translate('left',[0,0,-.08])}, timeout_seconds=2)
s.act(left={'q':s.last_obs()['robot']['left']['joints'],'grip':0},timeout_seconds=2)
# Closure stalled at wide .088m finger sum. This alone was NOT grasp proof.
s.act(left={'q':translate('left',[0,0,.05])},accept_partial=True,timeout_seconds=2)
# obs324: cornet visibly follows lift. Subsequent .12m lift obs333 also retains.
```

Obs322 insertionTCP `[.789,.344,.863]`, pads `[.834,.356,.863]` / `[.742,.332,.863]`, q `[-1.70805,.54552,-2.25213,-.82231,.87621,.21324,-.77233]`. Obs324 liftTCP `[.789,.345,.911]`, fingers[.0389,.0491], q `[-1.84203,.60675,-2.26679,-.95538,.86845,.27871,-.8248]`.

This grasps central tube/valve region, not the mouthpiece. Actual wide closure indicates surrounding geometry participates; no exact contact-identity claim. Central stabilization prevented the large unsupported drift observed in earlier bell strokes. Lift exposed the final inner-bell patch, eventually cleaned in [inner-bell-cleaning-001.md](inner-bell-cleaning-001.md).

Images: `<observation-cache>/trumpet-run-026-p6-509a09/trumpet-practice-001/obs_0320.jpg`, `obs_0322.jpg`, `obs_0323.jpg`, `obs_0324.jpg`, `obs_0333.jpg`. Public FK local solver is not swept-object collision checking; inspect every endpoint. Do not replay these coordinates after a different reset/base/object pose without new RGBD measurement.
