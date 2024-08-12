import json
import os
import unittest


class TestConcatenateJsonArrays(unittest.TestCase):

    def setUp(self):
        # Set up a test directory and test files
        self.test_dir = 'test_json'
        os.makedirs(self.test_dir, exist_ok=True)
        # Create test JSON files
        self.create_test_file('array1.json', [1, 2, 3])
        self.create_test_file('array2.json', ['a', 'b', 'c'])
        self.create_test_file('not_array.json', {'key': 'value'})
        self.create_test_file('empty.json', [])
        self.create_test_file('non_json.txt', "This is not a JSON file.")

    def tearDown(self):
        # Clean up: Remove created files and directory
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))
        os.rmdir(self.test_dir)

    def create_test_file(self, filename, content):
        # Helper method to create JSON files
        with open(os.path.join(self.test_dir, filename), 'w') as f:
            json.dump(content, f)

    def test_concatenate_valid_json_arrays(self):
        # Test with valid JSON arrays
        result = concatenate_json_arrays(self.test_dir)
        self.assertCountEqual(result, [1, 2, 3, 'a', 'b', 'c'])

    def test_ignore_non_array_json(self):
        # Test that non-array JSON files are ignored
        result = concatenate_json_arrays(self.test_dir)
        self.assertNotIn('key', result)

    def test_ignore_non_json_files(self):
        # Test that non-JSON files are ignored
        result = concatenate_json_arrays(self.test_dir)
        self.assertNotIn("This is not a JSON file.", result)

    def test_handle_empty_arrays(self):
        # Test concatenation includes empty arrays
        result = concatenate_json_arrays(self.test_dir)
        self.assertNotIn([], result)

    def test_empty_directory(self):
        # Test with no JSON files in the directory
        empty_dir = 'empty_test_json'
        os.makedirs(empty_dir, exist_ok=True)
        result = concatenate_json_arrays(empty_dir)
        self.assertEqual(result, [])
        os.rmdir(empty_dir)
