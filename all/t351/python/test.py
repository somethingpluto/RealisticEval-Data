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
