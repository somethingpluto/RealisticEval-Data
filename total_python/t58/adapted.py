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
