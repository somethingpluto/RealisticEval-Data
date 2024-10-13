const {comb}= require('mathjs')

/**
 * Calculate the probability that x balls randomly drawn from a jar containing
 * n red balls and m blue balls will all be red balls.
 *
 * @param x - Number of balls to draw.
 * @param n - Number of red balls in the jar.
 * @param m - Number of blue balls in the jar.
 * @returns The probability that all x drawn balls are red.
 */
function probabilityRedBalls(x: number, n: number, m: number): number {
    if (x > n) {
        return 0; // Not enough red balls to draw x red balls
    }
    const totalBalls = n + m;
    if (x > totalBalls) {
        return 0; // Not enough balls to draw x balls of any color
    }

    // Number of ways to choose x red balls from n red balls
    const waysToChooseRed = comb(n, x);
    // Total number of ways to choose x balls from all balls
    const totalWaysToChooseBalls = comb(totalBalls, x);

    // Probability that all chosen balls are red
    const probability = waysToChooseRed / totalWaysToChooseBalls;

    return probability;
}