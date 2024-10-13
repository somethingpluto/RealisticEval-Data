import re
from typing import List


def parse_expression(expression: str) -> List[str]:
    tokens = []
    # Regular expression to match numbers (including decimals) and operators
    regex = r'\d+\.?\d*|[+*/()\-]'
    # Use regex to find matches in the expression
    matches = re.finditer(regex, expression)
    for match in matches:
        # Add each found token to the list
        tokens.append(match.group())
    return tokens
