import re

def is_camel_case(input: str) -> bool:
    """
    Detects whether the string is in CAMEL_CASE.

    :param input: The string to check.
    :return: True if the string is in CAMEL_CASE, otherwise False.
    """
    # Regular expression to match CAMEL_CASE
    camel_case_regex = r'^[a-z]+([A-Z][a-z]*)*$'
    return bool(re.match(camel_case_regex, input))
