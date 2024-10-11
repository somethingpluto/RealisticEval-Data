describe('handleNestedData', () => {
  it('should convert nested data types correctly', () => {
    const input = {
      name: 'John',
      age: 30,
      address: {
        street: '123 Main St',
        city: 'Anytown',
        zip: Buffer.from([49, 50, 51]) // Example byte array
      },
      scores: [85, 90, 95],
      isActive: true
    };

    const expectedOutput = {
      name: 'John',
      age: 30,
      address: {
        street: '123 Main St',
        city: 'Anytown',
        zip: '123' // Converted from byte array to string
      },
      scores: [85, 90, 95],
      isActive: true
    };

    const result = handleNestedData(input);
    expect(result).toEqual(expectedOutput);
  });

  it('should handle edge cases correctly', () => {
    const input = {
      name: Buffer.from([74, 111, 110]), // Example byte array
      age: null,
      address: null,
      scores: [],
      isActive: undefined
    };

    const expectedOutput = {
      name: 'Jon', // Converted from byte array to string
      age: null,
      address: null,
      scores: [],
      isActive: undefined
    };

    const result = handleNestedData(input);
    expect(result).toEqual(expectedOutput);
  });
});