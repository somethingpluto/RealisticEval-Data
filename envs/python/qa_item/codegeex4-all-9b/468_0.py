import numpy as np

def get_translation(matrix: np.ndarray) -> np.ndarray:
    """
    Given a 3x3 matrix, return the corresponding translation vector.

    Args:
        matrix (np.ndarray): A 3x3 affine transformation matrix.

    Returns:
        np.ndarray: A 2-element array containing the translation components (translation_x, translation_y).
    """
    if matrix.shape != (3, 3):
        raise ValueError("Input matrix must be a 3x3 affine transformation matrix.")
    
    translation_vector = matrix[:2, 2]
    return translation_vector
import numpy as np
import unittest


# Assume the get_translation function is defined as provided

class TestGetTranslationFunction(unittest.TestCase):

    def test_identity_matrix(self):
        """ Test for the identity matrix (no translation) """
        matrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        expected_translation = np.array([0.0, 0.0])
        np.testing.assert_array_equal(get_translation(matrix), expected_translation)

    def test_translation_matrix(self):
        """ Test for a translation matrix (5 in x, 10 in y) """
        matrix = np.array([[1, 0, 5],
                           [0, 1, 10],
                           [0, 0, 1]])
        expected_translation = np.array([5.0, 10.0])
        np.testing.assert_array_equal(get_translation(matrix), expected_translation)

    def test_negative_translation(self):
        """ Test for a translation matrix with negative values """
        matrix = np.array([[1, 0, -3],
                           [0, 1, -6],
                           [0, 0, 1]])
        expected_translation = np.array([-3.0, -6.0])
        np.testing.assert_array_equal(get_translation(matrix), expected_translation)
if __name__ == '__main__':
    unittest.main()