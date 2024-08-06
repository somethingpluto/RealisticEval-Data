import unittest


class TestMatrixMultiplication(unittest.TestCase):
    def test_standard_matrices(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected, "Should correctly multiply standard matrices")

    def test_incompatible_dimensions(self):
        mat1 = [[1, 2, 3], [4, 5, 6]]
        mat2 = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            matrix_multiply(mat1, mat2)

    def test_empty_matrices(self):
        mat1 = []
        mat2 = []
        expected = []
        self.assertEqual(matrix_multiply(mat1, mat2), expected, "Should handle empty matrices without error")

    def test_identity_matrix(self):
        mat1 = [[1, 0], [0, 1]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[5, 6], [7, 8]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "Multiplying by the identity matrix should yield the original.py matrix")
from typing import List


def matrix_multiply(matrixA: List[List[int]], matrixB: List[List[int]]) -> List[List[int]]:
    """
    Implementing matrix multiplication
    Args:
        matrixA (): matrix A
        matrixB (): matrix B

    Returns: matrixA matrixB multiplication result

    """
    if not matrixA or not matrixB or not matrixA[0] or not matrixB[0]:
        return []
    # Ensure matrix dimensions are compatible for multiplication
    if len(matrixA[0]) != len(matrixB):
        raise ValueError(
            "The number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrixB[0]))] for _ in range(len(matrixA))]

    # Perform matrix multiplication
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    return result
