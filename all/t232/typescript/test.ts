describe('convertHmsToMilliseconds', () => {
  test('should convert valid time strings to milliseconds', () => {
    expect(convertHmsToMilliseconds('1h')).toBe(3600000);
    expect(convertHmsToMilliseconds('20min')).toBe(1200000);
    expect(convertHmsToMilliseconds('30s')).toBe(30000);
    expect(convertHmsToMilliseconds('1h20min30s')).toBe(4830000);
  })
});