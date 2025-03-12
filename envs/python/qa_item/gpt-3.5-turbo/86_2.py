from typing import List

def bresenham_line(x1: int, y1: int, x2: int, y2: int) -> List[tuple]:
    """
    Generates integer coordinates on the line from (x1, y1) to (x2, y2) using Bresenham's line algorithm.

    Bresenham's algorithm calculates the points of an approximately straight line between two given points on a grid.
    It is particularly well-suited for computer graphics where an efficient, integer-based algorithm is needed to
    determine which points should be rasterized to represent the line.

    Args:
        x1 (int): The x-coordinate of the starting point of the line.
        y1 (int): The y-coordinate of the starting point of the line.
        x2 (int): The x-coordinate of the ending point of the line.
        y2 (int): The y-coordinate of the ending point of the line.

    Returns:
        list of tuples: A list where each tuple contains the x and y coordinates of a point on the line.
    """
    coordinates = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x_sign = 1 if x1 < x2 else -1
    y_sign = 1 if y1 < y2 else -1

    if dx > dy:
        p = 2 * dy - dx
        while x1 != x2:
            coordinates.append((x1, y1))
            if p >= 0:
                y1 += y_sign
                p -= 2 * dx
            x1 += x_sign
            p += 2 * dy
        coordinates.append((x1, y1))
    else:
        p = 2 * dx - dy
        while y1 != y2:
            coordinates.append((x1, y1))
            if p >= 0:
                x1 += x_sign
                p -= 2 * dy
            y1 += y_sign
            p += 2 * dx
        coordinates.append((x1, y1))

    return coordinates
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