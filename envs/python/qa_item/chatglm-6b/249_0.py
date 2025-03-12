
import PyPDF2

def extract_text_from_pdf(file_path: str) -> str:
    # Open the PDF file
    with open(file_path, 'rb') as pdf_file:
        # Create a PDF object
        pdf = PyPDF2.PdfFileReader(pdf_file)
        # Get the text from the PDF
        extracted_text = pdf.extractText()
        # Close the PDF file
        pdf.close()
        
    return extracted_text

extracted_text = extract_text_from_pdf('example.pdf')
print(extracted_text)

import unittest


class TestExtractTextFromPDF(unittest.TestCase):
    def test_empty_file(self):
        pdf_path = r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t249\testcase01.pdf"
        expected = " \n"
        output = extract_text_from_pdf(pdf_path)
        self.assertEqual(output, expected)

    def test_normal_file(self):
        pdf_path = r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t249\testcase02.pdf"
        expected = "11111  \n"
        output = extract_text_from_pdf(pdf_path)
        self.assertEqual(output, expected)

    def test_more_text_file(self):
        pdf_path = r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t249\testcase03.pdf"
        expected = "11111  \n22222  \n33333  \n44444  \n"
        output = extract_text_from_pdf(pdf_path)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()