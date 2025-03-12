import re

def is_valid_coordinate(coord: str) -> bool:
    if not coord or len(coord) > 11:
        return False

    if re.match(r'^[-]?(([0-8]?[0-9])\.(\d{6})|90(\.0{1,6})|([0-8]?[0-9])\.(\d{5})|89(\.0{1,5})|([0-7]?[0-9])\.(\d{4})|79(\.0{1,4})|([0-6]?[0-9])\.(\d{3})|69(\.0{1,3})|([0-5]?[0-9])\.(\d{2})|59(\.0{1,2})|([0-9])\.(\d{1})|90|-90|[0-9]{1,2})$', coord) is None:
        return False

    return True
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