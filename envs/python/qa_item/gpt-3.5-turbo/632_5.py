from typing import List


def parse_expression(expression: str) -> List[str]:
    """
    Parses a mathematical expression string into a list of tokens.
    This function identifies both operands (numbers) and operators (+, -, *, /, etc.)
    in the provided expression and returns them in a list format.

    Args:
        expression (str): The mathematical expression to be parsed.

    Returns:
        list[str]: A list containing the tokens identified in the expression.
                    The list will include both operands and operators in the order they appear.
    """
    tokens = []
    current_token = ''

    for char in expression:
        if char.isdigit() or char == '.':
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ''
            if char != ' ':
                tokens.append(char)
    
    if current_token:
        tokens.append(current_token)
    
    return tokens
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
if __name__ == '__main__':
    unittest.main()