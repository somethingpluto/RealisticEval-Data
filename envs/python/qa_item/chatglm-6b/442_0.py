
from typing import Union
from collections import defaultdict

def convert_strings_to_numbers(data: Union[Dict, List]) -> Union[Dict, List]:
    """
    Convert strings in nested structures (e.g. dictionaries, arrays) to numbers (integers or floating point numbers) as much as possible

    Args:
        data (Union[Dict, List]): before convert data

    Returns:
        Union[Dict, List]: after convert data
    """
    # 初始化一个字典，用于存储每个字符串的值
    numbers_dict = defaultdict(int)

    # 遍历数据中的每个字符串，将其值转换为整数或浮点数
    for key, value in data.items():
        if isinstance(value, str):
            # 如果字符串是数字，则将其值转换为整数
            numbers_dict[value] += 1
        else:
            # 如果字符串不是数字，则将其值转换为浮点数
            numbers_dict[value] = float(value)

    # 将结果转换为列表
    result = []
    for key, value in numbers_dict.items():
        result.append({"key": key, "value": value})

    # 返回结果
    return result

import unittest


class TestConvertStringsToNumbers(unittest.TestCase):

    def test_flat_dict(self):
        data = {'a': '1', 'b': '2.5', 'c': 'not a number'}
        expected = {'a': 1, 'b': 2.5, 'c': 'not a number'}
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_nested_dict(self):
        data = {'x': {'y': '10', 'z': '3.14'}, 'w': '20.0'}
        expected = {'x': {'y': 10, 'z': 3.14}, 'w': 20.0}
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_list_of_strings(self):
        data = ['1', '2.5', '3', 'invalid']
        expected = [1, 2.5, 3, 'invalid']
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_mixed_structure(self):
        data = {'numbers': ['1', '2.0', 3], 'more_numbers': [{'num': '4'}, '5']}
        expected = {'numbers': [1, 2.0, 3], 'more_numbers': [{'num': 4}, 5]}
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_empty_structure(self):
        data = {}
        expected = {}
        self.assertEqual(convert_strings_to_numbers(data), expected)
if __name__ == '__main__':
    unittest.main()