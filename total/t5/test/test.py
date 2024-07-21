import unittest

from total.t5.adapted import multiply_matrices


class TestMatrixMultiplication(unittest.TestCase):
    def test_standard_matrices(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(multiply_matrices(mat1, mat2), expected, "Should correctly multiply standard matrices")

    def test_incompatible_dimensions(self):
        mat1 = [[1, 2, 3], [4, 5, 6]]
        mat2 = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            multiply_matrices(mat1, mat2)

    def test_empty_matrices(self):
        mat1 = []
        mat2 = []
        expected = []
        self.assertEqual(multiply_matrices(mat1, mat2), expected, "Should handle empty matrices without error")

    def test_identity_matrix(self):
        mat1 = [[1, 0], [0, 1]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[5, 6], [7, 8]]
        self.assertEqual(multiply_matrices(mat1, mat2), expected, "Multiplying by the identity matrix should yield the original.py matrix")