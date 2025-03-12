from math import comb

def probability_red_balls(x: int, n: int, m: int) -> float:
    total_red_balls = n
    total_balls = n + m
    
    return comb(total_red_balls, x) / comb(total_balls, x)
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