import math
import unittest

from task_code.t12.adapted import haversine


class TestHaversine(unittest.TestCase):
    EARTH_RADIUS_FEET = 20_902_766

    def test_zero_distance(self):
        lat, lon = 40.748817, -73.985428  # Coordinates of the Empire State Building
        self.assertAlmostEqual(haversine(lat, lon, lat, lon), 0, places=5)

    def test_known_distance(self):
        # Coordinates of the Empire State Building and Statue of Liberty
        lat1, lon1 = 40.748817, -73.985428  # Empire State Building
        lat2, lon2 = 40.689247, -74.044502  # Statue of Liberty
        # Expected distance in feet, roughly calculated using an external tool
        expected_distance = 364578.98
        self.assertAlmostEqual(haversine(lat1, lon1, lat2, lon2), expected_distance, delta=1000)

    def test_polar_distance(self):
        # North Pole and South Pole coordinates
        lat1, lon1 = 90.0, 0.0  # North Pole
        lat2, lon2 = -90.0, 0.0  # South Pole
        # Half the circumference of the Earth in feet
        expected_distance = 20_902_766 * math.pi
        self.assertAlmostEqual(haversine(lat1, lon1, lat2, lon2), expected_distance, places=5)
