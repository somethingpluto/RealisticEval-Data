// ... (previous code for context)
function cleanObject(inputObj: Record<string, any>): Record<string, any> {
  const isValid = (value: any): boolean => {
    if (typeof value === 'string') {
      return value.trim() !== '';
    }
    return value !== null && !isNaN(value);
  };

  const cleanedObj: Record<string, any> = {};
  for (const key in inputObj) {
    if (inputObj.hasOwnProperty(key) && isValid(inputObj[key])) {
      cleanedObj[key] = inputObj[key];
    }
  }
  return cleanedObj;
}
// ... (continuation of the code if necessary)
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
