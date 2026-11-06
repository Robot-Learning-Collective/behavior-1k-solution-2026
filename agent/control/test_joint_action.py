"""Single focused nonactuating endpoint/NULL≠zero/slew/bounds check."""
import numpy as np
from joint_action import validate,target,InvalidAction
low=np.full(7,-2.);high=np.full(7,2.);bounds={a:(low,high) for a in ('left','right')}
motion=dict(seconds=2.,left=None,right=None,left_gripper=1.,right_gripper=1.,base=[0.]*3,torso_delta=[0.]*2)
assert validate(motion,bounds)==60
initial=np.full(7,.4)
assert np.array_equal(target(initial,initial,None,1,low,high),initial)
assert np.allclose(target(initial,initial,[0.]*7,1,low,high),initial-.025)
for endpoint in ([0.]*6,[float('nan')]*7,[2.01]*7,'not-joints'):
 try:validate({**motion,'left':endpoint},bounds)
 except InvalidAction:pass
 else:raise AssertionError('Invalidendpointaccepted')
for n in range(3,61):
 current=initial.copy()
 for i in range(n):
  nextq=target(initial,current,np.full(7,-1.3),(i+1)/n,low,high)
  assert np.max(np.abs(nextq-current))<=.025+1e-12
  assert np.all(nextq>=low) and np.all(nextq<=high)
  current=nextq
assert validate({**motion,'left':[0.]*7},bounds)==60
print('JOINT_NULL_ZERO_SHAPE_LIMITS_SLEW_NO_CART_FALLBACK_PASS')
