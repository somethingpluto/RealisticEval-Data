import numpy as np

def get_rotation(matrix:np.array) -> float:
    """
    Given an affine transformation matrix, return the corresponding rotation angle in radians.

    Args:
        matrix (np.array): A 2D affine transformation matrix.

    Returns:
        float: The rotation angle in radians, extracted from the affine matrix.
    """

    angle = np.arctan2(matrix[1, 0], matrix[0, 0])
    return angle
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

if __name__ == '__main__':
    unittest.main()