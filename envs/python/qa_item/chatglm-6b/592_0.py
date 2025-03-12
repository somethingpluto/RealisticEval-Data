
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
    if op not in ['+', '-', '*', '/', '^']:
        raise ValueError("Invalid operator: {}".format(op))

    try:
        result = float(op.lower()) * a + b
    except ValueError as e:
        raise ValueError("Invalid operator or operands: {}".format(e))

    return result

import unittest


class Tester(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(perform_operation(3, 4, '+'), 7)
        self.assertEqual(perform_operation(-1, -1, '+'), -2)

    def test_subtraction(self):
        self.assertEqual(perform_operation(10, 5, '-'), 5)
        self.assertEqual(perform_operation(5, 10, '-'), -5)

    def test_multiplication(self):
        self.assertEqual(perform_operation(3, 4, '*'), 12)
        self.assertEqual(perform_operation(-2, 5, '*'), -10)

    def test_division(self):
        self.assertEqual(perform_operation(8, 4, '/'), 2)
        self.assertEqual(perform_operation(5, 2, '/'), 2.5)
        with self.assertRaises(Exception):  # Change to ValueError for Python
            perform_operation(5, 0, '/')

    def test_exponentiation(self):
        self.assertEqual(apply_op(2, 3, '^'), 8)
        self.assertEqual(apply_op(9, 0.5, '^'), 3)  # Square root of 9

if __name__ == '__main__':
    unittest.main()