class TestGetTime(unittest.TestCase):

    def mock_datetime(self, date_string):
        """Mock the datetime to return a specific date."""
        class MockDate(datetime):
            @classmethod
            def now(cls):
                return datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')

        return MockDate

    @patch('datetime.datetime', new_callable=lambda: datetime)
    def test_should_return_a_string(self, mock_datetime):
        mock_datetime.now = self.mock_datetime('2024-10-01T10:30:00').now
        result = get_time()
        self.assertIsInstance(result, str)

    @patch('datetime.datetime', new_callable=lambda: datetime)
    def test_should_return_formatted_time_string_including_AM_PM(self, mock_datetime):
        mock_datetime.now = self.mock_datetime('2024-10-01T15:45:00').now
        result = get_time()
        self.assertRegex(result, r'^\d{1,2}:\d{2} (AM|PM)$')

    @patch('datetime.datetime', new_callable=lambda: datetime)
    def test_should_return_correct_time_during_AM_hours(self, mock_datetime):
        mock_datetime.now = self.mock_datetime('2024-10-01T08:15:00').now
        result = get_time()
        self.assertEqual(result, '08:15 AM')

    @patch('datetime.datetime', new_callable=lambda: datetime)
    def test_should_return_correct_time_during_PM_hours(self, mock_datetime):
        mock_datetime.now = self.mock_datetime('2024-10-01T17:20:00').now
        result = get_time()
        self.assertEqual(result, '05:20 PM')

    @patch('datetime.datetime', new_callable=lambda: datetime)
    def test_should_return_12_00_AM_at_midnight(self, mock_datetime):
        mock_datetime.now = self.mock_datetime('2024-10-01T00:00:00').now
        result = get_time()
        self.assertEqual(result, '12:00 AM')

    @patch('datetime.datetime', new_callable=lambda: datetime)
    def test_should_return_12_00_PM_at_noon(self, mock_datetime):
        mock_datetime.now = self.mock_datetime('2024-10-01T12:00:00').now
        result = get_time()
        self.assertEqual(result, '12:00 PM')

    @patch('datetime.datetime', new_callable=lambda: datetime)
    def test_should_handle_single_digit_minutes_correctly(self, mock_datetime):
        mock_datetime.now = self.mock_datetime('2024-10-01T09:05:00').now
        result = get_time()
        self.assertEqual(result, '09:05 AM')
