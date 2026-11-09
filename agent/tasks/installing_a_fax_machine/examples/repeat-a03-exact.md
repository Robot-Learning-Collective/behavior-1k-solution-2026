# a03 exact public action sequence

Historical record, not a blind replay script. Includes unsuccessful recovery motions and rejected requests; inspect images and remeasure before contacts. All arguments preserved, including max_steps.

## 1. a03 repeat verified empty-hand aisle approach

```python
s.act(**{'intent': 'a03 repeat verified empty-hand aisle approach', 'left': {'grip': 1}, 'right': {'grip': 1}, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 65.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792115644301913000_0de6e67b3fba43fc8dad69828b897138.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0065.jpg`
Sim seconds: 8.0

```text
[obs #065 | act=d196ddf5 | sim=  8.00s | wall=  63.0s | a03 repeat verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0065_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 2. a03 repeat verified empty-hand aisle approach

```python
s.act(**{'intent': 'a03 repeat verified empty-hand aisle approach', 'left': None, 'right': None, 'base': {'fwd': 1.0}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 149.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792115713704676000_49d5efb081d54c2cb4268360035885b7.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0149.jpg`
Sim seconds: 18.5

```text
[obs #149 | act=b32342b5 | sim= 18.50s | wall= 132.4s | a03 repeat verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0149_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 3. a03 repeat verified empty-hand aisle approach

```python
s.act(**{'intent': 'a03 repeat verified empty-hand aisle approach', 'left': None, 'right': None, 'base': {'fwd': 0.8}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 217.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792115763791312000_dc7c4afea90f4bb8983226275c18eaad.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0217.jpg`
Sim seconds: 27.0

```text
[obs #217 | act=2fbf2cd2 | sim= 27.00s | wall= 182.6s | a03 repeat verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0217_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 4. a03 repeat verified empty-hand aisle approach

```python
s.act(**{'intent': 'a03 repeat verified empty-hand aisle approach', 'left': None, 'right': None, 'base': {'yaw_deg': -90}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 281.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792115812138793000_5b6f7046ff25480d8e1aab185c6c163b.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0281.jpg`
Sim seconds: 35.0

```text
[obs #281 | act=5a605603 | sim= 35.00s | wall= 230.9s | a03 repeat verified empty-hand aisle approach]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0281_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 5. a03 traverse known clear wall-side aisle to fax passage

```python
s.act(**{'intent': 'a03 traverse known clear wall-side aisle to fax passage', 'left': None, 'right': None, 'base': {'left': 0.35}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 313.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792115853762468000_a237449b23f54b5d9ea03352a9db93bc.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0313.jpg`
Sim seconds: 39.0

```text
[obs #313 | act=e51ce596 | sim= 39.00s | wall= 272.5s | a03 traverse known clear wall-side aisle to fax passage]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0313_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 6. a03 traverse known clear wall-side aisle to fax passage

```python
s.act(**{'intent': 'a03 traverse known clear wall-side aisle to fax passage', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 413.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792115936557358000_bd3d75421c414ca49fb9c89bf180511c.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0413.jpg`
Sim seconds: 51.5

```text
[obs #413 | act=93472a0b | sim= 51.50s | wall= 355.4s | a03 traverse known clear wall-side aisle to fax passage]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0413_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 7. a03 traverse known clear wall-side aisle to fax passage

```python
s.act(**{'intent': 'a03 traverse known clear wall-side aisle to fax passage', 'left': None, 'right': None, 'base': {'fwd': 1.2}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 513.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116020570466000_b742b006bf6a4d4bbc8eed57db276016.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0513.jpg`
Sim seconds: 64.0

```text
[obs #513 | act=3165ef83 | sim= 64.00s | wall= 439.4s | a03 traverse known clear wall-side aisle to fax passage]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0513_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 8. a03 traverse known clear wall-side aisle to fax passage

```python
s.act(**{'intent': 'a03 traverse known clear wall-side aisle to fax passage', 'left': None, 'right': None, 'base': {'fwd': 1.15}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 609.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116103220879000_80c6aec167a142b6bdaec6906b5bf2f5.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0609.jpg`
Sim seconds: 76.0

```text
[obs #609 | act=37330c32 | sim= 76.00s | wall= 522.0s | a03 traverse known clear wall-side aisle to fax passage]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0609_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 9. a03 traverse known clear wall-side aisle to fax passage

```python
s.act(**{'intent': 'a03 traverse known clear wall-side aisle to fax passage', 'left': None, 'right': None, 'base': {'yaw_deg': -70}, 'torso': None, 'seconds': None, 'max_steps': 32, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 661.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116149474252000_04e858e3de0b4c4e8e158fef46f8516b.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0661.jpg`
Sim seconds: 82.5

```text
[obs #661 | act=6f893a85 | sim= 82.50s | wall= 568.1s | a03 traverse known clear wall-side aisle to fax passage]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0661_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 10. Approach fax while raising empty hands using proven joint endpoints

```python
s.act(**{'intent': 'Approach fax while raising empty hands using proven joint endpoints', 'left': {'q': [-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232]}, 'right': {'q': [-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.0372, -0.79466]}, 'base': {'fwd': 0.78}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: request_rejected; observation None.

## 11. Approach with proven pregrasp joints inside exact wrist limit

```python
s.act(**{'intent': 'Approach with proven pregrasp joints inside exact wrist limit', 'left': {'q': [-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232]}, 'right': {'q': [-0.52695, -0.35921, 0.79382, -0.97008, -1.51884, 1.036, -0.79466]}, 'base': {'fwd': 0.78}, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 767.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116264210109000_2ff79fa4307d49c3908d43ce8b4762f5.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0767.jpg`
Sim seconds: 96.33333333333333

```text
[obs #767 | act=03765a06 | sim= 96.33s | wall= 683.0s | Approach with proven pregrasp joints inside exact wrist limit]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0767_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 12. Deep floor crouch

```python
s.act(**{'intent': 'Deep floor crouch', 'left': None, 'right': None, 'base': None, 'torso': {'q': [1.68, -2.54, -1.62, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 783.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116272870229000_3ed25f1df444414fa59f8815f9c2c70d.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0783.jpg`
Sim seconds: 98.73333333333333

```text
[obs #783 | act=42f838d0 | sim= 98.73s | wall= 691.7s | Deep floor crouch]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0783_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 13. Align downward open fingers above fax

```python
s.act(**{'intent': 'Align downward open fingers above fax', 'left': None, 'right': {'pos': [0.61, -0.32, 0.15], 'finger_dir': [0, 0, -1], 'close_dir': [0, 1, 0]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: request_rejected; observation None.

## 14. Align downward fingers above fax

```python
s.act(**{'intent': 'Align downward fingers above fax', 'left': None, 'right': {'to': [0.61, -0.32, 0.15], 'finger_dir': [0, 0, -1], 'close_dir': [0, 1, 0]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 833.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116411773938000_52d2384591bb432cbbb9c86f3fdfebc9.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0833.jpg`
Sim seconds: 105.7

```text
[obs #833 | act=177f0f33 | sim=105.70s | wall= 830.6s | Align downward fingers above fax]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0833_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 15. Lower open grasp around fax casing

```python
s.act(**{'intent': 'Lower open grasp around fax casing', 'left': None, 'right': {'to': [0.61, -0.32, 0.035]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: no_progress; observation 862.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116441114713000_b5a666cf03a24787a5926c263bdc7ea2.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0862.jpg`
Sim seconds: 109.63333333333334

```text
[obs #862 | act=54673c4a | sim=109.63s | wall= 859.7s | Lower open grasp around fax casing]
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
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0862_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 16. Close at measured casing-height pose; close left for switch probe

```python
s.act(**{'intent': 'Close at measured casing-height pose; close left for switch probe', 'left': {'grip': 0}, 'right': {'q': [-1.17843, -0.12875, 1.02494, -0.03335, -0.98062, 0.4317, 0.10983], 'grip': 0}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 4, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 870.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116454426922000_59e25ee83add4db29b0a76f199352914.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0870.jpg`
Sim seconds: 110.63333333333334

```text
[obs #870 | act=b92a024b | sim=110.63s | wall= 873.2s | Close at measured casing-height pose; close left for switch probe]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.001, 0.001, 0.002] | torso=[1.68, -2.54, -1.62, -0.0] err=[0.0, 0.0, -0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[60.563819885253906, 22.862585067749023, -41.88727951049805, 22.86583709716797]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.278, 0.277, 0.235] pad_end=[0.278, 0.282, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.73] q=[-0.41193, 0.60026, -0.73517, -1.60057, 2.24216, 0.96343, 1.5223] q_lag=[-0.0, 0.0, -0.0, -0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[0.11614617705345154, 0.29575851559638977, 0.036444082856178284, 0.0715799555182457, -0.005200459621846676, -0.0010836431756615639, 0.011508799158036709] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.602, -0.318, 0.053]m fingers=[0.0356, 0.0329]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.602, -0.286, 0.053] pad_end=[0.602, -0.349, 0.053] measured_pinch=[0.602, -0.317, 0.053]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-1.1785, -0.12863, 1.02515, -0.03253, -0.97767, 0.43138, 0.1094] q_lag=[0.0, -0.0, -0.0, -0.001, -0.003, 0.0, 0.0]rad limit_margins=[2.478, 0.293, 1.321, 0.372, 1.369, 0.606, 1.451]rad min=0.293rad
     q_cmd=[-1.17843, -0.12875, 1.02494, -0.03335, -0.98062, 0.4317, 0.10983] effort_Nm=[10.27396011352539, 3.057938575744629, 0.23961663246154785, -0.6694393754005432, 0.12157559394836426, -4.106388568878174, 2.2724807262420654] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0870_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 17. Lift fax to verify retention

```python
s.act(**{'intent': 'Lift fax to verify retention', 'left': None, 'right': {'to': [0.602, -0.318, 0.2]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 12, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 893.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116470417046000_528cfc30799c4b4faae7afc738bacae8.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0893.jpg`
Sim seconds: 113.8

```text
[obs #893 | act=6bdee680 | sim=113.80s | wall= 889.3s | Lift fax to verify retention]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-2.685114860534668, -1.1612050533294678, 2.048168897628784, -2.47914457321167]
  L: rigid_TCP(fwd,left,up)=[0.278, 0.28, 0.235]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.278, 0.277, 0.235] pad_end=[0.278, 0.282, 0.235] measured_pinch=[0.278, 0.28, 0.235]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.69, -0.0, -0.72] q=[-0.41199, 0.60026, -0.73522, -1.60057, 2.24216, 0.96342, 1.52232] q_lag=[0.0, 0.0, 0.0, -0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.711, 0.765, 1.611, 0.484, 0.104, 0.074, 0.038]rad min=0.038rad
     q_cmd=[-0.41196, 0.60027, -0.73519, -1.60058, 2.24216, 0.96342, 1.52232] effort_Nm=[-0.02922515943646431, -0.05777185037732124, -0.009554583579301834, 0.016443349421024323, -0.0011054822243750095, -0.00019769254140555859, -0.0006731486646458507] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.602, -0.318, 0.199]m fingers=[0.0355, 0.0329]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.602, -0.286, 0.199] pad_end=[0.602, -0.349, 0.199] measured_pinch=[0.602, -0.317, 0.199]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.0, -0.0, -1.0] q=[-0.84638, -0.57354, 0.65334, -1.37435, -1.41258, 0.9573, -0.75458] q_lag=[0.0, -0.0, -0.0, -0.0, -0.001, -0.001, -0.0]rad limit_margins=[2.145, 0.738, 1.693, 0.71, 0.934, 0.08, 0.806]rad min=0.08rad
     q_cmd=[-0.84637, -0.57355, 0.65316, -1.37452, -1.4134, 0.95668, -0.75505] effort_Nm=[-0.8886634707450867, -1.3085023164749146, -0.8039906024932861, -0.6570643186569214, 0.2515384554862976, -0.05065910518169403, -0.29257696866989136] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0893_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 18. Tilt retained fax and approach switch with closed left fingers

```python
s.act(**{'intent': 'Tilt retained fax and approach switch with closed left fingers', 'left': {'to': [0.58, -0.06, 0.36], 'finger_dir': [0.220337, -0.708506, -0.670426], 'close_dir': [-0.038811, 0.680406, -0.731807]}, 'right': {'to': [0.5, -0.08, 0.23], 'pitch_deg': 35}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 24, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 958.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116521882727000_419643ba4fd54399ae3156ef24bb7d6a.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0958.jpg`
Sim seconds: 122.9

```text
[obs #958 | act=6b2361d2 | sim=122.90s | wall= 940.7s | Tilt retained fax and approach switch with closed left fingers]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, -0.0, -0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-4.862015247344971, -2.0710699558258057, 3.342311382293701, 0.3100426197052002]
  L: rigid_TCP(fwd,left,up)=[0.58, -0.06, 0.36]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.58, -0.062, 0.362] pad_end=[0.58, -0.058, 0.358] measured_pinch=[0.58, -0.06, 0.36]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.62912, 0.00339, -0.6686, -1.7853, 1.4247, 0.73073, 0.7783] q_lag=[-0.0, -0.0, 0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.928, 0.168, 1.678, 0.299, 0.921, 0.306, 0.782]rad min=0.168rad
     q_cmd=[-0.62922, 0.00327, -0.6686, -1.78521, 1.42468, 0.73079, 0.7784] effort_Nm=[0.6073737740516663, 0.692486047744751, 0.06489618122577667, 0.08882327377796173, -0.011129514314234257, 0.015449082478880882, 0.041173744946718216] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0355, 0.0329]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.5, -0.048, 0.23] pad_end=[0.5, -0.111, 0.23] measured_pinch=[0.5, -0.079, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.40783, -0.14118, 1.0222, -1.51646, -0.5857, 0.15617, -1.00947] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.002, 0.001]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.551]rad min=0.306rad
     q_cmd=[-0.40786, -0.14117, 1.02218, -1.51655, -0.58567, 0.1546, -1.00875] effort_Nm=[-1.387380599975586, 1.191483497619629, 0.25004103779792786, -2.457507848739624, 1.1677135229110718, -0.7051717638969421, -0.03739917278289795] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0958_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 19. Approach measured red switch

```python
s.act(**{'intent': 'Approach measured red switch', 'left': {'to': [0.5968801379203796, -0.12931489944458008, 0.28273138403892517], 'offset': [-0.01, 0.015, 0.02]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 969.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116541572824000_80ec2a5b8cd944d0907bb7936891c796.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0969.jpg`
Sim seconds: 124.43333333333334

```text
[obs #969 | act=289f4aba | sim=124.43s | wall= 960.3s | Approach measured red switch]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, -0.001, -0.0] | torso=[1.68, -2.54, -1.62, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.95953369140625, -2.3517093658447266, 4.268467903137207, 0.2832666039466858]
  L: rigid_TCP(fwd,left,up)=[0.587, -0.114, 0.304]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.587, -0.116, 0.306] pad_end=[0.587, -0.112, 0.302] measured_pinch=[0.587, -0.114, 0.304]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.7204, -0.0919, -0.77296, -1.43015, 1.26082, 0.57432, 0.53543] q_lag=[-0.0, -0.0, -0.0, 0.0, -0.0, -0.0, -0.0]rad limit_margins=[2.019, 0.073, 1.573, 0.654, 1.085, 0.463, 1.025]rad min=0.073rad
     q_cmd=[-0.72049, -0.09199, -0.77302, -1.42985, 1.26072, 0.57418, 0.53525] effort_Nm=[0.06713974475860596, 0.35241439938545227, 0.1413051038980484, -0.2714155614376068, -0.0023598521947860718, -0.0164661705493927, -0.007764399517327547] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0355, 0.0329]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.5, -0.048, 0.23] pad_end=[0.5, -0.111, 0.23] measured_pinch=[0.5, -0.079, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.40783, -0.14118, 1.0222, -1.51645, -0.58572, 0.15617, -1.00947] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.002, 0.001]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.551]rad min=0.306rad
     q_cmd=[-0.40786, -0.14117, 1.02218, -1.51655, -0.58567, 0.1546, -1.00875] effort_Nm=[-1.54990553855896, 1.253393292427063, 0.22334487736225128, -2.5704710483551025, 1.2245824337005615, -0.7343031764030457, -0.0316489078104496] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0969_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 20. Press switch along angled finger direction

```python
s.act(**{'intent': 'Press switch along angled finger direction', 'left': {'to': [0.5981175899505615, -0.12919782102108002, 0.28286632895469666], 'offset': [0.003, -0.004, -0.005]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 6, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: no_progress; observation 986.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116561413546000_1e04b6a4ceff4900a5a567ae75d7b2e6.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0986.jpg`
Sim seconds: 126.63333333333334

```text
[obs #986 | act=dfe54f3f | sim=126.63s | wall= 980.1s | Press switch along angled finger direction]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[0.001, -0.001, -0.003] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-5.422159671783447, -2.197739601135254, 3.678997278213501, -0.7655520439147949]
  L: rigid_TCP(fwd,left,up)=[0.597, -0.141, 0.287]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm) TRACKING_ERROR(q5=-0.027)
     pad_start=[0.597, -0.143, 0.289] pad_end=[0.597, -0.14, 0.285] measured_pinch=[0.597, -0.142, 0.287]m
     close_dir=[-0.04, 0.66, -0.75] fing_dir=[0.21, -0.73, -0.65] q=[-0.81394, -0.13071, -0.84348, -1.24219, 1.2892, 0.48474, 0.42772] q_lag=[-0.0, 0.0, 0.016, 0.016, -0.027, 0.005, 0.003]rad limit_margins=[2.113, 0.034, 1.503, 0.842, 1.057, 0.552, 1.133]rad min=0.034rad
     q_cmd=[-0.81403, -0.13021, -0.82707, -1.22627, 1.26219, 0.48987, 0.43093] effort_Nm=[-16.07170867919922, 37.917137145996094, 24.999942779541016, 25.00012969970703, -11.726770401000977, -12.347906112670898, 14.243487358093262] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.498, -0.08, 0.229]m fingers=[0.0356, 0.0329]m grip=command=0.0 finger_sum(6.9cm)
     pad_start=[0.498, -0.047, 0.229] pad_end=[0.498, -0.11, 0.229] measured_pinch=[0.498, -0.079, 0.229]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, 0.0, -0.82] q=[-0.40836, -0.14142, 1.02312, -1.51554, -0.59327, 0.15817, -1.00948] q_lag=[0.001, 0.0, -0.001, -0.001, 0.008, -0.004, 0.001]rad limit_margins=[1.707, 0.306, 1.323, 0.569, 1.753, 0.879, 0.551]rad min=0.306rad
     q_cmd=[-0.40786, -0.14117, 1.02218, -1.51655, -0.58567, 0.1546, -1.00875] effort_Nm=[15.199280738830566, 5.045105934143066, 11.01465129852295, -17.30000114440918, 10.233047485351562, -7.355302333831787, -8.082910537719727] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"blocked","causes":["blocked"],"confidence":"suspected","plateau":true,"normalized_error_history":[7.0833815331592564,2.5743320247389763,2.5772361315551504,2.5769040892276607,2.580896491087588],"normalized_progress":4.502485042071669,"recent_max_joint_lag_rad":[0.02728736400604248,0.02715909481048584,0.027009010314941406],"outward_near_limit_joints":[],"meaning":"blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=no_progress fault=None uncertain=False pending=['left']
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_0986_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 21. Withdraw probe from switch

```python
s.act(**{'intent': 'Withdraw probe from switch', 'left': {'to': [0.61, -0.04, 0.36]}, 'right': None, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1004.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116573432549000_830db9195a4b42af9c2e4e2017da81fe.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1004.jpg`
Sim seconds: 129.0

```text
[obs #1004 | act=1cf3dc7a | sim=129.00s | wall= 992.0s | Withdraw probe from switch]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.0, -0.0, 0.0] | torso=[1.68, -2.54, -1.62, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[1.68, -2.54, -1.62, 0.0] effort_Nm=[-3.9590816497802734, -1.4792762994766235, 2.952016830444336, -1.0656614303588867]
  L: rigid_TCP(fwd,left,up)=[0.61, -0.04, 0.359]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.61, -0.042, 0.361] pad_end=[0.61, -0.039, 0.357] measured_pinch=[0.61, -0.041, 0.359]m
     close_dir=[-0.04, 0.68, -0.73] fing_dir=[0.22, -0.71, -0.67] q=[-0.73115, 0.0702, -0.65655, -1.74969, 1.54455, 0.72406, 0.78404] q_lag=[0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]rad limit_margins=[2.03, 0.235, 1.69, 0.335, 0.802, 0.313, 0.777]rad min=0.235rad
     q_cmd=[-0.73112, 0.07028, -0.65647, -1.74988, 1.54478, 0.72413, 0.7842] effort_Nm=[0.20699703693389893, -0.35336941480636597, -0.2484651803970337, 0.26611536741256714, 0.008076000958681107, 0.01921641267836094, 0.005347533151507378] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.5, -0.08, 0.23]m fingers=[0.0354, 0.033]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.5, -0.048, 0.23] pad_end=[0.5, -0.111, 0.23] measured_pinch=[0.5, -0.079, 0.23]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[0.57, -0.0, -0.82] q=[-0.40783, -0.14118, 1.0222, -1.51646, -0.58572, 0.1561, -1.00939] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.002, 0.001]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.551]rad min=0.306rad
     q_cmd=[-0.40786, -0.14117, 1.02218, -1.51655, -0.58567, 0.1546, -1.00875] effort_Nm=[-1.4935853481292725, 1.2360081672668457, 0.2506360709667206, -2.548356533050537, 1.2069298028945923, -0.7156664729118347, -0.01577564887702465] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1004_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 22. Stand tall with retained fax while still in open aisle

```python
s.act(**{'intent': 'Stand tall with retained fax while still in open aisle', 'left': None, 'right': None, 'base': None, 'torso': {'q': [0.84, -1.00609, -0.42, 0]}, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1020.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116592499484000_e46fe8d169e24b84a1bbae1dedace8e6.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1020.jpg`
Sim seconds: 131.4

```text
[obs #1020 | act=7d80332a | sim=131.40s | wall=1011.3s | Stand tall with retained fax while still in open aisle]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[-0.001, 0.001, -0.0] | torso=[0.841, -1.007, -0.42, 0.0] err=[-0.001, 0.001, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-99.99112701416016, -66.81766510009766, 38.208335876464844, 0.036329030990600586]
  L: rigid_TCP(fwd,left,up)=[0.689, -0.04, 1.038]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.688, -0.042, 1.04] pad_end=[0.69, -0.039, 1.036] measured_pinch=[0.689, -0.041, 1.038]m
     close_dir=[0.32, 0.68, -0.66] fing_dir=[0.52, -0.71, -0.48] q=[-0.73113, 0.07029, -0.65646, -1.74986, 1.54442, 0.72426, 0.7842] q_lag=[0.0, -0.0, -0.0, -0.0, 0.0, -0.0, 0.0]rad limit_margins=[2.03, 0.235, 1.69, 0.335, 0.802, 0.313, 0.777]rad min=0.235rad
     q_cmd=[-0.73112, 0.07028, -0.65647, -1.74988, 1.54478, 0.72413, 0.7842] effort_Nm=[1.3543553352355957, -1.007299780845642, -0.6819328665733337, -2.4034512042999268, 0.19586139917373657, 0.07506369799375534, -0.290923148393631] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.655, -0.08, 0.871]m fingers=[0.0355, 0.0329]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.655, -0.048, 0.871] pad_end=[0.655, -0.111, 0.871] measured_pinch=[0.655, -0.079, 0.871]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[0.9, -0.0, -0.44] q=[-0.40782, -0.14118, 1.0222, -1.51641, -0.58596, 0.15634, -1.00959] q_lag=[-0.0, 0.0, -0.0, -0.0, 0.0, -0.002, 0.001]rad limit_margins=[1.707, 0.306, 1.324, 0.568, 1.76, 0.881, 0.551]rad min=0.306rad
     q_cmd=[-0.40786, -0.14117, 1.02218, -1.51655, -0.58567, 0.1546, -1.00875] effort_Nm=[-1.0712668895721436, 2.2000041007995605, 0.16054946184158325, -4.80615234375, 2.245147228240967, -1.3633679151535034, -0.20211169123649597] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1020_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 23. Raise straight high carry before any desk approach; tuck unused left arm

```python
s.act(**{'intent': 'Raise straight high carry before any desk approach; tuck unused left arm', 'left': {'q': [0, 0, 0, 0, 0, 0, 0]}, 'right': {'q': [-1.8, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1038.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116603185251000_5214fd0cea394b7fa38be0198afee87d.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1038.jpg`
Sim seconds: 134.0

```text
[obs #1038 | act=cc34ea5f | sim=134.00s | wall=1021.8s | Raise straight high carry before any desk approach; tuck unused left arm]
  base_odom(sim): rel_xyz=[-3.795, -1.552, -0.003]m rel_yaw=+1.958rad vel=[0.001, -0.0, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-10.841010093688965, -8.488691329956055, 9.662086486816406, -2.2243404388427734]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.00014, 0.0, -0.00017, -0.00044, 6e-05, 0.0, -0.0] q_lag=[-0.0, -0.0, 0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.34, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-3.1653103828430176, -0.14892533421516418, 0.024252712726593018, -1.4755384922027588, 0.024462521076202393, -0.2808239161968231, -0.005551503971219063] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.972, -0.241, 1.138]m fingers=[0.0355, 0.0329]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.973, -0.209, 1.137] pad_end=[0.97, -0.272, 1.139] measured_pinch=[0.972, -0.24, 1.138]m
     close_dir=[0.05, 1.0, -0.04] fing_dir=[0.61, -0.06, -0.79] q=[-1.79986, 0.05003, -0.13064, -0.11978, 0.06516, 1.00016, -0.13967] q_lag=[-0.0, -0.0, 0.001, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[2.641, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.8, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-6.588425636291504, -0.12867915630340576, 0.272469162940979, -3.756056785583496, 0.21380436420440674, -1.5379106998443604, -0.09943989664316177] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"reached","causes":[],"confidence":"measured"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1038_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 24. Advance high-carried fax into cross passage

```python
s.act(**{'intent': 'Advance high-carried fax into cross passage', 'left': None, 'right': None, 'base': {'fwd': 0.45}, 'torso': None, 'seconds': None, 'max_steps': 16, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1078.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116661062550000_d0902553ab1f48dc9d8b6d6e5ba31604.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1078.jpg`
Sim seconds: 139.0

```text
[obs #1078 | act=34d01591 | sim=139.00s | wall=1079.8s | Advance high-carried fax into cross passage]
  base_odom(sim): rel_xyz=[-3.964, -1.136, -0.001]m rel_yaw=+1.958rad vel=[0.028, -0.0, 0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-8.546662330627441, -6.2599029541015625, 6.6699748039245605, -0.47854065895080566]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-1e-05, 0.0, 0.0, -2e-05, -0.0, 0.0, -0.0] q_lag=[0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.006172730587422848, 0.0004030053678434342, 1.311826054006815e-06, -0.0017624055035412312, 2.131302608177066e-06, -0.00021268261480145156, 5.1473551138769835e-05] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.972, -0.241, 1.138]m fingers=[0.0355, 0.0329]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.973, -0.209, 1.137] pad_end=[0.97, -0.272, 1.139] measured_pinch=[0.972, -0.24, 1.138]m
     close_dir=[0.05, 1.0, -0.04] fing_dir=[0.61, -0.06, -0.79] q=[-1.79987, 0.05002, -0.13068, -0.11978, 0.06512, 1.00016, -0.13967] q_lag=[-0.0, -0.0, 0.001, -0.0, -0.0, -0.0, -0.0]rad limit_margins=[2.641, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.8, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.931536674499512, 0.016697704792022705, 0.2776212692260742, -3.4361391067504883, 0.2198408842086792, -1.4538633823394775, -0.11319293826818466] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1078_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 25. Face left carrel with fax already above tabletop

```python
s.act(**{'intent': 'Face left carrel with fax already above tabletop', 'left': None, 'right': None, 'base': {'yaw_deg': 115}, 'torso': None, 'seconds': None, 'max_steps': 28, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1162.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116731051368000_8da645d4abae4637ad8b7a2b4e937b74.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1162.jpg`
Sim seconds: 149.5

```text
[obs #1162 | act=63535e1d | sim=149.50s | wall=1149.8s | Face left carrel with fax already above tabletop]
  base_odom(sim): rel_xyz=[-3.964, -1.136, 0.001]m rel_yaw=-2.322rad vel=[-0.001, -0.001, 0.157] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-14.44438648223877, -13.443098068237305, 28.237577438354492, 63.35150146484375]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[0.00031, 0.0, 0.00037, -0.00062, -1e-05, 0.00019, -2e-05] q_lag=[-0.0, -0.0, -0.0, 0.001, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.34, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.1339365541934967, 0.10567832738161087, 0.0014122165739536285, -0.07288769632577896, 0.0012372536584734917, -0.013448208570480347, 0.002890039002522826] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.97, -0.265, 1.139]m fingers=[0.0345, 0.034]m grip=command=0.0 finger_sum(6.8cm) TRACKING_ERROR(q3=-0.026,q5=-0.059,q7=+0.019)
     pad_start=[0.972, -0.234, 1.134] pad_end=[0.968, -0.296, 1.143] measured_pinch=[0.97, -0.265, 1.139]m
     close_dir=[0.07, 0.99, -0.14] fing_dir=[0.61, -0.15, -0.78] q=[-1.79904, 0.04352, -0.1043, -0.11784, 0.12388, 1.00782, -0.15855] q_lag=[-0.001, 0.006, -0.026, -0.002, -0.059, -0.008, 0.019]rad limit_margins=[2.642, 0.121, 2.242, 0.457, 2.222, 0.029, 1.402]rad min=0.029rad
     q_cmd=[-1.8, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-40.68467712402344, 55.02161407470703, -4.557079315185547, -23.477706909179688, -9.097677230834961, -17.99241828918457, 18.00363540649414] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1162_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 26. Shift toward open carrel edge instead of lowering across divider rail

```python
s.act(**{'intent': 'Shift toward open carrel edge instead of lowering across divider rail', 'left': None, 'right': None, 'base': {'left': -0.32}, 'torso': None, 'seconds': None, 'max_steps': 14, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1190.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116776884144000_1205668339dd4ace9edae906e1ce0e04.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1190.jpg`
Sim seconds: 153.0

```text
[obs #1190 | act=49dbb255 | sim=153.00s | wall=1195.7s | Shift toward open carrel edge instead of lowering across divider rail]
  base_odom(sim): rel_xyz=[-4.197, -0.918, 0.01]m rel_yaw=-2.322rad vel=[0.0, -0.053, -0.002] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[20.054664611816406, 10.622124671936035, -3.2584304809570312, -2.9363417625427246]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-1e-05, 0.0, 1e-05, -1e-05, -0.0, 0.0, -0.0] q_lag=[0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.0007437247550114989, -0.04105542227625847, -0.0001568533480167389, -0.000509752775542438, -0.00014289154205471277, 5.014697308070026e-05, -0.0014622188173234463] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.972, -0.241, 1.138]m fingers=[0.0346, 0.0338]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.973, -0.209, 1.137] pad_end=[0.97, -0.273, 1.14] measured_pinch=[0.972, -0.241, 1.138]m
     close_dir=[0.05, 1.0, -0.04] fing_dir=[0.61, -0.06, -0.79] q=[-1.79988, 0.05003, -0.13114, -0.11979, 0.06437, 1.00006, -0.1396] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.001, -0.0, -0.0]rad limit_margins=[2.641, 0.114, 2.215, 0.459, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.8, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-5.880059719085693, -0.3248884677886963, 0.33893847465515137, -3.4879231452941895, 0.3041079044342041, -1.525923728942871, -0.22171680629253387] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1190_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 27. Back off foot pressure before lowering retained fax

```python
s.act(**{'intent': 'Back off foot pressure before lowering retained fax', 'left': None, 'right': None, 'base': {'fwd': -0.08}, 'torso': None, 'seconds': None, 'max_steps': 6, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1198.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116792099082000_3877783f2b9748c88d84e897911660c0.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1198.jpg`
Sim seconds: 154.0

```text
[obs #1198 | act=1fd6b2b3 | sim=154.00s | wall=1210.5s | Back off foot pressure before lowering retained fax]
  base_odom(sim): rel_xyz=[-4.143, -0.861, -0.001]m rel_yaw=-2.322rad vel=[-0.062, -0.001, 0.002] | torso=[0.84, -1.006, -0.42, 0.0] err=[-0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-10.4210786819458, -7.5345306396484375, 7.567949295043945, -1.8281819820404053]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-2e-05, 0.0, 0.0, -0.0, 0.0, -0.0, -0.0] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, 0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.048526469618082047, -0.013460799120366573, -0.00015183910727500916, 0.011881972663104534, -0.00011005229316651821, 0.0010719135170802474, -8.891646575648338e-05] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.972, -0.241, 1.138]m fingers=[0.0346, 0.0337]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.973, -0.209, 1.137] pad_end=[0.97, -0.272, 1.139] measured_pinch=[0.972, -0.241, 1.138]m
     close_dir=[0.05, 1.0, -0.04] fing_dir=[0.61, -0.06, -0.79] q=[-1.79987, 0.05004, -0.13169, -0.1198, 0.06357, 0.99998, -0.1396] q_lag=[-0.0, -0.0, 0.002, -0.0, 0.001, 0.0, -0.0]rad limit_margins=[2.641, 0.114, 2.215, 0.459, 2.283, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.8, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-6.284458160400391, -1.1939564943313599, 0.5242583751678467, -3.712512254714966, 0.5424884557723999, -1.5094685554504395, -0.5100786685943604] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1198_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 28. Lower fax over open tabletop without crossing divider

```python
s.act(**{'intent': 'Lower fax over open tabletop without crossing divider', 'left': None, 'right': {'q': [-1.45, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1203.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116795544138000_a1aa8e37f7a1426994a8e39916463d11.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1203.jpg`
Sim seconds: 154.73333333333332

```text
[obs #1203 | act=7669cb15 | sim=154.73s | wall=1214.3s | Lower fax over open tabletop without crossing divider]
  base_odom(sim): rel_xyz=[-4.143, -0.861, -0.001]m rel_yaw=-2.322rad vel=[0.001, -0.001, 0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-72.30805206298828, -49.015625, 51.558773040771484, 4.388566970825195]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-0.0, 0.0, 8e-05, -0.00016, -1e-05, 4e-05, -2e-05] q_lag=[0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.5998995900154114, 0.004841669462621212, 0.0010440722107887268, 0.015636427327990532, 0.0014330800622701645, -0.025214793160557747, 0.0016189482994377613] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.875, -0.241, 0.907]m fingers=[0.0346, 0.0338]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.876, -0.209, 0.905] pad_end=[0.874, -0.273, 0.908] measured_pinch=[0.875, -0.241, 0.907]m
     close_dir=[0.03, 1.0, -0.05] fing_dir=[0.31, -0.06, -0.95] q=[-1.45016, 0.05002, -0.13165, -0.11902, 0.06465, 1.0003, -0.13959] q_lag=[0.0, -0.0, 0.002, -0.001, 0.0, -0.0, -0.0]rad limit_margins=[2.749, 0.114, 2.215, 0.458, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.45, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-45.04560089111328, 3.090017318725586, 0.8051586151123047, -22.790767669677734, 0.23865604400634766, -7.325151443481445, 0.41268253326416016] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1203_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 29. Set fax down to measured tabletop height

```python
s.act(**{'intent': 'Set fax down to measured tabletop height', 'left': None, 'right': {'q': [-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1207.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116812727334000_c6ad52c87fee4969be2f31ee2ff891d8.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1207.jpg`
Sim seconds: 155.23333333333332

```text
[obs #1207 | act=f5ba1b8d | sim=155.23s | wall=1231.5s | Set fax down to measured tabletop height]
  base_odom(sim): rel_xyz=[-4.143, -0.861, -0.001]m rel_yaw=-2.322rad vel=[0.001, 0.001, -0.0] | torso=[0.84, -1.006, -0.42, -0.0] err=[-0.0, -0.0, 0.0, 0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-40.71609878540039, -26.671545028686523, 22.825130462646484, 0.5966873168945312]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, -0.0] fing_dir=[-0.25, -0.0, -0.97] q=[-1e-05, 0.0, 4e-05, -7e-05, -0.0, 1e-05, -1e-05] q_lag=[0.0, -0.0, -0.0, 0.0, 0.0, -0.0, 0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[1.0525075197219849, 0.011357896961271763, -0.0029424279928207397, 0.23484386503696442, -0.002528514713048935, 0.01622943952679634, 0.0005898135132156312] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.838, -0.241, 0.854]m fingers=[0.0346, 0.0338]m grip=command=0.0 finger_sum(6.8cm)
     pad_start=[0.839, -0.21, 0.852] pad_end=[0.837, -0.273, 0.856] measured_pinch=[0.838, -0.241, 0.854]m
     close_dir=[0.02, 1.0, -0.06] fing_dir=[0.22, -0.06, -0.97] q=[-1.35989, 0.05002, -0.13111, -0.11962, 0.06467, 1.00014, -0.13963] q_lag=[-0.0, -0.0, 0.001, -0.0, 0.0, -0.0, -0.0]rad limit_margins=[2.659, 0.114, 2.215, 0.459, 2.282, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-14.849706649780273, 0.6434891223907471, 0.4602193832397461, -7.369594573974609, 0.314727783203125, -2.1186509132385254, -0.1798572838306427] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1207_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 30. Release fax onto carrel

```python
s.act(**{'intent': 'Release fax onto carrel', 'left': None, 'right': {'grip': 1}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 4, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1211.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116824826530000_acec8fa765574f1c8e3520b91c1e4c61.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1211.jpg`
Sim seconds: 155.73333333333332

```text
[obs #1211 | act=e7b7f4b7 | sim=155.73s | wall=1243.6s | Release fax onto carrel]
  base_odom(sim): rel_xyz=[-4.143, -0.861, -0.001]m rel_yaw=-2.322rad vel=[-0.0, -0.001, -0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, -0.0, 0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-0.03929932415485382, 0.03517048805952072, 0.017203789204359055, -0.028959520161151886]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-0.004734826274216175, -0.01404552347958088, -0.00010859279427677393, -0.002249713521450758, -1.4845572877675295e-06, -0.0005671859253197908, -0.0001877680915640667] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.838, -0.242, 0.854]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.839, -0.194, 0.852] pad_end=[0.837, -0.289, 0.857] measured_pinch=[0.838, -0.242, 0.854]m
     close_dir=[0.02, 1.0, -0.06] fing_dir=[0.22, -0.06, -0.97] q=[-1.36, 0.05, -0.12999, -0.12, 0.06501, 1.0, -0.14] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[2.659, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.36, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-0.008404392749071121, -0.0218779556453228, -0.0006282317917793989, -0.00321116391569376, -3.6892539355903864e-05, -0.0001949903671629727, -8.502554555889219e-05] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1211_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 31. Withdraw hand to verify independent tabletop support

```python
s.act(**{'intent': 'Withdraw hand to verify independent tabletop support', 'left': None, 'right': {'q': [-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14]}, 'base': None, 'torso': None, 'seconds': None, 'max_steps': 8, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1216.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116828120745000_2862c3f2f9f544bba5027593ac1248a0.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1216.jpg`
Sim seconds: 156.36666666666667

```text
[obs #1216 | act=e7b363f9 | sim=156.37s | wall=1247.0s | Withdraw hand to verify independent tabletop support]
  base_odom(sim): rel_xyz=[-4.143, -0.861, -0.001]m rel_yaw=-2.322rad vel=[-0.001, -0.0, -0.0] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[65.01074981689453, 41.54181671142578, -31.118770599365234, 2.679593086242676]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[3e-05, -0.0, -1e-05, 4e-05, 0.0, -1e-05, 1e-05] q_lag=[-0.0, 0.0, 0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.164, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.164rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[-1.7184360027313232, 0.27733519673347473, 0.006319701671600342, -0.3605033755302429, 0.0049046725034713745, -0.01946883276104927, 0.008971101604402065] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.242, 1.035]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.942, -0.195, 1.033] pad_end=[0.938, -0.289, 1.038] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.05] fing_dir=[0.49, -0.06, -0.87] q=[-1.64948, 0.04998, -0.12906, -0.12012, 0.06606, 1.00007, -0.14] q_lag=[-0.001, 0.0, -0.001, 0.0, -0.001, -0.0, 0.0]rad limit_margins=[2.791, 0.115, 2.217, 0.459, 2.28, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[14.285154342651367, 0.8405792713165283, -0.3120999336242676, 5.507002830505371, -0.27742600440979004, 0.661298394203186, 0.28437739610671997] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"reached","causes":[],"confidence":"measured"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1216_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```

## 32. Verify powered fax remains stable unsupported by robot

```python
s.act(**{'intent': 'Verify powered fax remains stable unsupported by robot', 'left': None, 'right': None, 'base': None, 'torso': None, 'seconds': 2, 'max_steps': 1, 'position_tol': 0.005, 'rotation_tol': 0.035, 'accept_partial': False})
```
Result: tolerance_reached; observation 1229.

Receipt: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116834862731000_cd101e4801b0437a8bcfd63600e5c184.json`
Image: `/tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1229.jpg`
Sim seconds: 158.36666666666667

```text
[obs #1229 | act=8916806b | sim=158.37s | wall=1253.7s | Verify powered fax remains stable unsupported by robot]
  base_odom(sim): rel_xyz=[-4.143, -0.861, -0.001]m rel_yaw=-2.322rad vel=[0.0, 0.001, 0.001] | torso=[0.84, -1.006, -0.42, 0.0] err=[0.0, 0.0, -0.0, -0.0]
  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.
  torso_cmd=[0.84, -1.00609, -0.42, 0.0] effort_Nm=[-0.292320191860199, -0.06953033059835434, 0.059104859828948975, -0.06570732593536377]
  L: rigid_TCP(fwd,left,up)=[0.072, 0.252, 0.532]m fingers=[0.0, 0.0]m grip=command=0.0 finger_sum(0.0cm)
     pad_start=[0.072, 0.249, 0.532] pad_end=[0.072, 0.254, 0.532] measured_pinch=[0.072, 0.252, 0.532]m
     close_dir=[-0.0, 1.0, 0.0] fing_dir=[-0.25, 0.0, -0.97] q=[-0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0] q_lag=[0.0, -0.0, -0.0, -0.0, -0.0, 0.0, -0.0]rad limit_margins=[1.299, 0.165, 2.346, 0.339, 2.346, 1.037, 1.561]rad min=0.165rad
     q_cmd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] effort_Nm=[0.051392823457717896, -0.18725164234638214, -0.001660376787185669, 0.009097752161324024, -0.0013276329264044762, -7.057952461764216e-05, -0.008286422118544579] (PhysX measured joint effort; not contact force)
  R: rigid_TCP(fwd,left,up)=[0.94, -0.242, 1.035]m fingers=[0.05, 0.05]m grip=command=1.0 finger_sum(10.0cm)
     pad_start=[0.942, -0.194, 1.033] pad_end=[0.939, -0.289, 1.038] measured_pinch=[0.94, -0.242, 1.035]m
     close_dir=[0.04, 1.0, -0.05] fing_dir=[0.49, -0.06, -0.87] q=[-1.65, 0.05, -0.12999, -0.12, 0.06501, 1.0, -0.14] q_lag=[0.0, -0.0, -0.0, 0.0, -0.0, -0.0, 0.0]rad limit_margins=[2.791, 0.114, 2.216, 0.459, 2.281, 0.037, 1.421]rad min=0.037rad
     q_cmd=[-1.65, 0.05, -0.13, -0.12, 0.065, 1.0, -0.14] effort_Nm=[-0.028887175023555756, -0.15832461416721344, -0.00907604955136776, -0.011435216292738914, -0.0034021898172795773, -0.000377542688511312, 0.002541538095101714] (PhysX measured joint effort; not contact force)
  diagnosis={"left":{"status":"not_targeted","causes":[],"confidence":"none"},"right":{"status":"not_targeted","causes":[],"confidence":"none"}}
  status=tolerance_reached fault=None uncertain=False pending=[]
  depth saved: /tmp/fax-run-008_obs/fax-run-008-v4-a03/obs_1229_depth.npz -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN
```
