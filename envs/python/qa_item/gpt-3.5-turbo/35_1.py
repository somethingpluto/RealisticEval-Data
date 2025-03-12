from typing import List

def is_point_in_polygon(point: tuple, polygon: List[tuple]) -> bool:
    def is_point_on_segment(p: tuple, q: tuple, r: tuple) -> bool:
        if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
            return True
        return False

    def orientation(p: tuple, q: tuple, r: tuple) -> int:
        val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1]))
        if val == 0:
            return 0
        return 1 if val > 0 else -1

    def do_intersect(p1: tuple, q1: tuple, p2: tuple, q2: tuple) -> bool:
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return True

        if (o1 == 0 and is_point_on_segment(p1, p2, q1)):
            return True

        if (o2 == 0 and is_point_on_segment(p1, q2, q1)):
            return True

        if (o3 == 0 and is_point_on_segment(p2, p1, q2)):
            return True

        if (o4 == 0 and is_point_on_segment(p2, q1, q2)):
            return True

        return False

    n = len(polygon)
    if n < 3:
        return False

    extreme = (float('inf'), point[1])
    count = 0
    i = 0

    while True:
        next_point = (i + 1) % n
        if do_intersect(polygon[i], polygon[next_point], point, extreme):
            if orientation(polygon[i], point, polygon[next_point]) == 0:
                return is_point_on_segment(polygon[i], point, polygon[next_point])
            count += 1
        i = next_point
        if i == 0:
            break

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