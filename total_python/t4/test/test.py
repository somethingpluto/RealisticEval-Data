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
