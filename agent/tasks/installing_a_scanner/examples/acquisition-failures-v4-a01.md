# Scanner acquisition failures — v4-a01

Switch skill succeeded (separate switch-first-success.md). No retained scanner grasp or placement achieved.

Through obs3295, tried left vertical edge pinch, forward/diagonal fingers, closed-finger lid friction pulls with both hands, and right top-down corner pinches. All tested pinch/lift pairs closed to zero finger gap and scanner stayed behind. Several insertions pushed/rotated scanner farther away. At obs3295 scanner disappeared beyond far table edge during open downward-jaw insertion; probable fall, not verified floor pose. Last visible indicator was green. No task-completion claim.

Important geometry correction: grey reflective center is TABLETOP, not floor (XYZ BODY-Z ~0.765 upright). Forward base attempts hit table and tilted robot; retreat restored upright. Don't interpret grey region as a navigation corridor. Table front-to-back reach is substantial.

Reach changes helped but did not establish grasp: torso [1.25,-1.46,-.61,0] increased left reach ~8cm relative to [1.25,-1.76,-.85,0]; upright [1.05,-.67,-.15,0] allowed right TCP ~1.29m, with limits. Near-edge sample later ~[1.207,-.277,.825]. Reacquire after every displacement. Jaw closure at a merely requested target is meaningless when actual TCP stops centimetres short.

Friction pulls did not meaningfully translate scanner; wrist/table interference and fingertip slip remain possible explanations, not proven causes. Top-down corner approach caused loss beyond edge. Need use demo push preparation or approach from opposite table side rather than chase an increasingly distant object.

Transport reset during folded-arm command: recovered with observe, which showed partial execution. Explicitly initialize BOTH grip intents after uncertain RPC. Unknown closed grip plus compound motion is rejected; opening both with measured joint/torso targets succeeded. Retreat 0.30m and fixed torso [.84,-.669,-.42,0] restored upright by obs3378. No pending targets then. Dynamic 'tall' maintains other torso geometry and is not universally equivalent to that fixed configuration.

Lead msg_000068 grants own-scene reset after admin_finish. Reset planned; preserve this failed practice evidence.
