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

    def test_invalid_matrix_shape(self):
        """ Test for an invalid matrix input (not 3x3) """
        invalid_matrix = np.array([[1, 2],
                                   [3, 4]])  # 2x2 matrix
        with self.assertRaises(ValueError):
            get_translation(invalid_matrix)

    def test_invalid_matrix_type(self):
        """ Test for an invalid input type (not a numpy array) """
        invalid_matrix = [[1, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1]]  # A list, not a numpy array
        with self.assertRaises(ValueError):
            get_translation(invalid_matrix)
