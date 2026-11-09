# TRAIN237 a12 — rejected insertion, subsequent overdraw failure

Fresh native reset, no snapshot/restores, no grasp closure/regrasp, no observed robot tilt. Finish-only Q0, both predicates false, 2091/6387steps,69.7sim,441.300959242wall; reset separately reported403.213469429s. Finish a12-overdraw-after-rejected-insertion-scanner-fell. Failure remains in denominator.

Raised before table approach. BASE-only preparation .25/.16; second draw ineffective (rear freshly measured [1.4536546,-.2632652,.82753617], front [1.263778,-.22071768,.8248227]). Corrected base+.16, hand stage1.35/-.26/.98 thenZ.79 (achieved forward1.329; IK/contact limits noted), BASE-.20, clear. Rear [1.2885572,-.23597291,.8289453]; front [1.1275147,-.19796444,.8274247]. Another BASE-.08 at1.32/-.24/.79. Withdrew-.30, achieved~.256 with stall, not forced; opened, rotated vertical, staged [.98,-.25,.81], approach+.25.

Preinsertion head(v,u) front(351,490) [1.1479481,-.23984568,.8264865]; desk brackets(343,375) [1.2633555,-.03602605,.7297547],(384,570) [1.1638572,-.45725808,.7042037]; interpolated desk forward1.2152117, apparent overhang6.73cm. Refined brackets(333,375) [1.2636346,-.03482746,.7615194],(374,570) [1.1669748,-.44274262,.7350555] with front(354,490) [1.1416476,-.23847833,.82521266] yielded7.37cm. These brackets include desk-face/bevel depths, not guaranteed top-edge clearance. Front lower rim(365,490) [1.1266481,-.2385381,.8118254].

Open align [1.08,-.24,.815], insert[1.16,-.24,.815] visibly displaced scanner away. Followed new stop rule: withdrew immediately to1.03 WITHOUT closing. Thus estimated overhang did not establish swept lower-jaw clearance; insertion was not a first-grasp success.

Post-displacement rear[1.3826094,-.25855738,.8283955],front[1.183572,-.2504227,.8248131]. Withdrew base-.20, reoriented safely, closed empty preparation fingers, approached+.30, stage[1.32,-.25,.98]. Fresh rear[1.2858964,-.25680822,.82835793]. LowerZ.79 and BASE-.12 drew scanner off desk; clearing hand revealed scanner on floor. Stopped instead of floor recovery.

Lesson: neither nominal BASE-only sequence nor interpolated 6–7cm apparent overhang suffices. Desk bevel/face samples and scanner yaw make scalar forward difference uncertain; assess actual jaw swept volume and scanner-bottom height. More draw can eject scanner rather than fix insertion. Do not increase draw blindly after an insertion failure.

Terminal receipt scanner-run-007-instance237-a12/receipt_01792138584909317000_2c69dc48a0fc4dffbd7203c358c03123.json under scanner-run-007-p6-93a5c8 cache.
