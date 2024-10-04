import os
import unittest


class TestMarkdownProcessor(unittest.TestCase):
    def setUp(self):
        """Setup test case data."""
        # Sample Markdown content for testing
        self.test_cases = {
            "test_case_2.md": "This is _italic_ text.",
            "test_case_3.md": "This is **bold** and _italic_ text.",
            "test_case_5.md": "This text has no special formatting.",
            "test_case_6.md": "*Asterisks at the start* and end*.",
            "test_case_7.md": "Mixed *text with **multiple** asterisks*."
        }

        # Expected outputs after processing
        self.expected_outputs = {
            "test_case_1.md": "This is **bold** text.",
            "test_case_2.md": "This is _italic_ text.",
            "test_case_3.md": "This is **bold** and _italic_ text.",
            "test_case_4.md": "This is **bold and _italic_** text.",
            "test_case_5.md": "This text has no special formatting.",
            "test_case_6.md": "*Asterisks at the start* and end*.",
            "test_case_7.md": "Mixed *text with **multiple** asterisks*."
        }

    def write_temp_file(self, filename, content):
        """Helper method to write content to a temporary test file."""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

    def test_markdown_processing(self):
        """Run all test cases."""
        for filename, content in self.test_cases.items():
            self.write_temp_file(filename, content)
            processed_content = process_markdown_file(filename)
            expected_content = self.expected_outputs[filename]
            self.assertEqual(processed_content, expected_content)

    def tearDown(self):
        """Cleanup temporary test files after tests."""
        for filename in self.test_cases.keys():
            try:
                os.remove(filename)
            except FileNotFoundError:
                pass
