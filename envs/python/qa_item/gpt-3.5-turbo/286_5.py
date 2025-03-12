from typing import Union

def find_largest_divisible(n: int) -> Union[int, None]:
    """
    find the largest integer between a given number n and half of it that is divisible by 10 or 5
    Args:
        n (int): The upper bound of the range.

    Returns:
        The largest integer between n and half of n that is divisible by 5, or
         None if no such number exists.
    """
    for i in range(n, n//2, -1):
        if i % 10 == 0 or i % 5 == 0:
            return i
    return None
import unittest


class TestFindLargestDivisible(unittest.TestCase):
    def test_typical_case(self):
        """Test with a typical input where the largest divisible number should be found."""
        self.assertEqual(find_largest_divisible(50), 50)
        self.assertEqual(find_largest_divisible(47), 45)

    def test_no_divisible_found(self):
        """Test a case where no divisible number is found within the range."""
        self.assertIsNone(find_largest_divisible(4))

    def test_exact_half_divisible(self):
        """Test when the half of n is exactly divisible by 5."""
        self.assertEqual(find_largest_divisible(10), 10)

    def test_large_number(self):
        """Test with a large number to ensure performance and correctness."""
        self.assertEqual(find_largest_divisible(1000), 1000)

    def test_lower_bound(self):
        """Test the function with the lowest bound that should find a divisible number."""
        self.assertEqual(find_largest_divisible(5), 5)

if __name__ == '__main__':
    unittest.main()