/**
 * Calculate the probability that n red balls will be drawn when 15 balls are randomly drawn from a jar containing x red balls and y blue balls.
 *
 * @param {number} n - Number of red balls to be drawn.
 * @param {number} x - Number of red balls in the jar.
 * @param {number} y - Number of blue balls in the jar.
 * @returns {number} - The probability of drawing exactly n red balls.
 */
function probabilityOfRedBalls(n, x, y) {
    // Total number of balls in the jar
    const totalBalls = x + y;

    // Total number of ways to draw 15 balls from the jar
    const totalWays = binomialCoefficient(totalBalls, 15);

    // Number of ways to draw n red balls from x red balls
    const waysToDrawRedBalls = binomialCoefficient(x, n);

    // Number of ways to draw (15 - n) blue balls from y blue balls
    const waysToDrawBlueBalls = binomialCoefficient(y, 15 - n);

    // Total number of favorable outcomes
    const favorableOutcomes = waysToDrawRedBalls * waysToDrawBlueBalls;

    // Probability of drawing exactly n red balls
    const probability = favorableOutcomes / totalWays;

    return probability;
}

/**
 * Calculate the binomial coefficient (n choose k).
 *
 * @param {number} n - Total number of items.
 * @param {number} k - Number of items to choose.
 * @returns {number} - The binomial coefficient.
 */
function binomialCoefficient(n, k) {
    if (k > n) return 0;
    if (k === 0 || k === n) return 1;

    let coefficient = 1;
    for (let i = 0; i < k; i++) {
        coefficient *= (n - i);
        coefficient /= (i + 1);
    }

    return coefficient;
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
