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
    def bezier_x(t: float, p0: Tuple[float, float], p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
        return (1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]

    def derivative_bezier_x(t: float, p0: Tuple[float, float], p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
        return 2 * (1 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0])

    t = 0.0
    step = 0.01
    min_distance = float('inf')
    best_t = 0.0

    while t <= 1.0:
        x = bezier_x(t, p0, p1, p2)
        distance = abs(target_x - x)
        if distance < min_distance:
            min_distance = distance
            best_t = t
        t += step

    # Refine the result using Newton's method
    for _ in range(10):
        t = best_t
        x = bezier_x(t, p0, p1, p2)
        derivative = derivative_bezier_x(t, p0, p1, p2)
        if derivative == 0.0:
            break
        t -= (x - target_x) / derivative

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