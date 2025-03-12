from typing import List

def cubic_bezier(t: float, p0: List[float], p1: List[float], p2: List[float], p3: List[float]) -> List[float]:
    def lerp(a, b, t):
        return a + (b - a) * t
    
    def bezier_point(t, p0, p1, p2, p3):
        x = lerp(lerp(lerp(p0[0], p1[0], t), lerp(p1[0], p2[0], t), t), lerp(lerp(p1[0], p2[0], t), lerp(p2[0], p3[0], t), t), t)
        y = lerp(lerp(lerp(p0[1], p1[1], t), lerp(p1[1], p2[1], t), t), lerp(lerp(p1[1], p2[1], t), lerp(p2[1], p3[1], t), t), t)
        return [x, y]
    
    return bezier_point(t, p0, p1, p2, p3)
import unittest
from typing import List

class TestCubicBezier(unittest.TestCase):
    def test_cubic_bezier_t0(self):
        p0 = [0.0, 0.0]
        p1 = [0.0, 1.0]
        p2 = [1.0, 1.0]
        p3 = [1.0, 0.0]
        t = 0.0
        expected = [0.0, 0.0]
        self.assertAlmostEqual(cubic_bezier(t, p0, p1, p2, p3), expected)

    def test_cubic_bezier_t1(self):
        p0 = [0.0, 0.0]
        p1 = [0.0, 1.0]
        p2 = [1.0, 1.0]
        p3 = [1.0, 0.0]
        t = 1.0
        expected = [1.0, 0.0]
        self.assertAlmostEqual(cubic_bezier(t, p0, p1, p2, p3), expected)

    def test_cubic_bezier_t0_5(self):
        p0 = [0.0, 0.0]
        p1 = [0.0, 1.0]
        p2 = [1.0, 1.0]
        p3 = [1.0, 0.0]
        t = 0.5
        expected = [0.5, 0.75]
        self.assertAlmostEqual(cubic_bezier(t, p0, p1, p2, p3), expected, places=9)

    def test_cubic_bezier_mid_point(self):
        p0 = [0.0, 0.0]
        p1 = [1.0, 1.0]
        p2 = [2.0, 1.0]
        p3 = [3.0, 0.0]
        t = 0.5
        expected = [1.5, 0.75]
        self.assertAlmostEqual(cubic_bezier(t, p0, p1, p2, p3), expected, places=9)

    def test_cubic_bezier_arbitrary_t(self):
        p0 = [0.0, 0.0]
        p1 = [0.0, 2.0]
        p2 = [2.0, 2.0]
        p3 = [2.0, 0.0]
        t = 0.75
        expected = [1.6875, 1.125]
        self.assertAlmostEqual(cubic_bezier(t, p0, p1, p2, p3), expected, places=9)
if __name__ == '__main__':
    unittest.main()