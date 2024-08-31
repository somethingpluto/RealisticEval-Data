import unittest

class TestHypergeometricProbability(unittest.TestCase):
    def test_typical_case(self):
        # Test with typical values
        x, y, n = 10, 20, 5
        result = hypergeometric_probability(x, y, n)
        self.assertAlmostEqual(result, 0.202381, places=6)

    def test_impossible_case_more_red_than_exist(self):
        # Test case where more red balls are requested than exist
        x, y, n = 10, 20, 11
        result = hypergeometric_probability(x, y, n)
        self.assertEqual(result, 0.0)

    def test_impossible_case_too_many_balls_requested(self):
        # Test case where number of requested red balls is more than 15
        x, y, n = 30, 30, 16
        result = hypergeometric_probability(x, y, n)
        self.assertEqual(result, 0.0)

    def test_edge_case_minimum_red_balls(self):
        # Test case at the edge where n red balls are exactly available
        x, y, n = 15, 30, 15
        result = hypergeometric_probability(x, y, n)
        self.assertAlmostEqual(result, 0.002165, places=6)

    def test_zero_red_balls(self):
        # Test case where there are zero red balls
        x, y, n = 0, 30, 1
        result = hypergeometric_probability(x, y, n)
        self.assertEqual(result, 0.0)
from math import comb


def hypergeometric_probability(x, y, n):
    """
    Calculate the probability of drawing at least n red balls
    when 15 balls are drawn from a jar containing x red balls and y blue balls.

    :param x: Number of red balls in the jar
    :param y: Number of blue balls in the jar
    :param n: Minimum number of red balls to be drawn
    :return: Probability of drawing at least n red balls
    """
    total_balls = x + y
    if x < n or n > 15:
        # It's impossible to draw more red balls than exist or more than 15
        return 0.0

    probability = 0.0
    for k in range(n, min(16, x + 1)):  # k cannot exceed the total number of red balls
        numerator = comb(x, k) * comb(y, 15 - k)
        denominator = comb(total_balls, 15)
        probability += numerator / denominator
    return probability
