from typing import List

def sort_names(arr: List[str]) -> List[str]:
    def custom_sort(name):
        parts = name.split()
        return (int(parts[1]), parts[0])
    
    return sorted(arr, key=custom_sort)
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