from typing import List
from collections import Counter

def min_removals_to_make_unique(nums: List[int]) -> int:
    # Count the frequency of each number in the list
    count = Counter(nums)
    
    # Initialize the number of removals needed
    removals = 0
    
    # List to keep track of the frequencies we have seen so far
    seen_frequencies = []
    
    # Iterate over the counts of each number
    for freq in count.values():
        # While the current frequency is greater than 1 and already seen
        while freq > 1 and freq in seen_frequencies:
            # Decrease the frequency by 1 and increase the removals by 1
            freq -= 1
            removals += 1
        
        # Add the current frequency to the seen frequencies list
        seen_frequencies.append(freq)
    
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