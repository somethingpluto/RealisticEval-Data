import unittest


class TestLineSegmentIntersection(unittest.TestCase):
    def test_intersecting_lines(self):
        self.assertEqual(get_line_segment_intersection(((1, 1), (4, 4)), ((1, 4), (4, 1))), (2.5, 2.5))

    def test_parallel_lines(self):
        self.assertIsNone(get_line_segment_intersection(((1, 1), (4, 4)), ((2, 2), (5, 5))))

    def test_no_intersection(self):
        self.assertIsNone(get_line_segment_intersection(((1, 1), (2, 2)), ((3, 3), (4, 4))))
