# Native a06 — first acquisition failed

Attempt `scanner-run-007-v6-native-a06`, native reset, no snapshots/restores. Finished for operator image-fix boundary at48.4 simulated seconds (~1452 nominal30Hz steps),435.4897 wall seconds. Not a completion; clean consecutive success count remains0.

Repeated native navigation and first two sweeps, then immediately added the a04 large third sweep before any acquisition: base left.20; right [1.23,-.18,.96]→[1.23,-.18,.80]→[1.,-.18,.815]→[1.12,-.18,1.02]. Fresh obs47 showed scanner front overhang. Retreat.60, remote vertical-jaw q [-.01207,-.52959,.68534,-1.34945,-2.31305,-.43568,1.16463], open; stage [.823,-.30,.79], approach.35.

Fresh head depth obs55: pixel(510,475)=[.915159,-.196167,.839477], (500,460)=[.936440,-.190454,.836964], (470,460)=[.938503,-.151586,.832142]. Aligned [.85,-.18,.79], inserted [.95,-.18,.79]. Insertion stalled at measured [.934,-.179,.774], q1 lag-.041, jaws9.8cm; scanner visually shifted backward. Closure was rejected prerequisite_not_met; subsequent lift [.95,-.18,.88] was empty/open and scanner stayed supported. This was not a retained grasp.

Likely next improvement: upper jaw Z~.835 was below observed top .837–.839 at insertion; don't force a fixed .79 height without checking actual top and full pad clearance. Larger sweep alone is not sufficient. No controlled causal attribution yet. Native a05 remains the only full native visual completion (with recoveries), not first-try clean.

Evidence `/tmp/scanner-run-007-p6-57b375/scanner-run-007-v6-native-a06/`: obs55 geometry, obs58/59 blocked insertion, obs62 empty lift. Final receipt `receipt_01792120778405502000_81b7d98a511c47bbb713e524a304ca8f.json`. All acts followed by observe; no calls after admin_finish pending operator swap.
