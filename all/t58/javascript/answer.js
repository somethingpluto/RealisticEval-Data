const { comb } = require('mathjs');

function probabilityOfRedBalls(n, x, y) {
    /**
     * Calculate the probability that n red balls will be drawn when 15 balls are drawn with replacement
     * from a jar containing x red balls and y blue balls.
     *
     * @param {number} n - Number of red balls to be drawn.
     * @param {number} x - Number of red balls in the jar.
     * @param {number} y - Number of blue balls in the jar.
     *
     * @returns {number} - The probability of drawing exactly n red balls.
     */
    const N = 15;  // Total number of draws
    const p = x / (x + y);  // Probability of drawing a red ball

    // Calculate the probability using the binomial formula
    const probability = comb(N, n) * Math.pow(p, n) * Math.pow(1 - p, N - n);
    return probability;
}