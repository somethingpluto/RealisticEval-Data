
from typing import List, Any

def elements_before_null(array: List[Any]) -> List[Any]:
    """
    Iterates through the array of elements until the first None is encountered,
    returning a new list that includes all elements before None.

    Args:
        array (List[Any]): The array to iterate through.

    Returns:
        List[Any]: A new list containing elements before the first None.
    """
    # 定义一个变量，用于保存当前迭代的索引
    current_index = 0

    # 遍历数组并更新当前索引
    for element in array:
        # 如果当前索引大于等于0，则跳过None
        if current_index >= len(array) and element is None:
            current_index = 0
            continue

        # 将当前索引设置为当前元素的索引
        array[current_index] = element

        # 更新当前索引
        current_index += 1

    # 如果当前索引为0，则返回所有元素
    return array[:current_index]

import unittest


class TestElementsBeforeNull(unittest.TestCase):

    def test_returns_elements_before_first_null(self):
        input_array = ['element1', 'element2', None, 'element3', 'element4']
        result = elements_before_null(input_array)
        self.assertEqual(result, ['element1', 'element2'])

    def test_returns_empty_array_when_input_is_empty(self):
        input_array = []
        result = elements_before_null(input_array)
        self.assertEqual(result, [])

    def test_returns_same_array_if_no_null(self):
        input_array = ['element1', 'element2', 'element3']
        result = elements_before_null(input_array)
        self.assertEqual(result, ['element1', 'element2', 'element3'])

    def test_returns_empty_array_if_first_element_is_null(self):
        input_array = [None, 'element2', 'element3']
        result = elements_before_null(input_array)
        self.assertEqual(result, [])

    def test_handles_mixed_types_with_null(self):
        input_array = [1, 'text', None, True, False]
        result = elements_before_null(input_array)
        self.assertEqual(result, [1, 'text'])

    def test_handles_array_with_only_null(self):
        input_array = [None]
        result = elements_before_null(input_array)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()