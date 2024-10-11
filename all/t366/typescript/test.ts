describe('extractTextFromWord', () => {
  it('should extract text from a valid .docx file', async () => {
    const filePath = path.join(__dirname, 'test.docx'); // Path to your test .docx file
    const expectedText = 'Expected text content'; // Replace with the actual expected text content

    try {
      const result = await extractTextFromWord(filePath);
      expect(result).toBe(expectedText);
    } catch (error) {
      fail(`Failed to extract text from ${filePath}: ${error}`);
    }
  });

  it('should handle non-existent file', async () => {
    const nonExistentFilePath = path.join(__dirname, 'non-existent-file.docx');

    try {
      await extractTextFromWord(nonExistentFilePath);
      fail('Should throw an error when the file does not exist');
    } catch (error) {
      expect(error.message).toContain('File does not exist');
    }
  });
});