from typing import Dict

def handle_nested_data(data: Dict) -> Dict:
    def decode_bytes(item):
        if isinstance(item, bytes):
            return item.decode('utf-8')
        else:
            return item
    
    def convert_numbers(item):
        if isinstance(item, int) or isinstance(item, float):
            return item
        try:
            return int(item)
        except ValueError:
            try:
                return float(item)
            except ValueError:
                return item

    def handle_nested(item):
        if isinstance(item, dict):
            return {key: handle_nested(value) for key, value in item.items()}
        elif isinstance(item, list):
            return [handle_nested(element) for element in item]
        else:
            return item
    
    def handle_data(item):
        item = decode_bytes(item)
        item = convert_numbers(item)
        item = handle_nested(item)
        return item
    
    return handle_data(data)
import unittest
from enum import Enum
from numbers import Number


class TestHandleNestedData(unittest.TestCase):
    def test_simple_dictionary(self):
        data = {"name": b"Alice", "age": "30"}
        expected = {"name": "Alice", "age": 30}
        self.assertEqual(handle_nested_data(data), expected)

    def test_nested_dictionary(self):
        data = {"user": {"name": b"Bob", "details": {"age": "25", "height": "175.5"}}}
        expected = {"user": {"name": "Bob", "details": {"age": 25, "height": 175.5}}}
        self.assertEqual(handle_nested_data(data), expected)

    def test_list_of_mixed_data_types(self):
        data = ["100", b"200", 300.0, "400.5"]
        expected = [100, "200", 300.0, 400.5]
        self.assertEqual(handle_nested_data(data), expected)

    def test_incorrect_byte_decoding(self):
        data = {"invalid_bytes": b"\xff\xfe\xfd\xfc"}
        with self.assertRaises(UnicodeDecodeError):
            handle_nested_data(data)

    def test_complex_nested_structure(self):
        data = {
            "team": [
                {"name": b"Charlie", "scores": ["1000", "2000.2"]},
                {"name": b"Daisy", "skills": [b"Coding", "Design"], "age": "22"}
            ]
        }
        expected = {
            "team": [
                {"name": "Charlie", "scores": [1000, 2000.2]},
                {"name": "Daisy", "skills": ["Coding", "Design"], "age": 22}
            ]
        }
        self.assertEqual(handle_nested_data(data), expected)
if __name__ == '__main__':
    unittest.main()