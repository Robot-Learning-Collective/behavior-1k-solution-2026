# Brush pickup — first observed retention, not yet repeatability

Attempt trumpet-practice-001, observations1–17. Snapshot `brush-left-lift-001` saved after lift. Full receipts/images: `<observation-cache>/trumpet-run-026-p6-509a09/trumpet-practice-001/`. Actions recorded in run `control-action-results.jsonl`.

## Commands in executed order
Use matching run client; inspect each endpoint. This is an evidence record, not a blind navigation macro.
1. `act(left={'grip':1},right={'grip':1},base={'left':-.20},timeout_seconds=8)`
2. Five separately inspected `act(base={'fwd':.20},timeout_seconds=8)` calls. Each floor sampled from latest head RGBD; preserve cabinet/stool clearance.
3. Two separately inspected `act(base={'yaw_deg':35},timeout_seconds=8)` calls.
4. `act(torso={'q':[.645,-.755,-.421,0]},left={'q':[-.85,-.138,-.223,-.98,.322,1.0,.454],'grip':1},timeout_seconds=10)`
5. **Failed approach:** `act(left={'to':[.632,-.052,.88]},timeout_seconds=10)` hit left shoulder2 lower limit, ending [.644,-.002,.864]. Do not reproduce this unnecessary miss.
6. Corrective recenter: `act(left={'q':[-.85,-.138,-.223,-.98,.322,1.0,.454]},base={'left':-.18},timeout_seconds=10)`.
7. `act(left={'to':[.64,.12,.87]},timeout_seconds=10)`
8. `act(left={'to':[.64,.12,.795]},timeout_seconds=10)`
9. `act(left={'to':[.64,.12,.782]},timeout_seconds=8)` stalled at measured z.789 with tabletop preload. A following grip-only close was prerequisite-rejected, zero motion.
10. `act(left={'q':s.last_obs()['robot']['left']['joints'],'grip':0},accept_partial=True,timeout_seconds=8)` releases preload and closes at measured pose. Achieved arm, blocked fingers, not itself proof of grasp.
11. `act(left={'up':.12},timeout_seconds=10)` retained brush visibly above desk.

## Geometry and state
Initial brush head(265,404) BODY[1.253,.361,.788], desktop .768. After recenter: brush head(304,548) [.639,.116,.785]; wrist brush bristles [.643,.120,.776], desktop .768. Before contact obs14 pad refs [.640,.167,.799]/[.639,.073,.793], TCP[.639,.120,.796].
Contact obs15: base odom[1.135,-.266],yaw1.154; torso[.645,-.755,-.421,0]; Lq[-.49008,-.12062,-.41706,-1.11529,.41377,.71203,.5832]. Command .782 stopped at measured TCP[.644,.118,.789], torso effort87Nm; measured-q release removed preload.
Closed obs16 fingers[.0398,0], pads[.645,.155,.791]/[.644,.121,.789]. Asymmetry is real, not failed grasp proof.
Lift obs17 TCP[.648,.118,.909], pads[.647,.155,.911]/[.648,.120,.909], Lq[-.4997,-.0939,-.46728,-1.58227,.84492,1.03711,1.07511]. Brush depth [.662,.133,.902] vs original tabletop .768 confirms lift; wrist image retained brush and head view shows cleared original footprint.

Key images: obs0013 before descent, obs0015 contact/preload, obs0016 closed, obs0017 after lift (corresponding receipt JSON identifies raw/local JPEG paths).
