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
    # Convert degrees to radians
    roll_rad = np.radians(roll)
    pitch_rad = np.radians(pitch)
    yaw_rad = np.radians(yaw)
    
    # Calculate sine and cosine values
    cr = np.cos(roll_rad)
    sr = np.sin(roll_rad)
    cp = np.cos(pitch_rad)
    sp = np.sin(pitch_rad)
    cy = np.cos(yaw_rad)
    sy = np.sin(yaw_rad)
    
    # Construct the rotation matrix
    rotation_matrix = np.array([
        [cy * cp, cy * sp * sr - sy * cr, cy * sp * cr + sy * sr],
        [sy * cp, sy * sp * sr + cy * cr, sy * sp * cr - cy * sr],
        [-sp, cp * sr, cp * cr]
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