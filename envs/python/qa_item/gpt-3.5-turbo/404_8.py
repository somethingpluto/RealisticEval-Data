from typing import List

def multiply_matrices(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def power(matrix: List[List[int]], n: int) -> List[List[int]]:
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    result = [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]

    while n > 0:
        if n % 2 == 1:
            result = multiply_matrices(result, matrix)
        matrix = multiply_matrices(matrix, matrix)
        n //= 2

    return result
import unittest

class TestMatrixPower(unittest.TestCase):

    def test_identity_matrix(self):
        # Testing the power function with an identity matrix
        matrix = [[1, 0], [0, 1]]
        expected = [[1, 0], [0, 1]]
        result = power(matrix, 1)
        self.assertEqual(result, expected)

    def test_zero_power(self):
        # Testing matrix to the power of zero (should return identity)
        matrix = [[2, 3], [1, 4]]
        expected = [[1, 0], [0, 1]]
        result = power(matrix, 0)
        self.assertEqual(result, expected)

    def test_positive_power(self):
        # Testing matrix to a positive power
        matrix = [[2, 1], [1, 3]]
        expected = [[5, 5], [5, 10]]  # This is the result of matrix^2
        result = power(matrix, 2)
        self.assertEqual(result, expected)

    def test_negative_power(self):
        # Testing matrix to a negative power (should raise ValueError)
        matrix = [[2, 1], [1, 3]]
        with self.assertRaises(ValueError):
            power(matrix, -1)
if __name__ == '__main__':
    unittest.main()