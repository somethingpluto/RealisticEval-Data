/**
 * Iterates through the array of elements until the first null is encountered,
 * returning a new array that includes all elements before the null.
 *
 * @param {Array<any>} array - The array to iterate through.
 * @returns {Array<any>} - A new array containing elements before the first null.
 */
function elementsBeforeNull(array: Array<any>): Array<any> {
    let nullIndex = array.indexOf(null);
    if (nullIndex === -1) {
        return array;
    } else {
        return array.slice(0, nullIndex);
    }
}
describe('elementsBeforeNull', () => {
    test('returns elements before the first null', () => {
        const inputArray: (string | null)[] = ['element1', 'element2', null, 'element3', 'element4'];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual(['element1', 'element2']);
    });

    test('returns an empty array when input is empty', () => {
        const inputArray: (string | null)[] = [];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual([]);
    });

    test('returns the same array if there is no null', () => {
        const inputArray: string[] = ['element1', 'element2', 'element3'];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual(['element1', 'element2', 'element3']);
    });

    test('returns an empty array if the first element is null', () => {
        const inputArray: (string | null)[] = [null, 'element2', 'element3'];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual([]);
    });

    test('handles mixed types with null', () => {
        const inputArray: (number | string | boolean | null)[] = [1, 'text', null, true, false];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual([1, 'text']);
    });

    test('handles an array with only null', () => {
        const inputArray: (null)[] = [null];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual([]);
    });
});
