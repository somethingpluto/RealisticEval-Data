import json
import os
import unittest


class TestReadJsonl(unittest.TestCase):

    def setUp(self):
        """Create temporary JSON Lines files for testing."""
        self.valid_jsonl_file = 'test_valid.jsonl'
        self.invalid_jsonl_file = 'test_invalid.jsonl'
        self.non_existent_file = 'non_existent.jsonl'

        # Valid JSON Lines content
        with open(self.valid_jsonl_file, 'w') as file:
            file.write('{"name": "Alice", "age": 30}\n')
            file.write('{"name": "Bob", "age": 25}\n')
            file.write('{"name": "Charlie", "age": 35}\n')

        # Invalid JSON Lines content
        with open(self.invalid_jsonl_file, 'w') as file:
            file.write('{"name": "Alice", "age": 30}\n')
            file.write('{"name": "Bob", "age": "twenty-five}\n')  # Missing closing quote

    def tearDown(self):
        """Remove the temporary JSON Lines files after testing."""
        if os.path.isfile(self.valid_jsonl_file):
            os.remove(self.valid_jsonl_file)
        if os.path.isfile(self.invalid_jsonl_file):
            os.remove(self.invalid_jsonl_file)

    def test_read_valid_jsonl(self):
        """Test reading a valid JSON Lines file."""
        expected_data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35}
        ]
        result = read_jsonl(self.valid_jsonl_file)
        self.assertEqual(result, expected_data)

    def test_file_not_found(self):
        """Test for FileNotFoundError when the file does not exist."""
        with self.assertRaises(FileNotFoundError):
            read_jsonl(self.non_existent_file)

    def test_empty_jsonl_file(self):
        """Test reading an empty JSON Lines file."""
        empty_jsonl_file = 'test_empty.jsonl'
        with open(empty_jsonl_file, 'w') as file:
            file.write("")  # Create an empty JSON Lines file

        result = read_jsonl(empty_jsonl_file)
        self.assertEqual(result, [])  # Expecting an empty list for empty file

        os.remove(empty_jsonl_file)  # Cleanup after the test