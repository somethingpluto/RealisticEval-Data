from typing import Union

def check_segments_intersection(seg1: tuple, seg2: tuple) -> Union[tuple, None]:
    """
    Calculate the intersection point of two line segments, if it exists.

    Args:
        seg1 (tuple): Coordinates of the first line segment, defined as ((x1, y1), (x2, y2)).
        seg2 (tuple): Coordinates of the second line segment, defined as ((x3, y3), (x4, y4)).

    Returns:
        Union[tuple, None]: The (x, y) coordinates of the intersection point if the line segments intersect,
                            otherwise None.
    """
    
    def ccw(A, B, C):
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

    def intersect(seg1, seg2):
        A, B = seg1
        C, D = seg2
        return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

    x1, y1 = seg1[0]
    x2, y2 = seg1[1]
    x3, y3 = seg2[0]
    x4, y4 = seg2[1]

    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)

    if denom == 0:  # Lines are parallel
        return None

    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom

    if ua >= 0 and ua <= 1 and ub >= 0 and ub <= 1:
        x = x1 + ua * (x2 - x1)
        y = y1 + ua * (y2 - y1)
        return x, y
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