# Hard-segment human proprioception
BODY axes: forward,left,up metres; angles/joints radians; EEF quaternions xyzw. The EEF is the rigid TCP origin used by our state, not a sensed contact point. Grip width is sum of measured finger travel, not a grasp sensor.
**Timing:** for RGB frame n, position/camera groups use source row n−1; velocity and requested grip use n−2. Source-reported lag, not simultaneous shutter/contact proof. Closing and pre-release samples are **contact candidates**, never measured contact.
**Base/target:** 61D has no absolute base or object pose. We integrate BODY velocities into an episode-start planar estimate. For pictures only, nail location is a manually selected public RGBD point at hang start, propagated using odometry (drift; flat-base assumption). Other task target poses remain unavailable/null; dense RGB replaces unsupported numerical guesses. Target orientation and true base pose are unavailable. A nail reference is NOT a grasp location.
**Pads:** both hands’ pad-ray reference endpoints use static FK and reconstructed model-local finger offsets (public robot self-state geometry from practice v4-a06); not deformable contact measurements. No hidden world/scorer/contact fields are loaded.
Use examples as posture/approach comparisons, NEVER replay historical coordinates or out-of-limit joints blindly. Re-measure your own RGBD.

## Episode6846 / TRAIN71

|RGB frame / phase|Right TCP BODY m|Right width mm|Estimated nail BODY m|
|---|---|---:|---|
|940 / left_pre_close|[0.3711, -0.3927, 0.5389]|100.0|[-0.75, 0.956, 1.702]|
|960 / left_closing_contact_candidate|[0.3711, -0.3927, 0.5389]|100.0|[-0.749, 0.956, 1.702]|
|1000 / left_post_close_lift_candidate|[0.369, -0.3929, 0.5375]|100.0|[-0.707, 0.981, 1.702]|
|1211 / right_pre_close|[0.5247, -0.228, 0.9139]|100.0|[0.269, 1.192, 1.702]|
|1231 / right_closing_contact_candidate|[0.5237, -0.2249, 0.9118]|20.4|[0.269, 1.192, 1.702]|
|1271 / right_post_close_lift_candidate|[0.5249, -0.2265, 0.9145]|17.1|[0.264, 1.193, 1.702]|
|1984 / attach_approach|[0.6682, -0.0344, 1.4566]|17.1|[0.663, 0.115, 1.702]|
|2010 / pre_release_contact_candidate|[0.6559, -0.0263, 1.4421]|16.8|[0.663, 0.114, 1.702]|
|2014 / release_command|[0.6567, -0.0273, 1.4393]|16.8|[0.663, 0.114, 1.702]|
|2029 / release_in_progress|[0.6756, -0.0487, 1.4372]|100.0|[0.694, 0.13, 1.702]|
|2059 / post_release|[0.6127, -0.0292, 1.3256]|100.0|[0.793, 0.181, 1.702]|

## Episode6854 / TRAIN88

|RGB frame / phase|Right TCP BODY m|Right width mm|Estimated nail BODY m|
|---|---|---:|---|
|930 / right_pre_close|[0.8187, -0.2589, 1.0554]|99.9|[0.381, 1.383, 1.702]|
|950 / right_closing_contact_candidate|[0.8189, -0.2587, 1.0551]|12.0|[0.368, 1.382, 1.702]|
|990 / right_post_close_lift_candidate|[0.814, -0.2586, 1.0764]|12.0|[0.386, 1.382, 1.702]|
|1816 / attach_approach|[0.6213, -0.057, 1.4536]|12.0|[0.66, 0.139, 1.702]|
|1842 / pre_release_contact_candidate|[0.5672, -0.0517, 1.4449]|11.5|[0.66, 0.124, 1.702]|
|1846 / release_command|[0.5693, -0.0493, 1.4437]|11.5|[0.66, 0.124, 1.702]|
|1861 / release_in_progress|[0.6228, -0.0583, 1.4524]|99.2|[0.66, 0.124, 1.702]|
|1891 / post_release|[0.6172, -0.0571, 1.4021]|100.0|[0.807, 0.189, 1.702]|

## Episode6863 / TRAIN110

|RGB frame / phase|Right TCP BODY m|Right width mm|Estimated nail BODY m|
|---|---|---:|---|
|696 / right_pre_close|[0.8687, -0.3025, 1.0397]|99.9|[-0.565, 1.266, 1.705]|
|716 / right_closing_contact_candidate|[0.8683, -0.303, 1.0396]|14.3|[-0.563, 1.267, 1.705]|
|756 / right_post_close_lift_candidate|[0.8672, -0.3032, 1.0547]|11.6|[-0.56, 1.268, 1.705]|
|1923 / attach_approach|[0.7422, -0.0103, 1.4192]|11.7|[0.75, 0.13, 1.705]|
|1949 / pre_release_contact_candidate|[0.6813, -0.0163, 1.3939]|11.1|[0.749, 0.13, 1.705]|
|1953 / release_command|[0.6823, -0.016, 1.3975]|11.1|[0.749, 0.13, 1.705]|
|1968 / release_in_progress|[0.7548, -0.015, 1.42]|100.0|[0.749, 0.131, 1.705]|
|1998 / post_release|[0.7564, -0.0161, 1.4193]|100.0|[0.759, 0.138, 1.705]|
