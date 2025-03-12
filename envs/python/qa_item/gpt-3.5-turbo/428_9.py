import ast
from typing import List

def parse_type_hint(type_hint_string: str) -> List:
    node = ast.parse(type_hint_string, mode="eval").body
    return get_types(node)

def get_types(node):
    if isinstance(node, ast.Name):
        return [node.id]
    elif isinstance(node, ast.Attribute):
        return get_types(node.value) + [node.attr]
    elif isinstance(node, ast.Subscript):
        return get_types(node.value) + get_types(node.slice)
    elif isinstance(node, ast.Tuple):
        types = []
        for element in node.elts:
            types.extend(get_types(element))
        return types
    elif isinstance(node, ast.Call):
        types = []
        types.extend(get_types(node.func))
        for arg in node.args:
            types.extend(get_types(arg))
        return types
    elif isinstance(node, ast.List):
        types = []
        for element in node.elts:
            types.extend(get_types(element))
        return types
    elif isinstance(node, ast.Dict):
        types = []
        for key, value in zip(node.keys, node.values):
            types.extend(get_types(key) + get_types(value))
        return types
    elif isinstance(node, ast.Constant):
        return [node.value]
    else:
        return []

# Example usage
type_hint = "Union[typing.List[str], typing.Dict[str, int], Tuple[int, str], Optional[int]]"
parsed_types = parse_type_hint(type_hint)
print(parsed_types)
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