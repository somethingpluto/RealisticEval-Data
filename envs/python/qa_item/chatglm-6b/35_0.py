
from typing import List

def is_point_in_polygon(point: tuple, polygon: List[tuple]) -> bool:
    """
    Determine if the point (x, y) is inside the given polygon.
    The polygon is defined as a list of tuples (x, y) representing the vertices.

    Args:
    point: A tuple (x, y) representing the point to check.
    polygon: A list of tuples (x, y) representing the vertices of the polygon.

    Returns:
    bool: True if the point is inside the polygon, False otherwise.
    """
    for vertex in polygon:
        if point == vertex[0] and point == vertex[1]:
            return True
    return False

import unittest

class TestPointInPolygon(unittest.TestCase):
    def setUp(self):
        # Define some polygons to use in tests
        self.square = [(0, 0), (0, 10), (10, 10), (10, 0)]
        self.triangle = [(0, 0), (5, 10), (10, 0)]
        self.concave = [(0, 0), (5, 5), (10, 0), (5, 10), (0, 10)]

    def test_point_inside_square(self):
        # Point inside the square
        self.assertTrue(is_point_in_polygon((5, 5), self.square))

    def test_point_outside_square(self):
        # Point outside the square
        self.assertFalse(is_point_in_polygon((15, 5), self.square))

    def test_point_on_edge_of_triangle(self):
        # Point on the edge of the triangle
        self.assertFalse(is_point_in_polygon((5, 0), self.triangle))

    def test_point_inside_concave_polygon(self):
        # Point inside concave polygon
        self.assertTrue(is_point_in_polygon((5, 9), self.concave))

    def test_point_outside_concave_polygon(self):
        # Point outside concave polygon
        self.assertFalse(is_point_in_polygon((5, 1), self.concave))
if __name__ == '__main__':
    unittest.main()