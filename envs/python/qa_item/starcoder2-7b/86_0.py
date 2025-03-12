from typing import List

def bresenham_line(x1: int, y1: int, x2: int, y2: int) -> List[tuple]:
    dx = x2 - x1
    dy = y2 - y1

    x, y = x1, y1

    points = []

    is_steep = abs(dy) > abs(dx)

    if is_steep:
        dx, dy = dy, dx

    if dx >= 0:
        step = 1
    else:
        dx = -dx
        step = -1

    error = dx // 2

    for _ in range(abs(dx)):
        if error >= abs(dy):
            error -= abs(dy)
            x += step
        else:
            y += step if is_steep else 0
            error += abs(dx)

        points.append((x, y))

    return points
import unittest


class TestBresenhamLineAlgorithm(unittest.TestCase):
    def test_horizontal_line(self):
        self.assertEqual(bresenham_line(1, 5, 5, 5), [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])

    def test_vertical_line(self):
        self.assertEqual(bresenham_line(3, 2, 3, 6), [(3, 2), (3, 3), (3, 4), (3, 5), (3, 6)])

    def test_diagonal_line(self):
        self.assertEqual(bresenham_line(2, 2, 6, 6), [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])

    def test_steep_slope(self):
        self.assertEqual(bresenham_line(1, 1, 4, 6), [(1, 1), (2, 2), (2, 3), (3, 4), (3, 5), (4, 6)])

    def test_negative_slope(self):
        self.assertEqual(bresenham_line(5, 1, 1, 5), [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)])

if __name__ == '__main__':
    unittest.main()