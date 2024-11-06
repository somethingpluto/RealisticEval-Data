describe('TestShearTransformation', () => {
  /**
   * Test with zero shear factor which should return the original matrix unchanged.
   */
  test('testIdentityShear', () => {
    const matrix: number[][] = [[1, 2], [3, 4]];
    const shearFactor: number = 0;
    const expectedOutput: number[][] = [[1, 2], [3, 4]];
    const result = applyShearX(matrix, shearFactor);
    expect(result).toEqual(expectedOutput);
  });

  /**
   * Test with a positive shear factor.
   */
  test('testPositiveShear', () => {
    const matrix: number[][] = [[1, 2], [3, 4]];
    const shearFactor: number = 1;
    const expectedOutput: number[][] = [[1, 3], [3, 7]];
    const result = applyShearX(matrix, shearFactor);
    expect(result).toEqual(expectedOutput);
  });

  /**
   * Test with a negative shear factor.
   */
  test('testNegativeShear', () => {
    const matrix: number[][] = [[1, 2], [3, 4]];
    const shearFactor: number = -1;
    const expectedOutput: number[][] = [[1, 1], [3, 1]];
    const result = applyShearX(matrix, shearFactor);
    expect(result).toEqual(expectedOutput);
  });

  /**
   * Test with a high shear factor to see how the matrix adapts to extreme transformations.
   */
  test('testHighShearFactor', () => {
    const matrix: number[][] = [[1, 1], [1, 1]];
    const shearFactor: number = 10;
    const expectedOutput: number[][] = [[1, 11], [1, 11]];
    const result = applyShearX(matrix, shearFactor);
    expect(result).toEqual(expectedOutput);
  });
});