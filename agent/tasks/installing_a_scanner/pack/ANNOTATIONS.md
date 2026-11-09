# Public human annotation summary

Pinned dataset `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three first available demonstrations with TRAIN instance>=20, excluding evaluation11–19 and practice10. Labels are annotations, not contact sensors. Durations use clipped half-open frame intervals at30Hz. Missing coarse annotations are reported, not synthesized.

## Episode18411 / TRAIN20

Length137.333s; valid interval[0, 4120]; raw ID920200; `annotations/task-0092/episode_00920200.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 720] → [[0, 720]]|24.000|move to|[['scanner']] / []|
|[720, 1841] → [[720, 1841]]|37.367|push to|[['scanner', 'desk']] / ['scanner']|
|[1841, 2190] → [[1841, 2190]]|11.633|pick up from|[['scanner', 'desk']] / ['scanner']|
|[2190, 2910] → [[2190, 2910]]|24.000|move to|[['laptop']] / []|
|[2910, 3240] → [[2910, 3240]]|11.000|turn on switch|[['scanner']] / ['scanner']|
|[3240, 4110] → [[3240, 4110]]|29.000|place on|[['scanner', 'desk']] / ['scanner']|

First annotated manipulation: **push to**, objects `[['scanner', 'desk']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode18412 / TRAIN21

Length127.133s; valid interval[0, 3814]; raw ID920210; `annotations/task-0092/episode_00920210.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 450] → [[0, 450]]|15.000|move to|[['scanner']] / []|
|[450, 2216] → [[450, 2216]]|58.867|push to|[['scanner', 'desk']] / ['scanner']|
|[2216, 2370] → [[2216, 2370]]|5.133|pick up from|[['scanner', 'desk']] / ['scanner']|
|[2370, 2970] → [[2370, 2970]]|20.000|move to|[['laptop']] / []|
|[2970, 3210] → [[2970, 3210]]|8.000|turn on switch|[['scanner']] / ['scanner']|
|[3210, 3810] → [[3210, 3810]]|20.000|place on|[['scanner', 'desk']] / ['scanner']|

First annotated manipulation: **push to**, objects `[['scanner', 'desk']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode18413 / TRAIN22

Length106.900s; valid interval[0, 3207]; raw ID920220; `annotations/task-0092/episode_00920220.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 1140] → [[0, 1140]]|38.000|move to|[['scanner']] / []|
|[1140, 1557] → [[1140, 1557]]|13.900|push to|[['scanner', 'desk']] / ['scanner']|
|[1557, 2100] → [[1557, 2100]]|18.100|pick up from|[['scanner', 'desk']] / ['scanner']|
|[2100, 2910] → [[2100, 2910]]|27.000|move to|[['laptop']] / []|
|[2910, 3000] → [[2910, 3000]]|3.000|turn on switch|[['scanner']] / ['scanner']|
|[3000, 3207] → [[3000, 3207]]|6.900|place on|[['scanner', 'desk']] / ['scanner']|

First annotated manipulation: **push to**, objects `[['scanner', 'desk']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Shared order and decision points

Shared ordered motif (longest common subsequence of fine labels; optional/repeated stages may be omitted): **move to → push to → pick up from → move to → turn on switch → place on**. This is a descriptive motif, not a compulsory policy.

Use TASK.md to decide required object counts, common destinations, closures, cooking/cleaning or attachment conditions. Compare the per-episode first manipulation and partner objects before choosing which object to handle first. Remeasure current geometry, reachability and clearance; verify object motion, supported release and retention separately from TCP completion. Label timing is not a physical contact or success guarantee.
