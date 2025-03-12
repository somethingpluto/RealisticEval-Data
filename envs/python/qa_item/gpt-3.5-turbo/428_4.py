import ast
from typing import List

def parse_type_hint(type_hint_string:str) -> List:
    types = []

    def visit(node):
        if isinstance(node, ast.Name):
            types.append(node.id)
        elif isinstance(node, ast.Subscript):
            visit(node.value)
            for subnode in node.slice.value.elts:
                visit(subnode)
        elif isinstance(node, ast.Attribute):
            visit(node.value)
            types.append(node.attr)

    tree = ast.parse(type_hint_string)
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            types.append(node.id)
        elif isinstance(node, ast.Call):
            visit(node.func)

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