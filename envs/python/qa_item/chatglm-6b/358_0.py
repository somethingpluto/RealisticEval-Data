
from rpds import List

def sort_names(arr: List[str]) -> List[str]:
    """
    Sort a list of strings with the format "name + number" in ascending order.

    If the numbers are the same, the strings are sorted by name in ascending order.

    Args:
        arr (list of str): A reference to the list of strings to be sorted.

    Returns:
        list of str: A list of strings sorted according to the rules described above.
    """
    # Convert the list of strings to a dictionary with the format "name + number"
    sorted_dict = {k: arr[k] for k in arr}
    # Sort the dictionary by the number in descending order
    sorted_dict.sort(key=lambda x: x[1])
    # Convert the sorted dictionary back to a list of strings
    sorted_arr = [sorted_dict.get(k, k) for k in arr]
    return sorted_arr

import unittest


class Tester(unittest.TestCase):
    def test_sort_names_same_numbers(self):
        arr = ["Alice10", "Charlie10", "Bob10"]
        expected = ["Alice10", "Bob10", "Charlie10"]
        self.assertEqual(sort_names(arr), expected)

    def test_sort_names_mixed_case(self):
        arr = ["Alice3", "Bob2", "Charlie3", "Bob1"]
        expected = ["Bob1", "Bob2", "Alice3", "Charlie3"]
        self.assertEqual(sort_names(arr), expected)

    def test_sort_names_single_element(self):
        arr = ["Alice5"]
        expected = ["Alice5"]
        self.assertEqual(sort_names(arr), expected)

    def test_sort_names_empty_array(self):
        arr = []
        expected = []
        self.assertEqual(sort_names(arr), expected)
if __name__ == '__main__':
    unittest.main()