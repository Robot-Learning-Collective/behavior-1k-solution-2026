# First native patio completion — unscored TRAIN10 practice

Attempt `patio-probe-001`, source8432188/protocol6. Native success at30497ticks, Q1, satisfied_fraction1, observation366. `../practice-001-success.json` and `../practice-001-finish.json` preserve actual feedback. Saved native snapshot `patio-first-native-success` then admin-finished; no live active attempt during subsequent human study.

This is a successful full original world in unbounded practice, not a scored rollout, efficiency result or reset-reliability claim. Endpoint sim1016.5667s / wall7547.2s; admin-finish wall includes later documentation. Same broom grasp retained from35 through366.

## Exact final cleaning segments
Use assigned client only. These are observed successful commands at the specified local frames, NOT blind replay coordinates from reset. Navigate with fresh RGBD and account for whole handle, both arms and furniture. Full authoritative ordered actions (including all failures/navigation) are in `../control-action-results.jsonl`; all attempt images/receipts reside under `<observation-cache>/patio-run-027-p6-3b5a95/patio-probe-001/`.

After tipped bench relocation, wide interior detour reached three exposed orange clusters. Do not reuse the unsuccessful tree/lamp corridor.

```python
# Patch18, obs346 measured orange BODY [.8410,.1588,-.0052].
s.act(torso={'q':[1.75,-1.75,-1.073,0]},
      left={'to':[.4,.3,.16], 'finger_dir':[0,0,-1],
            'close_dir':[.31,.95,0], 'grip':0}, timeout_seconds=4)
# obs347 reached low staging pose, retained ~.0345m finger sum.
s.act(left={'to':[.55,.25,.005]}, seconds=2, timeout_seconds=2)
# obs348 achieved [.55,.25,.007],1.10sim seconds.
reveal_q=[-.34825,.62665,-1.3462,-1.19364,.82925,-.21662,.68141]
s.act(left={'q':reveal_q},timeout_seconds=3)
# obs349 reveal .933s; orange absent, native stillfalse at29527ticks.

# After separately verified navigation/recovery352–363, fresh targets:
# right [.93475,.22602,.00072], left [.88159,.58877,-.00394].
s.act(left={'to':[.63,.32,.01]},seconds=2,timeout_seconds=2)
# obs364 .867s, visible forward remainder; not complete.
s.act(left={'to':[.69,.32,.01]},seconds=1.5,timeout_seconds=1.5)
# obs365 .2s; requested extension over visible remainder.
s.act(left={'q':reveal_q},timeout_seconds=3)
# obs366 .9s; BOTH remaining orange clusters absent.
s.practice_feedback()  # actual native success=true/Q1 at30497ticks
```

No exact per-particle removal mechanism inferred: after second stroke/reveal both clusters were absent; do not claim each had independently verified tool contact.

## Final self-state and evidence
- Torso `[1.75,-1.75,-1.073,0]`; left TCP `[.4,.3,.16]`, measured pinch `[.405,.316,.16]`, pad endpoints `[.409,.330,.160]` and `[.400,.302,.160]`.
- Left close_dir `[.31,.95,0]`, finger_dir `[0,0,-1]`, grip0 / fingers~`[.0345,0]`; no outstanding arm target.
- Right empty/open: q `[.13555,-.00027,-.01092,.0044,-.0232,-.00365,.0021]`, fingers `[.05,.05]`.
- Final odometry `[-3.661,1.174]`, yaw−1.334rad is drifting proprio-integrated estimate, not world pose.
- Before final strokes: `obs_0363_raw.jpg`; contact endpoints364/365; revealed after366 `obs_0366_raw.jpg`.
- Final receipt `receipt_01792164901150424000_3c65733703404d208e471047993659e4.json`.

## Primary efficiency issue
Strokes generally removed visible mud in1–3sim seconds, but search, tool-clearance failures and repeated recovery dominated the two-hour wall practice. Final success came after explicitly exposing and reaching furniture-hidden patches. Next experiment should measure systematic coverage and furniture handling, not add contact force to already effective strokes.
