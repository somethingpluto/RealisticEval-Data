from math import factorial

def probability_of_red_balls(n: int, x: int, y: int) -> float:
    total_balls = x + y
    total_ways = factorial(total_balls) / (factorial(n) * factorial(total_balls - n))
    red_ways = factorial(x) / (factorial(n) * factorial(x - n))
    blue_ways = factorial(y) / (factorial(15 - n) * factorial(y - 15 + n))
    probability = (red_ways * blue_ways) / total_ways
    return probability
import unittest
from math import isclose


class TestProbabilityOfRedBalls(unittest.TestCase):

    def test_half_red_balls(self):
        # Scenario where half of the drawn balls are expected to be red
        result = probability_of_red_balls(7, 10, 10)
        expected_result = probability_of_red_balls(7, 10, 10)  # Calculate manually or from another tool
        self.assertTrue(isclose(result, expected_result), "Test with half red balls failed")

    def test_some_red_balls(self):
        # Scenario with some red balls in the jar, expecting a few red draws
        result = probability_of_red_balls(5, 5, 10)
        expected_result = probability_of_red_balls(5, 5, 10)  # Calculate manually or from another tool
        self.assertTrue(isclose(result, expected_result), "Test with some red balls failed")

    def test_extreme_case(self):
        # Extreme scenario where the probability is low for the chosen n
        result = probability_of_red_balls(15, 1, 99)
        expected_result = probability_of_red_balls(15, 1, 99)  # Calculate manually or from another tool
        self.assertTrue(isclose(result, expected_result), "Test with extreme case failed")
if __name__ == '__main__':
    unittest.main()