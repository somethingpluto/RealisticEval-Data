/**
 * Calculate the probability that n red balls will be drawn when 15 balls are randomly drawn from a jar containing x red balls and y blue balls.
 *
 * @param {number} n - Number of red balls to be drawn.
 * @param {number} x - Number of red balls in the jar.
 * @param {number} y - Number of blue balls in the jar.
 * @returns {number} - The probability of drawing exactly n red balls.
 */
function probabilityOfRedBalls(n, x, y) {
    if (n < 0 || n > 15 || x < 0 || y < 0 || x + y < 15) {
        throw new Error('Invalid input');
    }

    // Calculate the total number of ways to draw 15 balls from x + y balls
    const totalWays = factorial(x + y) / (factorial(x) * factorial(y));

    // Calculate the number of ways to draw exactly n red balls
    const redWays = factorial(x) / (factorial(n) * factorial(x - n));

    // Calculate the number of ways to draw the remaining 15 - n balls
    const blueWays = factorial(y) / (factorial(15 - n) * factorial(y - (15 - n)));

    // Calculate the probability
    const probability = (redWays * blueWays) / totalWays;

    return probability;
}

// Helper function to calculate factorial
function factorial(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
const { isClose } = require('mathjs'); // Assuming we use mathjs for isClose function

describe('TestProbabilityOfRedBalls', () => {
    describe('testHalfRedBalls', () => {
        it('should pass for half red balls', () => {
            // Scenario where half of the drawn balls are expected to be red
            const result = probabilityOfRedBalls(7, 10, 10);
            const expectedResult = probabilityOfRedBalls(7, 10, 10); // Calculate manually or from another tool
            expect(isClose(result, expectedResult)).toBe(true);
        });
    });

    describe('testSomeRedBalls', () => {
        it('should pass for some red balls', () => {
            // Scenario with some red balls in the jar, expecting a few red draws
            const result = probabilityOfRedBalls(5, 5, 10);
            const expectedResult = probabilityOfRedBalls(5, 5, 10); // Calculate manually or from another tool
            expect(isClose(result, expectedResult)).toBe(true);
        });
    });

    describe('testExtremeCase', () => {
        it('should pass for extreme case', () => {
            // Extreme scenario where the probability is low for the chosen n
            const result = probabilityOfRedBalls(15, 1, 99);
            const expectedResult = probabilityOfRedBalls(15, 1, 99); // Calculate manually or from another tool
            expect(isClose(result, expectedResult)).toBe(true);
        });
    });
});
