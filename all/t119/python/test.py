class TestGetCookie(unittest.TestCase):

    def setUp(self):
        """Clear cookies before each test"""
        self.cookie_string = ''  # Start with no cookies

    def test_returns_correct_cookie_value_for_existing_cookie(self):
        """Test: Returns correct cookie value for existing cookie"""
        self.cookie_string = "username=JohnDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/"
        result = get_cookie('username', self.cookie_string)
        self.assertEqual(result, 'JohnDoe')

    def test_returns_none_if_cookie_does_not_exist(self):
        """Test: Returns None if cookie does not exist"""
        self.cookie_string = "username=JohnDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/"
        result = get_cookie('user', self.cookie_string)
        self.assertIsNone(result)

    def test_returns_none_when_no_cookies_are_set(self):
        """Test: Returns None when no cookies are set"""
        result = get_cookie('username', self.cookie_string)
        self.assertIsNone(result)

    def test_handles_multiple_cookies_and_retrieves_correct_one(self):
        """Test: Handles multiple cookies and retrieves the correct one"""
        self.cookie_string = "user=JaneDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/"
        self.cookie_string += "; username=JohnDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/"
        result = get_cookie('username', self.cookie_string)
        self.assertEqual(result, 'JohnDoe')
