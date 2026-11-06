# TRAIN237 a16 — insertion displaced scanner, rejected

Native fresh practice Q0, both predicates false, 1401/6387 steps, 46.7 simulated seconds, 439.491105849 wall seconds. No restores, grasp closure, or observed robot tilt.

BASE rear draws .25/.16/.10 with upward clearing, withdraw .30 before wrist rotation, return .30. Fresh rim head[390,505]=[1.076973,-.253483,.803059], upper [382,505]=[1.090401,-.255812,.808351]. True desktop head[350,390]=[1.208146,-.064627,.764907], [390,630]=[1.104361,-.512581,.764884]; interpolated edge about1.165. Underside unseen.

Align [1.025,-.25,.81], shallow insertion [1.095,-.25,.81] visibly shifted scanner backward on table (obs25→26), despite adequate apparent horizontal overhang. Lower pad measured [1.099,-.249,.765]. Withdrew immediately without closing, no blind additional rear draw. Scanner remained supported. Finish a16-insertion-displacement-rejected-no-closure.

This breaks a13–a15 three-success streak. Likely vertical clearance sensitivity: fresh rim was lower than prior successes; horizontal overhang alone insufficient. Next attempt should estimate scanner thickness/underside with side RGBD and lower shallow approach a few mm if justified, rather than replay Z.81.

Terminal receipt: scanner-run-007-instance237-a16/receipt_01792143184151395000_15f8df15f1014968b6e1c2635bdcc729.json under scanner-run-007-p6-93a5c8 cache.
