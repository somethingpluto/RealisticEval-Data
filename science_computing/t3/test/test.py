import unittest

from task_code.t11.adapted import multiply_matrices


class TestMultiplyMatrices(unittest.TestCase):

    def test_square_matrices(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(multiply_matrices(mat1, mat2), expected_result)

    def test_rectangular_matrices(self):
        mat1 = [[1, 2, 3], [4, 5, 6]]
        mat2 = [[7, 8], [9, 10], [11, 12]]
        expected_result = [[58, 64], [139, 154]]
        self.assertEqual(multiply_matrices(mat1, mat2), expected_result)

    def test_single_element_matrices(self):
        mat1 = [[2]]
        mat2 = [[3]]
        expected_result = [[6]]
        self.assertEqual(multiply_matrices(mat1, mat2), expected_result)

    def test_incompatible_matrices(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6, 7], [8, 9, 10]]
        with self.assertRaises(IndexError):
            multiply_matrices(mat1, mat2)
