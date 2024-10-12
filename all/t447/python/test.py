class TestCalculateAge(unittest.TestCase):

    def test_calculates_age_correctly_for_a_birth_date_in_the_past(self):
        self.assertEqual(calculate_age('2000-01-01'), datetime.now().year - 2000)

    def test_calculates_age_correctly_for_a_birth_date_in_the_long_past(self):
        self.assertEqual(calculate_age('1000-01-01'), datetime.now().year - 1000)

    def test_calculates_age_correctly_for_a_birth_date_today(self):
        today = datetime.now().strftime('%Y-%m-%d')  # Get today's date in YYYY-MM-DD format
        self.assertEqual(calculate_age(today), 0)

    def test_calculates_age_correctly_for_a_person_born_yesterday(self):
        yesterday = datetime.now() - timedelta(days=1)  # Set to yesterday
        birth_date_string = yesterday.strftime('%Y-%m-%d')  # Format as YYYY-MM-DD
        self.assertEqual(calculate_age(birth_date_string), 0)
