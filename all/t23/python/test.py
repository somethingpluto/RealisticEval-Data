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

