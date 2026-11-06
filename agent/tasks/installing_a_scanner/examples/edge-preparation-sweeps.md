# Follow-up back-edge sweeps — a02

Two further visible translations after first sweep; scanner approached and then overhung near table edge. NOT a grasp success. Following open-hand approach accidentally knocked scanner to floor (obs1311). Scanner visible on floor in front/right; no retention claim.

Exact commands and complete per-step proprio/image paths are in `edge-preparation-evidence.json` (submitted_action plus compact_state/robot). Key steps:

Second sweep, base [.616,-.795,0]/yaw-1.278, torso [1.15,-.67,-.02,0], left q[-.4,0,0,-1.9,0,0,0] open, right closed diagonal fingers [.707,0,-.707], closing [0,1,0]:
1. Right to [1.21,-.17,.94] obs898.
2. Right to [1.21,-.17,.80] obs928; actual Z=.807, not reached due press residual.
3. Right to [.97,-.17,.81] obs1027; actual [.990,-.192,.796], joint-limited. Scanner visibly translated/rotated again.
4. Right to [.97,-.17,.96] attempted; outer bash timed out. Fresh observe1071 shows TCP[1.058,-.228,.972], scanner remains shifted. Reset both grip intents explicitly; no blind retry.
5. Restore both open and unload right q[-2.20997,-.63774,1.77748,-2.084,-2.346,-.14186,-1.55894], then base fwd-.20, torso [.84,-.669,-.42,0], obs1099.

Third sweep, base [.559,-.605,0], yaw-1.278, torso [.84,-.669,-.42,0]:
1. Right to[1.15,-.25,.94], finger_dir[.707,0,-.707], close_dir[0,1,0] obs1134.
2. Right grip0 obs1138.
3. Right to[1.15,-.25,.80] obs1191; actualZ=.814, press residual.
4. Right to[.94,-.25,.81] obs1220 actual[.942,-.249,.811], visible scanner shift.
5. Right to[1.0,-.25,.98] obs1243, scanner remains at edge. Near-front scanner head(600,615)=[.6167,-.31745,.81359], (560,610)=[.62253,-.26001,.82662]; floor beyond head(580,640)=[.5513,-.4764,.4474] is chair geometry, NOT floor. Edge safety needs remeasurement.

Failure after these successes: base fwd-.15 obs1255; then right to[.66,-.30,.80], finger_dir[1,0,0], close_dir[0,0,1], grip1 obs1311. Goal reached but scanner fell. Endpoint target was not inside scanner, yet intermediate wrist rotation/translation crossed its position. Next trial should withdraw horizontally at high Z to well in front FIRST, rotate jaws there, then descend, then slowly insert. Do not diagonal-interpolate from behind/above object to a low forward grasp pose.

Max_steps: second positioning20/descent16/sweep20/withdraw16; third positioning20/close8/descent12/sweep16/withdraw16; retreat16/pregrasp20. These command endpoints must be adapted to fresh geometry, especially after rotation or partial motion.
