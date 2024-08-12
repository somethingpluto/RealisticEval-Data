import unittest


class TestBresenhamLineAlgorithm(unittest.TestCase):
    def test_horizontal_line(self):
        """Test a horizontal line from left to right."""
        result = bresenham_line(1, 5, 10, 5)
        expected = [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5)]
        self.assertEqual(result, expected)

    def test_vertical_line(self):
        """Test a vertical line from top to bottom."""
        result = bresenham_line(7, 2, 7, 10)
        expected = [(7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10)]
        self.assertEqual(result, expected)

    def test_diagonal_line(self):
        """Test a diagonal line."""
        result = bresenham_line(0, 0, 5, 5)
        expected = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        self.assertEqual(result, expected)

    def test_negative_slope_line(self):
        """Test a line with a negative slope."""
        result = bresenham_line(6, 8, 1, 3)
        expected = [(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3)]
        self.assertEqual(result, expected)

    def test_steep_slope_line(self):
        """Test a line that is steeper than it is wide."""
        result = bresenham_line(2, 2, 3, 7)
        expected = [(2, 2), (2, 3), (2, 4), (3, 5), (3, 6), (3, 7)]
        self.assertEqual(result, expected)

def bresenham_line(x1, y1, x2, y2):
    """
    Generate points of a line using Bresenham's line algorithm between two points.

    Args:
    x1, y1: Coordinates of the start point.
    x2, y2: Coordinates of the end point.

    Returns:
    list of tuples: A list of points (tuples of x and y coordinates) that the line passes through.
    """
    points = []
    dx = abs(x2 - x1)
    dy = -abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx + dy  # error value e_xy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        # horizontal step
        if e2 >= dy:
            if x1 == x2:
                break
            err += dy
            x1 += sx
        # vertical step
        if e2 <= dx:
            if y1 == y2:
                break
            err += dx
            y1 += sy

    return points
