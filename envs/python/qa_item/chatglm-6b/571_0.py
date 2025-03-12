
def is_valid_coordinate(coord: str) -> bool:
    """
    Checks if the string conforms to the latitude and longitude identification specification.

    Args:
        coord: The coordinate string to check (can be latitude or longitude).

    Returns:
        A boolean indicating whether the coordinate is valid.
    """
    # Define the identification specification
    identification_ specification = {
        "latitude": "0.0",
        "longitude": "0.0",
        "accuracy": "0.0",
        "min_latitude": "-0.0",
        "min_longitude": "-0.0",
        "max_latitude": "0.0",
        "max_longitude": "0.0",
        "min_longitude_十八度": "-0.0",
        "max_longitude_十八度": "0.0",
        "min_latitude_十八度": "-0.0",
        "max_latitude_十八度": "0.0"
    }

    # Check if the string matches the identification specification
    if coord in identification_ specification:
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