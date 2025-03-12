import decimal

def compute_pi(digits: int) -> str:
    decimal.getcontext().prec = digits + 2

    three = decimal.Decimal(3)
    four = decimal.Decimal(4)
    one = decimal.Decimal(1)
    fifteen = decimal.Decimal(15)

    a = three
    b = four / decimal.Decimal(2).sqrt()
    t = one / four
    p = one

    for _ in range(digits):
        a_new = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_new) * (a - a_new)
        a = a_new
        p *= two

    pi = (a + b) * (a + b) / (four * t)

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