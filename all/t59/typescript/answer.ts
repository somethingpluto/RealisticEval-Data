function probabilityRedBalls(x: number, n: number, m: number): number {
    /**
     * Calculate the probability that x balls will be randomly drawn from a jar containing n red balls and m blue balls,
     * and all of them will be red balls.
     *
     * @param {number} x - Number of balls to draw.
     * @param {number} n - Number of red balls in the jar.
     * @param {number} m - Number of blue balls in the jar.
     * @returns {number} - The probability that all x drawn balls are red.
     */

    if (x > n || x > (n + m)) {
        return 0; // It's impossible to draw more red balls than available or more balls than total
    }

    const totalWaysToDrawXFromNPlusM = factorial(n + m) / (factorial(x) * factorial(n + m - x));
    const waysToDrawXRedBallsFromN = factorial(n) / (factorial(x) * factorial(n - x));

    return waysToDrawXRedBallsFromN / totalWaysToDrawXFromNPlusM;
}

// Helper function to calculate factorial
function factorial(num: number): number {
    let result = 1;
    for (let i = 2; i <= num; i++) {
        result *= i;
    }
    return result;
}