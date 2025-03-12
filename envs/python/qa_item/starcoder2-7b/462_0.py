from typing import List

def spiral_order(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    res = []
    up = left = 0
    right = cols - 1
    down = rows - 1

    while len(res) < rows * cols:
        # Traverse from left to right.
        for col in range(left, right + 1):
            res.append(matrix[up][col])

        # Traverse from top to down.
        for row in range(up + 1, down):
            res.append(matrix[row][right])

        # Traverse from right to left.
        if up != down:
            for col in range(right, left - 1, -1):
                res.append(matrix[down][col])

        # Traverse from down to up.
        if left != right:
            for row in range(down - 1, up, -1):
                res.append(matrix[row][left])

        left += 1
        right -= 1
        up += 1
        down -= 1

    return res
import unittest


class TestSpiralOrder(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(spiral_order([]), [])

    def test_single_row_matrix(self):
        self.assertEqual(spiral_order([[1, 2, 3]]), [1, 2, 3])

    def test_single_column_matrix(self):
        self.assertEqual(spiral_order([[1], [2], [3]]), [1, 2, 3])

    def test_square_matrix(self):
        self.assertEqual(spiral_order([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_rectangle_matrix(self):
        self.assertEqual(spiral_order([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
if __name__ == '__main__':
    unittest.main()