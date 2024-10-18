describe('TestLookAndSay', () => {
  it('should replicate a single digit correctly', () => {
    expect(lookAndSay('1')).toBe('11');
  });

  it('should handle a sequence of the same digits', () => {
    expect(lookAndSay('111')).toBe('31');
  });

  it('should handle a sequence with different digits', () => {
    expect(lookAndSay('1211')).toBe('111221');
  });

  it('should handle a more complex sequence', () => {
    expect(lookAndSay('312211')).toBe('13112221');
  });
});