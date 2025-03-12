from typing import List

def power(matrix: List[List[int]], n: int) -> List[List[int]]:
    """
    Computes the n-th power of a matrix using the fast exponentiation method.

    Args:
        matrix (List[List[int]]): A square matrix to be exponentiated.
        n (int): The exponent to raise the matrix to. Must be a non-negative integer.

    Returns:
        List[List[int]]: The matrix raised to the power of n.

    Raises:
        ValueError: If n is negative.
        TypeError: If matrix is not a list of lists or n is not an integer.
    """
    if not isinstance(matrix, List) or not all(isinstance(row, List) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(b[0]) for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        return result

    def fast_exponentiation(matrix: List[List[int]], n: int) -> List[List[int]]:
        if n == 0:
            return [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
        if n == 1:
            return matrix
        half_power = fast_exponentiation(matrix, n // 2)
        if n % 2 == 0:
            return multiply(half_power, half_power)
        else:
            return multiply(multiply(half_power, half_power), matrix)

    return fast_exponentiation(matrix, n)
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