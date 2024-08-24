import unittest

class TestMatrixTraversal(unittest.TestCase):
    def setUp(self):
        self.mt = MatrixTraversal()

    def test_empty_matrix(self):
        # 异常值测试：空矩阵
        self.assertEqual(self.mt.spiral_traversal([]), [], "Should return an empty list for an empty matrix")

    def test_single_element_matrix(self):
        # 基本逻辑功能测试：单元素矩阵
        matrix = [[42]]
        self.assertEqual(self.mt.spiral_traversal(matrix), [42], "Should return the single element in the matrix")

    def test_single_row_matrix(self):
        # 边界值测试：单行矩阵
        matrix = [[1, 2, 3, 4, 5]]
        self.assertEqual(self.mt.spiral_traversal(matrix), [1, 2, 3, 4, 5], "Should return all elements in a single row")

    def test_single_column_matrix(self):
        # 边界值测试：单列矩阵
        matrix = [[1], [2], [3], [4], [5]]
        self.assertEqual(self.mt.spiral_traversal(matrix), [1, 2, 3, 4, 5], "Should return all elements in a single column")

    def test_general_case(self):
        # 基本逻辑功能测试：多行多列矩阵
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.mt.spiral_traversal(matrix), [1, 2, 3, 6, 9, 8, 7, 4, 5], "Should return elements in spiral order for a general case matrix")

from typing import List


class MatrixTraversal:
    def spiral_traversal(self, matrix: List[List[int]]) -> List[int]:
        """
        Traverse a given m x n matrix in a spiral order and return all elements as a list.

        The function starts at the top-left corner of the matrix and traverses it in a
        clockwise spiral order, moving right across the top row, down the right column,
        left across the bottom row, and up the left column, repeating this process
        until all elements are traversed.

        Args:
            matrix (List[List[int]]): A 2D list representing the matrix with m rows and n columns.

        Returns:
            List[int]: A list of integers representing the elements of the matrix
            in the order they were traversed.
        """
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        row_start, row_end = 0, m - 1
        col_start, col_end = 0, n - 1
        result = []

        while row_start <= row_end and col_start <= col_end:
            # Traverse Right along the top row
            for j in range(col_start, col_end + 1):
                result.append(matrix[row_start][j])
            row_start += 1

            # Traverse Down along the right column
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1

            # Traverse Left along the bottom row, if still within bounds
            if row_start <= row_end:
                for j in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][j])
                row_end -= 1

            # Traverse Up along the left column, if still within bounds
            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1

        return result


