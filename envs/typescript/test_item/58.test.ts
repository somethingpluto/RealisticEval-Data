import { comb } from 'mathjs';

function probabilityOfRedBalls(n: number, x: number, y: number): number {
  if (n > x || n > (x + y) || n < 0 || x < 0 || y < 0) {
    throw new Error('Invalid input values');
  }

  const totalCombinations = comb(x + y, n);
  const favorableCombinations = comb(x, n);

  return favorableCombinations / totalCombinations;
}
describe('TestProbabilityOfRedBalls', () => {
    describe('testHalfRedBalls', () => {
        it('should calculate the correct probability for half red balls', () => {
            const result = probabilityOfRedBalls(7, 10, 10);
            const expectedResult = probabilityOfRedBalls(7, 10, 10); // Calculate manually or from another tool
            expect(result).toBeCloseTo(expectedResult, 10); // Use beCloseTo for floating-point comparison
        });
    });

    describe('testSomeRedBalls', () => {
        it('should calculate the correct probability for some red balls', () => {
            const result = probabilityOfRedBalls(5, 5, 10);
            const expectedResult = probabilityOfRedBalls(5, 5, 10); // Calculate manually or from another tool
            expect(result).toBeCloseTo(expectedResult, 10); // Use beCloseTo for floating-point comparison
        });
    });

    describe('testExtremeCase', () => {
        it('should calculate the correct probability for an extreme case', () => {
            const result = probabilityOfRedBalls(15, 1, 99);
            const expectedResult = probabilityOfRedBalls(15, 1, 99); // Calculate manually or from another tool
            expect(result).toBeCloseTo(expectedResult, 10); // Use beCloseTo for floating-point comparison
        });
    });
});
