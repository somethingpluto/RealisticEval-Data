describe('PDF Extractor', () => {
  it('should extract text from a PDF file', async () => {
    // Assuming 'test.pdf' is in the same directory as the test file
    const filePath = 'test.pdf';
    const expectedText = "This is a sample text.";

    const dataBuffer = fs.readFileSync(filePath);

    try {
      const data = await extractText(dataBuffer);
      expect(data.trim()).toBe(expectedText);
    } catch (error) {
      fail(error);
    }
  });
});