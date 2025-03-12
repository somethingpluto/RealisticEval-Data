import PyPDF2

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a given PDF file.

    Args:
    file_path (str): The path to the PDF file from which to extract text.

    Returns:
    str: The extracted text from the PDF.
    """
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
    except Exception as e:
        print(f"An error occurred while extracting text: {e}")
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