# Public human annotation summary

Pinned dataset `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three first available demonstrations with TRAIN instance>=20, excluding evaluation11–19 and practice10. Labels are annotations, not contact sensors. Durations use clipped half-open frame intervals at30Hz. Missing coarse annotations are reported, not synthesized.

## Episode15609 / TRAIN21

Length74.333s; valid interval[0, 2230]; raw ID780210; `annotations/task-0078/episode_00780210.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 150] → [[0, 150]]|5.000|move to|[['cabinet_door']] / []|
|[150, 657] → [[150, 657]]|16.900|pick up from|[['cabinet_door', 'floors']] / ['cabinet_door']|
|[657, 810] → [[657, 810]]|5.100|move to|[['cabinet_base']] / []|
|[810, 1020] → [[810, 1020]]|7.000|tip over|[['cabinet_base']] / ['cabinet_base']|
|[1020, 1890] → [[1020, 1890]]|29.000|place on|[['cabinet_door', 'cabinet_base']] / ['cabinet_door']|
|[1890, 2190] → [[1890, 2190]]|10.000|attach|[['cabinet_door', 'cabinet_base']] / ['cabinet_door']|

First annotated manipulation: **pick up from**, objects `[['cabinet_door', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode15610 / TRAIN23

Length139.000s; valid interval[0, 4170]; raw ID780230; `annotations/task-0078/episode_00780230.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 420] → [[0, 420]]|14.000|move to|[['cabinet_door']] / []|
|[420, 930] → [[420, 930]]|17.000|pick up from|[['cabinet_door', 'floors']] / ['cabinet_door']|
|[930, 1860] → [[930, 1860]]|31.000|move to|[['cabinet_base']] / []|
|[1860, 2100] → [[1860, 2100]]|8.000|tip over|[['cabinet_base']] / ['cabinet_base']|
|[2100, 2325] → [[2100, 2325]]|7.500|move to|[['cabinet_base']] / []|
|[2325, 3441] → [[2325, 3441]]|37.200|place on|[['cabinet_door', 'cabinet_base']] / ['cabinet_door']|
|[3441, 4170] → [[3441, 4170]]|24.300|attach|[['cabinet_door', 'cabinet_base']] / ['cabinet_door']|

First annotated manipulation: **pick up from**, objects `[['cabinet_door', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode15611 / TRAIN24

Length106.867s; valid interval[0, 3206]; raw ID780240; `annotations/task-0078/episode_00780240.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 180] → [[0, 180]]|6.000|move to|[['cabinet_door']] / []|
|[180, 550] → [[180, 550]]|12.333|pick up from|[['cabinet_door', 'floors']] / ['cabinet_door']|
|[550, 1110] → [[550, 1110]]|18.667|move to|[['cabinet_base']] / []|
|[1110, 1523] → [[1110, 1523]]|13.767|turn to|[['cabinet_base']] / ['cabinet_base']|
|[1523, 2000] → [[1523, 2000]]|15.900|tip over|[['cabinet_base']] / ['cabinet_base']|
|[2000, 2700] → [[2000, 2700]]|23.333|place on|[['cabinet_door', 'cabinet_base']] / ['cabinet_door']|
|[2700, 3180] → [[2700, 3180]]|16.000|attach|[['cabinet_door', 'cabinet_base']] / ['cabinet_door']|

First annotated manipulation: **pick up from**, objects `[['cabinet_door', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Shared order and decision points

Shared ordered motif (longest common subsequence of fine labels; optional/repeated stages may be omitted): **move to → pick up from → move to → tip over → place on → attach**. This is a descriptive motif, not a compulsory policy.

Use TASK.md to decide required object counts, common destinations, closures, cooking/cleaning or attachment conditions. Compare the per-episode first manipulation and partner objects before choosing which object to handle first. Remeasure current geometry, reachability and clearance; verify object motion, supported release and retention separately from TCP completion. Label timing is not a physical contact or success guarantee.
