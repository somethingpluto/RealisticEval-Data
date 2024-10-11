describe('Eight Queens Problem', () => {
  it('should return a valid solution when called', () => {
    const expectedOutput = [
      '. . Q . . . . .',
      '. . . . Q . . .',
      '. Q . . . . . .',
      '. . . . . . . Q',
      '. . . . . Q . .',
      '. . . Q . . . .',
      '. . . . . . Q .',
      'Q . . . . . . .'
    ];

    // Call the function and store the result
    const result = eightQueens();

    // Check if the result matches the expected output
    expect(result).toEqual(expectedOutput);
  });
});