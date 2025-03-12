import math

def calculate_bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    calculate the azimuth between two points on the earth. This function accepts the latitude and longitude of the two points as a parameter and returns the azimuth from the first point to the second point in degrees
    Args:
        lat1 (float): Latitude of the starting point in decimal degrees.
        lon1 (float): Longitude of the starting point in decimal degrees.
        lat2 (float): Latitude of the ending point in decimal degrees.
        lon2 (float): Longitude of the ending point in decimal degrees.

    Returns:
        float: Bearing in degrees from the starting point to the ending point, ranging from 0 to 360.
    """
    
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    delta_lon = lon2 - lon1
    
    y = math.sin(delta_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    
    bearing = math.atan2(y, x)
    
    bearing = math.degrees(bearing)
    bearing = (bearing + 360) % 360
    
    return bearing
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
if __name__ == '__main__':
    unittest.main()