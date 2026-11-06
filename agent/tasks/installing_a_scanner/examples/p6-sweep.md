# Protocol6 sweep: persistent translation/rotation, not acquisition

Attempt `practice-restore-a04-before-preparation-5f004a05c298459c9006f4ea8351a621`, restored from `a04-before-preparation` (saved in original a04 at sim14.133s). Own scanner slot only. [Full endpoint proprio and image/depth pointers](p6-sweep-evidence.json).

IMPORTANT temporary protocol6 workaround from lead: after EVERY act call below, call `s.observe()` and use its RGB/depth for decisions. Act-return RGB can be stale. Observe IDs1/3/5/7/9/11/13/15 are the fresh before/after evidence. Never run the sequence blindly without inspecting results.

Snapshot starts base estimated `[.547,-.502,0]`, yaw−1.243, torso commanded `[1.15,-.67,-.02,0]`; left q `[-.4,0,0,-1.9,0,0,0]`, right q `[-.6,0,0,-1.9,0,0,0]`; both open. Snapshot restore returns a new practice attempt, not a clean independent full episode. Odom now integrated proprio estimate, not absolute scene pose.

Exact ordered calls, with a fresh observe after EACH:
```python
s.restore('a04-before-preparation')
s.act(intent='Improve rear-edge reach with clear elevated hands',base={'fwd':.28})
s.act(intent='Use bent-elbow sweep approach to avoid straight-arm singular branch',right={'q':[-1.55108,-.25594,.73343,-1.39238,-1.75775,.91743,-1.33985]})
s.act(intent='Stage bent-elbow closed hand above rear edge',right={'to':[1.30,-.34,.96],'grip':0})
s.act(intent='Close sweeping fingers after staging',right={'grip':0})
s.act(intent='Lower bent-elbow hand behind scanner for sweep',right={'to':[1.30,-.34,.80]})
s.act(intent='Sweep scanner rear edge toward robot',right={'to':[1.08,-.34,.82]})
s.act(intent='Withdraw above scanner after preparation sweep',right={'to':[1.14,-.25,1.0]})
```
Staging returned stalled although arm within tolerance and no pose pending; fingers remained OPEN, so separate close was required and visibly executed. Lowering stalled at TCP `[1.302,-.340,.813]`, closed fingers, rather than requested .800Z. Sweep explicitly replaced that target, reached `[1.080,-.340,.820]`. Withdrawal reached `[1.142,-.251,1.000]`; scanner remained on table, visibly translated/rotated toward near-right area after withdrawal. No retained grasp, no placement, switch remains red.

Geometry reference before snapshot (original a04 obs9, head `(u,v)`): `(480,260)`→`[1.485717,-.315895,.824226]`, `(450,280)`→`[1.414580,-.226219,.810461]`, `(560,300)`→`[1.303849,-.441906,.832603]`, `(420,400)`→`[1.089393,-.115823,.759083]`. Recompute after moving; these are NOT current body coordinates.

Result posture obs15: base estimate `[.635,-.761,0]`, yaw−1.247; torso `[1.15,-.67,-.02,0]`; left remains open/parked; right q `[-1.78604,-.67230,1.03175,-1.74150,-2.24063,.68513,-1.44497]`, closed; pad references `[1.142,-.254,1.000]` and `[1.142,-.248,1.000]`. Full precision state is in JSON.

## Follow-on second sweep (same restored attempt)
Exact ordered calls, again fresh observe after EACH act:
```python
s.act(intent='Face displaced scanner for edge measurement',base={'yaw_deg':-20,'fwd':-.12})
s.snapshot('a04-after-first-sweep')
s.act(intent='Center sweeping hand behind scanner long axis',right={'to':[1.28,-.16,.96]})
s.act(intent='Lower behind centered scanner rear face',right={'to':[1.28,-.16,.80]})
s.act(intent='Pull centered rear edge toward near table edge',right={'to':[1.00,-.16,.815]})
s.act(intent='Withdraw from rotated scanner without continuing surface load',right={'to':[1.15,-.2,1.0]})
s.snapshot('a04-second-sweep')
```
Fresh obs17 before,21 contact,23 sweep,25 withdrawal (31.3sim). Scanner rotated counterclockwise and moved left/near, remains supported. Not yet adequate underside exposure, no grasp. Latest right TCP `[1.150,-.201,1.000]`, closed; base estimate `[.598,-.651,0]`, yaw−1.587. Full state and images in evidence JSON. Before second sweep head XYZ obs17 `(440,320)`→`[1.229088,-.161282,.830456]`, `(460,450)`→`[.961768,-.147590,.813241]`, tabletop `(450,590)`→`[.800762,-.112188,.764842]`, `(420,620)`→`[.772440,-.071299,.764838]`. Object motion was mainly rotation, not the requested 28cm straight translation: do not equate hand endpoint displacement to object displacement.

Earlier original-a04 failure: far reach `[1.43,-.32,.805]` stopped at `[1.327,-.306,.842]`; withdrawal through near-straight elbow produced major unwanted joint-branch changes. Restoring snapshot and explicitly selecting a previously measured bent-elbow posture avoided that branch and enabled this sweep. This is a useful initial posture, not a universal grasp recipe.
