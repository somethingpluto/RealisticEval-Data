import math

def radians_to_degrees(radians: float) -> int:
    """
    Convert an angle from radians to degrees.

    Args:
        radians (float): The angle in radians to convert.

    Returns:
        int: The angle in degrees.
    """
    return int(math.degrees(radians))
import math
import unittest


class TestRadiansToDegrees(unittest.TestCase):
    def test_zero_radians(self):
        """Test conversion of 0 radians"""
        self.assertAlmostEqual(radians_to_degrees(0), 0, places=5)

    def test_pi_over_two_radians(self):
        """Test conversion of π/2 radians"""
        self.assertAlmostEqual(radians_to_degrees(math.pi / 2), 90, places=5)

    def test_pi_radians(self):
        """Test conversion of π radians"""
        self.assertAlmostEqual(radians_to_degrees(math.pi), 180, places=5)

    def test_three_pi_over_two_radians(self):
        """Test conversion of 3π/2 radians"""
        self.assertAlmostEqual(radians_to_degrees(3 * math.pi / 2), 270, places=5)

    def test_two_pi_radians(self):
        """Test conversion of 2π radians"""
        self.assertAlmostEqual(radians_to_degrees(2 * math.pi), 360, places=5)

    def test_negative_pi_over_two_radians(self):
        """Test conversion of -π/2 radians"""
        self.assertAlmostEqual(radians_to_degrees(-math.pi / 2), -90, places=5)

    def test_large_radians(self):
        """Test conversion of a large angle (4π radians)"""
        self.assertAlmostEqual(radians_to_degrees(4 * math.pi), 720, places=5)
if __name__ == '__main__':
    unittest.main()