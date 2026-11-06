# Recovered a11: first acquisition; native goal FAILED

New SETUP-bound r3 client, instance1054ef. Reset `scanner-run-007-recovered-a11`; saved `a11-native-start` before motion. No restores. Saved intermediate preparation/retention snapshots: `a11-before-final-draw`, `a11-overhang-candidate`, `a11-retained-first-grasp`.

Finished86.1sim seconds /2583steps /608.431191409wall. Native practice feedback: toggled_on=true, nextto=false, Q=.5, success=false. Clean pair count remains0. Visual proximity to laptop was NOT native nextto success.

Preparation: standard navigation from a10; yaw-20, original sweep seed, base left.20/fwd.15, closed right stage[1.27,-.18,.96]→[1.27,-.18,.80]; base draws-.35,-.25; lift.98. Reengage/draw-.08/lift; reengage/draw-.10/lift. These dragged top then slipped off, with scanner rotation. Recenter base fwd.20,left-.12; stage[1.34,-.18,.96]→.80, draw-.15, lift.98; reengage/draw-.08/lift, then-.05/lift. Repeated 1.34 low targets were IK/tracking limited around1.316–1.32 and Z.81. Preparation works in this one case, not a validated repeatable recipe.

At obs036 head scanner(500,347)=[1.1593393,-.26209697,.82511294]; tabletop edge-adjacent(420,333)=[1.2599671,-.13493828,.7649148], fascia(420,337)=[1.2566723,-.13587838,.75568277]. Other side fascia(580,370)=[1.1800824,-.47145012,.73224616]. Approx local edge interpolation supports several cm positive overhang, uncertainty from differing sampled heights/lateral positions retained.

Retreat-.30 stalled after~.218 measured; open, vertical-jaw seed; stage[.823,-.30,.805]; base+.40. Obs041 front(550,425)=[.99521065,-.2870642,.82699317],(520,420)=[1.0023457,-.24337082,.8294267]. Align[.90,-.28,.805], first insertion[1.015,-.28,.805] achieved[1.013,-.28,.803] without displacement. Close measured q[-.41754,-.5907,.65999,-1.66605,-2.22791,-.59409,.48483], grip0, accept_partial. Finger sum5.3cm; lift[1.013,-.28,.90], withdraw-.30 retained visually (obs046). Snapshot `a11-retained-first-grasp` saved.

Carry yaw-25, fwd.50 (NOT older .65), lower[1.013,-.28,.79]; release measured[-.41481,-.56385,.65352,-1.60944,-2.23971,-.55719,.5127], grip1; withdraw-.20. Visually beside laptop but native nextto ultimately false. Need improve placement via live RGBD and training feedback, not assume old visual completion.

Switch torso[1.25,-1.76,-.85,0] + historical switch seed, stage[.84,-.18,.94], base+.40. Raised[1.04,-.28,1.06] limited to[1.004,-.278,1.054]. Head button(481,333)=[1.0278834,-.29403692,.82367355]. Close at measured q, stage[1.028,-.294,.884], press[1.028,-.294,.828] IK limited but activated. Withdraw[.98,-.294,.94] revealed green; unnecessary additional base+.15 preserved green. Native feedback confirms toggled_on only.

Evidence root `<observation-cache>/scanner-run-007-p6-1054ef/scanner-run-007-recovered-a11/`; final obs060 receipt `receipt_01792127909216886000_78154bb4267e410c86852c5edd8ba477.json`. All calls serialized, no transport/schema errors. Finish reason text mentions goal confirmation but actual feedback was failure; no success claim.
