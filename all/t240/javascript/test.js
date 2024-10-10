describe('genTimeoutTimedelta', () => {
  it('should convert "1d 2h 3m 4s 500ms" to correct timedelta', () => {
    const result = genTimeoutTimedelta("1d 2h 3m 4s 500ms");
    expect(result).toEqual({
      days: 1,
      hours: 2,
      minutes: 3,
      seconds: 4,
      milliseconds: 500
    });
  });

  it('should handle negative values correctly', () => {
    const result = genTimeoutTimedelta("-1d -2h -3m -4s -500ms");
    expect(result).toEqual({
      days: -1,
      hours: -2,
      minutes: -3,
      seconds: -4,
      milliseconds: -500
    });
  });

  it('should handle fractional values correctly', () => {
    const result = genTimeoutTimedelta("0.5d 1.5h 2.5m 3.5s 4.5ms");
    expect(result).toEqual({
      days: 0.5,
      hours: 1.5,
      minutes: 2.5,
      seconds: 3.5,
      milliseconds: 4.5
    });
  });

  it('should throw error for invalid input', () => {
    expect(() => genTimeoutTimedelta("invalid_input")).toThrow();
  });
});