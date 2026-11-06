# Public human annotation summary

Pinned dataset `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three first available demonstrations with TRAIN instance>=20, excluding evaluation11–19 and practice10. Labels are annotations, not contact sensors. Durations use clipped half-open frame intervals at30Hz. Missing coarse annotations are reported, not synthesized.

## Episode12612 / TRAIN20

Length128.400s; valid interval[0, 3850]; raw ID630200; `annotations/task-0063/episode_00630200.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 531] → [[0, 531]]|17.700|move to|[['fire_alarm']] / []|
|[531, 1599] → [[531, 1599]]|35.600|pick up from|[['fire_alarm', 'coffee_table']] / ['fire_alarm']|
|[1599, 1724] → [[1599, 1724]]|4.167|place on|[['fire_alarm', 'coffee_table']] / ['fire_alarm']|
|[1724, 2100] → [[1724, 2100]]|12.533|pick up from|[['fire_alarm', 'coffee_table']] / ['fire_alarm']|
|[2100, 3236] → [[2100, 3236]]|37.867|move to|[['wall_nail']] / []|
|[3236, 3840] → [[3236, 3840]]|20.133|attach|[['fire_alarm', 'wall_nail']] / ['fire_alarm']|

First annotated manipulation: **pick up from**, objects `[['fire_alarm', 'coffee_table']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode12613 / TRAIN21

Length84.967s; valid interval[0, 2549]; raw ID630210; `annotations/task-0063/episode_00630210.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 944] → [[0, 944]]|31.467|move to|[['fire_alarm']] / []|
|[945, 1470] → [[945, 1470]]|17.500|pick up from|[['fire_alarm', 'coffee_table']] / ['fire_alarm']|
|[1470, 2190] → [[1470, 2190]]|24.000|move to|[['wall_nail']] / []|
|[2190, 2520] → [[2190, 2520]]|11.000|attach|[['fire_alarm', 'wall_nail']] / ['fire_alarm']|

First annotated manipulation: **pick up from**, objects `[['fire_alarm', 'coffee_table']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode12614 / TRAIN24

Length86.100s; valid interval[0, 2583]; raw ID630240; `annotations/task-0063/episode_00630240.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 420] → [[0, 420]]|14.000|move to|[['fire_alarm']] / []|
|[420, 820] → [[420, 820]]|13.333|pick up from|[['fire_alarm', 'coffee_table']] / ['fire_alarm']|
|[820, 1020] → [[820, 1020]]|6.667|place on|[['fire_alarm', 'coffee_table']] / ['fire_alarm']|
|[1020, 1294] → [[1020, 1294]]|9.133|pick up from|[['fire_alarm', 'coffee_table']] / ['fire_alarm']|
|[1260, 2100] → [[1260, 2100]]|28.000|move to|[['wall_nail']] / []|
|[2100, 2580] → [[2100, 2580]]|16.000|attach|[['fire_alarm', 'wall_nail']] / ['fire_alarm']|

First annotated manipulation: **pick up from**, objects `[['fire_alarm', 'coffee_table']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Shared order and decision points

Shared ordered motif (longest common subsequence of fine labels; optional/repeated stages may be omitted): **move to → pick up from → move to → attach**. This is a descriptive motif, not a compulsory policy.

Use TASK.md to decide required object counts, common destinations, closures, cooking/cleaning or attachment conditions. Compare the per-episode first manipulation and partner objects before choosing which object to handle first. Remeasure current geometry, reachability and clearance; verify object motion, supported release and retention separately from TCP completion. Label timing is not a physical contact or success guarantee.
