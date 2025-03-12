from typing import List
from math import inf

def is_point_in_polygon(point: tuple, polygon: List[tuple]) -> bool:
    x, y = point
    n = len(polygon)
    inside = False

    min_x = min(p[0] for p in polygon)
    min_y = min(p[1] for p in polygon)
    max_x = max(p[0] for p in polygon)
    max_y = max(p[1] for p in polygon)

    if x < min_x or x > max_x or y < min_y or y > max_y:
        return False

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        if y1 == y2:
            continue

        if y > min(y1, y2):
            if y <= max(y1, y2):
                if x <= max(x1, x2):
                    if y1 != y2:
                        xinters = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                    if x1 == x2 or x <= xinters:
                        inside = not inside

    return inside
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