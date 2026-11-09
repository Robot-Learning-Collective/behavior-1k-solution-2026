# TRAIN237 round2-a05 — Q1, closer placement repeated

Fresh e361cf/a47213f native reset, no restores. Reset setup343.016458176s separately. Native finish2169steps /72.3sim /362.082579189wall; both predicates true. First acquisition/press. Round2 completed3/5, latest a04/a05 both Q1, familiar TRAIN237 only.

After BASE-.25/-.16, front head[390,500]=[1.0789,-.2463,.8004]; true desk[380,370]=[1.1282,-.0204,.7649], [425,630]=[1.0300,-.4692,.7649]. Near-zero overhang; final BASE-.06, clear, withdraw-.30 before wrist rotation/opening, stage low and return+.30. Fresh front[390,500]=[1.0826,-.2492,.7952]; desk[360,370]=[1.1800,-.0216,.7649],[405,630]=[1.0709,-.4930,.7649]. Align[1.015,-.24,.785], insert[1.096,-.24,.785]. Blocked at[1.089,-.227,.780], lower finger deflected. No visible scanner displacement; replaced insertion with achieved q[-.73186,-.44131,.87269,-1.33385,-2.31126,-.57994,.55127] and closed with accept_partial. Lift[1.089,-.227,.94], base-.25/yaw-30 retained visibly. Jaw gap alone was not the retention evidence.

Laptop near edge head[215,590]=[1.8091,-.77495,.7866]; visible scanner edge[300,635]=[1.0897,-.3627,.9875], supportZ.765. Base+.43; carry[1.19,-.59,.94], lower.835. IK stalled at[1.181,-.579,.840]; replace with q[-1.32368,-.64149,.51027,-.04749,-2.03943,.6114,.81985], open, level backout[.98,-.579,.84], raise.98. Raise stalled marginally at.975 due joint limit, not contact proof; next high press q replaced the miss. Scanner changed attitude during release/backout but then remained supported and stable; no zero-displacement claim.

Yaw-20, high press orientation, base+.18. Switch cross-localized right[125,32]=[1.2672,-.3430,.8225], head[311,521]=[1.2678,-.3406,.8215]. Close empty hand, stage[1.268,-.342,.89], press.815→green, clear[1.15,-.20,1.02]. Native nextto true after clear. No robot tilt observed; planar odometry cannot establish tilt.

Final receipt: `<observation-cache>/scanner-run-007-p6-e361cf/scanner-run-007-instance237-round2-a05/receipt_01792156576374203000_3240f747671d4f288ef27be788450c04.json`.

Two closer-placement successes support the training correction but not held-out reliability. Continue geometry-based practice; avoid deeper insertion or fixed final draw. Release settling still deserves improvement.
