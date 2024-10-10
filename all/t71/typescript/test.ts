describe('readColumns', () => {
  it('should read numerical columns from a file starting from the line after the last line containing \'/\'', async () => {
    const fileName = 'path/to/your/file.txt'; // Replace with your actual file path
    const mockFileContent = `
      line1
      line2/
      line3
      1 2 3
      4 5 6
    `;

    // Create a temporary file for testing
    const tempFilePath = '/tmp/tempfile.txt';
    fs.writeFileSync(tempFilePath, mockFileContent);

    try {
      const result = await readColumns(tempFilePath);
      expect(result).toEqual([
        [1, 2, 3],
        [4, 5, 6]
      ]);
    } finally {
      // Clean up the temporary file
      fs.unlinkSync(tempFilePath);
    }
  });

  it('should throw an error if the file does not contain any \'/\' character', async () => {
    const fileName = 'path/to/your/file.txt'; // Replace with your actual file path
    const mockFileContent = `
      line1
      line2
      line3
      1 2 3
      4 5 6
    `;

    // Create a temporary file for testing
    const tempFilePath = '/tmp/tempfile.txt';
    fs.writeFileSync(tempFilePath, mockFileContent);

    try {
      await readColumns(tempFilePath);
      fail('Expected an error to be thrown');
    } catch (error) {
      expect(error.message).toBe('The file does not contain any \'=\' character.');
    } finally {
      // Clean up the temporary file
      fs.unlinkSync(tempFilePath);
    }
  });
});