# Seen207 direct initial-handle trial005 — failed before grasp

`cabinet-train207-direct-handle-005` deliberately tested whether a directly useful initial handle grasp could remove the later broad-support/regrasp sequence. Native reset, no snapshots/restores. Finished **false/Q0 at321ticks/10.7sim s/191.4828866500029task-wall s** after3 execution-certain actions. The panel fell during a combined close-range torso/arm reposition, before grip close or any retention claim. This was an intentionally closed component failure, not an unexpected attempt end or runtime hold. [Native finish](../train207-direct-handle-005-finish.json).

Exact requested sequence:
```python
s.act(left={'preset':'ready','grip':1},right={'preset':'ready','grip':1},base={'yaw_deg':-40},seconds=5)
s.act(base={'fwd':1.05,'left':-.43},seconds=7)
s.act(torso={'q':[1.744,-2.75,-1.3,0]},left={'q':[-.79885,.23545,-.22258,-1.00292,-1.09656,1.0072,-1.38177]},seconds=3)
```

Before final action, public handle~[.723,.214,.235]BODY, door upright/top~.45. Candidate endpoint TCP[.581,.310,.310],Fdown,C[.57,.82,0], wrist margin.03rad. Offline interpolated TCP stayed outward of the door and reached its target, yet **whole-hand/arm swept-volume clearance was not checked**. Public endpoint showed panel lying flat, sampled top.011–.020m. This is a counterexample to treating a clear TCP path or reached pose as collision-safe. Exact contacting link/time is unknown; do not label it a confirmed pad/palm force event.

Multiple offline searches for horizontal fingers at low handle height found no seed solution in the tested postures; that does not prove global unreachability. An offline torso1.9rad candidate was outside supplied upper1.8326rad and was never executed. Subsequent downward-finger candidate was within bounds but failed physically as above.

Failure triggered a renewed three-demo initial-pickup study (not another blind retry). See NOTES human-vs-own table. Changed test: stage the crouch/reorientation while FAR from the standing panel, then approach the measured handle in small translation steps with a slanted downward/outward hand geometry; retain top-edge acquisition as the demonstrated fallback. Neither direct handle acquisition nor its claimed efficiency is yet established.
