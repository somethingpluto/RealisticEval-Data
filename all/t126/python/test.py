import unittest


class TestCalculateDistance(unittest.TestCase):

    def test_calculate_distance_same_city(self):
        # Coordinates for two points in Los Angeles
        distance = calculate_distance(34.052235, -118.243683, 34.052236, -118.243684)
        self.assertAlmostEqual(distance, 0.00013, places=4)  # The distance should be very small

    def test_calculate_distance_major_cities(self):
        # Coordinates for Los Angeles and New York
        distance = calculate_distance(34.052235, -118.243683, 40.712776, -74.005974)
        expected_distance = 3940  # Known distance is approximately 3940 kilometers
        tolerance = 30  # Tolerance of 30 kilometers
        self.assertGreater(distance, expected_distance - tolerance)
        self.assertLess(distance, expected_distance + tolerance)

    def test_calculate_distance_different_continents(self):
        # Coordinates for New York in the USA and London in the UK
        distance = calculate_distance(40.712776, -74.005974, 51.507351, -0.127758)
        expected_distance = 5567  # Known distance is approximately 5567 kilometers
        tolerance = 30  # Tolerance of 30 kilometers
        self.assertGreater(distance, expected_distance - tolerance)
        self.assertLess(distance, expected_distance + tolerance)

    def test_calculate_distance_zero_distance(self):
        # Same coordinates for a location in Paris
        distance = calculate_distance(48.8566, 2.3522, 48.8566, 2.3522)
        self.assertEqual(distance, 0)  # Distance should be zero

    def test_calculate_distance_negative_positive_coordinates(self):
        # Coordinates for Sydney and Auckland
        distance = calculate_distance(-33.8688, 151.2093, -36.8485, 174.7633)
        expected_distance = 2159  # Known distance is approximately 2159 kilometers
        tolerance = 30  # Tolerance of 30 kilometers
        self.assertGreater(distance, expected_distance - tolerance)
        self.assertLess(distance, expected_distance + tolerance)

