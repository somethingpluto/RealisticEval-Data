from typing import List

def spiral_order(matrix: List[List[int]]) -> List[int]:
    result = []
    if not matrix:
        return result
    
    rowBegin = 0
    rowEnd = len(matrix)
    colBegin = 0
    colEnd = len(matrix[0])
    
    while rowBegin < rowEnd and colBegin < colEnd:
        # Traverse Right
        for i in range(colBegin, colEnd):
            result.append(matrix[rowBegin][i])
        rowBegin += 1
        
        # Traverse Down
        for i in range(rowBegin, rowEnd):
            result.append(matrix[i][colEnd - 1])
        colEnd -= 1
        
        if rowBegin < rowEnd:
            # Traverse Left
            for i in range(colEnd - 1, colBegin - 1, -1):
                result.append(matrix[rowEnd - 1][i])
            rowEnd -= 1
            
        if colBegin < colEnd:
            # Traverse Up
            for i in range(rowEnd - 1, rowBegin - 1, -1):
                result.append(matrix[i][colBegin])
            colBegin += 1
            
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