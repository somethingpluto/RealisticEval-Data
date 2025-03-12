from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(lower_bound: int, upper_bound: int) -> list:
    primes = []
    for num in range(lower_bound, upper_bound + 1):
        if is_prime(num):
            primes.append(num)
    return primes
import unittest


class TestFindPrimesInRange(unittest.TestCase):
    def test_find_primes_in_range(self):
        expected = [2, 3, 5, 7, 11]
        self.assertEqual(find_primes(1, 12), expected, "Check primes between 1 and 12")

    def test_find_primes_single_prime(self):
        expected = [29]
        self.assertEqual(find_primes(29, 29), expected, "Check single prime number")

    def test_find_primes_in_big_range(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(find_primes(1, 100), expected, "Check primes between 1 and 100")

    def test_find_primes_no_primes(self):
        expected = []
        self.assertEqual(find_primes(0, 1), expected, "Check range with no primes")

if __name__ == '__main__':
    unittest.main()