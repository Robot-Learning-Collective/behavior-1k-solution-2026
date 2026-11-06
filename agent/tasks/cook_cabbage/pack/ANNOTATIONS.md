# Public human annotation summary

Pinned dataset `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three first available demonstrations with TRAIN instance>=20, excluding evaluation11–19 and practice10. Labels are annotations, not contact sensors. Durations use clipped half-open frame intervals at30Hz. Missing coarse annotations are reported, not synthesized.

## Episode8214 / TRAIN20

Length492.400s; valid interval[15, 14772]; raw ID410200; `annotations/task-0041/episode_00410200.json`.

### Coarse

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[15, 2020] → [[15, 2020]]|66.833|open door|[['fridge_dszchb_0']] / []|
|[2020, 3427] → [[2020, 3427]]|46.900|pick up from|[[['chili_211', 'head_cabbage_212'], 'fridge_dszchb_0']] / [['chili_211', 'head_cabbage_212']]|
|[3427, 4302] → [[3427, 4302]]|29.167|close door|[['fridge_dszchb_0']] / []|
|[4302, 4999] → [[4302, 4999]]|23.233|place on|[['chili_211', 'plate_207']] / ['chili_211']|
|[4999, 5917] → [[4999, 5917]]|30.600|place on|[['head_cabbage_212', 'cutting_board_210']] / ['head_cabbage_212']|
|[5917, 7516] → [[5917, 7516]]|53.300|pick up from/place on|[['frying_pan_208', 'countertop_kelker_0'], ['frying_pan_208', 'burner_mjvqii_0']] / ['frying_pan_208', 'frying_pan_208']|
|[7516, 8868] → [[7516, 8868]]|45.067|chop|[['carving_knife_209', ['head_cabbage_212', 'half_head_cabbage_212_1', 'half_head_cabbage_212_0']]] / ['carving_knife_209']|
|[8868, 10240] → [[8868, 10240]]|45.733|pour|[[['diced__head_cabbage'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[10240, 11464] → [[10240, 11464]]|40.800|pick up from/place on|[['chili_211', 'plate_207'], ['chili_211', 'cutting_board_210']] / ['chili_211', 'chili_211']|
|[11464, 13378] → [[11464, 13378]]|63.800|chop|[['carving_knife_209', ['chili_211', 'half_chili_211_0', 'half_chili_211_1']]] / ['carving_knife_209']|
|[13378, 14454] → [[13378, 14454]]|35.867|pour|[[['diced__chili'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[14454, 14772] → [[14454, 14772]]|10.600|turn on switch|[['burner_mjvqii_0']] / ['burner_mjvqii_0']|

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[15, 933] → [[15, 933]]|30.600|move to|[['fridge_dszchb_0']] / []|
|[933, 2020] → [[933, 2020]]|36.233|open door|[['fridge_dszchb_0']] / []|
|[2020, 2932] → [[2020, 2932]]|30.400|pick up from|[['chili_211', 'fridge_dszchb_0']] / ['chili_211']|
|[2932, 3427] → [[2932, 3427]]|16.500|pick up from|[['head_cabbage_212', 'fridge_dszchb_0']] / ['head_cabbage_212']|
|[3427, 4302] → [[3427, 4302]]|29.167|close door|[['fridge_dszchb_0']] / []|
|[4302, 4519] → [[4302, 4519]]|7.233|move to|[['plate_207']] / []|
|[4519, 4999] → [[4519, 4999]]|16.000|place on|[['chili_211', 'plate_207']] / ['chili_211']|
|[4999, 5227] → [[4999, 5227]]|7.600|move to|[['cutting_board_210']] / []|
|[5227, 5917] → [[5227, 5917]]|23.000|place on|[['head_cabbage_212', 'cutting_board_210']] / ['head_cabbage_212']|
|[5917, 6125] → [[5917, 6125]]|6.933|move to|[['frying_pan_208']] / []|
|[6125, 6888] → [[6125, 6888]]|25.433|pick up from|[['frying_pan_208', 'countertop_kelker_0']] / ['frying_pan_208']|
|[6888, 6985] → [[6888, 6985]]|3.233|move to|[['burner_mjvqii_0']] / []|
|[6985, 7516] → [[6985, 7516]]|17.700|place on|[['frying_pan_208', 'burner_mjvqii_0']] / ['frying_pan_208']|
|[7516, 7633] → [[7516, 7633]]|3.900|move to|[['carving_knife_209']] / []|
|[7633, 8142] → [[7633, 8142]]|16.967|pick up from|[['carving_knife_209', 'countertop_kelker_0']] / ['carving_knife_209']|
|[8142, 8447] → [[8142, 8447]]|10.167|chop|[['carving_knife_209', 'head_cabbage_212']] / ['carving_knife_209']|
|[8447, 8578] → [[8447, 8578]]|4.367|chop|[['carving_knife_209', 'half_head_cabbage_212_1']] / ['carving_knife_209']|
|[8578, 8679] → [[8578, 8679]]|3.367|chop|[['carving_knife_209', 'half_head_cabbage_212_0']] / ['carving_knife_209']|
|[8679, 8868] → [[8679, 8868]]|6.300|place on next to|[['carving_knife_209', 'countertop_kelker_0', 'cutting_board_210']] / ['carving_knife_209']|
|[8868, 9357] → [[8868, 9357]]|16.300|pick up from|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[9357, 9881] → [[9357, 9881]]|17.467|pour|[[['diced__head_cabbage'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[9881, 10240] → [[9881, 10240]]|11.967|place on|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[10240, 10444] → [[10240, 10444]]|6.800|move to|[['chili_211']] / []|
|[10444, 10836] → [[10444, 10836]]|13.067|pick up from|[['chili_211', 'plate_207']] / ['chili_211']|
|[10836, 11147] → [[10836, 11147]]|10.367|move to|[['cutting_board_210']] / []|
|[11147, 11464] → [[11147, 11464]]|10.567|place on|[['chili_211', 'cutting_board_210']] / ['chili_211']|
|[11464, 12452] → [[11464, 12452]]|32.933|pick up from|[['carving_knife_209', 'countertop_kelker_0']] / ['carving_knife_209']|
|[12452, 12611] → [[12452, 12611]]|5.300|chop|[['carving_knife_209', 'chili_211']] / ['carving_knife_209']|
|[12611, 12690] → [[12611, 12690]]|2.633|chop|[['carving_knife_209', 'half_chili_211_0']] / ['carving_knife_209']|
|[12690, 13143] → [[12690, 13143]]|15.100|chop|[['carving_knife_209', 'half_chili_211_1']] / ['carving_knife_209']|
|[13143, 13378] → [[13143, 13378]]|7.833|place on|[['carving_knife_209', 'countertop_kelker_0']] / ['carving_knife_209']|
|[13378, 13923] → [[13378, 13923]]|18.167|pick up from|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[13923, 14113] → [[13923, 14113]]|6.333|pour|[[['diced__chili'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[14113, 14454] → [[14113, 14454]]|11.367|place on|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[14454, 14772] → [[14454, 14772]]|10.600|turn on switch|[['burner_mjvqii_0']] / ['burner_mjvqii_0']|

First annotated manipulation: **open door**, objects `[['fridge_dszchb_0']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode8215 / TRAIN21

Length543.367s; valid interval[0, 16290]; raw ID410210; `annotations/task-0041/episode_00410210.json`.

### Coarse

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 1418] → [[0, 1418]]|47.267|open door|[['fridge_dszchb_0']] / []|
|[1418, 3650] → [[1418, 3650]]|74.400|pick up from|[[['chili_211', 'head_cabbage_212'], 'fridge_dszchb_0']] / [['chili_211', 'head_cabbage_212']]|
|[3650, 4632] → [[3650, 4632]]|32.733|close door|[['fridge_dszchb_0']] / []|
|[4794, 5631] → [[4794, 5631]]|27.900|place on|[['head_cabbage_212', 'cutting_board_210']] / ['head_cabbage_212']|
|[5631, 6093] → [[5631, 6093]]|15.400|place on|[['chili_211', 'plate_207']] / ['chili_211']|
|[6093, 7161] → [[6093, 7161]]|35.600|pick up from/place on|[['frying_pan_208', 'countertop_kelker_0'], ['frying_pan_208', 'burner_mjvqii_0']] / ['frying_pan_208', 'frying_pan_208']|
|[7161, 9124] → [[7161, 9124]]|65.433|chop|[['carving_knife_209', ['head_cabbage_212', 'half_head_cabbage_212_1', 'half_head_cabbage_212_0']]] / ['carving_knife_209']|
|[9124, 11636] → [[9124, 11636]]|83.733|pour|[[['diced__head_cabbage'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[11636, 12693] → [[11636, 12693]]|35.233|pick up from/place on|[['chili_211', 'plate_207'], ['chili_211', 'cutting_board_210']] / ['chili_211', 'chili_211']|
|[12693, 14247] → [[12693, 14247]]|51.800|chop|[['carving_knife_209', ['chili_211', 'half_chili_211_1', 'half_chili_211_0']]] / ['carving_knife_209']|
|[14247, 15610] → [[14247, 15610]]|45.433|pour|[[['diced__chili'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[15610, 16290] → [[15610, 16290]]|22.667|turn on switch|[['burner_mjvqii_0']] / ['burner_mjvqii_0']|

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 376] → [[0, 376]]|12.533|move to|[['fridge_dszchb_0']] / []|
|[376, 1418] → [[376, 1418]]|34.733|open door|[['fridge_dszchb_0']] / []|
|[1418, 2739] → [[1418, 2739]]|44.033|pick up from|[['chili_211', 'fridge_dszchb_0']] / ['chili_211']|
|[2739, 3650] → [[2739, 3650]]|30.367|pick up from|[['head_cabbage_212', 'fridge_dszchb_0']] / ['head_cabbage_212']|
|[3650, 4632] → [[3650, 4632]]|32.733|close door|[['fridge_dszchb_0']] / []|
|[4794, 4980] → [[4794, 4980]]|6.200|move to|[['cutting_board_210']] / []|
|[4980, 5631] → [[4980, 5631]]|21.700|place on|[['head_cabbage_212', 'cutting_board_210']] / ['head_cabbage_212']|
|[5631, 5784] → [[5631, 5784]]|5.100|move to|[['plate_207']] / []|
|[5784, 6093] → [[5784, 6093]]|10.300|place on|[['chili_211', 'plate_207']] / ['chili_211']|
|[6093, 6242] → [[6093, 6242]]|4.967|move to|[['frying_pan_208']] / []|
|[6242, 6630] → [[6242, 6630]]|12.933|pick up from|[['frying_pan_208', 'countertop_kelker_0']] / ['frying_pan_208']|
|[6630, 6754] → [[6630, 6754]]|4.133|move to|[['burner_mjvqii_0']] / []|
|[6754, 7161] → [[6754, 7161]]|13.567|place on|[['frying_pan_208', 'burner_mjvqii_0']] / ['frying_pan_208']|
|[7161, 7927] → [[7161, 7927]]|25.533|pick up from|[['carving_knife_209', 'countertop_kelker_0']] / ['carving_knife_209']|
|[7927, 8076] → [[7927, 8076]]|4.967|move to|[['head_cabbage_212']] / []|
|[8076, 8436] → [[8076, 8436]]|12.000|chop|[['carving_knife_209', 'head_cabbage_212']] / ['carving_knife_209']|
|[8436, 8517] → [[8436, 8517]]|2.700|chop|[['carving_knife_209', 'half_head_cabbage_212_1']] / ['carving_knife_209']|
|[8517, 8787] → [[8517, 8787]]|9.000|chop|[['carving_knife_209', 'half_head_cabbage_212_0']] / ['carving_knife_209']|
|[8787, 9124] → [[8787, 9124]]|11.233|place on next to|[['carving_knife_209', 'countertop_kelker_0', 'cutting_board_210']] / ['carving_knife_209']|
|[9124, 9227] → [[9124, 9227]]|3.433|move to|[['cutting_board_210']] / []|
|[9227, 9882] → [[9227, 9882]]|21.833|push to|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[9882, 10255] → [[9882, 10255]]|12.433|pick up from|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[10255, 10588] → [[10255, 10588]]|11.100|move to|[['frying_pan_208']] / []|
|[10588, 11044] → [[10588, 11044]]|15.200|pour|[[['diced__head_cabbage'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[11044, 11636] → [[11044, 11636]]|19.733|place on|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[11636, 11921] → [[11636, 11921]]|9.500|move to|[['chili_211']] / []|
|[11921, 12204] → [[11921, 12204]]|9.433|pick up from|[['chili_211', 'plate_207']] / ['chili_211']|
|[12204, 12355] → [[12204, 12355]]|5.033|move to|[['cutting_board_210']] / []|
|[12355, 12693] → [[12355, 12693]]|11.267|place on|[['chili_211', 'cutting_board_210']] / ['chili_211']|
|[12693, 13260] → [[12693, 13260]]|18.900|pick up from|[['carving_knife_209', 'countertop_kelker_0']] / ['carving_knife_209']|
|[13260, 13691] → [[13260, 13691]]|14.367|chop|[['carving_knife_209', 'chili_211']] / ['carving_knife_209']|
|[13691, 13750] → [[13691, 13750]]|1.967|chop|[['carving_knife_209', 'half_chili_211_1']] / ['carving_knife_209']|
|[13750, 13894] → [[13750, 13894]]|4.800|chop|[['carving_knife_209', 'half_chili_211_0']] / ['carving_knife_209']|
|[13894, 14247] → [[13894, 14247]]|11.767|place on|[['carving_knife_209', 'countertop_kelker_0']] / ['carving_knife_209']|
|[14247, 14388] → [[14247, 14388]]|4.700|move to|[['cutting_board_210']] / []|
|[14388, 14718] → [[14388, 14718]]|11.000|pick up from|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[14718, 14996] → [[14718, 14996]]|9.267|move to|[['frying_pan_208']] / []|
|[14996, 15109] → [[14996, 15109]]|3.767|pour|[[['diced__chili'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[15109, 15610] → [[15109, 15610]]|16.700|place on|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[15610, 15820] → [[15610, 15820]]|7.000|move to|[['burner_mjvqii_0']] / []|
|[15820, 16290] → [[15820, 16290]]|15.667|turn on switch|[['burner_mjvqii_0']] / ['burner_mjvqii_0']|

First annotated manipulation: **open door**, objects `[['fridge_dszchb_0']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode8216 / TRAIN23

Length352.633s; valid interval[18, 10578]; raw ID410230; `annotations/task-0041/episode_00410230.json`.

### Coarse

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[18, 940] → [[18, 940]]|30.733|open door|[['fridge_dszchb_0']] / []|
|[940, 1927] → [[940, 1927]]|32.900|pick up from|[[['head_cabbage_212', 'chili_211'], 'fridge_dszchb_0']] / [['head_cabbage_212', 'chili_211']]|
|[1927, 2808] → [[1927, 2808]]|29.367|close door|[['fridge_dszchb_0']] / []|
|[2808, 3480] → [[2808, 3480]]|22.400|place on|[['head_cabbage_212', 'cutting_board_210']] / ['head_cabbage_212']|
|[3480, 3826] → [[3480, 3826]]|11.533|place on|[['chili_211', 'plate_207']] / ['chili_211']|
|[3826, 4682] → [[3826, 4682]]|28.533|pick up from/place on|[['frying_pan_208', 'countertop_kelker_0'], ['frying_pan_208', 'burner_mjvqii_0']] / ['frying_pan_208', 'frying_pan_208']|
|[4682, 6276] → [[4682, 6276]]|53.133||[] / []|
|[6276, 7932] → [[6276, 7932]]|55.200|chop|[['carving_knife_209', ['head_cabbage_212', 'half_head_cabbage_212_1', 'half_head_cabbage_212_0']]] / ['carving_knife_209']|
|[7932, 8589] → [[7932, 8589]]|21.900|pour|[[['diced__head_cabbage'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[8589, 9170] → [[8589, 9170]]|19.367|pick up from/place on|[['chili_211', 'plate_207'], ['chili_211', 'cutting_board_210']] / ['chili_211', 'chili_211']|
|[9170, 9910] → [[9170, 9910]]|24.667|chop|[['carving_knife_209', ['chili_211', 'half_chili_211_0', 'half_chili_211_1']]] / ['carving_knife_209']|
|[9919, 10345] → [[9919, 10345]]|14.200|pour|[[['diced__chili'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[10345, 10578] → [[10345, 10578]]|7.767|turn on switch|[['burner_mjvqii_0']] / ['burner_mjvqii_0']|

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[18, 57] → [[18, 57]]|1.300|move to|[['fridge_dszchb_0']] / []|
|[57, 940] → [[57, 940]]|29.433|open door|[['fridge_dszchb_0']] / []|
|[940, 1436] → [[940, 1436]]|16.533|pick up from|[['head_cabbage_212', 'fridge_dszchb_0']] / ['head_cabbage_212']|
|[1436, 1927] → [[1436, 1927]]|16.367|pick up from|[['chili_211', 'fridge_dszchb_0']] / ['chili_211']|
|[1927, 2808] → [[1927, 2808]]|29.367|close door|[['fridge_dszchb_0']] / []|
|[2808, 3243] → [[2808, 3243]]|14.500|move to|[['cutting_board_210']] / []|
|[3243, 3480] → [[3243, 3480]]|7.900|place on|[['head_cabbage_212', 'cutting_board_210']] / ['head_cabbage_212']|
|[3480, 3508] → [[3480, 3508]]|0.933|move to|[['plate_207']] / []|
|[3508, 3826] → [[3508, 3826]]|10.600|place on|[['chili_211', 'plate_207']] / ['chili_211']|
|[3826, 4313] → [[3826, 4313]]|16.233|pick up from|[['frying_pan_208', 'countertop_kelker_0']] / ['frying_pan_208']|
|[4313, 4527] → [[4313, 4527]]|7.133|move to|[['burner_mjvqii_0']] / []|
|[4527, 4682] → [[4527, 4682]]|5.167|place on|[['frying_pan_208', 'burner_mjvqii_0']] / ['frying_pan_208']|
|[4682, 4974] → [[4682, 4974]]|9.733|move to|[['carving_knife_209']] / []|
|[4974, 5721] → [[4974, 5721]]|24.900|turn to|[['carving_knife_209', 'robot']] / ['carving_knife_209']|
|[5721, 5931] → [[5721, 5931]]|7.000|pick up from|[['carving_knife_209', 'countertop_kelker_0']] / ['carving_knife_209']|
|[5931, 6276] → [[5931, 6276]]|11.500|place on|[['carving_knife_209', 'countertop_kelker_0']] / ['carving_knife_209']|
|[6276, 7068] → [[6276, 7068]]|26.400|pick up from|[['carving_knife_209', 'countertop_kelker_0']] / ['carving_knife_209']|
|[7068, 7172] → [[7068, 7172]]|3.467|move to|[['head_cabbage_212']] / []|
|[7172, 7575] → [[7172, 7575]]|13.433|chop|[['carving_knife_209', 'head_cabbage_212']] / ['carving_knife_209']|
|[7575, 7642] → [[7575, 7642]]|2.233|chop|[['carving_knife_209', 'half_head_cabbage_212_1']] / ['carving_knife_209']|
|[7642, 7812] → [[7642, 7812]]|5.667|chop|[['carving_knife_209', 'half_head_cabbage_212_0']] / ['carving_knife_209']|
|[7812, 7932] → [[7812, 7932]]|4.000|place on next to|[['carving_knife_209', 'countertop_kelker_0', 'cutting_board_210']] / ['carving_knife_209']|
|[7932, 8243] → [[7932, 8243]]|10.367|pick up from|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[8243, 8346] → [[8243, 8346]]|3.433|pour|[[['diced__head_cabbage'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[8346, 8589] → [[8346, 8589]]|8.100|place on|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[8589, 8651] → [[8589, 8651]]|2.067|move to|[['chili_211']] / []|
|[8651, 8895] → [[8651, 8895]]|8.133|pick up from|[['chili_211', 'plate_207']] / ['chili_211']|
|[8895, 9009] → [[8895, 9009]]|3.800|move to|[['cutting_board_210']] / []|
|[9009, 9170] → [[9009, 9170]]|5.367|place on|[['chili_211', 'cutting_board_210']] / ['chili_211']|
|[9170, 9477] → [[9170, 9477]]|10.233|pick up from|[['carving_knife_209', 'countertop_kelker_0']] / ['carving_knife_209']|
|[9477, 9600] → [[9477, 9600]]|4.100|chop|[['carving_knife_209', 'chili_211']] / ['carving_knife_209']|
|[9600, 9696] → [[9600, 9696]]|3.200|chop|[['carving_knife_209', 'half_chili_211_0']] / ['carving_knife_209']|
|[9696, 9792] → [[9696, 9792]]|3.200|chop|[['carving_knife_209', 'half_chili_211_1']] / ['carving_knife_209']|
|[9792, 9910] → [[9792, 9910]]|3.933|place on|[['carving_knife_209', 'countertop_kelker_0']] / ['carving_knife_209']|
|[9919, 10079] → [[9919, 10079]]|5.333|pick up from|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[10079, 10204] → [[10079, 10204]]|4.167|pour|[[['diced__chili'], 'cutting_board_210', 'frying_pan_208']] / ['cutting_board_210']|
|[10204, 10345] → [[10204, 10345]]|4.700|place on|[['cutting_board_210', 'countertop_kelker_0']] / ['cutting_board_210']|
|[10345, 10578] → [[10345, 10578]]|7.767|turn on switch|[['burner_mjvqii_0']] / ['burner_mjvqii_0']|

First annotated manipulation: **open door**, objects `[['fridge_dszchb_0']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Shared order and decision points

Shared ordered motif (longest common subsequence of fine labels; optional/repeated stages may be omitted): **move to → open door → pick up from → pick up from → close door → move to → place on → move to → place on → move to → pick up from → place on → move to → chop → chop → chop → place on next to → pick up from → pour → place on → move to → pick up from → move to → place on → pick up from → chop → chop → chop → place on → pick up from → pour → place on → turn on switch**. This is a descriptive motif, not a compulsory policy.

Use TASK.md to decide required object counts, common destinations, closures, cooking/cleaning or attachment conditions. Compare the per-episode first manipulation and partner objects before choosing which object to handle first. Remeasure current geometry, reachability and clearance; verify object motion, supported release and retention separately from TCP completion. Label timing is not a physical contact or success guarantee.
