import { PDFDocument } from 'pdf-lib';
import fs from 'fs';

/**
 * Extracts text from a given PDF file.
 *
 * @param filePath - The path to the PDF file from which to extract text.
 * @returns A promise that resolves to the extracted text from the PDF.
 */
async function extractTextFromPdf(filePath: string): Promise<string> {
    try {
        const fileStream = fs.createReadStream(filePath);
        const pdfDoc = await PDFDocument.load(fileStream);
        const text = pdfDoc.getText();
        return text;
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
