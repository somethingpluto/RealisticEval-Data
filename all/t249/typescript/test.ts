describe('extract_text_from_pdf', () => {
  it('should extract text from a PDF file', async () => {
    const filePath = 'path/to/your/pdf/file.pdf'; // Replace with the actual path to your PDF file

    // Read the PDF file
    const dataBuffer = fs.readFileSync(filePath);

    // Parse the PDF file
    const data = await parse(dataBuffer);

    // Check if the extracted text is not empty
    expect(data.text).not.toBe('');
  });

  it('should handle an empty PDF file', async () => {
    const filePath = 'path/to/your/empty/pdf/file.pdf'; // Replace with the actual path to your empty PDF file

    // Read the PDF file
    const dataBuffer = fs.readFileSync(filePath);

    // Parse the PDF file
    const data = await parse(dataBuffer);

    // Check if the extracted text is empty
    expect(data.text).toBe('');
  });
});