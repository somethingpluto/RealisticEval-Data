
import math
from typing import List

def pascal_triangle_row(i: int) -> List:
    """
    Generates the ith row of Pascal's Triangle.

    Args:
        i (int): Row index (0-indexed)

    Returns:
        List: A list representing the ith row of Pascal's Triangle
    """
    row_count = math.floor(i / 10)
    row = [0] * row_count
    for j in range(1, row_count + 1):
        row[j] = i - row[j - 1]
    return row

import unittest


class TestPascalTriangleRow(unittest.TestCase):

    def test_row_0(self):
        """ Test the 0th row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(0), [1])

    def test_row_1(self):
        """ Test the 1st row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(1), [1, 1])

    def test_row_2(self):
        """ Test the 2nd row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(2), [1, 2, 1])

    def test_row_3(self):
        """ Test the 3rd row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(3), [1, 3, 3, 1])

    def test_row_4(self):
        """ Test the 4th row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(4), [1, 4, 6, 4, 1])

    def test_row_5(self):
        """ Test the 5th row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(5), [1, 5, 10, 10, 5, 1])

if __name__ == '__main__':
    unittest.main()