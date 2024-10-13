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