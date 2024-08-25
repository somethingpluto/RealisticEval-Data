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