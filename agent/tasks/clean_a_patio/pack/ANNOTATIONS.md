# Public human annotation summary

Pinned dataset `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three first available demonstrations with TRAIN instance>=20, excluding evaluation11–19 and practice10. Labels are annotations, not contact sensors. Durations use clipped half-open frame intervals at30Hz. Missing coarse annotations are reported, not synthesized.

## Episode7217 / TRAIN20

Length394.200s; valid interval[0, 11820]; raw ID360200; `annotations/task-0036/episode_00360200.json`.

### Coarse

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 2019] → [[0, 2019]]|67.300|pick up from|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[2028, 3834] → [[2028, 3834]]|60.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[[3834, 4422], 6361] → [[3834, 6361]] **DERIVED envelope of linked fine spans; malformed coarse source**|84.233|push to|[[['garden_chair_cottya_2', 'garden_chair_cottya_1', 'garden_chair_cottya_0'], 'robot']] / [['garden_chair_cottya_2', 'garden_chair_cottya_1', 'garden_chair_cottya_0']]|
|[[6361, 6694], 11190] → [[6361, 11190]] **DERIVED envelope of linked fine spans; malformed coarse source**|160.967|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[11310, 11820] → [[11310, 11820]]|17.000|place on|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 420] → [[0, 420]]|14.000|move to|[['broom_172']] / []|
|[420, 1773] → [[420, 1773]]|45.100|pick up from|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[1833, 2019] → [[1833, 2019]]|6.200|hold|[['broom_172']] / ['broom_172']|
|[2028, 2223] → [[2028, 2223]]|6.500|move to|[['mud']] / []|
|[2223, 2310] → [[2223, 2310]]|2.900|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[2310, 2406] → [[2310, 2406]]|3.200|move to|[['mud']] / []|
|[2406, 2523] → [[2406, 2523]]|3.900|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[2523, 2832] → [[2523, 2832]]|10.300|move to|[['mud']] / []|
|[2832, 2952] → [[2832, 2952]]|4.000|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[2952, 3013] → [[2952, 3013]]|2.033|move to|[['mud']] / []|
|[3013, 3034] → [[3013, 3034]]|0.700|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[3034, 3042] → [[3034, 3042]]|0.267|move to|[['mud']] / []|
|[3042, 3064] → [[3042, 3064]]|0.733|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[3064, 3136] → [[3064, 3136]]|2.400|move to|[['mud']] / []|
|[3136, 3172] → [[3136, 3172]]|1.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[3172, 3370] → [[3172, 3370]]|6.600|move to|[['mud']] / []|
|[3370, 3390] → [[3370, 3390]]|0.667|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[3390, 3421] → [[3390, 3421]]|1.033|move to|[['mud']] / []|
|[3421, 3445] → [[3421, 3445]]|0.800|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[3445, 3487] → [[3445, 3487]]|1.400|move to|[['mud']] / []|
|[3487, 3597] → [[3487, 3597]]|3.667|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[3597, 3759] → [[3597, 3759]]|5.400|move to|[['mud']] / []|
|[3759, 3834] → [[3759, 3834]]|2.500|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[[3834, 4422], [4702, 4789]] → [[3834, 4422], [4702, 4789]]|22.500|move to|[['garden_chair_cottya_2']] / []|
|[4422, 4702] → [[4422, 4702]]|9.333|release|[['broom_172']] / ['broom_172']|
|[4789, 5299] → [[4789, 5299]]|17.000|push to|[['garden_chair_cottya_2', 'robot']] / ['garden_chair_cottya_2']|
|[5299, 5509] → [[5299, 5509]]|7.000|move to|[['garden_chair_cottya_1']] / []|
|[5509, 5725] → [[5509, 5725]]|7.200|push to|[['garden_chair_cottya_1', 'robot']] / ['garden_chair_cottya_1']|
|[5725, 5947] → [[5725, 5947]]|7.400|move to|[['garden_chair_cottya_0']] / []|
|[5947, 6361] → [[5947, 6361]]|13.800|push to|[['garden_chair_cottya_0', 'robot']] / ['garden_chair_cottya_0']|
|[[6361, 6694], [7009, 7203]] → [[6361, 6694], [7009, 7203]]|17.567|move to|[['mud']] / []|
|[6694, 7009] → [[6694, 7009]]|10.500|hold|[['broom_172']] / ['broom_172']|
|[7203, 7258] → [[7203, 7258]]|1.833|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[7258, 7796] → [[7258, 7796]]|17.933|move to|[['mud']] / []|
|[7796, 7886] → [[7796, 7886]]|3.000|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[7886, 8328] → [[7886, 8328]]|14.733|move to|[['mud']] / []|
|[8334, 8403] → [[8334, 8403]]|2.300|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[8409, 10011] → [[8409, 10011]]|53.400|move to|[['mud']] / []|
|[10011, 10110] → [[10011, 10110]]|3.300|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[10110, 10364] → [[10110, 10364]]|8.467|move to|[['mud']] / []|
|[10364, 10400] → [[10364, 10400]]|1.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[10400, 10710] → [[10400, 10710]]|10.333|move to|[['mud']] / []|
|[10710, 10763] → [[10710, 10763]]|1.767|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[10763, 10794] → [[10763, 10794]]|1.033|move to|[['mud']] / []|
|[10794, 10860] → [[10794, 10860]]|2.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[10860, 11103] → [[10860, 11103]]|8.100|move to|[['mud']] / []|
|[11103, 11190] → [[11103, 11190]]|2.900|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[11310, 11418] → [[11310, 11418]]|3.600|release|[['broom_172']] / ['broom_172']|
|[11418, 11820] → [[11418, 11820]]|13.400|place on|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|

First annotated manipulation: **pick up from**, objects `[['broom_172', 'floors_ghetev_0']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode7218 / TRAIN22

Length362.900s; valid interval[3, 10887]; raw ID360220; `annotations/task-0036/episode_00360220.json`.

### Coarse

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[3, 1071] → [[3, 1071]]|35.600|pick up from|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[1071, 2074] → [[1071, 2074]]|33.433|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[[2074, 2667], 2940] → [[2074, 2940]] **DERIVED envelope of linked fine spans; malformed coarse source**|28.867|push to|[['garden_chair_lraplz_0', 'robot']] / ['garden_chair_lraplz_0']|
|[[2940, 2967], 3831] → [[2940, 3831]] **DERIVED envelope of linked fine spans; malformed coarse source**|29.700|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[3831, 4417] → [[3831, 4417]]|19.533|push to|[['garden_chair_cottya_0', 'robot']] / ['garden_chair_cottya_0']|
|[[4417, 4486], 6724] → [[4417, 6724]] **DERIVED envelope of linked fine spans; malformed coarse source**|76.900|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[[6724, 6880], 7290] → [[6724, 7290]] **DERIVED envelope of linked fine spans; malformed coarse source**|18.867|push to|[['garden_chair_cottya_2', 'robot']] / ['garden_chair_cottya_2']|
|[7290, 10390] → [[7290, 10390]]|103.333|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[10390, 10887] → [[10390, 10887]]|16.567|place on|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[3, 36] → [[3, 36]]|1.100|move to|[['broom_172']] / []|
|[36, 903] → [[36, 903]]|28.900|pick up from|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[903, 1071] → [[903, 1071]]|5.600|hold|[['broom_172']] / ['broom_172']|
|[1071, 1770] → [[1071, 1770]]|23.300|move to|[['mud']] / []|
|[1770, 1861] → [[1770, 1861]]|3.033|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[1861, 2014] → [[1861, 2014]]|5.100|move to|[['mud']] / []|
|[2014, 2074] → [[2014, 2074]]|2.000|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[[2074, 2667], [2760, 2781]] → [[2074, 2667], [2760, 2781]]|20.467|move to|[['garden_chair_lraplz_0']] / []|
|[2667, 2760] → [[2667, 2760]]|3.100|release|[['broom_172']] / ['broom_172']|
|[2781, 2940] → [[2781, 2940]]|5.300|push to|[['garden_chair_lraplz_0', 'robot']] / ['garden_chair_lraplz_0']|
|[[2940, 2967], [3079, 3108]] → [[2940, 2967], [3079, 3108]]|1.867|move to|[['mud']] / []|
|[2967, 3079] → [[2967, 3079]]|3.733|hold|[['broom_172']] / ['broom_172']|
|[3108, 3144] → [[3108, 3144]]|1.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[3144, 3687] → [[3144, 3687]]|18.100|move to|[['mud']] / []|
|[3687, 3831] → [[3687, 3831]]|4.800|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[3831, 4062] → [[3831, 4062]]|7.700|move to|[['garden_chair_cottya_0']] / []|
|[4062, 4116] → [[4062, 4116]]|1.800|release|[['broom_172']] / ['broom_172']|
|[4116, 4417] → [[4116, 4417]]|10.033|push to|[['garden_chair_cottya_0', 'robot']] / ['garden_chair_cottya_0']|
|[[4417, 4486], [4599, 4677]] → [[4417, 4486], [4599, 4677]]|4.900|move to|[['mud']] / []|
|[4486, 4599] → [[4486, 4599]]|3.767|hold|[['broom_172']] / ['broom_172']|
|[4677, 4749] → [[4677, 4749]]|2.400|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[4749, 4980] → [[4749, 4980]]|7.700|move to|[['mud']] / []|
|[4980, 5023] → [[4980, 5023]]|1.433|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[5023, 5226] → [[5023, 5226]]|6.767|move to|[['mud']] / []|
|[5226, 5436] → [[5226, 5436]]|7.000|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[5436, 5844] → [[5436, 5844]]|13.600|move to|[['mud']] / []|
|[5844, 5889] → [[5844, 5889]]|1.500|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[5889, 6138] → [[5889, 6138]]|8.300|move to|[['mud']] / []|
|[6138, 6186] → [[6138, 6186]]|1.600|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[6186, 6453] → [[6186, 6453]]|8.900|move to|[['mud']] / []|
|[6453, 6666] → [[6453, 6666]]|7.100|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[6666, 6687] → [[6666, 6687]]|0.700|move to|[['mud']] / []|
|[6687, 6724] → [[6687, 6724]]|1.233|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[[6724, 6880], [7017, 7059]] → [[6724, 6880], [7017, 7059]]|6.600|move to|[['garden_chair_cottya_2']] / []|
|[6880, 7017] → [[6880, 7017]]|4.567|release|[['broom_172']] / ['broom_172']|
|[7059, 7290] → [[7059, 7290]]|7.700|push to|[['garden_chair_cottya_2', 'robot']] / ['garden_chair_cottya_2']|
|[7290, 7449] → [[7290, 7449]]|5.300|hold|[['broom_172']] / ['broom_172']|
|[7449, 7509] → [[7449, 7509]]|2.000|move to|[['mud']] / []|
|[7509, 7575] → [[7509, 7575]]|2.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[7575, 8434] → [[7575, 8434]]|28.633|move to|[['mud']] / []|
|[8434, 8535] → [[8434, 8535]]|3.367|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[8535, 8563] → [[8535, 8563]]|0.933|move to|[['mud']] / []|
|[8563, 8617] → [[8563, 8617]]|1.800|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[8617, 9094] → [[8617, 9094]]|15.900|move to|[['mud']] / []|
|[9094, 9163] → [[9094, 9163]]|2.300|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[9163, 9349] → [[9163, 9349]]|6.200|move to|[['mud']] / []|
|[9349, 9436] → [[9349, 9436]]|2.900|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[9436, 9787] → [[9436, 9787]]|11.700|move to|[['mud']] / []|
|[9787, 9870] → [[9787, 9870]]|2.767|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[9870, 10030] → [[9870, 10030]]|5.333|move to|[['mud']] / []|
|[10030, 10132] → [[10030, 10132]]|3.400|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[10132, 10289] → [[10132, 10289]]|5.233|move to|[['mud']] / []|
|[10289, 10390] → [[10289, 10390]]|3.367|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[10390, 10450] → [[10390, 10450]]|2.000|release|[['broom_172']] / ['broom_172']|
|[10450, 10887] → [[10450, 10887]]|14.567|place on|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|

First annotated manipulation: **pick up from**, objects `[['broom_172', 'floors_ghetev_0']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode7219 / TRAIN24

Length468.633s; valid interval[11, 14058]; raw ID360240; `annotations/task-0036/episode_00360240.json`.

### Coarse

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[11, 1562] → [[11, 1562]]|51.700|pick up from|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[1565, 3942] → [[1565, 3942]]|79.233|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[[3942, 4113], 7614] → [[3942, 7614]] **DERIVED envelope of linked fine spans; malformed coarse source**|122.400|push to|[[['garden_chair_cottya_0', 'garden_chair_cottya_1', 'garden_chair_cottya_2', 'garden_chair_lraplz_0'], 'robot']] / [['garden_chair_cottya_0', 'garden_chair_cottya_1', 'garden_chair_cottya_2', 'garden_chair_lraplz_0']]|
|[[7614, 7841], 13290] → [[7614, 13290]] **DERIVED envelope of linked fine spans; malformed coarse source**|189.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[13290, 14058] → [[13290, 14058]]|25.600|place on|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[11, 324] → [[11, 324]]|10.433|move to|[['broom_172']] / []|
|[324, 1143] → [[324, 1143]]|27.300|pick up from|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[1143, 1562] → [[1143, 1562]]|13.967|hold|[['broom_172']] / ['broom_172']|
|[1565, 1710] → [[1565, 1710]]|4.833|move to|[['mud']] / []|
|[1710, 1967] → [[1710, 1967]]|8.567|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[1967, 2142] → [[1967, 2142]]|5.833|move to|[['mud']] / []|
|[2142, 2361] → [[2142, 2361]]|7.300|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[2361, 2829] → [[2361, 2829]]|15.600|move to|[['mud']] / []|
|[2829, 2895] → [[2829, 2895]]|2.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[2895, 2916] → [[2895, 2916]]|0.700|move to|[['mud']] / []|
|[2916, 2982] → [[2916, 2982]]|2.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[2982, 3198] → [[2982, 3198]]|7.200|move to|[['mud']] / []|
|[3198, 3289] → [[3198, 3289]]|3.033|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[3289, 3769] → [[3289, 3769]]|16.000|move to|[['mud']] / []|
|[3769, 3831] → [[3769, 3831]]|2.067|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[3831, 3875] → [[3831, 3875]]|1.467|move to|[['mud']] / []|
|[3875, 3942] → [[3875, 3942]]|2.233|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[[3942, 4113], [4365, 4435]] → [[3942, 4113], [4365, 4435]]|8.033|move to|[['garden_chair_cottya_0']] / []|
|[4113, 4365] → [[4113, 4365]]|8.400|release|[['broom_172']] / ['broom_172']|
|[4435, 5196] → [[4435, 5196]]|25.367|push to|[['garden_chair_cottya_0', 'robot']] / ['garden_chair_cottya_0']|
|[5196, 5409] → [[5196, 5409]]|7.100|move to|[['garden_chair_cottya_1']] / []|
|[5412, 5817] → [[5412, 5817]]|13.500|push to|[['garden_chair_cottya_1', 'robot']] / ['garden_chair_cottya_1']|
|[5817, 5976] → [[5817, 5976]]|5.300|move to|[['garden_chair_cottya_2']] / []|
|[5976, 6651] → [[5976, 6651]]|22.500|push to|[['garden_chair_cottya_2', 'robot']] / ['garden_chair_cottya_2']|
|[6651, 6936] → [[6651, 6936]]|9.500|move to|[['garden_chair_lraplz_0']] / []|
|[6936, 7614] → [[6936, 7614]]|22.600|push to|[['garden_chair_lraplz_0', 'robot']] / ['garden_chair_lraplz_0']|
|[[7614, 7841], [8322, 8553]] → [[7614, 7841], [8322, 8553]]|15.267|move to|[['mud']] / []|
|[7841, 8322] → [[7841, 8322]]|16.033|hold|[['broom_172']] / ['broom_172']|
|[8553, 8718] → [[8553, 8718]]|5.500|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[8718, 8964] → [[8718, 8964]]|8.200|move to|[['mud']] / []|
|[8964, 9120] → [[8964, 9120]]|5.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[9120, 9678] → [[9120, 9678]]|18.600|move to|[['mud']] / []|
|[9678, 9834] → [[9678, 9834]]|5.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[9834, 10380] → [[9834, 10380]]|18.200|move to|[['mud']] / []|
|[10380, 10803] → [[10380, 10803]]|14.100|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[10803, 11214] → [[10803, 11214]]|13.700|move to|[['mud']] / []|
|[11214, 11331] → [[11214, 11331]]|3.900|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[11331, 12006] → [[11331, 12006]]|22.500|move to|[['mud']] / []|
|[12006, 12129] → [[12006, 12129]]|4.100|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[12129, 12300] → [[12129, 12300]]|5.700|move to|[['mud']] / []|
|[12300, 12447] → [[12300, 12447]]|4.900|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[12447, 12657] → [[12447, 12657]]|7.000|move to|[['mud']] / []|
|[12657, 12831] → [[12657, 12831]]|5.800|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[12831, 12842] → [[12831, 12842]]|0.367|move to|[['mud']] / []|
|[12842, 12933] → [[12842, 12933]]|3.033|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[12933, 13134] → [[12933, 13134]]|6.700|move to|[['mud']] / []|
|[13134, 13290] → [[13134, 13290]]|5.200|sweep surface|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|
|[13290, 13449] → [[13290, 13449]]|5.300|release|[['broom_172']] / ['broom_172']|
|[13449, 14058] → [[13449, 14058]]|20.300|place on|[['broom_172', 'floors_ghetev_0']] / ['broom_172']|

First annotated manipulation: **pick up from**, objects `[['broom_172', 'floors_ghetev_0']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Shared order and decision points

Shared ordered motif (longest common subsequence of fine labels; optional/repeated stages may be omitted): **move to → pick up from → hold → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → sweep surface → move to → sweep surface → release → place on**. This is a descriptive motif, not a compulsory policy.

Use TASK.md to decide required object counts, common destinations, closures, cooking/cleaning or attachment conditions. Compare the per-episode first manipulation and partner objects before choosing which object to handle first. Remeasure current geometry, reachability and clearance; verify object motion, supported release and retention separately from TCP completion. Label timing is not a physical contact or success guarantee.
