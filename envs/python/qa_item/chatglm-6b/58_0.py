
def probability_of_red_balls(n: int, x: int, y: int) -> float:
    """
    Calculate the probability that n red balls will be drawn when 15 balls are randomly returned from a jar containing x red balls and y blue balls.

    Args:
        n (int): Number of red balls to be drawn.
        x (int): Number of red balls in the jar.
        y (int): Number of blue balls in the jar.

    Returns:
        float: The probability of drawing exactly n red balls.
    """
    # Calculate the number of red balls and blue balls in the jar
    red_balls = x + y
    blue_balls = y

    # Calculate the number of red balls drawn
    red_ball_count = 0
    for i in range(n):
        # Check if the ball is red
        if (i % 2 == 0 and red_balls > 0) or (i % 2 == 1 and blue_balls > 0):
            red_ball_count += 1

    # Calculate the probability of drawing exactly n red balls
    return red_ball_count / (red_balls + blue_balls)

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