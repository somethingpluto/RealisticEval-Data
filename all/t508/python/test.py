import json
import unittest


class TestCustomJSONEncoder(unittest.TestCase):

    def test_encode_true(self):
        """ Test encoding of True should return 1. """
        data = {"is_active": True}
        expected = '{"is_active": 1}'
        result = json.dumps(data, cls=CustomJSONEncoder)
        self.assertEqual(result, expected)

    def test_encode_false(self):
        """ Test encoding of False should return 0. """
        data = {"is_verified": False}
        expected = '{"is_verified": 0}'
        result = json.dumps(data, cls=CustomJSONEncoder)
        self.assertEqual(result, expected)

    def test_encode_boolean_in_list(self):
        """ Test encoding of a list containing boolean values. """
        data = {"preferences": [True, False, True]}
        expected = '{"preferences": [1, 0, 1]}'
        result = json.dumps(data, cls=CustomJSONEncoder)
        self.assertEqual(result, expected)

    def test_encode_nested_structures(self):
        """ Test encoding of nested structures with boolean values. """
        data = {
            "name": "Alice",
            "settings": {
                "notifications": True,
                "dark_mode": False
            }
        }
        expected = '{"name": "Alice", "settings": {"notifications": 1, "dark_mode": 0}}'
        result = json.dumps(data, cls=CustomJSONEncoder)
        self.assertEqual(result, expected)

    def test_encode_with_non_boolean(self):
        """ Test encoding with mixed types. """
        data = {
            "age": 30,
            "is_active": True,
            "email_verified": False,
            "tags": ["python", "developer"]
        }
        expected = '{"age": 30, "is_active": 1, "email_verified": 0, "tags": ["python", "developer"]}'
        result = json.dumps(data, cls=CustomJSONEncoder)
        self.assertEqual(result, expected)
