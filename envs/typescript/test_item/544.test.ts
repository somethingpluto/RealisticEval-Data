import { isEven } from './utils';

/**
 * Filters out all even numbers from an array.
 *
 * @param {number[]} array - The array of numbers to filter.
 * @returns {number[]} - A new array containing only the odd numbers.
 */
function filterOutEvenNumbers(array: number[]): number[] {
    return array.filter(isEven);
}
describe('filterOutEvenNumbers', () => {
    test('removes all even numbers from the array', () => {
        const inputArray: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        const result: number[] = filterOutEvenNumbers(inputArray);
        expect(result).toEqual([1, 3, 5, 7, 9]);
    });

    test('returns an empty array when input is empty', () => {
        const inputArray: number[] = [];
        const result: number[] = filterOutEvenNumbers(inputArray);
        expect(result).toEqual([]);
    });

    test('returns the same array if all numbers are odd', () => {
        const inputArray: number[] = [1, 3, 5, 7, 9];
        const result: number[] = filterOutEvenNumbers(inputArray);
        expect(result).toEqual([1, 3, 5, 7, 9]);
    });

    test('returns an empty array if all numbers are even', () => {
        const inputArray: number[] = [2, 4, 6, 8, 10];
        const result: number[] = filterOutEvenNumbers(inputArray);
        expect(result).toEqual([]);
    });

    test('handles mixed positive and negative numbers', () => {
        const inputArray: number[] = [-3, -2, -1, 0, 1, 2, 3];
        const result: number[] = filterOutEvenNumbers(inputArray);
        expect(result).toEqual([-3, -1, 1, 3]);
    });

    test('handles large numbers and zero correctly', () => {
        const inputArray: number[] = [0, 1000000000, 1000000001, 1000000002, 1000000003];
        const result: number[] = filterOutEvenNumbers(inputArray);
        expect(result).toEqual([1000000001, 1000000003]);
    });
});
