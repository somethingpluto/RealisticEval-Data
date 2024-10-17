describe('TestModExp', () => {
  it('test_case_1', () => {
    // Test with base = 2, exponent = 10, modulus = 1000
    expect(modExp(2, 10, 1000)).toBe(24);
  });

  it('test_case_2', () => {
    // Test with base = 3, exponent = 7, modulus = 50
    expect(modExp(3, 7, 50)).toBe(37);
  });

  it('test_case_3', () => {
    // Test with base = 5, exponent = 0, modulus = 13 (any number^0 = 1)
    expect(modExp(5, 0, 13)).toBe(1);
  });

  it('test_case_4', () => {
    // Test with base = 7, exponent = 5, modulus = 20
    expect(modExp(7, 5, 20)).toBe(7);  // 7^5 = 16807, 16807 % 20 = 7
  });

  it('test_case_5', () => {
    // Test with base = 10, exponent = 5, modulus = 6
    expect(modExp(10, 5, 6)).toBe(4);  // 10^5 = 100000, 100000 % 6 = 4
  });
});