from typing import List

def matrix_multiply(matrixA: List[List[int]], matrixB: List[List[int]]) -> List[List[int]]:
    """
    Implementing matrix multiplication

    Args:
        matrixA (List[List[int]]): matrix A
        matrixB (List[List[int]]): matrix B

    Returns:
        List[List[int]]: matrixA matrixB multiplication result
    """
    rows_A = len(matrixA)
    cols_A = len(matrixA[0])
    cols_B = len(matrixB[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    return result
import unittest


class TestMatrixMultiplication(unittest.TestCase):
    def test_standard_matrices(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected, "Should correctly multiply standard matrices")

    def test_identity_matrix(self):
        mat1 = [[1, 0], [0, 1]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[5, 6], [7, 8]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "Multiplying by the identity matrix should yield the answer.py matrix")

    def test_zero_matrix(self):
        mat1 = [[0, 0], [0, 0]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[0, 0], [0, 0]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "Multiplying by the zero matrix should yield a zero matrix")

    def test_square_matrix_multiplication(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "The multiplication of two square matrices should yield the correct product")

    def test_large_identity_matrix(self):
        mat1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        mat2 = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
        expected = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "Multiplying by the larger identity matrix should yield the answer matrix")

if __name__ == '__main__':
    unittest.main()