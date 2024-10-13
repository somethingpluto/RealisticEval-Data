import re

def is_pascal_case(input: str) -> bool:
    """
    Detects whether the string is in PASCAL_CASE.

    :param input: The string to check.
    :return: True if the string is in PASCAL_CASE, otherwise False.
    """
    # Regular expression to match PASCAL_CASE
    pascal_case_regex = r'^[A-Z][a-z]*(?:[A-Z][a-z]*)*$'
    return bool(re.match(pascal_case_regex, input))
