# Recovered native a12 — Q1, first full clean success

Attempt `scanner-run-007-recovered-a12`: native TRAIN10 reset, no restores, first closure retained through lift and 0.30m withdrawal, no observed tilt or transport/schema error. Native feedback both predicates true at2752 steps (91.733sim), final endpoint wall543.5s; reset setup346.953s separately. Consecutive clean success count1, pair NOT yet demonstrated.

Evidence cache `<observation-cache>/scanner-run-007-p6-1054ef/scanner-run-007-recovered-a12/`. Final receipt `receipt_01792128958475802000_c7733a6a168548a8bd6daa858e7635fb.json`.

Preparation followed a11 adaptive rear-draw recipe. First insertion1.035,-.28,.805 achieved1.021,-.28,.787; close measured q[-.46874,-.59893,.71726,-1.62036,-2.28929,-.60293,.48855]. Finger sum5cm; lift1.021,-.28,.90 and base-.30 retained.

Carry yaw-25/fwd.65 and lower1.021,-.28,.79 achieved1.025,-.287,.802. Release measured q[-.48311,-.61764,.72106,-1.63475,-2.28437,-.63555,.49941], retreat-.20. Native nextto FALSE: inherited carry recipe not sufficient. Scanner gap to laptop visibly larger than restored drill.

Switch transition improved: clear hand1.05,-.28,.94 then directly q[-2.38097,-.512,1.73448,-1.59406,.4181,-.38701,1.24799] gives high1.13,-.18,1.025, avoiding low old seed. Base+.20,left-.22. Initial RGBD press1.285,-.092,.817 joint-limited; additional base+.05, shorter reach1.235 still missed. Fresh bilateral red-button samples then agreed [1.251,-.116,.792]. StageZ.86, pressZ.788, withdraw1.20,-.116,.96: native toggled true at2619 steps. Do not reuse pre-contact button coordinates.

Placement correction without reacquisition: RGBD scanner left side around[1.075,-.01,.79], right side~y-.20, laptop left~-.30. Closed right stage[1.075,.06,.91] limited y.03; lower[1.075,.06,.78] limited actual[1.099,0,.773]; slide[1.075,-.08,.78], withdrawZ.96. Scanner moved right toward laptop; both native predicates true, independently supported. No reset/restore/regrasp in this full run. Next full run should use live geometry, not assume carry fixes adjacency.
