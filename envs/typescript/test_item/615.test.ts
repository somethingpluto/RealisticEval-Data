import { calculateAverage } from './calculateAverage';

function calculate(values: number[], period: number): number {
  if (values.length < period) {
    throw new Error('Period is larger than the array length.');
  }
  return calculateAverage(values.slice(-period));
}
describe('calculate', () => {
    
    test('should calculate the average with valid input', () => {
        const values: number[] = [1, 2, 3, 4, 5];
        const period: number = 3;
        const expected: number = 4.0; // (3 + 4 + 5) / 3
        expect(calculate(values, period)).toBe(expected);
    });

    test('should calculate the average with all same values', () => {
        const values: number[] = [5, 5, 5, 5, 5];
        const period: number = 5;
        const expected: number = 5.0; // (5 + 5 + 5 + 5 + 5) / 5
        expect(calculate(values, period)).toBe(expected);
    });

    test('should calculate the average with a single value', () => {
        const values: number[] = [10];
        const period: number = 1;
        const expected: number = 10.0; // (10) / 1
        expect(calculate(values, period)).toBe(expected);
    });

    test('should return NaN with insufficient values', () => {
        const values: number[] = [1, 2];
        const period: number = 3;
        expect(calculate(values, period)).toBeNaN(); // Expecting NaN
    });

    test('should return NaN with an empty list', () => {
        const values: number[] = [];
        const period: number = 1;
        expect(calculate(values, period)).toBeNaN(); // Expecting NaN
    });

    test('should return NaN with negative period', () => {
        const values: number[] = [1, 2, 3, 4, 5];
        const period: number = -1;
        expect(calculate(values, period)).toBeNaN(); // Expecting NaN
    });
});
