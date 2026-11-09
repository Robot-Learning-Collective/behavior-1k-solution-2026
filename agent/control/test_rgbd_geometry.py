"""CPU projection/unprojection and invalid-depth tests, without simulator/RPC."""
import copy
import unittest
import numpy as np
from rgbd_geometry import xyz_from_depth, project_body


class GeometryTest(unittest.TestCase):
    def test_native_pixel_roundtrip_and_body_axes(self):
        for h,w in ((480,480),(720,720),(3,7)):
            camera={'image_size_hw':[h,w],'intrinsics':[[388.,0.,w/2],[0.,391.,h/2],[0.,0.,1.]],
                    'camera_to_body':[[0.,-1.,0.,.2],[1.,0.,0.,-.1],[0.,0.,1.,.3],[0.,0.,0.,1.]]}
            depth=np.linspace(.2,4.,h*w,dtype=np.float32).reshape(h,w)
            xyz=xyz_from_depth(depth,camera)
            self.assertEqual(xyz.shape,(h,w,3));self.assertEqual(xyz.dtype,np.float32)
            uv=project_body(xyz,camera);v,u=np.indices((h,w))
            self.assertLess(np.max(np.abs(uv-np.stack((u,v),axis=-1))),.0003)
            if h>=480:
                d=depth[h//2,w//2]
                np.testing.assert_allclose(xyz[h//2,w//2],[.2,-.1,d+.3],atol=1e-6)
                self.assertLess(xyz[h//2,w//2+1,0],.201)
                self.assertGreater(xyz[h//2,w//2+1,1],-.1)

    def test_invalids_and_calibration_rejection(self):
        c={'image_size_hw':[2,3],'intrinsics':np.eye(3).tolist(),'camera_to_body':np.eye(4).tolist()}
        depth=np.array([[0.,-1.,np.inf],[np.nan,1.,100.]],dtype=np.float32)
        xyz=xyz_from_depth(depth,c)
        self.assertTrue(np.isnan(xyz[0]).all());self.assertTrue(np.isnan(xyz[1,0]).all())
        np.testing.assert_allclose(xyz[1,2],[200.,100.,100.]) # No 2.4m palette saturation.
        self.assertTrue(np.isnan(project_body([[0.,0.,0.],[0.,0.,-1.]],c)).all())
        with self.assertRaises(ValueError):xyz_from_depth(depth[:1],c)
        for key,index,value in [('intrinsics',(0,0),0.),('camera_to_body',(0,0),2.)]:
            bad=copy.deepcopy(c);bad[key][index[0]][index[1]]=value
            with self.assertRaises(ValueError):xyz_from_depth(depth,bad)


if __name__=='__main__':unittest.main()
