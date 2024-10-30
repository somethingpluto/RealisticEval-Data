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
