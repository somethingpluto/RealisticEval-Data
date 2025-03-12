import numpy as np

def matrix_vector_multiplication(matrix: np.array, vector: np.array) -> numpy.ndarray:
    """
    Multiplies a given matrix by a vector using NumPy's dot product.

    Parameters:
    matrix (numpy.ndarray): A 2D array (matrix) of shape (m, n) where m is the number of rows
                            and n is the number of columns.
    vector (numpy.ndarray): A 1D array (vector) of shape (n,) that represents a vector
                            compatible for multiplication with the given matrix.

    Returns:
    numpy.ndarray: A 1D array (resulting vector) of shape (m,) representing the product of
                   the matrix and the vector.
    """
    return np.dot(matrix, vector)
import unittest

import numpy as np


class TestMatrixVectorMultiplication(unittest.TestCase):

    def test_case_1(self):
        # Test with a simple 2x2 matrix and a 2-element vector
        matrix = np.array([[1, 2], [3, 4]])
        vector = np.array([5, 6])
        expected_result = np.array([17, 39])  # [1*5 + 2*6, 3*5 + 4*6]
        np.testing.assert_array_equal(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_case_2(self):
        # Test with a 3x3 matrix and a 3-element vector
        matrix = np.array([[1, 0, 2], [0, 1, 2], [1, 1, 0]])
        vector = np.array([3, 4, 5])
        expected_result = np.array([13, 14, 7])  # [1*3 + 0*4 + 2*5, 0*3 + 1*4 + 2*5, 1*3 + 1*4 + 0*5]
        np.testing.assert_array_equal(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_case_3(self):
        # Test with a zero matrix and a vector
        matrix = np.array([[0, 0], [0, 0]])
        vector = np.array([1, 1])
        expected_result = np.array([0, 0])  # Zero matrix multiplied by any vector yields zero
        np.testing.assert_array_equal(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_case_4(self):
        # Test with a matrix having negative values
        matrix = np.array([[-1, -2], [-3, -4]])
        vector = np.array([1, 1])
        expected_result = np.array([-3, -7])  # [-1*1 + -2*1, -3*1 + -4*1]
        np.testing.assert_array_equal(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_case_5(self):
        # Test with non-square matrix (2x3) and a compatible vector (3-element)
        matrix = np.array([[1, 2, 3], [4, 5, 6]])
        vector = np.array([1, 0, 1])
        expected_result = np.array([4, 10])  # [1*1 + 2*0 + 3*1, 4*1 + 5*0 + 6*1]
        np.testing.assert_array_equal(matrix_vector_multiplication(matrix, vector), expected_result)
if __name__ == '__main__':
    unittest.main()