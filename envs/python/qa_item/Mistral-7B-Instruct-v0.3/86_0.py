from typing import List

def bresenham_line(x1: int, y1: int, x2: int, y2: int) -> List[tuple]:
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x = x1
    y = y1
    steps = 2 * dy - dx

    points = []
    points.append((x, y))

    while x < x2 if x1 < x2 else x > x2:
        x += 1 if x1 < x2 else -1
        if steps > 0:
            y += 1 if y1 < y2 else -1
            steps -= 2 * dx
        else:
            steps += 2 * dy

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