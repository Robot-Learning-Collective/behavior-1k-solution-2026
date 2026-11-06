# One visible mud patch removed

Attempt patio-probe-001; same retained broom as pickup-local. Obs43 base odom[.212,-.688,8.235rad], torso[1.75,-1.75,-1.073,0], left fingers[.0345,0], right open/q0. Left finger_dir~[0,0,-1], close_dir[.81,.59,0]. Mud selected head pixel(338,448), BODY[.746,.0545,-.0217] (near-ground depth; thin decal). Broom cream-head pixel(280,500)=[.684,.144,.195].

1. `s.act(left={'to':[.50,.30,.04]},timeout_seconds=4)` obs44, sim118.13. Brush sample head(300,460)=[.730,.135,.0573]. Narrow patch still visible at(338,448).
2. `s.act(left={'to':[.57,.30,.005]},timeout_seconds=4)` obs45, sim119.07. Returns stalled at TCP[.566,.304,.007], residual ~6mm, loaded wrist. Left measured q[-.69150,.23854,-.63244,-.54404,-.27664,.12751,.01184], fingers[.0344,0]. No pose-success claim. 28ticks / .933sim seconds.
3. `s.practice_feedback()` at3572ticks: Q0, sole not-covered predicate false. Public endpoint has no particle counts.
4. `s.act(left={'to':[.50,.42,.16]},timeout_seconds=4)` obs46 sim120.10. Relieves contact and reveals area. Previously narrow orange patch is absent, two farther patches remain unchanged. TCP[.497,.423,.159], q[-.10741,.73910,-.48586,-1.30020,-.08859,.17505,.03012], fingers[.0344,0].

One visible patch per .933sim-second stroke; 1.967sim seconds including reveal. Not a count of individual particles and not global goal success. Before/after obs_0044/obs_0046 under `<observation-cache>/patio-run-027-p6-3b5a95/patio-probe-001/`. Full receipts/actions retained.
