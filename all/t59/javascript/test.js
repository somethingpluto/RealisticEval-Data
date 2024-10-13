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