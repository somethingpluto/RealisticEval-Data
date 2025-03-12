from mpmath import mp

def compute_pi(digits: int) -> str:
    """
    Computing PI (π) Using Gauss-Legendre Algorithm with High-precision Arithmetic Library.

    Args:
        digits (int): The number of decimal digits to compute π to.

    Returns:
        str: The value of π to the specified number of digits.
    """
    mp.dps = digits  # Set the precision to the desired number of digits
    n = 10000000  # Number of terms to calculate
    a = [0] + list(mp.sqrt(5) * mp.cos(mp.pi * (2 * i - 1) / (2 * n)) for i in range(1, n + 1))
    b = [0] + list(mp.sqrt(5) * mp.sin(mp.pi * (2 * i - 1) / (2 * n)) for i in range(1, n + 1))
    pi = mp.pi * (sum([a[i] / b[i] for i in range(1, n + 1)]) / 2)
    return str(pi)
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