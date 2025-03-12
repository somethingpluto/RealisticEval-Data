import json

def save_as_json(data: dict, output_file_path: str) -> None:
    with open(output_file_path, 'w') as file:
        json.dump(data, file)
import json
import os
import unittest
from io import StringIO


class TestSaveAsJSON(unittest.TestCase):
    mock_file_path = 'test.json'

    def setUp(self):
        # Redirect console output
        self.console_output = StringIO()
        self.original_stdout = redirect_stdout(self.console_output)
        self.original_stdout.__enter__()

    def tearDown(self):
        # Clean up after each test
        if os.path.exists(self.mock_file_path):
            os.remove(self.mock_file_path)  # Remove test file if it exists

        self.original_stdout.__exit__(None, None, None)

    def test_save_valid_object_to_json_file(self):
        data = {"name": "Alice", "age": 25}
        save_as_json(data, self.mock_file_path)
        with open(self.mock_file_path, 'r', encoding='utf-8') as json_file:
            saved_data = json_file.read()
        self.assertEqual(saved_data, json.dumps(data, indent=2))

    def test_handle_empty_object(self):
        data = {}
        save_as_json(data, self.mock_file_path)
        with open(self.mock_file_path, 'r', encoding='utf-8') as json_file:
            saved_data = json_file.read()
        self.assertEqual(saved_data, json.dumps(data, indent=2))

    def test_save_nested_object_to_json_file(self):
        data = {"user": {"name": "Bob", "age": 30}, "active": True}
        save_as_json(data, self.mock_file_path)
        with open(self.mock_file_path, 'r', encoding='utf-8') as json_file:
            saved_data = json_file.read()
        self.assertEqual(saved_data, json.dumps(data, indent=2))

    def test_save_array_of_objects_to_json_file(self):
        data = [
            {"product": {"id": 1, "name": "Laptop", "price": 999.99}, "inStock": True},
            {"product": {"id": 2, "name": "Phone", "price": 499.99}, "inStock": False}
        ]
        save_as_json(data, self.mock_file_path)
        with open(self.mock_file_path, 'r', encoding='utf-8') as json_file:
            saved_data = json_file.read()
        self.assertEqual(saved_data, json.dumps(data, indent=2))

    def test_save_object_with_mixed_data_types_to_json_file(self):
        data = {
            "title": "Shopping List",
            "items": ["Milk", "Eggs", "Bread"],
            "total": 3.50,
            "completed": False
        }
        save_as_json(data, self.mock_file_path)
        with open(self.mock_file_path, 'r', encoding='utf-8') as json_file:
            saved_data = json_file.read()
        self.assertEqual(saved_data, json.dumps(data, indent=2))

    def test_save_deeply_nested_object_to_json_file(self):
        data = {
            "company": {
                "name": "TechCorp",
                "employees": [
                    {
                        "id": 1,
                        "name": "Alice",
                        "role": "Developer",
                        "contact": {"email": "alice@techcorp.com", "phone": "123-456-7890"}
                    },
                    {
                        "id": 2,
                        "name": "Bob",
                        "role": "Designer",
                        "contact": {"email": "bob@techcorp.com", "phone": "098-765-4321"}
                    }
                ]
            },
            "established": 2010
        }
        save_as_json(data, self.mock_file_path)
        with open(self.mock_file_path, 'r', encoding='utf-8') as json_file:
            saved_data = json_file.read()
        self.assertEqual(saved_data, json.dumps(data, indent=2))

if __name__ == '__main__':
    unittest.main()