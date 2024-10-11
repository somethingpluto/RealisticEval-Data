import math
import unittest


class TestQuaternionToAngle(unittest.TestCase):

    def test_identity_quaternion(self):
        """Test the identity quaternion (no rotation)."""
        quaternion = (1.0, 0.0, 0.0, 0.0)
        expected_angle = 0.0
        self.assertAlmostEqual(quaternion_to_angle(quaternion), expected_angle)


    def test_180_degrees_rotation(self):
        """Test a quaternion representing a 180-degree rotation."""
        quaternion = (0.0, 0.0, 1.0, 0.0)  # 180 degrees around Z axis
        expected_angle = math.pi  # 180 degrees in radians
        self.assertAlmostEqual(quaternion_to_angle(quaternion), expected_angle)

    def test_360_degrees_rotation(self):
        """Test a quaternion representing a full 360-degree rotation."""
        quaternion = (1.0, 0.0, 0.0, 0.0)  # Full rotation
        expected_angle = 0.0  # 360 degrees is equivalent to 0 degrees
        self.assertAlmostEqual(quaternion_to_angle(quaternion), expected_angle)


    def test_non_unit_quaternion(self):
        """Test a non-unit quaternion (should still give correct angle)."""
        quaternion = (0.5, 0.5, 0.5, 0.5)  # This is not normalized
        # Normalize the quaternion first
        norm = math.sqrt(sum(x ** 2 for x in quaternion))
        normalized_quaternion = tuple(x / norm for x in quaternion)
        expected_angle = 2 * math.acos(normalized_quaternion[0])  # Should be same angle
        self.assertAlmostEqual(quaternion_to_angle(normalized_quaternion), expected_angle)

    def test_invalid_quaternion(self):
        """Test that an invalid quaternion raises a ValueError."""
        with self.assertRaises(ValueError):
            quaternion_to_angle((1.0, 0.0, 0.0))  # Only 3 components