/**
 * Iterates through the array of elements until the first null is encountered,
 * returning a new array that includes all elements before the first null.
 *
 * @param {Array} array - The array to iterate through.
 * @returns {Array} - A new array containing elements before the first null.
 */
function elementsBeforeNull(array) {
  const result = [];
  for (let i = 0; i < array.length; i++) {
    if (array[i] === null) {
      break;
    }
    result.push(array[i]);
  }
  return result;
}

describe('elementsBeforeNull', () => {
    test('returns elements before the first null', () => {
        const inputArray = ['element1', 'element2', null, 'element3', 'element4'];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual(['element1', 'element2']);
    });

    test('returns an empty array when input is empty', () => {
        const inputArray = [];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual([]);
    });

    test('returns the same array if there is no null', () => {
        const inputArray = ['element1', 'element2', 'element3'];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual(['element1', 'element2', 'element3']);
    });

    test('returns an empty array if the first element is null', () => {
        const inputArray = [null, 'element2', 'element3'];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual([]);
    });

    test('handles mixed types with null', () => {
        const inputArray = [1, 'text', null, true, false];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual([1, 'text']);
    });

    test('handles an array with only null', () => {
        const inputArray = [null];
        const result = elementsBeforeNull(inputArray);
        expect(result).toEqual([]);
    });
});
