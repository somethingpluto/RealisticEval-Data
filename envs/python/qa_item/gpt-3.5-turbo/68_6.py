from typing import List

def split_list_into_parts(lst: List, n: int) -> List:
    """
    divide a list evenly into n parts and return a list of these parts. If the list length is not divisible by n, additional elements are added to the previous sections one by one
    Args:
        lst (List): The list to be divided.
        n (int): The number of parts to divide the list into.

    Returns:
        A list containing n sublists, where each sublist represents a part of the original list.
    """
    split_list = []
    length = len(lst)
    if length % n == 0:
        part_size = length // n
        for i in range(0, length, part_size):
            split_list.append(lst[i:i + part_size])
    else:
        part_size = length // n
        extra_elements = length % n
        index = 0
        for i in range(n):
            if extra_elements > 0:
                split_list.append(lst[index:index + part_size + 1])
                index += part_size + 1
                extra_elements -= 1
            else:
                split_list.append(lst[index:index + part_size])
                index += part_size
    return split_list
import unittest


class TestDivideList(unittest.TestCase):
    def test_even_division(self):
        lst = [1, 2, 3, 4, 5, 6]
        n = 3
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(split_list_into_parts(lst, n), expected)

    def test_uneven_division(self):
        lst = [1, 2, 3, 4, 5, 6, 7]
        n = 3
        expected = [[1, 2, 3], [4, 5], [6, 7]]
        self.assertEqual(split_list_into_parts(lst, n), expected)

    def test_more_parts_than_items(self):
        lst = [1, 2, 3]
        n = 5
        expected = [[1], [2], [3], [], []]
        self.assertEqual(split_list_into_parts(lst, n), expected)

    def test_single_element(self):
        lst = [1]
        n = 1
        expected = [[1]]
        self.assertEqual(split_list_into_parts(lst, n), expected)

    def test_empty_list(self):
        lst = []
        n = 3
        expected = [[], [], []]
        self.assertEqual(split_list_into_parts(lst, n), expected)

if __name__ == '__main__':
    unittest.main()