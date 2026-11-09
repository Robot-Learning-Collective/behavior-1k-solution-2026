# Coverage continuation: patches7–11

Same TRAIN10 `patio-probe-001`, retained grasp from obs35. All strokes followed by explicit left.to=[.4,.25,.16] lift/reveal. Torso=[1.75,-1.75,-1.073,0], grip0. No reset reproducibility claim.

|Patch|Grounded BODY target|Stroke TCP|Observations / sim seconds|
|---|---|---|---|
|7|[.817,.057,-.005]|[.59,.29,.005]|78→79→80;195.50→196.50→197.40|
|8|[.753,.091,-.005]|[.56,.32,.005]|85→86→87;210.63→212.10→213.07|
|9|[.804,.222,-.005]|[.58,.45,.01]|89→90→91;219.60→221.60→223.47|
|10|[.819,.223,-.005]|[.60,.45,.01], explicit finger_dir=[0,0,-1],close_dir=[.81,.59,0]|96→97→98;237.87→239.90→242.53|
|11|[.809,.164,ground]|[.59,.39,.01]|100→101→102;248.03→249.07→250.20|

Each orange patch absent in the reveal image while other visible patches persisted. Latest binary native goal at7506ticks still false/Q0. Eleven local visible removals do not prove global mud coverage solved.

Navigation failures preserved: base guard stops at75 and81 beside grill; at75 torso/right arm also deflected strongly. Retreat.2 restored torso; lateral offsets.25 then wider corridor allowed movement. Turning near grill at84 and103 also deflected torso despite base action saying reached; lateral withdrawal.18 and backward.3 respectively restored commanded torso. **Do not use reached as clearance proof.** Prefer bigger furniture margins and inspect torso/right-arm tracking after every turn.

Tan discoloration tests: obs73→74 failed to remove a faint mark, but TCP was4.2cm above floor (IK stall), so inconclusive. Better-placed obs106→107→108 test atBODY[.799,.271,ground],TCP[.59,.48,.01] measured[.592,.475,.026], then reveal, still leaves faint tan near the white paving edge. Unknown whether fixed floor texture vs remaining material; do not add to removal count. Larger tan candidate remains beneath grill; direct approach abandoned after torso deflection.

Torso='normal' is usable to raise view for travel; returning to explicit sweep torso retained broom. Cartesian orientation drift accumulated slightly over many motions; explicitly restoring downward fingers and close_dir at97 retained broom and removed patch10. No force/contact inference.
