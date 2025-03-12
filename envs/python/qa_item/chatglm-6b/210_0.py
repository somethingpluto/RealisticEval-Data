
def fibonacci_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

import unittest


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        """Test Case 1: Fibonacci of 0 should be 0"""
        self.assertEqual(fibonacci_recursive(0), 0)

    def test_fibonacci_1(self):
        """Test Case 2: Fibonacci of 1 should be 1"""
        self.assertEqual(fibonacci_recursive(1), 1)

    def test_fibonacci_5(self):
        """Test Case 3: Fibonacci of 5 should be 5"""
        self.assertEqual(fibonacci_recursive(5), 5)

    def test_fibonacci_10(self):
        """Test Case 4: Fibonacci of 10 should be 55"""
        self.assertEqual(fibonacci_recursive(10), 55)

    def test_fibonacci_20(self):
        """Test Case 5: Fibonacci of 20 should be 6765"""
        self.assertEqual(fibonacci_recursive(20), 6765)

if __name__ == '__main__':
    unittest.main()