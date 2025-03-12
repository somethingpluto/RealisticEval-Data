def increment_number(num: float) -> float:
    """
    Increments the entered number.

    If the number is non-positive (<= 0), returns the original value.
    If the number is positive, returns the value plus 1.

    Args:
        num (float): The number to increment.

    Returns:
        float: The incremented value or the original number.
    """

    if num <= 0:
        return num
    else:
        return num + 1
import unittest


class TestIncrementNumber(unittest.TestCase):

    def test_input_5(self):
        self.assertEqual(increment_number(5), 6)

    def test_input_0(self):
        self.assertEqual(increment_number(0), 0)

    def test_input_negative_3(self):
        self.assertEqual(increment_number(-3), -3)

    def test_input_0_5(self):
        self.assertEqual(increment_number(0.5), 1.5)

    def test_input_1(self):
        self.assertEqual(increment_number(1), 2)

    def test_input_negative_1(self):
        self.assertEqual(increment_number(-1), -1)

if __name__ == '__main__':
    unittest.main()