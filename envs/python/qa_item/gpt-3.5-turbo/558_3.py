import math

def degrees_to_radians(degrees: int) -> float:
    """
    Convert an angle from degrees to radians.

    Args:
        degrees (int): The angle in degrees to convert.

    Returns:
        float: The angle in radians.
    """
    return degrees * math.pi / 180.0
import math
import unittest


class TestDegreesToRadians(unittest.TestCase):
    def test_zero_degrees(self):
        """Test conversion of 0 degrees"""
        self.assertAlmostEqual(degrees_to_radians(0), 0, places=5)

    def test_ninety_degrees(self):
        """Test conversion of 90 degrees"""
        self.assertAlmostEqual(degrees_to_radians(90), math.pi / 2, places=5)

    def test_one_eighty_degrees(self):
        """Test conversion of 180 degrees"""
        self.assertAlmostEqual(degrees_to_radians(180), math.pi, places=5)

    def test_two_seventy_degrees(self):
        """Test conversion of 270 degrees"""
        self.assertAlmostEqual(degrees_to_radians(270), 3 * math.pi / 2, places=5)

    def test_three_sixty_degrees(self):
        """Test conversion of 360 degrees"""
        self.assertAlmostEqual(degrees_to_radians(360), 2 * math.pi, places=5)

    def test_negative_degrees(self):
        """Test conversion of negative degrees"""
        self.assertAlmostEqual(degrees_to_radians(-90), -math.pi / 2, places=5)

    def test_large_degrees(self):
        """Test conversion of a large angle (720 degrees)"""
        self.assertAlmostEqual(degrees_to_radians(720), 4 * math.pi, places=5)

if __name__ == '__main__':
    unittest.main()