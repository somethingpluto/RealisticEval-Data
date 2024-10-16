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
