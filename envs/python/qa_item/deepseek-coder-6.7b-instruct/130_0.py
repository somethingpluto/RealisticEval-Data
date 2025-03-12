from decimal import Decimal, getcontext

def compute_pi(digits: int) -> str:
    """
    Computing PI (π) Using Gauss-Legendre Algorithm with High-precision Arithmetic Library.

    Args:
        digits (int): The number of decimal digits to compute π to.

    Returns:
        str: The value of π to the specified number of digits.
    """
    # Set the precision for Decimal arithmetic
    getcontext().prec = digits + 2  # Extra precision to ensure accuracy

    # Initialize variables
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)

    # Iterate to improve the approximation
    for _ in range(digits):
        a_next = (a + b) / Decimal(2)
        b_next = (a * b).sqrt()
        t_next = t - p * (a - a_next) ** Decimal(2)
        p_next = Decimal(2) * p

        a, b, t, p = a_next, b_next, t_next, p_next

    # Compute the final approximation of π
    pi = (a + b) ** Decimal(2) / (Decimal(4) * t)

    # Return the value of π as a string with the specified number of digits
    return str(pi)[:digits + 2]  # Include the "3." part
import unittest


class TestComputePi(unittest.TestCase):

    def test_calculate_pi_5_decimal_places(self):
        digits = 5
        expected = '3.14159'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

    def test_calculate_pi_10_decimal_places(self):
        digits = 10
        expected = '3.1415926536'
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
        expected = '3.141592653589793238462643383280'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()