describe('invertDictionary', () => {
  it('inverts a simple dictionary', () => {
    const input = { 'a': 1, 'b': 2 };
    const expectedOutput = { '1': ['a'], '2': ['b'] };
    expect(invertDictionary(input)).toEqual(expectedOutput);
  });

  it('handles dictionaries with duplicate values', () => {
    const input = { 'a': 1, 'b': 1, 'c': 2 };
    const expectedOutput = { '1': ['a', 'b'], '2': ['c'] };
    expect(invertDictionary(input)).toEqual(expectedOutput);
  });

  it('returns an empty dictionary for an empty input dictionary', () => {
    const input = {};
    const expectedOutput = {};
    expect(invertDictionary(input)).toEqual(expectedOutput);
  });
});