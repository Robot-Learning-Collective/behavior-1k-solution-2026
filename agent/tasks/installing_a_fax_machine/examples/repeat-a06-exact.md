# a06 exact public action sequence

Historical record, not a blind replay script. Includes unsuccessful recovery motions and rejected requests; inspect images and remeasure before contacts. All arguments preserved, including max_steps.

## 1. Empty-hand aisle navigation 1

```python
s.act(**{'intent': 'Empty-hand aisle navigation 1', 'left': {'grip': 1}, 'right': {'grip': 1}, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 65.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792119517492917000_50045f105ded42bc98213043a77739a9.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0065.jpg`
Sim seconds: 8.0

```text
[obs #065 | act=09f77565 | sim=  8.00s | wall=  60.3s | Empty-hand aisle navigation 1]
  base_odom(sim): rel_xyz=[-0.0, -0.0, 0.0]m rel_yaw=-1.553rad vel=[-0.001, 0.0, -0.201] | torso=[1.025, -1.45, -0.47, 0.0] err=[-0.0, 0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.2793484628200531, 0.14373570680618286, -0.08937229216098785, 0.009063621051609516]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, 0.0, -0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.009620709344744682, 0.022692587226629257, 0.00034847206552512944, -0.00223710248246789, 0.0002911291958298534, -3.407906842767261e-05, 0.0009859352139756083] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.011940887197852135, 0.05562559515237808, 0.0004838267050217837, -0.0014220249140635133, 0.00041193829383701086, 0.0002225639473181218, 0.0025476175360381603] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0065_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 2. Empty-hand aisle navigation 2

```python
s.act(**{'intent': 'Empty-hand aisle navigation 2', 'left': None, 'right': None, 'base': {'fwd': 1.0}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 149.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792119587227214000_855e7c8a5e4c4a7d8b970dd9e7317327.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0149.jpg`
Sim seconds: 18.5

```text
[obs #149 | act=6e8ffe3e | sim= 18.50s | wall= 130.0s | Empty-hand aisle navigation 2]
  base_odom(sim): rel_xyz=[0.017, -0.999, -0.0]m rel_yaw=-1.553rad vel=[0.049, 0.0, 0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.02335178107023239, -0.01658075861632824, 0.007570438086986542, -0.0026570407208055258]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[1e-05, -0.0, -1e-05, 0.0, -0.0, 0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.0009683649986982346, -0.0015105705242604017, -1.3486229363479652e-05, 0.00036057253601029515, -1.4503786587738432e-05, 6.888743519084528e-05, -0.00012184426304884255] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.002127868589013815, -0.0013297476107254624, -6.757592927897349e-06, 0.0005231736577115953, -1.0294245839759242e-05, 4.93979241582565e-05, -0.00013004291395191103] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0149_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 3. Empty-hand aisle navigation 3

```python
s.act(**{'intent': 'Empty-hand aisle navigation 3', 'left': None, 'right': None, 'base': {'fwd': 0.8}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 217.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792119643871077000_66f94b154c754dd39c1d8997d4288397.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0217.jpg`
Sim seconds: 27.0

```text
[obs #217 | act=e6459524 | sim= 27.00s | wall= 186.7s | Empty-hand aisle navigation 3]
  base_odom(sim): rel_xyz=[0.031, -1.797, -0.005]m rel_yaw=-1.553rad vel=[0.039, -0.0, -0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.0061258189380168915, 0.0029280991293489933, -0.0010933345183730125, -0.0010656735394150019]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[1e-05, -0.0, -1e-05, 0.0, -0.0, 0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.0009272365132346749, 0.00045287839020602405, 5.8652904044720344e-06, -0.00027848570607602596, 2.583118657639716e-06, -3.07900772895664e-05, -7.121809630916687e-06] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.0004507193807512522, 0.00041225901804864407, 4.274364073353354e-06, -0.00023786279780324548, 1.8968828499055235e-06, -5.253653944237158e-05, -1.3405256140686106e-05] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0217_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 4. Empty-hand aisle navigation 4

```python
s.act(**{'intent': 'Empty-hand aisle navigation 4', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 281.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792119697321055000_6b1c1b7547a047bea397219543a1b2c3.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0281.jpg`
Sim seconds: 35.0

```text
[obs #281 | act=f614a203 | sim= 35.00s | wall= 240.1s | Empty-hand aisle navigation 4]
  base_odom(sim): rel_xyz=[0.031, -1.797, -0.005]m rel_yaw=-3.106rad vel=[-0.0, 0.001, -0.2] | torso=[1.025, -1.45, -0.47, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.2292858064174652, 0.11591701954603195, -0.07469308376312256, 0.009432237595319748]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, 0.0, -0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.008311132900416851, 0.030607158318161964, 0.0003740638494491577, -0.0019523173104971647, 0.0003064710181206465, -4.8653113481123e-05, 0.0014373735757544637] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, -0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.009620759636163712, 0.062381286174058914, 0.0005300864577293396, -0.0010116941994056106, 0.0004396578297019005, 0.00023133627837523818, 0.0030211317352950573] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0281_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 5. Empty-hand aisle navigation 5

```python
s.act(**{'intent': 'Empty-hand aisle navigation 5', 'left': None, 'right': None, 'base': {'left': 0.35}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 313.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792119724114335000_cdc06e95d7d243dbb0e35d9c3c10e8cc.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0313.jpg`
Sim seconds: 39.0

```text
[obs #313 | act=28348abe | sim= 39.00s | wall= 266.9s | Empty-hand aisle navigation 5]
  base_odom(sim): rel_xyz=[0.044, -2.146, -0.007]m rel_yaw=-3.106rad vel=[-0.0, 0.012, 0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, -0.0, -0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.06365014612674713, -0.024954315274953842, 0.016407843679189682, 0.0018369117751717567]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, -0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.0045333439484238625, -0.007962297648191452, -4.453863948583603e-05, 0.0013080836506560445, -2.7546659111976624e-05, 0.00012572412379086018, -0.0002636567805893719] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.002148536965250969, -0.006800372153520584, -3.914115950465202e-06, 0.0005157112027518451, 1.5085097402334213e-06, 3.579684198484756e-05, -0.0001806307991500944] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0313_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 6. Empty-hand aisle navigation 6

```python
s.act(**{'intent': 'Empty-hand aisle navigation 6', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 413.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792119806646541000_d074ee19055e409988b682d570adbedb.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0413.jpg`
Sim seconds: 51.5

```text
[obs #413 | act=a12e6b87 | sim= 51.50s | wall= 349.4s | Empty-hand aisle navigation 6]
  base_odom(sim): rel_xyz=[-1.154, -2.189, -0.007]m rel_yaw=-3.106rad vel=[0.06, 0.0, 0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.01744738221168518, -0.007173124700784683, 0.005280840210616589, -0.0009113363921642303]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[1e-05, -0.0, -1e-05, 0.0, -0.0, 0.0, -0.0] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.00016785798652563244, 0.009373238310217857, 1.1854339390993118e-05, -0.00017255045531783253, 8.448143489658833e-06, -4.9063066398957744e-05, 0.0003583210345823318] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.0011494732461869717, 0.008528921753168106, 1.5161465853452682e-05, 0.00031076735467649996, 1.110701123252511e-05, 4.316177000873722e-05, 0.0003674349864013493] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0413_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 7. Empty-hand aisle navigation 7

```python
s.act(**{'intent': 'Empty-hand aisle navigation 7', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 513.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792119887290326000_478c07c8b79a45038dfc0880dec12a2c.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0513.jpg`
Sim seconds: 64.0

```text
[obs #513 | act=3d3f18f8 | sim= 64.00s | wall= 430.1s | Empty-hand aisle navigation 7]
  base_odom(sim): rel_xyz=[-2.352, -2.231, -0.008]m rel_yaw=-3.106rad vel=[0.059, 0.0, 0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.0330045223236084, 0.030781181529164314, -0.013703377917408943, 0.00728846900165081]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[1e-05, -0.0, -1e-05, 0.0, -0.0, 0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.0006007737247273326, -0.0045739128254354, -4.302477464079857e-06, -0.00036945598549209535, 1.882115611806512e-05, -0.00013892474817112088, 7.97980756033212e-05] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.004195214714854956, -0.004270937759429216, -2.189014048781246e-05, -0.0008118581026792526, 2.8123613446950912e-06, -1.1289625945209991e-05, 0.00011769253615057096] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0513_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 8. Empty-hand aisle navigation 8

```python
s.act(**{'intent': 'Empty-hand aisle navigation 8', 'left': None, 'right': None, 'base': {'fwd': 1.15}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 609.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792119964073792000_d7e9901612ed4df0ab93b3aa68c9b5f8.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0609.jpg`
Sim seconds: 76.0

```text
[obs #609 | act=da8281f8 | sim= 76.00s | wall= 506.9s | Empty-hand aisle navigation 8]
  base_odom(sim): rel_xyz=[-3.5, -2.272, -0.008]m rel_yaw=-3.106rad vel=[0.056, 0.0, 0.0] | torso=[1.025, -1.45, -0.47, -0.0] err=[0.0, 0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.09114882349967957, 0.04480494558811188, -0.0036822871770709753, 0.0028039137832820415]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[1e-05, -0.0, -1e-05, 0.0, -0.0, 0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.0003323206037748605, 0.000702474731951952, -2.0118823158554733e-05, 0.00020253891125321388, -3.0721883376827464e-05, -0.00011140798596898094, 4.1121307731373236e-05] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, -0.0, -1e-05, 0.0, -0.0, -0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[0.00042632751865312457, 0.00019070092821493745, -1.0978721547871828e-05, 0.0002591092197690159, -2.142936864402145e-05, -5.852564936503768e-05, 2.5705512598506175e-05] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0609_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 9. Empty-hand aisle navigation 9

```python
s.act(**{'intent': 'Empty-hand aisle navigation 9', 'left': None, 'right': None, 'base': {'yaw_deg': -70}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 661.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120007017984000_cc8759c99a6c4436be976bd290024efe.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0661.jpg`
Sim seconds: 82.5

```text
[obs #661 | act=f94d6aca | sim= 82.50s | wall= 549.8s | Empty-hand aisle navigation 9]
  base_odom(sim): rel_xyz=[-3.5, -2.272, -0.008]m rel_yaw=+1.958rad vel=[-0.0, 0.001, -0.114] | torso=[1.025, -1.45, -0.47, 0.0] err=[0.0, -0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.2662099599838257, 0.15185751020908356, -0.0881786122918129, 0.02099042944610119]
  L: rigid_TCP(fwd,left,up)=[0.121, 0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, 0.299, 0.438] pad_end=[0.121, 0.204, 0.438] measured_pinch=[0.121, 0.252, 0.438]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[0.0, 0.0, -0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.010287945158779621, 0.05052463710308075, 0.000524517148733139, -0.003100222209468484, 0.0004114285111427307, -0.0002702597703319043, 0.00213175849057734] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.121, -0.252, 0.438]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.121, -0.205, 0.438] pad_end=[0.121, -0.3, 0.438] measured_pinch=[0.121, -0.252, 0.438]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.0, 0.0, 1e-05, -0.0, 0.0, 0.0, 0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0] effort_Nm=[-0.016622137278318405, 0.058856889605522156, 0.0004415549337863922, -0.0026409681886434555, 0.0003792727366089821, 5.9841579059138894e-05, 0.0026792448479682207] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0661_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 10. Approach fax with raised empty hands

```python
s.act(**{'intent': 'Approach fax with raised empty hands', 'left': {'q': [-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232]}, 'right': {'q': [-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466]}, 'base': {'fwd': 0.78}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 767.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120100901106000_26efae7cf0994deb9948760ee7bc68b9.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0767.jpg`
Sim seconds: 96.33333333333333

```text
[obs #767 | act=21814bc5 | sim= 96.33s | wall= 643.7s | Approach fax with raised empty hands]
  base_odom(sim): rel_xyz=[-3.794, -1.552, -0.003]m rel_yaw=+1.958rad vel=[0.098, -0.017, 0.006] | torso=[1.025, -1.45, -0.47, 0.0] err=[0.0, 0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[-0.5180917978286743, -0.28727152943611145, 0.18746492266654968, -0.03727775812149048]
  L: rigid_TCP(fwd,left,up)=[0.45, 0.28, 0.75]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.45, 0.327, 0.75] pad_end=[0.45, 0.232, 0.75] measured_pinch=[0.45, 0.28, 0.75]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[-0.012182217091321945, -0.022628311067819595, 0.0004158357623964548, -0.017974544316530228, -3.203412052243948e-05, 4.144327249377966e-05, -0.0007492119912058115] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.505, -0.27, 0.649]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.505, -0.223, 0.649] pad_end=[0.504, -0.318, 0.649] measured_pinch=[0.505, -0.27, 0.649]m
     close_dir=[0.01, 1.0, -0.0] fing_dir=[-0.03, -0.0, -1.0] q=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.03601, -0.79466] q_lag=[-0.0, -0.0, -0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[0.011038348078727722, -0.010492286644876003, -0.0006144163780845702, -0.00644928403198719, -0.0030384776182472706, 0.000594675017055124, 0.0029704475309699774] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0767_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 11. Deep floor crouch

```python
s.act(**{'intent': 'Deep floor crouch', 'left': None, 'right': None, 'base': None, 'torso': {'q': [1.68, -2.54, -1.62, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 783.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120109486835000_f7a86996d6ca40a69116ce9017f8bea1.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0783.jpg`
Sim seconds: 98.73333333333333

```text
[obs #783 | act=81e7fcc0 | sim= 98.73s | wall= 652.3s | Deep floor crouch]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[0.0, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, -0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-8.327493667602539, 1.8994674682617188, 5.4804582595825195, 0.16040468215942383]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.278, 0.327, 0.235] pad_end=[0.278, 0.232, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.4119, 0.60027, -0.73518, -1.60059, 2.24215, 0.96342, 1.52232] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, -0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[-0.7079445123672485, 0.429945707321167, 0.3584718108177185, -0.5155739188194275, 8.7738037109375e-05, 8.031679317355156e-05, -0.006752088200300932] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.253, -0.27, 0.123]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.253, -0.223, 0.123] pad_end=[0.252, -0.318, 0.124] measured_pinch=[0.253, -0.27, 0.123]m
     close_dir=[0.01, 1.0, -0.01] fing_dir=[-0.68, 0.0, -0.73] q=[-0.52689, -0.35921, 0.79381, -0.97008, -1.51893, 1.03598, -0.79466] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[-1.0481735467910767, -0.2802959978580475, -0.28998085856437683, -0.4755569100379944, 0.016000375151634216, -0.01657889597117901, -0.010432271286845207] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0783_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 12. Align downward open fingers above measured fax

```python
s.act(**{'intent': 'Align downward open fingers above measured fax', 'left': None, 'right': {'to': [0.61, -0.32, 0.15], 'finger_dir': [0, 0, -1], 'close_dir': [0, 1, 0]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 833.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120139657094000_6b0a9f73fc5d4cbd817eb9f7db2499aa.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0833.jpg`
Sim seconds: 105.7

```text
[obs #833 | act=2a70a10c | sim=105.70s | wall= 682.4s | Align downward open fingers above measured fax]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[0.0, -0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[0.2724786698818207, 0.006873190402984619, -0.33754342794418335, -0.3381076157093048]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.278, 0.327, 0.235] pad_end=[0.278, 0.232, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.41197, 0.60027, -0.7352, -1.60057, 2.24216, 0.96342, 1.52232] q_lag=[0.0, 0.0, 0.0, -0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[-0.01963743008673191, 0.03525109589099884, 0.01099489163607359, 0.01778503693640232, -0.0016051777638494968, -0.00030713650630787015, 0.001617221045307815] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.61, -0.32, 0.15]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.61, -0.273, 0.15] pad_end=[0.61, -0.368, 0.15] measured_pinch=[0.61, -0.32, 0.15]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-0.93538, -0.50537, 0.76731, -1.09542, -1.23758, 0.85127, -0.50449] q_lag=[-0.0, 0.0, 0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[2.234, 0.67, 1.579, 0.989, 1.109, 0.186, 1.056]rad min=0.186rad
     q_cmd=[-0.93545, -0.50534, 0.76734, -1.09532, -1.23767, 0.85129, -0.50443] effort_Nm=[0.5752475261688232, 0.04578360170125961, 0.16551773250102997, 0.05135997384786606, -0.019487733021378517, 0.03390582650899887, 0.00938499066978693] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0833_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 13. Lower open fingers around casing

```python
s.act(**{'intent': 'Lower open fingers around casing', 'left': None, 'right': {'to': [0.61, -0.32, 0.035]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: no_progress; observation 862.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120161190675000_15c0a423bebb4130ab67f76be0fc1e20.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0862.jpg`
Sim seconds: 109.63333333333334

```text
[obs #862 | act=3f7dfde2 | sim=109.63s | wall= 704.0s | Lower open fingers around casing]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-0.1240050196647644, -0.0983545109629631, 0.023619964718818665, -0.2427113950252533]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.278, 0.327, 0.235] pad_end=[0.278, 0.232, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[0.00714186392724514, -0.037315212190151215, -0.013035186566412449, -0.013529479503631592, 0.002814567182213068, 0.0005942092975601554, -0.002855599857866764] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.602, -0.318, 0.053]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.602, -0.271, 0.053] pad_end=[0.602, -0.365, 0.053] measured_pinch=[0.602, -0.318, 0.053]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17843, -0.12875, 1.02494, -0.03335, -0.98062, 0.4317, 0.10983] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.477, 0.293, 1.321, 0.372, 1.366, 0.605, 1.451]rad min=0.293rad
     q_cmd=[-1.17846, -0.1287, 1.02495, -0.03324, -0.98061, 0.43166, 0.10989] effort_Nm=[0.1032748818397522, -0.16788646578788757, 0.00036371126770973206, 0.03533134609460831, 0.0001218058168888092, 0.0023662634193897247, -0.0016559493960812688] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"IK_stalled","causes":["IK_stalled"],"confidence":"limited","plateau":true,"normalized_error_history":[23.07374612133151,13.347501091790638,5.315067847297525,3.9041216325642925,3.9045371511563607,3.904542169865021,3.90472371171722],"normalized_progress":19.16902240961429,"recent_max_joint_lag_rad":[0.00011532381176948547,0.00011539459228515625,0.00011517852544784546],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"}}
  status=no_progress fault=None uncertain=False pending=['right']
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0862_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 14. Close at casing height and ready left probe

```python
s.act(**{'intent': 'Close at casing height and ready left probe', 'left': {'grip': 0}, 'right': {'q': [-1.17843, -0.12875, 1.02494, -0.03335, -0.98062, 0.4317, 0.10983], 'grip': 0}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 4, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 870.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120176267144000_7b2e3ac16be34d26b8a8bd0eca7ca3bb.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0870.jpg`
Sim seconds: 110.63333333333334

```text
[obs #870 | act=be85300a | sim=110.63s | wall= 719.1s | Close at casing height and ready left probe]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, -0.0, 0.001] | torso=[1.68, -2.54, -1.62, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[38.385414123535156, 15.532102584838867, -25.628646850585938, 18.97982406616211]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.278, 0.277, 0.235] pad_end=[0.278, 0.282, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.41188, 0.60029, -0.73511, -1.60062, 2.24214, 0.96342, 1.52232] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[-0.1907820701599121, 0.04420001059770584, 0.033923421055078506, 0.16036878526210785, -0.010263603180646896, -0.001988928532227874, 0.005604228004813194] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.602, -0.318, 0.053]m fingers=[0.0357, 0.0344]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.602, -0.285, 0.053] pad_end=[0.602, -0.35, 0.053] measured_pinch=[0.602, -0.318, 0.053]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17845, -0.12884, 1.02416, -0.03312, -0.97856, 0.43162, 0.10931] q_lag=[0.0, 0.0, 0.001, -0.0, -0.002, 0.0, 0.001]rad limit_margins=[2.477, 0.293, 1.322, 0.372, 1.368, 0.606, 1.451]rad min=0.293rad
     q_cmd=[-1.17843, -0.12875, 1.02494, -0.03335, -0.98062, 0.4317, 0.10983] effort_Nm=[5.132716178894043, 9.123408317565918, 0.3853898048400879, -3.0454347133636475, 0.2710916996002197, -2.158237934112549, 0.6732176542282104] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0870_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 15. Lift retained fax

```python
s.act(**{'intent': 'Lift retained fax', 'left': None, 'right': {'to': [0.602, -0.318, 0.2]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 12, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 893.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120191586440000_a0f7b501eab8407e97faeb149588b155.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0893.jpg`
Sim seconds: 113.8

```text
[obs #893 | act=4a1149c0 | sim=113.80s | wall= 734.4s | Lift retained fax]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[0.0, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-3.0178465843200684, -1.2145664691925049, 2.27243709564209, -2.3853988647460938]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.278, 0.277, 0.235] pad_end=[0.278, 0.282, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.41198, 0.60026, -0.73521, -1.60057, 2.24216, 0.96342, 1.52232] q_lag=[0.0, 0.0, 0.0, -0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[-0.030818412080407143, 0.04291435703635216, 0.01253051683306694, 0.04154682531952858, -0.0036534396931529045, -0.0006803601863794029, 0.002923792926594615] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.602, -0.318, 0.199]m fingers=[0.0357, 0.0343]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.602, -0.286, 0.199] pad_end=[0.602, -0.35, 0.199] measured_pinch=[0.602, -0.318, 0.199]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-0.84627, -0.57343, 0.65307, -1.37437, -1.41302, 0.95703, -0.75458] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[2.145, 0.738, 1.693, 0.71, 0.933, 0.08, 0.806]rad min=0.08rad
     q_cmd=[-0.84628, -0.57344, 0.65292, -1.37455, -1.41324, 0.95684, -0.75506] effort_Nm=[-0.9784454107284546, -1.2271016836166382, -0.8060085773468018, -0.7350713014602661, 0.24951045215129852, -0.07100751996040344, -0.2811850309371948] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0893_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 16. Tilt fax and angle left fingers toward switch

```python
s.act(**{'intent': 'Tilt fax and angle left fingers toward switch', 'left': {'to': [0.58, -0.06, 0.36], 'finger_dir': [0.220337, -0.708506, -0.670426], 'close_dir': [-0.038811, 0.680406, -0.731807]}, 'right': {'to': [0.5, -0.08, 0.23], 'pitch_deg': 35}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 958.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120235948935000_7fde29a3b16741ef91beef44fd8fbfd9.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0958.jpg`
Sim seconds: 122.93333333333334

```text
[obs #958 | act=20aad71c | sim=122.93s | wall= 778.5s | Tilt fax and angle left fingers toward switch]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.810907363891602, -2.024897813796997, 3.31425142288208, 0.23953235149383545]
  L: rigid_TCP(fwd,left,up)=[0.58, -0.06, 0.36]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.58, -0.062, 0.362] pad_end=[0.58, -0.058, 0.358] measured_pinch=[0.58, -0.06, 0.36]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.62913, 0.00341, -0.66862, -1.7853, 1.42472, 0.73071, 0.77831] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.928, 0.168, 1.678, 0.299, 0.921, 0.306, 0.782]rad min=0.168rad
     q_cmd=[-0.62923, 0.00328, -0.66862, -1.78521, 1.42469, 0.73077, 0.7784] effort_Nm=[0.5815941095352173, 0.6819600462913513, 0.06866420805454254, 0.08434353023767471, -0.011137513443827629, 0.014400454238057137, 0.039875004440546036] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0357, 0.0343]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.5, -0.047, 0.23] pad_end=[0.5, -0.112, 0.23] measured_pinch=[0.5, -0.08, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.40772, -0.14112, 1.02202, -1.51645, -0.58577, 0.15578, -1.00913] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.552]rad min=0.306rad
     q_cmd=[-0.40777, -0.14111, 1.02203, -1.51655, -0.58554, 0.15467, -1.00864] effort_Nm=[-1.3572810888290405, 1.161003828048706, 0.23737673461437225, -2.4369311332702637, 1.1652401685714722, -0.7092165946960449, -0.05891038849949837] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0958_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 17. Approach measured switch

```python
s.act(**{'intent': 'Approach measured switch', 'left': {'to': [0.586910834312439, -0.11408680737018585, 0.30295385837554933]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 969.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120251701334000_c9b788b53f1047dfbb3901d99c63afc7.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0969.jpg`
Sim seconds: 124.43333333333334

```text
[obs #969 | act=8e9e15a7 | sim=124.43s | wall= 794.4s | Approach measured switch]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, 0.0, -0.001] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-6.192264556884766, -2.2627010345458984, 4.401508331298828, 0.3003750145435333]
  L: rigid_TCP(fwd,left,up)=[0.587, -0.114, 0.304]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.587, -0.115, 0.306] pad_end=[0.587, -0.112, 0.302] measured_pinch=[0.587, -0.114, 0.304]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.72011, -0.09146, -0.77251, -1.43161, 1.26136, 0.57507, 0.53633] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[2.019, 0.073, 1.574, 0.653, 1.085, 0.462, 1.024]rad min=0.073rad
     q_cmd=[-0.7202, -0.09154, -0.77257, -1.43132, 1.26126, 0.57494, 0.53615] effort_Nm=[0.03739801049232483, 0.33507028222084045, 0.14433202147483826, -0.2931431829929352, -0.0012366659939289093, -0.01700175739824772, -0.010342872701585293] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0357, 0.0343]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.5, -0.047, 0.23] pad_end=[0.5, -0.112, 0.23] measured_pinch=[0.5, -0.08, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.40771, -0.14112, 1.02202, -1.51645, -0.58579, 0.15577, -1.00913] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.552]rad min=0.306rad
     q_cmd=[-0.40777, -0.14111, 1.02203, -1.51655, -0.58554, 0.15467, -1.00864] effort_Nm=[-1.559207797050476, 1.2543214559555054, 0.20889325439929962, -2.5727853775024414, 1.225071907043457, -0.7405958771705627, -0.04736043140292168] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0969_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 18. Press measured switch

```python
s.act(**{'intent': 'Press measured switch', 'left': {'to': [0.6011453061103821, -0.13297130846977234, 0.2780851376056671]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 6, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: no_progress; observation 990.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120270384967000_182a0954e9904d69a738be50b11fbdc9.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0990.jpg`
Sim seconds: 127.13333333333334

```text
[obs #990 | act=d166912f | sim=127.13s | wall= 813.0s | Press measured switch]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[0.001, -0.0, -0.003] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.3957672119140625, -1.7364087104797363, 3.5068929195404053, -1.0835928916931152]
  L: rigid_TCP(fwd,left,up)=[0.598, -0.141, 0.288]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm) TRACKING_ERROR(q5=-0.027)
     pad_start=[0.598, -0.143, 0.29] pad_end=[0.597, -0.14, 0.286] measured_pinch=[0.598, -0.141, 0.288]m
     close_dir=[-0.04, 0.66, -0.75] fing_dir=[0.21, -0.73, -0.65] q=[-0.81438, -0.12952, -0.84419, -1.24537, 1.29102, 0.48424, 0.42901] q_lag=[-0.0, 0.001, 0.016, 0.018, -0.027, 0.005, 0.003]rad limit_margins=[2.113, 0.035, 1.502, 0.839, 1.055, 0.553, 1.132]rad min=0.035rad
     q_cmd=[-0.81447, -0.12901, -0.82824, -1.22784, 1.26429, 0.48944, 0.43226] effort_Nm=[-15.862060546875, 38.53496551513672, 25.00006866455078, 25.001001358032227, -11.619897842407227, -11.929642677307129, 14.420421600341797] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.498, -0.08, 0.229]m fingers=[0.0357, 0.0339]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.498, -0.047, 0.229] pad_end=[0.498, -0.111, 0.229] measured_pinch=[0.498, -0.079, 0.229]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[0.57, 0.0, -0.82] q=[-0.40821, -0.14134, 1.02302, -1.51551, -0.59349, 0.15793, -1.00917] q_lag=[0.0, 0.0, -0.001, -0.001, 0.008, -0.003, 0.001]rad limit_margins=[1.707, 0.306, 1.323, 0.569, 1.753, 0.879, 0.552]rad min=0.306rad
     q_cmd=[-0.40777, -0.14111, 1.02203, -1.51655, -0.58554, 0.15467, -1.00864] effort_Nm=[13.966238975524902, 3.5297563076019287, 9.552279472351074, -16.936370849609375, 10.57901382446289, -7.4941205978393555, -8.584256172180176] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"blocked","causes":["blocked"],"confidence":"suspected","plateau":true,"normalized_error_history":[7.0835231058350665,2.728895295340944,2.6686092572988884,2.661149420063559,2.6651937318491976,2.6664441427320082],"normalized_progress":4.417078963103059,"recent_max_joint_lag_rad":[0.026981830596923828,0.026828646659851074,0.026728034019470215],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=no_progress fault=None uncertain=False pending=['left']
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_0990_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 19. Withdraw probe

```python
s.act(**{'intent': 'Withdraw probe', 'left': {'to': [0.61, -0.04, 0.36]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1007.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120284959807000_353187a876a145e8873c2455804a054a.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1007.jpg`
Sim seconds: 129.43333333333334

```text
[obs #1007 | act=a1ec5604 | sim=129.43s | wall= 827.7s | Withdraw probe]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[0.0, 0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.105821132659912, -1.5371363162994385, 2.991457462310791, -1.0998766422271729]
  L: rigid_TCP(fwd,left,up)=[0.61, -0.04, 0.359]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.61, -0.042, 0.361] pad_end=[0.61, -0.039, 0.357] measured_pinch=[0.61, -0.041, 0.359]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.73213, 0.07147, -0.65829, -1.74971, 1.54589, 0.72214, 0.78414] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.031, 0.236, 1.688, 0.335, 0.8, 0.315, 0.777]rad min=0.236rad
     q_cmd=[-0.7321, 0.07155, -0.65821, -1.7499, 1.54613, 0.72221, 0.78431] effort_Nm=[0.23113997280597687, -0.37279438972473145, -0.2641918361186981, 0.27171459794044495, 0.008285649120807648, 0.020587975159287453, 0.0063343290239572525] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0353, 0.034]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.5, -0.048, 0.23] pad_end=[0.5, -0.112, 0.23] measured_pinch=[0.5, -0.08, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.40773, -0.14112, 1.02203, -1.51645, -0.58563, 0.15612, -1.00925] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.001, 0.001]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.761, 0.881, 0.552]rad min=0.306rad
     q_cmd=[-0.40777, -0.14111, 1.02203, -1.51655, -0.58554, 0.15467, -1.00864] effort_Nm=[-1.4701098203659058, 1.2059067487716675, 0.21098801493644714, -2.5063982009887695, 1.2074124813079834, -0.7380508780479431, -0.0357893668115139] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1007_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 20. Stand in open aisle

```python
s.act(**{'intent': 'Stand in open aisle', 'left': None, 'right': None, 'base': None, 'torso': {'q': [0.84, -1.00609, -0.42, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1024.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120306999306000_81fd47774ed049c6af9c9ab59f5c326f.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1024.jpg`
Sim seconds: 131.83333333333334

```text
[obs #1024 | act=1e17cf2c | sim=131.83s | wall= 849.7s | Stand in open aisle]
  base_odom(sim): rel_xyz=[-3.795, -1.551, -0.003]m rel_yaw=+1.958rad vel=[-0.0, 0.0, 0.0] | torso=[0.841, -1.007, -0.42, 0.0] err=[-0.001, 0.001, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-99.99105834960938, -66.92790222167969, 38.364952087402344, 0.6137341260910034]
  L: rigid_TCP(fwd,left,up)=[0.689, -0.04, 1.038]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.688, -0.042, 1.04] pad_end=[0.69, -0.039, 1.036] measured_pinch=[0.689, -0.041, 1.038]m
     close_dir=[0.32, 0.68, -0.66] fing_dir=[0.52, -0.71, -0.48] q=[-0.73212, 0.07156, -0.6582, -1.74988, 1.54577, 0.72234, 0.7843] q_lag=[0.0, -0.0, -0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.031, 0.236, 1.688, 0.335, 0.8, 0.315, 0.776]rad min=0.236rad
     q_cmd=[-0.7321, 0.07155, -0.65821, -1.7499, 1.54613, 0.72221, 0.78431] effort_Nm=[1.4114010334014893, -0.8100701570510864, -0.6362074017524719, -2.4140915870666504, 0.19688056409358978, 0.07594959437847137, -0.2891976237297058] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.655, -0.08, 0.871]m fingers=[0.0353, 0.034]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.655, -0.048, 0.871] pad_end=[0.655, -0.112, 0.871] measured_pinch=[0.655, -0.08, 0.871]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[0.9, -0.0, -0.44] q=[-0.40772, -0.14113, 1.02203, -1.51641, -0.5859, 0.15619, -1.0093] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.002, 0.001]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.551]rad min=0.306rad
     q_cmd=[-0.40777, -0.14111, 1.02203, -1.51655, -0.58554, 0.15467, -1.00864] effort_Nm=[-1.3024685382843018, 2.658735990524292, 0.25968217849731445, -4.966643810272217, 2.275908946990967, -1.376359462738037, -0.12795495986938477] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1024_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 21. Overhead carry clearing divider swept volume

```python
s.act(**{'intent': 'Overhead carry clearing divider swept volume', 'left': {'q': [0, 0, 0, 0, 0, 0, 0]}, 'right': {'q': [-2.6, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 20, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1045.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120320514097000_4b22404b335947959e72f181c211095e.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1045.jpg`
Sim seconds: 135.1

```text
[obs #1045 | act=a339e07f | sim=135.10s | wall= 863.2s | Overhead carry clearing divider swept volume]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[0.001, 0.0, 0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[100.00105285644531, 78.26622009277344, -60.529624938964844, 10.921735763549805]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[0.00012, -0.0, -4e-05, -0.00016, 4e-05, -0.0, 2e-05] q_lag=[-0.0, 0.0, 0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-1.1982166767120361, 0.20036767423152924, 0.008921921253204346, -0.47149792313575745, 0.008282128721475601, -0.09149354696273804, 0.0024788775481283665] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.871, -0.241, 1.69]m fingers=[0.0354, 0.034]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.873, -0.209, 1.69] pad_end=[0.869, -0.273, 1.69] measured_pinch=[0.871, -0.241, 1.69]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59972, 0.04996, -0.13025, -0.12, 0.06483, 0.99992, -0.13965] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, -0.0]rad limit_margins=[1.841, 0.115, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[33.3402214050293, -2.591486930847168, -0.10092020034790039, 14.7975435256958, 0.3126943111419678, 3.696030855178833, -0.6967405080795288] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1045_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 22. Translate directly to clear final base location

```python
s.act(**{'intent': 'Translate directly to clear final base location', 'left': None, 'right': None, 'base': {'fwd': 0.77, 'left': 0.06}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1113.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120378584001000_361c495eeaf849b6a03ad10662dd3420.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1113.jpg`
Sim seconds: 143.8

```text
[obs #1113 | act=c45f655a | sim=143.80s | wall= 921.4s | Translate directly to clear final base location]
  base_odom(sim): rel_xyz=[-4.141, -0.862, -0.001]m rel_yaw=+1.958rad vel=[0.086, 0.007, 0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.8447747230529785, -5.47554874420166, 5.869974613189697, -0.5051916837692261]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-1e-05, 0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[0.0, -0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.0016425696667283773, 0.0022503251675516367, -8.467701263725758e-06, 0.00014409494178835303, -1.2638498446904123e-05, -6.66721462039277e-05, 1.0515270787436748e-06] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0354, 0.034]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.874, -0.209, 1.689] pad_end=[0.87, -0.273, 1.689] measured_pinch=[0.872, -0.241, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59987, 0.05003, -0.13073, -0.11975, 0.06519, 1.00017, -0.13964] q_lag=[-0.0, -0.0, 0.001, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.215, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.0482354164123535, -0.014661669731140137, 0.2474043369293213, -3.266096591949463, 0.1853404939174652, -2.0264406204223633, -0.002063363790512085] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1113_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 23. Turn overhead fax toward open tabletop

```python
s.act(**{'intent': 'Turn overhead fax toward open tabletop', 'left': None, 'right': None, 'base': {'yaw_deg': 115}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1197.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120447754329000_62a0c6fa51e14fcc875aed68c792af1c.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1197.jpg`
Sim seconds: 154.3

```text
[obs #1197 | act=b86ef6af | sim=154.30s | wall= 990.6s | Turn overhead fax toward open tabletop]
  base_odom(sim): rel_xyz=[-4.14, -0.862, -0.001]m rel_yaw=-2.337rad vel=[0.006, 0.005, 0.2] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.942298889160156, -5.556652069091797, 5.920561790466309, -0.49008989334106445]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, -0.0, -1e-05, -0.0, 0.0, -0.0] q_lag=[0.0, -0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.005004621110856533, -0.019663752987980843, -0.00022337655536830425, 0.0027584636118263006, -0.0001627392484806478, 0.00047827468370087445, -0.0005702732596546412] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0354, 0.034]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.874, -0.209, 1.689] pad_end=[0.87, -0.273, 1.689] measured_pinch=[0.872, -0.241, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59987, 0.05002, -0.13071, -0.11975, 0.06513, 1.00016, -0.13964] q_lag=[-0.0, -0.0, 0.001, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.215, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.091423988342285, 0.045560598373413086, 0.2479534149169922, -3.2828352451324463, 0.18120050430297852, -2.027771472930908, 0.002774178981781006] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1197_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 24. Lower straight arm over clear tabletop

```python
s.act(**{'intent': 'Lower straight arm over clear tabletop', 'left': None, 'right': {'q': [-1.45, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1210.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120465311115000_1e68916daec7455c8ceab54da93c77ee.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1210.jpg`
Sim seconds: 156.26666666666668

```text
[obs #1210 | act=2f89fe8e | sim=156.27s | wall=1008.0s | Lower straight arm over clear tabletop]
  base_odom(sim): rel_xyz=[-4.14, -0.862, -0.001]m rel_yaw=-2.337rad vel=[0.003, -0.001, 0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-79.01834106445312, -52.56726837158203, 58.35715866088867, 5.281210899353027]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[1e-05, 1e-05, 8e-05, -0.00016, -1e-05, 4e-05, -2e-05] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.47385868430137634, -0.375375360250473, -0.000151708722114563, -0.019025079905986786, 0.0009414488449692726, -0.029215890914201736, -0.011216243728995323] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.875, -0.241, 0.906]m fingers=[0.0354, 0.034]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.876, -0.209, 0.905] pad_end=[0.874, -0.273, 0.908] measured_pinch=[0.875, -0.241, 0.906]m
     close_dir=[0.03, 1.0, -0.05] fing_dir=[0.3, -0.06, -0.95] q=[-1.4504, 0.05001, -0.13169, -0.11767, 0.06482, 1.00029, -0.13967] q_lag=[0.0, -0.0, 0.002, -0.002, 0.0, -0.0, -0.0]rad limit_margins=[2.749, 0.114, 2.215, 0.457, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.45, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-52.61280059814453, 3.649019241333008, 0.8887901306152344, -24.9954776763916, 0.25635528564453125, -7.746547698974609, 0.45407038927078247] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1210_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 25. Set fax onto tabletop

```python
s.act(**{'intent': 'Set fax onto tabletop', 'left': None, 'right': {'q': [-1.36, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 6, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1214.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120468315137000_b9aaa2c250d2447db0ca7f847c3c9f1f.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1214.jpg`
Sim seconds: 156.76666666666668

```text
[obs #1214 | act=437fb336 | sim=156.77s | wall=1011.1s | Set fax onto tabletop]
  base_odom(sim): rel_xyz=[-4.14, -0.862, -0.001]m rel_yaw=-2.337rad vel=[-0.0, 0.0, -0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-40.05646896362305, -26.258121490478516, 22.716875076293945, 0.45383596420288086]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-1e-05, 0.0, 4e-05, -7e-05, -0.0, 2e-05, -1e-05] q_lag=[0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.9789126515388489, -0.058218829333782196, -0.003055080771446228, 0.2134951502084732, -0.002540603280067444, 0.013686977326869965, -0.002259874250739813] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.838, -0.241, 0.854]m fingers=[0.0354, 0.034]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.839, -0.209, 0.852] pad_end=[0.837, -0.273, 0.856] measured_pinch=[0.838, -0.241, 0.854]m
     close_dir=[0.02, 1.0, -0.06] fing_dir=[0.22, -0.06, -0.97] q=[-1.35989, 0.05001, -0.13111, -0.11962, 0.06462, 1.00014, -0.13966] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[2.659, 0.114, 2.215, 0.459, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-14.943525314331055, 0.5266139507293701, 0.47272729873657227, -7.397363185882568, 0.332538366317749, -2.1128427982330322, -0.20254398882389069] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1214_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 26. Release supported powered fax

```python
s.act(**{'intent': 'Release supported powered fax', 'left': None, 'right': {'grip': 1}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 4, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1218.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120471552070000_109d231db4a541689d86ecdee7164adf.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1218.jpg`
Sim seconds: 157.26666666666668

```text
[obs #1218 | act=ab8aed45 | sim=157.27s | wall=1014.3s | Release supported powered fax]
  base_odom(sim): rel_xyz=[-4.14, -0.862, -0.001]m rel_yaw=-2.337rad vel=[0.0, -0.001, -0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-0.15823237597942352, -0.06132564693689346, 0.11852923035621643, -0.06169097125530243]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.0015847731847316027, -0.15852609276771545, -0.001144631765782833, -0.00035843177465721965, -0.0007349781226366758, -0.0002905289293266833, -0.005881055258214474] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.838, -0.242, 0.854]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.839, -0.194, 0.852] pad_end=[0.837, -0.289, 0.857] measured_pinch=[0.838, -0.242, 0.854]m
     close_dir=[0.02, 1.0, -0.06] fing_dir=[0.22, -0.06, -0.97] q=[-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[2.659, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-0.042849816381931305, -0.08058945834636688, -0.0034996960312128067, -0.015203148126602173, -0.0013440290931612253, -0.0009496463462710381, 0.0011577174300327897] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1218_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 27. Withdraw right hand from fax

```python
s.act(**{'intent': 'Withdraw right hand from fax', 'left': None, 'right': {'q': [-1.65, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1223.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120475081283000_ca63f429ef8a4bab8e6c537bdd4b90b5.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1223.jpg`
Sim seconds: 157.9

```text
[obs #1223 | act=c635d46a | sim=157.90s | wall=1017.9s | Withdraw right hand from fax]
  base_odom(sim): rel_xyz=[-4.14, -0.862, -0.001]m rel_yaw=-2.337rad vel=[-0.001, -0.0, 0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[65.94801330566406, 41.90145492553711, -31.360240936279297, 2.7367615699768066]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[3e-05, -0.0, -1e-05, 4e-05, 1e-05, -1e-05, 1e-05] q_lag=[-0.0, 0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-1.7772763967514038, 0.1187274307012558, 0.0061498284339904785, -0.3716316223144531, 0.004938438534736633, -0.019179046154022217, 0.0037248136941343546] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.242, 1.035]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.942, -0.195, 1.033] pad_end=[0.938, -0.289, 1.038] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.05] fing_dir=[0.49, -0.06, -0.87] q=[-1.64948, 0.04998, -0.12905, -0.12012, 0.06607, 1.00007, -0.14] q_lag=[-0.001, 0.0, -0.001, 0.0, -0.001, -0.0, 0.0]rad limit_margins=[2.791, 0.115, 2.217, 0.459, 2.28, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[14.255290985107422, 0.8816823959350586, -0.31302309036254883, 5.491148948669434, -0.28205323219299316, 0.6548454165458679, 0.2912473976612091] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1223_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 28. Verify independent stable support

```python
s.act(**{'intent': 'Verify independent stable support', 'left': None, 'right': None, 'base': None, 'torso': None, 'seconds': 2, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1236.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120481591972000_85dd3cc10363440eb27f711d1b0a5a85.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1236.jpg`
Sim seconds: 159.9

```text
[obs #1236 | act=f64b48b1 | sim=159.90s | wall=1024.4s | Verify independent stable support]
  base_odom(sim): rel_xyz=[-4.14, -0.862, -0.001]m rel_yaw=-2.337rad vel=[-0.0, 0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, -0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-0.13777577877044678, -0.10853177309036255, 0.052341438829898834, -0.0212339386343956]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.007638884242624044, 0.03838856890797615, 0.00017986120656132698, 0.003719282103702426, 5.476085061673075e-05, 0.0008085709414444864, 0.0009752935729920864] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.242, 1.035]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.942, -0.194, 1.033] pad_end=[0.939, -0.289, 1.038] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.05] fing_dir=[0.49, -0.06, -0.87] q=[-1.65, 0.05, -0.12999, -0.12, 0.06501, 1.0, -0.14] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[2.791, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-0.0029900320805609226, 0.010775445029139519, 0.0004662795690819621, -5.5816140957176685e-05, 0.0004824351635761559, 0.0011106583988294005, -0.0008106579771265388] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a06/obs_1236_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```
