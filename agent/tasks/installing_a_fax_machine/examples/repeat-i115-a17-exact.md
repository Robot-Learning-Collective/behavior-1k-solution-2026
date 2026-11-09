# i115-a17 exact public action sequence

Historical record, not a blind replay script. Includes unsuccessful recovery motions and rejected requests; inspect images and remeasure before contacts. All arguments preserved, including max_steps.

## 1. Initialize explicit open grips for fresh115 repeat

```python
s.act(**{'intent': 'Initialize explicit open grips for fresh115 repeat', 'left': {'grip': 1}, 'right': {'grip': 1}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 3})
```
Result: reached; observation 2.

Receipt: `<observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/receipt_01792130073220522000_37f8efbc66b8479388007e9c5374441a.json`
Image: `<observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/obs_0002.jpg`
Sim seconds: 0.06666666666666667

```text
[obs #002 | act=3341b8a1 | sim=  0.07s | wall=  12.1s | Initialize explicit open grips for fresh115 repeat]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.0, -0.0, 0.0]m rel_yaw=-0.000rad vel=[0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.11230076849460602, -0.14880307018756866, 0.06966280937194824, 0.027470363304018974]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.02367275580763817, 0.0812397450208664, 0.0013870669063180685, 0.006666711997240782, 0.0011778323678299785, 0.0009328027372248471, 0.0046119410544633865] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.0016443505883216858, 0.08396808803081512, 0.0013531248550862074, 0.0004164498532190919, 0.0011761145433411002, 0.0001519869256298989, 0.005036431830376387] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/obs_0002_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 2. Enter remeasured unobstructed corridor in short increment

```python
s.act(**{'intent': 'Enter remeasured unobstructed corridor in short increment', 'left': None, 'right': None, 'base': {'fwd': 0.2}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 4})
```
Result: reached; observation 3.

Receipt: `<observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/receipt_01792130085140601000_283ca7c2d1d9415ba1e65f5f067db3bb.json`
Image: `<observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/obs_0003.jpg`
Sim seconds: 2.033333333333333

```text
[obs #003 | act=a34af646 | sim=  2.03s | wall=  24.0s | Enter remeasured unobstructed corridor in short increment]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.195, 0.0, 0.0]m rel_yaw=+0.000rad vel=[0.001, 0.0, 0.001] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.6005536317825317, 0.5063874125480652, -0.2086719572544098, 0.028068508952856064]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.09594999253749847, 0.04477053880691528, -0.0009755238424986601, -0.03553520888090134, -0.0010443037608638406, -0.005726974457502365, -0.001673020888119936] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.09508059173822403, 0.023789342492818832, -0.0014474012423306704, -0.030747925862669945, -0.001357833854854107, -0.004848456475883722, -0.0024115373380482197] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/obs_0003_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 3. Advance 50 cm in measured straight corridor

```python
s.act(**{'intent': 'Advance 50 cm in measured straight corridor', 'left': None, 'right': None, 'base': {'fwd': 0.5}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 5})
```
Result: reached; observation 4.

Receipt: `<observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/receipt_01792130100538698000_d3e16f718e434ddf90604909c5b45fd6.json`
Image: `<observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/obs_0004.jpg`
Sim seconds: 5.5

```text
[obs #004 | act=108bc276 | sim=  5.50s | wall=  39.3s | Advance 50 cm in measured straight corridor]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.691, 0.0, 0.0]m rel_yaw=+0.000rad vel=[0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.907824695110321, 0.4803408980369568, -0.23446732759475708, -0.02454094961285591]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.11993006616830826, 0.03699534386396408, -0.0005795545876026154, -0.03995782509446144, -0.0006483439356088638, -0.005442166235297918, -0.001412330660969019] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.09211288392543793, 0.022252211347222328, -0.0010233300272375345, -0.03218724578619003, -0.0009636341128498316, -0.005178108345717192, -0.0019724376033991575] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/obs_0004_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 4. Continue 70 cm through measured floor to aisle junction

```python
s.act(**{'intent': 'Continue 70 cm through measured floor to aisle junction', 'left': None, 'right': None, 'base': {'fwd': 0.7}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 6})
```
Result: reached; observation 5.

Receipt: `<observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/receipt_01792130122648579000_ecc376047a8543c98f2245779c88af19.json`
Image: `<observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/obs_0005.jpg`
Sim seconds: 9.966666666666667

```text
[obs #005 | act=6aa6aed1 | sim=  9.97s | wall=  61.6s | Continue 70 cm through measured floor to aisle junction]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.386, 0.0, 0.0]m rel_yaw=+0.000rad vel=[-0.001, -0.0, -0.001] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.9382607936859131, 0.5072546601295471, -0.1943509876728058, -0.04074446111917496]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.10352577269077301, 0.006972345057874918, 0.0016744600143283606, -0.03054976649582386, 0.001602219301275909, -0.00349041516892612, 0.002544485032558441] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.08212406933307648, 0.017790591344237328, 0.001305015990510583, -0.02947862446308136, 0.0012951395474374294, -0.00459993164986372, 0.0030974086839705706] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/obs_0005_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 5. Small right turn to inspect aisle and divider clearance

```python
s.act(**{'intent': 'Small right turn to inspect aisle and divider clearance', 'left': None, 'right': None, 'base': {'yaw_deg': -15}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 5})
```
Result: stalled; observation 6.

Receipt: `<observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/receipt_01792130136263568000_c8ecaad59ef043f28109ec815c5a32ba.json`
Image: `<observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/obs_0006.jpg`
Sim seconds: 11.833333333333334

```text
[obs #006 | act=dc030924 | sim= 11.83s | wall=  75.1s | Small right turn to inspect aisle and divider clearance]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.425, 0.011, 0.0]m rel_yaw=-0.241rad vel=[0.0, 0.001, 0.001] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[3.154179096221924, 1.404811978340149, -0.7936516404151917, 0.02219333127140999]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.174167662858963, -0.2528665363788605, -0.0012224745005369186, -0.04889453575015068, -0.0004488751292228699, -0.005055541638284922, -0.007011143956333399] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.18534570932388306, -0.23494157195091248, -0.0020074062049388885, -0.050002321600914, -0.0011034514755010605, -0.00472508929669857, -0.0067635951563715935] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=stalled fault=None uncertain=False pending=['base']
  depth saved: <observation-cache>/fax-run-008-p6-176960/fax-run-008-v6-i115-a17/obs_0006_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```
