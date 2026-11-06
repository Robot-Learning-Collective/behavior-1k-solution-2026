# Public human annotations
Pinned HF `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three demonstrations, TRAIN>=20; none is dev11–19. Durations use half-open frame intervals /30, clipped to episode length; labels are not sensed contact. Coarse labels are original primitive annotations, not invented stages.

## Episode6846 / TRAIN71

Length70.533s; annotation valid window[30, 2100]. Raw ID340710; `annotations/task-0034/episode_00340710.json`.

### Coarse

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[30, 1092]]|35.400|pick up from|[['poster_73', 'bar_egwapq_0']]|
|[[1092, 2100]]|33.600|hang|[['poster_73', 'wall_nail_wlnail_1']]|

### Fine

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[30, 729]]|23.300|move to|[['poster_73']]|
|[[729, 1092]]|12.100|pick up from|[['poster_73', 'bar_egwapq_0']]|
|[[1092, 1482]]|13.000|hand over|[['poster_73', 'left', 'right']]|
|[[1483, 1576]]|3.100|move to|[['wall_nail_wlnail_1']]|
|[[1576, 2100]]|17.467|hang|[['poster_73', 'wall_nail_wlnail_1']]|

## Episode6854 / TRAIN88

Length65.000s; annotation valid window[0, 1950]. Raw ID340880; `annotations/task-0034/episode_00340880.json`.

### Coarse

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[0, 1288]]|42.933|pick up from|[['poster_73', 'bar_egwapq_0']]|
|[[1289, 1950]]|22.033|hang|[['poster_73', 'wall_nail_wlnail_1']]|

### Fine

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[0, 688]]|22.933|move to|[['poster_73']]|
|[[688, 1288]]|20.000|pick up from|[['poster_73', 'bar_egwapq_0']]|
|[[1289, 1410]]|4.033|move to|[['wall_nail_wlnail_1']]|
|[[1410, 1950]]|18.000|hang|[['poster_73', 'wall_nail_wlnail_1']]|

## Episode6863 / TRAIN110

Length70.967s; annotation valid window[22, 2099]. Raw ID341100; `annotations/task-0034/episode_00341100.json`.

### Coarse

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[22, 852]]|27.667|pick up from|[['poster_73', 'bar_egwapq_0']]|
|[[852, 2099]]|41.567|hang|[['poster_73', 'wall_nail_wlnail_1']]|

### Fine

|Frames|Seconds|Label|Objects|
|---|---:|---|---|
|[[22, 449]]|14.233|move to|[['poster_73']]|
|[[449, 852]]|13.433|pick up from|[['poster_73', 'bar_egwapq_0']]|
|[[852, 1234]]|12.733|move to|[['wall_nail_wlnail_1']]|
|[[1234, 2099]]|28.833|hang|[['poster_73', 'wall_nail_wlnail_1']]|

## Common order and decisions

All three: approach poster → lift from countertop → carry to wall nail → hang.6846 inserts left-to-right handover;6854/6863 use direct right grasp. Choose a visible accessible nail; the goal permits any nail, not a fixed historical coordinate. Acquisition/retention must be visually established before navigating. Near the nail: align and support the poster before release; separate opening from withdrawal and re-check retention. Public RGBD shows a nonzero front-to-wall stand-off; the visible front is not the back/mount, so zero front-gap is not a target. Wrist/base/torso configurations vary; no single average joint pose is a recipe.
