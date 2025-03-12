
import ast
from typing import List

def parse_type_hint(type_hint_string:str) -> List:
    """
    Parses a Python type hint string and returns the individual types as a list of strings.

    Args:
        type_hint_string (str): The type hint string to parse.

    Returns:
        List: The individual types parsed from the type hint string.

    Example:
        type_hint = "Union[typing.List[str], typing.Dict[str, int], Tuple[int, str], Optional[int]]"
        parsed_types = parse_type_hint(type_hint_string)
        print(parsed_types)
        # Output: ['Union', 'typing.List','str', 'typing.Dict','str', 'int', 'Tuple', 'int',
                  'str', 'Optional', 'int']
    """
    type_ hints = ast.parse(type_hint_string)
    types = []
    for type_ in type_ hints:
        if type_ == " Union":
            types.append(" Union")
        elif type_ == " Tuple":
            types.append(" Tuple")
        elif type_ == " List":
            types.append(" List")
        elif type_ == " Dict":
            types.append(" Dict")
        elif type_ == " Optional":
            types.append(" Optional")
        else:
            raise ValueError(f"Invalid type hint: {type_}")
    return types

import unittest


# Assuming the parse_type_hint function is defined above or imported here

class TestParseTypeHint(unittest.TestCase):

    def test_basic_types(self):
        type_hint = 'int'
        expected = ['int']
        self.assertEqual(parse_type_hint(type_hint), expected)

    def test_list_type(self):
        type_hint = 'List[int]'
        expected = ['List', 'int']
        self.assertEqual(parse_type_hint(type_hint), expected)

    def test_union_type(self):
        type_hint = 'Union[str, float]'
        expected = ['Union', 'str', 'float']
        self.assertEqual(parse_type_hint(type_hint), expected)

    def test_tuple_type(self):
        type_hint = 'Tuple[str, int, float]'
        expected = ['Tuple', 'str', 'int', 'float']
        self.assertEqual(parse_type_hint(type_hint), expected)

    def test_complex_type(self):
        type_hint = 'List[Union[int, float], Tuple[str, int]]'
        expected = ['List', 'Union', 'int', 'float', 'Tuple', 'str', 'int']
        self.assertEqual(parse_type_hint(type_hint), expected)

if __name__ == '__main__':
    unittest.main()