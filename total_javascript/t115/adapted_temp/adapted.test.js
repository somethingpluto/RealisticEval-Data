describe('sortByKey function', () => {
    test('should return an empty array when input is empty', () => {
        const result = sortByKey([], 'name');
        expect(result).toEqual([]);
    });

    test('should correctly handle an array with a single element', () => {
        const singleElementArray = [{ name: 'Apple' }];
        expect(sortByKey(singleElementArray, 'name')).toEqual([{ name: 'Apple' }]);
    });

    test('should sort an array of objects by the specified key', () => {
        const testData = [
            { name: 'banana' },
            { name: 'apple' },
            { name: 'orange' }
        ];
        const expected = [
            { name: 'apple' },
            { name: 'banana' },
            { name: 'orange' }
        ];
        expect(sortByKey(testData, 'name')).toEqual(expected);
    });

    test('should perform case-insensitive sorting', () => {
        const mixedCaseArray = [
            { name: 'banana' },
            { name: 'Apple' },
            { name: 'orange' }
        ];
        const expected = [
            { name: 'Apple' },
            { name: 'banana' },
            { name: 'orange' }
        ];
        expect(sortByKey(mixedCaseArray, 'name')).toEqual(expected);
    });

    test('should handle objects missing the specified key', () => {
        const incompleteData = [
            { name: 'banana' },
            { quantity: 20 },
            { name: 'apple' }
        ];
        const expected = [
            { quantity: 20 },  // Objects without the key go to the front if their comparison value defaults to empty
            { name: 'apple' },
            { name: 'banana' }
        ];
        expect(sortByKey(incompleteData, 'name')).toEqual(expected);
    });
});
/**
 * Sorts an array of objects alphabetically by a specified key.
 *
 * @param {Object[]} array - The array of objects to be sorted.
 * @param {string} key - The key in the objects to sort by.
 * @returns {Object[]} The sorted array based on the specified key.
 */
function sortByKey(array, key) {
    return array.sort((a, b) => {
        // Retrieve the string values from each object by the key, converting to lowercase for case-insensitive comparison
        const valueA = (a[key] || '').toString().toLowerCase();
        const valueB = (b[key] || '').toString().toLowerCase();

        // Compare the values to determine the order
        if (valueA < valueB) {
            return -1; // a comes first
        }
        if (valueA > valueB) {
            return 1; // b comes first
        }
        return 0; // a and b are equal
    });
}