import json

def parse_json_file(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
import json
import os
import unittest


class Tester(unittest.TestCase):

    def test_valid_json(self):
        json_content = '{"name": "John", "age": 30}'
        path = 'temp_valid.json'

        with open(path, 'w') as temp_file:
            temp_file.write(json_content)

        result = parse_json_file(path)
        self.assertEqual("John", result.get("name"))
        self.assertEqual(30, result.get("age"))

        os.remove(path)  # Clean up the temporary file

    def test_empty_json(self):
        json_content = '{}'
        path = 'temp_empty.json'

        with open(path, 'w') as temp_file:
            temp_file.write(json_content)

        result = parse_json_file(path)
        self.assertTrue(len(result) == 0)

        os.remove(path)  # Clean up the temporary file

    def test_null_input(self):
        with self.assertRaises(Exception):
            parse_json_file(None)

    def test_non_json_file(self):
        not_json_content = "Hello, World!"
        path = 'temp_not_json.txt'

        with open(path, 'w') as temp_file:
            temp_file.write(not_json_content)

        with self.assertRaises(json.JSONDecodeError):
            parse_json_file(path)

        os.remove(path)  # Clean up the temporary file

    def test_json_with_array(self):
        json_content = '{"names": ["John", "Doe"]}'
        path = 'temp_array.json'

        with open(path, 'w') as temp_file:
            temp_file.write(json_content)

        result = parse_json_file(path)
        self.assertIsNotNone(result.get("names"))

        os.remove(path)  # Clean up the temporary file
if __name__ == '__main__':
    unittest.main()