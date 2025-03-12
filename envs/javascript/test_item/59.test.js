/**
 * Calculate the probability that x balls will be randomly drawn from a jar containing n red balls and m blue balls, and all of them will be red balls.
 * 
 * @param {number} x - Number of balls to draw.
 * @param {number} n - Number of red balls in the jar.
 * @param {number} m - Number of blue balls in the jar.
 * 
 * @returns {number} The probability that all x drawn balls are red.
 */
function probabilityRedBalls(x, n, m) {
    // Total number of balls in the jar
    const totalBalls = n + m;

    // Check if it's possible to draw x red balls
    if (x > n) {
        return 0; // Not enough red balls to draw x red balls
    }

    // Calculate the number of ways to choose x red balls from n red balls
    const chooseRed = binomialCoefficient(n, x);

    // Calculate the number of ways to choose (x) balls from the total (n + m) balls
    const chooseTotal = binomialCoefficient(totalBalls, x);

    // The probability is the ratio of the number of ways to choose x red balls
    // to the number of ways to choose x balls from the total number of balls
    return chooseRed / chooseTotal;
}

/**
 * Helper function to calculate the binomial coefficient (n choose k).
 * 
 * @param {number} n - Total number of items.
 * @param {number} k - Number of items to choose.
 * 
 * @returns {number} The binomial coefficient.
 */
function binomialCoefficient(n, k) {
    if (k > n) return 0;
    if (k === 0 || k === n) return 1;

    let result = 1;
    for (let i = 1; i <= k; i++) {
        result *= (n - i + 1) / i;
    }
    return result;
}
const { comb } = require('js-combinatorics');

describe('TestProbabilityRedBalls', () => {
  describe('test_all_red', () => {
      it('should return 1 when all balls are red', () => {
          expect(probabilityRedBalls(5, 5, 0)).toBe(1);
      });
  });

  describe('test_no_red', () => {
      it('should return 0 when no red balls are available', () => {
          expect(probabilityRedBalls(1, 0, 5)).toBe(0);
      });
  });

  describe('test_typical_case', () => {
      it('should return the correct probability in a typical scenario', () => {
          const expectedProbability = comb(10, 2) / comb(15, 2);
          expect(probabilityRedBalls(2, 10, 5)).toBeCloseTo(expectedProbability, 10); // Adjust precision as needed
      });
  });

  describe('test_impossible_case', () => {
      it('should return 0 when more balls are requested than available', () => {
          expect(probabilityRedBalls(6, 5, 4)).toBe(0);
      });
  });

  describe('test_high_combinations', () => {
      it('should return the correct probability with higher number of combinations', () => {
          const expectedProbability = comb(20, 3) / comb(50, 3);
          expect(probabilityRedBalls(3, 20, 30)).toBeCloseTo(expectedProbability, 10); // Adjust precision as needed
      });
  });
});
