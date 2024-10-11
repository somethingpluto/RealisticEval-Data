from math import comb

def probability_red_balls(x, n, m):
    """
    Calculate the probability that x balls randomly drawn from a jar containing
    n red balls and m blue balls will all be red balls.

    Args:
    x (int): Number of balls to draw.
    n (int): Number of red balls in the jar.
    m (int): Number of blue balls in the jar.

    Returns:
    float: The probability that all x drawn balls are red.
    """
    if x > n:
        return 0  # Not enough red balls to draw x red balls
    total_balls = n + m
    if x > total_balls:
        return 0  # Not enough balls to draw x balls of any color

    # Number of ways to choose x red balls from n red balls
    ways_to_choose_red = comb(n, x)
    # Total number of ways to choose x balls from all balls
    total_ways_to_choose_balls = comb(total_balls, x)

    # Probability that all chosen balls are red
    probability = ways_to_choose_red / total_ways_to_choose_balls

    return probability