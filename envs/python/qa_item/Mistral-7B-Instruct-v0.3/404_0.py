from typing import List

def power(matrix: List[List[int]], n: int) -> List[List[int]]:
    if not matrix or not all(isinstance(row, list) for row in matrix) or not all(isinstance(x, int) for row in matrix for x in row):
        raise TypeError("matrix must be a list of lists and n must be an integer.")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(a[0]) for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[0])):
                for k in range(len(b[0])):
                    result[i][j] += a[i][k] * b[k][j]
        return result

    def fast_exponentiate(base: List[List[int]], exponent: int) -> List[List[int]]:
        if exponent == 0:
            return [[1] * len(base[0])]
        if exponent % 2 == 1:
            return multiply(fast_exponentiate(base, exponent - 1), base)
        half_result = fast_exponentiate(base, exponent // 2)
        return multiply(half_result, half_result)

    return fast_exponentiate(matrix, n)
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