def bezier(t: float, p0: float, p1: float, p2: float, p3: float) -> float:
    """
    Calculates the value of a cubic Bezier curve at a given parameter t.

    Args:
        t (float): The parameter value between 0 and 1 that represents a position along the curve.
        p0 (float): The first control point of the curve, typically where the curve starts.
        p1 (float): The second control point, which influences the tangent at the beginning of the curve.
        p2 (float): The third control point, which influences the tangent at the end of the curve.
        p3 (float): The fourth control point, typically where the curve ends.

    Returns:
        float: The point on the Bezier curve corresponding to the parameter t.
    """
    return (1 - t)**3 * p0 + 3 * t * (1 - t)**2 * p1 + 3 * t**2 * (1 - t) * p2 + t**3 * p3
import unittest

class TestAnswer(unittest.TestCase):

    def test_bezier_at_start(self):
        self.assertAlmostEqual(bezier(0, 1, 3, 3, 1), 1.0,
                               msg="Bezier at t=0 should return the first control point p0")

    def test_bezier_at_end(self):
        self.assertAlmostEqual(bezier(1, 1, 3, 3, 1), 1.0,
                               msg="Bezier at t=1 should return the last control point p3")

    def test_bezier_at_middle(self):
        expected = 1.0 * 0.125 + 3 * 0.375 + 3 * 0.375 + 1 * 0.125  # Calculate manually for t=0.5
        self.assertAlmostEqual(bezier(0.5, 1, 3, 3, 1), expected,
                               delta=0.001,
                               msg="Bezier at t=0.5 should return the correct middle value")

    def test_bezier_with_identical_control_points(self):
        self.assertAlmostEqual(bezier(0.5, 2, 2, 2, 2), 2.0,
                               msg="Bezier with all control points the same should return that value")

if __name__ == '__main__':
    unittest.main()