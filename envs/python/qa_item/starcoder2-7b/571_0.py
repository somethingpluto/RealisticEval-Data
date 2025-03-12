def is_valid_coordinate(coord: str) -> bool:
    try:
        # Split the coordinate into degrees and minutes
        degrees, minutes = coord.split('.')

        # Check if the degrees and minutes are valid
        if not degrees.isdigit() or not minutes.isdigit():
            return False

        # Check if the degrees are within the valid range
        if int(degrees) < 0 or int(degrees) > 90:
            return False

        # Check if the minutes are within the valid range
        if int(minutes) < 0 or int(minutes) > 59:
            return False

        return True
    except ValueError:
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