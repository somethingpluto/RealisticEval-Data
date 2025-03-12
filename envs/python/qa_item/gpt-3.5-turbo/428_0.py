import ast
from typing import List

def parse_type_hint(type_hint_string: str) -> List:
    node = ast.parse(type_hint_string)
    
    def extract_types(node):
        if isinstance(node, ast.Subscript):
            return [node.value.id] + extract_types(node.slice)
        elif isinstance(node, ast.Name):
            return [node.id]
        elif isinstance(node, ast.Tuple):
            types = []
            for el in node.elts:
                types += extract_types(el)
            return types
        elif isinstance(node, ast.Attribute):
            return [node.value.value.id, node.value.attr, node.attr]
        elif isinstance(node, ast.Call):
            types = []
            for arg in node.args:
                types += extract_types(arg)
            return [node.func.value.id] + types
        elif isinstance(node, list):
            types = []
            for item in node:
                types += extract_types(item)
            return types
        else:
            return []
        
    types = extract_types(node.body[0].value)
    
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