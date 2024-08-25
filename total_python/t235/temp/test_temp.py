import unittest

class TestCalculateBearing(unittest.TestCase):
    def test_north_bearing(self):
        # From equator directly north
        self.assertAlmostEqual(calculate_bearing(0, 0, 10, 0), 0)

    def test_east_bearing(self):
        # From prime meridian directly east
        self.assertAlmostEqual(calculate_bearing(0, 0, 0, 10), 90)

    def test_south_bearing(self):
        # From a point directly south
        self.assertAlmostEqual(calculate_bearing(10, 0, 0, 0), 180)

    def test_west_bearing(self):
        # From a point directly west
        self.assertAlmostEqual(calculate_bearing(0, 10, 0, 0), 270)

    def test_across_prime_meridian(self):
        # From a point west of the prime meridian to a point east
        self.assertAlmostEqual(calculate_bearing(0, -1, 0, 1), 90)
import math


def calculate_bearing(lat1, lon1, lat2, lon2):
    """
    Calculate the bearing from one latitude and longitude to another.

    Args:
    lat1 (float): Latitude of the starting point in decimal degrees.
    lon1 (float): Longitude of the starting point in decimal degrees.
    lat2 (float): Latitude of the ending point in decimal degrees.
    lon2 (float): Longitude of the ending point in decimal degrees.

    Returns:
    float: Bearing in degrees from the starting point to the ending point, ranging from 0 to 360.
    """
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Difference in longitude
    delta_lon_rad = lon2_rad - lon1_rad

    # Calculate the bearing components
    x = math.sin(delta_lon_rad) * math.cos(lat2_rad)
    y = math.cos(lat1_rad) * math.sin(lat2_rad) - (math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(delta_lon_rad))

    # Calculate the initial bearing in radians
    initial_bearing_rad = math.atan2(x, y)

    # Convert the initial bearing from radians to degrees
    initial_bearing_deg = math.degrees(initial_bearing_rad)

    # Normalize the bearing to 0-360 degrees
    compass_bearing = (initial_bearing_deg + 360) % 360

    return compass_bearing
