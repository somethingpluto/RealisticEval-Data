import unittest
import json


class TestCustomJSONEncoder(unittest.TestCase):

    def test_encode_simple_bits(self):
        """Test encoding simple dictionary with 'bits' key."""
        data = {'bits': 10}
        expected = json.dumps({'bits': '1010'})
        result = json.dumps(data, cls=CustomJSONEncoder)
        self.assertEqual(result, expected)

    def test_encode_nested_bits(self):
        """Test encoding nested dictionary containing 'bits' key."""
        data = {'nested': {'bits': 255}}
        expected = json.dumps({'nested': {'bits': '11111111'}})
        result = json.dumps(data, cls=CustomJSONEncoder)
        self.assertEqual(result, expected)

    def test_encode_without_bits(self):
        """Test encoding data without 'bits' key, ensuring normal behavior."""
        data = {'name': 'Alice', 'age': 30}
        expected = json.dumps(data)  # Use standard encoder
        result = json.dumps(data, cls=CustomJSONEncoder)
        self.assertEqual(result, expected)

    def test_incorrect_type_for_bits(self):
        """Test handling non-integer types under 'bits' key."""
        data = {'bits': 'not_an_integer'}
        with self.assertRaises(TypeError):
            json.dumps(data, cls=CustomJSONEncoder)

    def test_encode_with_non_dict_type(self):
        """Test encoding a non-dict type to ensure standard behavior is intact."""
        data = [1, 2, 3]  # List, not a dict
        expected = json.dumps(data)  # Use standard encoder
        result = json.dumps(data, cls=CustomJSONEncoder)
        self.assertEqual(result, expected)

import json


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        """
        Override the default() method to encode specific data types.

        Args:
        obj (any): The object to encode.

        Returns:
        any: A JSON-serializable form of the object or calls the base class's default method.
        """
        # Handle dictionary specially to convert certain keys
        if isinstance(obj, dict):
            new_obj = {}
            for key, value in obj.items():
                # Check if the key indicates a value that should be converted to binary
                if key == 'bits' and isinstance(value, int):
                    # Convert integer to a binary string
                    new_obj[key] = bin(value)[2:]  # bin() returns a string starting with '0b'
                else:
                    # Recursively handle all other values normally
                    new_obj[key] = value
            return new_obj
        # Use the default method for any other type not explicitly handled
        return super().default(obj)
