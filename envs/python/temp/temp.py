def save_content_to_file(content: str, path: str) -> None:
    """
    Saves the provided content to a specified file after cleaning up
    redundant whitespace.

    Args:
        content (str): The text content to be saved to the file.
        path (str): The file path where the content will be saved.

    Returns:
        None
    """
    # Remove redundant whitespace from the content.
    # Split the content into lines, strip leading/trailing whitespace,
    # and filter out empty lines.
    content = '\n'.join(line.strip() for line in content.splitlines() if line.strip())

    # Replace multiple spaces with a single space.
    content = ' '.join(content.split())

    # Write the cleaned content to the specified file.
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

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