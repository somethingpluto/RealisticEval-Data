from typing import List
import re

def sort_names(arr: List[str]) -> List[str]:
    def split_name_number(s):
        match = re.match(r'(\w+)(\d+)', s)
        if match:
            return match.groups()
        return (s, '0')  # default value for unsortable strings

    sorted_arr = sorted(arr, key=lambda x: (split_name_number(x)[0], int(split_name_number(x)[1])))
    return [split_name_number(x)[0] + str(split_name_number(x)[1]) for x in sorted_arr]
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