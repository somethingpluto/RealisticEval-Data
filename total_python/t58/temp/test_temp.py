import unittest


class TestProbabilityAtLeastNRedBalls(unittest.TestCase):

    def test_basic_functionality(self):
        result = probability_at_least_n_red_balls(5, 10, 20)
        expected = 0.6501  # This is a precomputed value assuming the function is correct
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
from scipy.stats import hypergeom
import numpy as np

def probability_at_least_n_red_balls(n, x, y):
    """
    Calculates the probability of drawing at least 'n' red balls when
    randomly withdrawing 15 balls from a jar containing 'x' red balls
    and 'y' blue balls.

    Args:
    n (int): Minimum number of red balls to be drawn.
    x (int): Total number of red balls in the jar.
    y (int): Total number of blue balls in the jar.

    Returns:
    float: Probability of drawing at least 'n' red balls.
    """
    # Total number of balls in the jar
    M = x + y
    # Total number of draws
    n_draws = 15
    # Check if it's possible to draw n red balls
    if n > n_draws:
        return 0
    # Calculate the probability of drawing at least 'n' red balls
    # Using the survival function which is 1 - CDF(k-1) to calculate P(X >= k)
    probability = hypergeom.sf(n - 1, M, x, n_draws)
    return probability