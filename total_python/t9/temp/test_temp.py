import unittest


def is_point_on_line(A, B, C):
    (x_a, y_a), (x_b, y_b), (x_c, y_c) = A, B, C
    if x_a == x_b:  # Check for vertical line
        return x_c == x_a
    return (y_c - y_a) * (x_b - x_a) == (y_b - y_a) * (x_c - x_a)


class TestPointOnLine(unittest.TestCase):
    def test_point_on_line(self):
        A = (0, 0)
        B = (10, 10)
        C = (5, 5)
        self.assertTrue(is_point_on_line(A, B, C))

    def test_point_not_on_line(self):
        A = (0, 0)
        B = (10, 10)
        C = (5, 6)
        self.assertFalse(is_point_on_line(A, B, C))

    def test_vertical_line(self):
        A = (5, 0)
        B = (5, 10)
        C = (5, 5)
        self.assertTrue(is_point_on_line(A, B, C))

    def test_horizontal_line(self):
        A = (0, 5)
        B = (10, 5)
        C = (5, 5)
        self.assertTrue(is_point_on_line(A, B, C))

    def test_point_not_on_vertical_line(self):
        A = (5, 0)
        B = (5, 10)
        C = (6, 5)
        self.assertFalse(is_point_on_line(A, B, C))
from typing import List


def is_point_on_line(A: List[int], B: List[int], C: List[int]) -> bool:
    """
    Check whether A point is on a line formed by two points, such as point C is on a line formed by points A and B
    Args:
        A (List[int]): point A xy
        B (List[int]): point B xy
        C (List[int]): point C xy

    Returns: is C in line of A B

    """
    (x_a, y_a), (x_b, y_b), (x_c, y_c) = A, B, C

    # Handle the vertical line case where the x-coordinates of points A and B are the same
    if x_a == x_b:
        return x_c == x_a  # C must also have the same x-coordinate

    # Calculate slopes using the formula (y2 - y1) / (x2 - x1)
    # Check if slopes of AC and BC are equal
    return (y_c - y_a) * (x_b - x_a) == (y_b - y_a) * (x_c - x_a)
