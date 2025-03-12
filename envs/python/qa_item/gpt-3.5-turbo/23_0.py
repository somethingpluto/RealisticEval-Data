from typing import Union

def check_segments_intersection(seg1: tuple, seg2: tuple) -> Union[tuple, None]:
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else -1

    def on_segment(p, q, r):
        if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
            return True
        return False

    p1, q1 = seg1
    p2, q2 = seg2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return ((p1[0] * q1[1] - p1[1] * q1[0]) * (p2[0] - q2[0]) - (p1[0] - q1[0]) * (p2[0] * q2[1] - p2[1] * q2[0]),
                (p1[0] * q1[1] - p1[1] * q1[0]) * (p2[1] - q2[1]) - (p1[1] - q1[1]) * (p2[0] * q2[1] - p2[1] * q2[0])) / \
               ((p1[0] - q1[0]) * (p2[1] - q2[1]) - (p1[1] - q1[1]) * (p2[0] - q2[0])
    elif o1 == 0 and on_segment(p1, p2, q1):
        return p2
    elif o2 == 0 and on_segment(p1, q2, q1):
        return q2
    elif o3 == 0 and on_segment(p2, p1, q2):
        return p1
    elif o4 == 0 and on_segment(p2, q1, q2):
        return q1
    else:
        return None
import unittest

class TestLineSegmentIntersection(unittest.TestCase):

    def test_intersection(self):
        seg1 = ((1, 1), (4, 4))
        seg2 = ((1, 4), (4, 1))
        expected = (2.5, 2.5)
        result = check_segments_intersection(seg1, seg2)
        self.assertEqual(result, expected, "The intersection should be at (2.5, 2.5)")

    def test_no_intersection(self):
        seg1 = ((1, 1), (2, 2))
        seg2 = ((3, 3), (4, 4))
        result = check_segments_intersection(seg1, seg2)
        self.assertIsNone(result, "There should be no intersection")

    def test_parallel_segments(self):
        seg1 = ((1, 1), (2, 2))
        seg2 = ((1, 2), (2, 3))
        result = check_segments_intersection(seg1, seg2)
        self.assertIsNone(result, "Parallel segments should not intersect")

    def test_no_intersection_due_to_offset(self):
        seg1 = ((1, 1), (3, 3))
        seg2 = ((3, 2), (4, 2))
        result = check_segments_intersection(seg1, seg2)
        self.assertIsNone(result, "There should be no intersection due to offset between segments")

    def test_intersection_with_large_coordinates(self):
        seg1 = ((1000, 1000), (2000, 2000))
        seg2 = ((1000, 2000), (2000, 1000))
        expected = (1500.0, 1500.0)
        result = check_segments_intersection(seg1, seg2)
        self.assertEqual(result, expected, "The intersection should be at (1500.0, 1500.0)")



if __name__ == '__main__':
    unittest.main()