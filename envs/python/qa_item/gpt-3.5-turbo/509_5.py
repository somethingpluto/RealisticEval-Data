def mod_exp(base:int, exponent:int, modulus:int) -> int:
    """
    Perform modular exponentiation: (base^exponent) % modulus efficiently.

    Args:
        base (int): The base value.
        exponent (int): The exponent value (should be non-negative).
        modulus (int): The modulus value (should be positive).

    Returns:
        int: The result of (base^exponent) % modulus.
    """
    result = 1
    base = base % modulus
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    
    return result
import unittest


class TestModExp(unittest.TestCase):
    def test_case_1(self):
        """ Test with base = 2, exponent = 10, modulus = 1000 """
        self.assertEqual(mod_exp(2, 10, 1000), 24)

    def test_case_2(self):
        """ Test with base = 3, exponent = 7, modulus = 50 """
        self.assertEqual(mod_exp(3, 7, 50), 37)

    def test_case_3(self):
        """ Test with base = 5, exponent = 0, modulus = 13 (any number^0 = 1) """
        self.assertEqual(mod_exp(5, 0, 13), 1)

    def test_case_4(self):
        """ Test with base = 7, exponent = 5, modulus = 20 """
        self.assertEqual(mod_exp(7, 5, 20), 7)  # 7^5 = 16807, 16807 % 20 = 7

    def test_case_5(self):
        """ Test with base = 10, exponent = 5, modulus = 6 """
        self.assertEqual(mod_exp(10, 5, 6), 4)  # 10^5 = 100000, 100000 % 6 = 4
if __name__ == '__main__':
    unittest.main()