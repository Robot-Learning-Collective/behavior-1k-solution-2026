# TRAIN207 first held-out full-reset attempt — failed attachment

Attempt `cabinet-train207-first-001`, source `e87cfaa129cc864da45ed45eba1a280277d3ae0a`, cache namespace `cabinet-run-023-p6-d689c6`. Switching `practice_client.py` import verified before first reset; reset printed SLOT_SWITCH / ZERO_SHOT. No calls to crashed TRAIN10. No demo study, snapshots/restores or intermediate feedback during this attempt. Existing NOTES procedure/examples and matching public robot FK/IK helper were used; every physical endpoint was inspected.

**Native finish: attached=false, Q=0, 5277 ticks / 175.9 sim seconds / 2495.676562425004 task-wall seconds.** Original budget 5163 ticks was exceeded by114ticks/3.8s; unbounded practice allowed continuation, not evaluation qualification. Backend-reported setup (~497s) is separate; actual reset-call wall latency was not independently timed. Final action image looked seated/flush, but that is NOT attachment. No runtime crash or uncertain execution occurred on this instance. Full finish: [`../heldout-train207-first-001-finish.json`](../heldout-train207-first-001-finish.json).

## What transferred and what did not

- Fresh near-corner top pinch acquired the upright door. Measured top approximately .4513m; partial shallow insertion was replaced with measured joints before closing. Bounded lift raised retained edge to about .578m. Door remained in left grip until final release.
- Cabinet opening was on the far side from initial approach. Right downward fingers drew the far upper rim with separate .06m backward base increments. Visible top-plane normals progressed through approximately[-.080,.008,.997],[-.174,.013,.985],[-.264,.016,.964],[-.354,.018,.935]. A guarded draw was not replayed. Measured-q cancellation plus .12m left separation allowed the cabinet to settle open-face-up (obs49,94.233sim s); rim depth around .2478m. This is an alternate tipping route, not a universal force strategy.
- Retained alternate-wrist path transferred: q0→quarter/half/three-quarter→qu→midpoint(qu,qh)→qh. Panel visibly horizontal/handle-up at obs60/105.667sim s. Numerical reference postures remain in existing reorientation example.
- **Major inefficiency:** attempted placement-side navigation around table/chairs repeatedly met velocity-tracking guards. Alternate routes were inspected, not automatic guard replays. Offline cross-body IK searches found no candidate in tested seeds; not proof of unreachability. Much of this could have been avoided by planning the final left-arm placement workspace before tipping/carrying.
- Cabinet was then relocated by right near-rim pinch and shallow lift/drag while the door remained in the left hand. Right upward Cartesian lift hit a wrist bound and elbow lag; replaced with bounded posture / measured-q cancellation, not continued pushing. This preserved retention but did NOT yield task success.
- Fresh mating-corner geometry, rather than historical base offsets, drove final yaw/translation and coupled seating. Native attached still false; hinge-side/registration/tilt/contact sequence remains unresolved. Do not promote apparent flush seating as the criterion.

## Relocation observations (not a task macro)

Right rim was measured around BODY[.54,-.48,.2477], with closing axis[.79,.61,0] across the short-end wall and fingers down. Shallow pinch at torso[1.744,-2.75,-1.3,0], right q[-.90689,-.38645,-.24012,-.36611,-.90669,.94003,-.61635], TCP[.54,-.48,.24], then right grip0. Cabinet near end visibly rose, but whole-body lift was not demonstrated.

With elbow preload cancelled, separate inspected base moves[-.2fwd,+.3left],[-.4fwd],[-.4fwd,+.5left] dragged the cabinet toward open floor. Door briefly contacted dresser-side space (left q3lag .155); cancelled measured q and compacted its horizontal posture rather than continuing preload. Compact left q[.73904,.06348,-.08539,-1.55326,1.63594,-.08407,-.91245] at torso[1.7,-2.5,-.95,0] placed TCP around[.30,.25,.50]. Right grip opened with cabinet's far edge floor-supported; after raising torso/right arm, two .4m right sidesteps finally reached a clear placement lane. This relocation cost too much native time and should not be blindly reproduced.

## Final fresh geometry and command evidence

Obs96 public head-depth samples (BODY metres):

| Feature | XYZ |
|---|---|
| Door near-left D | [.5634,.4754,.5841] |
| Door near-right C | [.7110,.2846,.5843] |
| Door far-left A | [.8628,.7503,.5798] |
| Door far-right B | [1.0210,.5633,.5799] |
| Cabinet far-left rim | [.7982,.6328,.2462] |
| Cabinet far-right rim | [.9286,.4214,.2472] |
| Cabinet near-right rim | [.5569,.1816,.2472] |

Cabinet long axis approximately[.842,.540,0], versus door's initial diagonal approximately[.74,.67,0]. Adjusted door about .13m back/.08m right and10°clockwise using FK/IK and inspected joint target, without moving base:

- Alignment: torso[1.4505,-2.227,-.818,0], L q[.27069,-.13519,.18464,-1.38585,1.69227,-.34098,-.54438]. Obs97 near door D[.4299,.3990,.5810], C[.5577,.1892,.5855]; far samples[.7816,.6274,.5654] and[.9115,.4252,.5696]. Near corners within about1cm of rim projection; samples are small public RGBD patches, not privileged object geometry.
- First descent: torso[1.75,-2.65,-1.2,0], L q[.04842,-.1176,.22767,-1.03287,1.80673,-.21743,-.93466]. Obs98 TCP[.435,.369,.355],175.5sim s.
- Final descent: torso[1.744,-2.75,-1.3,0], L q[-.02539,-.10481,.22741,-.93803,1.80926,-.22369,-.87151]. Obs99 TCP[.435,.369,.301], F[.84,.54,-.08],175.667sim s. Returned reached, not task success.
- Release: L grip1, obs100/5277ticks/175.9sim s. Apparent flush seating; finish subsequently returned false/Q0. No further motion after finish.

Last endpoint receipt: `cabinet-train207-first-001/receipt_01792178765038640000_697e97a72d5c4d4c9114678f5a228500.json`. All public action results remain in run `control-action-results.jsonl` and the named cache namespace.

## Next study target

Compare attachment/placement and neighbouring segments across 2–3 DIFFERENT human episodes, using time-aligned measured proprioception AND recorded actions with all three cameras. Determine mating/hinge-edge orientation and final contact/release/withdrawal differences. Compare navigation/pre-positioning before tipping. Do not assume the native failure was caused by one particular geometric error; current evidence does not identify it. Any further practice requires an authorized active attempt; this one is finished. One honest full-reset result is sufficient for the requested checkpoint/freeze handoff; no success gate.
