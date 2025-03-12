def perform_operation(a: float, b: float, op: str) -> float:
    """Performs a mathematical operation on two operands.

    This function takes two float values and an operator character, and performs
    the specified arithmetic operation. Supported operations include addition,
    subtraction, multiplication, division, and exponentiation.

    Args:
        a (float): The first operand.
        b (float): The second operand.
        op (str): A character representing the operation to perform:
                  '+' for addition,
                  '-' for subtraction,
                  '*' for multiplication,
                  '/' for division,
                  '^' for exponentiation.

    Returns:
        float: The result of the operation.

    Raises:
        ValueError: If the operator is not recognized or if
                    there is an attempt to divide by zero.
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    elif op == '^':
        return a ** b
    else:
        raise ValueError("Unsupported operator.")
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