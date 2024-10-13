import re

def is_kebab_case(input: str) -> bool:
    """
    Detects whether the string is in KEBAB_CASE.

    :param input: The string to check.
    :return: True if the string is in KEBAB_CASE, otherwise False.
    """
    # Regular expression to match KEBAB_CASE
    kebab_case_regex = r'^[a-z]+(-[a-z]+)*$'
    return bool(re.match(kebab_case_regex, input))