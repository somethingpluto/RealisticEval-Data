import numpy as np
import unittest


class TestGetRotationFunction(unittest.TestCase):

    def test_rotation_0_degrees(self):
        """ Test for a rotation of 0 degrees (identity matrix) """
        matrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        expected_rotation = 0.0
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

    def test_rotation_90_degrees(self):
        """ Test for a rotation of 90 degrees """
        matrix = np.array([[0, -1, 0],
                           [1, 0, 0],
                           [0, 0, 1]])
        expected_rotation = np.pi / 2  # 90 degrees in radians
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

    def test_rotation_180_degrees(self):
        """ Test for a rotation of 180 degrees """
        matrix = np.array([[-1, 0, 0],
                           [0, -1, 0],
                           [0, 0, 1]])
        expected_rotation = np.pi  # 180 degrees in radians
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

    def test_rotation_negative_90_degrees(self):
        """ Test for a rotation of -90 degrees """
        matrix = np.array([[0, 1, 0],
                           [-1, 0, 0],
                           [0, 0, 1]])
        expected_rotation = -np.pi / 2  # -90 degrees in radians
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

    def test_rotation_invalid_matrix(self):
        """ Test for an invalid matrix input """
        invalid_matrix = np.array([[1, 0], [0, 1]])  # Not a 3x3 matrix
        with self.assertRaises(ValueError):
            get_rotation(invalid_matrix)