class TestGetCurrentDate(unittest.TestCase):

    def test_should_return_a_string_in_the_format_YYYY_MM_DD(self):
        """Test that the return value is a string in the format YYYY-MM-DD."""
        date = get_current_date()
        self.assertIsInstance(date, str)
        self.assertRegex(date, r'^\d{4}-\d{2}-\d{2}$')

    def test_should_return_the_correct_date_for_today(self):
        """Test that the returned date is today's date in YYYY-MM-DD format."""
        expected_date = datetime.now().strftime('%Y-%m-%d')
        actual_date = get_current_date()
        self.assertEqual(actual_date, expected_date)

    def test_should_return_the_correct_year_part_in_YYYY_MM_DD(self):
        """Test that the returned date has the correct year part (YYYY)."""
        current_year = datetime.now().year
        actual_date = get_current_date()
        self.assertTrue(actual_date.startswith(str(current_year)))

    def test_should_return_the_correct_month_part_in_YYYY_MM_DD(self):
        """Test that the returned date has the correct month part (MM)."""
        current_month = datetime.now().strftime('%m')  # Zero-padded month
        actual_date = get_current_date()
        self.assertEqual(actual_date[5:7], current_month)

    def test_should_return_the_correct_day_part_in_YYYY_MM_DD(self):
        """Test that the returned date has the correct day part (DD)."""
        current_day = datetime.now().strftime('%d')  # Zero-padded day
        actual_date = get_current_date()
        self.assertEqual(actual_date[8:10], current_day)
