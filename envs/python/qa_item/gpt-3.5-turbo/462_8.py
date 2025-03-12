from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    result = []
    if not matrix:
        return result

    top_row, bottom_row = 0, len(matrix) - 1
    left_column, right_column = 0, len(matrix[0]) - 1

    while top_row <= bottom_row and left_column <= right_column:

        for i in range(left_column, right_column + 1):
            result.append(matrix[top_row][i])
        top_row += 1

        for i in range(top_row, bottom_row + 1):
            result.append(matrix[i][right_column])
        right_column -= 1

        if top_row <= bottom_row:
            for i in range(right_column, left_column - 1, -1):
                result.append(matrix[bottom_row][i])
            bottom_row -= 1

        if left_column <= right_column:
            for i in range(bottom_row, top_row - 1, -1):
                result.append(matrix[i][left_column])
            left_column += 1

    return result
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