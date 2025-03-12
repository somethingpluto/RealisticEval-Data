from math import log

def find_powers(num: int) -> tuple:
    if num == 0:
        return None
    
    # Find power of 2
    power_of_2 = 0
    while num % 2 == 0:
        power_of_2 += 1
        num //= 2
    
    # Find power of 3
    power_of_3 = 0
    while num % 3 == 0:
        power_of_3 += 1
        num //= 3
    
    if num == 1:
        return power_of_2, power_of_3
    else:
        return None, None
import unittest


class TestFindPowers(unittest.TestCase):

    def test_valid_cases(self):
        """Test valid numbers with only 2's and 3's as prime factors."""
        self.assertEqual(find_powers(18), (1, 2))  # 18 = 2^1 * 3^2
        self.assertEqual(find_powers(8), (3, 0))   # 8 = 2^3 * 3^0
        self.assertEqual(find_powers(27), (0, 3))  # 27 = 2^0 * 3^3
        self.assertEqual(find_powers(12), (2, 1))  # 12 = 2^2 * 3^1
        self.assertEqual(find_powers(1), (0, 0))    # 1 = 2^0 * 3^0

    def test_invalid_cases(self):
        """Test numbers with prime factors other than 2 and 3."""
        self.assertIsNone(find_powers(7))    # 7 is a prime factor
        self.assertIsNone(find_powers(14))   # 14 = 2^1 * 7^1 (contains 7)
        self.assertIsNone(find_powers(10))   # 10 = 2^1 * 5^1 (contains 5)


    def test_large_numbers(self):
        """Test large numbers that have only 2 and 3 as prime factors."""
        self.assertEqual(find_powers(864), (5, 3))  # 864 = 2^5 * 3^3
        self.assertEqual(find_powers(729), (0, 6))  # 729 = 2^0 * 3^6

    def test_edge_cases(self):
        """Test edge cases for minimal inputs."""
        self.assertEqual(find_powers(2), (1, 0))   # 2 = 2^1 * 3^0
        self.assertEqual(find_powers(3), (0, 1))   # 3 = 2^0 * 3^1
if __name__ == '__main__':
    unittest.main()