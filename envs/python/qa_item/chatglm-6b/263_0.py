
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
        # 初始化 spiral_traversal 为空列表
         spiral_traversal = []

        # 遍历 matrix 中的每个元素
        for row in matrix:
            # 初始化 top_row 为当前 row 的下标
            top_row = row[0]
            # 初始化 right_col 为当前 row 的下标
            right_col = row[1]
            # 初始化 bottom_row 为当前 row 的下标
            bottom_row = row[2]
            # 初始化 left_col 为当前 row 的下标
            left_col = row[3]

            # 遍历 spiral_traversal 中的每个元素
             spiral_traversal.append(top_row)
             spiral_traversal.append(right_col)
             spiral_traversal.append(bottom_row)
             spiral_traversal.append(left_col)

        # 返回 spiral_traversal 列表
        return spiral_traversal

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

if __name__ == '__main__':
    unittest.main()