import numpy as np
from camera_bootstrap import read_intrinsics

class Sim:
    current_time=0.
    renders=0
    advance=False
    def render(self):
        self.renders+=1
        if self.advance:self.current_time+=.01

class Sensor:
    def __init__(self, sim, required=8, message='intrinsic matrix for sensor: test is degenerate!'):
        self.sim,self.required,self.message=sim,required,message
        self.reads=0
    @property
    def intrinsic_matrix(self):
        self.reads+=1
        assert self.sim.renders>=self.required,self.message
        return np.eye(3)

s=Sim();c=Sensor(s);out=read_intrinsics([c],np.asarray,s)
assert s.renders==8 and c.reads==2 and np.array_equal(out[0],np.eye(3))
s=Sim();c=Sensor(s,required=0);read_intrinsics([c],np.asarray,s);assert s.renders==0 and c.reads==1
s=Sim();c=Sensor(s,required=9)
try:read_intrinsics([c],np.asarray,s)
except AssertionError:pass
else:raise AssertionError('Persistent degenerate matrix accepted')
assert c.reads==2 and s.renders==8
s=Sim();c=Sensor(s,message='unrelated assertion')
try:read_intrinsics([c],np.asarray,s)
except AssertionError:pass
else:raise AssertionError('Unrelated assertion swallowed')
assert s.renders==0 and c.reads==1
s=Sim();s.advance=True;c=Sensor(s)
try:read_intrinsics([c],np.asarray,s)
except RuntimeError:pass
else:raise AssertionError('Physics advancement accepted')
assert c.reads==1
print('CAMERA_BOOTSTRAP_BOUNDED_RETRY_NATIVE_ASSERTION_NO_PHYSICS_PASS')
