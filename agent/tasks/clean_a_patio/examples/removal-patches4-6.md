# Additional same-episode sweep evidence

Attempt `patio-probe-001`, TRAIN10. Same retained broom grasp from obs35; not independent reset trials. Torso throughout `[1.75,-1.75,-1.073,0]`, left grip0, downward fingers, close direction about[.81,.59,0]. TCP commands in BODY metres.

|Patch|Public grounding before sweep|Stroke|Reveal|Evidence/rate|
|---|---|---|---|---|
|4|obs56 head(263,424)=[.806,.246,-.016]|left.to=[.59,.47,.005], timeout4|left.to=[.5,.55,.16]|obs58 target gone; sim142.50→144.73→145.90, 2.23s stroke/3.40s total|
|5|obs60 head(284,420)=[.816,.193,-.016]|left.to=[.60,.42,.005], timeout4|left.to=[.4,.25,.16]|obs62 target gone, farther orange patches remain; sim151.30→153.37→154.70,2.07s stroke/3.40s total|
|6|obs67 head(270,263)=[1.236,.243,-.005]; base forward.4 before stroke|left.to=[.60,.46,.01], timeout3|left.to=[.4,.25,.16] plus base backward.35|obs70 target gone at revealed location beside chair; sim169.10→171.10→173.80,2s stroke/4.70s total|

Stroke endpoints sometimes status=stalled due IK/ground tracking, yet images establish local disappearance. Release via explicit lifted target immediately afterward. Do not repeatedly push stalled command.

Chair lesson: chair backs can occlude the target on approach while floor brush remains below them. Increase lateral clearance, re-ground before final approach, use a bounded low sweep then retreat to the prior visible vantage to verify; do not count occlusion as removal. Grill-wheel clearance required rightward rather than leftward withdrawal for patch5.

Latest queried native feedback after patch5: Q0,success=false at4641ticks; only binary whole-floor coverage goal available, not particle count. Six visible patches removed cumulatively, not full task completion.

Public evidence: local cache `patio-run-027-p6-3b5a95/patio-probe-001/obs_0056..0070`; run `control-action-results.jsonl`. No private geometry used.
