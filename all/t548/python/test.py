import os
import unittest


class TestReadTxtAddJsonBracket(unittest.TestCase):

    def setUp(self):
        # Create temporary files for testing
        self.valid_file = 'test_valid.txt'
        self.invalid_file = 'test_invalid.txt'
        self.empty_file = 'test_empty.txt'

        with open(self.valid_file, 'w', encoding='utf-8') as f:
            f.write('{"name": "Alice"}\n{"name": "Bob"}\n')

        with open(self.invalid_file, 'w', encoding='utf-8') as f:
            f.write('{"name": "Alice"\n{"name": "Bob"}\n')  # Missing closing brace

        with open(self.empty_file, 'w', encoding='utf-8') as f:
            f.write('')  # Empty file

    def tearDown(self):
        # Remove temporary files after testing
        os.remove(self.valid_file)
        os.remove(self.invalid_file)
        os.remove(self.empty_file)


    def test_invalid_json_file(self):
        result = read_txt_add_json_bracket(self.invalid_file)
        self.assertEqual(result, [])  # Expect empty list due to JSONDecodeError

    def test_empty_file(self):
        result = read_txt_add_json_bracket(self.empty_file)
        self.assertEqual(result, [])  # Expect empty list for empty input

    def test_file_not_found(self):
        result = read_txt_add_json_bracket('non_existent_file.txt')
        self.assertEqual(result, [])  # Expect empty list for file not found

    def test_single_valid_json_object(self):
        single_valid_file = 'test_single_valid.txt'
        with open(single_valid_file, 'w', encoding='utf-8') as f:
            f.write('{"name": "Charlie"}\n')

        expected_output = [
            {"name": "Charlie"}
        ]
        result = read_txt_add_json_bracket(single_valid_file)
        self.assertEqual(result, expected_output)

        os.remove(single_valid_file)  # Clean up temporary file