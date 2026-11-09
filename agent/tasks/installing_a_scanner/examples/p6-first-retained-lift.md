# First retained scanner lift — protocol6

Not full task completion or repeatability. Scanner remains red/off. Fresh observe after EVERY act; act RGB is stale.

Attempt `practice-restore-a04-overhang-1282ca8a1ca34019ae31975ec3230e50`, evidence root `/tmp/scanner-run-007-p6-57b375/`.

## Recipe from saved overhang

```python
s.restore('a04-overhang')
s.act(base={'fwd':-.60})
s.observe()
s.act(right={'q':[-.01207,-.52959,.68534,-1.34945,-2.31305,-.43568,1.16463], 'grip':1})
s.observe()
s.act(right={'to':[.823,-.30,.79]})
s.observe()
s.act(base={'fwd':.35})
s.observe()
s.snapshot('a04-overhang-pregrasp')
s.act(right={'to':[.85,-.13,.79]})
s.observe()
s.act(right={'to':[.94,-.13,.79]})
s.observe()
s.act(right={'grip':0})
s.observe()
s.act(right={'to':[.94,-.13,.88]})
s.observe()
s.act(base={'fwd':-.25})
s.observe()
s.snapshot('a04-retention-test')
```

## Evidence

- Fresh obs007/009: scanner stayed supported through .60m retreat and remote vertical-jaw reorientation. Earlier .30m retreat branch had scanner on floor; this larger retreat changed outcome, without proving collision causality.
- obs009 head XYZ samples: `(450,450)=[.949740,-.124784,.839178]`; `(420,450)=[.961546,-.088740,.813714]`; `(470,480)=[.918018,-.151699,.813703]`.
- obs013 insertion: measured rigid TCP `[.937,-.130,.788]`, upper pad `[.933,-.130,.835]`, lower `[.941,-.131,.740]`. Scanner shifted slightly but remained at edge.
- obs015 closure: actual fingers `[.05,.0054]`, 5.5cm sum, measured pinch `[.935,-.130,.811]`. `status=stalled` describes obstructed closure, NOT automatic grasp proof.
- obs017 lift: rigid TCP `[.940,-.131,.875]`, measured pinch `[.939,-.131,.897]`; fresh RGB shows scanner elevated with hand. Wrist tracking lag ~.034rad; requested Z.88 nearly achieved.
- obs019 base withdrawal: scanner remained at same body-relative position while table receded .245m in measured base odometry. This is first retained lift+withdrawal evidence. Right TCP `[.940,-.131,.878]`, pinch `[.938,-.131,.900]`, fingers unchanged. No hidden contact/held state used.
- obs019 receipt `receipt_01792118693686887000_3e0ce3a939094a5f9d0877fd61eb5f90.json`, sim55.07s.

## Failed comparison

Earlier higher-lip retry from `a04-before-grasp` used base-.1, targets `[.90,-.19,.85]`, `[.985,-.19,.85]`, close, lift `[.985,-.19,.92]`. Fingers closed to zero; no acquisition. Successful trial instead used larger overhang and full-thickness Z.79 jaw placement. These are multiple changed factors, not a controlled causal ablation.

Next: repeat retention, activate with other hand or place supported to activate, then transport/place beside laptop. Snapshot restores are local trials, not independent full episodes.
