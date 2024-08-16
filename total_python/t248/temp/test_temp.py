import unittest


class TestSanitizeData(unittest.TestCase):
    def test_empty_dict(self):
        """ Test with an empty dictionary. """
        data = {}
        expected = {}
        self.assertEqual(sanitize_data(data), expected)

    def test_remove_default_keys(self):
        """ Test removing default keys from a nested structure. """
        data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "metadata": {"submitted_at": "2021-07-10", "status": "pending"},
            "comments": ["Good", "Needs review"]
        }
        expected = {
            "name": "John Doe",
            "comments": ["Good", "Needs review"]
        }
        self.assertEqual(sanitize_data(data), expected)

    def test_specified_key_to_remove(self):
        """ Test removing a specified key from the dictionary. """
        data = {
            "name": "John Doe",
            "location": "Earth",
            "email": "johndoe@example.com"
        }
        expected = {
            "name": "John Doe",
            "location": "Earth"
        }
        self.assertEqual(sanitize_data(data, key_to_remove={"email"}), expected)

    def test_list_of_dicts(self):
        """ Test a list containing dictionaries. """
        data = [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"}
        ]
        expected = [
            {"name": "Alice"},
            {"name": "Bob"}
        ]
        self.assertEqual(sanitize_data(data), expected)

    def test_non_dict_non_list(self):
        """ Test with non-dict and non-list data types. """
        data = "Hello, world!"
        expected = "Hello, world!"
        self.assertEqual(sanitize_data(data), expected)
import json


def sanitize_data(data, key_to_remove=None
                  ):
    """Recursively sanitize a dictionary by removing specific keys."""
    if key_to_remove is None:
        key_to_remove = {"email", "pc_conflicts", "metadata", "eligible_student_paper_prize", "talk_poster",
                         "submitted_at",
                         "decision", "status", "submitted", "submission"}
    if isinstance(data, dict):
        return {key: sanitize_data(value) for key, value in data.items() if key not in key_to_remove}
    elif isinstance(data, list):
        return [sanitize_data(value) for value in data]
    else:
        return data
