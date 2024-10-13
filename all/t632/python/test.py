import unittest


class Tester(unittest.TestCase):

    def test_simple_addition(self):
        expression = "2 + 2"
        result = parse_expression(expression)
        self.assertEqual(result, ["2", "+", "2"])

    def test_complex_expression(self):
        expression = "3 + 5 * (2 - 8)"
        result = parse_expression(expression)
        self.assertEqual(result, ["3", "+", "5", "*", "(", "2", "-", "8", ")"])

    def test_negative_numbers(self):
        expression = "-1 + 4 - 5"
        result = parse_expression(expression)
        self.assertEqual(result, ["-", "1", "+", "4", "-", "5"])

    def test_decimals(self):
        expression = "3.5 + 2.1"
        result = parse_expression(expression)
        self.assertEqual(result, ["3.5", "+", "2.1"])

    def test_operators_only(self):
        expression = "+ - * /"
        result = parse_expression(expression)
        self.assertEqual(result, ["+", "-", "*", "/"])

    def test_empty_expression(self):
        expression = ""
        result = parse_expression(expression)
        self.assertTrue(len(result) == 0)

    def test_single_number(self):
        expression = "42"
        result = parse_expression(expression)
        self.assertEqual(result, ["42"])