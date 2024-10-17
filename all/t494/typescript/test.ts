describe('TestCleanDictionary', () => {
  it('test valid strings', () => {
    const inputDict = {
      'key1': 'valid string',
      'key2': 'another valid string'
    };
    const expectedOutput = {
      'key1': 'valid string',
      'key2': 'another valid string'
    };
    expect(cleanObject(inputDict)).toEqual(expectedOutput);
  });

  it('test None and NaN values', () => {
    const inputDict = {
      'key1': null,
      'key3': 'valid string'
    };
    const expectedOutput = {
      'key3': 'valid string'
    };
    expect(cleanObject(inputDict)).toEqual(expectedOutput);
  });

  it('test whitespace strings', () => {
    const inputDict = {
      'key1': '   ',
      'key2': '',
      'key3': 'valid'
    };
    const expectedOutput = {
      'key3': 'valid'
    };
    expect(cleanObject(inputDict)).toEqual(expectedOutput);
  });

  it('test empty dictionary', () => {
    const inputDict = {};
    const expectedOutput = {};
    expect(cleanObject(inputDict)).toEqual(expectedOutput);
  });
});