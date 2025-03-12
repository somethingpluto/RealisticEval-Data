
def increment_number(num: float) -> float:
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