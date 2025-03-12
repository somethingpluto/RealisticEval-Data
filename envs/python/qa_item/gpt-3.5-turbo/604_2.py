def power_tail(x: int, y: int, acc: int = 1) -> int:
    def power_helper(x, y, acc):
        if y == 0:
            return acc
        return power_helper(x, y - 1, acc * x)

    if y < 0:
        raise ValueError("Exponent cannot be negative")
    return power_helper(x, y, acc)
import unittest


class Tester(unittest.TestCase):
    def test_base_cases(self):
        # Test 0^0, should return 1 (by convention)
        self.assertEqual(power_tail(0, 0), 1)
        # Test x^0 for any x, should return 1
        self.assertEqual(power_tail(5, 0), 1)
        self.assertEqual(power_tail(12345, 0), 1)

    def test_power_of_one(self):
        # Test 1^y for any y, should return 1
        self.assertEqual(power_tail(1, 5), 1)
        self.assertEqual(power_tail(1, 123), 1)

    def test_power_of_zero(self):
        # Test 0^y for any y > 0, should return 0
        self.assertEqual(power_tail(0, 5), 0)
        self.assertEqual(power_tail(0, 100), 0)

    def test_positive_powers(self):
        # Test some positive powers
        self.assertEqual(power_tail(2, 3), 8)   # 2^3 = 8
        self.assertEqual(power_tail(3, 4), 81)  # 3^4 = 81
        self.assertEqual(power_tail(5, 2), 25)  # 5^2 = 25

if __name__ == '__main__':
    unittest.main()