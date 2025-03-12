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
    if n <= 0:
        raise ValueError("Number of parts should be greater than zero.")
    
    if len(lst) < n:
        raise ValueError("Number of parts is greater than the length of the list.")
    
    avg = len(lst) // n
    remainder = len(lst) % n
    result = []
    start = 0
    for i in range(n):
        if i < remainder:
            sub_list = lst[start:start+avg+1]
            start += avg + 1
        else:
            sub_list = lst[start:start+avg]
            start += avg
        result.append(sub_list)
    
    return result
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