import unittest

class TestLineSegmentIntersection(unittest.TestCase):
    def test_intersecting_lines(self):
        self.assertEqual(
            get_line_segment_intersection(((1, 1), (4, 4)), ((1, 4), (4, 1))),
            (2.5, 2.5),
            "Should find intersection at (2.5, 2.5)"
        )

    def test_parallel_lines(self):
        self.assertIsNone(
            get_line_segment_intersection(((1, 1), (4, 4)), ((2, 2), (5, 5))),
            "Should return None for parallel lines"
        )

    def test_no_intersection(self):
        self.assertIsNone(
            get_line_segment_intersection(((1, 1), (2, 2)), ((3, 3), (4, 4))),
            "Should return None when there is no intersection"
        )

    def test_intersection_in_middle(self):
        result = get_line_segment_intersection(((0, 0), (4, 4)), ((0, 4), (4, 0)))
        self.assertIsNotNone(result, "Should find an intersection at the middle (2, 2)")
        self.assertAlmostEqual(result[0], 2, places=7, msg="X coordinate should be close to 2")
        self.assertAlmostEqual(result[1], 2, places=7, msg="Y coordinate should be close to 2")

    def test_identical_segments(self):
        self.assertIsNone(
            get_line_segment_intersection(((1, 1), (4, 4)), ((1, 1), (4, 4))),
            "Should return None for identical segments"
        )


from typing import Union

def get_line_segment_intersection(seg1: tuple, seg2: tuple) -> Union[tuple, None]:
    """
    Calculate the intersection point of two line segments, if it exists.

    Args:
        seg1 (tuple): Coordinates of the first line segment, defined as ((x1, y1), (x2, y2)).
        seg2 (tuple): Coordinates of the second line segment, defined as ((x3, y3), (x4, y4)).

    Returns:
        Union[tuple, None]: The (x, y) coordinates of the intersection point if the line segments intersect,
                            otherwise None.
    """
    # Unpack segment points
    (x1, y1), (x2, y2) = seg1
    (x3, y3), (x4, y4) = seg2

    # Compute direction vectors and determinant
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3
    determinant = dx1 * dy2 - dx2 * dy1

    # Check for parallel lines or identical segments
    if abs(determinant) < 1e-10:
        return None

    # Calculate intersection parameters
    t1 = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / determinant
    t2 = ((x3 - x1) * dy1 - (y3 - y1) * dx1) / determinant

    # Allow for a small tolerance in the intersection check
    tolerance = 1e-10

    # Check if intersection is within the bounds of the line segments
    if 0 - tolerance <= t1 <= 1 + tolerance and 0 - tolerance <= t2 <= 1 + tolerance:
        x = x1 + t1 * dx1
        y = y1 + t1 * dy1
        return round(x, 7), round(y, 7)

    return None
