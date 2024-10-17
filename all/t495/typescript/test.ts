describe('TestFilterContentWithContext', () => {
  it('test_single_keyword_match', () => {
    // Test a single keyword match with context lines.
    const content = `Line one.
    This line contains a keyword.
    Line three.`;
    const keywords = ['keyword'];
    const expectedOutput = `Line one.
    This line contains a keyword.
    Line three.`;
    const result = filterContentWithContext(content, keywords, 1, 1);
    expect(result.trim()).toEqual(expectedOutput.trim());
  });

  it('test_no_keyword_match', () => {
    // Test when no keywords match.
    const content = `Line one.
    Line two.
    Line three.`;
    const keywords = ['missing'];
    const expectedOutput = '';
    const result = filterContentWithContext(content, keywords, 1, 1);
    expect(result.trim()).toEqual(expectedOutput);
  });

  it('test_lines_before_and_after', () => {
    // Test functionality with specified lines before and after.
    const content = `Line one.
    This line contains a keyword.
    Line three.
    Line four.
    Line five.`;
    const keywords = ['keyword'];
    const expectedOutput = `Line one.
    This line contains a keyword.
    Line three.`;
    const result = filterContentWithContext(content, keywords, 1, 1);
    expect(result.trim()).toEqual(expectedOutput.trim());
  });
});