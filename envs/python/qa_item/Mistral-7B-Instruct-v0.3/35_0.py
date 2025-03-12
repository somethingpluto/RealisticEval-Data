from typing import List
import math

def signed_distance(point1, point2, point):
    return math.fabs(point2[0] - point1[0]) * (point[1] - point2[1]) - math.fabs(point2[1] - point1[1]) * (point[0] - point2[0])

def is_point_in_polygon(point: tuple, polygon: List[tuple]) -> bool:
    intersections = 0
    last_point = polygon[-1]
    for current_point in polygon:
        if (current_point[1] <= point[1] < last_point[1] or last_point[1] <= point[1] < current_point[1]) and \
                (point[0] < (last_point[0] - current_point[0]) * (point[1] - current_point[1]) / (last_point[1] - current_point[1]) + current_point[0]):
            if current_point[1]!= last_point[1]:
                intersections += math.copysign(1, signed_distance((last_point[0], last_point[1]), (current_point[0], current_point[1]), point))
        last_point = current_point
    return intersections % 2!= 0
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