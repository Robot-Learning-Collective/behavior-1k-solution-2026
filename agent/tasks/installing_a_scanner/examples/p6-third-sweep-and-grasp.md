# Protocol6 third-sweep and grasp trials

All actions followed by fresh `s.observe()`; act RGB not used. No acquisition or placement success.

## Overlong third sweep
Continuation of `practice-restore-a04-before-preparation-5f004a05c298459c9006f4ea8351a621`: base left .2, right stages [1.23,-.18,.96], lowers [1.23,-.18,.80], sweeps [1.0,-.18,.815], withdraws [1.12,-.18,1.02]. Obs35 scanner significantly advanced; obs37/39 supported-looking overhang; snapshot `a04-overhang`. After base retreat -.30 and vertical-jaw q [-.01207,-.52959,.68534,-1.34945,-2.31305,-.43568,1.16463], fresh obs41 scanner on floor. Cannot distinguish unstable support from swept-arm collision from endpoints alone. This is NOT safe edge-preparation success.

## Shortened trial
Restored `a04-second-sweep` into `practice-restore-a04-second-sweep-3d8e15e149164e0b84de135b4e059c35`.
Sequence (right to unless noted):
- base left .2
- [1.23,-.18,.96], [1.23,-.18,.80], [1.11,-.18,.815], [1.06,-.18,.815], withdraw [1.15,-.18,1.0]; snapshot `a04-short-third-sweep` at obs13.
- [1.10,-.25,.96], [1.10,-.25,.80], [1.02,-.25,.815], base fwd -.05, withdraw [1.15,-.25,1.0]; snapshot `a04-small-overhang` at obs23.
- base fwd -.50, previous vertical-jaw q plus grip1; object stays on table at obs27. Raise TCP [.823,-.30,.812], base fwd .40. Snapshot `a04-before-grasp` at obs31.
- align [.81,-.19,.819], insert [.883,-.19,.819], grip0, lift [.883,-.19,.90].
Insertion reached but scanner shifted away. Actual closure reached 0+0m, no retained object. Lift stalled at elbow limit, measured TCP [.882,-.194,.850]; scanner remained table-supported in fresh obs39. No grasp success.

Obs31 depth pixels (head u,v): (500,520)=[.864938,-.172605,.826020]; (530,505)=[.882040,-.215460,.826726]; (575,490)=[.900162,-.280382,.827436]; tabletop(600,550)=[.843401,-.320357,.764843]. Insertion changed object position; do not reuse these as current coordinates.

Receipts and original RGBD for each attempt live under `/tmp/scanner-run-007-p6-57b375/<attempt>/`; latest fresh obs39 receipt `receipt_01792118287705957000_634870129e924c59bbe63311d54bb795.json`. Current right q [-.14534,-.53838,.9033,-2.0844,-1.58633,-1.01049,.08053], closed, persistent unmet lift target. Before next attempt restore `a04-before-grasp` or unload measured q. Half-metre retreat cleared this reorientation path; .30m with larger overhang did not prove clearance.
