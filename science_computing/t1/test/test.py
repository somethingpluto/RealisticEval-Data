import unittest

from task_code.t4.adapted import check_point_on_the_line


class TestOnLine(unittest.TestCase):
    def test_point_on_line(self):
        self.assertTrue(check_point_on_the_line((1, 1), (4, 4), (2, 2)), "Point should be on the line")

    def test_point_not_on_line(self):
        self.assertFalse(check_point_on_the_line((1, 1), (4, 4), (5, 5)), "Point should not be on the line")

    def test_point_not_between(self):
        self.assertFalse(check_point_on_the_line((1, 1), (4, 4), (3, 2)),
                         "Point should not be between the two points on the line")

    def test_point_on_line_but_outside_segment(self):
        self.assertFalse(check_point_on_the_line((1, 1), (4, 4), (5, 5)),
                         "Point is on the line but outside the segment")
