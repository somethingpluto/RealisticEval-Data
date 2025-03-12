from typing import Tuple
import numpy as np

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
    p0, p1, p2 = np.array(p0), np.array(p1), np.array(p2)
    t = 0.5  # initial guess
    eps = 1e-6  # convergence criterion

    while True:
        # Compute the derivative of the Bézier curve at t
        derivative = 2 * (1 - t) * (p1 - p0) + 2 * t * (p2 - p1)
        # Compute the value of the Bézier curve at t
        bezier_curve = (1 - t)**2 * p0 + 2 * (1 - t) * t * p1 + t**2 * p2
        # Compute the error between the target x-coordinate and the Bézier curve at t
        error = target_x - bezier_curve[0]
        # If the error is small enough, we have found the solution
        if abs(error) < eps:
            return t
        # Update the parameter t using the Newton-Raphson method
        t = t - error / derivative[0]
        # Clip t to the range [0, 1]
        t = max(0, min(t, 1))
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