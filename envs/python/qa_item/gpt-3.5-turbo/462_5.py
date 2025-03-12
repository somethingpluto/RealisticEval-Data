from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
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