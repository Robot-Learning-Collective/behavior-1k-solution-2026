# Public human annotation summary

Pinned dataset `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three first available demonstrations with TRAIN instance>=20, excluding evaluation11–19 and practice10. Labels are annotations, not contact sensors. Durations use clipped half-open frame intervals at30Hz. Missing coarse annotations are reported, not synthesized.

## Episode13010 / TRAIN20

Length355.133s; valid interval[0, 10654]; raw ID650200; `annotations/task-0065/episode_00650200.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 150] → [[0, 150]]|5.000|move to|[['door']] / []|
|[150, 750] → [[150, 750]]|20.000|open door|[['door']] / []|
|[750, 1680] → [[750, 1680]]|31.000|move to|[['car']] / []|
|[1680, 3450] → [[1680, 3450]]|59.000|open lid|[['car']] / ['car']|
|[3450, 4410] → [[3450, 4410]]|32.000|pick up from|[['briefcase', 'car']] / ['briefcase']|
|[4410, 5515] → [[4410, 5515]]|36.833|pick up from|[['satchel', 'car']] / ['satchel']|
|[5515, 6139] → [[5515, 6139]]|20.800|move to|[['floors']] / []|
|[6139, 6627] → [[6139, 6627]]|16.267|place on|[['satchel', 'floors']] / ['satchel']|
|[6627, 7112] → [[6627, 7112]]|16.167|close lid|[['car']] / ['car']|
|[7112, 7654] → [[7112, 7654]]|18.067|pick up from|[['satchel', 'floors']] / ['satchel']|
|[7654, 9450] → [[7654, 9450]]|59.867|move to|[['sofa']] / []|
|[9450, 9810] → [[9450, 9810]]|12.000|place on|[['satchel', 'floors']] / ['satchel']|
|[9810, 10650] → [[9810, 10650]]|28.000|place on|[['briefcase', 'floors']] / ['briefcase']|

First annotated manipulation: **open door**, objects `[['door']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode13011 / TRAIN21

Length343.000s; valid interval[0, 10289]; raw ID650210; `annotations/task-0065/episode_00650210.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 510] → [[0, 510]]|17.000|move to|[['door']] / []|
|[510, 1290] → [[510, 1290]]|26.000|open door|[['door']] / []|
|[1290, 2280] → [[1290, 2280]]|33.000|move to|[['car']] / []|
|[2280, 3570] → [[2280, 3570]]|43.000|open lid|[['car']] / ['car']|
|[3570, 4760] → [[3570, 4760]]|39.667|pick up from|[['briefcase', 'car']] / ['briefcase']|
|[4760, 5460] → [[4760, 5460]]|23.333|pick up from|[['satchel', 'car']] / ['satchel']|
|[5460, 6160] → [[5460, 6160]]|23.333|move to|[['floors']] / []|
|[6160, 6433] → [[6160, 6433]]|9.100|place on|[['satchel', 'floors']] / ['satchel']|
|[6433, 6857] → [[6433, 6857]]|14.133|move to|[['car']] / []|
|[6857, 7097] → [[6857, 7097]]|8.000|close lid|[['car']] / ['car']|
|[7097, 7555] → [[7097, 7555]]|15.267|pick up from|[['satchel', 'floors']] / ['satchel']|
|[7555, 9398] → [[7555, 9398]]|61.433|move to|[['sofa']] / []|
|[9398, 9573] → [[9398, 9573]]|5.833|place on|[['satchel', 'floors']] / ['satchel']|
|[9573, 10289] → [[9573, 10289]]|23.867|place on|[['briefcase', 'floors']] / ['briefcase']|

First annotated manipulation: **open door**, objects `[['door']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode13012 / TRAIN22

Length611.700s; valid interval[0, 18351]; raw ID650220; `annotations/task-0065/episode_00650220.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 630] → [[0, 630]]|21.000|move to|[['door']] / []|
|[630, 1110] → [[630, 1110]]|16.000|open door|[['door']] / []|
|[1110, 2280] → [[1110, 2280]]|39.000|move to|[['car']] / []|
|[2280, 3870] → [[2280, 3870]]|53.000|open lid|[['car']] / ['car']|
|[3870, 7170] → [[3870, 7170]]|110.000|pick up from|[['briefcase', 'car']] / ['briefcase']|
|[7170, 9948] → [[7170, 9948]]|92.600|pick up from|[['satchel', 'car']] / ['satchel']|
|[9948, 11413] → [[9948, 11413]]|48.833|place on|[['satchel', 'floors']] / ['satchel']|
|[11413, 12508] → [[11413, 12508]]|36.500|move to|[['car']] / []|
|[12508, 12810] → [[12508, 12810]]|10.067|close lid|[['car']] / ['car']|
|[12810, 14037] → [[12810, 14037]]|40.900|pick up from|[['satchel', 'floors']] / ['satchel']|
|[14037, 15729] → [[14037, 15729]]|56.400|move to|[['sofa']] / []|
|[15729, 16347] → [[15729, 16347]]|20.600|place on|[['satchel', 'floors']] / ['satchel']|
|[16347, 18330] → [[16347, 18330]]|66.100|place on|[['briefcase', 'floors']] / ['briefcase']|

First annotated manipulation: **open door**, objects `[['door']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Shared order and decision points

Shared ordered motif (longest common subsequence of fine labels; optional/repeated stages may be omitted): **move to → open door → move to → open lid → pick up from → pick up from → move to → close lid → pick up from → move to → place on → place on**. This is a descriptive motif, not a compulsory policy.

Use TASK.md to decide required object counts, common destinations, closures, cooking/cleaning or attachment conditions. Compare the per-episode first manipulation and partner objects before choosing which object to handle first. Remeasure current geometry, reachability and clearance; verify object motion, supported release and retention separately from TCP completion. Label timing is not a physical contact or success guarantee.
