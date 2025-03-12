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

    # Unpack the coordinates
    (x1, y1), (x2, y2) = seg1
    (x3, y3), (x4, y4) = seg2

    # Calculate the determinant and coefficients
    denominator = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

    if denominator == 0:
        return None  # No intersection if the line segments are parallel

    x = ((x1 * (y3 - y4) - y1 * (x3 - x4)) / denominator)
    y = ((y1 * (x3 - x4) - x1 * (y3 - y4)) / denominator)

    # Check if the intersection point is within the line segments
    if (x >= min(x1, x2) and x <= max(x1, x2)) and (y >= min(y1, y2) and y <= max(y1, y2)) and \
       (x >= min(x3, x4) and x <= max(x3, x4)) and (y >= min(y3, y4) and y <= max(y3, y4)):
        return (x, y)

    return None  # No intersection if the intersection point is not within both line segments
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