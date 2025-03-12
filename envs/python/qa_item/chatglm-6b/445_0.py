
import numpy as np

def create_rot_matrix(angle_deg: float, axis: str) -> np.ndarray:
    """
    Create a pose matrix representing a rotation about a given axis.

    Args:
        angle_deg (float): Rotation angle in degrees.
        axis (str): Axis to rotate about, must be one of 'X', 'Y', or 'Z'.

    Returns:
        np.ndarray: 4x4 pose matrix representing the rotation.
    """
    # Convert angle_deg to radians
    angle_deg = np.rad2deg(angle_deg)

    # Convert axis to a string
    axis = axis.lower() if axis.isdigit() else axis

    # Create a rotation matrix
    R = np.array([[np.cos(angle_deg) * np.cos(axis) - np.sin(angle_deg) * np.sin(axis),
                   np.cos(angle_deg) * np.sin(axis) + np.sin(angle_deg) * np.cos(axis),
                   np.sin(angle_deg) * np.cos(axis) - np.cos(angle_deg) * np.sin(axis),
                   np.sin(angle_deg) * np.sin(axis) + np.cos(angle_deg) * np.cos(axis)]])

    # Rotate the matrix 90 degrees clockwise
    R = np.rot90(R, 90)

    # Return the rotation matrix
    return R

import unittest
import numpy as np
from numpy.testing import assert_array_almost_equal



class TestCreateRotMatrix(unittest.TestCase):
    def test_rotation_x_90_degrees(self):
        """ Test rotation around X-axis for 90 degrees """
        expected_matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ])
        result_matrix = create_rot_matrix(90, 'x')
        assert_array_almost_equal(result_matrix, expected_matrix)

    def test_rotation_y_180_degrees(self):
        """ Test rotation around Y-axis for 180 degrees """
        expected_matrix = np.array([
            [-1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1]
        ])
        result_matrix = create_rot_matrix(180, 'y')
        assert_array_almost_equal(result_matrix, expected_matrix)

    def test_rotation_z_270_degrees(self):
        """ Test rotation around Z-axis for 270 degrees (or -90 degrees) """
        expected_matrix = np.array([
            [0, 1, 0, 0],
            [-1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        result_matrix = create_rot_matrix(270, 'z')
        assert_array_almost_equal(result_matrix, expected_matrix)

    def test_invalid_axis(self):
        """ Test behavior with invalid axis input """
        with self.assertRaises(ValueError):
            create_rot_matrix(90, 'a')

    def test_zero_rotation(self):
        """ Test zero degree rotation which should lead to identity matrix """
        expected_matrix = np.eye(4)
        result_matrix = create_rot_matrix(0, 'x')
        assert_array_almost_equal(result_matrix, expected_matrix)
if __name__ == '__main__':
    unittest.main()