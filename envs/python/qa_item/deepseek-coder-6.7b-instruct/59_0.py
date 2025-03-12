from math import comb

def probability_red_balls(x: int, n: int, m: int) -> float:
    """
    Calculate the probability that x balls will be randomly drawn from a jar containing n red balls and m blue balls, and all of them will be red balls.

    Args:
        x (int): Number of balls to draw.
        n (int): Number of red balls in the jar.
        m (int): Number of blue balls in the jar.

    Returns:
        The probability that all x drawn balls are red.
    """
    # Total number of balls in the jar
    total_balls = n + m
    
    # Check if it's possible to draw x red balls
    if x > n:
        return 0.0
    
    # Calculate the number of ways to choose x red balls out of n red balls
    num_ways_to_choose_red = comb(n, x)
    
    # Calculate the number of ways to choose x balls out of total_balls
    num_ways_to_choose_any = comb(total_balls, x)
    
    # The probability is the ratio of the two combinations
    probability = num_ways_to_choose_red / num_ways_to_choose_any
    
    return probability
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