// ... (previous code for context)

function invertDictionary(originalDict: Record<string, string | string[]>): Record<string, string | string[]> {
  const invertedDict: Record<string, string | string[]> = {};

  for (const key in originalDict) {
    if (originalDict.hasOwnProperty(key)) {
      const value = originalDict[key];
      if (invertedDict[value]) {
        if (Array.isArray(invertedDict[value])) {
          invertedDict[value].push(key);
        } else {
          invertedDict[value] = [invertedDict[value], key];
        }
      } else {
        invertedDict[value] = key;
      }
    }
  }

  return invertedDict;
}

// ... (rest of the code)
describe('TestInvertDictionary', () => {
    it('test_normal_dictionary', () => {
        /** Test inversion of a dictionary without duplicate values. */
        const originalDict = { 'a': 1, 'b': 2, 'c': 3 };
        const expected = { 1: 'a', 2: 'b', 3: 'c' };
        const result = invertDictionary(originalDict);
        expect(result).toEqual(expected);
    });

    it('test_dictionary_with_duplicates', () => {
        /** Test inversion of a dictionary with duplicate values. */
        const originalDict = { 'a': 1, 'b': 1, 'c': 2 };
        const expected = { 1: ['a', 'b'], 2: 'c' };
        const result = invertDictionary(originalDict);
        expect(result).toEqual(expected);
    });

    it('test_empty_dictionary', () => {
        /** Test inversion of an empty dictionary. */
        const originalDict = {};
        const expected = {};
        const result = invertDictionary(originalDict);
        expect(result).toEqual(expected);
    });

    it('test_non_string_keys', () => {
        /** Test inversion of a dictionary with non-string keys. */
        const originalDict = { 1: 'apple', 2: 'banana', 3: 'apple' };
        const expected = { 'apple': [1, 3], 'banana': 2 };
        const result = invertDictionary(originalDict);
        expect(result).toEqual(expected);
    });

    it('test_mixed_types', () => {
        /** Test inversion of a dictionary with mixed key and value types. */
        const originalDict = { 'a': 1, 2: 'two', 'three': 3 };
        const expected = { 1: 'a', 'two': 2, 3: 'three' };
        const result = invertDictionary(originalDict);
        expect(result).toEqual(expected);
    });
});
