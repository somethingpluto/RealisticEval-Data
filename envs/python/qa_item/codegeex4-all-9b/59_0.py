def probability_red_balls(x: int, n: int, m: int) -> float:
    """
    calculate the probability that x balls will be randomly drawn from a jar containing n red balls and m blue balls, and all of them will be red balls
    Args:
        x (int): Number of balls to draw.
        n (int): Number of red balls in the jar.
        m (int): Number of blue balls in the jar.

    Returns:
        The probability that all x drawn balls are red.
    """
    if x > n:
        return 0.0
    else:
        return (n / (n + m)) * ((n - 1) / (n + m - 1)) * ... * ((n - x + 1) / (n + m - x + 1))
import unittest
from math import comb


class TestProbabilityRedBalls(unittest.TestCase):
    def test_all_red(self):
        # Case where all balls are red
        self.assertEqual(probability_red_balls(5, 5, 0), 1)

    def test_no_red(self):
        # Case where no red balls are available
        self.assertEqual(probability_red_balls(1, 0, 5), 0)

    def test_typical_case(self):
        # Typical scenario
        self.assertAlmostEqual(probability_red_balls(2, 10, 5), comb(10, 2) / comb(15, 2))

    def test_impossible_case(self):
        # More balls requested than available
        self.assertEqual(probability_red_balls(6, 5, 4), 0)

    def test_high_combinations(self):
        # Test with higher number of combinations
        self.assertAlmostEqual(probability_red_balls(3, 20, 30), comb(20, 3) / comb(50, 3))
if __name__ == '__main__':
    unittest.main()