import json
import os
from typing import List, Dict, Any

def read_jsonl(file_path: str) -> List[Dict[str, Any]]:
    """
    Reads a JSON Lines file and returns its content as a list of dictionaries.

    Args:
        file_path (str): The path to the JSON Lines file.

    Returns:
        List[Dict[str, Any]]: A list of JSON objects parsed from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If there is an error parsing a line in the JSON Lines file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found")

    json_objects = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                json_object = json.loads(line)
                json_objects.append(json_object)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(f"Error decoding JSON: {str(e)}")

    return json_objects
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
if __name__ == '__main__':
    unittest.main()