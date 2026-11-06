# a05 exact public action sequence

Historical record, not a blind replay script. Includes unsuccessful recovery motions and rejected requests; inspect images and remeasure before contacts. All arguments preserved, including max_steps.

## 1. a05 empty-hand clear aisle navigation

```python
s.act(**{'intent': 'a05 empty-hand clear aisle navigation', 'left': {'grip': 1}, 'right': {'grip': 1}, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 65.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118279337375000_33f40ace867343eeb0d6c0a348176f43.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0065.jpg`
Sim seconds: 8.0

```text
[obs #065 | act=59b77f56 | sim=  8.00s | wall=  66.6s | a05 empty-hand clear aisle navigation]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0065_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 2. a05 empty-hand clear aisle navigation

```python
s.act(**{'intent': 'a05 empty-hand clear aisle navigation', 'left': None, 'right': None, 'base': {'fwd': 1.0}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 149.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118347676605000_122eb93022b34561ab98ce2ac765dece.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0149.jpg`
Sim seconds: 18.5

```text
[obs #149 | act=7e632cfb | sim= 18.50s | wall= 135.0s | a05 empty-hand clear aisle navigation]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0149_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 3. a05 empty-hand clear aisle navigation

```python
s.act(**{'intent': 'a05 empty-hand clear aisle navigation', 'left': None, 'right': None, 'base': {'fwd': 0.8}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 217.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118404111471000_3c77c662f7434c8d97899125345cbecf.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0217.jpg`
Sim seconds: 27.0

```text
[obs #217 | act=86616296 | sim= 27.00s | wall= 191.6s | a05 empty-hand clear aisle navigation]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0217_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 4. a05 empty-hand clear aisle navigation

```python
s.act(**{'intent': 'a05 empty-hand clear aisle navigation', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 281.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118458752542000_b7375f8c23984a0d9437245ec94c001c.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0281.jpg`
Sim seconds: 35.0

```text
[obs #281 | act=debadfb7 | sim= 35.00s | wall= 246.2s | a05 empty-hand clear aisle navigation]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0281_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 5. a05 empty-hand clear aisle navigation

```python
s.act(**{'intent': 'a05 empty-hand clear aisle navigation', 'left': None, 'right': None, 'base': {'left': 0.35}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 313.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118485145618000_c10bacceed454b04a169d43705d0e3e3.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0313.jpg`
Sim seconds: 39.0

```text
[obs #313 | act=97dda0b8 | sim= 39.00s | wall= 272.5s | a05 empty-hand clear aisle navigation]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0313_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 6. a05 empty-hand clear aisle navigation

```python
s.act(**{'intent': 'a05 empty-hand clear aisle navigation', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 413.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118566772702000_5fae8c1a755a4fdcac8595e92c6b56e0.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0413.jpg`
Sim seconds: 51.5

```text
[obs #413 | act=620723ac | sim= 51.50s | wall= 354.2s | a05 empty-hand clear aisle navigation]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0413_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 7. a05 empty-hand clear aisle navigation

```python
s.act(**{'intent': 'a05 empty-hand clear aisle navigation', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 513.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118650933822000_6c878b298f2a4487811656777b55b23c.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0513.jpg`
Sim seconds: 64.0

```text
[obs #513 | act=996ec1fc | sim= 64.00s | wall= 438.4s | a05 empty-hand clear aisle navigation]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0513_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 8. a05 empty-hand clear aisle navigation

```python
s.act(**{'intent': 'a05 empty-hand clear aisle navigation', 'left': None, 'right': None, 'base': {'fwd': 1.15}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 609.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118731342869000_8220b49595494916a3160f99280e8648.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0609.jpg`
Sim seconds: 76.0

```text
[obs #609 | act=cf906956 | sim= 76.00s | wall= 518.7s | a05 empty-hand clear aisle navigation]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0609_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 9. a05 empty-hand clear aisle navigation

```python
s.act(**{'intent': 'a05 empty-hand clear aisle navigation', 'left': None, 'right': None, 'base': {'yaw_deg': -70}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 661.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118774765046000_31ff8ee342e847bab295cb50c8e0397e.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0661.jpg`
Sim seconds: 82.5

```text
[obs #661 | act=cd73abe6 | sim= 82.50s | wall= 562.0s | a05 empty-hand clear aisle navigation]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0661_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 10. Approach fax with raised empty hands

```python
s.act(**{'intent': 'Approach fax with raised empty hands', 'left': {'q': [-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232]}, 'right': {'q': [-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466]}, 'base': {'fwd': 0.78}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 771.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118877004555000_8db6cd42ac0e4475bc6b3e237e8fb247.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0771.jpg`
Sim seconds: 96.83333333333333

```text
[obs #771 | act=b65a6b77 | sim= 96.83s | wall= 664.4s | Approach fax with raised empty hands]
  base_odom(sim): rel_xyz=[-3.795, -1.551, -0.003]m rel_yaw=+1.958rad vel=[0.011, -0.002, 0.001] | torso=[1.025, -1.45, -0.47, 0.0] err=[0.0, 0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.025, -1.45, -0.47, -0.0] effort_Nm=[0.026168785989284515, -0.021443387493491173, 0.006469354033470154, 0.00085429847240448]
  L: rigid_TCP(fwd,left,up)=[0.45, 0.28, 0.75]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.45, 0.327, 0.75] pad_end=[0.45, 0.232, 0.75] measured_pinch=[0.45, 0.28, 0.75]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.04, -0.0, -1.0] q=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, -0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[0.0022809146903455257, 0.010084068402647972, 0.0014421835076063871, 0.002350819995626807, 0.0005109705380164087, 7.474645099136978e-05, -9.032151865540072e-05] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.505, -0.27, 0.649]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.505, -0.223, 0.649] pad_end=[0.504, -0.318, 0.649] measured_pinch=[0.505, -0.27, 0.649]m
     close_dir=[0.01, 1.0, -0.0] fing_dir=[-0.03, -0.0, -1.0] q=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51885, 1.036, -0.79466] q_lag=[-0.0, -0.0, -0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[0.002779837930575013, 0.005396322812885046, 0.0004155010683462024, -0.0004175933136139065, 0.00020103513088542968, -3.4724613215075806e-05, -0.00016228764434345067] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0771_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 11. Deep floor crouch

```python
s.act(**{'intent': 'Deep floor crouch', 'left': None, 'right': None, 'base': None, 'torso': {'q': [1.68, -2.54, -1.62, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 787.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118886802440000_54486c182def46779ca3dbb1353c432a.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0787.jpg`
Sim seconds: 99.23333333333333

```text
[obs #787 | act=6078b95d | sim= 99.23s | wall= 674.3s | Deep floor crouch]
  base_odom(sim): rel_xyz=[-3.795, -1.55, -0.003]m rel_yaw=+1.958rad vel=[0.0, -0.0, 0.001] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, -0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-8.252994537353516, 1.8478305339813232, 5.439462661743164, 0.1557210087776184]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.278, 0.327, 0.235] pad_end=[0.278, 0.232, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.4119, 0.60027, -0.73518, -1.60059, 2.24215, 0.96342, 1.52232] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, -0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[-0.7037792205810547, 0.42123904824256897, 0.35276085138320923, -0.5249694585800171, 0.001711726188659668, 0.0004184143617749214, -0.007571044843643904] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.253, -0.27, 0.123]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.253, -0.223, 0.123] pad_end=[0.252, -0.318, 0.124] measured_pinch=[0.253, -0.27, 0.123]m
     close_dir=[0.01, 1.0, -0.01] fing_dir=[-0.68, 0.0, -0.73] q=[-0.52689, -0.35921, 0.79381, -0.97008, -1.51893, 1.03598, -0.79466] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0]rad limit_margins=[1.826, 0.524, 1.552, 1.114, 0.827, 0.001, 0.766]rad min=0.001rad
     q_cmd=[-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466] effort_Nm=[-1.033282995223999, -0.30212149024009705, -0.2907494604587555, -0.45859766006469727, 0.01845984160900116, -0.016874372959136963, -0.013026723638176918] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0787_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 12. Align downward open fingers above measured fax

```python
s.act(**{'intent': 'Align downward open fingers above measured fax', 'left': None, 'right': {'to': [0.61, -0.32, 0.15], 'finger_dir': [0, 0, -1], 'close_dir': [0, 1, 0]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 837.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118919049716000_26ec836be5b246bd9904d1235d324639.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0837.jpg`
Sim seconds: 106.26666666666667

```text
[obs #837 | act=8a99da05 | sim=106.27s | wall= 706.5s | Align downward open fingers above measured fax]
  base_odom(sim): rel_xyz=[-3.795, -1.55, -0.003]m rel_yaw=+1.958rad vel=[0.0, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[0.1289139986038208, -0.015016421675682068, -0.3036050498485565, -0.38719189167022705]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.278, 0.327, 0.235] pad_end=[0.278, 0.232, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.41197, 0.60027, -0.7352, -1.60057, 2.24216, 0.96342, 1.52232] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[-0.01698380708694458, -0.013769310899078846, -0.002358430065214634, 0.003318337956443429, 2.6500842068344355e-05, 4.6468223445117474e-05, -0.0003722559195011854] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.61, -0.32, 0.15]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.61, -0.273, 0.15] pad_end=[0.61, -0.368, 0.15] measured_pinch=[0.61, -0.32, 0.15]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-0.93538, -0.50537, 0.7673, -1.09542, -1.23758, 0.85127, -0.50449] q_lag=[-0.0, 0.0, 0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[2.234, 0.67, 1.579, 0.989, 1.109, 0.186, 1.056]rad min=0.186rad
     q_cmd=[-0.93545, -0.50534, 0.76733, -1.09532, -1.23767, 0.85129, -0.50443] effort_Nm=[0.5963797569274902, 0.0072495099157094955, 0.16443414986133575, 0.06522662937641144, -0.019118208438158035, 0.03405861556529999, 0.008478675037622452] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0837_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 13. Lower open fingers around casing

```python
s.act(**{'intent': 'Lower open fingers around casing', 'left': None, 'right': {'to': [0.61, -0.32, 0.035]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: no_progress; observation 867.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118941146344000_052ae121136c432186964ed8e9d03d0c.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0867.jpg`
Sim seconds: 110.2

```text
[obs #867 | act=0d97dc06 | sim=110.20s | wall= 728.5s | Lower open fingers around casing]
  base_odom(sim): rel_xyz=[-3.795, -1.55, -0.003]m rel_yaw=+1.958rad vel=[0.0, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[0.0, -0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-0.046010278165340424, -0.060970500111579895, 0.007746674120426178, -0.1619328260421753]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.278, 0.327, 0.235] pad_end=[0.278, 0.232, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] q_lag=[0.0, 0.0, 0.0, -0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[0.0031590955331921577, 0.0001242409780388698, -0.0010714245727285743, -0.0005622796015813947, 0.00030515456455759704, 5.734308797400445e-05, -0.00015727007121313363] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.602, -0.318, 0.053]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.602, -0.271, 0.053] pad_end=[0.602, -0.365, 0.053] measured_pinch=[0.602, -0.318, 0.053]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17843, -0.12875, 1.02494, -0.03335, -0.98062, 0.4317, 0.10983] q_lag=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.477, 0.293, 1.321, 0.372, 1.366, 0.605, 1.451]rad min=0.293rad
     q_cmd=[-1.17846, -0.1287, 1.02495, -0.03324, -0.98061, 0.43166, 0.10989] effort_Nm=[0.066172756254673, -0.1328919678926468, 0.0007479526102542877, 0.021651389077305794, 0.0006661256775259972, 8.700644684722647e-05, -0.0018304322147741914] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"IK_stalled","causes":["IK_stalled"],"confidence":"limited","plateau":true,"normalized_error_history":[23.07368275354528,13.347642530632841,5.3151746159482585,3.904095599766144,3.904735223820113,3.9046589633337576,3.904776281167889],"normalized_progress":19.168906472377394,"recent_max_joint_lag_rad":[0.0001150183379650116,0.00011500343680381775,0.00011512264609336853],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"}}
  status=no_progress fault=None uncertain=False pending=['right']
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0867_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 14. Close at casing height and ready left probe

```python
s.act(**{'intent': 'Close at casing height and ready left probe', 'left': {'grip': 0}, 'right': {'q': [-1.17843, -0.12875, 1.02494, -0.03335, -0.98062, 0.4317, 0.10983], 'grip': 0}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 4, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 875.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118958149889000_6729730d50aa404a9c268f98e45f105a.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0875.jpg`
Sim seconds: 111.2

```text
[obs #875 | act=a8fe28fc | sim=111.20s | wall= 745.5s | Close at casing height and ready left probe]
  base_odom(sim): rel_xyz=[-3.795, -1.55, -0.003]m rel_yaw=+1.958rad vel=[0.0, 0.001, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[33.593387603759766, 12.69326114654541, -22.977705001831055, 18.97616958618164]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.278, 0.277, 0.235] pad_end=[0.278, 0.282, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.41189, 0.60029, -0.73512, -1.60062, 2.24214, 0.96342, 1.52232] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[0.01296071708202362, 0.005488443188369274, -0.004419303964823484, 0.012169940397143364, 0.0011948004830628633, 0.00016939666238613427, -0.0004348561051301658] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.602, -0.318, 0.053]m fingers=[0.0356, 0.0346]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.602, -0.285, 0.053] pad_end=[0.602, -0.35, 0.053] measured_pinch=[0.602, -0.318, 0.053]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17844, -0.12883, 1.02446, -0.03309, -0.97861, 0.43162, 0.10934] q_lag=[0.0, 0.0, 0.0, -0.0, -0.002, 0.0, 0.0]rad limit_margins=[2.477, 0.293, 1.322, 0.372, 1.368, 0.606, 1.451]rad min=0.293rad
     q_cmd=[-1.17843, -0.12875, 1.02494, -0.03335, -0.98062, 0.4317, 0.10983] effort_Nm=[5.305816173553467, 8.789335250854492, 0.3104362487792969, -2.9998717308044434, 0.19795942306518555, -2.2139337062835693, 0.7363280057907104] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0875_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 15. Lift retained fax

```python
s.act(**{'intent': 'Lift retained fax', 'left': None, 'right': {'to': [0.602, -0.318, 0.2]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 12, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 898.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792118972896953000_87defcddb3e94842a2511cd288ca2668.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0898.jpg`
Sim seconds: 114.36666666666666

```text
[obs #898 | act=116d508d | sim=114.37s | wall= 760.3s | Lift retained fax]
  base_odom(sim): rel_xyz=[-3.795, -1.55, -0.003]m rel_yaw=+1.958rad vel=[-0.001, 0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-2.3982412815093994, -1.1116198301315308, 1.888051986694336, -2.520848512649536]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.278, 0.277, 0.235] pad_end=[0.278, 0.282, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.41198, 0.60026, -0.73521, -1.60057, 2.24216, 0.96342, 1.52232] q_lag=[0.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[-0.05776450037956238, -0.04005599766969681, -0.002244845498353243, 0.039243392646312714, -0.0005779708735644817, -2.1106097847223282e-05, -0.002313025761395693] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.602, -0.318, 0.199]m fingers=[0.0356, 0.0344]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.602, -0.286, 0.199] pad_end=[0.602, -0.351, 0.199] measured_pinch=[0.602, -0.318, 0.199]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-0.8463, -0.57342, 0.65309, -1.37425, -1.4129, 0.957, -0.75441] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.001]rad limit_margins=[2.145, 0.738, 1.693, 0.71, 0.933, 0.08, 0.806]rad min=0.08rad
     q_cmd=[-0.8463, -0.57343, 0.65294, -1.37445, -1.41312, 0.95683, -0.75491] effort_Nm=[-0.8646779656410217, -1.253416657447815, -0.7864357233047485, -0.6482401490211487, 0.24466179311275482, -0.054218754172325134, -0.2892903983592987] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0898_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 16. Tilt fax and angle left fingers toward switch

```python
s.act(**{'intent': 'Tilt fax and angle left fingers toward switch', 'left': {'to': [0.58, -0.06, 0.36], 'finger_dir': [0.220337, -0.708506, -0.670426], 'close_dir': [-0.038811, 0.680406, -0.731807]}, 'right': {'to': [0.5, -0.08, 0.23], 'pitch_deg': 35}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 962.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119017102091000_14b3f9c1d3dc4eb69e1db69119d9d809.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0962.jpg`
Sim seconds: 123.43333333333334

```text
[obs #962 | act=fe325759 | sim=123.43s | wall= 804.4s | Tilt fax and angle left fingers toward switch]
  base_odom(sim): rel_xyz=[-3.795, -1.55, -0.003]m rel_yaw=+1.958rad vel=[0.0, -0.001, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.884592056274414, -2.209803819656372, 3.2803397178649902, -0.05362206697463989]
  L: rigid_TCP(fwd,left,up)=[0.58, -0.06, 0.36]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.58, -0.062, 0.362] pad_end=[0.58, -0.058, 0.358] measured_pinch=[0.58, -0.06, 0.36]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.62911, 0.00339, -0.66859, -1.7853, 1.4247, 0.73073, 0.7783] q_lag=[-0.0, -0.0, 0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.928, 0.168, 1.678, 0.299, 0.921, 0.306, 0.782]rad min=0.168rad
     q_cmd=[-0.62921, 0.00327, -0.66859, -1.78521, 1.42467, 0.7308, 0.7784] effort_Nm=[0.5974270105361938, 0.6912058591842651, 0.06390208005905151, 0.07765716314315796, -0.009653471410274506, 0.015660807490348816, 0.03870350494980812] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0356, 0.0344]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.5, -0.047, 0.23] pad_end=[0.5, -0.112, 0.23] measured_pinch=[0.5, -0.08, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.40769, -0.14111, 1.022, -1.51645, -0.58575, 0.15578, -1.00909] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.552]rad min=0.306rad
     q_cmd=[-0.40774, -0.1411, 1.022, -1.51655, -0.5855, 0.15469, -1.00861] effort_Nm=[-1.1743810176849365, 0.8749206066131592, 0.07952253520488739, -2.2524967193603516, 1.111724853515625, -0.7030434608459473, -0.1406504511833191] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0962_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 17. Approach measured switch

```python
s.act(**{'intent': 'Approach measured switch', 'left': {'to': [0.5868675017356872, -0.11438874959945679, 0.3026577723026276]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 973.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119169810028000_24cf5568640b47648d12e708546d4c9d.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0973.jpg`
Sim seconds: 124.96666666666667

```text
[obs #973 | act=8060c310 | sim=124.97s | wall= 957.0s | Approach measured switch]
  base_odom(sim): rel_xyz=[-3.795, -1.55, -0.003]m rel_yaw=+1.958rad vel=[0.0, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-6.147683143615723, -2.3893542289733887, 4.470560550689697, 0.614024817943573]
  L: rigid_TCP(fwd,left,up)=[0.587, -0.114, 0.304]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.587, -0.116, 0.306] pad_end=[0.587, -0.112, 0.302] measured_pinch=[0.587, -0.114, 0.304]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.72048, -0.09205, -0.77309, -1.42967, 1.26063, 0.57408, 0.53514] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[2.019, 0.072, 1.573, 0.655, 1.086, 0.463, 1.026]rad min=0.072rad
     q_cmd=[-0.72057, -0.09214, -0.77316, -1.42937, 1.26053, 0.57394, 0.53495] effort_Nm=[0.03788778558373451, 0.35181328654289246, 0.1452750861644745, -0.2857851982116699, -0.0014897510409355164, -0.01704934611916542, -0.010304451920092106] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0356, 0.0344]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.5, -0.047, 0.23] pad_end=[0.5, -0.112, 0.23] measured_pinch=[0.5, -0.08, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.40769, -0.14111, 1.02198, -1.51644, -0.58579, 0.15572, -1.00906] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.552]rad min=0.306rad
     q_cmd=[-0.40774, -0.1411, 1.022, -1.51655, -0.5855, 0.15469, -1.00861] effort_Nm=[-1.7449517250061035, 1.5476617813110352, 0.36857375502586365, -2.7748141288757324, 1.2669570446014404, -0.728532075881958, 0.06497631222009659] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0973_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 18. Press measured switch

```python
s.act(**{'intent': 'Press measured switch', 'left': {'to': [0.6010634093284607, -0.13338979268074036, 0.2776792895793915]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 6, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: no_progress; observation 991.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119185806427000_92898169f52b4a948e365d37eb69de0e.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0991.jpg`
Sim seconds: 127.16666666666667

```text
[obs #991 | act=874aca08 | sim=127.17s | wall= 973.1s | Press measured switch]
  base_odom(sim): rel_xyz=[-3.795, -1.55, -0.003]m rel_yaw=+1.958rad vel=[0.002, -0.001, -0.002] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.149656295776367, -1.8997938632965088, 3.966398239135742, -0.16250112652778625]
  L: rigid_TCP(fwd,left,up)=[0.598, -0.142, 0.288]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm) TRACKING_ERROR(q4=+0.019,q5=-0.027)
     pad_start=[0.598, -0.144, 0.29] pad_end=[0.598, -0.14, 0.286] measured_pinch=[0.598, -0.142, 0.288]m
     close_dir=[-0.04, 0.66, -0.75] fing_dir=[0.22, -0.73, -0.65] q=[-0.81461, -0.13077, -0.84347, -1.24396, 1.28941, 0.4834, 0.42718] q_lag=[-0.0, 0.001, 0.015, 0.019, -0.027, 0.005, 0.003]rad limit_margins=[2.114, 0.034, 1.503, 0.84, 1.057, 0.554, 1.134]rad min=0.034rad
     q_cmd=[-0.8147, -0.13026, -0.82838, -1.22493, 1.26284, 0.48851, 0.43041] effort_Nm=[-15.802607536315918, 38.5746955871582, 25.000076293945312, 24.998756408691406, -11.521337509155273, -11.913366317749023, 14.292470932006836] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.498, -0.08, 0.229]m fingers=[0.0357, 0.0341]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.498, -0.047, 0.229] pad_end=[0.498, -0.112, 0.229] measured_pinch=[0.498, -0.079, 0.229]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[0.57, 0.0, -0.82] q=[-0.4082, -0.14134, 1.02294, -1.51551, -0.59342, 0.15786, -1.00911] q_lag=[0.0, 0.0, -0.001, -0.001, 0.008, -0.003, 0.001]rad limit_margins=[1.707, 0.306, 1.323, 0.569, 1.753, 0.879, 0.552]rad min=0.306rad
     q_cmd=[-0.40774, -0.1411, 1.022, -1.51655, -0.5855, 0.15469, -1.00861] effort_Nm=[13.791036605834961, 4.326841354370117, 10.01738166809082, -17.268648147583008, 10.57625675201416, -7.503974437713623, -8.257587432861328] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"blocked","causes":["blocked"],"confidence":"suspected","plateau":true,"normalized_error_history":[7.109829872984638,2.7846260662463163,2.7399906612470186,2.72208204364135,2.7278420391724416],"normalized_progress":4.381987833812197,"recent_max_joint_lag_rad":[0.027121782302856445,0.026790142059326172,0.026564598083496094],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=no_progress fault=None uncertain=False pending=['left']
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_0991_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 19. Withdraw probe

```python
s.act(**{'intent': 'Withdraw probe', 'left': {'to': [0.61, -0.04, 0.36]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1008.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119198391275000_e73469109ecc4acc8c228a9e3f540994.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1008.jpg`
Sim seconds: 129.5

```text
[obs #1008 | act=e49a4297 | sim=129.50s | wall= 985.7s | Withdraw probe]
  base_odom(sim): rel_xyz=[-3.795, -1.55, -0.003]m rel_yaw=+1.958rad vel=[0.0, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.266277313232422, -1.105381727218628, 3.179641008377075, -0.6157727241516113]
  L: rigid_TCP(fwd,left,up)=[0.61, -0.04, 0.359]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.61, -0.042, 0.361] pad_end=[0.61, -0.039, 0.357] measured_pinch=[0.61, -0.041, 0.359]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.7318, 0.07104, -0.65772, -1.74966, 1.5454, 0.72277, 0.78404] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.031, 0.236, 1.688, 0.335, 0.801, 0.314, 0.777]rad min=0.236rad
     q_cmd=[-0.73178, 0.07112, -0.65764, -1.74984, 1.54563, 0.72284, 0.7842] effort_Nm=[0.1474398970603943, -0.3532421588897705, -0.22597727179527283, 0.24696040153503418, 0.005290701985359192, 0.017279408872127533, 0.0073245977982878685] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0352, 0.0342]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.5, -0.048, 0.23] pad_end=[0.5, -0.112, 0.23] measured_pinch=[0.5, -0.08, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.40771, -0.14111, 1.02201, -1.51646, -0.58556, 0.1562, -1.00927] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.002, 0.001]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.761, 0.881, 0.552]rad min=0.306rad
     q_cmd=[-0.40774, -0.1411, 1.022, -1.51655, -0.5855, 0.15469, -1.00861] effort_Nm=[-1.6484729051589966, 1.5178759098052979, 0.3557719886302948, -2.6835312843322754, 1.227455973625183, -0.72327721118927, 0.02909158542752266] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1008_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 20. Stand in open aisle

```python
s.act(**{'intent': 'Stand in open aisle', 'left': None, 'right': None, 'base': None, 'torso': {'q': [0.84, -1.00609, -0.42, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1024.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119217305615000_2216f6b7540747729b30df20f5c5d316.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1024.jpg`
Sim seconds: 131.9

```text
[obs #1024 | act=0fc7ef2b | sim=131.90s | wall=1004.6s | Stand in open aisle]
  base_odom(sim): rel_xyz=[-3.795, -1.55, -0.003]m rel_yaw=+1.958rad vel=[-0.0, -0.0, 0.0] | torso=[0.841, -1.007, -0.42, 0.0] err=[-0.001, 0.001, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-99.99113464355469, -66.83777618408203, 38.22779083251953, 0.08248567581176758]
  L: rigid_TCP(fwd,left,up)=[0.689, -0.04, 1.038]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.688, -0.042, 1.04] pad_end=[0.69, -0.039, 1.036] measured_pinch=[0.689, -0.041, 1.038]m
     close_dir=[0.32, 0.68, -0.66] fing_dir=[0.52, -0.71, -0.48] q=[-0.73179, 0.07113, -0.65763, -1.74982, 1.54527, 0.72296, 0.7842] q_lag=[0.0, -0.0, -0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.031, 0.236, 1.689, 0.335, 0.801, 0.314, 0.777]rad min=0.236rad
     q_cmd=[-0.73178, 0.07112, -0.65764, -1.74984, 1.54563, 0.72284, 0.7842] effort_Nm=[1.377037525177002, -0.9063787460327148, -0.6534267663955688, -2.409637212753296, 0.1957959681749344, 0.07476112246513367, -0.2897183299064636] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.655, -0.08, 0.871]m fingers=[0.0353, 0.0342]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.655, -0.048, 0.871] pad_end=[0.655, -0.112, 0.871] measured_pinch=[0.655, -0.08, 0.871]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[0.9, -0.0, -0.44] q=[-0.4077, -0.14111, 1.02201, -1.5164, -0.58583, 0.15632, -1.00937] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.002, 0.001]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.551]rad min=0.306rad
     q_cmd=[-0.40774, -0.1411, 1.022, -1.51655, -0.5855, 0.15469, -1.00861] effort_Nm=[-1.1265652179718018, 2.2447450160980225, 0.09926557540893555, -4.794608116149902, 2.2863101959228516, -1.3790969848632812, -0.21709907054901123] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1024_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 21. Overhead carry clearing divider swept volume

```python
s.act(**{'intent': 'Overhead carry clearing divider swept volume', 'left': {'q': [0, 0, 0, 0, 0, 0, 0]}, 'right': {'q': [-2.6, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 20, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1046.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119231775390000_2396e91de7104e82a90a46799fb5cdce.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1046.jpg`
Sim seconds: 135.16666666666666

```text
[obs #1046 | act=2d4814a2 | sim=135.17s | wall=1019.1s | Overhead carry clearing divider swept volume]
  base_odom(sim): rel_xyz=[-3.795, -1.55, -0.003]m rel_yaw=+1.958rad vel=[-0.001, -0.0, -0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[100.0010986328125, 78.34188079833984, -60.55457305908203, 11.017065048217773]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[0.00012, -0.0, -4e-05, -0.00017, 4e-05, -0.0, 2e-05] q_lag=[-0.0, 0.0, 0.0, 0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-1.2080957889556885, 0.24648571014404297, 0.00929531455039978, -0.4797014594078064, 0.008449144661426544, -0.09325266629457474, 0.002525638323277235] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.871, -0.241, 1.69]m fingers=[0.0354, 0.0342]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.873, -0.209, 1.69] pad_end=[0.869, -0.273, 1.69] measured_pinch=[0.871, -0.241, 1.69]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59972, 0.04996, -0.13021, -0.12, 0.06488, 0.99992, -0.13967] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, 0.0, -0.0]rad limit_margins=[1.841, 0.115, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[33.42755889892578, -2.474069118499756, -0.10924053192138672, 14.871807098388672, 0.2994215488433838, 3.713963747024536, -0.6736572980880737] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1046_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 22. Translate directly to clear final base location

```python
s.act(**{'intent': 'Translate directly to clear final base location', 'left': None, 'right': None, 'base': {'fwd': 0.77, 'left': 0.06}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1110.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119286080530000_7947d731611145ecb561150c017a292b.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1110.jpg`
Sim seconds: 143.16666666666666

```text
[obs #1110 | act=32882159 | sim=143.17s | wall=1073.4s | Translate directly to clear final base location]
  base_odom(sim): rel_xyz=[-4.141, -0.861, -0.001]m rel_yaw=+1.958rad vel=[0.084, 0.007, 0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.487621307373047, -5.229884624481201, 5.712993621826172, -0.44030606746673584]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-1e-05, 0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[0.0, -0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.021685365587472916, 0.031479157507419586, -2.8362497687339783e-05, -0.007409277372062206, -2.8362032026052475e-05, -0.0009877269621938467, 0.0007613816414959729] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0354, 0.0342]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.874, -0.209, 1.689] pad_end=[0.87, -0.273, 1.689] measured_pinch=[0.872, -0.241, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59987, 0.05003, -0.13068, -0.11974, 0.06524, 1.00018, -0.13968] q_lag=[-0.0, -0.0, 0.001, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.0234503746032715, 0.03054976463317871, 0.23744350671768188, -3.2430431842803955, 0.1734037697315216, -2.0309982299804688, 0.009627088904380798] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1110_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 23. Turn overhead fax toward open tabletop

```python
s.act(**{'intent': 'Turn overhead fax toward open tabletop', 'left': None, 'right': None, 'base': {'yaw_deg': 115}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1194.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119358979343000_760366c188114a1f823530142b6e9745.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1194.jpg`
Sim seconds: 153.66666666666666

```text
[obs #1194 | act=0a3e7b7c | sim=153.67s | wall=1146.4s | Turn overhead fax toward open tabletop]
  base_odom(sim): rel_xyz=[-4.141, -0.861, -0.001]m rel_yaw=-2.336rad vel=[0.005, 0.004, 0.2] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.960904121398926, -5.6720685958862305, 5.895320415496826, -0.4275383949279785]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, -0.0, -1e-05, -0.0, 0.0, -0.0] q_lag=[0.0, -0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.01917172782123089, 0.011687366291880608, -9.932112880051136e-05, 0.00492685055360198, -0.00012057952699251473, 0.0006214517634361982, 0.00011846546840388328] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0354, 0.0342]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.874, -0.209, 1.689] pad_end=[0.87, -0.273, 1.689] measured_pinch=[0.872, -0.241, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59987, 0.05003, -0.13067, -0.11975, 0.0652, 1.00017, -0.13968] q_lag=[-0.0, -0.0, 0.001, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.057159423828125, 0.11841320991516113, 0.24318742752075195, -3.2902283668518066, 0.1740022897720337, -2.0190353393554688, 0.008283376693725586] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1194_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 24. Lower straight arm over clear tabletop

```python
s.act(**{'intent': 'Lower straight arm over clear tabletop', 'left': None, 'right': {'q': [-1.45, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1206.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119379006334000_cf9679ec3cf34f95987a2e1566dd0486.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1206.jpg`
Sim seconds: 155.63333333333333

```text
[obs #1206 | act=3f34111e | sim=155.63s | wall=1166.4s | Lower straight arm over clear tabletop]
  base_odom(sim): rel_xyz=[-4.141, -0.861, -0.001]m rel_yaw=-2.336rad vel=[0.003, 0.0, 0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-78.6269302368164, -52.47562026977539, 58.251956939697266, 5.135997772216797]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[1e-05, 1e-05, 8e-05, -0.00016, -1e-05, 4e-05, -2e-05] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.42267096042633057, -0.30125242471694946, 0.0001519918441772461, -0.031546931713819504, 0.0010009026154875755, -0.029674680903553963, -0.010283049196004868] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.875, -0.241, 0.906]m fingers=[0.0354, 0.0342]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.876, -0.209, 0.905] pad_end=[0.874, -0.273, 0.908] measured_pinch=[0.875, -0.241, 0.906]m
     close_dir=[0.03, 1.0, -0.05] fing_dir=[0.3, -0.06, -0.95] q=[-1.4504, 0.05001, -0.13165, -0.11767, 0.0649, 1.0003, -0.13971] q_lag=[0.0, -0.0, 0.002, -0.002, 0.0, -0.0, -0.0]rad limit_margins=[2.749, 0.114, 2.215, 0.457, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.45, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-52.60322570800781, 3.6033620834350586, 0.8805942535400391, -24.99555778503418, 0.2532615661621094, -7.735464572906494, 0.4484498202800751] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1206_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 25. Set fax onto tabletop

```python
s.act(**{'intent': 'Set fax onto tabletop', 'left': None, 'right': {'q': [-1.36, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 6, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1210.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119382347545000_f679ec02e60a453485b983ed48eb0eb8.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1210.jpg`
Sim seconds: 156.13333333333333

```text
[obs #1210 | act=38c98844 | sim=156.13s | wall=1169.8s | Set fax onto tabletop]
  base_odom(sim): rel_xyz=[-4.141, -0.861, -0.001]m rel_yaw=-2.336rad vel=[0.001, -0.0, -0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-40.20528793334961, -26.196746826171875, 22.61332130432129, 0.37412023544311523]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-1e-05, 0.0, 4e-05, -7e-05, -0.0, 2e-05, -1e-05] q_lag=[0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.9960101842880249, -0.16339682042598724, -0.0037267059087753296, 0.2181752771139145, -0.0028925836086273193, 0.013644227758049965, -0.0050555625930428505] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.838, -0.241, 0.854]m fingers=[0.0354, 0.0342]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.839, -0.209, 0.852] pad_end=[0.837, -0.273, 0.856] measured_pinch=[0.838, -0.241, 0.854]m
     close_dir=[0.02, 1.0, -0.06] fing_dir=[0.22, -0.06, -0.97] q=[-1.35989, 0.05002, -0.13107, -0.11962, 0.06476, 1.00016, -0.1397] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[2.659, 0.114, 2.215, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-14.856911659240723, 0.49523353576660156, 0.46950721740722656, -7.3769731521606445, 0.32570862770080566, -2.0903563499450684, -0.18931137025356293] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1210_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 26. Release supported powered fax

```python
s.act(**{'intent': 'Release supported powered fax', 'left': None, 'right': {'grip': 1}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 4, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1214.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119385942126000_1d2d75162de4432bb2eb53b8a5f37c9e.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1214.jpg`
Sim seconds: 156.63333333333333

```text
[obs #1214 | act=33318c93 | sim=156.63s | wall=1173.3s | Release supported powered fax]
  base_odom(sim): rel_xyz=[-4.141, -0.861, -0.001]m rel_yaw=-2.336rad vel=[0.0, 0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, 0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-0.269180029630661, -0.14653831720352173, 0.06477944552898407, 0.1243797168135643]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.0, 0.0, -0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[-0.0, -0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.02124703675508499, 0.03698405623435974, 0.0005796157638542354, 0.006145585794001818, 0.00048525206511840224, 0.0007063972298055887, 0.0022025012876838446] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.838, -0.242, 0.854]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.839, -0.194, 0.852] pad_end=[0.837, -0.289, 0.857] measured_pinch=[0.838, -0.242, 0.854]m
     close_dir=[0.02, 1.0, -0.06] fing_dir=[0.22, -0.06, -0.97] q=[-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, 0.0]rad limit_margins=[2.659, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[0.004056014120578766, 0.09205588698387146, 0.003320852294564247, 0.004298773594200611, -0.0006049755611456931, -0.00045435770880430937, 0.0017236139392480254] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1214_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 27. Withdraw right hand from fax

```python
s.act(**{'intent': 'Withdraw right hand from fax', 'left': None, 'right': {'q': [-1.65, 0.05, -0.13, -0.12, 0.065, 1, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1219.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119389890295000_a518e18e23e5492c841421708a36829f.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1219.jpg`
Sim seconds: 157.26666666666668

```text
[obs #1219 | act=34c832cd | sim=157.27s | wall=1177.2s | Withdraw right hand from fax]
  base_odom(sim): rel_xyz=[-4.141, -0.861, -0.001]m rel_yaw=-2.336rad vel=[-0.001, -0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[65.30946350097656, 41.63106918334961, -31.300861358642578, 2.7253823280334473]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[3e-05, -0.0, -1e-05, 4e-05, 0.0, -1e-05, 1e-05] q_lag=[-0.0, 0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-1.7548820972442627, 0.3632153570652008, 0.007143586874008179, -0.37238749861717224, 0.005500409752130508, -0.020603038370609283, 0.012296861037611961] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.242, 1.035]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.942, -0.195, 1.033] pad_end=[0.938, -0.289, 1.038] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.05] fing_dir=[0.49, -0.06, -0.87] q=[-1.64948, 0.04998, -0.12906, -0.12012, 0.06606, 1.00007, -0.14] q_lag=[-0.001, 0.0, -0.001, 0.0, -0.001, -0.0, 0.0]rad limit_margins=[2.791, 0.115, 2.217, 0.459, 2.28, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[14.355863571166992, 0.8790478706359863, -0.30840539932250977, 5.529986381530762, -0.27399635314941406, 0.6630873084068298, 0.2806708514690399] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1219_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 28. Verify independent stable support

```python
s.act(**{'intent': 'Verify independent stable support', 'left': None, 'right': None, 'base': None, 'torso': None, 'seconds': 2, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1232.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/receipt_01792119408919151000_15cdc0695e4444928abdc485e5dafbfa.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1232.jpg`
Sim seconds: 159.26666666666668

```text
[obs #1232 | act=2cd581c5 | sim=159.27s | wall=1196.3s | Verify independent stable support]
  base_odom(sim): rel_xyz=[-4.141, -0.861, -0.001]m rel_yaw=-2.336rad vel=[-0.0, -0.001, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-0.002629470080137253, 0.03268700838088989, -0.005937587469816208, 0.025431618094444275]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.0014159019337967038, -0.004432620480656624, 9.802647400647402e-05, 0.00016488568508066237, 0.00011329830158501863, -0.00011765476665459573, 0.0002354790922254324] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.242, 1.035]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.942, -0.194, 1.033] pad_end=[0.939, -0.289, 1.038] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.05] fing_dir=[0.49, -0.06, -0.87] q=[-1.65, 0.05, -0.12998, -0.12, 0.06502, 1.0, -0.14] q_lag=[-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, 0.0]rad limit_margins=[2.791, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-0.002025080379098654, 0.010451911948621273, 0.0001398415770381689, 5.746237002313137e-05, -0.000496524095069617, -0.00042259381734766066, 0.0007912436267361045] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a05/obs_1232_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```
