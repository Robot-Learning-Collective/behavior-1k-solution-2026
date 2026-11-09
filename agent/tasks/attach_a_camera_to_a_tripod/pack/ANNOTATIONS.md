# Public human annotations
Pinned HF `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three demonstrations, TRAIN>=20; none is dev11–19. Durations use half-open frame intervals /30, clipped to episode length; labels are not sensed contact. Coarse labels are original primitive annotations, not invented stages.

## Episode7016 / TRAIN20

Length141.900s; annotation valid window[0, 4197]. Raw ID350200; `annotations/task-0035/episode_00350200.json`.

### Coarse

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[0, 1595]]|53.167|pick up from|[['digital_camera_87', 'floors_nlswvt_0']]|
|[[2254, 4197]]|64.767|attach|[['digital_camera_87', 'camera_tripod_86']]|

### Fine

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[0, 401]]|13.367|move to|[['digital_camera_87']]|
|[[401, 1595]]|39.800|pick up from|[['digital_camera_87', 'floors_nlswvt_0']]|
|[[2254, 2522]]|8.933|move to|[['camera_tripod_86']]|
|[[2522, 2877]]|11.833|hold|[['camera_tripod_86']]|
|[[3707, 4053]]|11.533|attach|[['digital_camera_87', 'camera_tripod_86']]|
|[[4053, 4197]]|4.800|release|[['camera_tripod_86']]|

## Episode7017 / TRAIN21

Length147.200s; annotation valid window[0, 4284]. Raw ID350210; `annotations/task-0035/episode_00350210.json`.

### Coarse

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[0, 2004]]|66.800|pick up from|[['digital_camera_87', 'floors_nlswvt_0']]|
|[[2004, 4284]]|76.000|attach|[['digital_camera_87', 'camera_tripod_86']]|

### Fine

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[0, 387]]|12.900|move to|[['digital_camera_87']]|
|[[387, 2004]]|53.900|pick up from|[['digital_camera_87', 'floors_nlswvt_0']]|
|[[2004, 3076]]|35.733|move to|[['camera_tripod_86']]|
|[[3337, 3688]]|11.700|hold|[['camera_tripod_86']]|
|[[3689, 4141]]|15.067|attach|[['digital_camera_87', 'camera_tripod_86']]|
|[[4141, 4284]]|4.767|release|[['camera_tripod_86']]|

## Episode7018 / TRAIN22

Length120.533s; annotation valid window[32, 3599]. Raw ID350220; `annotations/task-0035/episode_00350220.json`.

### Coarse

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[32, 1806]]|59.133|pick up from|[['digital_camera_87', 'floors_nlswvt_0']]|
|[[1806, 3599]]|59.767|attach|[['digital_camera_87', 'camera_tripod_86']]|

### Fine

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[32, 719]]|22.900|move to|[['digital_camera_87']]|
|[[719, 1806]]|36.233|pick up from|[['digital_camera_87', 'floors_nlswvt_0']]|
|[[1806, 2185]]|12.633|move to|[['camera_tripod_86']]|
|[[2712, 3002]]|9.667|hold|[['camera_tripod_86']]|
|[[3002, 3212]]|7.000|attach|[['digital_camera_87', 'camera_tripod_86']]|
|[[3212, 3599]]|12.900|release|[['camera_tripod_86']]|

## Common order and decisions

Read the explicit object relations in TASK.md, then compare the ordered fine labels above. Different demonstrations may manipulate different instances/order; labels are not guaranteed contact. Navigation and unlabelled gaps between manipulation segments are also densely pictured rather than assigned invented actions. Measure fresh geometry before grasp/door/press/attach/release; validate visible object motion and retention separately from TCP achievement.

### Camera-specific common sequence

All three fine sequences: approach camera on floor → pick camera up → approach tripod → hold tripod → attach camera → release tripod. Dense release/attachment views show left-hand camera handling and right-hand tripod support in these examples. Stabilizing the tripod and aligning the mounting faces are separate from acquiring the camera. Choose whether support is needed from fresh geometry, not from these historic coordinates. Confirm camera retention before withdrawing either hand. Several annotation gaps are substantial (e.g.7016 frames1595–2254 and2877–3707); dense RGB/proprio covers them without inventing labels. Different episode lengths and acquisition times are not a universal timing recipe.
