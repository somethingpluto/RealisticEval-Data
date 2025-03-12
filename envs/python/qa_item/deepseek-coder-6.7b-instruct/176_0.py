import math
from typing import List


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        """Calculate the Euclidean distance to another point."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def find_k_nearest_neighbors(points: List[Point], query_point: Point, k: int) -> List[Point]:
    """Find the k nearest neighbors to the query_point.

    Args:
        points (List[Point]): A list of Point objects representing the available points in the space.
        query_point (Point): The Point object for which we want to find the nearest neighbors.
        k (int): The number of nearest neighbors to find.

    Returns:
        List[Point]: A list of the k nearest Point objects to the query_point.
    """
    # Calculate distances from the query_point to all other points
    distances = [(point, query_point.distance_to(point)) for point in points]
    
    # Sort the points based on the distance
    distances.sort(key=lambda x: x[1])
    
    # Extract the k nearest neighbors
    k_nearest_neighbors = [point for point, _ in distances[:k]]
    
    return k_nearest_neighbors
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        """Calculate the Euclidean distance to another point."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)import math
import unittest


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Tester(unittest.TestCase):

    def test_find_k_nearest_neighbors_simple_case(self):
        points = [
            Point(1, 2),
            Point(3, 4),
            Point(1, -1),
            Point(5, 2)
        ]
        query_point = Point(2, 2)
        k = 2
        result = find_k_nearest_neighbors(points, query_point, k)

        self.assertEqual(len(result), 2)
        self.assertTrue(self.contains_point(result, Point(1, 2)))
        self.assertTrue(self.contains_point(result, Point(3, 4)))

    def test_find_k_nearest_neighbors_exact_match(self):
        points = [
            Point(1, 2),
            Point(2, 2),
            Point(3, 3)
        ]
        query_point = Point(2, 2)
        k = 1
        result = find_k_nearest_neighbors(points, query_point, k)

        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0].x, 2.0, delta=0.001)
        self.assertAlmostEqual(result[0].y, 2.0, delta=0.001)

    def test_find_k_nearest_neighbors_larger_k(self):
        points = [
            Point(1, 2),
            Point(3, 4),
            Point(1, -1),
            Point(5, 2)
        ]
        query_point = Point(2, 2)
        k = 5  # k is larger than the number of points
        result = find_k_nearest_neighbors(points, query_point, k)

        self.assertEqual(len(result), 4)

    def test_find_k_nearest_neighbors_empty_points(self):
        points = []
        query_point = Point(2, 2)
        k = 3
        result = find_k_nearest_neighbors(points, query_point, k)

        self.assertEqual(len(result), 0)

    def test_find_k_nearest_neighbors_all_points_equidistant(self):
        points = [
            Point(2, 3),
            Point(3, 2),
            Point(1, 2),
            Point(2, 1)
        ]
        query_point = Point(2, 2)
        k = 2
        result = find_k_nearest_neighbors(points, query_point, k)

        self.assertEqual(len(result), 2)
        self.assertTrue(self.contains_point(result, Point(2, 3)))
        self.assertTrue(self.contains_point(result, Point(3, 2)))

    def contains_point(self, points, point):
        for p in points:
            if math.isclose(p.x, point.x, abs_tol=0.001) and math.isclose(p.y, point.y, abs_tol=0.001):
                return True
        return False

if __name__ == '__main__':
    unittest.main()