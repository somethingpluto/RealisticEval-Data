const PDFJS = require('pdfjs-dist');

/**
 * Extracts text from a given PDF file.
 *
 * @param {string} fileUrl - The URL/path to the PDF file from which to extract text.
 * @returns {Promise<string>} A promise that resolves to the extracted text from the PDF.
 */
async function extractTextFromPdf(fileUrl) {
    try {
        // Fetch the PDF file
        const loadingTask = PDFJS.getDocument(fileUrl);
        const pdfDocument = await loadingTask.promise;

        // Initialize an array to hold the text from each page
        let extractedText = '';

        // Iterate through each page
        for (let pageNumber = 1; pageNumber <= pdfDocument.numPages; pageNumber++) {
            const page = await pdfDocument.getPage(pageNumber);
            const textContent = await page.getTextContent();

            // Extract text from the page
            const pageText = textContent.items.map(item => item.str).join(' ');
            extractedText += pageText + ' ';
        }

        return extractedText.trim();
    } catch (error) {
        throw new Error(`Failed to extract text from PDF: ${error.message}`);
    }
}
describe('TestExtractTextFromPDF', () => {
  it('should handle an empty file correctly', async () => {
      const pdfPath = 'E:/code/code_back/python_project/RealisticEval-Data/envs/python/test_case/t249/testcase01.pdf';
      const expected = ' \n';
      const output = await extractTextFromPdf(pdfPath);
      expect(output).toEqual(expected);
  });

  it('should handle a normal file correctly', async () => {
      const pdfPath = 'E:/code/code_back/python_project/RealisticEval-Data/envs/python/test_case/t249/testcase02.pdf';
      const expected = '11111  \n';
      const output = await extractTextFromPdf(pdfPath);
      expect(output).toEqual(expected);
  });

  it('should handle a file with more text correctly', async () => {
      const pdfPath = 'E:/code/code_back/python_project/RealisticEval-Data/envs/python/test_case/t249/testcase03.pdf';
      const expected = '11111  \n22222  \n33333  \n44444  \n';
      const output = await extractTextFromPdf(pdfPath);
      expect(output).toEqual(expected);
  });
});
