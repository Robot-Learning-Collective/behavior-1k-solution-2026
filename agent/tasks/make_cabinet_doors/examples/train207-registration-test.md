# Seen-TRAIN207 post-release registration test

Attempt `cabinet-train207-registration-002`, matching source `e87cfaa129cc864da45ed45eba1a280277d3ae0a`, namespace `cabinet-run-023-p6-d689c6`. Authorized by lead848 after preserving the first held-out result. This is **learning on now-seen207**, not a second zero-shot/frozen evaluation. Native reset; snapshots saved but **no restore used** in this attempt. Intermediate native practice feedback was explicitly permitted.

## Result

[Native finish](../train207-registration-002-finish.json): **attached=false, Q0**, step3782,126.06666666666666sim s,1852.4042191229964task-wall s. Native budget5163ticks was not exceeded (1381ticks remaining), but this unbounded, studied, feedback-assisted practice is not qualified evaluation. No crash or uncertain action; old TRAIN10 attach-joint crash remains unresolved and unexercised.

The three-demo study in NOTES motivated a distinct release→withdraw→open-hand registration phase. **That implemented hypothesis did not produce attachment.** It does not establish that all registration corrections fail, nor that orientation/contact location was correct.

| Endpoint | Native step / sim s | Native attachment |
|---|---:|---|
|65: release|3521 /117.3667|false/Q0|
|66: fully withdraw open pads|3542 /118.0667|false/Q0|
|71: first along-axis approach|3738 /124.6|false/Q0|
|72: second small along/down nudge|3759 /125.3|false/Q0|
|74: cancel preload and withdraw|3782 /126.0667|false/Q0|

Feedback JSONs live in run root as `train207-registration-{release,withdraw,first-nudge,second-nudge,after-nudges}-feedback.json`. These are training feedback, not policy geometry/contact information. All observations/actions are preserved in `control-action-results.jsonl` and own cache under the exact attempt.

## Setup and changed actions

Acquisition, carry and far-rim tipping repeated. At obs33 the retained panel was raised above nearby furniture. Alternate wrist quarter/half/three-quarter/qu/midpoint/qh produced handle-up posture at63.13sim s. Placement workspace still required correction: guarded right sidestep stopped after about.34m, with `base_velocity_tracking_mismatch`; no blind replay. Turned to inspect the occupied corridor, then approached the cabinet through the open aisle.

Right pads grasped a fresh measured short rim. Lift partially moved it but generated q4lag~.099 and wrist-limit overshoot; canceled to measured bounded q (q5=1.03), then two inspected backward.4m moves relocated the cabinet. Released with far edge floor-supported, raised both arms, and lateral.5+.3m plus30deg heading change reached useful left workspace. This is not a universal route or collision-free claim.

### Fresh alignment

Obs61 head RGBD (BODY metres, manually selected public patches):

|Corner|Door|Cabinet|
|---|---|---|
|near-left D|[.51755,.40799,.59848]|[.55566,.34768,.24774]|
|near-right C|[.65075,.20094,.59856]|[.67565,.13172,.24776]|
|far-right B|[.97101,.41730,.59082]|[1.04961,.36791,.24340]|

Long axes agreed approximately32deg. Base `[+.038 forward,−.060 left]` aligned near-corner projections. This geometry was approximate, not native attachment-frame alignment. Saved `train207-aligned-before-registration` before descending; never restored during this test.

Coupled approach at obs63: torso `[1.75,-2.65,-1.2,0]`, L q `[-.25627,-.11114,.22195,-.83873,1.75964,-.30687,-.84591]`, reached TCP[.551,.360,.355]. Final obs64: torso `[1.744,-2.75,-1.3,0]`, L q `[-.35199,-.09401,.23135,-.67898,1.772,-.30012,-.82548]`, TCP[.550,.360,.300], F[.84,.54,−.08]. Left grip remained0; right open/raised.

### Separate release / withdrawal

- Obs65 `left={'grip':1}`: fingers opened to.10m; native false.
- Obs66 `left={'fwd':-.10,'left':-.064}`: open hand withdrew along negative measured long axis to TCP[.450,.300,.300]; panel settled visibly flush; native still false.
- Obs67 raised empty hand.15m. Obs68 reoriented toward downward fingers;3s tick cap left q5~.157rad short, **not execution uncertainty**. A new inspected pose goal at69 reached TCP[.55,.283,.38],Fdown,C[.54,−.84,0], with.111rad minimum margin. No unattended replay.
- Door public plane measured~.256m; near short-edge center estimated[.575,.299]. Obs70 lowered open downward pads.13m to TCP[.549,.283,.251], just outside that edge.
- Obs71 moved `[+.021 forward,+.0135 left]` (2.5cm along axis). Reached with q5lag−.019; false/Q0.
- Obs72 moved `[+.0126 forward,+.0081 left,−.004 up]` (1.5cm along axis /4mm down). Stalled near TCP[.581,.299,.248], q5lag−.023. False/Q0. Effort/lag is not contact-force proof or proof that only the door, rather than cabinet too, was moved.
- Obs73 replaced missed target with measured q. Obs74 withdrew `[−.017 forward,−.011 left,+.08 up]`, removing preload; false/Q0 persisted.

Saved `train207-postregistration-unattached` while active, then admin_finished. This snapshot is specific to current instance/source and is not evaluation material.

## Limits and next discriminating question

This test rejects **withdrawal plus this particular near-short-center along-axis/downward nudge as sufficient**. It does not identify the attachment failure cause. Remaining candidates include wrong mating-edge/180deg registration, small planar offset, or contact at a different location than the human adjustment. Do not escalate pressure or repeat stalled pushes merely because seating looks flush. Compare actual visible hinge/handle relationship and human near-edge contact point before the next changed manipulation. No controller/backend repair is authorized or implied.

Original `heldout-train207-first-001-finish.json` remains untouched: false/Q0,5277ticks/175.9sim s,2495.6766wall s,114ticks over budget. Historical TRAIN10 successes and attach-joint crash remain separate evidence.
