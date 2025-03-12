import { isInteger, isNumber } from 'util';

function calculateAverageDifference(numbers: number[]): number {
  if (numbers.length < 2) {
    return 0;
  }

  const sortedNumbers = numbers.filter(isNumber).sort((a, b) => a - b).filter(isInteger);
  const differences = sortedNumbers.slice(1).map((num, index) => num - sortedNumbers[index]);

  return differences.reduce((acc, curr) => acc + curr, 0) / differences.length;
}
describe('calculateAverageDifference', () => {
    test('calculates average difference for positive integers', () => {
        const numbers: number[] = [10, 20, 30, 40];
        const result = calculateAverageDifference(numbers);
        const expected = 10.0;
        expect(result).toBeCloseTo(expected, 5); // Precision for floating point comparison
    });

    test('calculates average difference for mixed positive and negative integers', () => {
        const numbers: number[] = [-10, 0, 10, 20];
        const result = calculateAverageDifference(numbers);
        const expected = 10.0;
        expect(result).toBeCloseTo(expected, 5);
    });

    test('calculates average difference for same values', () => {
        const numbers: number[] = [5, 5, 5, 5];
        const result = calculateAverageDifference(numbers);
        const expected = 0.0;
        expect(result).toBeCloseTo(expected, 5);
    });

    test('returns 0.0 for single element list', () => {
        const numbers: number[] = [100];
        const result = calculateAverageDifference(numbers);
        const expected = 0.0; // Not enough data to calculate differences
        expect(result).toBeCloseTo(expected, 5);
    });

    test('returns 0.0 for empty list', () => {
        const numbers: number[] = [];
        const result = calculateAverageDifference(numbers);
        const expected = 0.0; // Not enough data to calculate differences
        expect(result).toBeCloseTo(expected, 5);
    });
});
