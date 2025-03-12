from typing import List

def is_point_in_polygon(point: tuple, polygon: List[tuple]) -> bool:
    def is_inside(x, y, xp, yp):
        n = len(xp)
        c = False
        for i in range(n):
            j = (i + 1) % n
            if ((yp[i] <= y and y < yp[j]) or (yp[j] <= y and y < yp[i])) and \
                    (x < (xp[j] - xp[i]) * (y - yp[i]) / (yp[j] - yp[i]) + xp[i]):
                c = not c
        return c

    x, y = point
    xp, yp = zip(*polygon)
    return is_inside(x, y, xp, yp)
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