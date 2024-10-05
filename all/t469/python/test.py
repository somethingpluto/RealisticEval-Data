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


    def test_uniform_scaling(self):
        # Test case with uniform scaling
        matrix = np.array([[2, 0, 0],
                           [0, 2, 0],
                           [0, 0, 1]])
        expected = (2.0, 2.0)
        self.assertEqual(get_scale(matrix), expected)

    def test_non_uniform_scaling(self):
        # Test case with non-uniform scaling
        matrix = np.array([[3, 0, 0],
                           [0, 5, 0],
                           [0, 0, 1]])
        expected = (3.0, 5.0)
        self.assertEqual(get_scale(matrix), expected)

    def test_reflection_matrix(self):
        # Test case with reflection matrix
        matrix = np.array([[-1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        expected = (1.0, 1.0)
        self.assertEqual(get_scale(matrix), expected)