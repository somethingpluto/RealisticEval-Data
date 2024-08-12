import unittest
import os

class TestPrependToEachLine(unittest.TestCase):
    def setUp(self):
        """Create a temporary file for testing."""
        self.test_file_path = "test_file.txt"
        with open(self.test_file_path, 'w') as f:
            f.write("Line 1\nLine 2\nLine 3")

    def tearDown(self):
        """Remove the temporary file after testing."""
        os.remove(self.test_file_path)

    def test_prepend_string(self):
        """Test appending a simple string to the beginning of each line."""
        prepend_to_each_line(self.test_file_path, "Test: ")
        with open(self.test_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(lines, ["Test: Line 1\n", "Test: Line 2\n", "Test: Line 3"])

    def test_prepend_empty_string(self):
        """Test appending an empty string."""
        prepend_to_each_line(self.test_file_path, "")
        with open(self.test_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(lines, ["Line 1\n", "Line 2\n", "Line 3"])

    def test_prepend_special_characters(self):
        """Test appending special characters to the beginning of each line."""
        prepend_to_each_line(self.test_file_path, "#$%^&* ")
        with open(self.test_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(lines, ["#$%^&* Line 1\n", "#$%^&* Line 2\n", "#$%^&* Line 3"])

    def test_prepend_numeric_string(self):
        """Test appending numeric string to the beginning of each line."""
        prepend_to_each_line(self.test_file_path, "123 ")
        with open(self.test_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(lines, ["123 Line 1\n", "123 Line 2\n", "123 Line 3"])

    def test_file_not_found(self):
        """Test the response when the file does not exist."""
        with self.assertRaises(FileNotFoundError):
            prepend_to_each_line("non_existent_file.txt", "Test: ")
def prepend_to_each_line(file_path, prefix):
    """
    Appends the specified string to the beginning of each line of the file.

    Args:
    file_path (str): Path to the file whose lines will be modified.
    prefix (str): String to append to the beginning of each line.
    """
    import os
    temp_file_path = file_path + ".tmp"

    with open(file_path, 'r') as file, open(temp_file_path, 'w') as temp_file:
        for line in file:
            temp_file.write(prefix + line)

    # Replace the original file with the modified file
    os.replace(temp_file_path, file_path)
