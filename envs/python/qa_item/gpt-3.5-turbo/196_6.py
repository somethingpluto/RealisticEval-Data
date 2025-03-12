from typing import List

def generate_primes(limit: int) -> List[int]:
    def sieve(limit: int) -> List[bool]:
        is_prime = [True] * (limit + 1)
        is_prime[0] = False
        is_prime[1] = False
        
        p = 2
        while p * p <= limit:
            if is_prime[p]:
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False
            p += 1
        
        return is_prime
    
    primes = []
    is_prime = sieve(limit)
    
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
    
    return primes
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