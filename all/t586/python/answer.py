import re

def is_snake_case(input: str) -> bool:
    """
    Detects whether the string is in SNAKE_CASE.

    :param input: The string to check.
    :return: True if the string is in SNAKE_CASE, otherwise False.
    """
    # Regular expression to match SNAKE_CASE
    snake_case_regex = r'^[a-z]+(_[a-z]+)*$'
    return bool(re.match(snake_case_regex, input))
