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
    roll = np.radians(roll)
    pitch = np.radians(pitch)
    yaw = np.radians(yaw)

    cos_roll = np.cos(roll)
    sin_roll = np.sin(roll)
    cos_pitch = np.cos(pitch)
    sin_pitch = np.sin(pitch)
    cos_yaw = np.cos(yaw)
    sin_yaw = np.sin(yaw)

    rotation_matrix = np.array([
        [cos_pitch * cos_yaw, cos_pitch * sin_yaw, -sin_pitch],
        [sin_roll * sin_pitch * cos_yaw - cos_roll * sin_yaw, sin_roll * sin_pitch * sin_yaw + cos_roll * cos_yaw, sin_roll * cos_pitch],
        [cos_roll * sin_pitch * cos_yaw + sin_roll * sin_yaw, cos_roll * sin_pitch * sin_yaw - sin_roll * cos_yaw, cos_roll * cos_pitch]
    ])

    return rotation_matrix
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