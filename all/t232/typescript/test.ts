describe('convertHmsToMilliseconds', () => {
  it('should convert valid time strings to milliseconds', () => {
    expect(convertHmsToMilliseconds('1h')).toBe(3600000);
    expect(convertHmsToMilliseconds('20min')).toBe(1200000);
    expect(convertHmsToMilliseconds('30s')).toBe(30000);
    expect(convertHmsToMilliseconds('1h20min30s')).toBe(4830000);
  });

  it('should return null for invalid time strings', () => {
    expect(convertHmsToMilliseconds('invalid')).toBeNull();
    expect(convertHmsToMilliseconds('1hinvalid')).toBeNull();
    expect(convertHmsToMilliseconds('invalid20min')).toBeNull();
    expect(convertHmsToMilliseconds('1h20mininvalid')).toBeNull();
    expect(convertHmsToMilliseconds('1h20min30invalid')).toBeNull();
  });
});