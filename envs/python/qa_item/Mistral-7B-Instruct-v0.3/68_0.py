from typing import List

def split_list_into_parts(lst: List, n: int) -> List:
    parts = [lst[i:i+n] for i in range(0, len(lst), n)]
    if len(parts) < n:
        remaining_elements = lst[len(parts[-1]):]
        for part in parts:
            if len(part) < n:
                part.extend(remaining_elements)
                remaining_elements = []
                break
        if len(remaining_elements) > 0:
            parts[-1].extend(remaining_elements)
    return parts
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