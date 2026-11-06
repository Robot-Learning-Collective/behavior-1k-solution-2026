# a04 exact public action sequence

Historical record, not a blind replay script. Includes unsuccessful recovery motions and rejected requests; inspect images and remeasure before contacts. All arguments preserved, including max_steps.

## 1. a04 verified empty-hand aisle approach

```python
s.act(**{'intent': 'a04 verified empty-hand aisle approach', 'left': {'grip': 1}, 'right': {'grip': 1}, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 65.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117033876585000_ba9b2d9061684b1a8366ef8610dab465.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0065.jpg`
Sim seconds: 8.0

```text
[obs #065 | act=e559b74a | sim=  8.00s | wall=  59.3s | a04 verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0065_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 2. a04 verified empty-hand aisle approach

```python
s.act(**{'intent': 'a04 verified empty-hand aisle approach', 'left': None, 'right': None, 'base': {'fwd': 1.0}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 149.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117103676900000_11e5d21c521d4fd9917a1bb5cb7e6f27.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0149.jpg`
Sim seconds: 18.5

```text
[obs #149 | act=2ef7877c | sim= 18.50s | wall= 129.1s | a04 verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0149_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 3. a04 verified empty-hand aisle approach

```python
s.act(**{'intent': 'a04 verified empty-hand aisle approach', 'left': None, 'right': None, 'base': {'fwd': 0.8}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 217.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117160893351000_33837dfbd4ea48ecad219af7a1d75dca.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0217.jpg`
Sim seconds: 27.0

```text
[obs #217 | act=340785b3 | sim= 27.00s | wall= 186.3s | a04 verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0217_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 4. a04 verified empty-hand aisle approach

```python
s.act(**{'intent': 'a04 verified empty-hand aisle approach', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 281.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117213437203000_945e1e74c4d545aeba28bd31d06c5719.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0281.jpg`
Sim seconds: 35.0

```text
[obs #281 | act=5b0ee941 | sim= 35.00s | wall= 238.8s | a04 verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0281_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 5. a04 verified empty-hand aisle approach

```python
s.act(**{'intent': 'a04 verified empty-hand aisle approach', 'left': None, 'right': None, 'base': {'left': 0.35}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 313.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117240854706000_6af93dfde1f748aba0832c5eb5d6810a.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0313.jpg`
Sim seconds: 39.0

```text
[obs #313 | act=4eb3b5ec | sim= 39.00s | wall= 266.1s | a04 verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0313_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 6. a04 verified empty-hand aisle approach

```python
s.act(**{'intent': 'a04 verified empty-hand aisle approach', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 413.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117323927490000_394e684d0e2b4ffd885fa1fb193e9a99.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0413.jpg`
Sim seconds: 51.5

```text
[obs #413 | act=6a554c55 | sim= 51.50s | wall= 349.3s | a04 verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0413_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 7. a04 verified empty-hand aisle approach

```python
s.act(**{'intent': 'a04 verified empty-hand aisle approach', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 513.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117403960088000_81d059ae700c43dabb617888bf2d1ad6.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0513.jpg`
Sim seconds: 64.0

```text
[obs #513 | act=d529bfa0 | sim= 64.00s | wall= 429.4s | a04 verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0513_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 8. a04 verified empty-hand aisle approach

```python
s.act(**{'intent': 'a04 verified empty-hand aisle approach', 'left': None, 'right': None, 'base': {'fwd': 1.15}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 609.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117480704040000_43615a54334f47159889290e28664ee2.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0609.jpg`
Sim seconds: 76.0

```text
[obs #609 | act=3b9e604e | sim= 76.00s | wall= 506.1s | a04 verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0609_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 9. a04 verified empty-hand aisle approach

```python
s.act(**{'intent': 'a04 verified empty-hand aisle approach', 'left': None, 'right': None, 'base': {'yaw_deg': -70}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 661.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117523661113000_8e3992d65eb2457785461dc1a1a65b5e.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0661.jpg`
Sim seconds: 82.5

```text
[obs #661 | act=e557c999 | sim= 82.50s | wall= 549.1s | a04 verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0661_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 10. Approach fax with raised empty hands

```python
s.act(**{'intent': 'Approach fax with raised empty hands', 'left': {'q': [-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232]}, 'right': {'q': [-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466]}, 'base': {'fwd': 0.78}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 767.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117649880482000_d1d273e1df66490193a17c22002028cb.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0767.jpg`
Sim seconds: 96.33333333333333

```text
[obs #767 | act=ae5c8e60 | sim= 96.33s | wall= 675.2s | Approach fax with raised empty hands]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0767_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 11. Deep floor crouch

```python
s.act(**{'intent': 'Deep floor crouch', 'left': None, 'right': None, 'base': None, 'torso': {'q': [1.68, -2.54, -1.62, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 783.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117659391246000_0e1d3e9d20b64cef90405b54bad4f5c8.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0783.jpg`
Sim seconds: 98.73333333333333

```text
[obs #783 | act=f2881a30 | sim= 98.73s | wall= 684.8s | Deep floor crouch]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0783_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 12. Align downward open fingers above measured fax

```python
s.act(**{'intent': 'Align downward open fingers above measured fax', 'left': None, 'right': {'to': [0.61, -0.32, 0.15], 'finger_dir': [0, 0, -1], 'close_dir': [0, 1, 0]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 833.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117693689563000_407373f4336c404da5ba75b948359a1a.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0833.jpg`
Sim seconds: 105.7

```text
[obs #833 | act=e137d39a | sim=105.70s | wall= 718.9s | Align downward open fingers above measured fax]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0833_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 13. Lower open right fingers around casing

```python
s.act(**{'intent': 'Lower open right fingers around casing', 'left': None, 'right': {'to': [0.61, -0.32, 0.035]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: no_progress; observation 862.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117725478340000_8fbdc33ddbce44b89f5ab5890ed2eef2.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0862.jpg`
Sim seconds: 109.63333333333334

```text
[obs #862 | act=721a9dea | sim=109.63s | wall= 750.9s | Lower open right fingers around casing]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0862_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 14. Close casing grip at measured endpoint

```python
s.act(**{'intent': 'Close casing grip at measured endpoint', 'left': {'grip': 0}, 'right': {'q': [-1.17843, -0.12875, 1.02494, -0.03335, -0.98062, 0.4317, 0.10983], 'grip': 0}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 4, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 870.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117742275878000_f1c6a7107d97460ab63e8779748e3178.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0870.jpg`
Sim seconds: 110.63333333333334

```text
[obs #870 | act=a3e4847c | sim=110.63s | wall= 767.7s | Close casing grip at measured endpoint]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.001, 0.0, 0.001] | torso=[1.68, -2.54, -1.62, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[37.14909744262695, 14.441457748413086, -25.924455642700195, 16.767719268798828]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.278, 0.277, 0.235] pad_end=[0.278, 0.282, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.41191, 0.60028, -0.73515, -1.60059, 2.24214, 0.96343, 1.52231] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[-0.0011867920402437449, -0.007151947822421789, -0.0029130775947123766, 0.008942433632910252, -0.000506347743794322, -5.2805349696427584e-05, -0.0002879811800085008] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.602, -0.318, 0.053]m fingers=[0.0354, 0.0346]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.602, -0.285, 0.053] pad_end=[0.602, -0.35, 0.053] measured_pinch=[0.602, -0.318, 0.053]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.17845, -0.12875, 1.02501, -0.03318, -0.97953, 0.43171, 0.10955] q_lag=[0.0, 0.0, -0.0, -0.0, -0.001, -0.0, 0.0]rad limit_margins=[2.477, 0.293, 1.321, 0.372, 1.367, 0.605, 1.451]rad min=0.293rad
     q_cmd=[-1.17843, -0.12875, 1.02494, -0.03335, -0.98062, 0.4317, 0.10983] effort_Nm=[7.124093055725098, 5.803116321563721, 0.16760587692260742, -0.9634912014007568, 0.05888831615447998, -1.9946292638778687, 0.09237471222877502] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0870_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 15. Lift to confirm retained fax

```python
s.act(**{'intent': 'Lift to confirm retained fax', 'left': None, 'right': {'to': [0.602, -0.318, 0.2]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 12, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 893.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117761699371000_59dc30d25d6a42cfa01630c2bf6591b6.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0893.jpg`
Sim seconds: 113.8

```text
[obs #893 | act=b2bd3605 | sim=113.80s | wall= 787.0s | Lift to confirm retained fax]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-2.4791085720062256, -0.8587007522583008, 1.9449619054794312, -2.408341884613037]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.278, 0.277, 0.235] pad_end=[0.278, 0.282, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.41198, 0.60026, -0.73521, -1.60057, 2.24216, 0.96342, 1.52232] q_lag=[0.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[-0.06611171364784241, -0.026220815256237984, 0.007138093933463097, 0.016057973727583885, -0.003172817872837186, -0.000575349316932261, 0.0011720636393874884] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.602, -0.318, 0.199]m fingers=[0.0354, 0.0345]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.602, -0.286, 0.199] pad_end=[0.602, -0.351, 0.199] measured_pinch=[0.602, -0.318, 0.199]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-0.8463, -0.57342, 0.65309, -1.37426, -1.41286, 0.95703, -0.75442] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.001]rad limit_margins=[2.145, 0.738, 1.693, 0.71, 0.933, 0.08, 0.806]rad min=0.08rad
     q_cmd=[-0.8463, -0.57343, 0.65293, -1.37445, -1.41312, 0.95683, -0.75492] effort_Nm=[-0.9107661247253418, -1.2961525917053223, -0.7911570072174072, -0.6482729315757751, 0.24999454617500305, -0.05611022189259529, -0.2974858283996582] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0893_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 16. Tilt retained fax and align left switch probe

```python
s.act(**{'intent': 'Tilt retained fax and align left switch probe', 'left': {'to': [0.58, -0.06, 0.36], 'finger_dir': [0.220337, -0.708506, -0.670426], 'close_dir': [-0.038811, 0.680406, -0.731807]}, 'right': {'to': [0.5, -0.08, 0.23], 'pitch_deg': 35}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 958.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117807797509000_5d8220141cbc44118655101178e12f83.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0958.jpg`
Sim seconds: 122.83333333333333

```text
[obs #958 | act=36daa329 | sim=122.83s | wall= 833.1s | Tilt retained fax and align left switch probe]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.766762733459473, -2.0892066955566406, 3.288773536682129, 0.22231626510620117]
  L: rigid_TCP(fwd,left,up)=[0.58, -0.06, 0.36]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.58, -0.062, 0.362] pad_end=[0.58, -0.058, 0.358] measured_pinch=[0.58, -0.06, 0.36]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.62911, 0.00338, -0.66858, -1.7853, 1.42469, 0.73074, 0.7783] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.928, 0.168, 1.678, 0.299, 0.922, 0.306, 0.783]rad min=0.168rad
     q_cmd=[-0.6292, 0.00326, -0.66858, -1.78521, 1.42466, 0.73081, 0.77839] effort_Nm=[0.6107031106948853, 0.7100998759269714, 0.0674971491098404, 0.0957014337182045, -0.010884232819080353, 0.015069881454110146, 0.04073880985379219] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0354, 0.0345]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.5, -0.048, 0.23] pad_end=[0.5, -0.112, 0.23] measured_pinch=[0.5, -0.08, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.4077, -0.14111, 1.022, -1.51645, -0.58573, 0.15583, -1.00913] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.001, 0.001]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.552]rad min=0.306rad
     q_cmd=[-0.40775, -0.1411, 1.022, -1.51655, -0.58551, 0.15468, -1.00861] effort_Nm=[-1.3798340559005737, 1.1564099788665771, 0.22172172367572784, -2.461312770843506, 1.1702978610992432, -0.7107996940612793, -0.05292733013629913] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0958_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 17. Approach measured switch

```python
s.act(**{'intent': 'Approach measured switch', 'left': {'to': [0.5969013571739197, -0.1291404664516449, 0.2829010486602783], 'offset': [-0.01, 0.015, 0.02]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 969.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117827752156000_1b84fce20d6a4f199e91a4e7ec0909ba.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0969.jpg`
Sim seconds: 124.36666666666666

```text
[obs #969 | act=6fd5c466 | sim=124.37s | wall= 853.0s | Approach measured switch]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[0.001, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-6.128363609313965, -2.6803433895111084, 4.35399866104126, 0.15579253435134888]
  L: rigid_TCP(fwd,left,up)=[0.587, -0.114, 0.304]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.587, -0.116, 0.306] pad_end=[0.587, -0.112, 0.302] measured_pinch=[0.587, -0.114, 0.304]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.72018, -0.09156, -0.77262, -1.43127, 1.26123, 0.57489, 0.53612] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[2.019, 0.073, 1.574, 0.653, 1.085, 0.462, 1.025]rad min=0.073rad
     q_cmd=[-0.72026, -0.09164, -0.77268, -1.43097, 1.26113, 0.57475, 0.53594] effort_Nm=[0.06272219121456146, 0.3076115846633911, 0.12251881510019302, -0.2765998840332031, -0.0010475516319274902, -0.015070699155330658, -0.010773132555186749] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0354, 0.0345]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.5, -0.048, 0.23] pad_end=[0.5, -0.112, 0.23] measured_pinch=[0.5, -0.08, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.40769, -0.14111, 1.022, -1.51644, -0.58576, 0.1558, -1.00911] q_lag=[-0.0, 0.0, 0.0, -0.0, 0.0, -0.001, 0.0]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.552]rad min=0.306rad
     q_cmd=[-0.40775, -0.1411, 1.022, -1.51655, -0.58551, 0.15468, -1.00861] effort_Nm=[-1.479323387145996, 1.207275152206421, 0.21319149434566498, -2.5570812225341797, 1.2242003679275513, -0.7358369827270508, -0.03180335834622383] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0969_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 18. Press angled finger onto switch

```python
s.act(**{'intent': 'Press angled finger onto switch', 'left': {'to': [0.5981376767158508, -0.12902718782424927, 0.2830297350883484], 'offset': [0.003, -0.004, -0.005]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 6, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: no_progress; observation 990.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117845463739000_625acea690384f4098db35b9faafec71.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0990.jpg`
Sim seconds: 127.06666666666666

```text
[obs #990 | act=7ec2797d | sim=127.07s | wall= 870.9s | Press angled finger onto switch]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[0.002, -0.0, -0.003] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.098921775817871, -2.2225213050842285, 3.5805716514587402, 0.006162106990814209]
  L: rigid_TCP(fwd,left,up)=[0.598, -0.141, 0.289]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm) TRACKING_ERROR(q4=+0.020,q5=-0.027)
     pad_start=[0.598, -0.143, 0.291] pad_end=[0.598, -0.14, 0.287] measured_pinch=[0.598, -0.142, 0.289]m
     close_dir=[-0.04, 0.65, -0.75] fing_dir=[0.22, -0.73, -0.65] q=[-0.81461, -0.12953, -0.84313, -1.24697, 1.29112, 0.4839, 0.4289] q_lag=[-0.0, 0.001, 0.014, 0.02, -0.027, 0.005, 0.003]rad limit_margins=[2.114, 0.035, 1.503, 0.837, 1.055, 0.553, 1.132]rad min=0.035rad
     q_cmd=[-0.81469, -0.12902, -0.82863, -1.22743, 1.26451, 0.48903, 0.43211] effort_Nm=[-15.30664348602295, 38.89686965942383, 24.999935150146484, 24.99950408935547, -11.634211540222168, -11.98111629486084, 14.405887603759766] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.498, -0.08, 0.229]m fingers=[0.0355, 0.0341]m grip=command=0.0 finger_sum(7.0cm)
     pad_start=[0.498, -0.047, 0.229] pad_end=[0.498, -0.112, 0.229] measured_pinch=[0.498, -0.079, 0.229]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[0.57, 0.0, -0.82] q=[-0.4082, -0.14133, 1.023, -1.51552, -0.59351, 0.15795, -1.00916] q_lag=[0.0, 0.0, -0.001, -0.001, 0.008, -0.003, 0.001]rad limit_margins=[1.707, 0.306, 1.323, 0.569, 1.753, 0.879, 0.552]rad min=0.306rad
     q_cmd=[-0.40775, -0.1411, 1.022, -1.51655, -0.58551, 0.15468, -1.00861] effort_Nm=[14.251681327819824, 4.086676597595215, 9.552038192749023, -16.823144912719727, 10.166428565979004, -7.62015438079834, -8.461263656616211] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"blocked","causes":["blocked"],"confidence":"suspected","plateau":true,"normalized_error_history":[7.084092550551548,2.881228147307926,2.7806868414022317,2.7624033460164705,2.750947069994481,2.745204027657183],"normalized_progress":4.338888522894365,"recent_max_joint_lag_rad":[0.02691960334777832,0.026731371879577637,0.026610493659973145],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=no_progress fault=None uncertain=False pending=['left']
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_0990_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 19. Withdraw probe

```python
s.act(**{'intent': 'Withdraw probe', 'left': {'to': [0.61, -0.04, 0.36]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1007.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117856864388000_86f638357a4645e39fd72f159c513255.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1007.jpg`
Sim seconds: 129.33333333333334

```text
[obs #1007 | act=e95c768d | sim=129.33s | wall= 882.2s | Withdraw probe]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, 0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.040839195251465, -1.765871524810791, 3.01163911819458, -1.2148889303207397]
  L: rigid_TCP(fwd,left,up)=[0.61, -0.04, 0.359]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.61, -0.042, 0.361] pad_end=[0.61, -0.039, 0.357] measured_pinch=[0.61, -0.041, 0.359]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.73231, 0.0717, -0.65861, -1.7497, 1.54612, 0.72178, 0.78413] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.031, 0.236, 1.688, 0.335, 0.8, 0.315, 0.777]rad min=0.236rad
     q_cmd=[-0.73228, 0.07178, -0.65853, -1.74989, 1.54636, 0.72186, 0.7843] effort_Nm=[0.23230236768722534, -0.4007079303264618, -0.27655163407325745, 0.271146297454834, 0.010732538998126984, 0.021554838865995407, 0.003171874675899744] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0351, 0.0342]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.5, -0.048, 0.23] pad_end=[0.5, -0.112, 0.23] measured_pinch=[0.5, -0.08, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.40771, -0.14111, 1.02201, -1.51645, -0.58557, 0.15619, -1.00927] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.002, 0.001]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.761, 0.881, 0.552]rad min=0.306rad
     q_cmd=[-0.40775, -0.1411, 1.022, -1.51655, -0.58551, 0.15468, -1.00861] effort_Nm=[-1.448535442352295, 1.1503899097442627, 0.20094034075737, -2.51114821434021, 1.1943925619125366, -0.7256777286529541, -0.059722211211919785] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1007_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 20. Stand retaining fax in bent-arm posture

```python
s.act(**{'intent': 'Stand retaining fax in bent-arm posture', 'left': None, 'right': None, 'base': None, 'torso': {'q': [0.84, -1.00609, -0.42, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1023.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117883555754000_d94203295aa8477aba074050cab3aa16.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1023.jpg`
Sim seconds: 131.73333333333332

```text
[obs #1023 | act=17c62544 | sim=131.73s | wall= 908.9s | Stand retaining fax in bent-arm posture]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.001, 0.0, -0.0] | torso=[0.841, -1.007, -0.42, 0.0] err=[-0.001, 0.001, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-99.99108123779297, -66.88055419921875, 38.36887741088867, 0.40198802947998047]
  L: rigid_TCP(fwd,left,up)=[0.689, -0.04, 1.038]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.688, -0.042, 1.04] pad_end=[0.69, -0.039, 1.036] measured_pinch=[0.689, -0.041, 1.038]m
     close_dir=[0.32, 0.68, -0.66] fing_dir=[0.52, -0.71, -0.48] q=[-0.7323, 0.07179, -0.65852, -1.74987, 1.546, 0.72198, 0.7843] q_lag=[0.0, -0.0, -0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.031, 0.236, 1.688, 0.335, 0.8, 0.315, 0.776]rad min=0.236rad
     q_cmd=[-0.73228, 0.07178, -0.65853, -1.74989, 1.54636, 0.72186, 0.7843] effort_Nm=[1.3800976276397705, -0.9100373983383179, -0.6631072759628296, -2.3934757709503174, 0.19560900330543518, 0.07623441517353058, -0.288571298122406] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.655, -0.08, 0.871]m fingers=[0.0351, 0.0342]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.655, -0.048, 0.871] pad_end=[0.655, -0.112, 0.871] measured_pinch=[0.655, -0.08, 0.871]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[0.9, -0.0, -0.44] q=[-0.4077, -0.14112, 1.02201, -1.5164, -0.58584, 0.15631, -1.00937] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.002, 0.001]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.551]rad min=0.306rad
     q_cmd=[-0.40775, -0.1411, 1.022, -1.51655, -0.58551, 0.15468, -1.00861] effort_Nm=[-1.3202787637710571, 2.6306166648864746, 0.2651328444480896, -4.988252639770508, 2.3052077293395996, -1.3824925422668457, -0.12849563360214233] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1023_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 21. Retract high carry to reduce rotational swept radius

```python
s.act(**{'intent': 'Retract high carry to reduce rotational swept radius', 'left': {'q': [0, 0, 0, 0, 0, 0, 0]}, 'right': {'to': [0.42, -0.2, 1.05]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: no_progress; observation 1090.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117927167983000_e48ce437448f4818866c585002dc9f59.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1090.jpg`
Sim seconds: 141.26666666666668

```text
[obs #1090 | act=5b811cc4 | sim=141.27s | wall= 952.6s | Retract high carry to reduce rotational swept radius]
  base_odom(sim): rel_xyz=[-3.795, -1.551, 0.001]m rel_yaw=+1.962rad vel=[0.0, -0.001, -0.001] | torso=[0.841, -1.006, -0.42, 0.0] err=[-0.001, -0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-100.00204467773438, -39.051551818847656, 20.051040649414062, -32.17647933959961]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-0.00029, -2e-05, -0.00042, 0.00044, 5e-05, -0.00017, 6e-05] q_lag=[0.0, 0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.7191122174263, 0.2414814680814743, -0.0013275444507598877, 0.19516566395759583, -0.0018221018835902214, 0.01972953788936138, 0.006008476484566927] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.4, -0.255, 0.909]m fingers=[0.0351, 0.0343]m grip=command=0.0 finger_sum(6.9cm) TRACKING_ERROR(q2=-0.063)
     pad_start=[0.4, -0.223, 0.907] pad_end=[0.4, -0.287, 0.911] measured_pinch=[0.4, -0.255, 0.909]m
     close_dir=[0.0, 1.0, -0.05] fing_dir=[0.88, -0.03, -0.47] q=[0.25699, -0.84176, 1.20192, -2.08435, -0.24844, -0.24663, -1.27549] q_lag=[0.002, -0.063, -0.001, -0.0, 0.0, -0.001, 0.001]rad limit_margins=[1.042, 1.006, 1.144, 0.0, 2.098, 0.791, 0.285]rad min=0.0rad
     q_cmd=[0.25885, -0.90448, 1.20112, -2.0844, -0.24843, -0.24806, -1.2747] effort_Nm=[24.650480270385742, -54.99757385253906, 4.076094627380371, -2.5373034477233887, 1.9664006233215332, -0.5684220194816589, -0.023388803005218506] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"joint_limit","causes":["joint_limit"],"confidence":"limited","plateau":false,"normalized_error_history":[63.766083867277935,53.9926678518016,44.19428445338049,35.31538753485962,31.931702877230766,30.0809969431443,29.421889804041317,29.347479975320027,29.192857717800813,29.008046230743545,30.55716108703008],"normalized_progress":33.20892278024785,"recent_max_joint_lag_rad":[0.04027819633483887,0.07237845659255981,0.06271934509277344],"outward_near_limit_joints":[3],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"}}
  status=no_progress fault=None uncertain=False pending=['right']
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1090_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 22. Replace stalled folded pose with overhead carry clear of divider height

```python
s.act(**{'intent': 'Replace stalled folded pose with overhead carry clear of divider height', 'left': None, 'right': {'q': [-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1116.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792117955964524000_1489a3098ddf4140914872d3a6171071.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1116.jpg`
Sim seconds: 145.26666666666668

```text
[obs #1116 | act=b399aea1 | sim=145.27s | wall= 981.3s | Replace stalled folded pose with overhead carry clear of divider height]
  base_odom(sim): rel_xyz=[-3.794, -1.55, -0.003]m rel_yaw=+1.961rad vel=[0.001, -0.001, -0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[100.00110626220703, 79.7511215209961, -62.803707122802734, 12.437126159667969]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[5e-05, -0.0, 5e-05, 3e-05, 1e-05, -0.0, 2e-05] q_lag=[-0.0, 0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.6764082908630371, 0.2252567857503891, -0.003662027418613434, 0.34036338329315186, -0.004325546324253082, 0.054259542375802994, 0.00393432192504406] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.871, -0.241, 1.69]m fingers=[0.0352, 0.0342]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.873, -0.209, 1.69] pad_end=[0.869, -0.273, 1.69] measured_pinch=[0.871, -0.241, 1.69]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59941, 0.04996, -0.13029, -0.12054, 0.06473, 0.99992, -0.13968] q_lag=[-0.001, 0.0, 0.0, 0.001, 0.0, 0.0, -0.0]rad limit_margins=[1.841, 0.115, 2.216, 0.46, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[34.43699645996094, -2.9397897720336914, -0.0784459114074707, 14.9277925491333, 0.3608675003051758, 3.5800771713256836, -0.7507092356681824] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1116_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 23. Move overhead carried fax toward clear turn location, avoiding prior side-shift contact

```python
s.act(**{'intent': 'Move overhead carried fax toward clear turn location, avoiding prior side-shift contact', 'left': None, 'right': None, 'base': {'fwd': 0.77, 'left': 0.06}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1180.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792118014024632000_841a178f7dd4407e8e486faff0ca9f48.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1180.jpg`
Sim seconds: 153.26666666666668

```text
[obs #1180 | act=298cc9e9 | sim=153.27s | wall=1039.5s | Move overhead carried fax toward clear turn location, avoiding prior side-shift contact]
  base_odom(sim): rel_xyz=[-4.143, -0.862, -0.001]m rel_yaw=+1.961rad vel=[0.084, 0.006, 0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-7.89523983001709, -5.48497200012207, 5.806393623352051, -0.443587064743042]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-1e-05, 0.0, -1e-05, -0.0, -0.0, -0.0, -0.0] q_lag=[0.0, -0.0, 0.0, 0.0, 0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.02752486988902092, -0.01503779273480177, 4.039425402879715e-05, 0.007916186936199665, 1.9577564671635628e-05, 0.0008509219624102116, -0.00029197838739492] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0352, 0.0342]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.874, -0.209, 1.689] pad_end=[0.87, -0.273, 1.689] measured_pinch=[0.872, -0.241, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59987, 0.05003, -0.13069, -0.11974, 0.06527, 1.00018, -0.13968] q_lag=[-0.0, -0.0, 0.001, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.004681587219238, -0.0016553401947021484, 0.2491639256477356, -3.2505555152893066, 0.18576756119728088, -2.026577949523926, -8.58306884765625e-06] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1180_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 24. Turn overhead fax above divider with base at final clear location

```python
s.act(**{'intent': 'Turn overhead fax above divider with base at final clear location', 'left': None, 'right': None, 'base': {'yaw_deg': 115}, 'torso': None, 'seconds': None, 'max_steps': 28, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1264.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792118094596051000_2e358a2bb8194bcc8d61a2e9216b4115.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1264.jpg`
Sim seconds: 163.76666666666668

```text
[obs #1264 | act=f7686934 | sim=163.77s | wall=1120.0s | Turn overhead fax above divider with base at final clear location]
  base_odom(sim): rel_xyz=[-4.142, -0.862, -0.001]m rel_yaw=-2.336rad vel=[0.006, 0.005, 0.2] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-8.094476699829102, -5.682977199554443, 5.968305587768555, -0.5025188326835632]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, -0.0, -1e-05, -0.0, 0.0, -0.0] q_lag=[0.0, -0.0, 0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.014093960635364056, -0.01962178573012352, -0.0002023843117058277, 0.004087710753083229, -0.00016263278666883707, 0.0005551638314500451, -0.0008049517055042088] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.872, -0.241, 1.689]m fingers=[0.0352, 0.0342]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.874, -0.209, 1.689] pad_end=[0.87, -0.273, 1.689] measured_pinch=[0.872, -0.241, 1.689]m
     close_dir=[0.06, 1.0, 0.0] fing_dir=[0.99, -0.06, -0.11] q=[-2.59987, 0.05003, -0.1307, -0.11975, 0.06519, 1.00017, -0.13968] q_lag=[-0.0, -0.0, 0.001, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[1.841, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-2.6, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.081544399261475, 0.027547121047973633, 0.25188350677490234, -3.274364471435547, 0.1860494613647461, -2.025521755218506, -0.0008193254470825195] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1264_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 25. Lower overhead fax above unobstructed desktop

```python
s.act(**{'intent': 'Lower overhead fax above unobstructed desktop', 'left': None, 'right': {'q': [-1.45, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 12, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1277.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792118110178055000_d561d9dc0bfc4ec484bd6ec3b5e64b94.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1277.jpg`
Sim seconds: 165.73333333333332

```text
[obs #1277 | act=4c29a089 | sim=165.73s | wall=1135.5s | Lower overhead fax above unobstructed desktop]
  base_odom(sim): rel_xyz=[-4.142, -0.862, -0.001]m rel_yaw=-2.336rad vel=[0.003, -0.001, -0.001] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-79.21978759765625, -52.669498443603516, 58.39599609375, 5.221750259399414]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[1e-05, 1e-05, 8e-05, -0.00016, -1e-05, 4e-05, -3e-05] q_lag=[-0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.4861432909965515, -0.31545454263687134, -0.00015942752361297607, -0.013954081572592258, 0.0006751406472176313, -0.027991533279418945, -0.011340140365064144] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.875, -0.241, 0.906]m fingers=[0.0352, 0.0342]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.876, -0.209, 0.905] pad_end=[0.874, -0.273, 0.908] measured_pinch=[0.875, -0.241, 0.906]m
     close_dir=[0.03, 1.0, -0.05] fing_dir=[0.3, -0.06, -0.95] q=[-1.4504, 0.05001, -0.13167, -0.11767, 0.06489, 1.0003, -0.13971] q_lag=[0.0, -0.0, 0.002, -0.002, 0.0, -0.0, -0.0]rad limit_margins=[2.749, 0.114, 2.215, 0.457, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.45, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-52.62765884399414, 3.6485204696655273, 0.8935146331787109, -24.995420455932617, 0.2615203857421875, -7.74940299987793, 0.4528310298919678] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1277_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 26. Lower last five centimetres onto table

```python
s.act(**{'intent': 'Lower last five centimetres onto table', 'left': None, 'right': {'q': [-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1281.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792118113388801000_cd4735403805410fa18df4e95c09730a.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1281.jpg`
Sim seconds: 166.23333333333332

```text
[obs #1281 | act=0c5a2888 | sim=166.23s | wall=1138.8s | Lower last five centimetres onto table]
  base_odom(sim): rel_xyz=[-4.142, -0.862, -0.001]m rel_yaw=-2.336rad vel=[0.001, -0.0, -0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-39.933982849121094, -26.15118408203125, 22.623157501220703, 0.30812883377075195]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-1e-05, 0.0, 4e-05, -7e-05, -0.0, 2e-05, -1e-05] q_lag=[0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.9679312705993652, -0.16832348704338074, -0.003639429807662964, 0.2112710177898407, -0.0029314085841178894, 0.013647284358739853, -0.007202995475381613] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.838, -0.241, 0.854]m fingers=[0.0352, 0.0342]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.839, -0.209, 0.852] pad_end=[0.837, -0.273, 0.856] measured_pinch=[0.838, -0.241, 0.854]m
     close_dir=[0.02, 1.0, -0.06] fing_dir=[0.22, -0.06, -0.97] q=[-1.35989, 0.05002, -0.13108, -0.11962, 0.06469, 1.00015, -0.13971] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[2.659, 0.114, 2.215, 0.459, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-14.927115440368652, 0.43541955947875977, 0.47304391860961914, -7.3881731033325195, 0.3358149528503418, -2.1107211112976074, -0.20607797801494598] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1281_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 27. Release powered fax on carrel

```python
s.act(**{'intent': 'Release powered fax on carrel', 'left': None, 'right': {'grip': 1}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 4, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1285.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792118124195750000_e0ca961f9b794bc5baf1ebf4c22efa95.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1285.jpg`
Sim seconds: 166.73333333333332

```text
[obs #1285 | act=fd3b91e7 | sim=166.73s | wall=1149.6s | Release powered fax on carrel]
  base_odom(sim): rel_xyz=[-4.142, -0.862, -0.001]m rel_yaw=-2.336rad vel=[0.001, 0.002, -0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[0.006585568189620972, 0.013075549155473709, -0.013858586549758911, 0.09506280720233917]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.012098219245672226, 0.03178175538778305, 0.00023570959456264973, 0.0004810762475244701, 0.00012279057409614325, -0.00038442001095972955, 0.0007856183219701052] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.838, -0.242, 0.854]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.839, -0.194, 0.852] pad_end=[0.837, -0.289, 0.857] measured_pinch=[0.838, -0.242, 0.854]m
     close_dir=[0.02, 1.0, -0.06] fing_dir=[0.22, -0.06, -0.97] q=[-1.36, 0.05, -0.12999, -0.12, 0.06501, 1.0, -0.14] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[2.659, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-0.009905926883220673, 0.044640351086854935, 0.002120007760822773, -0.0006483509205281734, 0.000607973663136363, -0.000951633439399302, -0.00023089781461749226] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1285_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 28. Withdraw above fax

```python
s.act(**{'intent': 'Withdraw above fax', 'left': None, 'right': {'q': [-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1290.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792118127480900000_4c50f25889a741bfa998af2470b8bf9e.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1290.jpg`
Sim seconds: 167.36666666666667

```text
[obs #1290 | act=b9d7f255 | sim=167.37s | wall=1152.9s | Withdraw above fax]
  base_odom(sim): rel_xyz=[-4.142, -0.862, -0.001]m rel_yaw=-2.336rad vel=[-0.0, 0.0, -0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[66.50753784179688, 42.22193145751953, -31.532548904418945, 2.5853538513183594]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[3e-05, -0.0, -1e-05, 4e-05, 0.0, -1e-05, 1e-05] q_lag=[-0.0, 0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-1.84129798412323, 0.2526271939277649, 0.00637701153755188, -0.3984212577342987, 0.004906125366687775, -0.02363816276192665, 0.006799493450671434] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.242, 1.035]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.942, -0.195, 1.033] pad_end=[0.938, -0.289, 1.038] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.05] fing_dir=[0.49, -0.06, -0.87] q=[-1.64948, 0.04998, -0.12906, -0.12012, 0.06606, 1.00007, -0.14] q_lag=[-0.001, 0.0, -0.001, 0.0, -0.001, -0.0, 0.0]rad limit_margins=[2.791, 0.115, 2.217, 0.459, 2.28, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[14.285618782043457, 0.7811710834503174, -0.31383275985717773, 5.499844074249268, -0.2764706611633301, 0.6576529145240784, 0.28304046392440796] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1290_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 29. Verify two seconds independent stable support

```python
s.act(**{'intent': 'Verify two seconds independent stable support', 'left': None, 'right': None, 'base': None, 'torso': None, 'seconds': 2, 'max_steps': 1, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1303.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/receipt_01792118134782994000_feee08cf892f43cc99d6d94476470abe.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1303.jpg`
Sim seconds: 169.36666666666667

```text
[obs #1303 | act=cc6ad1fb | sim=169.37s | wall=1160.0s | Verify two seconds independent stable support]
  base_odom(sim): rel_xyz=[-4.142, -0.862, -0.001]m rel_yaw=-2.336rad vel=[-0.0, 0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[0.022666383534669876, -0.006232391111552715, -0.01964534819126129, 0.028856094926595688]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.0016504189698025584, 0.040602508932352066, 0.00018491619266569614, 0.0007735129329375923, 0.00011545943561941385, 0.00023276761930901557, 0.0014668568037450314] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.242, 1.035]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.942, -0.194, 1.033] pad_end=[0.939, -0.289, 1.038] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.05] fing_dir=[0.49, -0.06, -0.87] q=[-1.65, 0.05, -0.12998, -0.12, 0.06501, 1.0, -0.14] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[2.791, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[0.014835110865533352, 0.028148144483566284, 0.0012736646458506584, 0.00597489345818758, 0.0004928738344460726, 0.0006410082569345832, -0.0004188830789644271] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a04/obs_1303_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```
