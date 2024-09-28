import re


def camel_to_snake(camel_str):
    """
    Convert a CamelCase string to snake_case.

    Parameters:
    camel_str (str): The CamelCase string to convert.

    Returns:
    str: The converted snake_case string.
    """
    # Use regular expression to insert underscores before each uppercase letter,
    # and then convert the whole string to lowercase
    snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_case_str
