# Human switch reference (not a live trajectory)

Source: local official demo18410 `cross-press.json` and `cross-press-1.jpg`; RGB30Hz, position row=RGB row−1, velocity/command row=RGB row−2. Different native instance19; do not directly replay in live instance10.

| RGB frame | left EEF BODY m | right EEF BODY m | right aperture m | visible state |
|---|---|---|---|---|
|4112|[.454,.234,1.212]|[.526,−.113,1.098]|.100|red, right hand open and below button|
|4217|[.510,.166,1.119]|[.601,.108,1.346]|.000002|red, closed right hand above button|
|4350|[.510,.169,1.119]|[.628,.068,1.334]|.000004|green, right hand near button|
|4374|[.510,.171,1.121]|[.711,−.130,1.354]|.100|green, right withdrawn/open|

Measured left aperture≈.0732m throughout; visible left retention is corroborated by scanner position, not closure alone. Torso remains [.450,−.400,−.0206,0]rad. During the contact interval4217→4350 left EEF changes only millimetres while right translates [+27,−40,−12]mm. Therefore stabilization plus a small right downward/lateral correction is the useful mechanism. Exact button-normal motion must come from live RGB/depth, not transplanting these BODY offsets.

Right xyzw quaternion at4217 [−.336,.645,.337,.597]; at4350 [−.307,.668,.340,.587]. This human EEF link is not asserted to equal current rigid TCP/pad reference. No force or hidden contact data used.
