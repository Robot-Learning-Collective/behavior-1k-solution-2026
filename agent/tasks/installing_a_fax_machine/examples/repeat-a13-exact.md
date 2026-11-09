# a13 exact public action sequence

Historical record, not a blind replay script. Includes unsuccessful recovery motions and rejected requests; inspect images and remeasure before contacts. All arguments preserved, including max_steps.

## 1. Turn toward verified doorway

```python
s.act(**{'intent': 'Turn toward verified doorway', 'left': {'grip': 1}, 'right': {'grip': 1}, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 2.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126814170326000_1796cb75375d4c0b803657105ca6a679.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0002.jpg`
Sim seconds: 5.2

```text
[obs #002 | act=71c62807 | sim=  5.20s | wall=  13.6s | Turn toward verified doorway]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0002_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 2. Measured clear doorway approach

```python
s.act(**{'intent': 'Measured clear doorway approach', 'left': None, 'right': None, 'base': {'fwd': 1}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 3.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126821798493000_a2ae787db6e742cabb35fe445a755eda.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0003.jpg`
Sim seconds: 11.166666666666666

```text
[obs #003 | act=f57bc5e1 | sim= 11.17s | wall=  21.3s | Measured clear doorway approach]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0003_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 3. Measured clear doorway approach

```python
s.act(**{'intent': 'Measured clear doorway approach', 'left': None, 'right': None, 'base': {'fwd': 0.8}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 4.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126828234316000_7c12e8fc75ce4e39aaf3c82ae09ecb9d.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0004.jpg`
Sim seconds: 16.133333333333333

```text
[obs #004 | act=6787c20a | sim= 16.13s | wall=  27.8s | Measured clear doorway approach]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0004_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 4. Clear junction turn

```python
s.act(**{'intent': 'Clear junction turn', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 5.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126841108567000_15801975c624441fbc83f61ff3ffb400.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0005.jpg`
Sim seconds: 21.333333333333332

```text
[obs #005 | act=546b60df | sim= 21.33s | wall=  40.5s | Clear junction turn]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0005_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 5. Aisle offset

```python
s.act(**{'intent': 'Aisle offset', 'left': None, 'right': None, 'base': {'left': 0.5}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 6.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126846433677000_aea949d5a56c4836b7d8f4c531943ca0.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0006.jpg`
Sim seconds: 24.8

```text
[obs #006 | act=4dc19f65 | sim= 24.80s | wall=  45.8s | Aisle offset]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0006_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 6. Measured outer aisle

```python
s.act(**{'intent': 'Measured outer aisle', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 7.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126871380699000_081b0aee948f47828aa9d0172b2514bd.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0007.jpg`
Sim seconds: 31.766666666666666

```text
[obs #007 | act=db7bf2f4 | sim= 31.77s | wall=  70.8s | Measured outer aisle]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0007_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 7. Measured outer aisle

```python
s.act(**{'intent': 'Measured outer aisle', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 8.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126881368624000_35fe52ac41324f27a81c4b6c2152017a.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0008.jpg`
Sim seconds: 38.733333333333334

```text
[obs #008 | act=fc269594 | sim= 38.73s | wall=  80.8s | Measured outer aisle]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0008_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 8. Measured outer aisle

```python
s.act(**{'intent': 'Measured outer aisle', 'left': None, 'right': None, 'base': {'fwd': 1.15}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 9.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126890568826000_313f41b51f494518806dbf40fc0b0277.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0009.jpg`
Sim seconds: 45.46666666666667

```text
[obs #009 | act=cb3948ae | sim= 45.47s | wall=  90.0s | Measured outer aisle]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0009_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 9. Face fax aisle

```python
s.act(**{'intent': 'Face fax aisle', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 10.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126907968653000_059b6309375c40fea37f63c9ddf2780b.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0010.jpg`
Sim seconds: 50.666666666666664

```text
[obs #010 | act=487e8132 | sim= 50.67s | wall= 107.3s | Face fax aisle]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0010_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 10. Align aisle

```python
s.act(**{'intent': 'Align aisle', 'left': None, 'right': None, 'base': {'left': 0.48}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 11.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126914005660000_73178efff85c460f84252986ea94dfe4.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0011.jpg`
Sim seconds: 54.03333333333333

```text
[obs #011 | act=52cba0d9 | sim= 54.03s | wall= 113.4s | Align aisle]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0011_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 11. Narrow arms clear of divider

```python
s.act(**{'intent': 'Narrow arms clear of divider', 'left': {'q': [-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56]}, 'right': {'q': [-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 12.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126919595412000_d596118021fb4974b24941b6d5cb886b.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0012.jpg`
Sim seconds: 57.2

```text
[obs #012 | act=73884e0f | sim= 57.20s | wall= 118.9s | Narrow arms clear of divider]
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
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0012_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 12. Centered fax approach

```python
s.act(**{'intent': 'Centered fax approach', 'left': None, 'right': None, 'base': {'fwd': 0.8}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 13.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126935879202000_3f82858a4396431babbc866566c4501b.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0013.jpg`
Sim seconds: 62.166666666666664

```text
[obs #013 | act=1eb98dda | sim= 62.17s | wall= 135.2s | Centered fax approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.009, -1.53, 0.0]m rel_yaw=-4.699rad vel=[0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[1.5514084100723267, 1.1819303035736084, -0.6888768672943115, -0.37019795179367065]
  L: rigid_TCP(fwd,left,up)=[0.705, 0.086, 0.997]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.705, 0.133, 0.994] pad_end=[0.704, 0.038, 0.999] measured_pinch=[0.705, 0.086, 0.997]m
     close_dir=[0.01, 1.0, -0.05] fing_dir=[0.34, -0.05, -0.94] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, -0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.029693908989429474, -0.17193007469177246, -0.03519389405846596, 0.01547381840646267, 0.000517337117344141, 0.0004946049302816391, -0.006127720233052969] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.505, -0.27, 0.649]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.505, -0.223, 0.649] pad_end=[0.504, -0.318, 0.649] measured_pinch=[0.505, -0.27, 0.649]m
     close_dir=[0.01, 1.0, -0.0] fing_dir=[-0.03, -0.0, -1.0] q=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[-0.0006093168631196022, -0.14069393277168274, -0.02021043375134468, 0.04211486130952835, 0.00014844629913568497, -0.0009160495828837156, -0.0012501318706199527] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0013_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 13. Centered fax approach

```python
s.act(**{'intent': 'Centered fax approach', 'left': None, 'right': None, 'base': {'fwd': 0.27}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 14.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126940430080000_42d09c4a0df540259061520a2cdc48f2.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0014.jpg`
Sim seconds: 64.46666666666667

```text
[obs #014 | act=c7a6eab6 | sim= 64.47s | wall= 139.8s | Centered fax approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.265, 0.0]m rel_yaw=-4.699rad vel=[-0.0, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[1.9537204504013062, 1.4181474447250366, -0.821411669254303, -0.13226976990699768]
  L: rigid_TCP(fwd,left,up)=[0.705, 0.086, 0.997]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.705, 0.133, 0.994] pad_end=[0.704, 0.038, 0.999] measured_pinch=[0.705, 0.086, 0.997]m
     close_dir=[0.01, 1.0, -0.05] fing_dir=[0.34, -0.05, -0.94] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.04862017557024956, -0.028720524162054062, -0.02075767144560814, 0.04958049952983856, -0.005274639930576086, -0.0006984742358326912, 0.0008403565734624863] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.505, -0.27, 0.649]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.505, -0.223, 0.649] pad_end=[0.504, -0.318, 0.649] measured_pinch=[0.505, -0.27, 0.649]m
     close_dir=[0.01, 1.0, -0.0] fing_dir=[-0.03, -0.0, -1.0] q=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[-0.03884639963507652, -0.041578806936740875, -0.011775237508118153, 0.016852563247084618, -0.0009484271868132055, -0.0019837815780192614, 0.0015927954809740186] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0014_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 14. Floor pickup crouch

```python
s.act(**{'intent': 'Floor pickup crouch', 'left': None, 'right': None, 'base': None, 'torso': {'q': [1.68, -2.54, -1.62, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 15.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126944753600000_b98af5e3363f4815bb425c7fead3cf35.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0015.jpg`
Sim seconds: 66.03333333333333

```text
[obs #015 | act=a89cceb9 | sim= 66.03s | wall= 144.2s | Floor pickup crouch]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.265, 0.0]m rel_yaw=-4.700rad vel=[0.0, 0.0, 0.0] | torso=[1.687, -2.54, -1.62, 0.0] err=[-0.007, -0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-100.0, -46.521148681640625, 60.04341506958008, 0.39210379123687744]
  L: rigid_TCP(fwd,left,up)=[0.631, 0.086, 0.25]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.63, 0.133, 0.248] pad_end=[0.633, 0.038, 0.252] measured_pinch=[0.631, 0.086, 0.25]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.37, -0.05, -0.93] q=[-1.30825, 0.05613, -0.97218, -1.0032, 2.34496, 0.83544, 1.55998] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-6.320456027984619, -2.199882984161377, 1.4928048849105835, -3.890822172164917, 0.12165933847427368, 0.018160458654165268, -0.0661364197731018] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.251, -0.27, 0.121]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.252, -0.223, 0.121] pad_end=[0.251, -0.318, 0.122] measured_pinch=[0.251, -0.27, 0.121]m
     close_dir=[0.01, 1.0, -0.01] fing_dir=[-0.68, -0.0, -0.73] q=[-0.52689, -0.35922, 0.79381, -0.97008, -1.51885, 1.036, -0.79466] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[0.8010823726654053, -0.9102396368980408, -0.3186657130718231, -1.4348491430282593, -0.018421709537506104, 0.05025726929306984, -0.014280686154961586] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0015_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 15. Top approach

```python
s.act(**{'intent': 'Top approach', 'left': None, 'right': {'to': [0.61, -0.3, 0.15], 'finger_dir': [0, 0, -1], 'close_dir': [0, 1, 0]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 16.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126955391021000_04d1ef413e4f42e4a608fa0b3df8cb62.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0016.jpg`
Sim seconds: 66.63333333333334

```text
[obs #016 | act=3a78b557 | sim= 66.63s | wall= 154.6s | Top approach]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.265, 0.0]m rel_yaw=-4.700rad vel=[-0.001, 0.0, -0.001] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-0.14464592933654785, 0.08198115974664688, 0.04740498960018158, -0.025825509801506996]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.631, 0.133, 0.252] pad_end=[0.633, 0.038, 0.257] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.020735803991556168, -0.014101887121796608, 0.0018385215662419796, -0.005139695480465889, -0.0003836255054920912, -6.131459667813033e-05, 0.00012621739006135613] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.61, -0.299, 0.151]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.61, -0.252, 0.151] pad_end=[0.61, -0.347, 0.151] measured_pinch=[0.61, -0.3, 0.151]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.0, -0.0, -1.0] q=[-0.93471, -0.47131, 0.77643, -1.11647, -1.27483, 0.84647, -0.57795] q_lag=[-0.0, 0.0, 0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[2.234, 0.636, 1.57, 0.968, 1.071, 0.191, 0.983]rad min=0.191rad
     q_cmd=[-0.93472, -0.47131, 0.77644, -1.11646, -1.27483, 0.84648, -0.57793] effort_Nm=[0.028291301801800728, -0.013338161632418633, 0.005372769199311733, 0.005013517569750547, 0.0006673736497759819, 0.0011127316392958164, -0.001953358529135585] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0016_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 16. Cartesian descent preserve narrow vertical path

```python
s.act(**{'intent': 'Cartesian descent preserve narrow vertical path', 'left': None, 'right': {'to': [0.61, -0.3, 0.035]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': True, 'timeout_seconds': 30.0})
```
Result: stalled; observation 17.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126960300681000_3dd76c8952014fcba69243808f52d032.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0017.jpg`
Sim seconds: 68.6

```text
[obs #017 | act=42b2dc1e | sim= 68.60s | wall= 159.7s | Cartesian descent preserve narrow vertical path]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.265, 0.0]m rel_yaw=-4.701rad vel=[0.0, 0.001, -0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[0.0, 0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[0.21982866525650024, 0.27513402700424194, -0.10502982139587402, 0.2990298569202423]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.631, 0.133, 0.252] pad_end=[0.633, 0.038, 0.257] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] q_lag=[-0.0, 0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.041554611176252365, 0.1548207402229309, 0.027552589774131775, 0.029891040176153183, -0.00720633752644062, -0.0013629912864416838, 0.007737035397440195] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.299, 0.051]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.603, -0.251, 0.051] pad_end=[0.603, -0.346, 0.051] measured_pinch=[0.603, -0.299, 0.051]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17902, -0.09569, 1.07878, -0.03462, -1.0501, 0.43294, 0.07114] q_lag=[0.0, 0.0, -0.0, -0.0, -0.0, 0.0, 0.0]rad limit_margins=[2.478, 0.26, 1.267, 0.374, 1.296, 0.604, 1.49]rad min=0.26rad
     q_cmd=[-1.17902, -0.09568, 1.07877, -0.03462, -1.0501, 0.43294, 0.07114] effort_Nm=[-0.04062214493751526, 0.14195336401462555, -0.001131843775510788, -0.04419803246855736, -0.001495465636253357, -0.0019356098491698503, 0.005830318666994572] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"IK_stalled","causes":["IK_stalled"],"confidence":"limited","plateau":true,"normalized_error_history":[23.212655096406568,23.098591693918085,23.658842271043685,24.875556791026394,26.675558078655687,27.261753735948624,27.625247302195373,27.656259673021065,27.030704075309885,27.27976443774361,27.182965239149524,27.248733688967715,27.24633899787836,27.01214365764394,26.588822804963407,26.23788876739599,25.879358834849093,25.532286340477583,25.189893262500696,24.786899396288845,23.869500099996575,23.20724855809127,21.246878165247917,20.95150163781687,20.02060512071751,19.320158745616325,18.537491005561133,17.77494140584037,17.540019482752246,17.066787651127015,16.36503861254795,15.720922827497374,15.01477561851724,14.22394270719478,13.618960393988855,13.11823798240761,12.690275892069973,12.156446480876602,11.748532433719648,9.6243576819467,5.67622567603532,4.590867863344772,3.655721776489683,3.5194086795830484,3.522155257629425,3.5195175182513525,3.518055191718539,3.5177096284855915,3.517338047144621,3.5172766823832107,3.5171037179500186,3.517157198868953,3.5170727617273334,3.5170981833840966,3.5170375756451087,3.517261621258045,3.5169955980000935,3.517012260000121,3.516969896163707,3.5171365930696403],"normalized_progress":19.695518503336928,"recent_max_joint_lag_rad":[1.0728836059570312e-05,1.239776611328125e-05,5.0067901611328125e-06],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"}}
  status=stalled fault=None uncertain=False pending=['right']
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0017_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 17. Freeze low pose and pinch

```python
s.act(**{'intent': 'Freeze low pose and pinch', 'left': {'grip': 0}, 'right': {'q': [-1.17902, -0.09568, 1.07877, -0.03462, -1.0501, 0.43294, 0.07114], 'grip': 0}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: stalled; observation 18.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126975142376000_fca4b27aa5664f82823a40025a2f3b9d.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0018.jpg`
Sim seconds: 69.23333333333333

```text
[obs #018 | act=c17317f1 | sim= 69.23s | wall= 174.3s | Freeze low pose and pinch]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.265, 0.0]m rel_yaw=-4.700rad vel=[0.0, -0.001, -0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[27.2313232421875, 10.274335861206055, -18.631669998168945, 12.46915054321289]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.255] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30833, 0.0561, -0.97214, -1.00324, 2.345, 0.83544, 1.56002] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[-0.0005303265061229467, 0.009959174320101738, 0.0012941020540893078, 0.0021325000561773777, -0.0003732876502908766, -9.683717507869005e-05, 0.000642414903268218] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.299, 0.051]m fingers=[0.033, 0.0417]m grip=command=0.0 finger_sum(7.5cm)
     pad_start=[0.603, -0.269, 0.051] pad_end=[0.603, -0.338, 0.051] measured_pinch=[0.603, -0.303, 0.051]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17902, -0.09569, 1.07905, -0.0343, -1.04895, 0.43288, 0.07117] q_lag=[0.0, 0.0, -0.0, -0.0, -0.001, 0.0, -0.0]rad limit_margins=[2.478, 0.26, 1.267, 0.373, 1.297, 0.604, 1.49]rad min=0.26rad
     q_cmd=[-1.17902, -0.09568, 1.07877, -0.03462, -1.0501, 0.43294, 0.07114] effort_Nm=[4.276318550109863, 3.8641586303710938, 0.08790469169616699, -1.3210036754608154, 0.024286389350891113, -1.9246786832809448, 0.7127627730369568] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=stalled fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0018_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 18. Lift fax

```python
s.act(**{'intent': 'Lift fax', 'left': None, 'right': {'to': [0.603, -0.299, 0.2]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 19.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126980274625000_0f8ba09a93304beb8dbc73e1e97e8d89.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0019.jpg`
Sim seconds: 71.9

```text
[obs #019 | act=27edbd26 | sim= 71.90s | wall= 179.6s | Lift fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.700rad vel=[-0.0, 0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.7901692390441895, -2.1251821517944336, 3.666275978088379, -0.6173673868179321]
  L: rigid_TCP(fwd,left,up)=[0.632, 0.086, 0.255]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.632, 0.083, 0.255] pad_end=[0.632, 0.088, 0.254] measured_pinch=[0.632, 0.086, 0.255]m
     close_dir=[-0.03, 1.0, -0.05] fing_dir=[-0.36, -0.05, -0.93] q=[-1.30835, 0.05609, -0.97215, -1.00322, 2.34501, 0.83545, 1.56] q_lag=[0.0, 0.0, 0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.607, 0.221, 1.374, 1.081, 0.001, 0.202, 0.001]rad min=0.001rad
     q_cmd=[-1.30834, 0.05609, -0.97215, -1.00322, 2.345, 0.83545, 1.56] effort_Nm=[0.02378072589635849, 0.15640020370483398, 0.013149630278348923, 0.04849524423480034, -0.004106195643544197, -0.000785153592005372, 0.0053238398395478725] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.603, -0.301, 0.2]m fingers=[0.0329, 0.0415]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.603, -0.271, 0.199] pad_end=[0.603, -0.34, 0.2] measured_pinch=[0.603, -0.305, 0.2]m
     close_dir=[-0.0, 1.0, -0.01] fing_dir=[0.0, -0.01, -1.0] q=[-0.99161, -0.64317, 0.96667, -1.38933, -1.65275, 0.75902, -0.84758] q_lag=[-0.0, 0.0, -0.0, 0.0, -0.0, -0.001, -0.0]rad limit_margins=[2.291, 0.808, 1.38, 0.695, 0.693, 0.278, 0.713]rad min=0.278rad
     q_cmd=[-0.99169, -0.64315, 0.96663, -1.38933, -1.65298, 0.75825, -0.84775] effort_Nm=[-1.787473440170288, 0.6587262749671936, -0.8724732398986816, -2.021653175354004, 0.016669392585754395, -0.20733770728111267, 0.2579168379306793] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0019_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 19. Expose switch with tilted fax

```python
s.act(**{'intent': 'Expose switch with tilted fax', 'left': {'to': [0.58, -0.06, 0.36], 'finger_dir': [0.220337, -0.708506, -0.670426], 'close_dir': [-0.038811, 0.680406, -0.731807]}, 'right': {'to': [0.5, -0.08, 0.23], 'pitch_deg': 35}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 20.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792126992376706000_1a55990cdc61482fb96111dae6654853.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0020.jpg`
Sim seconds: 72.96666666666667

```text
[obs #020 | act=c8a459d6 | sim= 72.97s | wall= 191.8s | Expose switch with tilted fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.701rad vel=[-0.001, 0.001, -0.001] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.662674903869629, -2.2534711360931396, 4.149289608001709, -0.39782610535621643]
  L: rigid_TCP(fwd,left,up)=[0.581, -0.06, 0.358]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.581, -0.062, 0.361] pad_end=[0.581, -0.058, 0.357] measured_pinch=[0.581, -0.06, 0.359]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.87845, 0.21564, -1.02692, -1.77819, 1.68529, 0.34264, 0.79112] q_lag=[0.0, -0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.177, 0.38, 1.319, 0.306, 0.661, 0.695, 0.77]rad min=0.306rad
     q_cmd=[-0.87845, 0.21564, -1.02692, -1.77822, 1.68526, 0.34266, 0.79109] effort_Nm=[0.040996942669153214, 0.07372689992189407, -0.001102246344089508, 0.07083013653755188, -0.002225533127784729, -0.0003818189725279808, 0.015646979212760925] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.496, -0.08, 0.228]m fingers=[0.0328, 0.0415]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.496, -0.05, 0.227] pad_end=[0.497, -0.12, 0.228] measured_pinch=[0.496, -0.085, 0.228]m
     close_dir=[-0.0, 1.0, -0.01] fing_dir=[0.55, -0.01, -0.83] q=[-0.63735, -0.22494, 1.36924, -1.51601, -0.87811, -0.01587, -1.23756] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.936, 0.389, 0.977, 0.568, 1.468, 1.021, 0.323]rad min=0.323rad
     q_cmd=[-0.63738, -0.22491, 1.36922, -1.51608, -0.87798, -0.01675, -1.23738] effort_Nm=[-1.7716009616851807, 1.398756742477417, -0.2616257965564728, -2.2926363945007324, 1.5035573244094849, -0.5198251008987427, -0.02942322939634323] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0020_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 20. Approach red switch

```python
s.act(**{'intent': 'Approach red switch', 'left': {'to': [0.616091718673706, -0.0861270135641098, 0.3218520772457123]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 21.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792127001596488000_3c7deec5815d43719354af3ccc686a28.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0021.jpg`
Sim seconds: 73.36666666666666

```text
[obs #021 | act=af37ae88 | sim= 73.37s | wall= 201.0s | Approach red switch]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.266, 0.0]m rel_yaw=-4.701rad vel=[0.0, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.723891735076904, -2.1616318225860596, 3.603968620300293, -0.35931113362312317]
  L: rigid_TCP(fwd,left,up)=[0.616, -0.086, 0.323]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.616, -0.088, 0.325] pad_end=[0.615, -0.084, 0.321] measured_pinch=[0.616, -0.086, 0.323]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.96182, 0.11654, -1.03388, -1.5114, 1.65435, 0.36177, 0.64381] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, -0.0, -0.0]rad limit_margins=[2.261, 0.281, 1.312, 0.573, 0.692, 0.675, 0.917]rad min=0.281rad
     q_cmd=[-0.96182, 0.11653, -1.03389, -1.51138, 1.65437, 0.36176, 0.6438] effort_Nm=[0.006487742532044649, 0.02241920493543148, 0.004072489682585001, -0.01787821389734745, 0.0001790989190340042, -0.0006044512847438455, -0.00413393834605813] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.496, -0.08, 0.228]m fingers=[0.0328, 0.0415]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.496, -0.05, 0.227] pad_end=[0.497, -0.12, 0.228] measured_pinch=[0.496, -0.085, 0.228]m
     close_dir=[-0.0, 1.0, -0.01] fing_dir=[0.56, -0.01, -0.83] q=[-0.63734, -0.22494, 1.36924, -1.516, -0.87809, -0.01588, -1.23756] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.936, 0.389, 0.977, 0.568, 1.468, 1.021, 0.323]rad min=0.323rad
     q_cmd=[-0.63738, -0.22491, 1.36922, -1.51608, -0.87798, -0.01675, -1.23738] effort_Nm=[-1.6201021671295166, 1.3708802461624146, -0.22114276885986328, -2.1834065914154053, 1.471433401107788, -0.5158414840698242, -0.0325712189078331] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0021_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 21. Press switch

```python
s.act(**{'intent': 'Press switch', 'left': {'to': [0.6327101378440857, -0.10445751929283142, 0.2967842173576355]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: stalled; observation 22.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792127011666444000_51069224aa0b4c88a36faf85582f69e1.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0022.jpg`
Sim seconds: 74.13333333333334

```text
[obs #022 | act=8f5e0f6c | sim= 74.13s | wall= 211.1s | Press switch]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.265, 0.0]m rel_yaw=-4.701rad vel=[0.001, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.1180033683776855, -1.8806543350219727, 3.7941040992736816, -0.29783689975738525]
  L: rigid_TCP(fwd,left,up)=[0.632, -0.111, 0.309]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm) TRACKING_ERROR(q4=+0.027)
     pad_start=[0.632, -0.113, 0.311] pad_end=[0.632, -0.109, 0.307] measured_pinch=[0.632, -0.111, 0.309]m
     close_dir=[-0.04, 0.66, -0.75] fing_dir=[0.22, -0.73, -0.65] q=[-1.01154, 0.04205, -1.05042, -1.3434, 1.63168, 0.35494, 0.52801] q_lag=[0.0, 0.0, 0.0, 0.027, -0.01, 0.003, 0.003]rad limit_margins=[2.311, 0.207, 1.296, 0.741, 0.715, 0.682, 1.033]rad min=0.207rad
     q_cmd=[-1.01143, 0.04244, -1.04994, -1.31684, 1.62158, 0.35771, 0.53051] effort_Nm=[5.625851631164551, 28.083559036254883, 3.411301612854004, 25.0000057220459, -5.0230937004089355, -2.7590088844299316, 10.788101196289062] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.495, -0.08, 0.227]m fingers=[0.0329, 0.0415]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.495, -0.05, 0.226] pad_end=[0.495, -0.12, 0.227] measured_pinch=[0.495, -0.085, 0.227]m
     close_dir=[-0.01, 1.0, -0.01] fing_dir=[0.55, -0.01, -0.83] q=[-0.63718, -0.22503, 1.37002, -1.5152, -0.88171, -0.0138, -1.23719] q_lag=[-0.0, 0.0, -0.001, -0.001, 0.004, -0.003, -0.0]rad limit_margins=[1.936, 0.39, 0.976, 0.569, 1.464, 1.023, 0.324]rad min=0.324rad
     q_cmd=[-0.63738, -0.22491, 1.36922, -1.51608, -0.87798, -0.01675, -1.23738] effort_Nm=[-7.292699813842773, 3.078138589859009, -2.0897016525268555, -14.07699966430664, 12.552578926086426, -6.397320747375488, -4.8941330909729] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"blocked","causes":["blocked"],"confidence":"suspected","plateau":true,"normalized_error_history":[7.280315603362607,6.830493600260552,7.811669296788484,8.009471594263255,6.966211046636721,5.22760159273174,3.3778614206716386,2.742575364710996,2.7999589658049215,2.799474978816549,2.7773293838502946,2.7748048006413786,2.7607678937086644,2.7632288117609134,2.7626282906694977,2.762882765227826,2.7628771920214277,2.76259020966786,2.763202947942744,2.7627490593810684,2.762560477654189,2.762843370219668,2.762957235627089,2.7630657571503585],"normalized_progress":4.517249846212248,"recent_max_joint_lag_rad":[0.02655947208404541,0.026560306549072266,0.02656257152557373],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=stalled fault=None uncertain=False pending=['left']
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0022_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 22. Withdraw switch finger

```python
s.act(**{'intent': 'Withdraw switch finger', 'left': {'to': [0.61, -0.04, 0.36]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 23.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792127014377302000_7682fcaff6b8409ba3de596c7bd8b697.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0023.jpg`
Sim seconds: 74.73333333333333

```text
[obs #023 | act=f08527f6 | sim= 74.73s | wall= 213.7s | Withdraw switch finger]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.265, 0.0]m rel_yaw=-4.701rad vel=[-0.0, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.277613639831543, -2.2464561462402344, 3.901057720184326, -0.5983184576034546]
  L: rigid_TCP(fwd,left,up)=[0.611, -0.039, 0.356]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.611, -0.041, 0.358] pad_end=[0.61, -0.038, 0.354] measured_pinch=[0.611, -0.039, 0.356]m
     close_dir=[-0.05, 0.69, -0.72] fing_dir=[0.22, -0.7, -0.68] q=[-0.92842, 0.25095, -0.96633, -1.74181, 1.74895, 0.40595, 0.76625] q_lag=[0.0, 0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[2.227, 0.415, 1.38, 0.343, 0.597, 0.631, 0.795]rad min=0.343rad
     q_cmd=[-0.92842, 0.25095, -0.96633, -1.74184, 1.74892, 0.40596, 0.76625] effort_Nm=[0.037310630083084106, -0.035008739680051804, -0.018071195110678673, 0.055497922003269196, -0.0012577017769217491, -7.340568117797375e-05, 0.006876274477690458] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.496, -0.08, 0.228]m fingers=[0.0328, 0.0416]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.496, -0.05, 0.227] pad_end=[0.497, -0.12, 0.228] measured_pinch=[0.496, -0.085, 0.228]m
     close_dir=[-0.0, 1.0, -0.01] fing_dir=[0.56, -0.01, -0.83] q=[-0.63734, -0.22494, 1.36924, -1.516, -0.87813, -0.0161, -1.23739] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.936, 0.389, 0.977, 0.568, 1.468, 1.021, 0.323]rad min=0.323rad
     q_cmd=[-0.63738, -0.22491, 1.36922, -1.51608, -0.87798, -0.01675, -1.23738] effort_Nm=[-1.625264048576355, 1.257430911064148, -0.22902262210845947, -2.2116281986236572, 1.4635664224624634, -0.5177907347679138, -0.05191287025809288] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0023_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 23. Stand with fax

```python
s.act(**{'intent': 'Stand with fax', 'left': None, 'right': None, 'base': None, 'torso': {'q': [0.84, -1.00609, -0.42, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 24.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792127024527207000_d114886795eb4096bb4dffb6c0a9561d.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0024.jpg`
Sim seconds: 76.83333333333333

```text
[obs #024 | act=a82ec1f7 | sim= 76.83s | wall= 223.9s | Stand with fax]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.011, -1.266, 0.0]m rel_yaw=-4.701rad vel=[0.001, -0.0, -0.001] | torso=[0.842, -1.006, -0.42, -0.0] err=[-0.002, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-99.99725341796875, -58.38994598388672, 36.48366928100586, -0.3269476890563965]
  L: rigid_TCP(fwd,left,up)=[0.693, -0.039, 1.034]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.692, -0.041, 1.036] pad_end=[0.693, -0.038, 1.032] measured_pinch=[0.692, -0.039, 1.034]m
     close_dir=[0.31, 0.69, -0.66] fing_dir=[0.52, -0.7, -0.49] q=[-0.92842, 0.25097, -0.96633, -1.74183, 1.74881, 0.40601, 0.76626] q_lag=[0.0, -0.0, 0.0, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[2.227, 0.415, 1.38, 0.343, 0.597, 0.631, 0.795]rad min=0.343rad
     q_cmd=[-0.92842, 0.25095, -0.96633, -1.74184, 1.74892, 0.40596, 0.76625] effort_Nm=[-0.37688493728637695, -1.1905580759048462, -0.015688329935073853, -2.42974853515625, 0.07063208520412445, 0.03161255270242691, -0.25962498784065247] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.654, -0.08, 0.866]m fingers=[0.0328, 0.0416]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.654, -0.05, 0.866] pad_end=[0.654, -0.12, 0.867] measured_pinch=[0.654, -0.085, 0.866]m
     close_dir=[0.0, 1.0, -0.01] fing_dir=[0.89, -0.01, -0.46] q=[-0.63728, -0.22497, 1.36926, -1.51593, -0.87836, -0.01607, -1.23739] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.936, 0.389, 0.977, 0.568, 1.468, 1.021, 0.323]rad min=0.323rad
     q_cmd=[-0.63738, -0.22491, 1.36922, -1.51608, -0.87798, -0.01675, -1.23738] effort_Nm=[-2.3620173931121826, 2.081638813018799, -0.7721748352050781, -4.512741565704346, 2.6582679748535156, -0.9404223561286926, -0.0743725523352623] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0024_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 24. Overhead clearance carry

```python
s.act(**{'intent': 'Overhead clearance carry', 'left': {'q': [0, 0, 0, 0, 0, 0, 0]}, 'right': {'q': [-2.6, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 25.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792127029763147000_e4a7a0f377694a3b8eb1db0dbc15c289.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0025.jpg`
Sim seconds: 79.5

```text
[obs #025 | act=f83be83c | sim= 79.50s | wall= 229.2s | Overhead clearance carry]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.012, -1.266, 0.0]m rel_yaw=-4.702rad vel=[0.001, 0.0, -0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-38.073387145996094, -26.443702697753906, 20.107959747314453, -1.7083768844604492]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, 1e-05, -2e-05, 0.0, 0.0, -1e-05] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.7941201329231262, -0.12498042732477188, -0.0034213289618492126, 0.18485336005687714, -0.0026559606194496155, 0.014324652962386608, -0.003420436754822731] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.242, 1.689]m fingers=[0.0329, 0.0416]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.874, -0.212, 1.689] pad_end=[0.869, -0.281, 1.689] measured_pinch=[0.871, -0.246, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59978, 0.05001, -0.12973, -0.11973, 0.06632, 1.00026, -0.13956] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.001, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.216, 0.459, 2.28, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-10.476668357849121, 0.8213610649108887, 0.15437112748622894, -5.6433539390563965, -0.0033800331875681877, -2.7231781482696533, 0.2762197256088257] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0025_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 25. Center beneath open turn area

```python
s.act(**{'intent': 'Center beneath open turn area', 'left': None, 'right': None, 'base': {'fwd': 0.35}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 26.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792127043878588000_c341d4d795aa4d12ad3b3c01fef84aad.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0026.jpg`
Sim seconds: 82.2

```text
[obs #026 | act=f66f2574 | sim= 82.20s | wall= 243.4s | Center beneath open turn area]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.015, -0.921, 0.0]m rel_yaw=-4.702rad vel=[0.0, -0.001, -0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.343255519866943, -5.18067741394043, 5.6917314529418945, -0.5617859959602356]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, 0.0, -1e-05, 0.0, -0.0, -0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.06423373520374298, -0.03308930993080139, 0.00026779621839523315, -0.02312752604484558, 0.0002930988557636738, -0.00357454433105886, -0.001110332552343607] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0329, 0.0416]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.873, -0.211, 1.689] pad_end=[0.869, -0.28, 1.689] measured_pinch=[0.871, -0.246, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59985, 0.05003, -0.13082, -0.11976, 0.06453, 1.00007, -0.13956] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.215, 0.459, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.031408309936523, -0.139937162399292, 0.2229205220937729, -3.2914443016052246, 0.16929037868976593, -2.041931629180908, -0.01115885004401207] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0026_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 26. Turn above divider

```python
s.act(**{'intent': 'Turn above divider', 'left': None, 'right': None, 'base': {'yaw_deg': 115}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.005, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 27.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792127052928173000_53be4b68ecad49e392b78cff9d1f36cb.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0027.jpg`
Sim seconds: 88.46666666666667

```text
[obs #027 | act=6406c732 | sim= 88.47s | wall= 252.4s | Turn above divider]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.015, -0.921, 0.0]m rel_yaw=-2.699rad vel=[0.0, -0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.696839332580566, -5.57188081741333, 5.83478307723999, -0.4943215847015381]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, -0.0, -1e-05, 0.0, -0.0, -0.0] q_lag=[0.0, -0.0, 0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.011890174821019173, 0.05664224550127983, 0.00029077380895614624, 0.00589490681886673, 9.367946768179536e-05, 0.0015250085853040218, 0.0017456369241699576] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0329, 0.0416]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.873, -0.211, 1.689] pad_end=[0.869, -0.28, 1.689] measured_pinch=[0.871, -0.246, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59986, 0.05003, -0.1309, -0.11976, 0.06438, 1.00005, -0.13956] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.001, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.215, 0.459, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.035669326782227, -0.046819210052490234, 0.23893141746520996, -3.282703399658203, 0.1842496395111084, -2.043466806411743, -0.03190207481384277] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0027_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 27. Lower only to above-rail release pose

```python
s.act(**{'intent': 'Lower only to above-rail release pose', 'left': None, 'right': {'q': [-1.65, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 28.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792127063665829000_da6dc39ad9d94de382af4522efb602c3.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0028.jpg`
Sim seconds: 89.76666666666667

```text
[obs #028 | act=18507bd7 | sim= 89.77s | wall= 263.1s | Lower only to above-rail release pose]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.015, -0.921, 0.0]m rel_yaw=-2.699rad vel=[0.001, 0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[21.19461441040039, 13.63241958618164, -11.169845581054688, -4.787106513977051]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-4e-05, -0.0, -1e-05, 2e-05, 1e-05, -1e-05, 0.0] q_lag=[0.0, 0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.394485741853714, -0.10242858529090881, -0.0005468316376209259, -0.04454769939184189, -0.0006002811715006828, 0.00649619335308671, -0.004759435076266527] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.24, 1.035]m fingers=[0.0329, 0.0415]m grip=command=0.0 finger_sum(7.4cm)
     pad_start=[0.942, -0.21, 1.034] pad_end=[0.939, -0.279, 1.036] measured_pinch=[0.94, -0.244, 1.035]m
     close_dir=[0.04, 1.0, -0.04] fing_dir=[0.49, -0.05, -0.87] q=[-1.64995, 0.05006, -0.13394, -0.11948, 0.05932, 0.99948, -0.13957] q_lag=[-0.0, -0.0, 0.004, -0.001, 0.006, 0.001, -0.0]rad limit_margins=[2.791, 0.114, 2.212, 0.459, 2.287, 0.038, 1.421]rad min=0.038rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[6.172004222869873, -4.621878623962402, 0.759873628616333, 2.337501049041748, 1.111430048942566, 0.6416932344436646, -1.518086552619934] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0028_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 28. Release above solid carrel surface short drop

```python
s.act(**{'intent': 'Release above solid carrel surface short drop', 'left': None, 'right': {'grip': 1}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 29.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792127075388033000_1bfb27017e6f4af4b7237e5ba298371d.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0029.jpg`
Sim seconds: 89.9

```text
[obs #029 | act=ce9bd44e | sim= 89.90s | wall= 274.7s | Release above solid carrel surface short drop]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.015, -0.921, 0.0]m rel_yaw=-2.699rad vel=[-0.0, 0.0, 0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, 0.0, -0.0, -0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[0.2695227861404419, -0.011828887276351452, -0.03056742250919342, 0.19561144709587097]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.006760789081454277, 0.09643380343914032, 0.0007595587521791458, 0.0005025430582463741, 0.0005036694929003716, 0.00021293935424182564, 0.003848069114610553] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.242, 1.035]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.942, -0.194, 1.033] pad_end=[0.939, -0.289, 1.038] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.05] fing_dir=[0.49, -0.06, -0.87] q=[-1.65, 0.05, -0.12999, -0.12, 0.06501, 1.0, -0.14] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[2.791, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[0.0027602482587099075, 0.12878091633319855, 0.005886890459805727, 0.0028183553367853165, 0.0011562018189579248, -0.0018309281440451741, 7.237937825266272e-05] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0029_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 29. Withdraw empty hand to verify independent support

```python
s.act(**{'intent': 'Withdraw empty hand to verify independent support', 'left': None, 'right': {'q': [-2.1, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False, 'timeout_seconds': 30.0})
```
Result: reached; observation 30.

Receipt: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/receipt_01792127078005509000_c48693010a3647919cdc7e3353ed0717.json`
Image: `<observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0030.jpg`
Sim seconds: 90.53333333333333

```text
[obs #030 | act=517c413b | sim= 90.53s | wall= 277.3s | Withdraw empty hand to verify independent support]
  base_odom(integrated_proprio_base_qvel_planar_estimate): rel_xyz=[-4.016, -0.921, 0.0]m rel_yaw=-2.699rad vel=[-0.0, -0.001, 0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, -0.0, -0.0, 0.0]
  odom_uncertainty: uncalibrated drift; no absolute world pose, vertical motion or tilt observation
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-26.552967071533203, -17.174983978271484, 10.457154273986816, -1.017546534538269]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-0.0, -0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, 0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[1.0535006523132324, -0.0786958560347557, -0.0042861998081207275, 0.25688934326171875, -0.003498576581478119, 0.0217531006783247, -0.001643447089008987] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.987, -0.242, 1.353]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.989, -0.194, 1.352] pad_end=[0.984, -0.289, 1.354] measured_pinch=[0.987, -0.242, 1.353]m
     close_dir=[0.06, 1.0, -0.03] fing_dir=[0.82, -0.06, -0.57] q=[-2.09997, 0.05, -0.13, -0.12001, 0.06497, 0.99999, -0.14] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, -0.0]rad limit_margins=[2.341, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.1, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-2.1799442768096924, -0.26219475269317627, 0.047791123390197754, -0.7865500450134277, 0.05101817846298218, -0.050718724727630615, -0.06104852259159088] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=reached fault=None uncertain=False pending=[]
  depth saved: <observation-cache>/fax-run-008-p6-1946b1/fax-run-008-v6-a13/obs_0030_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```
