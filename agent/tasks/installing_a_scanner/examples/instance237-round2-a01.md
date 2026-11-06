# TRAIN237 round2-a01 — native Q1

Rebuilt worker e361cf/source a47213f30cb8dcf37551dd75fb011bc129700841, protocol6/controller26efe4a. Fresh native reset; no snapshots/restores. First acquisition retained through lift/withdrawal/carry; first switch press green. Native finish: both toggled_on and nextto true; Q1, 2093 steps,69.76666666666667sim seconds,499.2409612529991wall seconds (includes authority-reconciliation hold). No observed base tilt; odometry cannot establish tilt.

Fresh RGBD justified shallow lowered insertion: head rim[1.07613,-.25279,.80424], true desktopZ.7649. Right lip[1.11484,-.08413,.76023]; exact underside uncertain. Align TCP[1.015,-.24,.785], insert[1.085,-.24,.785], lower padZ.738. No observed insertion displacement. Closed at achieved q, liftedZ.94, withdrew base.25 before yaw-30.

Laptop samples before approach: [1.86312,-.74401,.79723], [1.71233,-.78307,.79764], [1.75357,-1.01660,.79473]; support[1.73314,-.61933,.76499]. Base+.45, carry[1.16,-.54,.94], lowerZ.835. Replaced target with measured q[-.93108,-.6634,.18362,-.69294,-2.10489,.38653,.51143] before opening, level backout[.98,-.54,.835], then raiseZ.98. Scanner changed attitude while settling after release, but remained supported and subsequently stable through switch approach/press/clear. Do NOT claim zero release displacement.

Important duration correction: requested seconds=.5 on achieved measured-q goal advanced only .0667s; seconds is an UPPER CAP, not guaranteed dwell. Subsequent clear/approach supplied settling physics. No .5s retained-settle claim.

Fresh switch right[1.24512,-.31584,.82185], head[1.24632,-.31793,.82345]. Stage[1.246,-.317,.89], pressZ.815, clear[1.15,-.20,1.02]. First press green; supported placement remained beside laptop.

Terminal receipt: `<observation-cache>/scanner-run-007-p6-e361cf/scanner-run-007-instance237-round2-a01/receipt_01792154895234718000_10737fce42c649c58359f23089204e71.json`.
Finish reason `round2-a01-native-first-grasp-level-release-first-green-press`.

Training-only repeat on familiar TRAIN237, not held-out/layout-generalization evidence and not resolution of lead-reported dev11 failure. Continue fresh attempts and retain failure denominator.
