import ast
from typing import List

def parse_type_hint(type_hint_string:str) -> List:
    tree = ast.parse(type_hint_string, mode='eval')
    
    def get_types(node):
        if isinstance(node, ast.Name):
            return [node.id]
        elif isinstance(node, ast.Subscript):
            return [node.value.id] + get_types(node.slice)
        elif isinstance(node, ast.Tuple):
            types = []
            for el in node.elts:
                types.extend(get_types(el))
            return types
        elif isinstance(node, ast.Call):
            types = [node.func.id]
            for arg in node.args:
                types.extend(get_types(arg))
            return types
        elif isinstance(node, ast.Index):
            return get_types(node.value)
        elif isinstance(node, ast.Attribute):
            return [node.attr]
        else:
            return []
    
    parsed_types = []
    for node in ast.walk(tree):
        parsed_types.extend(get_types(node))
    
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