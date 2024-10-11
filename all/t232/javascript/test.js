describe('convertHmsToMilliseconds', () => {
  it('should convert "1h20min30s" to milliseconds', () => {
    expect(convertHmsToMilliseconds('1h20min30s')).toBe(5400000);
  });

  it('should convert "2h" to milliseconds', () => {
    expect(convertHmsToMilliseconds('2h')).toBe(7200000);
  });

  it('should convert "30min" to milliseconds', () => {
    expect(convertHmsToMilliseconds('30min')).toBe(1800000);
  });

  it('should convert "45s" to milliseconds', () => {
    expect(convertHmsToMilliseconds('45s')).toBe(45000);
  });

  it('should return null for invalid input', () => {
    expect(convertHmsToMilliseconds('invalid_input')).toBeNull();
    expect(convertHmsToMilliseconds('1h20min')).toBeNull();
    expect(convertHmsToMilliseconds('h20min30s')).toBeNull();
    expect(convertHmsToMilliseconds('1h20s')).toBeNull();
    expect(convertHmsToMilliseconds('1h20min30')).toBeNull();
  });
});