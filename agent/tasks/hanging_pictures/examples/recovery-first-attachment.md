# First protocol6 native attachment (snapshot practice only)

Runtime ebf054. Attempt `practice-restore-recovery-before-wall-compensation-50a08f667ea149d29f8364ac75b862ae`.
Native attached true / Q1 at step1343 (44.7667sim s); remained true after full opening,10cm withdrawal and15cm hand lowering, step1417 (47.2333sim s), then admin_finish. This is NOT full-reset proof.

Receipts: `<observation-cache>/pictures-run-009-p6-ebf054/<attempt>/` obs008 attachment;009open;010withdraw;011handlower.

Previous recovery a11 failed (full release/drop); full-frame wall-parallel restored drill c81997 also failed (ended on restore). Premature wall-parallel alignment produced high arm/torso effort before attachment. Do not infer contact identity from effort.

Successful approach preserved historical OBLIQUE a07 pre-seat poster pose, calibrated normal, top edge and pose relative to visible nail. `align_saved_nail.py` / `recovery-geometric-alignment.json` compute public RGBD geometry; old p4 public base odometry only transforms old observed nail into old pre-seat BODY frame. New p6 odometry is not treated as ground truth. Exposed current nail by lowering poster10cm, then restored matching pose. Matched pre-seat horizontal translation +25.76mm forward /−29.51mm left; height +100.44mm with small orientation correction. From there15mmnormal +10mmnormal, then10mmdown, then another10mmnormal caused snap/native true. Immediately canceled right command to measured q and fully opened, then withdrew and lowered hand.

Earlier normal-only calibration achieved normal [0.7587483,−0.6494805,−0.0497605] versus old [0.7581742,−0.6502060,−0.0490305], but same nominal base target still left wall ~30mm farther away. RGBD wall/nail alignment is required; command replay alone is not sufficient.

Next: fresh native-reset run, no restore, within3581steps. Keep public RGBD corrections and distinguish practice feedback from full-reset scoring.
