# a12 exact public action sequence

Historical record, not a blind replay script. Includes unsuccessful recovery motions and rejected requests; inspect images and remeasure before contacts. All arguments preserved, including max_steps.

## 1. Turn into verified instance10 aisle

```python
s.act(**{'intent': 'Turn into verified instance10 aisle', 'left': {'grip': 1}, 'right': {'grip': 1}, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 2.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126436289304000_da8ec82e1873484b83990d2005bbb564.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0002.jpg`
Sim seconds: 5.2

```text
[obs #002 | act=c40ada00 | sim=  5.20s | wall=  15.7s | Turn into verified instance10 aisle]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0002_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 2. Grounded known aisle advance

```python
s.act(**{'intent': 'Grounded known aisle advance', 'left': None, 'right': None, 'base': {'fwd': 1}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 3.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126452307941000_4d387d209be84797be6fa9818e0aff8d.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0003.jpg`
Sim seconds: 11.166666666666666

```text
[obs #003 | act=23e3ec41 | sim= 11.17s | wall=  32.0s | Grounded known aisle advance]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0003_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 3. Grounded known aisle advance

```python
s.act(**{'intent': 'Grounded known aisle advance', 'left': None, 'right': None, 'base': {'fwd': 0.8}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 4.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126459060394000_78132b32976343979b1bbdb22d2990cf.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0004.jpg`
Sim seconds: 16.133333333333333

```text
[obs #004 | act=9f1e0ce3 | sim= 16.13s | wall=  38.9s | Grounded known aisle advance]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0004_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 4. Clear junction turn

```python
s.act(**{'intent': 'Clear junction turn', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 5.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126472053792000_f61f3c9da97b478ca89a3c14c0875932.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0005.jpg`
Sim seconds: 21.333333333333332

```text
[obs #005 | act=1a161977 | sim= 21.33s | wall=  51.8s | Clear junction turn]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0005_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 5. Center away from divider

```python
s.act(**{'intent': 'Center away from divider', 'left': None, 'right': None, 'base': {'left': 0.5}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 6.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126477470658000_571c5c4a1a0f41849a6728036c6713ef.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0006.jpg`
Sim seconds: 24.8

```text
[obs #006 | act=63756575 | sim= 24.80s | wall=  57.1s | Center away from divider]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0006_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 6. Measured known corridor segment

```python
s.act(**{'intent': 'Measured known corridor segment', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 7.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126496136061000_46a7f86e2bee4ed788bc9b15d9c47c2d.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0007.jpg`
Sim seconds: 31.766666666666666

```text
[obs #007 | act=6052e9bc | sim= 31.77s | wall=  75.6s | Measured known corridor segment]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0007_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 7. Measured known corridor segment

```python
s.act(**{'intent': 'Measured known corridor segment', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 8.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126507752548000_30a7712624c449cbb542350f2a01bf5b.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0008.jpg`
Sim seconds: 38.733333333333334

```text
[obs #008 | act=6fba2181 | sim= 38.73s | wall=  87.4s | Measured known corridor segment]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0008_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 8. Measured known corridor segment

```python
s.act(**{'intent': 'Measured known corridor segment', 'left': None, 'right': None, 'base': {'fwd': 1.15}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 9.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126519400782000_ae62b981f46f461da9670bae900481c9.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0009.jpg`
Sim seconds: 45.46666666666667

```text
[obs #009 | act=68ce0356 | sim= 45.47s | wall=  99.0s | Measured known corridor segment]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0009_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 9. Face fax aisle

```python
s.act(**{'intent': 'Face fax aisle', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 10.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126535954391000_a6f2e117a89f434b8d5dc66a89dc0a7f.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0010.jpg`
Sim seconds: 50.666666666666664

```text
[obs #010 | act=74da0fb8 | sim= 50.67s | wall= 115.7s | Face fax aisle]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0010_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 10. Align aisle center

```python
s.act(**{'intent': 'Align aisle center', 'left': None, 'right': None, 'base': {'left': 0.48}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 11.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126541269469000_080c48e308274d56913ce7a76a9439a8.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0011.jpg`
Sim seconds: 54.03333333333333

```text
[obs #011 | act=d08b7b78 | sim= 54.03s | wall= 121.0s | Align aisle center]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0011_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 11. Narrow elbow approach

```python
s.act(**{'intent': 'Narrow elbow approach', 'left': {'q': [-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56]}, 'right': {'q': [-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 12.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126546623411000_7bc42685cb8e4ca593ebf38a825142df.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0012.jpg`
Sim seconds: 57.2

```text
[obs #012 | act=e73fe5e7 | sim= 57.20s | wall= 126.2s | Narrow elbow approach]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0012_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 12. Centered gap approach

```python
s.act(**{'intent': 'Centered gap approach', 'left': None, 'right': None, 'base': {'fwd': 0.8}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 13.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126564213617000_0a6ee6753e0f4046aa26a46672e6e744.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0013.jpg`
Sim seconds: 62.166666666666664

```text
[obs #013 | act=c72a8116 | sim= 62.17s | wall= 143.9s | Centered gap approach]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0013_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 13. Centered gap approach

```python
s.act(**{'intent': 'Centered gap approach', 'left': None, 'right': None, 'base': {'fwd': 0.27}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 14.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126568450032000_d49a4a1c96884111a63a1838085ed8d5.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0014.jpg`
Sim seconds: 64.46666666666667

```text
[obs #014 | act=6643a6f7 | sim= 64.47s | wall= 148.1s | Centered gap approach]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0014_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 14. Crouch for floor pickup

```python
s.act(**{'intent': 'Crouch for floor pickup', 'left': None, 'right': None, 'base': None, 'torso': {'q': [1.68, -2.54, -1.62, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 15.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126572132763000_b0f5de25716546eaa800f41277adb1d0.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0015.jpg`
Sim seconds: 66.03333333333333

```text
[obs #015 | act=2515ddac | sim= 66.03s | wall= 151.8s | Crouch for floor pickup]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0015_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 15. Approach fax

```python
s.act(**{'intent': 'Approach fax', 'left': None, 'right': {'to': [0.61, -0.3, 0.15], 'finger_dir': [0, 0, -1], 'close_dir': [0, 1, 0]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 16.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126585081203000_2d08fc98735e432b9415ed78fee4c3cd.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0016.jpg`
Sim seconds: 66.63333333333334

```text
[obs #016 | act=83a1e061 | sim= 66.63s | wall= 164.8s | Approach fax]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0016_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 16. Attain known low pinch pose without unreachable target

```python
s.act(**{'intent': 'Attain known low pinch pose without unreachable target', 'left': None, 'right': {'q': [-1.17902, -0.09568, 1.07877, -0.03462, -1.0501, 0.43294, 0.07114]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 17.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126588525267000_b1151e40be534b05ae67d175eef9938d.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0017.jpg`
Sim seconds: 68.13333333333334

```text
[obs #017 | act=cdeee8c1 | sim= 68.13s | wall= 168.2s | Attain known low pinch pose without unreachable target]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.701rad vel=[-0.001, -0.0, -0.002] | torso=[1.68, -2.54, -1.62, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[55.26511001586914, 24.015911102294922, -50.48796081542969, -15.908256530761719]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.631, 0.133, 0.253] pad_end=[0.633, 0.038, 0.257] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.3083, 0.05588, -0.97218, -1.0029, 2.34481, 0.83562, 1.55962] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.607, 0.22, 1.374, 1.082, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.6736119389533997, -0.9110937118530273, 0.07967868447303772, -0.7434574365615845, 0.04320138692855835, 0.006521318107843399, -0.023906266316771507] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.605, -0.294, 0.052]m fingers=[0.0495, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.605, -0.248, 0.052] pad_end=[0.604, -0.342, 0.051] measured_pinch=[0.605, -0.295, 0.052]m
     close_dir=[0.01, 1.0, 0.01] fing_dir=[0.01, 0.01, -1.0] q=[-1.17945, -0.09481, 1.07336, -0.04006, -1.05558, 0.43332, 0.07304] q_lag=[0.0, -0.001, 0.005, 0.005, 0.005, -0.0, -0.002]rad limit_margins=[2.478, 0.259, 1.273, 0.379, 1.291, 0.604, 1.488]rad min=0.259rad
     q_cmd=[-1.17902, -0.09568, 1.07877, -0.03462, -1.0501, 0.43294, 0.07114] effort_Nm=[43.628150939941406, -28.28879165649414, 1.565988302230835, 24.984081268310547, 0.9790019989013672, 7.119032859802246, -4.704949378967285] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0017_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 17. Close around fax body

```python
s.act(**{'intent': 'Close around fax body', 'left': {'grip': 0}, 'right': {'grip': 0}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 18.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126590792915000_9e94098e368d40f291d56fad3b62ad11.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0018.jpg`
Sim seconds: 68.36666666666666

```text
[obs #018 | act=e91f3455 | sim= 68.37s | wall= 170.6s | Close around fax body]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.701rad vel=[0.0, 0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[0.005686324089765549, -0.05629780888557434, -0.004649804905056953, 0.08188071101903915]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, -0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.015098516829311848, 0.032513417303562164, 0.0010390114039182663, 0.006658647209405899, -0.0009717708453536034, -0.00030138716101646423, 0.001994704594835639] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.299, 0.051]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.603, -0.301, 0.051] pad_end=[0.603, -0.296, 0.051] measured_pinch=[0.603, -0.299, 0.051]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17902, -0.09568, 1.07877, -0.03462, -1.0501, 0.43294, 0.07114] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, -0.0]rad limit_margins=[2.478, 0.26, 1.267, 0.374, 1.296, 0.604, 1.49]rad min=0.26rad
     q_cmd=[-1.17902, -0.09568, 1.07877, -0.03462, -1.0501, 0.43294, 0.07114] effort_Nm=[0.01104271225631237, 0.023331737145781517, 0.0005228575319051743, -0.004352931398898363, 0.0001750485971570015, 0.00042846050928346813, 0.0005467483424581587] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0018_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 18. Lift retained fax

```python
s.act(**{'intent': 'Lift retained fax', 'left': None, 'right': {'to': [0.603, -0.299, 0.2]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 19.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126596157525000_a5d794bc9f9c4ef0b251f5e2d642ccd5.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0019.jpg`
Sim seconds: 71.03333333333333

```text
[obs #019 | act=8ccf5dcd | sim= 71.03s | wall= 175.9s | Lift retained fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.700rad vel=[-0.0, -0.0, -0.001] | torso=[1.68, -2.54, -1.62, 0.0] err=[0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[0.06851477921009064, -0.0682382583618164, -0.04790686070919037, -0.1179756447672844]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.024956148117780685, -0.048984602093696594, -0.012273592874407768, -0.004683668725192547, 0.0025730826891958714, 0.0005126993637531996, -0.002797114197164774] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.301, 0.2]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.603, -0.304, 0.2] pad_end=[0.603, -0.299, 0.2] measured_pinch=[0.603, -0.301, 0.2]m
     close_dir=[0.0, 1.0, -0.01] fing_dir=[0.0, -0.01, -1.0] q=[-0.99169, -0.64315, 0.96663, -1.38933, -1.653, 0.75824, -0.84779] q_lag=[-0.0, 0.0, -0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.291, 0.808, 1.38, 0.695, 0.693, 0.279, 0.713]rad min=0.279rad
     q_cmd=[-0.99169, -0.64315, 0.96663, -1.38933, -1.65298, 0.75825, -0.84775] effort_Nm=[0.026902657002210617, -0.04536522179841995, 0.0011047953739762306, 0.017668766900897026, 0.001980728469789028, 0.0005621194723062217, -0.0053698159754276276] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0019_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 19. Reopen above shifted fax

```python
s.act(**{'intent': 'Reopen above shifted fax', 'left': None, 'right': {'grip': 1}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 20.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126739578700000_8cac52bd485f4a919ce9a62c30939548.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0020.jpg`
Sim seconds: 71.26666666666667

```text
[obs #020 | act=cf7ec8e7 | sim= 71.27s | wall= 319.2s | Reopen above shifted fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.700rad vel=[0.0, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[0.08349926769733429, 0.09613799303770065, -0.06544153392314911, -0.040598537772893906]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, -0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.01594279333949089, -0.014711160212755203, -0.00587458536028862, 0.002023235894739628, 0.0008566797478124499, 0.00012960933963768184, -0.0006749784224666655] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.301, 0.2]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.603, -0.254, 0.199] pad_end=[0.603, -0.349, 0.2] measured_pinch=[0.603, -0.301, 0.2]m
     close_dir=[0.0, 1.0, -0.01] fing_dir=[0.0, -0.01, -1.0] q=[-0.99169, -0.64315, 0.96663, -1.38933, -1.65298, 0.75825, -0.84775] q_lag=[0.0, -0.0, -0.0, -0.0, 0.0, 0.0, -0.0]rad limit_margins=[2.291, 0.808, 1.38, 0.695, 0.693, 0.279, 0.713]rad min=0.279rad
     q_cmd=[-0.99169, -0.64315, 0.96663, -1.38933, -1.65298, 0.75825, -0.84775] effort_Nm=[0.004008788149803877, -0.01924535073339939, 0.0002744935918599367, 0.007514085620641708, 0.00018787826411426067, 0.0003529782989062369, -0.0011534264776855707] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0020_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 20. Recenter above shifted fax

```python
s.act(**{'intent': 'Recenter above shifted fax', 'left': None, 'right': {'to': [0.63, -0.36, 0.15], 'finger_dir': [0, 0, -1], 'close_dir': [0, 1, 0]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 21.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126751414845000_f38e88bfe19047629d485e5d07d448b6.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0021.jpg`
Sim seconds: 71.9

```text
[obs #021 | act=dc747fa8 | sim= 71.90s | wall= 331.1s | Recenter above shifted fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.700rad vel=[-0.0, -0.001, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[0.17054739594459534, 0.08360403776168823, -0.09590242803096771, -0.044483378529548645]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.0027120260056108236, -0.009827510453760624, -0.0008082798449322581, 0.0023169326595962048, -8.179162978194654e-05, 7.207214366644621e-05, -0.000874113931786269] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.629, -0.362, 0.151]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.629, -0.314, 0.151] pad_end=[0.629, -0.409, 0.152] measured_pinch=[0.629, -0.362, 0.151]m
     close_dir=[0.0, 1.0, -0.01] fing_dir=[0.0, -0.01, -1.0] q=[-1.13856, -0.62403, 1.14107, -0.97902, -1.4699, 0.7095, -0.39779] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.438, 0.789, 1.205, 1.105, 0.876, 0.328, 1.163]rad min=0.328rad
     q_cmd=[-1.13856, -0.62403, 1.14107, -0.97901, -1.46987, 0.7095, -0.39775] effort_Nm=[0.005961424671113491, -0.004077506717294455, 0.0013388623483479023, 0.0016110293800011277, 0.000386964064091444, 0.00030349494772963226, -0.0015875642420724034] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0021_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 21. Cartesian vertical pinch descent

```python
s.act(**{'intent': 'Cartesian vertical pinch descent', 'left': None, 'right': {'to': [0.63, -0.36, 0.035]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': True, 'timeout_seconds': 30.0})
```
Result: stalled; observation 22.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126755320758000_fd0c5f4229e54b92868a9794dd0caae9.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0022.jpg`
Sim seconds: 73.73333333333333

```text
[obs #022 | act=9db313e3 | sim= 73.73s | wall= 335.1s | Cartesian vertical pinch descent]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.01, -1.266, 0.0]m rel_yaw=-4.700rad vel=[-0.0, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[0.01900675520300865, 0.0053182500414550304, -0.014808516949415207, -0.04629197716712952]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.0035273395478725433, -0.015001583844423294, -0.002999599790200591, -0.0015519947046414018, 0.0007541908416897058, 0.0001815633149817586, -0.0011089267209172249] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.616, -0.354, 0.064]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.616, -0.307, 0.064] pad_end=[0.616, -0.402, 0.065] measured_pinch=[0.616, -0.354, 0.064]m
     close_dir=[0.0, 1.0, -0.01] fing_dir=[0.0, -0.01, -1.0] q=[-1.21498, -0.1844, 1.37548, -0.0185, -1.29538, 0.44868, 0.17281] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, 0.0]rad limit_margins=[2.514, 0.349, 0.971, 0.358, 1.051, 0.589, 1.388]rad min=0.349rad
     q_cmd=[-1.21498, -0.1844, 1.37548, -0.0185, -1.29538, 0.44868, 0.17281] effort_Nm=[0.005335125140845776, -0.006063845008611679, -0.00019197762594558299, 0.0021211188286542892, -0.00017751852283254266, 0.00044283809256739914, 0.00011121421994175762] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"IK_stalled","causes":["IK_stalled"],"confidence":"limited","plateau":true,"normalized_error_history":[23.260805958779724,23.180904269614828,22.30789558629599,21.29202554011325,20.643381647055524,20.28203327674726,20.254149830897113,20.787644233478304,22.419173963964045,24.48095713542123,26.609562657830104,28.668821902574226,30.791017315609842,29.65199513688251,29.851507343617584,29.43679994536353,29.312142932210083,28.23550566110496,28.386072512853605,27.968380963291995,27.233228944120757,26.64913760522238,25.974771347602626,25.325751432340702,24.640933082878576,23.938063896021344,23.199514164755392,22.417561517663188,21.579635161311746,20.67089057064467,19.67388217567234,18.569325915171824,17.335390268055107,15.950173576727043,14.396428057320831,12.74089103657933,10.831828769517701,8.939398853746168,7.34041885008192,6.655308611023261,6.653954871391945,6.654235070331861,6.654161070133761,6.6540334459261965,6.654110799724928,6.65404921295065,6.6541861921821415,6.654201614834805,6.653962174690807,6.654173744420606,6.65413212408424,6.654250326778881,6.654245154160504,6.654112919082144,6.65404175962612,6.654305586985679],"normalized_progress":16.606500371794045,"recent_max_joint_lag_rad":[1.1801719665527344e-05,9.298324584960938e-06,2.7418136596679688e-06],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"}}
  status=stalled fault=None uncertain=False pending=['right']
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0022_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 22. Freeze reachable pinch and close

```python
s.act(**{'intent': 'Freeze reachable pinch and close', 'left': None, 'right': {'q': [-1.21498, -0.1844, 1.37548, -0.0185, -1.29538, 0.44868, 0.17281], 'grip': 0}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 23.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126765267630000_a6854fa8022a47f284e9a9e9b971e8c9.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0023.jpg`
Sim seconds: 73.96666666666667

```text
[obs #023 | act=0f2222c9 | sim= 73.97s | wall= 345.0s | Freeze reachable pinch and close]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.01, -1.266, 0.0]m rel_yaw=-4.700rad vel=[0.0, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-0.028439640998840332, -0.006493024528026581, 0.006306413561105728, 0.02540360577404499]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[-0.0, -0.0, -0.0, -0.0, 0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.0014299304457381368, -0.0016629036981612444, -0.0009656241163611412, 0.0005274096038192511, -0.0005361472140066326, -0.00013455594307743013, 0.0007288370979949832] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.616, -0.354, 0.064]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.616, -0.357, 0.064] pad_end=[0.616, -0.352, 0.064] measured_pinch=[0.616, -0.354, 0.064]m
     close_dir=[0.0, 1.0, -0.01] fing_dir=[0.0, -0.01, -1.0] q=[-1.21498, -0.1844, 1.37548, -0.0185, -1.29538, 0.44868, 0.17281] q_lag=[0.0, 0.0, -0.0, -0.0, -0.0, 0.0, 0.0]rad limit_margins=[2.514, 0.349, 0.971, 0.358, 1.051, 0.589, 1.388]rad min=0.349rad
     q_cmd=[-1.21498, -0.1844, 1.37548, -0.0185, -1.29538, 0.44868, 0.17281] effort_Nm=[0.008367464877665043, 0.013792467303574085, -0.0004758378490805626, -0.006933126598596573, -0.0005424716509878635, 0.0002693875867407769, 0.0017222166061401367] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0023_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 23. Verify object lift

```python
s.act(**{'intent': 'Verify object lift', 'left': None, 'right': {'to': [0.616, -0.354, 0.2]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 24.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/receipt_01792126769675213000_2fa156a3ae73446cbf70d312df2f7ce1.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0024.jpg`
Sim seconds: 76.0

```text
[obs #024 | act=641c2741 | sim= 76.00s | wall= 349.4s | Verify object lift]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.700rad vel=[-0.0, -0.001, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[0.1155456006526947, -0.09620395302772522, -0.08393451571464539, -0.3463829457759857]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00321, 2.345, 0.83545, 1.55999] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.051533427089452744, -0.13626116514205933, -0.02818891778588295, -0.016368919983506203, 0.005976093001663685, 0.0011660594027489424, -0.007001736667007208] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.616, -0.354, 0.2]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.616, -0.357, 0.2] pad_end=[0.616, -0.352, 0.2] measured_pinch=[0.616, -0.354, 0.2]m
     close_dir=[0.0, 1.0, -0.01] fing_dir=[0.0, -0.01, -1.0] q=[-1.17226, -0.78095, 1.24509, -1.29957, -1.72669, 0.66118, -0.63362] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.471, 0.945, 1.101, 0.785, 0.62, 0.376, 0.927]rad min=0.376rad
     q_cmd=[-1.17227, -0.78093, 1.2451, -1.29956, -1.72665, 0.6612, -0.63361] effort_Nm=[0.04566389322280884, -0.18082596361637115, 0.0068811457604169846, 0.061814725399017334, 0.002759937196969986, 0.002493713516741991, -0.010810930281877518] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a12/obs_0024_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```
