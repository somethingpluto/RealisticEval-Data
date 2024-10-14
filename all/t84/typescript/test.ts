describe('findMinWindowSubstring', () => {
  it('should return an empty string when source is empty', () => {
    expect(findMinWindowSubstring("", "abc")).toBe("");
  });

  it('should return an empty string when target is empty', () => {
    expect(findMinWindowSubstring("abc", "")).toBe("");
  });

  it('should return an empty string when no valid window exists', () => {
    expect(findMinWindowSubstring("abcdef", "xyz")).toBe("");
  });

  it('should return the entire string when it is an exact match', () => {
    expect(findMinWindowSubstring("abcd", "abcd")).toBe("abcd");
  });

  it('should return BANC as the smallest window containing all characters of ABC', () => {
    expect(findMinWindowSubstring("ADOBECODEBANC", "ABC")).toBe("BANC");
  });
});