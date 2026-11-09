# i115-a29 exact public action sequence

Historical record, not a blind replay script. Includes unsuccessful recovery motions and rejected requests; inspect images and remeasure before contacts. All arguments preserved, including max_steps.

## 1. Initialize open grippers and stand upright

```python
s.act(**{'intent': 'Initialize open grippers and stand upright', 'left': {'grip': 1}, 'right': {'grip': 1}, 'base': None, 'torso': {'q': [0.84, -1.00609, -0.42, 0]}, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 3})
```
Result: reached; observation 2.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792142925030282000_e0a80dd8212a4332aeb76b7ac1e0b9a3.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0002.jpg`
Sim seconds: 0.6333333333333333

```text
[obs #002 | act=7a3923c4 | sim=  0.63s | wall=  11.5s | Initialize open grippers and stand upright]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-0.0, -0.0, 0.0]m rel_yaw=+0.000rad vel=[0.001, -0.0, -0.001] | torso=[0.841, -1.006, -0.42, -0.0] err=[-0.001, -0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-99.99755096435547, -55.345115661621094, 28.47321128845215, -0.013957083225250244]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-6e-05, -0.0, 1e-05, 1e-05, 0.0, -1e-05, -0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[5.050570964813232, 0.3794885277748108, -0.014200329780578613, 1.234887719154358, -0.012881465256214142, 0.0976826474070549, 0.01020763348788023] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-4e-05, -0.0, 2e-05, -1e-05, 1e-05, -0.0, -0.0] q_lag=[0.0, 0.0, -0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[4.67488956451416, 0.3845783472061157, 0.011722028255462646, 1.1051661968231201, 0.003819648176431656, 0.09749624878168106, 0.010790877975523472] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0002_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 2. Left ten centimetres away from chair foot

```python
s.act(**{'intent': 'Left ten centimetres away from chair foot', 'left': None, 'right': None, 'base': {'left': 0.1}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 3})
```
Result: reached; observation 3.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792142936870050000_7c437f15180347d486185b02e6b54fd6.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0003.jpg`
Sim seconds: 2.1

```text
[obs #003 | act=13d0deb2 | sim=  2.10s | wall=  23.2s | Left ten centimetres away from chair foot]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-0.0, 0.095, 0.0]m rel_yaw=+0.000rad vel=[-0.0, 0.0, 0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[0.46514973044395447, 0.025807324796915054, -0.07685446739196777, 0.051384665071964264]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.002210015431046486, 0.4426969587802887, 0.0034437160938978195, 0.0009689985308796167, 0.0024040068965405226, 0.0013058569747954607, 0.01602626033127308] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] q_lag=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.015587212517857552, 0.42003676295280457, 0.0029248734936118126, -0.0007029185071587563, 0.002199198119342327, 0.000639531237538904, 0.016315016895532608] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0003_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 3. First clear metre entry aisle

```python
s.act(**{'intent': 'First clear metre entry aisle', 'left': None, 'right': None, 'base': {'fwd': 1}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 8})
```
Result: reached; observation 4.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792142953813104000_e79b26d6067b486b949b125565fc53c4.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0004.jpg`
Sim seconds: 8.066666666666666

```text
[obs #004 | act=a43b16cf | sim=  8.07s | wall=  40.3s | First clear metre entry aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.995, 0.096, 0.0]m rel_yaw=+0.000rad vel=[-0.0, 0.0, 0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[1.554263710975647, 0.7743898630142212, -0.34593093395233154, 0.026895614340901375]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.12270047515630722, 0.27216070890426636, 0.002578635234385729, -0.03880561515688896, 0.0019176951609551907, -0.004535135347396135, 0.009700908325612545] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, -0.0, -1e-05, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.13090619444847107, 0.2572193741798401, 0.0017320453189313412, -0.04082272946834564, 0.0013971789740025997, -0.0058220126666128635, 0.009854098781943321] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0004_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 4. Second clear metre toward cross aisle

```python
s.act(**{'intent': 'Second clear metre toward cross aisle', 'left': None, 'right': None, 'base': {'fwd': 1}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 8})
```
Result: reached; observation 5.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792142970362529000_7663d062fcf0459fb6e2154b6119520c.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0005.jpg`
Sim seconds: 14.033333333333333

```text
[obs #005 | act=86a6b345 | sim= 14.03s | wall=  56.7s | Second clear metre toward cross aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.99, 0.096, 0.0]m rel_yaw=+0.000rad vel=[0.0, -0.0, -0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[1.2993279695510864, 0.8187160491943359, -0.356637567281723, 0.009423449635505676]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.12080776691436768, -0.18908868730068207, 0.00046713114716112614, -0.03847601264715195, 0.0007718906854279339, -0.005521916784346104, -0.004555894527584314] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.12178710103034973, -0.1688457727432251, 0.0001500148791819811, -0.038549721240997314, 0.00045162596506997943, -0.005555627401918173, -0.004139404743909836] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0005_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 5. Twelve centimetres to clear turning stance

```python
s.act(**{'intent': 'Twelve centimetres to clear turning stance', 'left': None, 'right': None, 'base': {'fwd': 0.12}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 3})
```
Result: reached; observation 6.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792142985738139000_e16a3d293596473eb9c8c150b0766b2c.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0006.jpg`
Sim seconds: 15.6

```text
[obs #006 | act=560a7ed8 | sim= 15.60s | wall=  72.2s | Twelve centimetres to clear turning stance]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[2.106, 0.096, 0.0]m rel_yaw=+0.000rad vel=[-0.0, 0.0, -0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[1.1384968757629395, 0.6598207354545593, -0.28642022609710693, -0.04576915130019188]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, 0.0, -0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.13493597507476807, -0.029210930690169334, -0.0005312319844961166, -0.0431138277053833, -0.00042548682540655136, -0.005804534535855055, -0.0026101956609636545] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, 0.0, -0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.0920226201415062, -0.035296954214572906, -0.001014248700812459, -0.03156135603785515, -0.0008122536819428205, -0.00498193921521306, -0.002944094594568014] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0006_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 6. Right ninety in clear cross aisle

```python
s.act(**{'intent': 'Right ninety in clear cross aisle', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 7})
```
Result: reached; observation 7.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143004383173000_77445cbbb7244ce2bae70c7fb08a7fd4.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0007.jpg`
Sim seconds: 20.8

```text
[obs #007 | act=e3a35e08 | sim= 20.80s | wall=  90.9s | Right ninety in clear cross aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[2.106, 0.096, 0.0]m rel_yaw=-1.566rad vel=[-0.0, -0.0, -0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-0.08524134755134583, -0.03189108148217201, 0.013224411755800247, -0.04589070379734039]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.018122036010026932, -0.08425748348236084, -0.001439591869711876, -0.005746190901845694, -0.0012063290923833847, -0.0008091751369647682, -0.004842889029532671] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.020906081423163414, -0.08556366711854935, -0.0014023855328559875, 0.005480583291500807, -0.0012244898825883865, 0.0005570693756453693, -0.005249536130577326] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0007_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 7. Main aisle clear first metre

```python
s.act(**{'intent': 'Main aisle clear first metre', 'left': None, 'right': None, 'base': {'fwd': 1}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 8})
```
Result: reached; observation 8.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143021503600000_a6b65bef4de045a7a1dae5280cdab64a.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0008.jpg`
Sim seconds: 26.766666666666666

```text
[obs #008 | act=140e52b3 | sim= 26.77s | wall= 108.0s | Main aisle clear first metre]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[2.111, -0.899, 0.0]m rel_yaw=-1.566rad vel=[-0.0, -0.0, -0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[1.0478832721710205, 0.7321470379829407, -0.2932793200016022, -0.05813717842102051]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.1257818341255188, -0.29748624563217163, -0.0019253939390182495, -0.0389631986618042, -0.001272624358534813, -0.005590612534433603, -0.011655871756374836] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.09468929469585419, -0.2850148677825928, -0.0021168887615203857, -0.03319556266069412, -0.0015486013144254684, -0.00539202056825161, -0.011788524687290192] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0008_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 8. Second metre clear main aisle

```python
s.act(**{'intent': 'Second metre clear main aisle', 'left': None, 'right': None, 'base': {'fwd': 1}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 8})
```
Result: reached; observation 9.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143038955861000_1bcea5b02882442da0a79eeb8c52e301.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0009.jpg`
Sim seconds: 32.733333333333334

```text
[obs #009 | act=aa108e98 | sim= 32.73s | wall= 125.5s | Second metre clear main aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[2.115, -1.895, 0.0]m rel_yaw=-1.566rad vel=[-0.0, 0.0, -0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[1.4008070230484009, 0.8132530450820923, -0.35572969913482666, 0.02746070921421051]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, -0.0, -1e-05, -0.0, -0.0, 0.0, 0.0] q_lag=[-0.0, 0.0, 0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.12035566568374634, 0.0036313864402472973, 0.0020641200244426727, -0.03852784261107445, 0.0018628090620040894, -0.005257046315819025, 0.0026478287763893604] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.12313967198133469, 0.014245091937482357, 0.0014937110245227814, -0.038233738392591476, 0.001430470496416092, -0.005461475811898708, 0.0032017556950449944] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0009_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 9. Third metre clear main aisle

```python
s.act(**{'intent': 'Third metre clear main aisle', 'left': None, 'right': None, 'base': {'fwd': 1}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 8})
```
Result: reached; observation 10.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143059662545000_38fe78e8a8cb425ea39e427e18754b86.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0010.jpg`
Sim seconds: 38.7

```text
[obs #010 | act=a32d5af4 | sim= 38.70s | wall= 146.0s | Third metre clear main aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[2.12, -2.89, 0.0]m rel_yaw=-1.566rad vel=[-0.0, -0.0, -0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[0.9662606120109558, 0.6823983788490295, -0.25924772024154663, -0.05012625455856323]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.13069310784339905, -0.23362275958061218, -0.0008854120969772339, -0.04197753593325615, -0.0005089826881885529, -0.006181378848850727, -0.00881484430283308] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.0915612205862999, -0.2212902158498764, -0.001127772033214569, -0.03269144147634506, -0.000794372521340847, -0.005530958063900471, -0.008998776786029339] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0010_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 10. Pass visible fax .885m clear aisle

```python
s.act(**{'intent': 'Pass visible fax .885m clear aisle', 'left': None, 'right': None, 'base': {'fwd': 0.885}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 8})
```
Result: reached; observation 11.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143075747839000_e59fb5d15f4248698cb82bb52a674a0b.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0011.jpg`
Sim seconds: 44.1

```text
[obs #011 | act=54d3a1c3 | sim= 44.10s | wall= 162.2s | Pass visible fax .885m clear aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[2.124, -3.771, 0.0]m rel_yaw=-1.566rad vel=[-0.0, -0.0, 0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[1.1681863069534302, 0.819330096244812, -0.35232651233673096, -0.07520177960395813]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.14865899085998535, -0.3268660306930542, -0.0020592883229255676, -0.045485448092222214, -0.0014188699424266815, -0.0063277343288064, -0.013110687024891376] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.09496999531984329, -0.31229010224342346, -0.0022547170519828796, -0.03351328521966934, -0.0016916971653699875, -0.00557955726981163, -0.013550907373428345] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0011_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 11. Right ninety toward floor fax through entry gap

```python
s.act(**{'intent': 'Right ninety toward floor fax through entry gap', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 7})
```
Result: reached; observation 12.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143311524202000_fee901d4a51646f987f70a8e4a3c28e5.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0012.jpg`
Sim seconds: 49.3

```text
[obs #012 | act=9c28ff19 | sim= 49.30s | wall= 397.9s | Right ninety toward floor fax through entry gap]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[2.124, -3.77, 0.0]m rel_yaw=-3.132rad vel=[0.0, 0.0, -0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[0.5221531987190247, 0.07473289966583252, -0.11660534143447876, -0.022368788719177246]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.02125253714621067, 0.2585427761077881, 0.001987084746360779, -0.003716397564858198, 0.0012969709932804108, 0.0008341730572283268, 0.008588198572397232] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.003978375345468521, 0.24211645126342773, 0.0016697347164154053, -0.0005298932082951069, 0.0011859908699989319, 0.00015175214502960443, 0.008630565367639065] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0012_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 12. Twenty centimetres toward fax keeping chassis off object

```python
s.act(**{'intent': 'Twenty centimetres toward fax keeping chassis off object', 'left': None, 'right': None, 'base': {'fwd': 0.2}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 3})
```
Result: reached; observation 13.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143323660593000_1511a7e30ef440c5ba42484a7c143e1a.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0013.jpg`
Sim seconds: 51.266666666666666

```text
[obs #013 | act=3ac14fe4 | sim= 51.27s | wall= 410.1s | Twenty centimetres toward fax keeping chassis off object]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.929, -3.772, 0.0]m rel_yaw=-3.132rad vel=[-0.001, -0.0, -0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[1.2880662679672241, 1.0341500043869019, -0.3710935413837433, -0.004452630877494812]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.14970487356185913, -0.2264510840177536, -0.0012892335653305054, -0.049264874309301376, -0.0008333995938301086, -0.007676496636122465, -0.008990971371531487] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.1295691579580307, -0.21834993362426758, -0.001762092113494873, -0.04081922397017479, -0.001288093626499176, -0.006298060063272715, -0.009334628470242023] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0013_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 13. Final twenty centimetres to stationary pickup stance

```python
s.act(**{'intent': 'Final twenty centimetres to stationary pickup stance', 'left': None, 'right': None, 'base': {'fwd': 0.2}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 3})
```
Result: reached; observation 14.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143335826947000_fc2adcbe0b9a48a3af73244f67e90e06.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0014.jpg`
Sim seconds: 53.233333333333334

```text
[obs #014 | act=365dba69 | sim= 53.23s | wall= 422.3s | Final twenty centimetres to stationary pickup stance]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.734, -3.774, 0.0]m rel_yaw=-3.132rad vel=[-0.0, -0.0, -0.002] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[1.162532091140747, 0.7362064123153687, -0.2990037798881531, -0.01156904548406601]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, 0.299, 0.532] pad_end=[0.072, 0.204, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, 0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.12670913338661194, 0.05715608596801758, 0.00180145725607872, -0.03939717635512352, 0.0015586065128445625, -0.005102923605591059, 0.003167727729305625] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.072, -0.252, 0.532]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.072, -0.205, 0.532] pad_end=[0.072, -0.3, 0.532] measured_pinch=[0.072, -0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.1101764366030693, 0.06094326823949814, 0.0012640245258808136, -0.03630891814827919, 0.001159784384071827, -0.005637953523546457, 0.0035373629070818424] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0014_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 14. Stationary crouch and arms clear beside floor fax

```python
s.act(**{'intent': 'Stationary crouch and arms clear beside floor fax', 'left': {'q': [-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56]}, 'right': {'q': [-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466]}, 'base': None, 'torso': {'q': [1.68, -2.54, -1.62, 0]}, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 4})
```
Result: reached; observation 15.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143350602443000_0e6ec43a7fd24b349ebc30ad362f76ad.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0015.jpg`
Sim seconds: 56.4

```text
[obs #015 | act=59ea0730 | sim= 56.40s | wall= 437.0s | Stationary crouch and arms clear beside floor fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.735, -3.774, 0.0]m rel_yaw=-3.131rad vel=[-0.001, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[0.06654327362775803, -0.0208781436085701, -0.031229320913553238, 0.011031614616513252]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.631, 0.133, 0.252] pad_end=[0.633, 0.038, 0.257] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.34498, 0.83545, 1.56] q_lag=[-0.0, 0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.0029097110964357853, 0.007623630575835705, 0.0005265353247523308, 0.005070776678621769, -0.004251760896295309, -0.0005942237912677228, 0.0025432368274778128] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.253, -0.27, 0.123]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.253, -0.223, 0.123] pad_end=[0.252, -0.318, 0.124] measured_pinch=[0.253, -0.27, 0.123]m
     close_dir=[0.01, 1.0, -0.01] fing_dir=[-0.68, -0.0, -0.73] q=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] q_lag=[0.0, 0.0, 0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[-0.0019645916763693094, -0.001761458464898169, -4.422001074999571e-05, 0.0019156326306983829, 0.0005729188560508192, -0.0002053176867775619, -0.0005595698021352291] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0015_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 15. Approach above current narrow end

```python
s.act(**{'intent': 'Approach above current narrow end', 'left': None, 'right': {'to': [0.612, -0.2, 0.1], 'finger_dir': [0, 0, -1], 'close_dir': [-0.4, 0.9165, 0]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 3})
```
Result: reached; observation 16.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143375714389000_c6065f13555f4f5e9e71ebcfad6e9f94.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0016.jpg`
Sim seconds: 57.233333333333334

```text
[obs #016 | act=7ade8e75 | sim= 57.23s | wall= 462.2s | Approach above current narrow end]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.735, -3.774, 0.0]m rel_yaw=-3.131rad vel=[0.0, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-0.8314232230186462, -0.48910459876060486, 0.4801044166088104, -0.08724238723516464]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.631, 0.133, 0.252] pad_end=[0.633, 0.038, 0.257] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.02912055514752865, -0.03125578165054321, 0.005280276760458946, -0.03137572854757309, 0.0023780125193297863, 0.00038710038643330336, -0.0016181819373741746] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.612, -0.202, 0.102]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.593, -0.159, 0.101] pad_end=[0.631, -0.246, 0.102] measured_pinch=[0.612, -0.203, 0.102]m
     close_dir=[-0.4, 0.92, -0.01] fing_dir=[0.01, -0.01, -1.0] q=[-1.11876, -0.22651, 1.20545, -0.76987, -1.03904, 0.74012, -0.31691] q_lag=[-0.0, 0.0, 0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[2.418, 0.391, 1.141, 1.109, 1.307, 0.297, 1.244]rad min=0.297rad
     q_cmd=[-1.11877, -0.2265, 1.20546, -0.76985, -1.03909, 0.74011, -0.31688] effort_Nm=[0.0812847837805748, -0.037387482821941376, 0.01351125817745924, 0.0060948277823626995, 0.0032756291329860687, 0.0036953382659703493, -0.0060504102148115635] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0016_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 16. Lower to straddle narrow end

```python
s.act(**{'intent': 'Lower to straddle narrow end', 'left': None, 'right': {'to': [0.6, -0.214, 0.06]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 2})
```
Result: reached; observation 17.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143385664007000_46798a115636415ba673d47e4af50b04.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0017.jpg`
Sim seconds: 57.7

```text
[obs #017 | act=e4cee081 | sim= 57.70s | wall= 472.2s | Lower to straddle narrow end]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.735, -3.774, 0.0]m rel_yaw=-3.131rad vel=[-0.0, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[0.1064768135547638, -0.13412851095199585, -0.077151820063591, -0.030005905777215958]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.631, 0.133, 0.252] pad_end=[0.633, 0.038, 0.257] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.04551921784877777, -0.0018663916271179914, -0.009906693361699581, 0.008913975208997726, 0.0013859716709703207, 0.0001880545460153371, -0.0004325264599174261] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.598, -0.214, 0.064]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.58, -0.171, 0.063] pad_end=[0.618, -0.258, 0.064] measured_pinch=[0.599, -0.215, 0.064]m
     close_dir=[-0.4, 0.92, -0.01] fing_dir=[0.01, -0.01, -1.0] q=[-1.12897, -0.12192, 1.27934, -0.4484, -0.96733, 0.56984, -0.12569] q_lag=[-0.0, 0.0, 0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[2.428, 0.286, 1.067, 0.788, 1.379, 0.467, 1.435]rad min=0.286rad
     q_cmd=[-1.12897, -0.1219, 1.27935, -0.44837, -0.96735, 0.56983, -0.12568] effort_Nm=[0.033549461513757706, -0.017453046515583992, 0.0028899789322167635, -0.0021208827383816242, -5.50542026758194e-05, -0.00033278175396844745, 0.001063696458004415] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0017_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 17. Set narrow-end pinch depth

```python
s.act(**{'intent': 'Set narrow-end pinch depth', 'left': None, 'right': {'to': [0.6, -0.214, 0.05]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 2})
```
Result: reached; observation 18.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143394991993000_967ab6f0219244f8aedd833d0ed2c15f.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0018.jpg`
Sim seconds: 57.96666666666667

```text
[obs #018 | act=529787d5 | sim= 57.97s | wall= 481.4s | Set narrow-end pinch depth]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.735, -3.774, 0.0]m rel_yaw=-3.131rad vel=[-0.0, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[0.0, -0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-0.010239331051707268, -0.022504836320877075, 0.016140498220920563, 0.024451665580272675]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.631, 0.133, 0.252] pad_end=[0.633, 0.038, 0.257] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.006195434834808111, 0.01606784574687481, 0.0037973644211888313, 0.00498280581086874, -0.0014132040087133646, -0.00025736604584380984, 0.0012307249708101153] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.598, -0.214, 0.054]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.579, -0.171, 0.053] pad_end=[0.617, -0.258, 0.055] measured_pinch=[0.598, -0.215, 0.054]m
     close_dir=[-0.4, 0.92, -0.01] fing_dir=[0.01, -0.01, -1.0] q=[-1.14571, -0.05241, 1.30361, -0.28359, -0.94571, 0.50654, -0.04436] q_lag=[-0.0, 0.0, 0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[2.445, 0.217, 1.043, 0.623, 1.4, 0.531, 1.516]rad min=0.217rad
     q_cmd=[-1.14571, -0.0524, 1.30361, -0.28356, -0.94571, 0.50653, -0.04435] effort_Nm=[-0.00026559681282378733, 0.011960322968661785, -0.0007830602116882801, -0.013580838218331337, -0.0008024359121918678, -0.0017626953776925802, 0.002394552808254957] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0018_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 18. Freeze measured straddle and close

```python
s.act(**{'intent': 'Freeze measured straddle and close', 'left': {'grip': 0}, 'right': {'q': [-1.1457065343856812, -0.052407123148441315, 1.303605318069458, -0.2835860848426819, -0.9457097053527832, 0.5065356492996216, -0.044358979910612106], 'grip': 0}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 2})
```
Result: stalled; observation 19.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143407583562000_e4d348f128a6419495325c984c1b9101.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0019.jpg`
Sim seconds: 58.63333333333333

```text
[obs #019 | act=2d9539de | sim= 58.63s | wall= 494.0s | Freeze measured straddle and close]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.735, -3.774, 0.0]m rel_yaw=-3.131rad vel=[0.0, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[16.26044464111328, 6.261445045471191, -11.271364212036133, 10.770398139953613]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.255] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30832, 0.05613, -0.97214, -1.00327, 2.34502, 0.83543, 1.56005] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.010854815132915974, 0.09350042045116425, 0.01026826910674572, 0.043510694056749344, -0.004902524407953024, -0.0007397888693958521, 0.0030398122034966946] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.598, -0.215, 0.054]m fingers=[0.0315, 0.031]m grip=command=0.0 finger_sum(6.2cm)
     pad_start=[0.587, -0.189, 0.054] pad_end=[0.61, -0.241, 0.055] measured_pinch=[0.598, -0.215, 0.054]m
     close_dir=[-0.4, 0.92, -0.02] fing_dir=[0.01, -0.01, -1.0] q=[-1.14579, -0.0525, 1.30416, -0.28332, -0.94351, 0.50683, -0.04453] q_lag=[0.0, 0.0, -0.001, -0.0, -0.002, -0.0, 0.0]rad limit_margins=[2.445, 0.217, 1.042, 0.622, 1.403, 0.53, 1.516]rad min=0.217rad
     q_cmd=[-1.14571, -0.05241, 1.30361, -0.28359, -0.94571, 0.50654, -0.04436] effort_Nm=[3.108621835708618, 6.4254679679870605, 0.41154932975769043, -2.444603681564331, -0.1319880485534668, -1.3905762434005737, 1.0823559761047363] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=stalled fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0019_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 19. Lift and verify powered fax retention

```python
s.act(**{'intent': 'Lift and verify powered fax retention', 'left': None, 'right': {'to': [0.598, -0.214, 0.18]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': True, 'timeout_seconds': 3})
```
Result: reached; observation 20.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143418151941000_d16d6531721a4b8793f04a0e8c54dc18.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0020.jpg`
Sim seconds: 60.03333333333333

```text
[obs #020 | act=e2ae9309 | sim= 60.03s | wall= 504.6s | Lift and verify powered fax retention]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.735, -3.775, 0.0]m rel_yaw=-3.130rad vel=[0.001, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-8.850635528564453, -4.310041904449463, 6.650628566741943, 0.4558802843093872]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30835, 0.05609, -0.97215, -1.00322, 2.34501, 0.83545, 1.56001] q_lag=[0.0, -0.0, 0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.13875225186347961, -0.0719381719827652, 0.030906081199645996, -0.0956820696592331, 0.0045289695262908936, 0.0006915194680914283, -0.0025623831897974014] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.598, -0.214, 0.179]m fingers=[0.0315, 0.0311]m grip=command=0.0 finger_sum(6.3cm)
     pad_start=[0.587, -0.188, 0.178] pad_end=[0.61, -0.241, 0.179] measured_pinch=[0.598, -0.214, 0.179]m
     close_dir=[-0.4, 0.92, -0.01] fing_dir=[0.01, -0.01, -1.0] q=[-0.99401, -0.41624, 1.00908, -1.30855, -1.21455, 0.9911, -0.67287] q_lag=[-0.0, 0.0, -0.0, -0.0, -0.0, -0.001, -0.0]rad limit_margins=[2.293, 0.581, 1.337, 0.776, 1.132, 0.046, 0.888]rad min=0.046rad
     q_cmd=[-0.99408, -0.41622, 1.00893, -1.30859, -1.21457, 0.99032, -0.67314] effort_Nm=[-3.17085599899292, 1.9024475812911987, -1.218955636024475, -3.05039644241333, 0.14634466171264648, -0.7965081334114075, 0.28337955474853516] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0020_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 20. Bring retained already green fax inward

```python
s.act(**{'intent': 'Bring retained already green fax inward', 'left': None, 'right': {'to': [0.5, -0.16, 0.23], 'pitch_deg': 35}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 3})
```
Result: reached; observation 21.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143429898251000_8e83ca5d607041d6b07ad261ce255662.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0021.jpg`
Sim seconds: 60.9

```text
[obs #021 | act=82636f42 | sim= 60.90s | wall= 516.3s | Bring retained already green fax inward]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.735, -3.775, 0.0]m rel_yaw=-3.131rad vel=[-0.001, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-6.583002090454102, -2.763841390609741, 4.953763961791992, -0.4547930955886841]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30835, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, 0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.04910031333565712, -0.01330694742500782, 0.012430931441485882, -0.03425160050392151, 0.0008061826229095459, 7.634109351783991e-05, -1.4656849089078605e-05] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.161, 0.229]m fingers=[0.0315, 0.0311]m grip=command=0.0 finger_sum(6.3cm)
     pad_start=[0.49, -0.135, 0.222] pad_end=[0.509, -0.187, 0.236] measured_pinch=[0.5, -0.161, 0.229]m
     close_dir=[-0.33, 0.91, -0.25] fing_dir=[0.57, -0.02, -0.82] q=[-0.53234, -0.43769, 1.21202, -1.64424, -0.62233, 0.36726, -1.04798] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.002, 0.001]rad limit_margins=[1.831, 0.602, 1.134, 0.44, 1.724, 0.67, 0.513]rad min=0.44rad
     q_cmd=[-0.53239, -0.43767, 1.2119, -1.64438, -0.62188, 0.36532, -1.04724] effort_Nm=[-2.31473445892334, 1.198089838027954, -0.766791820526123, -3.006697654724121, 1.6308001279830933, -1.121029257774353, -0.541403591632843] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0021_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 21. Stand stationary with retained green fax

```python
s.act(**{'intent': 'Stand stationary with retained green fax', 'left': None, 'right': None, 'base': None, 'torso': {'q': [0.84, -1.00609, -0.42, 0]}, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 3})
```
Result: reached; observation 22.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143443528186000_a10a8a63296840ca9c9665a5c1733bdd.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0022.jpg`
Sim seconds: 63.0

```text
[obs #022 | act=4daebe5c | sim= 63.00s | wall= 529.9s | Stand stationary with retained green fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.737, -3.774, 0.0]m rel_yaw=-3.132rad vel=[0.0, -0.001, -0.002] | torso=[0.844, -1.006, -0.42, 0.0] err=[-0.004, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-99.99663543701172, -59.4373664855957, 38.08668899536133, -0.5661380290985107]
  L: rigid_TCP(fwd,left,up)=[0.761, 0.086, 0.954]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.761, 0.083, 0.954] pad_end=[0.761, 0.088, 0.954] measured_pinch=[0.761, 0.086, 0.954]m
     close_dir=[0.0, 1.0, -0.05] fing_dir=[0.13, -0.05, -0.99] q=[-1.30832, 0.0561, -0.97217, -1.00321, 2.34499, 0.83544, 1.55999] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-2.5357916355133057, -1.1844197511672974, 0.5471392273902893, -1.9397170543670654, 0.08901982754468918, 0.010474979877471924, -0.019160380586981773] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.657, -0.161, 0.868]m fingers=[0.0315, 0.0311]m grip=command=0.0 finger_sum(6.3cm)
     pad_start=[0.652, -0.135, 0.857] pad_end=[0.662, -0.187, 0.879] measured_pinch=[0.657, -0.161, 0.868]m
     close_dir=[-0.17, 0.91, -0.38] fing_dir=[0.9, -0.02, -0.45] q=[-0.53227, -0.4377, 1.21206, -1.64415, -0.62312, 0.36721, -1.04797] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.001, -0.002, 0.001]rad limit_margins=[1.831, 0.602, 1.134, 0.44, 1.723, 0.67, 0.513]rad min=0.44rad
     q_cmd=[-0.53239, -0.43767, 1.2119, -1.64438, -0.62188, 0.36532, -1.04724] effort_Nm=[-2.559478521347046, 1.2561428546905518, -1.443030595779419, -5.165561676025391, 2.4585156440734863, -1.7370033264160156, -1.0124664306640625] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0022_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 22. Tuck left independently before carry

```python
s.act(**{'intent': 'Tuck left independently before carry', 'left': {'q': [0, 0, 0, 0, 0, 0, 0]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 4})
```
Result: reached; observation 23.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143457837887000_68b226a039b548358a9fd91bf611f50d.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0023.jpg`
Sim seconds: 66.16666666666667

```text
[obs #023 | act=8082555f | sim= 66.17s | wall= 544.2s | Tuck left independently before carry]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.737, -3.774, 0.0]m rel_yaw=-3.135rad vel=[0.0, -0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-6.555764198303223, -3.9990673065185547, 4.427917957305908, -0.14742672443389893]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-1e-05, -0.0, -1e-05, -0.0, 3e-05, -0.0, 0.0] q_lag=[0.0, 0.0, 0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.016621991991996765, -0.04733218252658844, -0.00024457648396492004, 0.0024661305360496044, -3.0454248189926147e-06, -0.00048124155728146434, -0.0012227082625031471] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.655, -0.161, 0.871]m fingers=[0.0315, 0.0311]m grip=command=0.0 finger_sum(6.3cm)
     pad_start=[0.65, -0.135, 0.86] pad_end=[0.66, -0.187, 0.882] measured_pinch=[0.655, -0.161, 0.871]m
     close_dir=[-0.17, 0.91, -0.38] fing_dir=[0.9, -0.02, -0.44] q=[-0.53228, -0.43768, 1.21205, -1.64422, -0.62255, 0.36723, -1.04798] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.001, -0.002, 0.001]rad limit_margins=[1.831, 0.602, 1.134, 0.44, 1.724, 0.67, 0.513]rad min=0.44rad
     q_cmd=[-0.53239, -0.43767, 1.2119, -1.64438, -0.62188, 0.36532, -1.04724] effort_Nm=[-3.6442458629608154, 0.9896451234817505, -1.802419900894165, -2.729485511779785, 1.7341220378875732, -1.2566901445388794, -0.7602591514587402] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0023_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 23. Raise fax overhead before crossing rails

```python
s.act(**{'intent': 'Raise fax overhead before crossing rails', 'left': None, 'right': {'q': [-2.6, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 4})
```
Result: reached; observation 24.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143470936244000_6179cff1fbb247769e8294ba8f509798.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0024.jpg`
Sim seconds: 68.96666666666667

```text
[obs #024 | act=7c0559f3 | sim= 68.97s | wall= 557.3s | Raise fax overhead before crossing rails]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.738, -3.774, 0.0]m rel_yaw=-3.133rad vel=[0.002, 0.0, -0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-39.506439208984375, -26.935333251953125, 20.037643432617188, -0.5697627067565918]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, 0.0, 2e-05, -3e-05, -0.0, 1e-05, -1e-05] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.989818811416626, -0.15283021330833435, -0.005069740116596222, 0.2433834820985794, -0.004131149500608444, 0.020946407690644264, -0.005175457801669836] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.871, -0.242, 1.689]m fingers=[0.0314, 0.0311]m grip=command=0.0 finger_sum(6.3cm)
     pad_start=[0.873, -0.214, 1.689] pad_end=[0.87, -0.271, 1.689] measured_pinch=[0.871, -0.242, 1.689]m
     close_dir=[0.07, 1.0, -0.0] fing_dir=[0.99, -0.07, -0.11] q=[-2.59986, 0.04999, -0.12851, -0.11976, 0.06834, 1.00048, -0.13962] q_lag=[-0.0, 0.0, -0.001, -0.0, -0.003, -0.0, -0.0]rad limit_margins=[1.841, 0.115, 2.218, 0.459, 2.278, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-10.013534545898438, 2.1633524894714355, -0.08765649795532227, -5.345002174377441, -0.33678802847862244, -2.7203338146209717, 0.7300726175308228] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0024_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 24. Carry first clear sixty centimetres between chair feet

```python
s.act(**{'intent': 'Carry first clear sixty centimetres between chair feet', 'left': None, 'right': None, 'base': {'fwd': 0.6}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 6})
```
Result: reached; observation 25.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143485952811000_4d07152589974435bbc2d149d6f826f6.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0025.jpg`
Sim seconds: 72.93333333333334

```text
[obs #025 | act=006ee62c | sim= 72.93s | wall= 572.2s | Carry first clear sixty centimetres between chair feet]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[1.142, -3.779, 0.0]m rel_yaw=-3.133rad vel=[0.0, -0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.432401180267334, -5.225789546966553, 5.787467956542969, -0.5522148609161377]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, 0.0, -1e-05, 0.0, -0.0, -0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.06255999952554703, -0.01887974888086319, 0.00023746397346258163, -0.023142922669649124, 0.0003093311097472906, -0.003810351248830557, -0.00013768579810857773] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0315, 0.0311]m grip=command=0.0 finger_sum(6.3cm)
     pad_start=[0.873, -0.213, 1.689] pad_end=[0.87, -0.27, 1.689] measured_pinch=[0.872, -0.241, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59985, 0.05003, -0.13045, -0.11973, 0.06503, 1.00016, -0.13962] q_lag=[-0.0, -0.0, 0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.117029190063477, -0.16493889689445496, 0.20583784580230713, -3.3513758182525635, 0.15387912094593048, -2.104142904281616, -0.009023554623126984] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0025_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 25. Carry second sixty centimetres central opening

```python
s.act(**{'intent': 'Carry second sixty centimetres central opening', 'left': None, 'right': None, 'base': {'fwd': 0.6}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 6})
```
Result: reached; observation 26.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143501373870000_5376546f857a461ba4882aeaf0b84ff5.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0026.jpg`
Sim seconds: 76.86666666666666

```text
[obs #026 | act=fdf62e5f | sim= 76.87s | wall= 587.9s | Carry second sixty centimetres central opening]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.547, -3.784, 0.0]m rel_yaw=-3.133rad vel=[0.0, 0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.555576324462891, -5.310628890991211, 5.820004463195801, -0.5590221881866455]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, 0.0, -1e-05, 0.0, -0.0, -0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.05630985647439957, 0.013675629161298275, 0.00037187058478593826, -0.020780570805072784, 0.000369061715900898, -0.003328248392790556, 0.000820355664473027] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0315, 0.0311]m grip=command=0.0 finger_sum(6.3cm)
     pad_start=[0.873, -0.213, 1.689] pad_end=[0.87, -0.27, 1.689] measured_pinch=[0.872, -0.241, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59985, 0.05003, -0.13044, -0.11973, 0.06503, 1.00016, -0.13962] q_lag=[-0.0, -0.0, 0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.108778953552246, -0.14511458575725555, 0.2063901424407959, -3.3498780727386475, 0.15356343984603882, -2.095005750656128, -0.00794927030801773] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0026_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 26. Advance .37 to placement turning stance

```python
s.act(**{'intent': 'Advance .37 to placement turning stance', 'left': None, 'right': None, 'base': {'fwd': 0.37}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 4})
```
Result: reached; observation 27.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143514131612000_4ecb881df93a463cb9ea4250bdf66d79.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0027.jpg`
Sim seconds: 79.66666666666667

```text
[obs #027 | act=4934617d | sim= 79.67s | wall= 600.4s | Advance .37 to placement turning stance]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.182, -3.787, 0.0]m rel_yaw=-3.132rad vel=[0.0, -0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.433194160461426, -5.235593318939209, 5.7749342918396, -0.535468578338623]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, -0.0, -1e-05, 0.0, -0.0, -0.0] q_lag=[0.0, -0.0, 0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.06672058254480362, -0.00666461419314146, 0.0004230053164064884, -0.023981157690286636, 0.00039471290074288845, -0.003674884559586644, -0.00020625385513994843] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0315, 0.0311]m grip=command=0.0 finger_sum(6.3cm)
     pad_start=[0.873, -0.213, 1.689] pad_end=[0.87, -0.27, 1.689] measured_pinch=[0.872, -0.241, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59985, 0.05003, -0.13045, -0.11973, 0.06503, 1.00016, -0.13962] q_lag=[-0.0, -0.0, 0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.096378326416016, -0.11749285459518433, 0.20750629901885986, -3.341684103012085, 0.15379486978054047, -2.100783586502075, -0.008371993899345398] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0027_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 27. First thirty right with fax above rails

```python
s.act(**{'intent': 'First thirty right with fax above rails', 'left': None, 'right': None, 'base': {'yaw_deg': -30}, 'torso': None, 'seconds': None, 'max_steps': None, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 4})
```
Result: reached; observation 28.

Receipt: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/receipt_01792143531623482000_49cd4c378aa3402bb2b517f2eb7fc402.json`
Image: `<observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0028.jpg`
Sim seconds: 82.26666666666667

```text
[obs #028 | act=bdfbbb74 | sim= 82.27s | wall= 618.1s | First thirty right with fax above rails]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.182, -3.787, 0.0]m rel_yaw=-3.651rad vel=[-0.001, -0.0, -0.002] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.65727424621582, -5.45514440536499, 5.870102405548096, -0.39351844787597656]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, -0.0, -1e-05, 0.0, -0.0, -0.0] q_lag=[0.0, -0.0, 0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.013464136980473995, -0.04302525147795677, -0.00018141232430934906, -0.005908693186938763, -4.5865774154663086e-05, -0.0011526752496138215, -0.0007235240191221237] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0315, 0.0311]m grip=command=0.0 finger_sum(6.3cm)
     pad_start=[0.873, -0.213, 1.689] pad_end=[0.87, -0.27, 1.689] measured_pinch=[0.872, -0.242, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59986, 0.05003, -0.13027, -0.11973, 0.06533, 1.0002, -0.13966] q_lag=[-0.0, -0.0, 0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.0941996574401855, 0.0381016731262207, 0.18109631538391113, -3.336271286010742, 0.11552953720092773, -2.0920135974884033, 0.04280668497085571] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-da80ba/fax-run-008-v6g-i115-a29/obs_0028_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```
