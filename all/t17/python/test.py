import unittest


class TestHaversineDistance(unittest.TestCase):

    def test_same_point(self):
        # Same point should return a distance of 0
        lat, lon = 52.2296756, 21.0122287
        result = haversine_distance(lat, lon, lat, lon)
        self.assertAlmostEqual(result, 0.0, places=6)

    def test_small_distance(self):
        # Points that are very close together (few meters apart)
        lat1, lon1 = 52.2296756, 21.0122287  # Warsaw, Poland
        lat2, lon2 = 52.2296756, 21.0122297  # Very close to the previous point
        result = haversine_distance(lat1, lon1, lat2, lon2)
        self.assertAlmostEqual(result, 0.0001, places=4)  # Expected small distance

    def test_large_distance(self):
        # Points that are far apart
        lat1, lon1 = 52.2296756, 21.0122287  # Warsaw, Poland
        lat2, lon2 = 41.8919300, 12.5113300  # Rome, Italy
        result = haversine_distance(lat1, lon1, lat2, lon2)
        self.assertAlmostEqual(result, 1315.514, places=2)  # Approx distance in km

    def test_equator_distance(self):
        # Points on the equator
        lat1, lon1 = 0.0, 0.0  # Gulf of Guinea (Equator and Prime Meridian intersection)
        lat2, lon2 = 0.0, 90.0  # On the Equator, 90 degrees east
        result = haversine_distance(lat1, lon1, lat2, lon2)
        self.assertAlmostEqual(result, 10007.54, places=2)  # Approx quarter of Earth's circumference

    def test_pole_to_pole(self):
        # Distance from North Pole to South Pole
        lat1, lon1 = 90.0, 0.0  # North Pole
        lat2, lon2 = -90.0, 0.0  # South Pole
        result = haversine_distance(lat1, lon1, lat2, lon2)
        self.assertAlmostEqual(result, 20015.09, places=2)  # Approx half of Earth's circumference
