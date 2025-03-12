import numpy as np

def apply_shear_x(matrix: np.array, shear_factor: float):
    rows, cols = matrix.shape
    new_matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            new_j = int(j + shear_factor * i)
            if 0 <= new_j < cols:
                new_matrix[i, new_j] = matrix[i, j]
    return new_matrix
import numpy as np
import unittest

class TestShearTransformation(unittest.TestCase):
    def test_identity_shear(self):
        """ Test with zero shear factor which should return the original matrix unchanged. """
        matrix = np.array([[1, 2], [3, 4]])
        shear_factor = 0
        expected_output = np.array([[1, 2], [3, 4]])
        result = apply_shear_x(matrix, shear_factor)
        np.testing.assert_array_equal(result, expected_output, "The matrix should remain unchanged with zero shear factor.")

    def test_positive_shear(self):
        """ Test with a positive shear factor. """
        matrix = np.array([[1, 2], [3, 4]])
        shear_factor = 1
        expected_output = np.array([[1, 3], [3, 7]])
        result = apply_shear_x(matrix, shear_factor)
        np.testing.assert_array_equal(result, expected_output, "The matrix should be correctly sheared.")

    def test_negative_shear(self):
        """ Test with a negative shear factor. """
        matrix = np.array([[1, 2], [3, 4]])
        shear_factor = -1
        expected_output = np.array([[1, 1], [3, 1]])
        result = apply_shear_x(matrix, shear_factor)
        np.testing.assert_array_equal(result, expected_output, "The matrix should be correctly sheared negatively.")


    def test_high_shear_factor(self):
        """ Test with a high shear factor to see how the matrix adapts to extreme transformations. """
        matrix = np.array([[1, 1], [1, 1]])
        shear_factor = 10
        expected_output = np.array([[1, 11], [1, 11]])
        result = apply_shear_x(matrix, shear_factor)
        np.testing.assert_array_equal(result, expected_output, "The matrix should be correctly sheared with a high shear factor.")
if __name__ == '__main__':
    unittest.main()