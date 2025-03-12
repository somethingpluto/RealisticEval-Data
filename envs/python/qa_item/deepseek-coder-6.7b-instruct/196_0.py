from typing import List

def generate_primes(limit: int) -> List[int]:
    """
    Find all prime numbers that are less than or equal to limit using the Eichler sieve algorithm.

    Args:
        limit (int): The upper bound (inclusive) for finding prime numbers.

    Returns:
        List[int]: A list of integers containing all prime numbers less than or equal to the limit.
    """
    if limit < 2:
        return []
    
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    
    return [num for num, is_prime in enumerate(sieve) if is_prime]
import unittest


class Tester(unittest.TestCase):

    def test_small_limit(self):
        """Test Case 1: Small limit (10)"""
        expected = [2, 3, 5, 7]
        self.assertEqual(generate_primes(10), expected)

    def test_prime_limit(self):
        """Test Case 2: Prime limit (29)"""
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(generate_primes(29), expected)

    def test_non_prime_limit(self):
        """Test Case 3: Non-prime limit (30)"""
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(generate_primes(30), expected)

    def test_limit_of_two(self):
        """Test Case 4: Limit of 2 (smallest prime)"""
        expected = [2]
        self.assertEqual(generate_primes(2), expected)

    def test_invalid_limit(self):
        """Test Case 5: Invalid limit (1, should throw an exception)"""
        with self.assertRaises(ValueError):  # Catch ValueError instead of std::invalid_argument
            generate_primes(1)

if __name__ == '__main__':
    unittest.main()