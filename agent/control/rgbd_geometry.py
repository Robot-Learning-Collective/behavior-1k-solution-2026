"""Pure calibrated RGBD geometry, reusable in the official policy server.
Optical camera axes are +X right, +Y down, +Z forward; depth_linear is axial Z.
All transforms map optical camera coordinates into the current robot BODY frame.
"""
import numpy as np


def camera_arrays(camera):
    K=np.asarray(camera['intrinsics'],dtype=float)
    T=np.asarray(camera['camera_to_body'],dtype=float)
    offset=float(camera.get('pixel_center_offset',0.))
    if (not np.isfinite(offset) or abs(offset)>.5 or K.shape!=(3,3) or T.shape!=(4,4) or not np.isfinite(K).all() or not np.isfinite(T).all()
            or K[0,0]<=0 or K[1,1]<=0 or not np.allclose(K[2],[0,0,1])
            or not np.allclose(T[3],[0,0,0,1])
            or not np.allclose(T[:3,:3].T@T[:3,:3],np.eye(3),atol=2e-5)
            or not np.isclose(np.linalg.det(T[:3,:3]),1.,atol=2e-5)):
        raise ValueError('Invalid calibrated pinhole camera / rigid BODY transform')
    return K,T


def xyz_from_depth(depth, camera):
    """H×W×3 BODY metres, float32, NaN for nonfinite/nonpositive axial depth.
    Pixels refer to the original native camera image, never a JPEG depth palette.
    """
    depth=np.asarray(depth)
    if depth.ndim!=2 or list(depth.shape)!=list(camera['image_size_hw']):
        raise ValueError('Depth and native camera image dimensions disagree')
    K,T=camera_arrays(camera)
    v,u=np.indices(depth.shape,dtype=np.float32)
    offset=float(camera.get('pixel_center_offset',0.));u+=offset;v+=offset
    rays=np.einsum('...j,ij->...i',np.stack((u,v,np.ones_like(u)),axis=-1),np.linalg.inv(K))
    valid=np.isfinite(depth)&(depth>0)
    clean=np.where(valid,depth,0.)
    points=np.einsum('...j,ij->...i',rays*clean[...,None],T[:3,:3])+T[:3,3]
    points[~valid]=np.nan
    return points.astype(np.float32)


def project_body(points, camera):
    """Project BODY points to native [u,v]; behind/nonfinite points return NaNs.
    Outside-image but forward projections remain coordinates, for explicit bounds checks.
    """
    K,T=camera_arrays(camera)
    points=np.asarray(points,dtype=float)
    if points.shape[-1:]!=(3,):raise ValueError('Expected BODY XYZ points')
    optical=np.einsum('...j,ji->...i',points-T[:3,3],T[:3,:3])
    pixels=np.einsum('...j,ij->...i',optical,K)
    valid=np.isfinite(pixels).all(axis=-1)&(optical[...,2]>0)
    denom=np.where(valid,pixels[...,2],1.)
    uv=pixels[...,:2]/denom[...,None]-float(camera.get('pixel_center_offset',0.))
    return np.where(valid[...,None],uv,np.nan)
