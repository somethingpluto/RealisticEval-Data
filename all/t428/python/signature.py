import ast
from typing import List


def parse_type_hint(type_hint_string:str) -> List:
    """
    Parses a Python type hint string and returns the individual types as a list of strings.

    Args:
        type_hint_string (str): The type hint string to parse.

    Returns:
        list: The individual types parsed from the type hint string.

    Example:
        type_hint = "Union[typing.List[str], typing.Dict[str, int], Tuple[int, str], Optional[int]]"
        parsed_types = parse_type_hint(type_hint)
        print(parsed_types)
        # Output: ['Union', 'typing.List', 'str', 'typing.Dict', 'str', 'int', 'Tuple', 'int',
                   'str', 'Optional', 'int']
    """
