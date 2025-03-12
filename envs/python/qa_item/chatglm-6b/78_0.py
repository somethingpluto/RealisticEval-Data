
import numpy as np

def euler_to_rotation_matrix(roll: float, pitch: float, yaw: float) -> np.array:
    """
    Convert Euler angles (roll, pitch, yaw) to a rotation matrix.

    Args:
        roll (float): Rotation around the x-axis in degrees.
        pitch (float): Rotation around the y-axis in degrees.
        yaw (float): Rotation around the z-axis in degrees.

    Returns:
        np.array: A 3x3 rotation matrix.
    """
    # Convert Euler angles to rotation matrix
    matrix = np.array([[np.cos(yaw), np.sin(yaw), 0],
                      [np.sin(yaw), np.cos(yaw), 0],
                      [0, 0, 1]])
    
    # Rotate matrix around x-axis
    x_axis = np.cos(roll)
    y_axis = np.sin(roll)
    z_axis = 0
    matrix_x_axis = matrix[0, :, :] * x_axis + matrix[1, :, :] * y_axis + matrix[2, :, :] * z_axis
    matrix_y_axis = matrix[0, :, :] * y_axis + matrix[1, :, :] * x_axis + matrix[2, :, :] * z_axis
    matrix_z_axis = matrix[0, :, :] * z_axis + matrix[1, :, :] * y_axis + matrix[2, :, :] * x_axis
    
    # Rotate matrix around y-axis
    y_axis = np.sin(pitch)
    x_axis = np.cos(pitch)
    z_axis = 0
    matrix_y_axis_pitch = matrix[0, :, :] * y_axis + matrix[1, :, :] * x_axis + matrix[2, :, :] * z_axis
    matrix_y_axis_pitch = matrix_y_axis_pitch * np.cos(pitch) - matrix_y_axis_pitch * np.sin(pitch)
    matrix_y_axis_pitch = matrix_y_axis_pitch * np.sin(pitch) + matrix_y_axis_pitch * np.cos(pitch)
    
    # Rotate matrix around z-axis
    z_axis = np.cos(yaw)
    x_axis = np.sin(yaw)
    y_axis = 0
    matrix_z_axis_yaw = matrix[0, :, :] * z_axis + matrix[1, :, :] * x_axis + matrix[2, :, :] * y_axis
    matrix_z_axis_yaw = matrix_z_axis_yaw * np.cos(yaw) - matrix_z_axis_yaw * np.sin(yaw)
    matrix_z_axis_yaw = matrix_z_axis_yaw * np.sin(yaw) + matrix_z_axis_yaw * np.cos(yaw)
    
    return matrix_x_axis, matrix_y_axis, matrix_z_axis_yaw

import unittest
import numpy as np

class TestEulerToRotationMatrix(unittest.TestCase):
    def test_zero_rotation(self):
        # Test with zero rotation for all axes
        R = euler_to_rotation_matrix(0, 0, 0)
        np.testing.assert_array_almost_equal(R, np.identity(3))

    def test_rotation_about_x(self):
        # Test rotation about the x-axis
        R = euler_to_rotation_matrix(90, 0, 0)
        expected = np.array([
            [1, 0, 0],
            [0, 0, -1],
            [0, 1, 0]
        ])
        np.testing.assert_array_almost_equal(R, expected)

    def test_rotation_about_y(self):
        # Test rotation about the y-axis
        R = euler_to_rotation_matrix(0, 90, 0)
        expected = np.array([
            [0, 0, 1],
            [0, 1, 0],
            [-1, 0, 0]
        ])
        np.testing.assert_array_almost_equal(R, expected)

    def test_rotation_about_z(self):
        # Test rotation about the z-axis
        R = euler_to_rotation_matrix(0, 0, 90)
        expected = np.array([
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])
        np.testing.assert_array_almost_equal(R, expected)

    def test_combined_rotation(self):
        # Test combined rotation
        R = euler_to_rotation_matrix(30, 45, 60)
        # Expected model_answer_result manually calculated or verified via a reliable source
        expected = np.array([[ 0.35355339, -0.5732233,   0.73919892], [ 0.61237244 , 0.73919892,  0.28033009], [-0.70710678 , 0.35355339,  0.61237244]])
        np.testing.assert_array_almost_equal(R, np.array(expected), decimal=5)
if __name__ == '__main__':
    unittest.main()