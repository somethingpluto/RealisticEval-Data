import re

def is_valid_coordinate(coord: str) -> bool:
    """
    Checks if the string conforms to the latitude and longitude identification specification.

    Args:
        coord: The coordinate string to check (can be latitude or longitude).

    Returns:
        A boolean indicating whether the coordinate is valid.
    """
    pattern = r'^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?((1[0-7]\d(\.\d+)?)|([1-9]?\d(\.\d+)?)|180(\.0+)?)$'
    
    if re.match(pattern, coord):
        return True
    else:
        return False
import unittest


class TestIsValidCoordinate(unittest.TestCase):

    def test_valid_latitude_with_direction(self):
        coord = "45.123N"
        self.assertTrue(is_valid_coordinate(coord))

    def test_valid_latitude_without_direction(self):
        coord = "90.0"
        self.assertTrue(is_valid_coordinate(coord))

    def test_valid_longitude_with_direction(self):
        coord = "180.0E"
        self.assertTrue(is_valid_coordinate(coord))

    def test_valid_longitude_without_direction(self):
        coord = "-120.456"
        self.assertTrue(is_valid_coordinate(coord))

    def test_invalid_longitude_exceeding_range(self):
        coord = "-200.5"
        self.assertFalse(is_valid_coordinate(coord))
if __name__ == '__main__':
    unittest.main()