import { compare } from 'natural-compare-lite';

/**
 * Sorts an array of objects alphabetically by a specified key, with case-insensitive comparison.
 *
 * @param {Array<Record<string, any>>} array - The array of objects to be sorted.
 * @param {string} key - The key in the objects to sort by.
 * @returns {Array<Record<string, any>>} The sorted array based on the specified key.
 */
function sortByKey(array: Array<Record<string, any>>, key: string): Array<Record<string, any>> {
  return array.sort((a, b) => compare(a[key].toString().toLowerCase(), b[key].toString().toLowerCase()));
}
describe('sortByKey function', () => {
    test('should return an empty array when input is empty', () => {
        const result = sortByKey([], 'name');
        expect(result).toEqual([]);
    });

    test('should correctly handle an array with a single element', () => {
        const singleElementArray: Array<Record<string, any>> = [{ name: 'Apple' }];
        expect(sortByKey(singleElementArray, 'name')).toEqual([{ name: 'Apple' }]);
    });

    test('should sort an array of objects by the specified key', () => {
        const testData: Array<Record<string, any>> = [
            { name: 'banana' },
            { name: 'apple' },
            { name: 'orange' }
        ];
        const expected: Array<Record<string, any>> = [
            { name: 'apple' },
            { name: 'banana' },
            { name: 'orange' }
        ];
        expect(sortByKey(testData, 'name')).toEqual(expected);
    });

    test('should perform case-insensitive sorting', () => {
        const mixedCaseArray: Array<Record<string, any>> = [
            { name: 'banana' },
            { name: 'Apple' },
            { name: 'orange' }
        ];
        const expected: Array<Record<string, any>> = [
            { name: 'Apple' },
            { name: 'banana' },
            { name: 'orange' }
        ];
        expect(sortByKey(mixedCaseArray, 'name')).toEqual(expected);
    });
});
