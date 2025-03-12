from typing import List
import re

def sort_names(arr: List[str]) -> List[str]:
    """
    Sort a list of strings with the format "name + number" in ascending order.

    If the numbers are the same, the strings are sorted by name in ascending order.

    Args:
        arr (list of str): A reference to the list of strings to be sorted.

    Returns:
        list of str: A list of strings sorted according to the rules described above.
    """
    # Use regular expression to extract name and number from each string
    arr = [(re.match(r'(\D+)(\d+)', s).groups(), s) for s in arr]
    
    # Sort the list first by number, then by name
    arr.sort(key=lambda x: (int(x[0][1]), x[0][0]))
    
    # Return the sorted list of strings
    return [s[1] for s in arr]
import unittest


class Tester(unittest.TestCase):
    def test_sort_names(self):
        # Test Case 2: Same numbers, different names
        arr2 = ["Alice10", "Charlie10", "Bob10"]
        expected2 = ["Alice10", "Bob10", "Charlie10"]
        self.assertEqual(sort_names(arr2), expected2)

        # Test Case 3: Mixed case with different names and numbers
        arr3 = ["Alice3", "Bob2", "Charlie3", "Bob1"]
        expected3 = ["Bob1", "Bob2", "Alice3", "Charlie3"]
        self.assertEqual(sort_names(arr3), expected3)

        # Test Case 4: Single element
        arr4 = ["Alice5"]
        expected4 = ["Alice5"]
        self.assertEqual(sort_names(arr4), expected4)

        # Test Case 5: Empty array
        arr5 = []
        expected5 = []
        self.assertEqual(sort_names(arr5), expected5)

if __name__ == '__main__':
    unittest.main()