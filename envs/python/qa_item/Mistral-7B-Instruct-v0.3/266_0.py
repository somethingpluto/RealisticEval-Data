import typing
import json
import base64

def handle_nested_data(data: typing.Dict) -> typing.Dict:
    """
    handle nested question structures (e.g., dictionaries, lists, and enumerations), decode bytes to UTF8-strings, and convert numbers to integers or floating point numbers
    Args:
        data (Dict): question object

    Returns:
        after converted question
    """
    def _handle_value(value):
        if isinstance(value, bytes):
            return value.decode('utf-8')
        elif isinstance(value, (int, float)):
            return float(value) if value!= int(value) else int(value)
        elif isinstance(value, (list, tuple)):
            return [_handle_value(v) for v in value]
        elif isinstance(value, dict):
            return {k: _handle_value(v) for k, v in value.items()}
        else:
            return value

    for key, value in data.items():
        data[key] = _handle_value(value)

    return data
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