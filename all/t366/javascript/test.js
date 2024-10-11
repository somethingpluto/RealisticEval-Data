describe('extractTextFromWord', () => {
  it('should extract text from a .docx file', () => {
    const filePath = 'path/to/your/file.docx';
    const expectedText = 'Mocked extracted text from path/to/your/file.docx';

    const result = extractTextFromWord(filePath);

    expect(result).toBe(expectedText);
  });
});