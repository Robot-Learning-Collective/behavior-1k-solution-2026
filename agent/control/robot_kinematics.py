"""R1Pro BODY-frame FK/Jacobians from a shipped static model + measured joints.
No simulator, filesystem state, global robot pose, contact, or task dependency.
"""
import json
from pathlib import Path
import numpy as np


def rotation_vector_matrix(vector):
    v=np.asarray(vector,dtype=float);angle=float(np.linalg.norm(v))
    if angle<1e-12:return np.eye(3)
    x,y,z=v/angle
    skew=np.array([[0.,-z,y],[z,0.,-x],[-y,x,0.]])
    return np.eye(3)+np.sin(angle)*skew+(1.-np.cos(angle))*(skew@skew)


def quaternion_matrix(q):
    q=np.asarray(q,dtype=float)
    if q.shape!=(4,) or not np.isfinite(q).all() or np.linalg.norm(q)<1e-12:
        raise ValueError('Expected finite nonzero xyzw quaternion')
    x,y,z,w=q/np.linalg.norm(q)
    return np.array([[1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],
                     [2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],
                     [2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]])


def rotation_error(desired, measured):
    R=np.asarray(desired)@np.asarray(measured).T
    skew=np.array([R[2,1]-R[1,2],R[0,2]-R[2,0],R[1,0]-R[0,1]])
    angle=float(np.arctan2(np.linalg.norm(skew)*.5,np.clip((np.trace(R)-1.)*.5,-1.,1.)))
    if angle<1e-12:return np.zeros(3)
    if np.pi-angle<1e-6:
        _,vectors=np.linalg.eigh((R+R.T)*.5);axis=vectors[:,-1]
        if np.linalg.norm(skew)>1e-12:
            if np.dot(axis,skew)<0:axis=-axis
        elif axis[np.argmax(np.abs(axis))]<0:axis=-axis
        return axis*angle
    return skew/np.linalg.norm(skew)*angle


class RobotModel:
    def __init__(self, data=None):
        self.data=data or json.loads(Path(__file__).with_name('robot_model.json').read_text())
        self.base=self.data['base_link']
        self.by_child={j['child']:j for j in self.data['joints']}
        self.origins={}
        self.chains={}
        for joint in self.data['joints']:
            T=np.eye(4);T[:3,3]=joint['xyz']
            if 'quaternion_wxyz' in joint:
                w,x,y,z=joint['quaternion_wxyz'];R=quaternion_matrix([x,y,z,w])
            else:
                r,p,y=joint['rpy']
                R=rotation_vector_matrix([0,0,y])@rotation_vector_matrix([0,p,0])@rotation_vector_matrix([r,0,0])
            T[:3,:3]=R;self.origins[joint['name']]=T
        for child in self.by_child:
            chain=[];link=child
            while link!=self.base:
                if len(chain)>len(self.by_child):raise ValueError('Cyclic robot model')
                joint=self.by_child[link];chain.append(joint);link=joint['parent']
            self.chains[child]=chain[::-1]

    @staticmethod
    def measured_joints(robot):
        q={f'torso_joint{i+1}':v for i,v in enumerate(robot['torso_joints'])}
        for arm in ('left','right'):
            q.update({f'{arm}_arm_joint{i+1}':v for i,v in enumerate(robot[arm]['joints'])})
            q.update({f'{arm}_gripper_finger_joint{i+1}':v for i,v in enumerate(robot[arm]['finger_positions'])})
        return q

    def pose(self, link, joint_positions):
        return np.eye(4) if link==self.base else self._walk(link,joint_positions)[0]

    def _walk(self, link, q):
        T=np.eye(4);axes={};origins={}
        for joint in self.chains[link]:
            name=joint['name'];T=T@self.origins[name]
            if joint['type']=='fixed':continue
            value=float(q[name])
            if not np.isfinite(value):raise ValueError('Nonfinite model joint '+name)
            axis=np.asarray(joint['axis'],dtype=float)
            axes[name]=T[:3,:3]@axis;origins[name]=T[:3,3].copy()
            move=np.eye(4)
            if joint['type'] in ('revolute','continuous'):
                move[:3,:3]=rotation_vector_matrix(axis*value)
            elif joint['type']=='prismatic':move[:3,3]=axis*value
            else:raise ValueError('Unsupported joint type '+joint['type'])
            T=T@move
        return T,axes,origins

    def arm(self, arm, torso_q, arm_q, tcp_offset=None):
        torso_q=np.asarray(torso_q,dtype=float);arm_q=np.asarray(arm_q,dtype=float)
        if torso_q.shape!=(4,) or arm_q.shape!=(7,) or not np.isfinite(np.r_[torso_q,arm_q]).all():
            raise ValueError('Expected finite torso4/arm7 joint positions')
        q={f'torso_joint{i+1}':v for i,v in enumerate(torso_q)}
        q.update({f'{arm}_arm_joint{i+1}':v for i,v in enumerate(arm_q)})
        T,axes,origins=self._walk(arm+'_eef_link',q)
        offset=np.asarray(self.data['tcp']['translation_m'] if tcp_offset is None else tcp_offset,dtype=float)
        if offset.shape!=(3,) or not np.isfinite(offset).all():raise ValueError('Invalid rigid TCP offset')
        p=T[:3,3]+T[:3,:3]@offset
        J=np.empty((6,7))
        for i in range(7):
            name=f'{arm}_arm_joint{i+1}'
            J[:3,i]=np.cross(axes[name],p-origins[name]);J[3:,i]=axes[name]
        return p,T[:3,:3].copy(),J

    def all_link_poses(self, robot):
        q=self.measured_joints(robot)
        return {self.base:np.eye(4), **{link:self.pose(link,q) for link in self.by_child}}
