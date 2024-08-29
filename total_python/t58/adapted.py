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