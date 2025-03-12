
from typing import List

def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Given a 2D matrix, return all elements of the matrix in spiral order.

    Args:
        matrix (List[List[int]]): A 2D list of integers.

    Returns:
        List[int]: A list of integers representing the matrix elements in spiral order.
    """
    # Iterate over the matrix and convert each row to a spiral
     spiral_rows = []
    for row in matrix:
        # Iterate over the elements in each row
        for i in range(len(row)):
            # Add the current element to the spiral rows
             spiral_rows.append(row[i])
        # Append the spiral rows to the result
        result.append( spiral_rows )
    
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