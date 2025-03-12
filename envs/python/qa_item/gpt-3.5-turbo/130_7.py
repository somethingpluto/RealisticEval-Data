from mpmath import mp

def compute_pi(digits: int) -> str:
    mp.dps = digits
    mp.prec = digits + 10
    
    a = mp.mpf(1)
    b = mp.mpf(1/mp.sqrt(2))
    t = mp.mpf(1/4)
    p = mp.mpf(1)
    
    for _ in range(digits):
        a_next = (a + b) / 2
        b_next = mp.sqrt(a * b)
        t_next = t - p * ((a - a_next)**2)
        p_next = 2 * p
        
        a = a_next
        b = b_next
        t = t_next
        p = p_next
    
    pi = (a + b)**2 / (4 * t)
    
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