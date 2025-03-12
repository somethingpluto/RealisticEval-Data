def save_content_to_file(content: str, path: str) -> None:
    with open(path, 'w') as file:
        file.write(content.strip())
import os
import unittest


class TestSaveContentToFile(unittest.TestCase):

    def setUp(self):
        """Set up a temporary file path for testing."""
        self.test_file_path = 'test_output.txt'

    def tearDown(self):
        """Clean up the test file after each test."""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_basic_content(self):
        """Test with basic content and check if it saves correctly."""
        content = "Hello,  World!  "
        expected = "Hello, World!"
        save_content_to_file(content, self.test_file_path)
        with open(self.test_file_path, 'r', encoding='utf-8') as file:
            result = file.read().strip()
        self.assertEqual(result, expected)

    def test_multiple_spaces_and_empty_lines(self):
        """Test handling of multiple spaces and empty lines."""
        content = """

        This is a    test.

        Another line.      
        """
        expected = "This is a test. Another line."
        save_content_to_file(content, self.test_file_path)
        with open(self.test_file_path, 'r', encoding='utf-8') as file:
            result = file.read().strip()
        self.assertEqual(result, expected)

    def test_only_whitespace(self):
        """Test if only whitespace is handled correctly."""
        content = "    \n  \n   "
        expected = ""
        save_content_to_file(content, self.test_file_path)
        with open(self.test_file_path, 'r', encoding='utf-8') as file:
            result = file.read().strip()
        self.assertEqual(result, expected)

    def test_empty_content(self):
        """Test if empty content is saved correctly."""
        content = ""
        expected = ""
        save_content_to_file(content, self.test_file_path)
        with open(self.test_file_path, 'r', encoding='utf-8') as file:
            result = file.read().strip()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()