import unittest


class TestProbabilityAtLeastNRedBalls(unittest.TestCase):

    def test_basic_functionality(self):
        result = probability_at_least_n_red_balls(5, 10, 20)
        expected = 0.2025  # This is a precomputed value assuming the function is correct
        self.assertAlmostEqual(result, expected, places=4)

    def test_all_red_balls(self):
        result = probability_at_least_n_red_balls(10, 15, 0)
        expected = 1.0  # Since all balls are red, it's certain to draw 10 red balls
        self.assertEqual(result, expected)

    def test_no_red_balls(self):
        result = probability_at_least_n_red_balls(1, 0, 30)
        expected = 0.0  # No red balls, so it's impossible to draw any
        self.assertEqual(result, expected)

    def test_edge_case_for_minimum_n(self):
        result = probability_at_least_n_red_balls(15, 15, 20)
        expected = 0.0187  # Precomputed value for this scenario
        self.assertAlmostEqual(result, expected, places=4)

    def test_impossible_case(self):
        result = probability_at_least_n_red_balls(16, 10, 5)
        expected = 0.0  # It's impossible to draw 16 balls when only 15 draws are allowed
        self.assertEqual(result, expected)