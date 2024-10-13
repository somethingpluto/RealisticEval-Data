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