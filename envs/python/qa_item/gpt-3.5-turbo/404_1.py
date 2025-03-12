from typing import List

def power(matrix: List[List[int]], n: int) -> List[List[int]:
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
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    
    def multiply(A, B):
        return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*B)] for row_a in A]
    
    def identity_matrix(size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    
    def binary_exponentiation(base, exp):
        result = identity_matrix(len(base))
        while exp > 0:
            if exp % 2 == 1:
                result = multiply(result, base)
            base = multiply(base, base)
            exp //= 2
        return result
    
    return binary_exponentiation(matrix, n)
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