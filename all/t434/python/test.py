import unittest


class TestGetMaxPeople(unittest.TestCase):
    def test_case_1(self):
        people = [1, 2, 1]
        status = ['+', '+', '-']
        expected = 1
        self.assertEqual(get_max_people(people, status), expected)

    def test_case_2(self):
        people = [1, 2, 3]
        status = ['+', '+', '-']
        expected = -1
        self.assertEqual(get_max_people(people, status), expected)

    def test_case_3(self):
        people = [1, 2, 1]
        status = ['+', '-', '+']
        expected = -1
        self.assertEqual(get_max_people(people, status), expected)

    def test_case_4(self):
        people = [1, 2, 1]
        status = ['+', '+', '+']
        expected = -1
        self.assertEqual(get_max_people(people, status), expected)

    def test_case_5(self):
        people = [1, 2, 1]
        status = ['+', '+', '+']
        expected = -1
        self.assertEqual(get_max_people(people, status), expected)
