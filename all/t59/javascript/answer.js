function probabilityRedBalls(x, n, m) {
    /**
     * Calculate the probability that x balls will be randomly drawn from a jar containing n red balls and m blue balls, and all of them will be red balls
     * @param {number} x - Number of balls to draw.
     * @param {number} n - Number of red balls in the jar.
     * @param {number} m - Number of blue balls in the jar.
     * @returns {number} The probability that all x drawn balls are red.
     */

    // Check if it's possible to draw x balls from the jar
    if (x > n + m || x < 0) {
        return 0;
    }

    // Calculate combinations using factorial
    function factorial(num) {
        let result = 1;
        for(let i = num; i > 0; i--){
            result *= i;
        }
        return result;
    }

    const totalCombinations = factorial(n + m) / (factorial(x) * factorial(n + m - x));
    const redBallCombinations = factorial(n) / (factorial(x) * factorial(n - x));

    return redBallCombinations / totalCombinations;
}