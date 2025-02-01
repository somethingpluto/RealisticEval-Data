/**
 * Convert a dictionary of lists into a list of dictionaries.
 * 
 * @param {Object} dictOfLists - An object where each key has an array as its value.
 * @returns {Array} - An array where each item is an object formed by corresponding elements of arrays in the input object.
 * @throws {Error} - If arrays in the object are of different lengths.
 */
function dictOfListsToListOfDicts(dictOfLists) {
    const keys = Object.keys(dictOfLists);
    const lists = keys.map(key => dictOfLists[key]);
    const maxLength = Math.max(...lists.map(list => list.length));

    if (lists.some(list => list.length !== maxLength)) {
        throw new Error('Arrays in the object are of different lengths.');
    }

    const result = [];
    for (let i = 0; i < maxLength; i++) {
        const item = {};
        keys.forEach((key, index) => {
            item[key] = lists[index][i];
        });
        result.push(item);
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
