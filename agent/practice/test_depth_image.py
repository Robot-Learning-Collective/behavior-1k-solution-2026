"""CPU/OFFLINE image fixtures only; no provider/simulator/GPU evidence."""
import hashlib
from pathlib import Path
import tempfile
import unittest
import numpy as np
from PIL import Image
from depth_image import depth_rgb, compose_depth


class DepthImageTest(unittest.TestCase):
    def test_fixed_positive_invalid_far_mapping(self):
        depth = np.array([[0,-1,np.nan,np.inf,-np.inf],[.00001,.6,1.2,2.4,99]],dtype=np.float32)
        rgb = depth_rgb(depth)
        self.assertTrue((rgb[0] == [255,0,255]).all())
        self.assertEqual(rgb[1,:,0].tolist(),[0,64,128,255,255])
        self.assertTrue((rgb[1,:,0] == rgb[1,:,1]).all())
        self.assertTrue((depth_rgb(depth[...,None]) == rgb).all())

    def test_shape_rejects_point_cloud_or_multiple_channels(self):
        with self.assertRaises(AssertionError): depth_rgb(np.zeros((2,2,3)))
        with self.assertRaises(AssertionError): depth_rgb(np.zeros(3))

    def test_layout_nearest_sources_diagnostics_and_no_paths(self):
        with tempfile.TemporaryDirectory() as t:
            source = Path(t)/'observation_000123.jpg'
            rgb = Image.new('RGB',(1440,480))
            colors = [(30,100,180),(100,70,30),(50,90,110)]
            for index,color in enumerate(colors): rgb.paste(Image.new('RGB',(480,480),color),(index*480,0))
            rgb.save(source,quality=86)
            original = source.read_bytes()
            endpoint = {'image':str(source),'observation_id':123,'action_id':'CPUfixture','simulated_seconds':2,'wall_seconds':4.2,'capture_monotonic_ns':17,'robot':{}}
            raw = np.array([[1.2,2.4],[np.nan,.6]],dtype=np.float32)
            out, diagnostic = compose_depth(endpoint,raw,'HEADfixture')
            self.assertEqual(source.read_bytes(),original)
            self.assertEqual(out['image_layout']['dimensions'],[1920,480])
            self.assertEqual(out['image_layout']['action_id'],'CPUfixture')
            self.assertEqual(out['image_layout']['step'],60)
            self.assertNotIn(t,str(out['image_layout']))
            self.assertEqual(diagnostic['raw_depth_dtype'],'float32')
            self.assertEqual(diagnostic['raw_depth_shape'],[2,2])
            self.assertEqual(diagnostic['raw_depth_sha256'],hashlib.sha256(raw.tobytes()).hexdigest())
            self.assertEqual(diagnostic['finite_positive_count'],3)
            self.assertEqual(diagnostic['nonfinite_count'],1)
            self.assertNotIn('finite_positive_count',out['image_layout'])
            with Image.open(out['image']) as image:
                self.assertEqual(image.size,(1920,480))
                p=np.asarray(image)
                for index,color in enumerate(colors):
                    self.assertTrue(np.max(np.abs(p[300,index*480+120].astype(int)-np.array(color)))<6)
                self.assertTrue(np.max(np.abs(p[120,1560].astype(int)-128))<6)
                self.assertTrue(np.max(np.abs(p[120,1800].astype(int)-255))<6)
                self.assertTrue(np.max(np.abs(p[360,1560].astype(int)-np.array([255,0,255])))<6)
                self.assertTrue(np.max(np.abs(p[360,1800].astype(int)-64))<6)
            self.assertEqual(out['image_layout']['delivered_image_sha256'],hashlib.sha256(Path(out['image']).read_bytes()).hexdigest())


if __name__ == '__main__': unittest.main()
