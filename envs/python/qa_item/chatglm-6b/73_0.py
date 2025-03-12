
from typing import Dict, List

def dict_of_lists_to_list_of_dicts(dict_of_lists: Dict) -> List[Dict]:
    """
    Convert a dictionary of lists into a list of dictionaries.
    Args:
        dict_of_lists (Dict): A dictionary where each key has a list as its value.

    Returns:
        list of dicts: A list where each item is a dictionary formed by corresponding elements of lists in the input dictionary.
    """
    # Iterate over the keys and values in the input dictionary
    for key, value in dict_of_lists.items():
        # Create a new dictionary with the corresponding elements of the lists
        result = {}
        for i in range(len(value)):
            result[key][i] = value[i]
        # Add the new dictionary to the list of results
        result.append(result)
    return result

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

if __name__ == '__main__':
    unittest.main()