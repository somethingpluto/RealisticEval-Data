
def find_powers(num: int) -> tuple:
    """
    Find the powers of 2 and 3 that multiply to produce the given number.

    Args:
        num (int): A positive integer greater than zero.

    Returns:
        tuple: A tuple (n, m) where n is the power of 2 and m is the power of 3.
           Returns None if the number is zero or if the number has prime factors other than 2 and 3.
    """
    if num == 0:
        return None
    powers_of_2 = [2] * len(num)
    powers_of_3 = [3] * len(num)
    for i in range(len(num)):
        if num % i == 0:
            powers_of_2.append(i)
            powers_of_3.append(num / i)
    powers_of_2 = [x * 2 for x in powers_of_2]
    powers_of_3 = [x * 3 for x in powers_of_3]
    return tuple(powers_of_2 + powers_of_3)

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