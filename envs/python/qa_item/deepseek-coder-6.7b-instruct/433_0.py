def extract_paragraphs_and_lines(text: str):
    """
    Extracts paragraphs and lines from the given text. Paragraphs end with \n\n and lines end with \n.

    Args:
        text (str): The input text from which paragraphs and lines will be extracted.

    Returns:
        dict: A dictionary containing:
            - 'paragraphs': A list of paragraphs extracted from the text.
            - 'lines': A list of lines extracted from the text.
    """
    paragraphs = text.split('\n\n')
    lines = [line for paragraph in paragraphs for line in paragraph.split('\n') if line.strip()]
    
    return {
        'paragraphs': paragraphs,
        'lines': lines
    }
import unittest


class TestExtractParagraphsAndLines(unittest.TestCase):

    def test_single_paragraph(self):
        input_text = "This is a single paragraph."
        expected_output = {
            'paragraphs': ["This is a single paragraph."],
            'lines': ["This is a single paragraph."]
        }
        self.assertEqual(extract_paragraphs_and_lines(input_text), expected_output)

    def test_multiple_paragraphs(self):
        input_text = "First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line."
        expected_output = {
            'paragraphs': [
                "First paragraph.\nThis is the second line.",
                "Second paragraph.\nAnother line."
            ],
            'lines': [
                "First paragraph.",
                "This is the second line.",
                "Second paragraph.",
                "Another line."
            ]
        }
        self.assertEqual(extract_paragraphs_and_lines(input_text), expected_output)

    def test_leading_and_trailing_whitespace(self):
        input_text = "   This paragraph has leading whitespace.\nAnd a line after.\n\n   This one has trailing whitespace.   "
        expected_output = {
            'paragraphs': [
                "This paragraph has leading whitespace.\nAnd a line after.",
                "This one has trailing whitespace."
            ],
            'lines': [
                "This paragraph has leading whitespace.",
                "And a line after.",
                "This one has trailing whitespace."
            ]
        }
        self.assertEqual(extract_paragraphs_and_lines(input_text), expected_output)

    def test_empty_string(self):
        input_text = ""
        expected_output = {
            'paragraphs': [],
            'lines': []
        }
        self.assertEqual(extract_paragraphs_and_lines(input_text), expected_output)

    def test_multiple_empty_paragraphs(self):
        input_text = "\n\n\n"
        expected_output = {
            'paragraphs': [],
            'lines': []
        }
        self.assertEqual(extract_paragraphs_and_lines(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()