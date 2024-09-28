import unittest


class TestMatrixMultiplication(unittest.TestCase):
    def test_standard_matrices(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected, "Should correctly multiply standard matrices")

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
                         "Multiplying by the identity matrix should yield the answer.py matrix")
