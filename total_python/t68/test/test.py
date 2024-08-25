import unittest


class TestDivideList(unittest.TestCase):
    def test_even_division(self):
        lst = [1, 2, 3, 4, 5, 6]
        n = 3
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(divide_list(lst, n), expected)

    def test_uneven_division(self):
        lst = [1, 2, 3, 4, 5, 6, 7]
        n = 3
        expected = [[1, 2, 3], [4, 5], [6, 7]]
        self.assertEqual(divide_list(lst, n), expected)

    def test_more_parts_than_items(self):
        lst = [1, 2, 3]
        n = 5
        expected = [[1], [2], [3], [], []]
        self.assertEqual(divide_list(lst, n), expected)

    def test_single_element(self):
        lst = [1]
        n = 1
        expected = [[1]]
        self.assertEqual(divide_list(lst, n), expected)

    def test_empty_list(self):
        lst = []
        n = 3
        expected = [[], [], []]
        self.assertEqual(divide_list(lst, n), expected)
