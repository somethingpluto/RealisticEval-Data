from typing import List

def min_removals_to_make_unique(nums: List[int]) -> int:
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    
    removals = 0
    for count in counter.values():
        if count > 1:
            removals += count - 1
    
    return removals
import unittest


class TestMinRemovalsToMakeUnique(unittest.TestCase):
    def test_basic_array(self):
        """Test with a basic array where multiple removals are needed."""
        self.assertEqual(min_removals_to_make_unique([3, 3, 1, 2, 2, 1]), 3)

    def test_all_identical(self):
        """Test an array where all elements are identical."""
        self.assertEqual(min_removals_to_make_unique([4, 4, 4, 4]), 3)

    def test_all_unique(self):
        """Test an array where all elements are already unique."""
        self.assertEqual(min_removals_to_make_unique([1, 2, 3, 4]), 0)

    def test_empty_array(self):
        """Test an empty array."""
        self.assertEqual(min_removals_to_make_unique([]), 0)

    def test_complex_case(self):
        """Test a more complex case with a larger array."""
        self.assertEqual(min_removals_to_make_unique([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), 6)
if __name__ == '__main__':
    unittest.main()