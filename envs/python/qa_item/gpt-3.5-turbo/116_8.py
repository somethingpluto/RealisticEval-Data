from typing import Dict, List

def calculate_toroidal_difference(point_a: Dict[str, float], point_b: Dict[str, float], width: float, height: float) -> List[float]:
    """
    Calculates the toroidal difference between two points in a wrap-around space.

    Args:
        point_a (Dict[str, float]): The first point with keys 'x' and 'y'.
        point_b (Dict[str, float]): The second point with keys 'x' and 'y'.
        width (float): The width of the toroidal space.
        height (float): The height of the toroidal space.

    Returns:
        List[float]: A list containing the x and y differences, accounting for wrap-around.
    """
    x_diff = point_a['x'] - point_b['x']
    y_diff = point_a['y'] - point_b['y']
    
    # Calculate toroidal differences
    if abs(x_diff) > width / 2:
        x_diff = (width - abs(x_diff)) * (-1 if x_diff > 0 else 1)
    
    if abs(y_diff) > height / 2:
        y_diff = (height - abs(y_diff)) * (-1 if y_diff > 0 else 1)
    
    return [x_diff, y_diff]
import unittest


class TestToroidalDiff(unittest.TestCase):

    def test_no_wrapping(self):
        this_point = {'x': 2, 'y': 3}
        other_point = {'x': 5, 'y': 6}
        width = 10
        height = 10
        result = calculate_toroidal_difference(this_point, other_point, width, height)
        self.assertEqual(result, [-3, -3])

    def test_wrapping_x_dimension(self):
        this_point = {'x': 9, 'y': 5}
        other_point = {'x': 1, 'y': 5}
        width = 10
        height = 10
        result = calculate_toroidal_difference(this_point, other_point, width, height)
        self.assertEqual(result, [-2, 0])  # dx wraps around the toroidal boundary

    def test_wrapping_y_dimension(self):
        this_point = {'x': 4, 'y': 9}
        other_point = {'x': 4, 'y': 1}
        width = 10
        height = 10
        result = calculate_toroidal_difference(this_point, other_point, width, height)
        self.assertEqual(result, [0, -2])  # dy wraps around the toroidal boundary

    def test_wrapping_both_dimensions(self):
        this_point = {'x': 9, 'y': 9}
        other_point = {'x': 1, 'y': 1}
        width = 10
        height = 10
        result = calculate_toroidal_difference(this_point, other_point, width, height)
        self.assertEqual(result, [-2, -2])  # Both dx and dy wrap around

    def test_same_position(self):
        this_point = {'x': 5, 'y': 5}
        other_point = {'x': 5, 'y': 5}
        width = 10
        height = 10
        result = calculate_toroidal_difference(this_point, other_point, width, height)
        self.assertEqual(result, [0, 0])  # No difference

if __name__ == '__main__':
    unittest.main()