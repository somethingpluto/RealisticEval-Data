describe('TestFlattenArray', () => {
  it('test a deeply nested array', () => {
      const nestedArray = [1, [2, [3, [4, [5]]]]];
      const expectedResult = [1, 2, 3, 4, 5];
      expect(flattenArray(nestedArray)).toEqual(expectedResult);
  });

  it('test an array with mixed types', () => {
      const mixedArray = ["a", ["b", 2, [true, [3.14]]], false];
      const expectedResult = ["a", "b", 2, true, 3.14, false];
      expect(flattenArray(mixedArray)).toEqual(expectedResult);
  });

  it('test an empty array', () => {
      const emptyArray = [];
      const expectedResult = [];
      expect(flattenArray(emptyArray)).toEqual(expectedResult);
  });

  it('test an array that includes empty subarrays', () => {
      const complexArray = [1, [], [2, [], 3], [4, [5, [], 6], 7], []];
      const expectedResult = [1, 2, 3, 4, 5, 6, 7];
      expect(flattenArray(complexArray)).toEqual(expectedResult);
  });

  it('test an array that has no nested structure', () => {
      const flatArray = [1, 2, 3, 4, 5];
      const expectedResult = [1, 2, 3, 4, 5];
      expect(flattenArray(flatArray)).toEqual(expectedResult);
  });
});