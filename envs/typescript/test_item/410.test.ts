// ... (previous code for context)

function checkXorSum(combination: number[][], requiredXorSums: number[]): boolean {
    if (combination.length === 0 || combination[0].length !== requiredXorSums.length) {
        throw new Error('Invalid input: combination array is empty or mismatched lengths.');
    }

    const xorSums: number[] = requiredXorSums.slice();
    for (let row = 0; row < combination.length; row++) {
        for (let col = 0; col < combination[row].length; col++) {
            xorSums[col] ^= combination[row][col];
        }
    }

    return xorSums.every(sum => sum === 0);
}

// ... (rest of the code)
describe('TestCheckXorSum', () => {
  /**
   * Test with combination values that produce the expected XOR sums.
   */
  it('test correct XOR sums', () => {
      const combination: number[][] = [
          [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
          [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
      ];
      expect(checkXorSum(combination)).toBe(false);
  });

  /**
   * Test with combination values that do not meet the expected XOR sums.
   */
  it('test incorrect XOR sums', () => {
      const combination: number[][] = [
          [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
          [0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00]
      ];
      expect(checkXorSum(combination)).toBe(false);
  });

  /**
   * Test with a combination where all values are zero.
   */
  it('test edge case with zero', () => {
      const combination: number[][] = [[0, 0, 0, 0, 0, 0, 0, 0]];
      expect(checkXorSum(combination)).toBe(false);
  });

  /**
   * Test with large numbers in the combination.
   */
  it('test large numbers', () => {
      const combination: number[][] = [
          [0x6b000000, 0x00000000, 0x00000012, 0x00000000, 0x76000000, 0x00000000, 0x00000000, 0x00000000],
          [0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000]
      ];
      expect(checkXorSum(combination)).toBe(false);
  });

  /**
   * Test with a combination that contains multiple rows.
   */
  it('test multiple rows', () => {
      const combination: number[][] = [
          [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
          [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
          [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00]
      ];
      expect(checkXorSum(combination)).toBe(true);
  });
});
