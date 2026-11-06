# a08 — native recovered completion, NOT clean first acquisition

Attempt `scanner-run-007-v6fixed-native-a08`, fixed protocol6; no snapshots. Finished 118.4 simulated seconds (~3552 nominal30Hz steps /6387), 663.0034271879995 wall seconds. Scanner visibly retained through lift/withdrawal/carry, independently supported beside laptop, green switch persisted after retreat. Not privileged-scored success. No visible base tilt. Consecutive clean count remains0.

Evidence root `/tmp/scanner-run-007-p6-b311c1/scanner-run-007-v6fixed-native-a08/`; final obs072 receipt `receipt_01792122003012642000_5214ae137342442bb99c2524439dbcf7.json`; full commands in run-local control-action-results.jsonl.

## Preparation failure
Initial geometry-adapted third/fourth sweeps did NOT provide adequate overhang. At obs033 top near rim head(440,430)=[.98986,-.12147,.82145], desk edge(440,450)=[.99314,-.13702,.74558]. First insertion target[1.025,-.13,.805] stalled actual[.971,-.124,.748]; higher .835 retry stalled[.973,-.117,.776]. Neither was closed. These retries disqualify clean acquisition.

Recovered by retreat .35, sweep branch `[-1.90272,-.5522,1.21352,-1.68676,-2.25046,.53347,-1.45134]`, forward .60. Measured rear edge head(450,425)=[.99463,-.13603,.82803], near edge(450,560)=[.82322,-.10259,.82779], desk(440,610)=[.78161,-.09664,.76392]. Thus earlier targets ending~.99 barely reached rear edge rather than pulling the scanner over desk. Closed sweep: [1.055,-.13,.96]→[1.055,-.13,.80]→[.83,-.13,.815]. This reached joint limits, rotated scanner, and created a protruding corner (not recommended as clean recipe). Lift target[1.08,-.13,1.02] stalled high but clear.

## Acquisition recovery
Retreat .60, open, vertical jaw seed, stage[.823,-.30,.805], forward .35. Unloading measured joint7 -1.5608 initially rejected endpoint bound; retry used explicit -1.560 and joint5 -2.346 (no simulator motion on rejection). Rounded measured joints at limits can be outside exact permitted bounds.

Head near corner(390,443)=[.96574,-.04397,.82768]. Base left .10 centers it; align[.87,-.15,.805], insert[.98,-.15,.805]→actual[.971,-.15,.793]. Unload and close q[-.45672,-.34024,.95259,-1.66649,-2.02801,-.91908,.41575], accept_partial. First closure after multiple insertion attempts retained 5cm finger sum; lift[.971,-.15,.89]. Withdraw .40 at q[-.52251,-.39816,.98312,-2.03773,-1.63019,-1.037,-.18848] (joint6 explicitly bounded, measured -1.04215). Unsupported retained scanner obs058.

## Placement and activation
Yaw−25; forward .50 then .15; lower[.971,-.15,.79] stalled on support. Release q[-.37368,-.28156,.81738,-1.84893,-1.87177,-.8083,.33061], accept_partial; retreat .20. Independent support obs064.
Close empty hand; torso q[1.25,-1.76,-.85,0], switch arm branch[-1.95597,-.4024,2.11198,-1.48611,.81688,.03802,.85601], stage[.84,-.18,.94], forward .20. Button right(406,157)=[.96407,-.08055,.82090], stage +.06Z. Reacquire right(265,103)=[.96405,-.07743,.82159], press+.004Z. Green obs070 despite joint-limit status; hand withdraw[.84,-.18,.94], base−.20; persistent green obs072.

Next native repetition should reproduce a07 preparation rather than a08's ineffective adapted sweeps. Validate actual near-edge overhang before insertion; a surface coordinate alone is not under-jaw clearance.
