npm install pdfjs-dist
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
