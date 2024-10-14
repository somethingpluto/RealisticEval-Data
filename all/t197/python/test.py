import unittest


class TestFindOrder(unittest.TestCase):

    def test_find_order_two_players(self):
        self.assertEqual(find_order(2), [2, 1])

    def test_find_order_three_players(self):
        self.assertEqual(find_order(3), [2, 3, 1])

    def test_find_order_five_players(self):
        self.assertEqual(find_order(5), [2, 5, 3, 4, 1])

    def test_find_order_seven_players(self):
        self.assertEqual(find_order(7), [2, 5, 4, 1, 6, 7, 3])

    def test_find_order_ten_players(self):
        self.assertEqual(find_order(10), [2, 5, 10, 9, 7, 3, 4, 6, 8, 1])
