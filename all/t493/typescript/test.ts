describe('wrapContentGenerator', () => {

  it('should handle a single line of content within default width', () => {
    const result = Array.from(wrapContentGenerator("Hello, world!"));
    expect(result).toEqual(["Hello, world!"]);
  });

  it('should handle multiple lines of content each fitting within default width', () => {
    const content = "Hello\nWorld\nPython";
    const result = Array.from(wrapContentGenerator(content));
    expect(result).toEqual(["Hello", "World", "Python"]);
  });

  it('should handle a single long line that exceeds the default width', () => {
    const content = "This is a very long line that should definitely be wrapped around the default width of 80 characters.";
    const result = Array.from(wrapContentGenerator(content));
    const longestLine = result.reduce((max, line) => line.length > max.length ? line : max, "");
    expect(longestLine.length).toBeLessThanOrEqual(80);
  });

  it('should handle a custom width', () => {
    const content = "This is a test for custom width setting.";
    const result = Array.from(wrapContentGenerator(content, 10));
    expect(result.every(line => line.length <= 10)).toBe(true);
  });

  it('should handle content that contains only whitespace characters', () => {
    const result = Array.from(wrapContentGenerator("     "));
    expect(result).toEqual(["\n"]);
  });
});