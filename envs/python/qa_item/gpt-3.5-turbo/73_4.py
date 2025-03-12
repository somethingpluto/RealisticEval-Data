from typing import Dict, List

def dict_of_lists_to_list_of_dicts(dict_of_lists: Dict) -> List[Dict]:
    """
    Convert a dictionary of lists into a list of dictionaries.
    Args:
        dict_of_lists (dict): A dictionary where each key has a list as its value.

    Returns:
        list of dicts: A list where each item is a dictionary formed by corresponding elements of lists in the input dictionary.
    """
    keys = dict_of_lists.keys()
    max_len = max([len(dict_of_lists[key]) for key in keys])
    
    list_of_dicts = []
    
    for i in range(max_len):
        new_dict = {}
        for key in keys:
            if i < len(dict_of_lists[key]):
                new_dict[key] = dict_of_lists[key][i]
            else:
                new_dict[key] = None
        list_of_dicts.append(new_dict)
    
    return list_of_dicts
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