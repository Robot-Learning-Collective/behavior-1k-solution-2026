# Chili acquisition — one observed success, TRAIN10

Practice `cabbage-practice-001`, obs114–119; no repeatability claim. Initial chili had been displaced by earlier failed grasps. Use fresh RGBD, not blind replay. All vectors BODY metres; robot posture and scene differ after reset.

1. From elevated clear posture, right q `[-.94489,-.62956,.2041,-1.59912,-.78197,.93884,.19002]` → TCP `[.700,-.299,1.396]`, open. Finger direction approximately `[.9,.4,-.16]`; close direction `[-.41,.91,.01]`.
2. `right={'to':[.82,-.25,1.31]}`, seconds4 → reached.
3. `right={'to':[.85,-.26,1.292]}`, seconds3 → blocked at `[.846,-.251,1.309]`; release downward preload rather than retry.
4. `right={'q':measured_right_q,'grip':0}`, accept_partial=True, seconds3 → finger sum8.3cm. q at closure `[-1.19136,-.31721,.42858,-.70856,-.46998,.31871,.43215]`.
5. `right={'up':.10,'fwd':-.04}`, seconds3 → chili visibly lifted with pads; sum7.7cm.
6. `right={'to':[.60,-.30,1.40]}`, seconds4 → visibly retained outside shelf; sum7.6cm.
7. Snapshot `both-ingredients-retained-001` saved after obs119, not yet restored.

Torso `[.44929,-.39939,.0021,-.00063]`; base odometry approximately `[3.529,-1.568]`, yaw−1.449 (drift-prone). Cabbage retained left throughout.

Do not directly command this pregrasp from a low/retracted arm: diagonal IK paths struck shelf underside. Raise a compact arm outside lip first; inspect intermediate endpoints. Top-down orientation hit wrist limit and shelf, while near-horizontal approach succeeded once. Grip separation alone is not contact/grasp proof; visual lift and withdrawal were the retention tests.
