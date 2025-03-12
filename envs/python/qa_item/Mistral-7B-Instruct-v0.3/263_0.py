from typing import List

class MatrixTraversal:
    def spiral_traversal(self, matrix: List[List[int]]) -> List[int]:
        direction = 0
        m, n = len(matrix), len(matrix[0])
        traversed = []
        i, j = 0, 0

        while len(traversed) < m * n:
            traversed.append(matrix[i][j])
            next_i, next_j = i, j

            if direction == 0:
                if j + 1 == n:
                    i += 1
                    direction = 1
                else:
                    j += 1
            elif direction == 1:
                if i + 1 == m:
                    j -= 1
                    direction = 2
                elif matrix[i + 1][j]!= None:
                    i += 1
                else:
                    i += 1
                    direction = 3
            elif direction == 2:
                if j - 1 < 0:
                    i -= 1
                    direction = 3
                elif matrix[i][j - 1]!= None:
                    j -= 1
                else:
                    j -= 1
                    direction = 0
            elif direction == 3:
                if i - 1 < 0:
                    j += 1
                    direction = 0
                elif matrix[i - 1][j]!= None:
                    i -= 1
                else:
                    i -= 1
                    direction = 1

            i, j = next_i, next_j

        return traversed
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