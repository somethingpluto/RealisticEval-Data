import yaml
import json

def convert_yaml_to_json(yaml_file: str, json_file: str) -> None:
    with open(yaml_file, 'r') as yaml_in:
        data = yaml.safe_load(yaml_in)
    
    with open(json_file, 'w') as json_out:
        json.dump(data, json_out, indent=4)
import unittest
import os
import json
import yaml


class TestConvertYamlToJson(unittest.TestCase):

    def setUp(self):
        # Create temporary YAML files for testing
        self.simple_yaml = 'simple.yaml'
        self.nested_yaml = 'nested.yaml'
        self.empty_yaml = 'empty.yaml'
        self.list_yaml = 'list.yaml'
        self.invalid_yaml = 'invalid.yaml'

        with open(self.simple_yaml, 'w') as file:
            file.write("name: John Doe\nage: 30\n")

        with open(self.nested_yaml, 'w') as file:
            file.write("person:\n  name: Jane Doe\n  age: 25\n  address:\n    city: New York\n    zip: 10001\n")

        with open(self.empty_yaml, 'w') as file:
            file.write("")

        with open(self.list_yaml, 'w') as file:
            file.write("- item1\n- item2\n- item3\n")

        with open(self.invalid_yaml, 'w') as file:
            file.write("{ invalid: YAML: structure }\n")

    def tearDown(self):
        # Remove temporary files after testing
        os.remove(self.simple_yaml)
        os.remove(self.nested_yaml)
        os.remove(self.empty_yaml)
        os.remove(self.list_yaml)
        os.remove(self.invalid_yaml)

        if os.path.exists('output.json'):
            os.remove('output.json')

    def test_simple_yaml_conversion(self):
        convert_yaml_to_json(self.simple_yaml, 'output.json')
        with open('output.json', 'r') as jf:
            data = json.load(jf)
        self.assertEqual(data, {"name": "John Doe", "age": 30})

    def test_nested_yaml_conversion(self):
        convert_yaml_to_json(self.nested_yaml, 'output.json')
        with open('output.json', 'r') as jf:
            data = json.load(jf)
        expected_data = {
            "person": {
                "name": "Jane Doe",
                "age": 25,
                "address": {
                    "city": "New York",
                    "zip": 10001
                }
            }
        }
        self.assertEqual(data, expected_data)

    def test_empty_yaml_conversion(self):
        convert_yaml_to_json(self.empty_yaml, 'output.json')
        with open('output.json', 'r') as jf:
            data = json.load(jf)
        self.assertEqual(data, None)  # YAML.safe_load() returns None for empty files

    def test_list_yaml_conversion(self):
        convert_yaml_to_json(self.list_yaml, 'output.json')
        with open('output.json', 'r') as jf:
            data = json.load(jf)
        self.assertEqual(data, ["item1", "item2", "item3"])

    def test_invalid_yaml_conversion(self):
        with self.assertRaises(yaml.YAMLError):
            convert_yaml_to_json(self.invalid_yaml, 'output.json')

if __name__ == '__main__':
    unittest.main()