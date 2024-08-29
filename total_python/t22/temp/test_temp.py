import unittest
from typing import Tuple

class TestCalculateEuclideanDistance(unittest.TestCase):

    def test_basic_functionality(self):
        # Basic logic functionality test
        point1 = (0, 0)
        point2 = (3, 4)
        expected_distance = 5.0
        self.assertEqual(calculate_euclidean_distance(point1, point2), expected_distance, "Should calculate the distance correctly")

    def test_negative_coordinates(self):
        # Test with negative coordinates
        point1 = (-1, -1)
        point2 = (-4, -5)
        expected_distance = 5.0
        self.assertEqual(calculate_euclidean_distance(point1, point2), expected_distance, "Should handle negative coordinates correctly")

    def test_zero_distance(self):
        # Boundary test: points are the same
        point1 = (2, 3)
        point2 = (2, 3)
        expected_distance = 0.0
        self.assertEqual(calculate_euclidean_distance(point1, point2), expected_distance, "Should return 0 when both points are the same")

    def test_large_coordinates(self):
        # Boundary test: large coordinates
        point1 = (1e6, 1e6)
        point2 = (1e6 + 3, 1e6 + 4)
        expected_distance = 5.0
        self.assertEqual(calculate_euclidean_distance(point1, point2), expected_distance, "Should handle large coordinates correctly")

    def test_invalid_input(self):
        # Exception handling test: invalid input (non-tuple)
        with self.assertRaises(TypeError):
            calculate_euclidean_distance("invalid", (0, 0))

if __name__ == "__main__":
    unittest.main()

from typing import Tuple


def calculate_euclidean_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    """
    Calculate the Euclidean distance between two points in a 2D space.

    Args:
        point1 (Tuple[float, float]): The first point as a tuple of coordinates (x1, y1).
        point2 (Tuple[float, float]): The second point as a tuple of coordinates (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.

    """
    if not (isinstance(point1, tuple) and isinstance(point2, tuple)):
        raise TypeError("Both points must be tuples")

    if not (len(point1) == 2 and len(point2) == 2):
        raise TypeError("Both points must be tuples of two elements")

    if not (all(isinstance(coord, (int, float)) for coord in point1) and
            all(isinstance(coord, (int, float)) for coord in point2)):
        raise TypeError("All coordinates must be integers or floats")

    # Extract coordinates from the input tuples
    x1, y1 = point1
    x2, y2 = point2

    # Compute differences and Euclidean distance using the Pythagorean theorem
    dx = x2 - x1
    dy = y2 - y1

    return (dx ** 2 + dy ** 2) ** 0.5
