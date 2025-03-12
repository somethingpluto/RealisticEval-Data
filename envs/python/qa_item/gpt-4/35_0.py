from typing import List

def is_point_in_polygon(point: tuple, polygon: List[tuple]) -> bool:
    def is_left(p0, p1, p2):
        return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])

    n = len(polygon)
    if n < 3:
        return False

    count = 0
    for i in range(n):
        if polygon[i] == point:
            return True
        j = (i + 1) % n
        if polygon[i][1] == polygon[j][1]:
            continue
        if min(polygon[i][1], polygon[j][1]) < point[1] <= max(polygon[i][1], polygon[j][1]):
            if point[0] <= max(polygon[i][0], polygon[j][0]):
                if polygon[i][1] != polygon[j][1]:
                    xinters = (point[1] - polygon[i][1]) * (polygon[j][0] - polygon[i][0]) / (polygon[j][1] - polygon[i][1]) + polygon[i][0]
                    if polygon[i][0] == polygon[j][0] or point[0] <= xinters:
                        count += 1
    return count % 2 == 1
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