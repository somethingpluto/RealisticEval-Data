from decimal import Decimal, getcontext, localcontext

def compute_pi(digits: int) -> str:
    getcontext().prec = digits + 2
    
    def gauss_legendre(iterations):
        a = Decimal(1)
        b = Decimal(1) / Decimal(2).sqrt()
        t = Decimal(1) / Decimal(4)
        p = Decimal(1)
        
        for _ in range(iterations):
            a_next = (a + b) / 2
            b = (a * b).sqrt()
            t -= p * (a - a_next) ** 2
            a = a_next
            p *= 2
            
        pi = (a + b) ** 2 / (4 * t)
        return str(pi)[:-1]
    
    return gauss_legendre(digits//14 + 1)
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