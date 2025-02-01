/**
 * Filters elements from an array based on a qualification function.
 *
 * @param {Array} unfilteredArray - The array to filter.
 * @param {Function} isQualified - The function that determines if an element qualifies.
 * @returns {Array} - A new array containing the elements that qualify.
 */
function filterArray(unfilteredArray, isQualified) {
    return unfilteredArray.filter(isQualified);
}
describe('filterArray', () => {
    // Qualification function that checks if a number is greater than 10
    const isGreaterThanTen = (num) => num > 10;

    test('filters out numbers less than or equal to 10', () => {
        const unfilteredArray = [5, 12, 3, 18, 7, 10, 15];
        const result = filterArray(unfilteredArray, isGreaterThanTen);
        expect(result).toEqual([12, 18, 15]);
    });

    test('returns an empty array when all elements are disqualified', () => {
        const unfilteredArray = [1, 2, 3, 4, 5];
        const result = filterArray(unfilteredArray, isGreaterThanTen);
        expect(result).toEqual([]);
    });

    test('returns the same array when all elements are qualified', () => {
        const unfilteredArray = [11, 12, 15, 20];
        const result = filterArray(unfilteredArray, isGreaterThanTen);
        expect(result).toEqual([11, 12, 15, 20]);
    });

    test('handles an empty array input', () => {
        const unfilteredArray = [];
        const result = filterArray(unfilteredArray, isGreaterThanTen);
        expect(result).toEqual([]);
    });

    test('filters out strings based on length', () => {
        const isLongerThanThreeChars = (str) => str.length > 3;
        const unfilteredArray = ['a', 'ab', 'abc', 'abcd', 'abcde'];
        const result = filterArray(unfilteredArray, isLongerThanThreeChars);
        expect(result).toEqual(['abcd', 'abcde']);
    });

    test('correctly filters an array with mixed types', () => {
        const isString = (item) => typeof item === 'string';
        const unfilteredArray = [1, 'hello', true, 'world', null];
        const result = filterArray(unfilteredArray, isString);
        expect(result).toEqual(['hello', 'world']);
    });

    test('filters based on an object property', () => {
        const hasValueGreaterThanFive = (obj) => obj.value > 5;
        const unfilteredArray = [{ value: 3 }, { value: 5 }, { value: 7 }];
        const result = filterArray(unfilteredArray, hasValueGreaterThanFive);
        expect(result).toEqual([{ value: 7 }]);
    });

    test('returns an empty array when no qualifying function is provided', () => {
        const unfilteredArray = [1, 2, 3, 4, 5];
        const result = filterArray(unfilteredArray, () => false); // Always returns false
        expect(result).toEqual([]);
    });
});
