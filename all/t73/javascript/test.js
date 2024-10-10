describe('dictOfListsToListOfDicts', () => {
  it('should convert a dictionary of lists into a list of dictionaries', () => {
    const dictOfLists = {
      a: [1, 2, 3],
      b: ['x', 'y', 'z'],
      c: [true, false, true]
    };

    const expectedResult = [
      { a: 1, b: 'x', c: true },
      { a: 2, b: 'y', c: false },
      { a: 3, b: 'z', c: true }
    ];

    expect(dictOfListsToListOfDicts(dictOfLists)).toEqual(expectedResult);
  });

  it('should handle empty input correctly', () => {
    const dictOfLists = {};

    const expectedResult = [];

    expect(dictOfListsToListOfDicts(dictOfLists)).toEqual(expectedResult);
  });

  it('should handle single key-value pair correctly', () => {
    const dictOfLists = {
      a: [1]
    };

    const expectedResult = [{ a: 1 }];

    expect(dictOfListsToListOfDicts(dictOfLists)).toEqual(expectedResult);
  });
});