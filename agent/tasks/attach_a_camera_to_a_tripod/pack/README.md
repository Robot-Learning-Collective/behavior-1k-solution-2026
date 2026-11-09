# Camera attachment — public-data task pack

1. Read **TASK.md** for the official instruction, exact BDDL/init and native budget.
2. Read **ANNOTATIONS.md** for three complete fine/coarse sequences, durations and camera-specific common order.
3. Before floor pickup, tripod support, mount alignment, seating and release, read **HUMAN-PROPRIO.md** and relevant pages in **keyframes/index.md**. Four timestamped rows per page; each row is **head | left wrist | right wrist**. Watch both the camera hand and supporting tripod hand through withdrawal, not just a final pose.
4. Retrieve both hands' numeric sample with `python3 query_proprio.py 7017 4137`. JSON includes joints, TCP xyz/xyzw, model pad references, fingers/requested grip, torso, measured base velocity and approximate planar odometry/approach. No dependencies or original shards needed at runtime.
5. Measure your own RGBD; never blindly replay demo coordinates/joints. Reached TCP, support and stable appearance do not establish attachment. Keep acting/reassessing until native termination, user stop or a genuine safety/runtime boundary.

## Coverage and limits

- HF `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`; episodes7016/7017/7018, TRAIN20/21/22. Excludes held-out dev11–19 and operator qualification23/24.
- **958 aligned timestamps / 2,874 views / 240 JPEG pages**, at most0.5s spacing through manipulation plus approach/contact-candidate/opening/withdrawal samples. Between-manipulation annotation gaps are also covered, with no invented labels. RGB14.26MB; entire pack under20MB. Sampled coverage, not continuous video or all-frame manual review.
- Selected video PTS agrees with expected episode frames within2ms. RGB n aligns to source position/camera row n−1 and velocity/requested command n−2. Source-reported lag is not a simultaneous shutter/contact guarantee.
- No absolute base, camera-object/tripod pose, mounting orientation or physical contact is provided. Target-relative fields remain null. Approximate odometry drifts; visual interaction and current measurements must establish placement geometry. Historical nail-named fields are null for this task.
- Pad endpoints are static model references derived from public robot self-state calibration, not deformable contacts. FK matches sampled human EEF to<5µm (model consistency, not physical calibration).
- Three representative pages7016-078/7017-080/7018-053 were visually reviewed; source labels distinguish attachment, release and unlabelled gaps. Demonstration object IDs are not live handles or privileges.

`provenance.json` records public source hashes, episode joins, model/reference provenance, exact selected frames/PTS and JPEG hashes. No private reasoning, held-out rollout data, live simulator/object/contact/scorer access or rewards were imported. Original data and video caches remain outside this pack.
