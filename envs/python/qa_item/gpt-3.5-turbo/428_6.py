import ast
from typing import List

def parse_type_hint(type_hint_string:str) -> List:
    def _parse_type(node):
        if isinstance(node, ast.Name):
            return [node.id]
        elif isinstance(node, ast.Subscript):
            return _parse_type(node.value) + _parse_type(node.slice)
        elif isinstance(node, ast.Tuple):
            return sum([_parse_type(e) for e in node.elts], [])
        elif isinstance(node, ast.Call):
            return [node.func.id] + sum([_parse_type(arg) for arg in node.args], [])
        elif isinstance(node, ast.Attribute):
            return _parse_type(node.value) + [node.attr]
        return []
    
    parsed_types = []
    root_node = ast.parse(type_hint_string, mode='eval').body
    if isinstance(root_node, ast.Name):
        parsed_types.append(root_node.id)
    else:
        parsed_types = _parse_type(root_node)

    return parsed_types
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