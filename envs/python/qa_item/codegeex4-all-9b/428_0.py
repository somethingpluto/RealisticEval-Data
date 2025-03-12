import ast
from typing import List


def parse_type_hint(type_hint_string: str) -> List[str]:
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
    class TypeHintVisitor(ast.NodeVisitor):
        def __init__(self):
            self.types = []

        def visit_Name(self, node):
            self.types.append(node.id)

        def visit_Attribute(self, node):
            self.types.append(f"{node.value.id}.{node.attr}")

        def visit_Subscript(self, node):
            self.generic_visit(node)

    type_hint_ast = ast.parse(type_hint_string)
    visitor = TypeHintVisitor()
    visitor.visit(type_hint_ast)
    return visitor.types
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