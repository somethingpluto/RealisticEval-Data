import fitz  # PyPDF2's fork with additional functionality

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a given PDF file.

    Args:
    file_path (str): The path to the PDF file from which to extract text.

    Returns:
    str: The extracted text from the PDF.
    """

    pdf = fitz.open(file_path)
    text = ""

    for page in pdf:
        text += page.get_text()

    return text
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