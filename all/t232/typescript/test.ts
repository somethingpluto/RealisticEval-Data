describe('TestConvertHmsToMilliseconds', () => {
  it('should convert 1h20min30s to 4830000 milliseconds', () => {
    expect(convertHmsToMilliseconds('1h20min30s')).toBe(4830000);
  });

  it('should convert 30s to 30000 milliseconds', () => {
    expect(convertHmsToMilliseconds('30s')).toBe(30000);
  });

  it('should return null for invalid time format', () => {
    expect(convertHmsToMilliseconds('1hour20minutes')).toBeNull();
  });

  it('should convert 23h59min59s to 86399000 milliseconds', () => {
    expect(convertHmsToMilliseconds('23h59min59s')).toBe(86399000);
  });

  it('should correctly convert 24h1min to 86460000 milliseconds', () => {
    expect(convertHmsToMilliseconds('24h1min')).toBe(86460000);
  });
});