
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
    if n % 2 == 0:
        # If the list length is even, split it into 2 parts and add the last element to the last part
        lst.insert(0, lst.pop())
    else:
        # If the list length is odd, split it into n+1 parts and add the last element to the last part
        for i in range(n+1):
            lst.insert(0, lst.pop())

    return lst

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