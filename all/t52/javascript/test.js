describe('renameFilePath', () => {
  it('should replace colons in the filename with underscores', () => {
    const inputPath = 'C:\\Users\\Username\\Documents\\example:file.txt';
    const expectedOutput = 'C:\\Users\\Username\\Documents\\example_file.txt';

    expect(renameFilePath(inputPath)).toBe(expectedOutput);
  });

  it('should not modify paths without colons', () => {
    const inputPath = 'C:\\Users\\Username\\Documents\\example_file.txt';
    const expectedOutput = 'C:\\Users\\Username\\Documents\\example_file.txt';

    expect(renameFilePath(inputPath)).toBe(expectedOutput);
  });

  it('should handle paths with multiple colons', () => {
    const inputPath = 'C:\\Users\\Username\\Documents\\example:file:name.txt';
    const expectedOutput = 'C:\\Users\\Username\\Documents\\example_file_name.txt';

    expect(renameFilePath(inputPath)).toBe(expectedOutput);
  });
});