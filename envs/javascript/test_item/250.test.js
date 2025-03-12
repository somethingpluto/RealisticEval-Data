/**
 * Invert the keys and values in an object. If multiple keys have the same value,
 * the new object's values will be an array of these keys.
 * 
 * @param {Object} originalDict - The object to invert.
 * @returns {Object} A new object with values and keys inverted.
 */
function invertDictionary(originalDict) {
    const invertedDict = {};

    for (const key in originalDict) {
        if (originalDict.hasOwnProperty(key)) {
            const value = originalDict[key];

            if (invertedDict[value] === undefined) {
                invertedDict[value] = key;
            } else {
                if (!Array.isArray(invertedDict[value])) {
                    invertedDict[value] = [invertedDict[value]];
                }
                invertedDict[value].push(key);
            }
        }
    }

    return invertedDict;
}
describe('TestInvertDictionary', () => {
  describe('test_normal_dictionary', () => {
      it('should correctly invert a dictionary without duplicate values', () => {
          const originalDict = {'a': 1, 'b': 2, 'c': 3};
          const expected = {1: 'a', 2: 'b', 3: 'c'};
          const result = invertDictionary(originalDict);
          expect(result).toEqual(expected);
      });
  });

  describe('test_dictionary_with_duplicates', () => {
      it('should correctly invert a dictionary with duplicate values', () => {
          const originalDict = {'a': 1, 'b': 1, 'c': 2};
          const expected = {1: ['a', 'b'], 2: 'c'};
          const result = invertDictionary(originalDict);
          expect(result).toEqual(expected);
      });
  });

  describe('test_empty_dictionary', () => {
      it('should correctly invert an empty dictionary', () => {
          const originalDict = {};
          const expected = {};
          const result = invertDictionary(originalDict);
          expect(result).toEqual(expected);
      });
  });

  describe('test_non_string_keys', () => {
      it('should correctly invert a dictionary with non-string keys', () => {
          const originalDict = {1: 'apple', 2: 'banana', 3: 'apple'};
          const expected = {'apple': [1, 3], 'banana': 2};
          const result = invertDictionary(originalDict);
          expect(result).toEqual(expected);
      });
  });

  describe('test_mixed_types', () => {
      it('should correctly invert a dictionary with mixed key and value types', () => {
          const originalDict = {'a': 1, 2: 'two', 'three': 3};
          const expected = {1: 'a', 'two': 2, 3: 'three'};
          const result = invertDictionary(originalDict);
          expect(result).toEqual(expected);
      });
  });
});
