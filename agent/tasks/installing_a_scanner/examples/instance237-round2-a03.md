# TRAIN237 round2-a03 — Q0.5, first acquisition/press; nextto false

Worker e361cf/source a47213f, fresh native reset, no restores. Finished 2079 steps / 69.3 simulated seconds / 443.460957019 wall seconds. Native toggled_on true, nextto false. Round2 denominator now 1/3 full successes.

## Preparation correction tested
After BASE draws -.25/-.16, scanner front head [400,500] ≈[1.0598,-.2414,.7977]. True desktop brackets [380,370]=[1.1282,-.0204,.7649], [425,630]=[1.0300,-.4692,.7649]; actual edge estimated around X1.074 at Y-.24, only ~1.4cm beyond front. Selected final BASE draw -.05 instead of failed a02 -.10. Scanner stayed supported. Cleared, withdrew -.30 before wrist orientation, opened/reoriented, returned+.30.

Fresh front [400,500]=[1.0570,-.2391,.8019], desktop brackets [365,370]=[1.1665,-.0213,.7649], [410,630]=[1.0603,-.4868,.7649]; bevel next row. Approx edge1.114 at grasp lateral, with uncertainty. Align [1.01,-.24,.787], shallow insert [1.075,-.24,.787]; achieved TCP[1.073,-.238,.791], lower pad[1.079,-.238,.745]. No obvious insertion displacement. Closed achieved joints, lifted .94, withdrew-.25 and yaw-30: retained scanner visibly.

## Placement failure retained
Laptop sample head[215,630]=[1.7816,-.8854,.7985], near edge[215,590]=[1.8035,-.7708,.7890]. Base+.40; carry[1.20,-.54,.94], lower.835, measured-joint replacement, open, level backout[.98,-.54,.835], raise.98. Scanner rotated/settled during release/backout, then visually stable; no zero-displacement claim. After yaw-20 and base+.18, switch cross-localized right[84,99]=[1.2304,-.2789,.8228], head[323,497]=[1.2296,-.2785,.8220]. First press via z.89→.815 turned green, clear[1.15,-.20,1.02]. Native finish nextto FALSE despite apparent proximity. No robot tilt observed; planar odometry cannot establish tilt.

Final receipt: `<observation-cache>/scanner-run-007-p6-e361cf/scanner-run-007-instance237-round2-a03/receipt_01792155580308065000_4b7ed40609364ee9b2b38f7a7fb6f48b.json`.

Next test: retain geometry-gated overhang; freshly measure whole scanner/laptop alignment after approach and require more overlap/smaller positive gap, not successful grasp TCP coordinates or visual closeness. Placement drift remains unresolved; one reduced-draw acquisition is not reliability proof.
