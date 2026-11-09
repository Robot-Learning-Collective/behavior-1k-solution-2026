# a03: safe pregrasp branch recovery, not acquisition

Attempt `scanner-run-007-v4-a03`, protocol4 run-local client. [Endpoint evidence](a03-endpoint-evidence.json) contains every saved endpoint through obs1149: full base/torso/arm/finger/pad proprioception, last emitted low-level action, and before/contact/after image/depth/receipt paths. `submitted_action` is the last emitted low-level chunk, NOT the complete high-level call; do not replay it as a complete trajectory.

## Successful supporting substep: recover usable vertical-jaw arm branch

Prerequisite at obs997: base rel `[.493,-.468,0]`, yaw−1.271rad; torso `[.84,-.669,-.42,0]`; left q `[-.4,0,0,-1.9,0,0,0]`, open. Right open at `[.659,-.429,.837]` with an unfavorable joint-limit branch. Both grip intents initialized. Scanner remains on desk. Clear floor behind robot verified visually. Never apply this unconditionally in a different scene.

Exact executed calls, in order:
```python
s.act(intent='Retreat for safe right-arm joint-branch change away from scanner',base={'fwd':-.30},max_steps=20)
s.act(intent='Use measured previously reached vertical-jaw posture in free space',right={'q':[-.01207,-.52959,.68534,-1.34945,-2.31305,-.43568,1.16463]},max_steps=24)
s.act(intent='Return to pregrasp base pose with jaws ahead of scanner',base={'fwd':.30},max_steps=20)
```
Before obs997, retreat1025, joint recovery1055, after1083. All three calls tolerance_reached. After: right TCP `[.660,-.300,.801]`; pads `[.660,-.300,.848]` and `[.660,-.300,.753]`; fingers .05/.05; finger_dir +X, close_dir +Z; base returned within ~1.4mm. Scanner remained visually supported. This is navigation/arm recovery success, not a scanner grasp.

## Short rear-edge preparation sequence before recovery

Starting obs678: base `[.537,-.610,0]`, yaw−1.271; torso `[1,-.67,-.15,0]`, left parked as above; right closed with diagonal forward/down fingers, withdrawn `[1.02,-.20,1.02]`.
```python
s.act(intent='Position rear-edge center for 8cm preparation sweep',right={'to':[1.04,-.34,.96]},max_steps=16)
s.act(intent='Lower behind rear edge center',right={'to':[1.04,-.34,.80]},max_steps=12)
s.act(intent='Short sweep to expose front edge without losing support',right={'to':[.94,-.34,.81]},max_steps=12)
s.act(intent='Withdraw vertically after edge exposure',right={'to':[1.0,-.34,1.05]},max_steps=16)
```
Endpoints700/735/751/781; compare image pointers in evidence. Scanner remained on table after withdrawal; adequate underside clearance was NOT established. Earlier sweeps are preserved as endpoint evidence but their full high-level calls are not reconstructed from last-chunk values.

Key pre-sweep head XYZ at obs678 `(u,v)` in BODY metres: `(500,520)`→`[.81451,-.20523,.82760]`, `(640,600)`→`[.72251,-.35399,.82578]`, `(520,580)`→`[.75031,-.23597,.76483]`, `(600,610)`→`[.71613,-.33544,.76482]`, `(490,430)`→`[.96033,-.23186,.83008]`.

## Failed lip insertion: preserve, do not label grasp

After recovery:
```python
s.act(intent='Align vertical jaws with scanner front lip just above table',right={'to':[.78,-.325,.818]},max_steps=16)
s.act(intent='Insert a short distance over scanner front lip',right={'to':[.817,-.325,.824]},max_steps=10)
s.act(intent='Close vertical jaws on front lip',right={'grip':0},max_steps=8)
s.act(intent='Test scanner retention with small vertical lift',right={'to':[.817,-.325,.90]},max_steps=12)
```
Obs1110 alignment reached, lower finger deflected to .0351m despite open command. Insertion obs1139 no_progress, actual TCP `[.798,-.290,.862]`; close returned prerequisite_not_met without new simulation or closure. Final obs1149 hand reached `[.817,-.325,.900]`, fingers stayed .05/.05; scanner stayed on table. Thus the last intent says retention test but no grip had executed: NOT a failed closed-grasp retention experiment. Do not chain dependent calls without inspecting their results.

Head XYZ obs997: `(540,470)`→`[.818475,-.331651,.764841]` tabletop; `(560,465)`→`[.809548,-.333988,.823350]` scanner; `(500,440)`→`[.856746,-.250552,.813289]`; `(570,490)`→`[.783779,-.372702,.764835]` tabletop. These support insufficient overhang for a clean vertical-jaw underside insertion. No switch activation, placement or task completion in a03 yet.
