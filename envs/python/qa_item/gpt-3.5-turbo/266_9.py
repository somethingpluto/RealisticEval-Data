from typing import Dict

def handle_nested_data(data: Dict) -> Dict:
    """
    handle nested question structures (e.g., dictionaries, lists, and enumerations), decode bytes to UTF8-strings, and convert numbers to integers or floating point numbers
    Args:
        data (Dict): question object

    Returns:
        after converted question
    """
    def decode_bytes(obj):
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
        elif isinstance(obj, dict):
            return {key: decode_bytes(val) for key, val in obj.items()}
        elif isinstance(obj, list):
            return [decode_bytes(item) for item in obj]
        else:
            return obj

    def convert_numbers(obj):
        try:
            return int(obj)
        except ValueError:
            try:
                return float(obj)
            except ValueError:
                return obj

    def convert_data(obj):
        if isinstance(obj, dict):
            return {key: convert_data(val) for key, val in obj.items()}
        elif isinstance(obj, list):
            return [convert_data(item) for item in obj]
        else:
            return convert_numbers(obj)

    converted_data = decode_bytes(data)
    converted_data = convert_data(converted_data)

    return converted_data
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