from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    calculate the distance between two points on the earth based on their latitude and longitude
    Args:
        lat1 (float): Latitude of the first point in degrees.
        lon1 (float): Longitude of the first point in degrees.
        lat2 (float): Latitude of the second point in degrees.
        lon2 (float): Longitude of the second point in degrees.

    Returns:
        Distance between the two points in kilometers.
    """
    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6371 * c  # Radius of Earth in kilometers

    return distance
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

if __name__ == '__main__':
    unittest.main()