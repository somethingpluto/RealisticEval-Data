import ast
from typing import List

def parse_type_hint(type_hint_string:str) -> List:
    node = ast.parse(type_hint_string)
    types = []

    def parse_node(node):
        if isinstance(node, ast.Name):
            types.append(node.id)
        elif isinstance(node, ast.Subscript):
            parse_node(node.value)
            for slice_node in node.slice.elts:
                parse_node(slice_node)
        elif isinstance(node, ast.Attribute):
            parse_node(node.value)
            types.append(node.attr)
        elif isinstance(node, ast.Tuple):
            for element_node in node.elts:
                parse_node(element_node)
        elif isinstance(node, ast.Call):
            parse_node(node.func)
            for arg_node in node.args:
                parse_node(arg_node)

    for statement in node.body:
        if isinstance(statement, ast.Expr):
            parse_node(statement.value)

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