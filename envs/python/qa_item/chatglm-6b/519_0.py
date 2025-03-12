
from typing import List

def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Transpose a given matrix (2D array).

    Args:
        matrix (List[List[int]]): The input 2D array to be transposed.

    Returns:
        List[List[int]]: The transposed 2D array.
    """
    # Iterate over the matrix and transpose each row
    for row in matrix:
        # Iterate over the list of rows
        for i in range(len(row)):
            # transpose the current row
            row[i] = row[i].transpose()

    return matrix

import unittest


class TestTransposeMatrix(unittest.TestCase):

    def test_square_matrix(self):
        """Test transposing a square matrix."""
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        result = transpose_matrix(matrix)
        self.assertEqual(result, expected)

    def test_rectangular_matrix(self):
        """Test transposing a rectangular matrix."""
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        result = transpose_matrix(matrix)
        self.assertEqual(result, expected)


    def test_matrix_with_empty_rows(self):
        """Test transposing a matrix with an empty row."""
        matrix = [[], []]
        expected = []
        result = transpose_matrix(matrix)
        self.assertEqual(result, expected)

    def test_single_element_matrix(self):
        """Test transposing a matrix with a single element."""
        matrix = [[5]]
        expected = [[5]]
        result = transpose_matrix(matrix)
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()