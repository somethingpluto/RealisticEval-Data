describe('dictOfListsToListOfDicts', () => {
  it('should convert a dictionary of lists into a list of dictionaries', () => {
    const dictOfLists = {
      'a': [1, 2],
      'b': ['x', 'y']
    };

    const expectedOutput = [
      {'a': 1, 'b': 'x'},
      {'a': 2, 'b': 'y'}
    ];

    // Assuming the function dictOfListsToListOfDicts exists and works as described
    const output = dictOfListsToListOfDicts(dictOfLists);

    expect(output).toEqual(expectedOutput);
  });
});