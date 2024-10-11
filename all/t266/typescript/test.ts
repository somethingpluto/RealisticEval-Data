describe('handle_nested_data', () => {
  test('should handle nested dictionaries correctly', () => {
    const input = {
      key1: 'value1',
      key2: {
        subKey1: 'subValue1',
        subKey2: 123,
      },
    };

    const expectedOutput = {
      key1: 'value1',
      key2: {
        subKey1: 'subValue1',
        subKey2: 123,
      },
    };

    expect(handle_nested_data(input)).toEqual(expectedOutput);
  });

  test('should handle nested lists correctly', () => {
    const input = {
      key1: 'value1',
      key2: [
        {
          subKey1: 'subValue1',
          subKey2: 123,
        },
        {
          subKey1: 'subValue2',
          subKey2: 456,
        },
      ],
    };

    const expectedOutput = {
      key1: 'value1',
      key2: [
        {
          subKey1: 'subValue1',
          subKey2: 123,
        },
        {
          subKey1: 'subValue2',
          subKey2: 456,
        },
      ],
    };

    expect(handle_nested_data(input)).toEqual(expectedOutput);
  });

  test('should handle nested enumerations correctly', () => {
    const input = {
      key1: 'value1',
      key2: ['item1', 'item2'],
    };

    const expectedOutput = {
      key1: 'value1',
      key2: ['item1', 'item2'],
    };

    expect(handle_nested_data(input)).toEqual(expectedOutput);
  });

  test('should decode bytes to UTF-8 strings', () => {
    const input = {
      key1: Buffer.from('value1').toString('utf-8'),
      key2: {
        subKey1: Buffer.from('subValue1').toString('utf-8'),
        subKey2: 123,
      },
    };

    const expectedOutput = {
      key1: 'value1',
      key2: {
        subKey1: 'subValue1',
        subKey2: 123,
      },
    };

    expect(handle_nested_data(input)).toEqual(expectedOutput);
  });

  test('should convert numbers to integers or floating point numbers', () => {
    const input = {
      key1: 'value1',
      key2: {
        subKey1: '123',
        subKey2: '456.78',
      },
    };

    const expectedOutput = {
      key1: 'value1',
      key2: {
        subKey1: 123,
        subKey2: 456.78,
      },
    };

    expect(handle_nested_data(input)).toEqual(expectedOutput);
  });
});