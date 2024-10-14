import unittest


class TestGetBezierPoint(unittest.TestCase):

    # Test case 1: Test with a simple linear curve
    def test_midpoint_of_two_points(self):
        points = [{'x': 0, 'y': 0}, {'x': 2, 'y': 2}]
        result = get_bezier_point(0.5, points)
        self.assertEqual(result, {'x': 1, 'y': 1})

    # Test case 2: Test with three points (quadratic curve)
    def test_quadratic_bezier_curve(self):
        points = [
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 0}
        ]
        result = get_bezier_point(0.5, points)
        self.assertEqual(result, {'x': 1, 'y': 1})

    # Test case 3: Test with four points (cubic curve)
    def test_cubic_bezier_curve(self):
        points = [
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 3},
            {'x': 3, 'y': 1},
            {'x': 4, 'y': 0}
        ]
        result = get_bezier_point(0.5, points)
        self.assertEqual(result, {'x': 2, 'y': 1.5})

    # Test case 4: Test with a single point (edge case)
    def test_single_control_point(self):
        points = [{'x': 5, 'y': 5}]
        result = get_bezier_point(0.5, points)
        self.assertEqual(result, {'x': 5, 'y': 5})

    # Test case 5: Test with extreme t value (0)
    def test_extreme_t_value_zero(self):
        points = [
            {'x': 0, 'y': 0},
            {'x': 5, 'y': 5}
        ]
        result = get_bezier_point(0, points)
        self.assertEqual(result, {'x': 0, 'y': 0})

    # Test case 6: Test with extreme t value (1)
    def test_extreme_t_value_one(self):
        points = [
            {'x': 0, 'y': 0},
            {'x': 5, 'y': 5}
        ]
        result = get_bezier_point(1, points)
        self.assertEqual(result, {'x': 5, 'y': 5})
