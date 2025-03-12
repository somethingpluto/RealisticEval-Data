from __future__ import division
from math import (
    sqrt,
    pow,
)
from typing import Tuple

def find_t_for_x(target_x: float, p0: Tuple[float, float], p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """
    Find the parameter t corresponding to a given x-coordinate target_x
    on a quadratic Bézier curve defined by control points p0, p1, and p2.

    Args:
        target_x (float): The x-coordinate for which we want to find the corresponding parameter t.
        p0 (Tuple[float, float]): The first control point of the Bézier curve.
        p1 (Tuple[float, float]): The second control point of the Bézier curve.
        p2 (Tuple[float, float]): The third control point of the Bézier curve.

    Returns:
        float: The parameter t (in the range [0, 1]) for which the Bézier curve evaluated at t is closest to target_x.
    """

    def bezier_curve(t: float) -> float:
        return pow((1 - t), 2) * p0[0] + 2 * t * (1 - t) * p1[0] + pow(t, 2) * p2[0]

    def bezier_curve_derivative(t: float) -> float:
        return 2 * (1 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0])

    def find_t_interval(lower_bound: float, upper_bound: float) -> Tuple[float, float]:
        if abs(bezier_curve(upper_bound) - target_x) > abs(bezier_curve(lower_bound) - target_x):
            return find_t_interval(upper_bound, (upper_bound + lower_bound) / 2)
        else:
            return (lower_bound, upper_bound)

    lower_bound, upper_bound = 0, 1
    while abs(bezier_curve(upper_bound) - target_x) > 1e-6:
        lower_bound, upper_bound = find_t_interval(lower_bound, upper_bound)

    t = (lower_bound + upper_bound) / 2
    while abs(bezier_curve_derivative(t)) > 1e-6:
        if abs(bezier_curve(t + 1e-6) - target_x) < abs(bezier_curve(t) - target_x):
            t += 1e-6
        else:
            t -= 1e-6

    return t
import unittest

class TestFindxTForX(unittest.TestCase):
    TOLERANCE = 1e-6

    def test_find_t_for_x_at_start(self):
        p0 = 0.0
        p1 = 0.5
        p2 = 1.0
        target_x = 0.0
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 0.0, delta=self.TOLERANCE)

    def test_find_t_for_x_at_end(self):
        p0 = 0.0
        p1 = 0.5
        p2 = 1.0
        target_x = 1.0
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 1.0, delta=self.TOLERANCE)

    def test_find_t_for_x_mid_curve(self):
        p0 = 0.0
        p1 = 0.5
        p2 = 1.0
        target_x = 0.25
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 0.25, delta=self.TOLERANCE)

    def test_find_t_for_x_near_mid_curve(self):
        p0 = 0.0
        p1 = 1.0
        p2 = 2.0
        target_x = 1.5
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 0.75, delta=self.TOLERANCE)
if __name__ == '__main__':
    unittest.main()