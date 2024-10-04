import unittest


class TestExtractTextFromPDF(unittest.TestCase):
    def test_empty_file(self):
        pdf_path = "./testcase1_empty.pdf"
        expected = " \n"
        output = extract_text_from_pdf(pdf_path)
        self.assertEqual(output, expected)

    def test_normal_file(self):
        pdf_path = "./testcase2_normal.pdf"
        expected = "Hello World  \n"
        output = extract_text_from_pdf(pdf_path)
        self.assertEqual(output, expected)
