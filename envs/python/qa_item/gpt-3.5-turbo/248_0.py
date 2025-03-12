from typing import Dict, List

def sanitize_data(data: Dict, key_to_remove: List = None) -> Dict:
    """
    remove the corresponding sensitive question in the given dictionary based on the given key_to_remove list

    Args:
        data (Dict): original question dict
        key_to_remove (List): key_to_remove list

    Returns:
        Dict: removed dict
    """ 
    if key_to_remove:
        for key in key_to_remove:
            if key in data:
                del data[key]
    return data
import unittest


class TestSanitizeData(unittest.TestCase):
    def test_empty_dict(self):
        """ Test with an empty dictionary. """
        data = {}
        key_to_remove = ["email", "metadata"]

        expected = {}
        self.assertEqual(sanitize_data(data, key_to_remove), expected)

    def test_remove_default_keys(self):
        """ Test removing default keys from a nested structure. """
        data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "metadata": {"submitted_at": "2021-07-10", "status": "pending"},
            "comments": ["Good", "Needs review"]
        }
        key_to_remove = ["email", "metadata"]
        expected = {
            "name": "John Doe",
            "comments": ["Good", "Needs review"]
        }
        self.assertEqual(sanitize_data(data, key_to_remove), expected)

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
        self.assertEqual(sanitize_data(data, key_to_remove=["email"]), expected)
if __name__ == '__main__':
    unittest.main()