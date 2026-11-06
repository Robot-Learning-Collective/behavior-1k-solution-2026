# Hard-segment human proprioception
BODY axes: forward,left,up metres; angles/joints radians; EEF quaternions xyzw. The EEF is the rigid TCP origin used by our state, not a sensed contact point. Grip width is sum of measured finger travel, not a grasp sensor.
**Timing:** for RGB frame n, position/camera groups use source row n−1; velocity and requested grip use n−2. Source-reported lag, not simultaneous shutter/contact proof. Closing and pre-release samples are **contact candidates**, never measured contact.
**Base/target:** 61D has no absolute base or object pose. We integrate BODY velocities into an episode-start planar estimate. For pictures only, nail location is a manually selected public RGBD point at hang start, propagated using odometry (drift; flat-base assumption). Other task target poses remain unavailable/null; dense RGB replaces unsupported numerical guesses. Target orientation and true base pose are unavailable. A nail reference is NOT a grasp location.
**Pads:** both hands’ pad-ray reference endpoints use static FK and reconstructed model-local finger offsets (public robot self-state geometry from practice v4-a06); not deformable contact measurements. No hidden world/scorer/contact fields are loaded.
Use examples as posture/approach comparisons, NEVER replay historical coordinates or out-of-limit joints blindly. Re-measure your own RGBD.

## Episode7016 / TRAIN20

|RGB frame / phase|Right TCP BODY m|Right width mm|Estimated nail BODY m|
|---|---|---:|---|
|1398 / left_pre_close|[0.7077, -0.0874, 0.2677]|100.0|unavailable|
|1418 / left_closing_contact_candidate|[0.7077, -0.0873, 0.2677]|100.0|unavailable|
|1458 / left_post_close_lift_candidate|[0.7077, -0.0874, 0.2677]|100.0|unavailable|
|2842 / right_pre_close|[0.7086, -0.3146, 0.9654]|99.9|unavailable|
|2862 / right_closing_contact_candidate|[0.6938, -0.3227, 0.9372]|40.1|unavailable|
|2902 / right_post_close_lift_candidate|[0.7114, -0.3172, 0.9722]|40.1|unavailable|
|3957 / left_pre_open|[0.647, -0.0639, 0.9627]|40.2|unavailable|
|3972 / left_open_command|[0.6484, -0.0631, 0.9661]|40.3|unavailable|
|3979 / right_pre_open|[0.6443, -0.0672, 0.9536]|40.4|unavailable|
|3994 / right_open_command|[0.6449, -0.0673, 0.9546]|40.3|unavailable|
|4017 / left_post_open_candidate|[0.649, -0.0628, 0.9679]|99.9|unavailable|
|4039 / right_post_open_candidate|[0.6488, -0.0628, 0.9682]|99.9|unavailable|

## Episode7017 / TRAIN21

|RGB frame / phase|Right TCP BODY m|Right width mm|Estimated nail BODY m|
|---|---|---:|---|
|1639 / left_pre_close|[0.6192, -0.1305, 0.1004]|100.0|unavailable|
|1659 / left_closing_contact_candidate|[0.6193, -0.1306, 0.1005]|100.0|unavailable|
|1699 / left_post_close_lift_candidate|[0.619, -0.1299, 0.1005]|100.0|unavailable|
|3442 / right_pre_close|[0.6065, -0.0935, 0.8933]|99.9|unavailable|
|3462 / right_closing_contact_candidate|[0.6145, -0.0946, 0.9009]|34.2|unavailable|
|3502 / right_post_close_lift_candidate|[0.635, -0.0922, 0.9441]|33.6|unavailable|
|4051 / left_pre_open|[0.5738, -0.1096, 0.9054]|33.6|unavailable|
|4066 / left_open_command|[0.5738, -0.11, 0.9052]|33.6|unavailable|
|4111 / left_post_open_candidate|[0.5732, -0.1066, 0.9057]|33.6|unavailable|
|4156 / right_pre_open|[0.5734, -0.1066, 0.9059]|33.6|unavailable|
|4171 / right_open_command|[0.5734, -0.1066, 0.9059]|33.6|unavailable|
|4216 / right_post_open_candidate|[0.564, -0.1121, 0.8836]|100.0|unavailable|

## Episode7018 / TRAIN22

|RGB frame / phase|Right TCP BODY m|Right width mm|Estimated nail BODY m|
|---|---|---:|---|
|1157 / left_pre_close|[0.5379, -0.1849, 0.0992]|100.0|unavailable|
|1177 / left_closing_contact_candidate|[0.538, -0.1849, 0.0993]|100.0|unavailable|
|1217 / left_post_close_lift_candidate|[0.5381, -0.1847, 0.0995]|100.0|unavailable|
|2984 / right_pre_close|[0.603, -0.0958, 0.9073]|100.0|unavailable|
|3004 / right_closing_contact_candidate|[0.6232, -0.0973, 0.9239]|34.2|unavailable|
|3044 / right_post_close_lift_candidate|[0.623, -0.0955, 0.9239]|34.2|unavailable|
|3176 / left_pre_open|[0.6218, -0.0965, 0.9219]|34.2|unavailable|
|3191 / left_open_command|[0.6218, -0.0965, 0.9219]|34.2|unavailable|
|3216 / right_pre_open|[0.6218, -0.0965, 0.9219]|34.2|unavailable|
|3231 / right_open_command|[0.6218, -0.0965, 0.9219]|34.2|unavailable|
|3236 / left_post_open_candidate|[0.6194, -0.0971, 0.9153]|94.0|unavailable|
|3276 / right_post_open_candidate|[0.6133, -0.101, 0.9008]|100.0|unavailable|
