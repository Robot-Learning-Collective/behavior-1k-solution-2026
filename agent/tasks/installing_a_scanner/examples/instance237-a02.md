# TRAIN237 a02 — native Q1 transfer
Full fresh reset; no snapshots/restores/regrasp. Native feedback first queried at finish: toggled_on=true,nextto=true,Q1,2271steps/75.7sim/551.254119059wall. Reset403.213469429s separate. Budget6387. Training rehearsal, not official/held-out score.

Evidence cache `<observation-cache>/scanner-run-007-p6-93a5c8/scanner-run-007-instance237-a02/`. Final observation45 receipt `receipt_01792132860375774000_b578e354643a4798a11d3af10e7016da.json`.

General procedure in ../NOTES.md. Specific realized path (not blind replay): initialize both open, yaw-176; left1m guard stalled at.63, advance.55 then left.35; park arms left[-.4,0,0,-1.9,0,0,0]/right[-.6,0,0,-1.9,0,0,0], torso[1.15,-.67,-.02,0]. Rear wrist[-1.55108,-.25594,.73343,-1.39238,-1.75775,.91743,-1.33985], close empty; forward.32. Measured scanner rear1.54/front1.40 before approach. Stage[1.32,-.24,.98], engageZ.79, base draws-.25/-.16/-.07 with high clearance/inspection between. Front rim~1.08/Z.828, edge~1.07/Z.736 before last draw.

CRITICAL fix from a01: withdraw-.30 BEFORE open + vertical wrist[-.01207,-.52959,.68534,-1.34945,-2.31305,-.43568,1.16463]. Stage[.98,-.24,.81], base+.30. Fresh rim head(520,390)=[1.07434,-.27725,.80673],top(520,375)=[1.09055,-.27453,.82793]. Align[1.04,-.25,.81], insert[1.105,-.25,.81], measured[1.103,-.248,.813]. First close measuredq[-.75778,-.49267,.83161,-1.4207,-2.30793,-.60435,.46985], grip0 partial. Gap5.6cm. Lift[1.103,-.248,.94] reached/retained, base-.25 then yaw-30.

Laptop head(640,215)=[1.78074,-.91743,.79884], open support(550,240)=[1.68038,-.59763,.76498]. Base+.45 avoiding chair right. Carry[1.16,-.54,.94], lowerZ.80 actual[1.161,-.537,.806] blocked/jaw-table interference. Release measuredq[-1.03991,-.61066,.27144,-.42125,-2.01167,.42774,.71732] grip1 partial; withdraw[.98,-.54,.82], clearZ1.03 (joint-limit actual1.02). Scanner independently supported. yaw-20, high switch posture[-2.38097,-.512,1.73448,-1.59406,.4181,-.38701,1.24799], base+.18, close empty.

Fresh button right(55,130)=[1.27282,-.32754,.82246], head(516,308)=[1.27492,-.33159,.82374]. Stage[1.264,-.33,.89], pressZ.815 actual[1.267,-.334,.835] blocked but green, clear[1.15,-.20,1.02]. Finish both predicates true without placement correction. No observed robot tilt; planar odometry cannot prove absolute tilt/height. Initial base stall and benign contact/joint-limit stalls are preserved, not counted as error-free tracking.

Preceding a01 Q0:1367steps/45.566666667sim/242.068542493wall. Draws-.25/-.18/-.08 produced supported rim but omitted withdrawal before wrist reorientation; scanner fell during transition. No restored credit. a02 is first success in new streak.
