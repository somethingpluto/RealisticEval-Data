import ast
from typing import List

def parse_type_hint(type_hint_string: str) -> List:
    type_hint = ast.parse(type_hint_string)
    types = []

    def parse_node(node):
        if isinstance(node, ast.Name):
            types.append(node.id)
        elif isinstance(node, ast.Subscript):
            parse_node(node.value)
            for elt in node.slice.elts:
                parse_node(elt)
        elif isinstance(node, ast.Tuple):
            for elt in node.elts:
                parse_node(elt)

    for node in type_hint.body[0].value.elts:
        parse_node(node)

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