import unittest


class TestInvertDictionary(unittest.TestCase):

    def test_normal_dictionary(self):
        """Test inversion of a dictionary without duplicate values."""
        original_dict = {'a': 1, 'b': 2, 'c': 3}
        expected = {1: 'a', 2: 'b', 3: 'c'}
        result = invert_dictionary(original_dict)
        self.assertEqual(result, expected)

    def test_dictionary_with_duplicates(self):
        """Test inversion of a dictionary with duplicate values."""
        original_dict = {'a': 1, 'b': 1, 'c': 2}
        expected = {1: ['a', 'b'], 2: 'c'}
        result = invert_dictionary(original_dict)
        self.assertEqual(result, expected)

    def test_empty_dictionary(self):
        """Test inversion of an empty dictionary."""
        original_dict = {}
        expected = {}
        result = invert_dictionary(original_dict)
        self.assertEqual(result, expected)

    def test_non_string_keys(self):
        """Test inversion of a dictionary with non-string keys."""
        original_dict = {1: 'apple', 2: 'banana', 3: 'apple'}
        expected = {'apple': [1, 3], 'banana': 2}
        result = invert_dictionary(original_dict)
        self.assertEqual(result, expected)

    def test_mixed_types(self):
        """Test inversion of a dictionary with mixed key and value types."""
        original_dict = {'a': 1, 2: 'two', 'three': 3}
        expected = {1: 'a', 'two': 2, 3: 'three'}
        result = invert_dictionary(original_dict)
        self.assertEqual(result, expected)

def invert_dictionary(original_dict):
    """
    Invert the keys and values in a dictionary. If multiple keys have the same value,
    the new dictionary's values will be a list of these keys.

    Args:
    original_dict (dict): The dictionary to invert.

    Returns:
    dict: A new dictionary with values and keys inverted.
    """
    new_dict = {}
    for key, value in original_dict.items():
        if value not in new_dict:
            new_dict[value] = key
        else:
            # If the value already exists as a key, we need to append to or create a list
            if not isinstance(new_dict[value], list):
                new_dict[value] = [new_dict[value]]
            new_dict[value].append(key)
    return new_dict