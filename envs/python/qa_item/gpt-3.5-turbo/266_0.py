from typing import Dict
from typing import Union

def handle_nested_data(data: Dict) -> Dict:
    def decode_bytes_to_utf8(data):
        if isinstance(data, bytes):
            return data.decode('utf-8')
        elif isinstance(data, dict):
            return {key: decode_bytes_to_utf8(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [decode_bytes_to_utf8(item) for item in data]
        else:
            return data

    def convert_numbers(data):
        if isinstance(data, dict):
            return {key: convert_numbers(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [convert_numbers(item) for item in data]
        elif isinstance(data, str):
            if data.isdigit():
                return int(data)
            try:
                return float(data)
            except ValueError:
                return data
        else:
            return data

    def recursive_handle(data):
        data = decode_bytes_to_utf8(data)
        data = convert_numbers(data)
        return data

    return recursive_handle(data)
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