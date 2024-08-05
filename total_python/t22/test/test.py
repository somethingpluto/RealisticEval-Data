import unittest


class TestEuclideanDistance(unittest.TestCase):
    def test_regular_distance(self):
        self.assertAlmostEqual(calculate_euclidean_distance((1, 2), (4, 6)), 5.0)

    def test_zero_distance(self):
        self.assertEqual(calculate_euclidean_distance((3, 3), (3, 3)), 0)

    def test_negative_coordinates(self):
        self.assertAlmostEqual(calculate_euclidean_distance((-1, -1), (1, 1)), 2.8284271247461903)
