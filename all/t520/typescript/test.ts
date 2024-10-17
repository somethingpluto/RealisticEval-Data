describe('TestComputeOutputIndex', () => {
  it('test_standard_case', () => {
    /** Test with two standard positive integers. */
    const idx_1 = 3; // binary: 11
    const idx_2 = 5; // binary: 101
    const expected = 6; // 3 XOR 5 = 6
    const result = computeOutputIndex(idx_1, idx_2);
    expect(result).toBe(expected);
  });

  it('test_identical_indices', () => {
    /** Test with identical indices (should return 0). */
    const idx_1 = 7; // binary: 111
    const idx_2 = 7; // binary: 111
    const expected = 0; // 7 XOR 7 = 0
    const result = computeOutputIndex(idx_1, idx_2);
    expect(result).toBe(expected);
  });

  it('test_zero_index', () => {
    /** Test with one index as zero. */
    const idx_1 = 0; // binary: 0
    const idx_2 = 5; // binary: 101
    const expected = 5; // 0 XOR 5 = 5
    const result = computeOutputIndex(idx_1, idx_2);
    expect(result).toBe(expected);
  });

  it('test_large_numbers', () => {
    /** Test with large integer values. */
    const idx_1 = 1024; // binary: 10000000000
    const idx_2 = 2048; // binary: 100000000000
    const expected = 3072; // 1024 XOR 2048 = 3072
    const result = computeOutputIndex(idx_1, idx_2);
    expect(result).toBe(expected);
  });
});