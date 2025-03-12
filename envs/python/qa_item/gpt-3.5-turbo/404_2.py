from typing import List

def power(matrix: List[List[int]], n: int) -> List[List[int]:
    def multiply(a, b):
        rows_a, cols_a = len(a), len(a[0])
        rows_b, cols_b = len(b), len(b[0])
        
        if cols_a != rows_b:
            raise ValueError("Number of columns in A must be equal to number of rows in B")
        
        result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += a[i][k] * b[k][j]
        
        return result
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not isinstance(n, int):
        raise TypeError("Matrix must be a list of lists and n must be an integer")
    
    if n < 0:
        raise ValueError("Exponent n must be non-negative")
    
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")
    
    result = [[int(i == j) for j in range(len(matrix))] for i in range(len(matrix))]
    base = matrix
    
    while n > 0:
        if n % 2 == 1:
            result = multiply(result, base)
        base = multiply(base, base)
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