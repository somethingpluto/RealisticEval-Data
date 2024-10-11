'''
I have a jar with 5625 red balls and 1875 blue ball.
I draw out 15 balls.
What is the probability that all 15 balls are red?
'''
from scipy.special import comb


def probability_all_red(n, N_red, N_blue):
    return (comb(n, n) * comb(N_red, n) * comb(N_blue, 0)) / comb(N_red + N_blue, n)


def all_red():
    # Given information
    N_red_balls = 5625
    N_blue_balls = 1875
    total_draws = 15

    # Calculate probability of all 15 balls being red
    probability_all_15_red = probability_all_red(total_draws, N_red_balls, N_blue_balls)

    print(f"The probability of drawing all 15 balls as red is: {probability_all_15_red:.6f}")


all_red()
