describe('renameFilePath', () => {
  it('replaces colons in the filename with underscores', () => {
    const inputPath = 'C:\\Users\\Username\\Documents\\file:name.txt';
    const expectedOutput = 'C:\\Users\\Username\\Documents\\file_name.txt';
    expect(renameFilePath(inputPath)).toBe(expectedOutput);
  });

  it('does not modify paths without colons', () => {
    const inputPath = 'C:\\Users\\Username\\Documents\\filename.txt';
    const expectedOutput = 'C:\\Users\\Username\\Documents\\filename.txt';
    expect(renameFilePath(inputPath)).toBe(expectedOutput);
  });

  it('handles multiple colons in the filename', () => {
    const inputPath = 'C:\\Users\\Username\\Documents\\file::name.txt';
    const expectedOutput = 'C:\\Users\\Username\\Documents\\file__name.txt';
    expect(renameFilePath(inputPath)).toBe(expectedOutput);
  });

  it('works with relative paths', () => {
    const inputPath = 'relative:path\\to\\file:name.txt';
    const expectedOutput = 'relative:path\\to\\file_name.txt';
    expect(renameFilePath(inputPath)).toBe(expectedOutput);
  });
});