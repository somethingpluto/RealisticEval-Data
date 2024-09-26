import unittest


class TestMatrixVectorMultiplication(unittest.TestCase):

    def test_non_square_matrix(self):
        """Test case for a non-square matrix and a compatible vector."""
        matrix = [[1, 2], [3, 4], [5, 6]]
        vector = [2, 3]
        expected_result = [8.0, 18.0, 28.0]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_invalid_dimensions(self):
        """Test case for incompatible dimensions."""
        matrix = [[1, 2], [3, 4]]
        vector = [1, 2, 3]
        with self.assertRaises(ValueError) as context:
            matrix_vector_multiplication(matrix, vector)
        self.assertEqual(str(context.exception), "Matrix and vector dimensions are not compatible for multiplication")

    def test_zero_vector(self):
        """Test case for a matrix and a zero vector."""
        matrix = [[1, 2, 3], [4, 5, 6]]
        vector = [0, 0, 0]
        expected_result = [0.0, 0.0]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_single_element(self):
        """Test case for a single element matrix and vector."""
        matrix = [[5]]
        vector = [3]
        expected_result = [15.0]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected_result)