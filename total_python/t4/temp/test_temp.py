import unittest
import math


class TestQuaternionToYaw(unittest.TestCase):
    def test_zero_rotation(self):
        # Quaternion for no rotation
        w, x, y, z = 1, 0, 0, 0
        expected_yaw = 0
        result = quaternion_to_yaw(w, x, y, z)
        self.assertAlmostEqual(result, expected_yaw, msg="Failed zero rotation test")

    def test_90_degrees_rotation(self):
        # Quaternion for 90 degrees rotation around z-axis
        w, x, y, z = math.cos(math.pi / 4), 0, 0, math.sin(math.pi / 4)
        expected_yaw = math.pi / 2
        result = quaternion_to_yaw(w, x, y, z)
        self.assertAlmostEqual(result, expected_yaw, msg="Failed 90 degrees rotation test")

    def test_180_degrees_rotation(self):
        # Quaternion for 180 degrees rotation around z-axis
        w, x, y, z = 0, 0, 0, 1
        expected_yaw = math.pi
        result = quaternion_to_yaw(w, x, y, z)
        self.assertAlmostEqual(result, expected_yaw, msg="Failed 180 degrees rotation test")

    def test_270_degrees_rotation(self):
        # Quaternion for 270 degrees (or -90 degrees) rotation around z-axis
        w, x, y, z = math.cos(-math.pi / 4), 0, 0, math.sin(-math.pi / 4)
        expected_yaw = -math.pi / 2
        result = quaternion_to_yaw(w, x, y, z)
        self.assertAlmostEqual(result, expected_yaw, msg="Failed 270 degrees rotation test")

    def test_negative_rotation(self):
        # Quaternion for negative rotation around z-axis
        w, x, y, z = math.cos(-math.pi / 6), 0, 0, math.sin(-math.pi / 6)
        expected_yaw = -math.pi / 3
        result = quaternion_to_yaw(w, x, y, z)
        self.assertAlmostEqual(result, expected_yaw, msg="Failed negative rotation test")

import math


def quaternion_to_yaw(w, x, y, z):
    """
    Convert a quaternion to a yaw angle around the z-axis.

    Parameters:
        w (float): The scalar component of the quaternion.
        x (float): The x-component of the quaternion vector part.
        y (float): The y-component of the quaternion vector part.
        z (float): The z-component of the quaternion vector part.

    Returns:
        float: The yaw angle in radians.
    """
    # Calculate the yaw (psi) using the atan2 function
    psi = math.atan2(2 * (w * z + x * y), 1 - 2 * (y ** 2 + z ** 2))
    return psi