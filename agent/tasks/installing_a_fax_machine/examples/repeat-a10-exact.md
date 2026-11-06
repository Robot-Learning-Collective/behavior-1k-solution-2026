# a10 exact public action sequence

Historical record, not a blind replay script. Includes unsuccessful recovery motions and rejected requests; inspect images and remeasure before contacts. All arguments preserved, including max_steps.

## 1. Start clean square navigation

```python
s.act(**{'intent': 'Start clean square navigation', 'left': {'grip': 1}, 'right': {'grip': 1}, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 2.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121480334257000_9a8428fc543a4f30b7b6d73a04725257.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0002.jpg`
Sim seconds: 5.2

```text
[obs #002 | act=8d403f71 | sim=  5.20s | wall=   7.2s | Start clean square navigation]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-0.0, -0.0, 0.0]m rel_yaw=-1.566rad vel=[-0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.026066377758979797, 0.08677893877029419, -0.023160815238952637, -0.07109510898590088]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.04235760122537613, -0.12107288092374802, -0.0016268196050077677, -0.012282192707061768, -0.0012888094643130898, -0.001596243353560567, -0.005984261631965637] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.01004391722381115, -0.11951792240142822, -0.001534906099550426, 0.0003752545453608036, -0.001284857396967709, -0.0004584453708957881, -0.006329148076474667] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0002_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 2. Clear aisle centered approach

```python
s.act(**{'intent': 'Clear aisle centered approach', 'left': None, 'right': None, 'base': {'fwd': 1.0}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 3.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121488213420000_eb6a7333921b44eaac209e7e28ff0bf3.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0003.jpg`
Sim seconds: 11.166666666666666

```text
[obs #003 | act=3a433145 | sim= 11.17s | wall=  15.0s | Clear aisle centered approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.005, -0.995, 0.0]m rel_yaw=-1.566rad vel=[0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.5733201503753662, 0.30627280473709106, -0.1295676827430725, 0.02258814312517643]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.06234970688819885, 0.09116644412279129, 0.002719627693295479, -0.02144102193415165, 0.0022952526342123747, -0.0028835509438067675, 0.0055376035161316395] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.0696013867855072, 0.09700844436883926, 0.0022644074633717537, -0.022657280787825584, 0.0019682985730469227, -0.0033987367060035467, 0.006049242801964283] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0003_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 3. Clear aisle centered approach

```python
s.act(**{'intent': 'Clear aisle centered approach', 'left': None, 'right': None, 'base': {'fwd': 0.8}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 4.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121494777515000_bcf0bfac36b5418ca624ada22841f722.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0004.jpg`
Sim seconds: 16.133333333333333

```text
[obs #004 | act=b9fad0af | sim= 16.13s | wall=  21.7s | Clear aisle centered approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.008, -1.791, 0.0]m rel_yaw=-1.566rad vel=[-0.001, -0.0, -0.001] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.44779863953590393, 0.5992990136146545, -0.17607799172401428, -0.00038455030880868435]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.10154988616704941, -0.019381076097488403, -0.0008325244998559356, -0.03544515371322632, -0.0006053814431652427, -0.005577830132097006, -0.00221998686902225] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, 0.0, -0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.0923968181014061, -0.023030556738376617, -0.0011786173563450575, -0.03127840906381607, -0.0008920020773075521, -0.005119632463902235, -0.002404451137408614] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0004_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 4. Clear aisle centered approach

```python
s.act(**{'intent': 'Clear aisle centered approach', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 5.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121501620347000_3812bd828ac543b28d1ad7a6f4d8d7dd.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0005.jpg`
Sim seconds: 21.333333333333332

```text
[obs #005 | act=0bb46f4e | sim= 21.33s | wall=  28.5s | Clear aisle centered approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.008, -1.791, 0.0]m rel_yaw=-3.132rad vel=[-0.0, -0.001, -0.001] | torso=[1.025, -1.45, -0.47, -0.0] err=[-0.0, -0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.5583339929580688, -0.14204423129558563, 0.11279131472110748, -0.027255820110440254]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.04, 0.0, -1.0] q=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.0002342322695767507, -0.2282145470380783, -0.0028561055660247803, -0.0027428902685642242, -0.00205131433904171, -0.0017790767597034574, -0.007872024551033974] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.0277657862752676, -0.22422750294208527, -0.0025924593210220337, 0.006703008431941271, -0.0019941385835409164, 0.0008283877396024764, -0.008103634230792522] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0005_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 5. Clear aisle centered approach

```python
s.act(**{'intent': 'Clear aisle centered approach', 'left': None, 'right': None, 'base': {'left': 0.5}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 6.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121506759163000_f7ef5885b7d241988dd3c7714cf40675.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0006.jpg`
Sim seconds: 24.8

```text
[obs #006 | act=b92df688 | sim= 24.80s | wall=  33.7s | Clear aisle centered approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.013, -2.286, 0.0]m rel_yaw=-3.133rad vel=[0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.036160774528980255, 0.06493433564901352, -0.021164938807487488, 0.01398615725338459]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.004726368468254805, 0.0284117441624403, 0.0007884856313467026, 0.0019286018796265125, 0.0006645484827458858, 0.00018075467960443348, 0.0020852270536124706] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.006631708703935146, 0.029982438310980797, 0.000758846290409565, -0.001503153471276164, 0.0006650788709521294, -0.00019079481717199087, 0.002385105937719345] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0006_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 6. Clear aisle centered approach

```python
s.act(**{'intent': 'Clear aisle centered approach', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 7.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121515774630000_1bce979a413c4a9aaefb5e747a0cb0a9.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0007.jpg`
Sim seconds: 31.766666666666666

```text
[obs #007 | act=a1f652bf | sim= 31.77s | wall=  42.6s | Clear aisle centered approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-1.182, -2.297, 0.0]m rel_yaw=-3.133rad vel=[0.0, -0.0, 0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.44234398007392883, 0.5136281251907349, -0.1765616089105606, -0.016479451209306717]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, -0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.08763719350099564, -0.05694076791405678, 0.0001956680789589882, -0.02933606132864952, 0.00039118784479796886, -0.0044141774997115135, -0.0013976721093058586] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, 0.0, -0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.07152719050645828, -0.05083392560482025, -0.0001086704432964325, -0.024338776245713234, 0.00011830450966954231, -0.003919227048754692, -0.0012058746069669724] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0007_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 7. Clear aisle centered approach

```python
s.act(**{'intent': 'Clear aisle centered approach', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 8.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121524798557000_396f89144d2442feb106682a81ab0e89.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0008.jpg`
Sim seconds: 38.733333333333334

```text
[obs #008 | act=65873338 | sim= 38.73s | wall=  51.7s | Clear aisle centered approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-2.378, -2.308, 0.0]m rel_yaw=-3.133rad vel=[-0.0, -0.001, 0.001] | torso=[1.025, -1.45, -0.47, 0.0] err=[-0.0, -0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.3924200236797333, -0.11814061552286148, 0.11803428828716278, -0.0713786780834198]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.05693739652633667, -0.07782607525587082, -0.0024909903295338154, -0.023262526839971542, -0.002144823782145977, -0.00391731970012188, -0.007496873382478952] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[3.9088343328330666e-05, -0.08667437732219696, -0.0024699904024600983, -0.007017737720161676, -0.0021995417773723602, -0.0024437105748802423, -0.008323240093886852] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0008_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 8. Clear aisle centered approach

```python
s.act(**{'intent': 'Clear aisle centered approach', 'left': None, 'right': None, 'base': {'fwd': 1.15}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 9.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121533759644000_21505b587668402eaf632547f72e3423.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0009.jpg`
Sim seconds: 45.46666666666667

```text
[obs #009 | act=4abb0d71 | sim= 45.47s | wall=  60.6s | Clear aisle centered approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-3.523, -2.318, 0.0]m rel_yaw=-3.133rad vel=[-0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, 0.0] err=[-0.0, -0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.17570097744464874, -0.01811615191400051, 0.022397272288799286, -0.0742415338754654]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.08760276436805725, 0.011480853892862797, -0.002054678276181221, -0.03195041045546532, -0.0020079733803868294, -0.004456621594727039, -0.005280197132378817] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.017957566305994987, -0.006195253226906061, -0.0022665560245513916, -0.011710882186889648, -0.0021847099997103214, -0.002839946886524558, -0.006288513075560331] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0009_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 9. Clear aisle centered approach

```python
s.act(**{'intent': 'Clear aisle centered approach', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 10.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121541020610000_01a3d10050a7490483bac038f900f4e8.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0010.jpg`
Sim seconds: 50.666666666666664

```text
[obs #010 | act=ffd2784c | sim= 50.67s | wall=  67.8s | Clear aisle centered approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-3.523, -2.318, 0.0]m rel_yaw=-4.699rad vel=[-0.0, -0.0, 0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[-0.0, -0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.5682740807533264, -0.31846919655799866, 0.1651797592639923, -0.03702668845653534]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.013120850548148155, -0.09239443391561508, -0.0022380948066711426, 0.0008705584914423525, -0.0019186325371265411, -0.0005275349249131978, -0.0061806924641132355] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.05273866280913353, -0.09721934795379639, -0.0020477548241615295, 0.014962561428546906, -0.001839788630604744, 0.001768456306308508, -0.006793624721467495] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0010_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 10. Clear aisle centered approach

```python
s.act(**{'intent': 'Clear aisle centered approach', 'left': None, 'right': None, 'base': {'left': 0.48}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 11.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121546129047000_20e15e878e144f3ca8120f835bdee8b0.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0011.jpg`
Sim seconds: 54.03333333333333

```text
[obs #011 | act=69ff76ef | sim= 54.03s | wall=  73.0s | Clear aisle centered approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-3.998, -2.324, 0.0]m rel_yaw=-4.699rad vel=[-0.0, -0.0, -0.001] | torso=[1.025, -1.45, -0.47, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.3015041947364807, -0.01110793836414814, -0.03743135929107666, 0.014397591352462769]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, 0.0] q_lag=[0.0, -0.0, 0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.006032630801200867, 0.20070120692253113, 0.002693653106689453, 0.004618034698069096, 0.0020722970366477966, 0.00150848098564893, 0.009134183637797832] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.010935286059975624, 0.1966182291507721, 0.0025255680084228516, -0.003197240177541971, 0.0020333342254161835, -0.0003083248157054186, 0.009614522568881512] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0011_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 11. Set narrow elbows before gap entry

```python
s.act(**{'intent': 'Set narrow elbows before gap entry', 'left': {'q': [-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56]}, 'right': {'q': [-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 12.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121579617615000_0e250071628047cb8b14e3908ba0495e.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0012.jpg`
Sim seconds: 57.2

```text
[obs #012 | act=02e48ba1 | sim= 57.20s | wall= 106.5s | Set narrow elbows before gap entry]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-3.998, -2.325, 0.0]m rel_yaw=-4.699rad vel=[0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.535383939743042, 0.2828078269958496, -0.18132875859737396, 0.4467199444770813]
  L: rigid_TCP(fwd,left,up)=[0.705, 0.086, 0.997]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.705, 0.133, 0.994] pad_end=[0.704, 0.038, 0.999] measured_pinch=[0.705, 0.086, 0.997]m
     close_dir=[0.01, 1.0, -0.05] fing_dir=[0.34, -0.05, -0.94] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.34498, 0.83545, 1.56] q_lag=[-0.0, 0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.032132674008607864, 0.1654064804315567, 0.013781647197902203, 0.04564201459288597, -0.010712469927966595, -0.002215595915913582, 0.013096177019178867] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.505, -0.27, 0.649]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.505, -0.223, 0.649] pad_end=[0.504, -0.318, 0.649] measured_pinch=[0.505, -0.27, 0.649]m
     close_dir=[0.01, 1.0, -0.0] fing_dir=[-0.03, -0.0, -1.0] q=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] q_lag=[0.0, 0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[-0.07315071672201157, 0.10808622092008591, 0.010903753340244293, -0.016193369403481483, 0.0033284053206443787, -0.003318355418741703, 0.00029605627059936523] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0012_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 12. Enter centered gap with narrow elbows

```python
s.act(**{'intent': 'Enter centered gap with narrow elbows', 'left': None, 'right': None, 'base': {'fwd': 1.07}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 13.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121587822346000_c365d7c5104846e98c3bc019fdc69c7a.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0013.jpg`
Sim seconds: 63.53333333333333

```text
[obs #013 | act=56a28555 | sim= 63.53s | wall= 114.7s | Enter centered gap with narrow elbows]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.26, 0.0]m rel_yaw=-4.699rad vel=[0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[1.5562607049942017, 1.13150954246521, -0.6706279516220093, -0.22254233062267303]
  L: rigid_TCP(fwd,left,up)=[0.705, 0.086, 0.997]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.705, 0.133, 0.994] pad_end=[0.704, 0.038, 0.999] measured_pinch=[0.705, 0.086, 0.997]m
     close_dir=[0.01, 1.0, -0.05] fing_dir=[0.34, -0.05, -0.94] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, -0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.0381879061460495, -0.07933539152145386, -0.02387646771967411, 0.028232764452695847, -0.000921894796192646, 0.0001245671883225441, -0.0030105167534202337] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.505, -0.27, 0.649]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.505, -0.223, 0.649] pad_end=[0.504, -0.318, 0.649] measured_pinch=[0.505, -0.27, 0.649]m
     close_dir=[0.01, 1.0, -0.0] fing_dir=[-0.03, -0.0, -1.0] q=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[-0.008296752348542213, -0.06865397095680237, -0.011445848271250725, 0.024335987865924835, -0.001730459975078702, -0.0007295248215086758, 0.0013872396666556597] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0013_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 13. Crouch with narrow elbow clearance

```python
s.act(**{'intent': 'Crouch with narrow elbow clearance', 'left': None, 'right': None, 'base': None, 'torso': {'q': [1.68, -2.54, -1.62, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 14.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121591721974000_4a4abcd567e945b78e0cc3d2cdb3b854.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0014.jpg`
Sim seconds: 65.1

```text
[obs #014 | act=a668d865 | sim= 65.10s | wall= 118.6s | Crouch with narrow elbow clearance]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.26, 0.0]m rel_yaw=-4.700rad vel=[0.0, 0.0, -0.0] | torso=[1.687, -2.54, -1.62, 0.0] err=[-0.007, -0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-100.00013732910156, -46.44306564331055, 60.01901626586914, 0.18420633673667908]
  L: rigid_TCP(fwd,left,up)=[0.631, 0.086, 0.25]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.63, 0.133, 0.248] pad_end=[0.633, 0.038, 0.252] measured_pinch=[0.631, 0.086, 0.25]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.37, -0.05, -0.93] q=[-1.30825, 0.05613, -0.97218, -1.0032, 2.34496, 0.83543, 1.55998] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-6.313240051269531, -2.2787179946899414, 1.4781757593154907, -3.904500961303711, 0.1263250708580017, 0.019177481532096863, -0.0715993344783783] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.251, -0.27, 0.121]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.252, -0.223, 0.121] pad_end=[0.251, -0.318, 0.122] measured_pinch=[0.251, -0.27, 0.121]m
     close_dir=[0.01, 1.0, -0.01] fing_dir=[-0.68, -0.0, -0.73] q=[-0.52689, -0.35922, 0.79381, -0.97008, -1.51886, 1.03599, -0.79466] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[0.8329900503158569, -0.9759005308151245, -0.3250521123409271, -1.4144797325134277, -0.013617157936096191, 0.05050294101238251, -0.02079709991812706] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0014_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 14. Reach above floor fax

```python
s.act(**{'intent': 'Reach above floor fax', 'left': None, 'right': {'to': [0.61, -0.3, 0.15], 'finger_dir': [0, 0, -1], 'close_dir': [0, 1, 0]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 15.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121614825511000_a284f2ceed2c4e348f5a43b1023d6079.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0015.jpg`
Sim seconds: 65.7

```text
[obs #015 | act=0b84d655 | sim= 65.70s | wall= 141.7s | Reach above floor fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.26, 0.0]m rel_yaw=-4.700rad vel=[0.001, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-0.11940038204193115, -0.03461708500981331, 0.056157186627388, -0.06301681697368622]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.631, 0.133, 0.252] pad_end=[0.633, 0.038, 0.257] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.017155112698674202, -0.02148560993373394, 0.0016900687478482723, -0.009172497317194939, 0.0010301326401531696, 0.00021272513549774885, -0.0011664247140288353] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.61, -0.299, 0.151]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.61, -0.252, 0.151] pad_end=[0.61, -0.347, 0.151] measured_pinch=[0.61, -0.3, 0.151]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.0, -0.0, -1.0] q=[-0.93471, -0.47131, 0.77643, -1.11647, -1.27483, 0.84647, -0.57795] q_lag=[-0.0, 0.0, 0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[2.234, 0.636, 1.57, 0.968, 1.071, 0.191, 0.983]rad min=0.191rad
     q_cmd=[-0.93472, -0.47131, 0.77644, -1.11646, -1.27483, 0.84648, -0.57793] effort_Nm=[0.0484672449529171, -0.013994916342198849, 0.0090646268799901, 0.005998308304697275, -0.0010917203035205603, 0.0024711417499929667, -0.0006355408695526421] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0015_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 15. Lower pads to casing sides

```python
s.act(**{'intent': 'Lower pads to casing sides', 'left': None, 'right': {'to': [0.61, -0.3, 0.035]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: stalled; observation 16.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121626143580000_07a0639e1def4bab9353efad3135fec6.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0016.jpg`
Sim seconds: 68.26666666666667

```text
[obs #016 | act=cf016a38 | sim= 68.27s | wall= 153.0s | Lower pads to casing sides]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.261, 0.0]m rel_yaw=-4.700rad vel=[-0.001, -0.001, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[3.6418004035949707, 1.1152201890945435, -2.2416462898254395, 5.560863494873047]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.631, 0.133, 0.252] pad_end=[0.633, 0.038, 0.257] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30833, 0.05612, -0.97214, -1.00325, 2.34502, 0.83543, 1.56004] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.008381993509829044, 0.0015659909695386887, 0.0028909093234688044, -0.00437808595597744, -0.0008716150186955929, -9.69726825132966e-05, 6.0330028645694256e-05] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.299, 0.051]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.602, -0.252, 0.051] pad_end=[0.603, -0.347, 0.051] measured_pinch=[0.603, -0.3, 0.051]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17897, -0.09574, 1.07758, -0.03424, -1.04423, 0.43282, 0.07094] q_lag=[0.0, 0.0, -0.003, -0.0, -0.002, 0.0, 0.0]rad limit_margins=[2.478, 0.26, 1.269, 0.373, 1.302, 0.604, 1.49]rad min=0.26rad
     q_cmd=[-1.17896, -0.09565, 1.07456, -0.03462, -1.04588, 0.43301, 0.07119] effort_Nm=[-0.01165442168712616, 4.693645477294922, -0.5608134269714355, -2.649458408355713, -0.6016621589660645, -0.49469488859176636, 1.5536692142486572] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"IK_stalled","causes":["IK_stalled"],"confidence":"limited","plateau":true,"normalized_error_history":[23.212568349599543,23.09851836988612,23.65878254739267,24.875533332030397,26.675545269036114,27.261750120350875,27.625154612900644,27.65581559065218,27.03061677463417,27.279684729819053,27.18267712741731,27.248629752987224,27.246714026813116,27.01234232604646,26.589206839551526,26.23828037003038,25.879190488927012,25.5324821917708,25.190255830575452,24.786564956513267,23.869966359672794,23.207616974754693,21.246785972893882,20.951429951459346,20.020599612846876,19.320103294047065,18.537502408112932,17.775069214783112,17.5012984757878,17.166263551731895,16.61522198990217,15.975491443101133,15.489703689454995,14.890800379393468,14.260448358748514,13.792191826534278,13.449333636191898,13.117659540205286,12.98518271659976,12.66831157263444,12.26509713927077,12.052780076140525,11.976496880022182,11.968999132867179,11.992513216403259,11.974589231550544,11.811456631713174,11.801955490312498,11.747300738663613,11.766267137547398,11.74901295007031,11.744308310357368,11.718600360513108,11.678322111935474,11.696838420213044,11.586266168306414,11.59698210294711,11.34615918376861,10.414604063576292,10.074639412245132,3.7026863851968552,3.521728907439486,3.5248337258768623,3.5122553881359293,3.519813970613001,3.519729390241471,3.5198617506907204,3.519738887567356,3.519796564596334,3.519729935814217,3.5198144313689683,3.5196872173222378,3.519741849879681,3.5196576532092805,3.5197260259445984,3.519888826177861,3.519694243160249,3.519807475765359],"normalized_progress":19.692760873834185,"recent_max_joint_lag_rad":[0.0030231475830078125,0.0030318498611450195,0.003020644187927246],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"}}
  status=stalled fault=None uncertain=False pending=['right']
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0016_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 16. Hold achieved low pose and grasp

```python
s.act(**{'intent': 'Hold achieved low pose and grasp', 'left': {'grip': 0}, 'right': {'q': [-1.17897, -0.09574, 1.07758, -0.03424, -1.04423, 0.43282, 0.07094], 'grip': 0}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': True, 'timeout_seconds': 30.0})
```
Result: stalled; observation 17.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121635975535000_9c63d38549c04abca5bc9c6cfac00105.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0017.jpg`
Sim seconds: 68.9

```text
[obs #017 | act=19307e89 | sim= 68.90s | wall= 162.9s | Hold achieved low pose and grasp]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.261, 0.0]m rel_yaw=-4.700rad vel=[-0.0, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[32.651390075683594, 12.011180877685547, -21.914974212646484, 14.662269592285156]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.255] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30833, 0.0561, -0.97214, -1.00324, 2.345, 0.83545, 1.56002] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.01615406572818756, -0.006051655858755112, -0.005021304823458195, -0.0003682116512209177, 0.0005174509715288877, 3.165926318615675e-05, 0.00013555248733609915] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.3, 0.051]m fingers=[0.0318, 0.043]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.602, -0.271, 0.051] pad_end=[0.603, -0.34, 0.051] measured_pinch=[0.603, -0.305, 0.051]m
     close_dir=[-0.01, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17896, -0.09573, 1.07824, -0.03387, -1.04325, 0.43278, 0.07093] q_lag=[-0.0, -0.0, -0.001, -0.0, -0.001, 0.0, 0.0]rad limit_margins=[2.478, 0.26, 1.268, 0.373, 1.303, 0.604, 1.49]rad min=0.26rad
     q_cmd=[-1.17897, -0.09574, 1.07758, -0.03424, -1.04423, 0.43282, 0.07094] effort_Nm=[3.9203550815582275, 3.776817798614502, 0.031220436096191406, -1.5033714771270752, -0.01262807846069336, -2.7460005283355713, 0.6504768133163452] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=stalled fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0017_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 17. Lift and verify acquisition

```python
s.act(**{'intent': 'Lift and verify acquisition', 'left': None, 'right': {'to': [0.603, -0.299, 0.2]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 18.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121640605065000_54228148b2de4e178d7e8978d3ab3df4.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0018.jpg`
Sim seconds: 71.56666666666666

```text
[obs #018 | act=980646fa | sim= 71.57s | wall= 167.5s | Lift and verify acquisition]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.261, 0.0]m rel_yaw=-4.700rad vel=[0.001, 0.0, 0.001] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.884102821350098, -2.221179723739624, 3.662167549133301, -0.7626242637634277]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30835, 0.05609, -0.97215, -1.00322, 2.34501, 0.83545, 1.56] q_lag=[0.0, 0.0, 0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.02773257903754711, 0.024833975359797478, -0.005210996605455875, 0.02238413691520691, -0.002676016418263316, -0.0005755146266892552, 0.0029941352549940348] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.303, 0.2]m fingers=[0.0317, 0.0426]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.603, -0.274, 0.199] pad_end=[0.603, -0.343, 0.201] measured_pinch=[0.603, -0.309, 0.2]m
     close_dir=[-0.0, 1.0, -0.02] fing_dir=[0.0, -0.02, -1.0] q=[-0.98928, -0.6407, 0.96171, -1.39058, -1.64834, 0.76484, -0.86138] q_lag=[-0.0, 0.0, -0.0, 0.0, -0.0, -0.001, -0.0]rad limit_margins=[2.288, 0.805, 1.384, 0.694, 0.698, 0.272, 0.699]rad min=0.272rad
     q_cmd=[-0.98937, -0.64068, 0.9617, -1.39058, -1.64846, 0.76429, -0.86169] effort_Nm=[-1.6818640232086182, 0.5241329073905945, -0.8249987363815308, -1.8971954584121704, -0.0005526542663574219, -0.14537981152534485, 0.21359820663928986] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0018_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 18. Present fax switch

```python
s.act(**{'intent': 'Present fax switch', 'left': {'to': [0.58, -0.06, 0.36], 'finger_dir': [0.220337, -0.708506, -0.670426], 'close_dir': [-0.038811, 0.680406, -0.731807]}, 'right': {'to': [0.5, -0.08, 0.23], 'pitch_deg': 35}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 19.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121651485801000_c1fd3134001b470a9ed8c7621ab2b9ed.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0019.jpg`
Sim seconds: 72.63333333333334

```text
[obs #019 | act=c820ce7b | sim= 72.63s | wall= 178.4s | Present fax switch]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.261, 0.0]m rel_yaw=-4.700rad vel=[-0.0, -0.0, 0.001] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.585366249084473, -2.184657573699951, 4.059717178344727, -0.3780554533004761]
  L: rigid_TCP(fwd,left,up)=[0.581, -0.06, 0.358]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.581, -0.062, 0.361] pad_end=[0.581, -0.058, 0.357] measured_pinch=[0.581, -0.06, 0.359]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.87845, 0.21564, -1.02692, -1.77818, 1.68529, 0.34264, 0.79112] q_lag=[0.0, -0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.177, 0.38, 1.319, 0.306, 0.661, 0.695, 0.77]rad min=0.306rad
     q_cmd=[-0.87845, 0.21564, -1.02692, -1.77822, 1.68526, 0.34266, 0.79109] effort_Nm=[0.03756505995988846, 0.058433882892131805, -0.0018884949386119843, 0.06675788760185242, -0.0021639447659254074, -0.00045409519225358963, 0.014884724281728268] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.497, -0.08, 0.228]m fingers=[0.0316, 0.0426]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.497, -0.052, 0.227] pad_end=[0.497, -0.121, 0.229] measured_pinch=[0.497, -0.086, 0.228]m
     close_dir=[0.0, 1.0, -0.03] fing_dir=[0.56, -0.02, -0.83] q=[-0.63692, -0.21602, 1.36818, -1.50979, -0.87355, -0.00982, -1.25166] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.936, 0.381, 0.978, 0.575, 1.473, 1.027, 0.309]rad min=0.309rad
     q_cmd=[-0.63695, -0.21599, 1.36817, -1.50985, -0.87346, -0.01071, -1.25158] effort_Nm=[-1.6699755191802979, 1.3829686641693115, -0.21971318125724792, -2.233048439025879, 1.4398459196090698, -0.46951040625572205, -0.058396972715854645] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0019_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 19. Approach measured switch

```python
s.act(**{'intent': 'Approach measured switch', 'left': {'to': [0.6062695288658142, -0.0881230241060257, 0.3157906723022461]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 20.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121661472976000_50f3bb9fa1e24daab0628f3327045965.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0020.jpg`
Sim seconds: 73.03333333333333

```text
[obs #020 | act=8c3d255f | sim= 73.03s | wall= 188.4s | Approach measured switch]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.261, 0.0]m rel_yaw=-4.700rad vel=[0.0, 0.0, -0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.845418930053711, -1.7789807319641113, 3.612830877304077, -0.35216936469078064]
  L: rigid_TCP(fwd,left,up)=[0.606, -0.088, 0.317]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.606, -0.089, 0.319] pad_end=[0.606, -0.086, 0.315] measured_pinch=[0.606, -0.088, 0.317]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.94147, 0.11643, -1.05005, -1.50704, 1.63221, 0.34332, 0.62695] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, -0.0, -0.0]rad limit_margins=[2.24, 0.281, 1.296, 0.577, 0.714, 0.694, 0.934]rad min=0.281rad
     q_cmd=[-0.94147, 0.11642, -1.05005, -1.50701, 1.63222, 0.34331, 0.62693] effort_Nm=[-0.013860979117453098, -0.010025876574218273, 0.0037754704244434834, -0.033841319382190704, 0.0005261525511741638, -0.00023145857267081738, -0.005409708712249994] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.497, -0.08, 0.228]m fingers=[0.0316, 0.0426]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.497, -0.052, 0.227] pad_end=[0.497, -0.121, 0.229] measured_pinch=[0.497, -0.086, 0.228]m
     close_dir=[0.0, 1.0, -0.03] fing_dir=[0.56, -0.02, -0.83] q=[-0.63691, -0.21601, 1.36818, -1.50978, -0.87353, -0.00983, -1.25167] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.936, 0.381, 0.978, 0.575, 1.473, 1.027, 0.309]rad min=0.309rad
     q_cmd=[-0.63695, -0.21599, 1.36817, -1.50985, -0.87346, -0.01071, -1.25158] effort_Nm=[-1.580012321472168, 1.3403563499450684, -0.17931467294692993, -2.157500982284546, 1.4139783382415771, -0.4543774127960205, -0.06257504969835281] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0020_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 20. Press switch

```python
s.act(**{'intent': 'Press switch', 'left': {'to': [0.6227929382324219, -0.10746880555152893, 0.29089876532554626]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: stalled; observation 21.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121673217155000_8c0e21f337b6481cae80cf79024ca1ac.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0021.jpg`
Sim seconds: 73.8

```text
[obs #021 | act=3abb200f | sim= 73.80s | wall= 200.2s | Press switch]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.26, 0.0]m rel_yaw=-4.700rad vel=[0.001, -0.0, 0.001] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.008292198181152, -2.0768520832061768, 3.675654888153076, -0.384978711605072]
  L: rigid_TCP(fwd,left,up)=[0.622, -0.114, 0.303]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm) TRACKING_ERROR(q4=+0.027)
     pad_start=[0.622, -0.116, 0.305] pad_end=[0.622, -0.112, 0.302] measured_pinch=[0.622, -0.114, 0.304]m
     close_dir=[-0.04, 0.66, -0.75] fing_dir=[0.22, -0.73, -0.65] q=[-0.99198, 0.03785, -1.06564, -1.33681, 1.61175, 0.33574, 0.51369] q_lag=[0.0, 0.0, 0.001, 0.027, -0.01, 0.002, 0.002]rad limit_margins=[2.291, 0.202, 1.281, 0.748, 0.734, 0.701, 1.047]rad min=0.202rad
     q_cmd=[-0.99189, 0.03821, -1.06505, -1.30984, 1.60222, 0.33805, 0.51593] effort_Nm=[3.9619736671447754, 25.53565216064453, 3.833071708679199, 25.00000762939453, -4.919719696044922, -3.161848306655884, 10.350753784179688] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.496, -0.08, 0.227]m fingers=[0.0316, 0.0426]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.496, -0.052, 0.226] pad_end=[0.496, -0.121, 0.228] measured_pinch=[0.496, -0.086, 0.227]m
     close_dir=[-0.0, 1.0, -0.03] fing_dir=[0.55, -0.02, -0.83] q=[-0.63681, -0.21615, 1.36866, -1.50906, -0.87606, -0.00868, -1.25118] q_lag=[-0.0, 0.0, -0.0, -0.001, 0.003, -0.002, -0.0]rad limit_margins=[1.936, 0.381, 0.978, 0.575, 1.47, 1.029, 0.31]rad min=0.31rad
     q_cmd=[-0.63695, -0.21599, 1.36817, -1.50985, -0.87346, -0.01071, -1.25158] effort_Nm=[-5.454596519470215, 6.809652805328369, 1.5670166015625, -15.310291290283203, 12.853163719177246, -4.747609615325928, -3.7976465225219727] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"blocked","causes":["blocked"],"confidence":"suspected","plateau":true,"normalized_error_history":[7.373304132632153,6.846477598285423,7.8238795255619,8.347507009132459,7.271179028807626,5.434697246841626,3.5870266515694755,2.7461528103136597,2.8176394166873457,2.7923444641154993,2.7933124541628445,2.7936170295670832,2.7878886330546715,2.7871427973984315,2.7873150574549745,2.7872137689910548,2.7861639796225077,2.777899418798597,2.7788599806117342,2.7791344629911148,2.7789568508939446,2.7787421114352036,2.779247793006411,2.779205673818959],"normalized_progress":4.594098458813194,"recent_max_joint_lag_rad":[0.026969194412231445,0.02697134017944336,0.02697432041168213],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=stalled fault=None uncertain=False pending=['left']
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0021_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 21. Withdraw switch hand

```python
s.act(**{'intent': 'Withdraw switch hand', 'left': {'to': [0.61, -0.04, 0.36]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 22.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121675937971000_2b3333059aa24858a474743cb6813230.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0022.jpg`
Sim seconds: 74.43333333333334

```text
[obs #022 | act=72d4a571 | sim= 74.43s | wall= 202.6s | Withdraw switch hand]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.26, 0.0]m rel_yaw=-4.700rad vel=[-0.0, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.133733749389648, -2.3527166843414307, 3.542266368865967, -1.1082779169082642]
  L: rigid_TCP(fwd,left,up)=[0.61, -0.04, 0.359]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.61, -0.042, 0.361] pad_end=[0.61, -0.039, 0.357] measured_pinch=[0.61, -0.041, 0.359]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.92921, 0.2513, -0.96751, -1.74964, 1.74968, 0.40474, 0.76664] q_lag=[0.0, 0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.228, 0.416, 1.379, 0.335, 0.597, 0.632, 0.794]rad min=0.335rad
     q_cmd=[-0.9292, 0.25131, -0.96751, -1.74966, 1.74967, 0.40474, 0.76663] effort_Nm=[0.053910404443740845, 0.05890706181526184, -0.0005807559937238693, 0.024617578834295273, -0.000771054532378912, -0.00039539323188364506, 0.005063544027507305] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.497, -0.08, 0.228]m fingers=[0.0315, 0.0427]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.497, -0.052, 0.227] pad_end=[0.497, -0.121, 0.229] measured_pinch=[0.497, -0.086, 0.228]m
     close_dir=[0.0, 1.0, -0.03] fing_dir=[0.56, -0.02, -0.83] q=[-0.63691, -0.21601, 1.36819, -1.50978, -0.87354, -0.00989, -1.25159] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.936, 0.381, 0.978, 0.575, 1.473, 1.027, 0.309]rad min=0.309rad
     q_cmd=[-0.63695, -0.21599, 1.36817, -1.50985, -0.87346, -0.01071, -1.25158] effort_Nm=[-1.0073729753494263, 0.7418758273124695, -0.20259559154510498, -1.8684873580932617, 1.3220800161361694, -0.510224461555481, -0.271531343460083] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0022_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 22. Stand with fax

```python
s.act(**{'intent': 'Stand with fax', 'left': None, 'right': None, 'base': None, 'torso': {'q': [0.84, -1.00609, -0.42, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 23.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121688402658000_dc91825e0ab842aa956d8c8233eceaf9.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0023.jpg`
Sim seconds: 76.53333333333333

```text
[obs #023 | act=58e14418 | sim= 76.53s | wall= 215.2s | Stand with fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.261, 0.0]m rel_yaw=-4.700rad vel=[0.001, 0.0, 0.001] | torso=[0.842, -1.006, -0.42, -0.0] err=[-0.002, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-99.9972915649414, -58.63388442993164, 36.74938201904297, 0.32250145077705383]
  L: rigid_TCP(fwd,left,up)=[0.691, -0.04, 1.037]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.69, -0.042, 1.038] pad_end=[0.691, -0.039, 1.035] measured_pinch=[0.691, -0.041, 1.037]m
     close_dir=[0.32, 0.68, -0.66] fing_dir=[0.52, -0.71, -0.49] q=[-0.92921, 0.25132, -0.96751, -1.74965, 1.74956, 0.40479, 0.76665] q_lag=[0.0, -0.0, -0.0, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[2.228, 0.416, 1.379, 0.335, 0.597, 0.632, 0.794]rad min=0.335rad
     q_cmd=[-0.9292, 0.25131, -0.96751, -1.74966, 1.74967, 0.40474, 0.76663] effort_Nm=[-0.2571016252040863, -0.9241611957550049, -0.00838923454284668, -2.430318832397461, 0.07741446793079376, 0.036692045629024506, -0.26122114062309265] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.654, -0.08, 0.867]m fingers=[0.0316, 0.0427]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.655, -0.052, 0.866] pad_end=[0.654, -0.121, 0.868] measured_pinch=[0.654, -0.086, 0.867]m
     close_dir=[0.01, 1.0, -0.02] fing_dir=[0.89, -0.02, -0.46] q=[-0.63685, -0.21605, 1.36819, -1.50971, -0.87374, -0.00993, -1.25158] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, -0.0]rad limit_margins=[1.936, 0.381, 0.978, 0.575, 1.472, 1.027, 0.309]rad min=0.309rad
     q_cmd=[-0.63695, -0.21599, 1.36817, -1.50985, -0.87346, -0.01071, -1.25158] effort_Nm=[-2.636357307434082, 2.716395139694214, -0.674961507320404, -4.679726600646973, 2.653855800628662, -0.8132320046424866, -0.00022000260651111603] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0023_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 23. Overhead divider clearance carry

```python
s.act(**{'intent': 'Overhead divider clearance carry', 'left': {'q': [0, 0, 0, 0, 0, 0, 0]}, 'right': {'q': [-2.6, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 24.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121693417609000_6c05757eaab44412b1cbf435e8d9df47.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0024.jpg`
Sim seconds: 79.2

```text
[obs #024 | act=e7c1d226 | sim= 79.20s | wall= 220.4s | Overhead divider clearance carry]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.261, 0.0]m rel_yaw=-4.700rad vel=[0.002, -0.0, 0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-38.11137008666992, -26.419132232666016, 20.080209732055664, -1.5946933031082153]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, 1e-05, -2e-05, 0.0, 0.0, -1e-05] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.791323184967041, -0.017081083729863167, -0.0025688093155622482, 0.185735285282135, -0.0021552431862801313, 0.014769861474633217, -5.697728192899376e-05] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.242, 1.689]m fingers=[0.0316, 0.0428]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.874, -0.213, 1.689] pad_end=[0.869, -0.282, 1.689] measured_pinch=[0.871, -0.247, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59979, 0.05001, -0.12972, -0.11975, 0.06629, 1.00024, -0.13943] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.001, -0.0, -0.001]rad limit_margins=[1.841, 0.114, 2.216, 0.459, 2.28, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-10.418947219848633, 1.134930968284607, 0.14679647982120514, -5.547137260437012, -0.028709370642900467, -2.673935890197754, 0.3219563066959381] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0024_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 24. Advance centrally without lateral divider approach

```python
s.act(**{'intent': 'Advance centrally without lateral divider approach', 'left': None, 'right': None, 'base': {'fwd': 0.35}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 25.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121699769450000_42766eae11e0404c9e4fb7477e7c32dd.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0025.jpg`
Sim seconds: 81.9

```text
[obs #025 | act=05c770a4 | sim= 81.90s | wall= 226.6s | Advance centrally without lateral divider approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.016, -0.916, 0.0]m rel_yaw=-4.700rad vel=[0.0, 0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.34508752822876, -5.094778060913086, 5.636026382446289, -0.4877976179122925]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, 0.0, -1e-05, 0.0, -0.0, -0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.05488498881459236, 0.07248681783676147, 0.0008305199444293976, -0.021315354853868484, 0.0006228191778063774, -0.003391959937289357, 0.0023395067546516657] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0316, 0.0428]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.873, -0.212, 1.689] pad_end=[0.869, -0.281, 1.689] measured_pinch=[0.871, -0.247, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59985, 0.05002, -0.13096, -0.11977, 0.06426, 1.00002, -0.13942] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.001, -0.0, -0.001]rad limit_margins=[1.841, 0.114, 2.215, 0.459, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-4.977434158325195, -0.13420063257217407, 0.22470788657665253, -3.2385149002075195, 0.17615705728530884, -2.027442216873169, -0.02460033819079399] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0025_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 25. Turn toward tabletop from centered aisle

```python
s.act(**{'intent': 'Turn toward tabletop from centered aisle', 'left': None, 'right': None, 'base': {'yaw_deg': 135}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 26.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121719587445000_a9fba708f7fe4344969c54f50a606ae1.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0026.jpg`
Sim seconds: 89.06666666666666

```text
[obs #026 | act=950612c7 | sim= 89.07s | wall= 246.4s | Turn toward tabletop from centered aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.016, -0.916, 0.0]m rel_yaw=-2.349rad vel=[0.0, -0.001, 0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.773491382598877, -5.528772354125977, 5.803064823150635, -0.44521963596343994]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-1e-05, 0.0, 0.0, -1e-05, -0.0, -0.0, -0.0] q_lag=[0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.001216805074363947, 0.035936202853918076, 0.0002328958362340927, 0.00319500220939517, 0.00015447157784365118, 0.0009982686024159193, 0.0020017644856125116] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0316, 0.0428]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.873, -0.212, 1.689] pad_end=[0.869, -0.281, 1.689] measured_pinch=[0.871, -0.247, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59985, 0.05002, -0.13099, -0.11977, 0.06417, 1.00001, -0.13947] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.001, -0.0, -0.001]rad limit_margins=[1.841, 0.114, 2.215, 0.459, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.005237579345703, 0.011095762252807617, 0.23592472076416016, -3.2574093341827393, 0.17856299877166748, -2.0298964977264404, -0.022696197032928467] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0026_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 26. Align hand sweep over RGBD solid tabletop

```python
s.act(**{'intent': 'Align hand sweep over RGBD solid tabletop', 'left': None, 'right': None, 'base': {'left': -0.22}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: stalled; observation 27.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121746713853000_e6f4d59ef2bd42e0a9c21cee68b3745e.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0027.jpg`
Sim seconds: 92.7

```text
[obs #027 | act=b67f8c67 | sim= 92.70s | wall= 273.5s | Align hand sweep over RGBD solid tabletop]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.148, -0.762, 0.0]m rel_yaw=-2.349rad vel=[0.0, -0.001, -0.002] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.689485549926758, -5.635564804077148, 6.000446319580078, -0.7802858352661133]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-1e-05, 0.0, -1e-05, -1e-05, -1e-05, 0.0, -0.0] q_lag=[0.0, -0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.002950802445411682, -0.1734941303730011, -0.0013092467561364174, -0.0023426737170666456, -0.0007290104404091835, -0.0005291153793223202, -0.004916118923574686] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0316, 0.0428]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.873, -0.212, 1.689] pad_end=[0.869, -0.281, 1.689] measured_pinch=[0.871, -0.247, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59985, 0.05002, -0.1311, -0.11977, 0.06413, 1.00001, -0.13947] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.001, -0.0, -0.001]rad limit_margins=[1.841, 0.114, 2.215, 0.459, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.160669326782227, -0.48416566848754883, 0.25850725173950195, -3.3476274013519287, 0.21904218196868896, -2.0511844158172607, -0.06154388189315796] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=stalled fault=None uncertain=False pending=['base']
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0027_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 27. Lower carried fax over measured tabletop

```python
s.act(**{'intent': 'Lower carried fax over measured tabletop', 'left': None, 'right': {'q': [-1.36, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': True, 'timeout_seconds': 30.0})
```
Result: reached; observation 28.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121769846736000_27304f01a25c427bb74c36a8778430e2.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0028.jpg`
Sim seconds: 94.4

```text
[obs #028 | act=7dd293f8 | sim= 94.40s | wall= 296.7s | Lower carried fax over measured tabletop]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.147, -0.762, 0.0]m rel_yaw=-2.354rad vel=[0.001, -0.0, 0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[2.8162784576416016, 1.3845572471618652, 1.528429627418518, -0.6722943782806396]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-0.0, 0.0, -1e-05, -2e-05, -1e-05, 0.0, -0.0] q_lag=[0.0, -0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.4562259018421173, -0.22061750292778015, 0.00017343461513519287, -0.11867625266313553, 0.0005697207525372505, -0.012169025838375092, -0.007478390820324421] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.838, -0.241, 0.854]m fingers=[0.0316, 0.0428]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.839, -0.212, 0.853] pad_end=[0.837, -0.281, 0.857] measured_pinch=[0.838, -0.247, 0.855]m
     close_dir=[0.02, 1.0, -0.06] fing_dir=[0.22, -0.06, -0.97] q=[-1.3599, 0.05001, -0.13141, -0.11987, 0.06335, 0.99988, -0.13948] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.002, 0.0, -0.001]rad limit_margins=[2.659, 0.114, 2.215, 0.459, 2.283, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-3.8029918670654297, -0.3617498278617859, 0.19137048721313477, -2.201690196990967, 0.17777109146118164, -0.7420358061790466, -0.16051922738552094] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=['base']
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0028_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 28. Settle fax closer to support surface

```python
s.act(**{'intent': 'Settle fax closer to support surface', 'left': None, 'right': {'q': [-1.3, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': True, 'timeout_seconds': 30.0})
```
Result: reached; observation 29.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121782165116000_f5e31e0225244b31b6f251781580e994.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0029.jpg`
Sim seconds: 94.53333333333333

```text
[obs #029 | act=944dd9c6 | sim= 94.53s | wall= 309.0s | Settle fax closer to support surface]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.147, -0.762, 0.0]m rel_yaw=-2.354rad vel=[-0.001, 0.0, -0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[69.75054168701172, 46.088645935058594, -57.59956359863281, 4.221719741821289]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[0.00011, -0.0, -2e-05, 0.00011, 0.0, -1e-05, 2e-05] q_lag=[-0.0, 0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.5499387979507446, -0.36429738998413086, -0.005320250988006592, 0.15711021423339844, -0.0038935597985982895, 0.017166653648018837, -0.011209812946617603] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.812, -0.241, 0.824]m fingers=[0.0316, 0.0428]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.813, -0.212, 0.822] pad_end=[0.812, -0.281, 0.826] measured_pinch=[0.812, -0.247, 0.824]m
     close_dir=[0.02, 1.0, -0.05] fing_dir=[0.17, -0.06, -0.98] q=[-1.30135, 0.05002, -0.13184, -0.12451, 0.06148, 0.99983, -0.13946] q_lag=[0.001, -0.0, 0.002, 0.005, 0.004, 0.0, -0.001]rad limit_margins=[2.6, 0.114, 2.214, 0.464, 2.285, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.3, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[54.99994659423828, 0.12842464447021484, 0.43187904357910156, 25.000642776489258, 0.8405542373657227, -0.9909628629684448, -0.831717312335968] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=['base']
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0029_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 29. Release fax

```python
s.act(**{'intent': 'Release fax', 'left': None, 'right': {'grip': 1}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': True, 'timeout_seconds': 30.0})
```
Result: reached; observation 30.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121784433768000_4f8a16e11ec84b4aa9630ce320a82344.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0030.jpg`
Sim seconds: 94.66666666666667

```text
[obs #030 | act=be46c13f | sim= 94.67s | wall= 311.3s | Release fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.147, -0.762, 0.0]m rel_yaw=-2.354rad vel=[0.001, 0.0, -0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[0.2764204442501068, 0.33587658405303955, -0.30859601497650146, 0.029820531606674194]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, -0.0, -1e-05, -1e-05, -1e-05, 0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.020968127995729446, 0.393364280462265, 0.0017465800046920776, 0.0016968155978247523, 0.0006861467845737934, 0.0018841464770957828, 0.010915243998169899] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.811, -0.242, 0.821]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.811, -0.194, 0.818] pad_end=[0.81, -0.289, 0.824] measured_pinch=[0.811, -0.242, 0.821]m
     close_dir=[0.02, 1.0, -0.06] fing_dir=[0.16, -0.06, -0.98] q=[-1.3, 0.05, -0.12999, -0.12, 0.06503, 1.0, -0.14] q_lag=[-0.0, 0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[2.599, 0.115, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.3, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[0.0808626189827919, 0.16382275521755219, 0.008290711790323257, 0.03844209015369415, 0.0059780944138765335, 0.006858005188405514, -0.007356869988143444] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=['base']
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0030_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 30. Withdraw from supported fax

```python
s.act(**{'intent': 'Withdraw from supported fax', 'left': None, 'right': {'q': [-1.65, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': True, 'timeout_seconds': 30.0})
```
Result: reached; observation 31.

Receipt: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/receipt_01792121787049351000_5a2e5cca298142aba3766362140f6a50.json`
Image: `/tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0031.jpg`
Sim seconds: 95.16666666666667

```text
[obs #031 | act=600c006d | sim= 95.17s | wall= 313.9s | Withdraw from supported fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.147, -0.761, 0.0]m rel_yaw=-2.354rad vel=[-0.0, -0.0, -0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[4.642886161804199, 1.9007413387298584, -0.8385581970214844, 1.549297571182251]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[2e-05, -0.0, -3e-05, -1e-05, -2e-05, 0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.5848190784454346, 1.5524014234542847, 0.014594420790672302, -0.1852293461561203, 0.009573888033628464, -0.02117748185992241, 0.04842490702867508] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.242, 1.035]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.942, -0.195, 1.033] pad_end=[0.939, -0.289, 1.038] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.05] fing_dir=[0.49, -0.06, -0.87] q=[-1.64997, 0.04999, -0.12977, -0.12001, 0.06534, 1.00003, -0.14] q_lag=[-0.0, 0.0, -0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[2.791, 0.115, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-0.1295662522315979, 1.8786739110946655, 0.04084467142820358, 0.026394158601760864, -0.02913074940443039, -0.012695599347352982, 0.04719305783510208] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=['base']
  depth saved: /tmp/fax-run-008-p6-918bba/fax-run-008-v6-a10/obs_0031_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```
