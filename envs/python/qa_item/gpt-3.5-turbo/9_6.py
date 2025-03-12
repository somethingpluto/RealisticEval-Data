from typing import List

def is_point_on_line(A: List[int], B: List[int], C: List[int]) -> bool:
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    
    return (x3 - x1) * (y2 - y1) == (y3 - y1) * (x2 - x1)
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

if __name__ == '__main__':
    unittest.main()