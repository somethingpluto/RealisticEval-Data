from typing import List

def spiral_order(matrix: List[List[int]]) -> List[int]:
    result = []
    if not matrix:
        return result
    
    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1
    
    while row_begin <= row_end and col_begin <= col_end:
        # Traverse Right
        for i in range(col_begin, col_end + 1):
            result.append(matrix[row_begin][i])
        row_begin += 1
        
        # Traverse Down
        for i in range(row_begin, row_end + 1):
            result.append(matrix[i][col_end])
        col_end -= 1
        
        if row_begin <= row_end:
            # Traverse Left
            for i in range(col_end, col_begin - 1, -1):
                result.append(matrix[row_end][i])
            row_end -= 1
        
        if col_begin <= col_end:
            # Traverse Up
            for i in range(row_end, row_begin - 1, -1):
                result.append(matrix[i][col_begin])
            col_begin += 1
    
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