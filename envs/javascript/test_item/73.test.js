/**
 * Convert a dictionary of lists into a list of dictionaries.
 * 
 * @param {Object} dictOfLists - An object where each key has an array as its value.
 * @returns {Array} - An array where each item is an object formed by corresponding elements of arrays in the input object.
 * @throws {Error} - If arrays in the object are of different lengths.
 */
function dictOfListsToListOfDicts(dictOfLists) {
    // Check if the input is an object
    if (typeof dictOfLists !== 'object' || dictOfLists === null || Array.isArray(dictOfLists)) {
        throw new Error('Input must be an object.');
    }

    // Extract all the keys and values from the input object
    const keys = Object.keys(dictOfLists);
    const values = Object.values(dictOfLists);

    // Check if all arrays have the same length
    const lengths = values.map(arr => arr.length);
    const allSameLength = lengths.every(len => len === lengths[0]);

    if (!allSameLength) {
        throw new Error('Arrays in the object must be of the same length.');
    }

    // Initialize the result array
    const result = [];

    // Iterate over the length of the arrays
    for (let i = 0; i < lengths[0]; i++) {
        // Create a new dictionary for the current index
        const newDict = {};

        // Populate the new dictionary with key-value pairs from the input object
        keys.forEach((key, index) => {
            newDict[key] = values[index][i];
        });

        // Add the new dictionary to the result array
        result.push(newDict);
    }

    return result;
}
describe('TestDictOfListsToListOfDicts', () => {
  describe('test_standard_conversion', () => {
      it('should correctly convert a dictionary of lists into a list of dictionaries with equal length lists', () => {
          const dictOfLists = {
              name: ['Alice', 'Bob', 'Charlie'],
              age: [25, 30, 35],
              city: ['New York', 'Los Angeles', 'Chicago']
          };
          const expectedResult = [
              { name: 'Alice', age: 25, city: 'New York' },
              { name: 'Bob', age: 30, city: 'Los Angeles' },
              { name: 'Charlie', age: 35, city: 'Chicago' }
          ];
          const result = dictOfListsToListOfDicts(dictOfLists);
          expect(result).toEqual(expectedResult);
      });
  });

  describe('test_empty_lists', () => {
      it('should handle empty lists correctly', () => {
          const dictOfLists = {
              name: [],
              age: [],
              city: []
          };
          const expectedResult = [];
          const result = dictOfListsToListOfDicts(dictOfLists);
          expect(result).toEqual(expectedResult);
      });
  });

  describe('test_single_element_lists', () => {
      it('should correctly convert a dictionary of single-element lists into a list of dictionaries', () => {
          const dictOfLists = {
              name: ['Alice'],
              age: [25],
              city: ['New York']
          };
          const expectedResult = [
              { name: 'Alice', age: 25, city: 'New York' }
          ];
          const result = dictOfListsToListOfDicts(dictOfLists);
          expect(result).toEqual(expectedResult);
      });
  });
});
