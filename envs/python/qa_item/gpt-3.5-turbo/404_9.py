from typing import List

def multiply_matrix(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            row.append(sum([a[i][k] * b[k][j] for k in range(len(a[0]))]))
        result.append(row)
    return result

def power(matrix: List[List[int]], n: int) -> List[List[int]]:
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
    if n == 1:
        return matrix

    result = [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
    current_power = 1
    base = matrix

    while current_power < n:
        if current_power * 2 <= n:
            base = multiply_matrix(base, base)
            current_power *= 2
        else:
            result = multiply_matrix(result, base)
            current_power += 1

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