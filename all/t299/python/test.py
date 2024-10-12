class TestCalculateAge(unittest.TestCase):

    def test_birthday_today(self):
        self.assertEqual(calculate_age('2000-08-23'), '2000-08-23 (24)')

    def test_birthday_passed_this_year(self):
        self.assertEqual(calculate_age('1990-01-15'), '1990-01-15 (34)')

    def test_birthday_at_end_of_year(self):
        self.assertEqual(calculate_age('1985-12-31'), '1985-12-31 (38)')

    def test_recently_turned_one_year_old(self):
        self.assertEqual(calculate_age('2023-05-05'), '2023-05-05 (1)')

    def test_invalid_date_input(self):
        self.assertEqual(calculate_age('invalid-date'), '')
