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
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    if not all(isinstance(val, int) for row in matrix for val in row):
        raise TypeError("matrix must contain only integers")
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    
    def multiply_matrix(a, b):
        rows_a = len(a)
        cols_a = len(a[0])
        rows_b = len(b)
        cols_b = len(b[0])
        
        if cols_a != rows_b:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        
        result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += a[i][k] * b[k][j]
        
        return result
    
    def power_matrix(matrix, power):
        if power == 0:
            return [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
        if power % 2 == 1:
            return multiply_matrix(matrix, power_matrix(matrix, power - 1))
        half_power = power_matrix(matrix, power // 2)
        return multiply_matrix(half_power, half_power)
    
    return power_matrix(matrix, n)
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