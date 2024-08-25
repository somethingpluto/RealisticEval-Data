import unittest


class TestDictOfListsToListOfDicts(unittest.TestCase):
    def test_standard_conversion(self):
        """Test standard conversion with equal length lists."""
        dict_of_lists = {
            "name": ["Alice", "Bob", "Charlie"],
            "age": [25, 30, 35],
            "city": ["New York", "Los Angeles", "Chicago"]
        }
        expected_result = [
            {'name': 'Alice', 'age': 25, 'city': 'New York'},
            {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
            {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
        ]
        result = dict_of_lists_to_list_of_dicts(dict_of_lists)
        self.assertEqual(result, expected_result)

    def test_unequal_list_lengths(self):
        """Test the function with lists of unequal lengths to trigger ValueError."""
        dict_of_lists = {
            "name": ["Alice", "Bob"],
            "age": [25, 30, 35]
        }
        with self.assertRaises(ValueError):
            dict_of_lists_to_list_of_dicts(dict_of_lists)

    def test_empty_lists(self):
        """Test the function with empty lists."""
        dict_of_lists = {
            "name": [],
            "age": [],
            "city": []
        }
        expected_result = []
        result = dict_of_lists_to_list_of_dicts(dict_of_lists)
        self.assertEqual(result, expected_result)

    def test_empty_dictionary(self):
        """Test the function with an empty dictionary."""
        dict_of_lists = {}
        expected_result = []
        result = dict_of_lists_to_list_of_dicts(dict_of_lists)
        self.assertEqual(result, expected_result)

    def test_single_element_lists(self):
        """Test the function with single-element lists."""
        dict_of_lists = {
            "name": ["Alice"],
            "age": [25],
            "city": ["New York"]
        }
        expected_result = [
            {'name': 'Alice', 'age': 25, 'city': 'New York'}
        ]
        result = dict_of_lists_to_list_of_dicts(dict_of_lists)
        self.assertEqual(result, expected_result)


def dict_of_lists_to_list_of_dicts(dict_of_lists):
    """
    Convert a dictionary of lists into a list of dictionaries.

    Args:
    dict_of_lists (dict): A dictionary where each key has a list as its value.

    Returns:
    list of dicts: A list where each item is a dictionary formed by corresponding elements of lists in the input dictionary.

    Raises:
    ValueError: If lists in the dictionary are of different lengths.
    """
    # Check if all lists are of the same length
    if len(dict_of_lists) == 0:
        return []
    if len(set(len(lst) for lst in dict_of_lists.values())) != 1:
        raise ValueError("All lists in the dictionary must have the same length.")

    # Using zip to iterate over lists simultaneously
    keys = dict_of_lists.keys()
    list_of_dicts = [dict(zip(keys, values)) for values in zip(*dict_of_lists.values())]

    return list_of_dicts
