# Hanging pictures — public-data task pack

1. Read **TASK.md** for the official instruction, exact BDDL and native budget.
2. Read **ANNOTATIONS.md** for three complete coarse/fine episode sequences, durations and alternatives.
3. Before pickup, handover or hanging, read **HUMAN-PROPRIO.md** and the relevant pages in **keyframes/index.md**. Each page has four timestamped rows; each row is **head | left wrist | right wrist**. Follow the sequence through approach, closing, object movement, opening and withdrawal—not just one final pose.
4. Retrieve the matching numeric sample with `python3 query_proprio.py 6846 960`. JSON has both hands' joints, TCP xyz/xyzw, model pad references, grip width/command, torso, measured base velocity and approximate odometry. No dependencies or source dataset access needed at runtime.
5. Measure your own RGBD before moving. Do not copy demo world/target coordinates, blindly replay joint endpoints, infer contact from a label, or declare success from a reached TCP. Keep acting/reassessing until the native evaluator terminates; never intentionally finish early.

## Coverage and limits

- HF `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`; episodes6846/6854/6863, TRAIN71/88/110. None is held-out dev11–19.
- **563 aligned timestamps / 1,689 camera views / 142 JPEG pages**, approximately0.25s spacing through every annotated manipulation segment, with0.5s approach and up to1.5s trailing margin (clipped to actual episode end). Three-camera RGB occupies17.62MB; entire pack is under20MB. This is dense sampled coverage, not continuous video or a claim that every frame was manually reviewed.
- All decoded timestamps checked against selected episode frames within2ms. Position groups are source row n−1, velocity/requested command n−2 for RGB frame n. Source-reported lag is not a simultaneous contact/shutter guarantee.
- Exact object pose, physical contact and target orientation are **unavailable**. Nail-relative values are public RGBD/manual-pixel plus planar-odometry estimates; drift and base tilt limit accuracy. Poster-grasp-target-relative poses remain null. Dense RGB supplies the missing visible interaction evidence; it does not manufacture sensor truth.
- Pad points are static model reference endpoints calibrated from public onboard robot self-state in practice v4-a06, not measured deformable contacts. No held-out evaluation trajectory/object pose is imported. FK agrees with sampled human EEF to<5µm; simulator/model consistency, not physical calibration.
- Annotation object names identify demonstration objects only. The evaluated world's geometry differs. Front-to-wall distance includes poster thickness/mount stand-off; zero front-gap is not the goal.

`provenance.json` records official source hashes, exact episode joins, static model/reference provenance, selected video frames/PTS and all JPEG hashes. No private transcripts/reasoning, live simulator access, rewards, scores, hidden object transforms or contact labels were used. Original large shards stay outside this pack.
