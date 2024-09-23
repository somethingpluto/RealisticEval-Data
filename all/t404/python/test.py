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