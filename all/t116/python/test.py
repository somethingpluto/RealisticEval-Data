class TestToroidalDiff(unittest.TestCase):

    def test_no_wrapping(self):
        this_point = {'x': 2, 'y': 3}
        other_point = {'x': 5, 'y': 6}
        width = 10
        height = 10
        result = toroidal_diff(this_point, other_point, width, height)
        self.assertEqual(result, [-3, -3])

    def test_wrapping_x_dimension(self):
        this_point = {'x': 9, 'y': 5}
        other_point = {'x': 1, 'y': 5}
        width = 10
        height = 10
        result = toroidal_diff(this_point, other_point, width, height)
        self.assertEqual(result, [-2, 0])  # dx wraps around the toroidal boundary

    def test_wrapping_y_dimension(self):
        this_point = {'x': 4, 'y': 9}
        other_point = {'x': 4, 'y': 1}
        width = 10
        height = 10
        result = toroidal_diff(this_point, other_point, width, height)
        self.assertEqual(result, [0, -2])  # dy wraps around the toroidal boundary

    def test_wrapping_both_dimensions(self):
        this_point = {'x': 9, 'y': 9}
        other_point = {'x': 1, 'y': 1}
        width = 10
        height = 10
        result = toroidal_diff(this_point, other_point, width, height)
        self.assertEqual(result, [-2, -2])  # Both dx and dy wrap around

    def test_same_position(self):
        this_point = {'x': 5, 'y': 5}
        other_point = {'x': 5, 'y': 5}
        width = 10
        height = 10
        result = toroidal_diff(this_point, other_point, width, height)
        self.assertEqual(result, [0, 0])  # No difference
