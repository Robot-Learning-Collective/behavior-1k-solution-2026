# First within-budget patio completion — fresh TRAIN10

`patio-speed-003`: native success true/Q1/fraction1 at **11541 native30Hz ticks =384.70 simulated seconds** (obs129). Budget18106ticks/603.533s; headroom6565ticks/218.833s. Target15000ticks/500s met. Endpoint wall3375.9s, admin finish3410.0065s, reset/setup excluded. Not wall-speed parity, official scored evaluation, or repeatability. One fresh reset, no restores/manual interventions. All128 motor calls used `budget_control.act`; action-log sum11541steps matches native feedback, and all128 requested positive finite max_steps. Privileged feedback only via dedicated practice admin API. Continuous original left broom grasp acquiredobs007/34.97s.

Actual evidence: `../speed-003-success.json`, `../speed-003-finish.json`, run `control-action-results.jsonl`; public cache `<observation-cache>/patio-run-027-p6-3b5a95/patio-speed-003/`, final receipt `receipt_01792170274476452000_bc867a682de3491f8a73c904d14d05d4.json`. Native false at6972/7964ticks, then true11541. Do not claim first true tick earlier than queried.

## Reproducible policy, not blind trajectory replay

Always reacquire RGBD after stance/posture changes and inspect endpoint/safety. Public odometry is only drifting proprioceptive integration. The following is a route record for this fixed TRAIN10 geometry, not universal coordinates.

1. **Pickup002–007,34.97s:** yaw−65,forward4.45/left−.95; lowtorso[1.75,−1.75,−1.073,0]; stage[.41,.4,.03], horizontalinsert[.499,.4,.027]/close, lift. Both aperture~.0328m and full broom lift confirmed. Move clear before turning: fixed low branch180deg turn008 still struck foliage; measured release/right.65 and survey010 recovered49.9s.
2. **Stones011–019,71.23s:** two orange marks, short contacts/reveals. Then interior020–041 covered10 total visual labels by145.57s. Bounded sweep TCP approximately[.65–.72,.27–.41,.01], fingersdown/close[.31,.95,0]. Current grasp brushXY offset~[+.32,−.10] relativeTCP; visually recheck.
3. **Bench042–053:** thin rail shifted under insertion; closed jaws empty. Bounded right-hand/base contactpush051,withdraw052 moved bench. This was NOT a grasp. New exposed floor subsequently covered.
4. **Opposite grill/chair055–078,232.4s:** labels11–15. Guard/torso deflection required measured release and changed route; native stillfalse.
5. **Exposed far bench086–092,265.47s:** labels16–18, native false. Search093–108 was avoidable navigation/recovery overhead, not contact cleaning time.
6. **Remaining near-chair/border113–129:** two orange clusters initially visible through chair gap: at113 head(438,328) [1.9921,−.4395,−.0082], and(713,590)[.8201,−1.1426,−.0048]. Tan mark(596,570) was left unchanged. Approach/recovery details in NOTES; the important final targets are below.

### Final two bounded contacts

-19: obs123 targethead(271,350) BODY[.995435,.230223,−.004865]. Stroke124 requestedTCP[.65,.33,.01], actual[.646,.331,.011],1.367s; known joint reveal plusback.25,2.2s. Orange absent after reveal125; tan adjacent mark persists.
-20: yaw+70, target126[1.267514,.189932,−.004816], nearbylamp[1.098087,.322970,.043738]. Forward.25; stroke128TCP[.70,.24,.01], actual[.696,.241,.011],1.067s. Slightly right-offset stroke kept brush away from lamp. Reveal129 .933s; native true. No increased floor force, object-pose API, particle count, or contact sensor.

## Pose/recovery lessons

Low reveal Lq `[-.34825,.62665,-1.3462,-1.19364,.82925,-.21662,.68141]`, torso `[1.75,-1.75,-1.073,0]` givesTCP[.4,.3,.16]. Surveytorso `[1.074,-.51557,0,0]`, Lq `[.00015,.45558,-1.38019,-.81915,.93791,-.25227,.47537]` givesTCP[.4,.3,.451]. Grasp retained throughout, including recoveries.

Both q0 and compact low-right stow failed near chairs during115–118. **Raise torso with measured arms first**, change clearance, stage desired arms while high, then lower torso. Successful121–123 rightq `[.2026,-.14358,-.39082,-1.10861,-.26479,-.60613,.51003]` giveslowTCP[.45,−.4,.25]. Branches are not collision-free guarantees.

Grill103 q2lag.317rad: measured releases/backing104–105 triggered velocity mismatch. Changed to yaw−50 at106, thenforward1.0 at107 restored clearance. Never repeat blocked base command or infer contact identity from efforts. All lagged persistent goals replaced; final129 low tracking errors/effort.

## Next acceptance gate

Independent fresh reset, same budget wrapper, no restores; complete natively again. Optimize navigation/visibility and avoiding bad posture transitions, not harder downward strokes. Current result is1 successful budgeted run after preserved earlier incomplete speed002 and over-budget probe001.
