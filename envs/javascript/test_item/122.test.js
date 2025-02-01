/**
 * Safely splices an array by removing a specified number of elements from a given index,
 * and optionally replaces them with a new element.
 * 
 * @param {Array} inputArray - The original array to be modified.
 * @param {number} amountToRemove - The number of elements to remove from the array.
 * @param {number} indexToRemove - The index at which to start removing elements.
 * @param {*} [replaceWith] - Optional. The element to replace the removed elements with.
 * @returns {Array} - A new array with the specified elements removed and optionally replaced.
 */
function safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith) {
    // Create a copy of the input array to avoid mutating the original array
    const newArray = [...inputArray];

    // Check if the index is within the bounds of the array
    if (indexToRemove < 0 || indexToRemove > newArray.length) {
        throw new Error('Index out of bounds');
    }

    // Check if the amount to remove is within the bounds of the array
    if (amountToRemove < 0 || indexToRemove + amountToRemove > newArray.length) {
        throw new Error('Amount to remove is out of bounds');
    }

    // If replaceWith is provided, replace the removed elements with it
    if (replaceWith !== undefined) {
        newArray.splice(indexToRemove, amountToRemove, replaceWith);
    } else {
        // Otherwise, just remove the specified number of elements
        newArray.splice(indexToRemove, amountToRemove);
    }

    return newArray;
}
describe('safeSplice', () => {
    test('replaces removed elements with a new element', () => {
        const inputArray = ['a', 'b', 'c', 'd', 'e'];
        const expected = ['a', 'z', 'e'];
        expect(safeSplice(inputArray, 3, 1, 'z')).toEqual(expected);
    });
    test('should remove specified elements and replace with new element', () => {
        const inputArray = [1, 2, 3, 4, 5];
        const amountToRemove = 2;
        const indexToRemove = 1;
        const replaceWith = 99;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        expect(result).toEqual([1, 99, 4, 5]);
    });

    test('should handle removing elements from the end of the array', () => {
        const inputArray = [1, 2, 3, 4, 5];
        const amountToRemove = 2;
        const indexToRemove = 3;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove);
        expect(result).toEqual([1, 2, 3]);
    });

    test('should handle the case where no elements are removed', () => {
        const inputArray = [1, 2, 3, 4, 5];
        const amountToRemove = 0;
        const indexToRemove = 2;
        const replaceWith = 99;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        expect(result).toEqual([1, 2, 99, 3, 4, 5]);
    });

    test('should handle edge case with an empty input array', () => {
        const inputArray = [];
        const amountToRemove = 1;
        const indexToRemove = 0;
        const replaceWith = 99;
        const result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        expect(result).toEqual([99]);
    });
});

