
import math

def compute_pi(digits: int) -> str:
    """
     Computing PI (π) Using Gauss-Legendre Algorithm with High-precision Arithmetic Library.

    Args:
        digits (int): The number of decimal digits to compute π to.

    Returns:
        str: The value of π to the specified number of digits.
    """
    # Initialize the pi value to 1
    pi = 1
    
    # Calculate the pi value using the Gauss-Legendre algorithm
     Legendre = (1 + math.sqrt(5)) / 2
    pi_digits = len(str( Legendre))
    pi_str = str(pi)
    
    # Convert the pi value to a string with the specified number of digits
    pi_str = str(pi)[:pi_digits]
    
    return pi_str

import unittest


class TestComputePi(unittest.TestCase):

    def test_calculate_pi_5_decimal_places(self):
        digits = 5
        expected = '3.14159'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

    def test_calculate_pi_10_decimal_places(self):
        digits = 10
        expected = '3.1415926535'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

    def test_calculate_pi_15_decimal_places(self):
        digits = 15
        expected = '3.141592653589793'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

    def test_calculate_pi_20_decimal_places(self):
        digits = 20
        expected = '3.14159265358979323846'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

    def test_calculate_pi_30_decimal_places(self):
        digits = 30
        expected = '3.141592653589793238462643383279'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()