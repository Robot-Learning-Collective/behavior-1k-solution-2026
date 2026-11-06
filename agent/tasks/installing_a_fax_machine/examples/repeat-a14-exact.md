# a14 exact public action sequence

Historical record, not a blind replay script. Includes unsuccessful recovery motions and rejected requests; inspect images and remeasure before contacts. All arguments preserved, including max_steps.

## 1. Turn toward doorway

```python
s.act(**{'intent': 'Turn toward doorway', 'left': {'grip': 1}, 'right': {'grip': 1}, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 2.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127119667573000_cf31431b1bf3490fb767db46cbac3147.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0002.jpg`
Sim seconds: 5.2

```text
[obs #002 | act=fec4c68d | sim=  5.20s | wall=  26.6s | Turn toward doorway]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0002_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 2. Measured clear doorway approach

```python
s.act(**{'intent': 'Measured clear doorway approach', 'left': None, 'right': None, 'base': {'fwd': 1}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 3.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127127299926000_3921625b9c4b486482b9fddb742a8fe5.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0003.jpg`
Sim seconds: 11.166666666666666

```text
[obs #003 | act=3123860a | sim= 11.17s | wall=  34.2s | Measured clear doorway approach]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0003_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 3. Measured clear doorway approach

```python
s.act(**{'intent': 'Measured clear doorway approach', 'left': None, 'right': None, 'base': {'fwd': 0.8}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 4.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127133847512000_387703b56c29446b996f8811f171bcbc.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0004.jpg`
Sim seconds: 16.133333333333333

```text
[obs #004 | act=24ed375b | sim= 16.13s | wall=  40.8s | Measured clear doorway approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.008, -1.791, 0.0]m rel_yaw=-1.566rad vel=[0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.7101281881332397, 0.3408242464065552, -0.15185126662254333, 0.02469569630920887]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.07193373888731003, 0.14609268307685852, 0.0026933762710541487, -0.025005333125591278, 0.002208262449130416, -0.003315262496471405, 0.006945576518774033] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.0770728662610054, 0.1456374078989029, 0.0021565451752394438, -0.02467537485063076, 0.0018409938784316182, -0.003587638260796666, 0.007386649493128061] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0004_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 4. Clear junction turn

```python
s.act(**{'intent': 'Clear junction turn', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 5.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127147229726000_c63bcb65ab7f4bb1ae27ee395bc98ff5.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0005.jpg`
Sim seconds: 21.333333333333332

```text
[obs #005 | act=93f5508a | sim= 21.33s | wall=  54.1s | Clear junction turn]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.008, -1.791, 0.0]m rel_yaw=-3.132rad vel=[-0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.31676605343818665, 0.04198914393782616, -0.06120135262608528, -0.053920477628707886]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.04048704728484154, -0.037462372332811356, -0.0013153119944036007, -0.012075777165591717, -0.0012771254405379295, -0.0011857935460284352, -0.00433517387136817] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.006379529368132353, -0.04646081477403641, -0.0013722758740186691, 0.0008646248606964946, -0.001347117591649294, -0.00012308030272834003, -0.004881780594587326] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0005_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 5. Center outer aisle

```python
s.act(**{'intent': 'Center outer aisle', 'left': None, 'right': None, 'base': {'left': 0.5}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 6.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127152482869000_676e4ce5a961462a82e0a4db42f1ce24.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0006.jpg`
Sim seconds: 24.8

```text
[obs #006 | act=cfe3d4d3 | sim= 24.80s | wall=  59.5s | Center outer aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[0.013, -2.286, 0.0]m rel_yaw=-3.133rad vel=[0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.22168421745300293, -0.08765937387943268, 0.0693933516740799, -0.02928750589489937]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.007659120950847864, -0.12035175412893295, -0.0016590692102909088, -0.003838916076347232, -0.0012556761503219604, -0.0009038657299242914, -0.005419800989329815] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.04, 0.0, -1.0] q=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.014826413244009018, -0.11669687926769257, -0.001473359763622284, 0.002627917565405369, -0.001190938986837864, 5.629242514260113e-05, -0.005664310418069363] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0006_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 6. Measured outer aisle

```python
s.act(**{'intent': 'Measured outer aisle', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 7.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127169074008000_853eff2eb2dd4e8da29105bab4fd80c3.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0007.jpg`
Sim seconds: 31.766666666666666

```text
[obs #007 | act=5ede4fda | sim= 31.77s | wall=  76.1s | Measured outer aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-1.182, -2.297, 0.0]m rel_yaw=-3.133rad vel=[0.0, 0.0, 0.001] | torso=[1.025, -1.45, -0.47, -0.0] err=[-0.0, 0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.8166518807411194, 0.35063299536705017, -0.17539864778518677, 0.06057165563106537]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.06782260537147522, 0.1033182293176651, 0.002251606434583664, -0.025929389521479607, 0.0019942782819271088, -0.003653028979897499, 0.005450807511806488] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.09544442594051361, 0.10776699334383011, 0.0016971826553344727, -0.028714515268802643, 0.0015967972576618195, -0.003746101399883628, 0.005897243972867727] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0007_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 7. Measured outer aisle

```python
s.act(**{'intent': 'Measured outer aisle', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 8.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127177428565000_ec3c58e0d0cf455d9b658ba372d9f3a0.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0008.jpg`
Sim seconds: 38.733333333333334

```text
[obs #008 | act=28c4d395 | sim= 38.73s | wall=  84.4s | Measured outer aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-2.378, -2.308, 0.0]m rel_yaw=-3.133rad vel=[-0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.03082779422402382, 0.21677598357200623, -0.03202289715409279, -0.039476603269577026]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, -0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.0661526694893837, -0.05637466534972191, -0.0012821750715374947, -0.02277483604848385, -0.0011865817941725254, -0.003908351995050907, -0.004045939538627863] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.036887992173433304, -0.06741591542959213, -0.0013051079586148262, -0.016925731673836708, -0.0012270386796444654, -0.0035824549850076437, -0.004524402320384979] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0008_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 8. Measured outer aisle

```python
s.act(**{'intent': 'Measured outer aisle', 'left': None, 'right': None, 'base': {'fwd': 1.15}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 9.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127185604504000_e99cf2f666484797bc28fda55e0827e8.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0009.jpg`
Sim seconds: 45.46666666666667

```text
[obs #009 | act=fb7db692 | sim= 45.47s | wall=  92.5s | Measured outer aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-3.523, -2.318, 0.0]m rel_yaw=-3.133rad vel=[0.0, -0.0, -0.001] | torso=[1.025, -1.45, -0.47, -0.0] err=[-0.0, -0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.403606116771698, 0.03995562717318535, 0.08153755217790604, -0.04161280393600464]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.057332444936037064, -0.1404488980770111, -0.0025833062827587128, -0.023234670981764793, -0.0020158113911747932, -0.004731047432869673, -0.006600507069379091] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.013484170660376549, -0.14572565257549286, -0.002536047250032425, -0.009818780235946178, -0.002088623121380806, -0.0024117513094097376, -0.007051505614072084] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0009_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 9. Face fax aisle

```python
s.act(**{'intent': 'Face fax aisle', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 10.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127203834700000_e79b047c1f6242f9953448d2155c1bdf.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0010.jpg`
Sim seconds: 50.666666666666664

```text
[obs #010 | act=b1d5533a | sim= 50.67s | wall= 110.7s | Face fax aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-3.523, -2.318, 0.0]m rel_yaw=-4.699rad vel=[0.001, 0.0, 0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[-0.0, -0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.7656835317611694, -0.41040563583374023, 0.24000591039657593, -0.05302226543426514]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.017316434532403946, -0.1865164041519165, -0.0034676343202590942, 0.0014617327833548188, -0.0028550885617733, -0.00099015305750072, -0.009738408960402012] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.057985126972198486, -0.19124488532543182, -0.003222435712814331, 0.01425499189645052, -0.0027859769761562347, 0.001433152356185019, -0.010568696074187756] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0010_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 10. Align aisle

```python
s.act(**{'intent': 'Align aisle', 'left': None, 'right': None, 'base': {'left': 0.48}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 11.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127208937476000_03be8d11ec5d489ebb09d1c80fb506b2.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0011.jpg`
Sim seconds: 54.03333333333333

```text
[obs #011 | act=87d49e5b | sim= 54.03s | wall= 115.9s | Align aisle]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-3.998, -2.324, 0.0]m rel_yaw=-4.699rad vel=[0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.6387648582458496, 0.28637784719467163, -0.16790489852428436, 0.03985757380723953]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, -0.0, 0.0, 0.0, 0.0] q_lag=[-0.0, -0.0, 0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.018680144101381302, 0.1010502427816391, 0.0026534870266914368, -0.003950824495404959, 0.0022540297359228134, 2.0505347492871806e-05, 0.006778096314519644] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, 0.0, -0.0, -0.0, 0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.046256620436906815, 0.10681968927383423, 0.0023852363228797913, -0.011748398654162884, 0.0021017994731664658, -0.001101788249798119, 0.0074192071333527565] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0011_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 11. Narrow arms clear of divider

```python
s.act(**{'intent': 'Narrow arms clear of divider', 'left': {'q': [-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56]}, 'right': {'q': [-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 12.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127213997787000_4b82c63523f5464d9a3c23d84b14d850.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0012.jpg`
Sim seconds: 57.2

```text
[obs #012 | act=1457f681 | sim= 57.20s | wall= 121.0s | Narrow arms clear of divider]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-3.998, -2.325, 0.0]m rel_yaw=-4.699rad vel=[-0.0, 0.0, 0.0] | torso=[1.025, -1.45, -0.47, 0.0] err=[0.0, 0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.07608094811439514, 0.008392468094825745, -0.036523282527923584, -0.3085149824619293]
  L: rigid_TCP(fwd,left,up)=[0.705, 0.086, 0.997]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.705, 0.133, 0.994] pad_end=[0.704, 0.038, 0.999] measured_pinch=[0.705, 0.086, 0.997]m
     close_dir=[0.01, 1.0, -0.05] fing_dir=[0.34, -0.05, -0.94] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.34497, 0.83545, 1.56] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.022804435342550278, -0.13855624198913574, -0.013392368331551552, -0.022573530673980713, 0.0008457419462502003, 0.0006822473369538784, -0.0056439959444105625] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.505, -0.27, 0.649]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.505, -0.223, 0.649] pad_end=[0.504, -0.318, 0.649] measured_pinch=[0.505, -0.27, 0.649]m
     close_dir=[0.01, 1.0, -0.0] fing_dir=[-0.03, -0.0, -1.0] q=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51883, 1.036, -0.79466] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[0.03671737760305405, -0.07929464429616928, -0.010043089278042316, 0.01764889806509018, -0.0028164226096123457, 0.0007968834252096713, 0.0014901073882356286] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0012_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 12. Centered fax approach

```python
s.act(**{'intent': 'Centered fax approach', 'left': None, 'right': None, 'base': {'fwd': 0.8}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 13.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127228668175000_d0f458fad1e940cc9fb464644e6e1bfb.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0013.jpg`
Sim seconds: 62.166666666666664

```text
[obs #013 | act=2c98f22b | sim= 62.17s | wall= 135.4s | Centered fax approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.009, -1.53, 0.0]m rel_yaw=-4.700rad vel=[-0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[1.6105477809906006, 1.1393425464630127, -0.6915305852890015, 0.06676217913627625]
  L: rigid_TCP(fwd,left,up)=[0.705, 0.086, 0.997]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.705, 0.133, 0.994] pad_end=[0.704, 0.038, 0.999] measured_pinch=[0.705, 0.086, 0.997]m
     close_dir=[0.01, 1.0, -0.05] fing_dir=[0.34, -0.05, -0.94] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, -0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.07543113827705383, 0.08097244799137115, -0.011412504129111767, 0.05321618169546127, -0.0015936573036015034, -0.0003093007253482938, 0.0022921774070709944] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.505, -0.27, 0.649]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.505, -0.223, 0.649] pad_end=[0.504, -0.318, 0.649] measured_pinch=[0.505, -0.27, 0.649]m
     close_dir=[0.01, 1.0, -0.0] fing_dir=[-0.03, -0.0, -1.0] q=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[-0.03693254664540291, 0.02262991853058338, -0.0013523197267204523, 0.010917333886027336, 0.004800308030098677, -0.002042619977146387, -0.0040530916303396225] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0013_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 13. Centered fax approach

```python
s.act(**{'intent': 'Centered fax approach', 'left': None, 'right': None, 'base': {'fwd': 0.27}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 14.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127232792772000_477181ff99de4d8c8a08f2c23b750986.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0014.jpg`
Sim seconds: 64.46666666666667

```text
[obs #014 | act=1160aa75 | sim= 64.47s | wall= 139.7s | Centered fax approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.265, 0.0]m rel_yaw=-4.700rad vel=[0.0, -0.001, -0.0] | torso=[1.025, -1.45, -0.47, 0.0] err=[-0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[1.1874459981918335, 1.136611819267273, -0.5921859741210938, -0.007147900760173798]
  L: rigid_TCP(fwd,left,up)=[0.705, 0.086, 0.997]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.705, 0.133, 0.994] pad_end=[0.704, 0.038, 0.999] measured_pinch=[0.705, 0.086, 0.997]m
     close_dir=[0.01, 1.0, -0.05] fing_dir=[0.34, -0.05, -0.94] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, -0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.009120816364884377, 0.02077113278210163, -0.006695606280118227, 0.0439564511179924, -0.00602380046620965, -0.000999480253085494, 0.003709500189870596] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.505, -0.27, 0.649]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.505, -0.223, 0.649] pad_end=[0.504, -0.318, 0.649] measured_pinch=[0.505, -0.27, 0.649]m
     close_dir=[0.01, 1.0, -0.0] fing_dir=[-0.03, -0.0, -1.0] q=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51883, 1.03601, -0.79466] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[-0.021113364025950432, 0.02329510636627674, 0.003621160751208663, -0.004416910465806723, -0.006956855300813913, 0.00014478969387710094, 0.007790996693074703] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0014_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 14. Floor pickup crouch

```python
s.act(**{'intent': 'Floor pickup crouch', 'left': None, 'right': None, 'base': None, 'torso': {'q': [1.68, -2.54, -1.62, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 15.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127236129603000_98ea61b681554f1693e224eff7eb794c.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0015.jpg`
Sim seconds: 66.03333333333333

```text
[obs #015 | act=0090d7ae | sim= 66.03s | wall= 143.1s | Floor pickup crouch]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.701rad vel=[-0.0, 0.0, 0.0] | torso=[1.687, -2.54, -1.62, 0.0] err=[-0.007, -0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-100.0001449584961, -46.48052978515625, 60.025596618652344, 0.14986765384674072]
  L: rigid_TCP(fwd,left,up)=[0.631, 0.086, 0.25]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.63, 0.133, 0.248] pad_end=[0.633, 0.038, 0.252] measured_pinch=[0.631, 0.086, 0.25]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.37, -0.05, -0.93] q=[-1.30825, 0.05613, -0.97218, -1.0032, 2.34496, 0.83543, 1.55998] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-6.293850421905518, -2.2782905101776123, 1.474745750427246, -3.9025044441223145, 0.12703049182891846, 0.019320718944072723, -0.07244443148374557] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.251, -0.27, 0.121]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.252, -0.223, 0.121] pad_end=[0.251, -0.318, 0.122] measured_pinch=[0.251, -0.27, 0.121]m
     close_dir=[0.01, 1.0, -0.01] fing_dir=[-0.68, -0.0, -0.73] q=[-0.52689, -0.35922, 0.79381, -0.97008, -1.51886, 1.03599, -0.79466] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[0.8112634420394897, -0.9961325526237488, -0.3354681134223938, -1.4163357019424438, -0.009909510612487793, 0.04874733090400696, -0.024324003607034683] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0015_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 15. Top approach

```python
s.act(**{'intent': 'Top approach', 'left': None, 'right': {'to': [0.61, -0.3, 0.15], 'finger_dir': [0, 0, -1], 'close_dir': [0, 1, 0]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 16.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127245706289000_5a5b0740a2214901b54df40052818f61.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0016.jpg`
Sim seconds: 66.63333333333334

```text
[obs #016 | act=28155c22 | sim= 66.63s | wall= 152.6s | Top approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.701rad vel=[-0.001, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-0.5451386570930481, -0.4011537432670593, 0.2302173376083374, -0.008397772908210754]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.631, 0.133, 0.252] pad_end=[0.633, 0.038, 0.257] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.08353748172521591, -0.008736430667340755, -0.023371830582618713, 0.0038793059065937996, 0.0008941404521465302, -0.0002035633660852909, 0.002825288102030754] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.61, -0.299, 0.151]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.61, -0.252, 0.151] pad_end=[0.61, -0.347, 0.151] measured_pinch=[0.61, -0.3, 0.151]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.0, -0.0, -1.0] q=[-0.93471, -0.47131, 0.77643, -1.11647, -1.27483, 0.84647, -0.57795] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.234, 0.636, 1.57, 0.968, 1.071, 0.191, 0.983]rad min=0.191rad
     q_cmd=[-0.93472, -0.47131, 0.77644, -1.11646, -1.27483, 0.84648, -0.57793] effort_Nm=[0.09622803330421448, -0.02461574599146843, 0.01925019547343254, 0.01773517206311226, 0.001851067878305912, 0.003707115538418293, -0.004704691004008055] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0016_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 16. Cartesian descent

```python
s.act(**{'intent': 'Cartesian descent', 'left': None, 'right': {'to': [0.61, -0.3, 0.035]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': True, 'timeout_seconds': 30.0})
```
Result: stalled; observation 17.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127249684645000_6c0849fa8c1e4205969e52a47281b5a9.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0017.jpg`
Sim seconds: 68.6

```text
[obs #017 | act=88d837a1 | sim= 68.60s | wall= 156.6s | Cartesian descent]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.702rad vel=[0.0, 0.0, -0.001] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-0.4766172170639038, 0.11508435010910034, 0.20174753665924072, 0.09185545891523361]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.631, 0.133, 0.252] pad_end=[0.633, 0.038, 0.257] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, -0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.006048141047358513, 0.014677975326776505, -0.0017826543189585209, -0.009594927541911602, 0.001991216093301773, 6.96724746376276e-05, 0.0013809925876557827] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.299, 0.051]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.603, -0.251, 0.051] pad_end=[0.603, -0.346, 0.051] measured_pinch=[0.603, -0.299, 0.051]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17902, -0.09569, 1.07878, -0.03462, -1.0501, 0.43294, 0.07114] q_lag=[0.0, 0.0, -0.0, -0.0, -0.0, 0.0, 0.0]rad limit_margins=[2.478, 0.26, 1.267, 0.374, 1.296, 0.604, 1.49]rad min=0.26rad
     q_cmd=[-1.17902, -0.09568, 1.07877, -0.03462, -1.0501, 0.43294, 0.07114] effort_Nm=[-0.016927234828472137, 0.018169965595006943, -0.001785995438694954, -0.007127399556338787, -0.0016577662900090218, 0.0015530086820945144, 0.0027414977084845304] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"IK_stalled","causes":["IK_stalled"],"confidence":"limited","plateau":true,"normalized_error_history":[23.21259777796935,23.098371616164204,23.658937491375944,24.875690262180616,26.67558357675105,27.261576783075846,27.625310465324198,27.655992243451426,27.031132092042753,27.279828433153156,27.182960059917814,27.248711944502286,27.24665857769491,27.012071013051937,26.588797901967425,26.237900064415438,25.879338032000582,25.532292769768965,25.1899775234423,24.786941376884474,23.869548324018687,23.20715753693879,21.247178848861452,20.951453454561406,20.020774237009896,19.32022499359888,18.53748064733277,17.774930871005427,17.66756062115513,17.185403547979966,16.662940766382413,15.737142792733058,14.967599651021448,14.319817248577351,13.353734676497467,11.8904820201505,10.206454157260417,9.216360932956105,8.055574557245897,6.8997405907755835,5.642786394243262,4.4962383478729295,3.701518057953119,3.5252325515667584,3.5218895556255547,3.5195601104114322,3.5181920020030244,3.5176394774075783,3.5173620698870556,3.5171466096557165,3.51710606710531,3.5170811819612227,3.5169482613415703,3.5170332464681935,3.5169611848396545,3.5169681275050224,3.5169289112506488,3.51709255101341,3.516994910569989,3.5170032232761077],"normalized_progress":19.695594554693244,"recent_max_joint_lag_rad":[1.2516975402832031e-05,1.3113021850585938e-05,4.887580871582031e-06],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"}}
  status=stalled fault=None uncertain=False pending=['right']
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0017_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 17. Freeze low pose and pinch

```python
s.act(**{'intent': 'Freeze low pose and pinch', 'left': {'grip': 0}, 'right': {'q': [-1.17902, -0.09568, 1.07877, -0.03462, -1.0501, 0.43294, 0.07114], 'grip': 0}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: stalled; observation 18.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127259578765000_4c0f0791f74d47109ba93cb5e5438892.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0018.jpg`
Sim seconds: 69.2

```text
[obs #018 | act=357a0f6c | sim= 69.20s | wall= 166.5s | Freeze low pose and pinch]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.701rad vel=[-0.0, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[27.14845085144043, 10.152359008789062, -18.190200805664062, 12.973370552062988]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.255] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30833, 0.05611, -0.97214, -1.00324, 2.345, 0.83544, 1.56002] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.022875383496284485, -0.08893782645463943, -0.006443073973059654, -0.017509393393993378, 0.0012639814522117376, 0.00032004364766180515, -0.002831363119184971] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.299, 0.051]m fingers=[0.0351, 0.0399]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.603, -0.267, 0.051] pad_end=[0.603, -0.336, 0.051] measured_pinch=[0.603, -0.302, 0.051]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17901, -0.0957, 1.0795, -0.03435, -1.04894, 0.43292, 0.07097] q_lag=[-0.0, 0.0, -0.001, -0.0, -0.001, 0.0, 0.0]rad limit_margins=[2.478, 0.26, 1.267, 0.373, 1.297, 0.604, 1.49]rad min=0.26rad
     q_cmd=[-1.17902, -0.09568, 1.07877, -0.03462, -1.0501, 0.43294, 0.07114] effort_Nm=[3.1591978073120117, 4.016350746154785, 0.005706310272216797, -1.5878770351409912, -0.03850209712982178, -2.1546132564544678, 0.5468198657035828] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=stalled fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0018_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 18. Lift fax

```python
s.act(**{'intent': 'Lift fax', 'left': None, 'right': {'to': [0.603, -0.299, 0.2]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 19.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127264406019000_04fe5d5214074f62ad1a93bbc368cfa5.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0019.jpg`
Sim seconds: 71.86666666666666

```text
[obs #019 | act=841a952a | sim= 71.87s | wall= 171.4s | Lift fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.701rad vel=[-0.0, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.112209320068359, -2.227586269378662, 3.848956823348999, -0.504021406173706]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30835, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, 0.0, 0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.049859028309583664, 0.03769145533442497, -0.008678751066327095, 0.02454891987144947, 0.0007058093324303627, 0.00010214111534878612, 0.00025550174177624285] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.301, 0.2]m fingers=[0.035, 0.0398]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.603, -0.269, 0.199] pad_end=[0.603, -0.338, 0.2] measured_pinch=[0.603, -0.304, 0.2]m
     close_dir=[-0.0, 1.0, -0.01] fing_dir=[0.0, -0.01, -1.0] q=[-0.99161, -0.64318, 0.96666, -1.38933, -1.65282, 0.75884, -0.84757] q_lag=[-0.0, 0.0, -0.0, -0.0, -0.0, -0.001, -0.0]rad limit_margins=[2.291, 0.808, 1.38, 0.695, 0.693, 0.278, 0.713]rad min=0.278rad
     q_cmd=[-0.99169, -0.64315, 0.96663, -1.38933, -1.65298, 0.75825, -0.84775] effort_Nm=[-1.7729657888412476, 0.8993127346038818, -0.8455157279968262, -2.1199324131011963, -0.11705470085144043, -0.16864706575870514, 0.34693488478660583] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0019_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 19. Expose switch with tilted fax

```python
s.act(**{'intent': 'Expose switch with tilted fax', 'left': {'to': [0.58, -0.06, 0.36], 'finger_dir': [0.220337, -0.708506, -0.670426], 'close_dir': [-0.038811, 0.680406, -0.731807]}, 'right': {'to': [0.5, -0.08, 0.23], 'pitch_deg': 35}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 20.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127276169377000_24e9a7bf428346ecadb283b1a52b3b37.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0020.jpg`
Sim seconds: 72.93333333333334

```text
[obs #020 | act=e45dd238 | sim= 72.93s | wall= 183.1s | Expose switch with tilted fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.702rad vel=[-0.0, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.355904579162598, -2.352689027786255, 3.7900097370147705, -1.1753144264221191]
  L: rigid_TCP(fwd,left,up)=[0.581, -0.06, 0.358]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.581, -0.062, 0.361] pad_end=[0.581, -0.058, 0.357] measured_pinch=[0.581, -0.06, 0.359]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.87846, 0.21564, -1.02692, -1.77818, 1.68529, 0.34264, 0.79112] q_lag=[0.0, 0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.177, 0.38, 1.319, 0.306, 0.661, 0.695, 0.77]rad min=0.306rad
     q_cmd=[-0.87845, 0.21564, -1.02692, -1.77822, 1.68526, 0.34266, 0.79109] effort_Nm=[0.02906249649822712, 0.03257463499903679, -0.005187714472413063, 0.06906840950250626, -0.0015675593167543411, -0.00019056955352425575, 0.013199472799897194] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.496, -0.08, 0.228]m fingers=[0.0349, 0.0397]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.496, -0.048, 0.227] pad_end=[0.496, -0.118, 0.228] measured_pinch=[0.496, -0.083, 0.228]m
     close_dir=[-0.0, 1.0, -0.01] fing_dir=[0.55, -0.01, -0.83] q=[-0.63735, -0.22494, 1.36925, -1.51601, -0.87812, -0.01581, -1.23758] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.936, 0.389, 0.977, 0.568, 1.468, 1.021, 0.323]rad min=0.323rad
     q_cmd=[-0.63738, -0.22491, 1.36922, -1.51608, -0.87798, -0.01675, -1.23738] effort_Nm=[-1.332403540611267, 0.7550786733627319, -0.3631214201450348, -1.9975178241729736, 1.425334095954895, -0.5764478445053101, -0.2030857801437378] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0020_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 20. Approach red switch

```python
s.act(**{'intent': 'Approach red switch', 'left': {'to': [0.6101575994491577, -0.08555049508810043, 0.31740265011787416]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 21.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127284080657000_98d33a8e083a49b9ac374f3dcafc07bc.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0021.jpg`
Sim seconds: 73.33333333333333

```text
[obs #021 | act=056f9716 | sim= 73.33s | wall= 191.0s | Approach red switch]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.702rad vel=[0.0, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.614043235778809, -2.0561814308166504, 3.4832842350006104, -0.5866035223007202]
  L: rigid_TCP(fwd,left,up)=[0.61, -0.085, 0.318]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.61, -0.087, 0.32] pad_end=[0.61, -0.083, 0.317] measured_pinch=[0.61, -0.085, 0.319]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.94835, 0.12123, -1.04253, -1.50977, 1.64092, 0.35199, 0.62969] q_lag=[0.0, -0.0, -0.0, 0.0, 0.0, -0.0, -0.0]rad limit_margins=[2.247, 0.286, 1.304, 0.575, 0.705, 0.685, 0.931]rad min=0.286rad
     q_cmd=[-0.94835, 0.12122, -1.04254, -1.50974, 1.64093, 0.35198, 0.62968] effort_Nm=[0.030587676912546158, -0.0074402145110070705, -0.011309480294585228, -0.012210428714752197, 0.0007299421122297645, 0.0009247462148778141, -0.0034202372189611197] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.496, -0.08, 0.228]m fingers=[0.0349, 0.0397]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.496, -0.048, 0.227] pad_end=[0.497, -0.118, 0.228] measured_pinch=[0.496, -0.083, 0.228]m
     close_dir=[-0.0, 1.0, -0.01] fing_dir=[0.56, -0.01, -0.83] q=[-0.63734, -0.22494, 1.36924, -1.51601, -0.87812, -0.01608, -1.23743] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.936, 0.389, 0.977, 0.568, 1.468, 1.021, 0.323]rad min=0.323rad
     q_cmd=[-0.63738, -0.22491, 1.36922, -1.51608, -0.87798, -0.01675, -1.23738] effort_Nm=[-1.55990469455719, 1.182199239730835, -0.2668672204017639, -2.128474235534668, 1.4061838388442993, -0.5090233087539673, -0.07964996993541718] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0021_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 21. Press switch

```python
s.act(**{'intent': 'Press switch', 'left': {'to': [0.6253967671394348, -0.10433434629440308, 0.2923839044570923]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: stalled; observation 22.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127294122455000_a4757b2fa6dd40ada65dad1314b4be73.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0022.jpg`
Sim seconds: 74.1

```text
[obs #022 | act=cfa9c387 | sim= 74.10s | wall= 201.1s | Press switch]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.702rad vel=[0.002, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.007582664489746, -1.9451419115066528, 3.6894423961639404, -0.45607078075408936]
  L: rigid_TCP(fwd,left,up)=[0.625, -0.111, 0.305]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm) TRACKING_ERROR(q4=+0.027)
     pad_start=[0.625, -0.112, 0.307] pad_end=[0.624, -0.109, 0.303] measured_pinch=[0.625, -0.111, 0.305]m
     close_dir=[-0.04, 0.66, -0.75] fing_dir=[0.22, -0.73, -0.65] q=[-0.9955, 0.04554, -1.05986, -1.34487, 1.61838, 0.34306, 0.51702] q_lag=[0.0, 0.0, 0.001, 0.027, -0.01, 0.002, 0.002]rad limit_margins=[2.295, 0.21, 1.286, 0.74, 0.728, 0.694, 1.044]rad min=0.21rad
     q_cmd=[-0.99542, 0.0459, -1.05923, -1.31771, 1.60841, 0.34544, 0.51925] effort_Nm=[3.551614999771118, 25.449127197265625, 4.133053779602051, 25.00000762939453, -5.154472827911377, -3.4158341884613037, 10.395014762878418] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.496, -0.08, 0.227]m fingers=[0.035, 0.0396]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.495, -0.048, 0.227] pad_end=[0.496, -0.118, 0.228] measured_pinch=[0.496, -0.083, 0.227]m
     close_dir=[-0.0, 1.0, -0.01] fing_dir=[0.55, -0.01, -0.83] q=[-0.63727, -0.22507, 1.36973, -1.51527, -0.88081, -0.01441, -1.23739] q_lag=[-0.0, 0.0, -0.001, -0.001, 0.003, -0.002, 0.0]rad limit_margins=[1.936, 0.39, 0.976, 0.569, 1.465, 1.023, 0.323]rad min=0.323rad
     q_cmd=[-0.63738, -0.22491, 1.36922, -1.51608, -0.87798, -0.01675, -1.23738] effort_Nm=[-5.086570739746094, 6.898209571838379, 1.7641578912734985, -15.58218002319336, 12.840082168579102, -4.944482803344727, -3.44992733001709] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"blocked","causes":["blocked"],"confidence":"suspected","plateau":true,"normalized_error_history":[7.202587611821551,6.753393047558569,7.665275033871452,7.9685679808593175,6.909728108160186,5.062265648950355,3.20326089473709,2.8481016466689018,2.8479704748275205,2.8069514068347754,2.810209076108501,2.8068711674624534,2.8046511058166694,2.8041462229743668,2.803065794970349,2.802233846115947,2.801840550446225,2.802228595883225,2.8022132753144757,2.8017351678075415,2.8021010341935253,2.8017347918044497,2.8026850507841274,2.8027943970944458],"normalized_progress":4.399793214727105,"recent_max_joint_lag_rad":[0.02714526653289795,0.027158498764038086,0.02716195583343506],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=stalled fault=None uncertain=False pending=['left']
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0022_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 22. Withdraw switch finger

```python
s.act(**{'intent': 'Withdraw switch finger', 'left': {'to': [0.61, -0.04, 0.36]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 23.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127296621831000_1fc04d17fd77468598613509d8dfbd7b.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0023.jpg`
Sim seconds: 74.7

```text
[obs #023 | act=b8bcca83 | sim= 74.70s | wall= 203.6s | Withdraw switch finger]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.702rad vel=[-0.0, 0.0, -0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.367199897766113, -2.314340114593506, 3.920013427734375, -0.4824449419975281]
  L: rigid_TCP(fwd,left,up)=[0.611, -0.039, 0.356]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.611, -0.041, 0.358] pad_end=[0.61, -0.038, 0.355] measured_pinch=[0.611, -0.04, 0.356]m
     close_dir=[-0.05, 0.69, -0.72] fing_dir=[0.22, -0.7, -0.68] q=[-0.92903, 0.25139, -0.96734, -1.74268, 1.74945, 0.405, 0.76604] q_lag=[0.0, 0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.228, 0.416, 1.379, 0.342, 0.597, 0.632, 0.795]rad min=0.342rad
     q_cmd=[-0.92903, 0.2514, -0.96735, -1.74271, 1.74942, 0.40501, 0.76604] effort_Nm=[0.030137890949845314, 0.010531419888138771, -0.0071290116757154465, 0.049903593957424164, -0.0017397664487361908, -0.00043277814984321594, 0.008269112557172775] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.496, -0.08, 0.228]m fingers=[0.0349, 0.0396]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.496, -0.048, 0.227] pad_end=[0.497, -0.118, 0.228] measured_pinch=[0.496, -0.083, 0.228]m
     close_dir=[-0.0, 1.0, -0.01] fing_dir=[0.56, -0.01, -0.83] q=[-0.63735, -0.22494, 1.36924, -1.51601, -0.87808, -0.01583, -1.23758] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.936, 0.389, 0.977, 0.568, 1.468, 1.021, 0.323]rad min=0.323rad
     q_cmd=[-0.63738, -0.22491, 1.36922, -1.51608, -0.87798, -0.01675, -1.23738] effort_Nm=[-1.5610122680664062, 1.3201394081115723, -0.21263468265533447, -2.194807529449463, 1.4374594688415527, -0.5084110498428345, -0.03603193536400795] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0023_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 23. Stand with fax

```python
s.act(**{'intent': 'Stand with fax', 'left': None, 'right': None, 'base': None, 'torso': {'q': [0.84, -1.00609, -0.42, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 24.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127309277635000_b6a8a838945c4c16ad5269425bb3ff46.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0024.jpg`
Sim seconds: 76.8

```text
[obs #024 | act=14572a91 | sim= 76.80s | wall= 216.2s | Stand with fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.267, 0.0]m rel_yaw=-4.702rad vel=[0.002, 0.0, -0.001] | torso=[0.842, -1.006, -0.42, -0.0] err=[-0.002, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-99.997314453125, -58.48324203491211, 36.423397064208984, 1.2327430248260498]
  L: rigid_TCP(fwd,left,up)=[0.692, -0.039, 1.034]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.691, -0.041, 1.036] pad_end=[0.693, -0.038, 1.033] measured_pinch=[0.692, -0.04, 1.035]m
     close_dir=[0.31, 0.69, -0.66] fing_dir=[0.52, -0.7, -0.49] q=[-0.92903, 0.25141, -0.96735, -1.7427, 1.74931, 0.40506, 0.76605] q_lag=[0.0, -0.0, 0.0, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[2.228, 0.416, 1.379, 0.342, 0.597, 0.632, 0.795]rad min=0.342rad
     q_cmd=[-0.92903, 0.2514, -0.96735, -1.74271, 1.74942, 0.40501, 0.76604] effort_Nm=[-0.15911132097244263, -0.26124775409698486, 0.12485465407371521, -2.377573013305664, 0.06380161643028259, 0.027015026658773422, -0.22845005989074707] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.654, -0.08, 0.867]m fingers=[0.0349, 0.0396]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.654, -0.048, 0.866] pad_end=[0.654, -0.118, 0.867] measured_pinch=[0.654, -0.083, 0.867]m
     close_dir=[0.0, 1.0, -0.01] fing_dir=[0.89, -0.01, -0.46] q=[-0.63728, -0.22496, 1.36926, -1.51594, -0.87828, -0.01566, -1.2377] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.936, 0.389, 0.977, 0.568, 1.468, 1.022, 0.323]rad min=0.323rad
     q_cmd=[-0.63738, -0.22491, 1.36922, -1.51608, -0.87798, -0.01675, -1.23738] effort_Nm=[-2.379598617553711, 2.7424418926239014, -0.7666316628456116, -4.5014967918396, 2.544299840927124, -0.9318034648895264, -0.10653248429298401] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0024_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 24. Overhead clearance carry

```python
s.act(**{'intent': 'Overhead clearance carry', 'left': {'q': [0, 0, 0, 0, 0, 0, 0]}, 'right': {'q': [-2.6, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 25.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127314273951000_db217a696dd54c43ab5c7fce3941e806.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0025.jpg`
Sim seconds: 79.46666666666667

```text
[obs #025 | act=e3c99407 | sim= 79.47s | wall= 221.2s | Overhead clearance carry]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.267, 0.0]m rel_yaw=-4.702rad vel=[0.002, 0.0, -0.002] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-38.767913818359375, -26.440141677856445, 20.209026336669922, -1.6981528997421265]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, 1e-05, -2e-05, 0.0, 0.0, -1e-05] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.7886477112770081, 0.017318475991487503, -0.0027940920554101467, 0.18316209316253662, -0.0022432387340813875, 0.01340296771377325, 0.0015607626410201192] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.242, 1.689]m fingers=[0.035, 0.0396]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.874, -0.21, 1.689] pad_end=[0.869, -0.279, 1.689] measured_pinch=[0.872, -0.244, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59979, 0.05002, -0.12964, -0.11973, 0.06646, 1.00028, -0.13959] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.001, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.217, 0.459, 2.28, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-10.44287109375, 0.8692059516906738, 0.13933537900447845, -5.590642929077148, -0.018032167106866837, -2.6938271522521973, 0.28164130449295044] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0025_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 25. Center beneath open turn area

```python
s.act(**{'intent': 'Center beneath open turn area', 'left': None, 'right': None, 'base': {'fwd': 0.35}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 26.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127324566478000_e782c81c6d80404ea3b5e0230f497483.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0026.jpg`
Sim seconds: 82.16666666666667

```text
[obs #026 | act=1a1bd598 | sim= 82.17s | wall= 231.4s | Center beneath open turn area]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.015, -0.922, 0.0]m rel_yaw=-4.702rad vel=[0.0, -0.0, -0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.3104400634765625, -5.229849338531494, 5.694872856140137, -0.5102745294570923]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, 0.0, -1e-05, 0.0, -0.0, -0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.06019018590450287, 0.004551581107079983, 0.0005315984599292278, -0.02159092389047146, 0.00042660150211304426, -0.003055225359275937, -5.731038254452869e-05] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.035, 0.0396]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.874, -0.209, 1.689] pad_end=[0.869, -0.279, 1.689] measured_pinch=[0.871, -0.244, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59986, 0.05003, -0.13074, -0.11975, 0.0647, 1.00009, -0.13959] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.215, 0.459, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.0124945640563965, -0.0672760009765625, 0.2175265997648239, -3.2691128253936768, 0.16218361258506775, -2.0376038551330566, -0.008338507264852524] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0026_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 26. Turn above divider

```python
s.act(**{'intent': 'Turn above divider', 'left': None, 'right': None, 'base': {'yaw_deg': 115}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 27.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127333625343000_22186bab388c443aaf0d949b7400fb89.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0027.jpg`
Sim seconds: 88.46666666666667

```text
[obs #027 | act=f0a9c7e6 | sim= 88.47s | wall= 240.6s | Turn above divider]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.015, -0.922, 0.0]m rel_yaw=-2.699rad vel=[-0.0, 0.0, -0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.762248992919922, -5.474048614501953, 5.882945537567139, -0.5642777681350708]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, 0.0, -1e-05, 0.0, -0.0, -0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.014518709853291512, -0.05925086885690689, -0.00034333113580942154, -0.00444341916590929, -0.00026332889683544636, -0.0006046770722605288, -0.00220765033736825] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.035, 0.0396]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.874, -0.209, 1.689] pad_end=[0.869, -0.278, 1.689] measured_pinch=[0.871, -0.244, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59986, 0.05003, -0.13081, -0.11976, 0.06457, 1.00008, -0.13961] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.215, 0.459, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.0977911949157715, -0.16782593727111816, 0.22548198699951172, -3.311558246612549, 0.1741955280303955, -2.047077178955078, -0.022803843021392822] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0027_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 27. Lower to above-rail release pose

```python
s.act(**{'intent': 'Lower to above-rail release pose', 'left': None, 'right': {'q': [-1.65, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 28.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127343249610000_5186b407b51f4f588f63d394178b19b2.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0028.jpg`
Sim seconds: 89.76666666666667

```text
[obs #028 | act=ad58a977 | sim= 89.77s | wall= 249.9s | Lower to above-rail release pose]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.014, -0.922, 0.0]m rel_yaw=-2.700rad vel=[-0.0, 0.0, -0.002] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[22.211013793945312, 14.395483016967773, -11.39848518371582, -4.231223106384277]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-4e-05, -0.0, -1e-05, 2e-05, 0.0, -1e-05, 0.0] q_lag=[0.0, 0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.4455554485321045, -0.0940718725323677, -0.0002637729048728943, -0.06339709460735321, -0.00019614584743976593, 0.0029763677157461643, -0.0022157756611704826] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.24, 1.035]m fingers=[0.035, 0.0396]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.942, -0.208, 1.034] pad_end=[0.939, -0.277, 1.036] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.04] fing_dir=[0.49, -0.05, -0.87] q=[-1.64995, 0.05006, -0.13372, -0.11949, 0.05982, 0.99955, -0.1396] q_lag=[-0.0, -0.0, 0.004, -0.001, 0.005, 0.0, -0.0]rad limit_margins=[2.791, 0.114, 2.212, 0.459, 2.286, 0.038, 1.421]rad min=0.038rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[5.9288482666015625, -4.28731632232666, 0.7367467880249023, 2.2288618087768555, 1.0621473789215088, 0.580154538154602, -1.4230026006698608] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0028_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 28. Release above solid desktop

```python
s.act(**{'intent': 'Release above solid desktop', 'left': None, 'right': {'grip': 1}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 29.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127462068826000_771c8767048341efb63ea6955334a572.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0029.jpg`
Sim seconds: 89.9

```text
[obs #029 | act=b2c10bcc | sim= 89.90s | wall= 368.9s | Release above solid desktop]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.014, -0.922, 0.0]m rel_yaw=-2.700rad vel=[0.0, -0.0, 0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[0.6196700930595398, 0.31082600355148315, -0.1638393998146057, 0.3181265890598297]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.03566299378871918, 0.2467706799507141, 0.002156294882297516, -0.010653703473508358, 0.0015341145917773247, -0.000854326062835753, 0.008989710360765457] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.242, 1.035]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.942, -0.194, 1.033] pad_end=[0.939, -0.289, 1.038] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.05] fing_dir=[0.49, -0.06, -0.87] q=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, -0.0]rad limit_margins=[2.791, 0.115, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-0.025956083089113235, 0.2780526876449585, 0.015325833112001419, -0.00021177716553211212, 0.0054632266983389854, -0.004303767345845699, -0.0034019260201603174] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0029_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 29. Withdraw after release

```python
s.act(**{'intent': 'Withdraw after release', 'left': None, 'right': {'q': [-2.1, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 30.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/receipt_01792127464571836000_12c00a58340b49468c5f45c75ff0770e.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0030.jpg`
Sim seconds: 90.53333333333333

```text
[obs #030 | act=c9a70566 | sim= 90.53s | wall= 371.6s | Withdraw after release]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.015, -0.922, 0.0]m rel_yaw=-2.700rad vel=[0.0, -0.0, -0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, -0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-26.544300079345703, -17.186140060424805, 10.417776107788086, -1.1998975276947021]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-0.0, -0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, 0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[1.0341687202453613, -0.1770355999469757, -0.004945188760757446, 0.2544105350971222, -0.0040413998067379, 0.022062474861741066, -0.0062936716713011265] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.987, -0.242, 1.353]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.989, -0.194, 1.352] pad_end=[0.984, -0.289, 1.354] measured_pinch=[0.987, -0.242, 1.353]m
     close_dir=[0.06, 1.0, -0.03] fing_dir=[0.82, -0.06, -0.57] q=[-2.09997, 0.05, -0.13, -0.12001, 0.06497, 0.99999, -0.14] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0]rad limit_margins=[2.341, 0.115, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.1, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-2.1653785705566406, -0.3751959204673767, 0.04215705394744873, -0.7844246625900269, 0.04979580640792847, -0.04833649843931198, -0.0610627755522728] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a14/obs_0030_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```
