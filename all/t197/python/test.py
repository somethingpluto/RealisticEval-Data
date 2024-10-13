class TestFindOrder(unittest.TestCase):

    def test_find_order_two_players(self):
        tester = Tester()
        self.assertEqual(tester.findOrder(2), [2, 1])

    def test_find_order_three_players(self):
        tester = Tester()
        self.assertEqual(tester.findOrder(3), [2, 3, 1])

    def test_find_order_five_players(self):
        tester = Tester()
        self.assertEqual(tester.findOrder(5), [2, 5, 3, 4, 1])

    def test_find_order_seven_players(self):
        tester = Tester()
        self.assertEqual(tester.findOrder(7), [2, 5, 4, 1, 6, 7, 3])

    def test_find_order_ten_players(self):
        tester = Tester()
        self.assertEqual(tester.findOrder(10), [2, 5, 10, 9, 7, 3, 4, 6, 8, 1])
