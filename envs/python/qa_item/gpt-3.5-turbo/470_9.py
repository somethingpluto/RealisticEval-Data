import numpy as np

def apply_shear_x(matrix: np.array, shear_factor: float):
    """
    Applies a shear transformation to a 2D matrix along the x-axis.

    Args:
    matrix (np.ndarray): A 2D numpy array representing the original matrix.
    shear_factor (float): The factor by which the matrix is sheared along the x-axis.

    Returns:
    np.ndarray: The sheared matrix.
    """
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