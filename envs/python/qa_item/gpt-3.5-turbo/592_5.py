import math

def perform_operation(a: float, b: float, op: str) -> float:
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    elif op == '^':
        return math.pow(a, b)
    else:
        raise ValueError("Unsupported operation: {}".format(op))
import unittest


class Tester(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(apply_op(3, 4, '+'), 7)
        self.assertEqual(apply_op(-1, -1, '+'), -2)

    def test_subtraction(self):
        self.assertEqual(apply_op(10, 5, '-'), 5)
        self.assertEqual(apply_op(5, 10, '-'), -5)

    def test_multiplication(self):
        self.assertEqual(apply_op(3, 4, '*'), 12)
        self.assertEqual(apply_op(-2, 5, '*'), -10)

    def test_division(self):
        self.assertEqual(apply_op(8, 4, '/'), 2)
        self.assertEqual(apply_op(5, 2, '/'), 2.5)
        with self.assertRaises(Exception):  # Change to ValueError for Python
            apply_op(5, 0, '/')

    def test_exponentiation(self):
        self.assertEqual(apply_op(2, 3, '^'), 8)
        self.assertEqual(apply_op(9, 0.5, '^'), 3)  # Square root of 9

if __name__ == '__main__':
    unittest.main()