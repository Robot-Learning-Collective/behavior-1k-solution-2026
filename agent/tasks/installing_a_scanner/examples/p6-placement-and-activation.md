# Scanner retained carry → supported placement → activation

Same restored-overhang attempt as `p6-first-retained-lift.md`; NOT an independent from-reset episode or hidden-score claim. Fresh observe after every action. Final scanner green and supported beside laptop; original preparation achieved through earlier snapshot practice.

## Carry and placement
From `a04-retention-test` at obs019, right fingers held 5.5cm separation:
- Base fwd-.30 (stalled after ~.258), yaw+90: wrong direction, wall near left hand. Retention survived; left joint lag .08rad. This detour should not be copied as ideal navigation.
- Base fwd-.25 to clear wall; yaw-160, then yaw+45 to face visible laptop desk. Fresh obs029 scanner still held.
- Measured laptop head(438,215) `[1.78025,-.25663,.79910]`, tabletop(340,240) `[1.68045,.06119,.76499]`.
- Base fwd+.45; then base left+.30/fwd+.15: scanner alongside laptop, not over it. Snapshot `a04-before-placement` at obs033.
- Right to `[.94,-.13,.79]` stalled, actual `[.932,-.130,.841]` with torso lag .018 and substantial effort. Did not force descent.
- Unloaded with measured q `[-.27336,-.19823,.78793,-1.69308,-1.75271,-.79113,.44409]`, grip1, accept_partial=True.
- Base fwd-.20 withdrew empty hand. Fresh obs039: scanner independently rests beside laptop, red/off. Snapshot `a04-placed-off`. Receipt `receipt_01792118894481446000_9a5a9a4e45a543feb11887491b3e8ee0.json`.

## Activation after placement
- Close empty right hand (grip0).
- Failed orientation route: direct right to `[.94,-.13,.96]` with finger_dir `[.707,0,-.707]`, close_dir `[0,-1,0]` timed out at joint limits; no contact claim. Replace rather than retry.
- Recovered via measured historical switch branch: torso q `[1.25,-1.76,-.85,0]`, right q `[-1.95597,-.4024,2.11198,-1.48611,.81688,.03802,.85601]`. Source was own a01 obs1488 receipt, no privileged object state. Fresh obs045 confirmed TCP `[.841,-.180,.840]`, finger axis down-forward.
- Raise right `[.84,-.18,.94]`; base fwd+.20; fresh obs049.
- Right camera pixel(398,127) switch XYZ `[.934259,-.096996,.820940]`. Stage at same XY/Z+.06.
- Reacquire right pixel(264,95): `[.933762,-.093847,.821197]`; press target `[.933762,-.093847,.825197]`.
- Fresh obs053 green. Withdraw right `[.84,-.18,.94]`; fresh obs055 still green with no ongoing press. Snapshot `a04-placed-on`.
- Final receipt `receipt_01792119108292198000_a4fde45c1d7f4874a796899e14073ca2.json`, sim121.73s, wall667.4s since restore. These times include navigation detour and failed orientation, but exclude original preparation before restored snapshot; not full-episode performance.

Evidence root `/tmp/scanner-run-007-p6-57b375/practice-restore-a04-overhang-1282ca8a1ca34019ae31975ec3230e50/`.

Next: repeat full preparation/acquisition/carry/activation from an earlier snapshot or native reset; no repeatability claim yet.
