import { factorial } from './mathUtils';

function probabilityRedBalls(x: number, n: number, m: number): number {
  if (x > n || x > (n + m)) {
    throw new Error('Invalid input: x cannot be greater than n or n + m.');
  }
  const numerator = factorial(n);
  const denominator = factorial(n - x) * factorial(x) * factorial(m);
  return numerator / denominator;
}
const { comb } = require('js-combinatorics');

describe('TestProbabilityRedBalls', () => {
    it('should return 1 when all balls are red', () => {
        // Case where all balls are red
        expect(probabilityRedBalls(5, 5, 0)).toBe(1);
    });

    it('should return 0 when no red balls are available', () => {
        // Case where no red balls are available
        expect(probabilityRedBalls(1, 0, 5)).toBe(0);
    });

    it('should return the correct probability in a typical scenario', () => {
        // Typical scenario
        const expectedProbability = comb(10, 2) / comb(15, 2);
        expect(probabilityRedBalls(2, 10, 5)).toBeCloseTo(expectedProbability, 6);
    });

    it('should return 0 when more balls are requested than available', () => {
        // More balls requested than available
        expect(probabilityRedBalls(6, 5, 4)).toBe(0);
    });

    it('should return the correct probability with higher number of combinations', () => {
        // Test with higher number of combinations
        const expectedProbability = comb(20, 3) / comb(50, 3);
        expect(probabilityRedBalls(3, 20, 30)).toBeCloseTo(expectedProbability, 6);
    });
});
