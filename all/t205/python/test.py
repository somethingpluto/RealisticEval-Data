class Tester(unittest.TestCase):

    def test_get_current_date_format(self):
        """Correct format YYYY-MM-DD"""
        current_date = get_current_date()
        self.assertEqual(len(current_date), 10)
        self.assertEqual(current_date[4], '-')
        self.assertEqual(current_date[7], '-')

    def test_get_current_date_year(self):
        """Returns correct year"""
        now = datetime.datetime.now()
        current_year = now.year
        current_date = get_current_date()
        year_part = current_date[:4]  # Get the year part
        self.assertEqual(int(year_part), current_year)

    def test_get_current_date_month(self):
        """Returns correct month"""
        now = datetime.datetime.now()
        current_month = now.month
        current_date = get_current_date()
        month_part = current_date[5:7]  # Get the month part
        self.assertEqual(int(month_part), current_month)

    def test_get_current_date_day(self):
        """Returns correct day"""
        now = datetime.datetime.now()
        current_day = now.day
        current_date = get_current_date()
        day_part = current_date[8:10]  # Get the day part
        self.assertEqual(int(day_part), current_day)

    def test_get_current_date_consistency(self):
        """Consistency of output within the same second"""
        first_call = get_current_date()
        second_call = get_current_date()
        self.assertEqual(first_call, second_call)
