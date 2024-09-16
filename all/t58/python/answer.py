from math import comb


def probability_of_red_balls(n: int, x: int, y: int) -> float:
    """
    Calculate the probability that n red balls will be drawn when 15 balls are drawn with replacement
    from a jar containing x red balls and y blue balls.

    Args:
        n (int): Number of red balls to be drawn.
        x (int): Number of red balls in the jar.
        y (int): Number of blue balls in the jar.

    Returns:
        float: The probability of drawing exactly n red balls.
    """
    N = 15  # Total number of draws
    p = x / (x + y)  # Probability of drawing a red ball

    # Calculate the probability using the binomial formula
    probability = comb(N, n) * (p ** n) * ((1 - p) ** (N - n))
    return probability