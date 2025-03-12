import numpy as np

def cubic_bezier(t: float, p0: list, p1: list, p2: list, p3: list) -> list:
    """
    Calculate the coordinates of a cubic Bézier curve at a given parameter t (typically between 0 and 1).

    Args:
        t (float): A float representing the parameter along the curve, where 0 <= t <= 1.
        p0 (list): A list of size 2 representing the x and y coordinates of the start point.
        p1 (list): A list of size 2 representing the x and y coordinates of the first control point.
        p2 (list): A list of size 2 representing the x and y coordinates of the second control point.
        p3 (list): A list of size 2 representing the x and y coordinates of the end point.

    Returns:
        list: A list of size 2 containing the x and y coordinates of the point on the curve corresponding to the parameter t.
    """
    x = (1 - t)**3 * p0[0] + 3 * t * (1 - t)**2 * p1[0] + 3 * t**2 * (1 - t) * p2[0] + t**3 * p3[0]
    y = (1 - t)**3 * p0[1] + 3 * t * (1 - t)**2 * p1[1] + 3 * t**2 * (1 - t) * p2[1] + t**3 * p3[1]
    
    return [x, y]
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