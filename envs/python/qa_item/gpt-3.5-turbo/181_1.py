import os

def read_file_to_byte_array(file_path: str) -> bytes:
    with open(file_path, 'rb') as file:
        byte_array = file.read()
    
    return byte_array
import os
import unittest


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.test_file = "testFile.txt"
        with open(self.test_file, 'wb') as f:
            f.write(b"Test content")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_file_with_content(self):
        """Test reading a file that exists and has content."""
        content = read_file_to_byte_array(self.test_file)
        self.assertEqual(b"Test content", content, "The file content should match the expected string.")

    def test_read_empty_file(self):
        """Test reading an empty file."""
        empty_file = "emptyFile.txt"
        open(empty_file, 'a').close()  # Create an empty file
        content = read_file_to_byte_array(empty_file)
        self.assertEqual(len(content), 0, "The content of an empty file should be a byte array of length 0.")
        os.remove(empty_file)  # Cleanup

    def test_read_non_existent_file(self):
        """Test reading a file that does not exist."""
        non_existent_file_path = "nonExistentFile.txt"
        with self.assertRaises(Exception):
            read_file_to_byte_array(non_existent_file_path)

    def test_read_file_with_special_characters(self):
        """Test reading a file with special characters in its content."""
        special_content = "Special content: !@#$%^&*()_+"
        with open(self.test_file, 'wb') as f:
            f.write(special_content.encode())
        content = read_file_to_byte_array(self.test_file)
        self.assertEqual(special_content.encode(), content, "The file content should match the special characters string.")

    def test_read_large_file(self):
        """Test reading a large file."""
        large_content = bytes(range(256)) * (10 * 1024)  # 10 MB
        with open(self.test_file, 'wb') as f:
            f.write(large_content)
        content = read_file_to_byte_array(self.test_file)
        self.assertEqual(large_content, content, "The content of the large file should match the expected byte array.")
if __name__ == '__main__':
    unittest.main()