def extract_paragraphs_and_lines(text: str):
    """
    Extracts paragraphs and lines from the given text.The paragraphs end with \n\n The line end with \n
    """
    paragraphs = []
    lines = []
    current_paragraph = ""

    for line in text.split("\n"):
        if line == "":
            if current_paragraph:
                paragraphs.append(current_paragraph)
                current_paragraph = ""
        else:
            current_paragraph += line + "\n"

    if current_paragraph:
        paragraphs.append(current_paragraph)

    for paragraph in paragraphs:
        lines.extend(paragraph.split("\n"))

    return {'paragraphs': paragraphs, 'lines': lines}
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