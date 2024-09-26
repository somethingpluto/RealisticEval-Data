import numpy as np
import unittest


# Assume the get_scale function is defined as provided

class TestGetScaleFunction(unittest.TestCase):

    def test_identity_matrix(self):
        """ Test for the identity matrix (no scaling) """
        matrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        expected_scale = (1.0, 1.0)
        self.assertEqual(get_scale(matrix), expected_scale)

    def test_scaling_matrix(self):
        """ Test for a scaling matrix (2x in x and 3x in y) """
        matrix = np.array([[2, 0, 0],
                           [0, 3, 0],
                           [0, 0, 1]])
        expected_scale = (2.0, 3.0)
        self.assertEqual(get_scale(matrix), expected_scale)


    def test_invalid_matrix_shape(self):
        """ Test for an invalid matrix input (not 3x3) """
        invalid_matrix = np.array([[1, 2],
                                   [3, 4]])  # 2x2 matrix
        with self.assertRaises(ValueError):
            get_scale(invalid_matrix)

    def test_invalid_matrix_type(self):
        """ Test for an invalid input type (not a numpy array) """
        invalid_matrix = [[1, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1]]  # A list, not a numpy array
        with self.assertRaises(ValueError):
            get_scale(invalid_matrix)