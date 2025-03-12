from typing import List

class MatrixTraversal:
    def spiral_traversal(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        top_row, bottom_row = 0, len(matrix) - 1
        left_col, right_col = 0, len(matrix[0]) - 1
        
        while top_row <= bottom_row and left_col <= right_col:
            for i in range(left_col, right_col + 1):
                result.append(matrix[top_row][i])
            top_row += 1
            
            for i in range(top_row, bottom_row + 1):
                result.append(matrix[i][right_col])
            right_col -= 1
            
            if top_row <= bottom_row:
                for i in range(right_col, left_col - 1, -1):
                    result.append(matrix[bottom_row][i])
                bottom_row -= 1
            
            if left_col <= right_col:
                for i in range(bottom_row, top_row - 1, -1):
                    result.append(matrix[i][left_col])
                left_col += 1
        
        return result
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