# Native-reset a12 success — protocol6

- Attempt: `pictures-run-009-v6-native-a12`, runtime ebf054, TRAIN10 original episode reset; NO snapshot restore in this attempt.
- One poster native `(attached poster.n.01_1 wall_nail.n.01_1)` true / Q1 at final step1401 =46.7sim seconds, below3581steps. Full opening,10cmwithdrawal and15cmhandlower completed; poster retained visually.
- Practice-mode episode (unbounded practice flag), NOT a separately scored benchmark episode. Native feedback was queried only at end after final verification, not used for action selection during a12. This is full-native-reset practice proof, not held-out/generalization evidence.
- 25 act calls + initial observe. Last endpoint wall205.1s from observe, not teleop-wall parity. Reset response reported setup_seconds313.6857; this is reported backend setup field, not independently timed end-to-end reset latency.
- First attempted act was rejected locally because admin_reset requires observe first; no motor replay occurred. Then observed and started full sequence.
- Native snap visually occurred obs022 during10mmdown; extra prebatched10mm seating obs023 was unnecessary and produced sustained arm lag. Improvement: inspect after each seating action and release immediately on visible snap, rather than batching another push.
- Final obs026 receipt: `<observation-cache>/pictures-run-009-p6-ebf054/pictures-run-009-v6-native-a12/receipt_01792128450940174000_406102354954462390344592f15e5c40.json`.
- Final image/depth and all action receipts in same attempt directory. admin_finish completed and repeated native true/Q1.

Recipe: verified55mm-insertion737pickup →8cmup/6cmwithdraw →25cmbasewithdraw/compactcarry →staging →historical447arm/torso pose →RGBD grasp-normal compensation →nominal approach →expose nail by lowering10cm →`align_saved_nail.py` full oblique poster-frame/nail-relative correction →15mm+10mmnormal →10mmdown (snap here) →explicit measured-q/open →withdraw10cm →lower15cm. Preserve oblique approach; forcing parallel early blocked previous drills. Current helper has manually selected pixels for this observation and must be visually revalidated, not blindly reused in other scenes.
