class TestGetLineNumber(unittest.TestCase):

    def test_returns_1_for_first_character(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3", 0), 1)

    def test_returns_1_for_last_character_of_first_line(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3", 5), 1)

    def test_returns_3_for_last_character_of_third_line(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3", 18), 3)

    def test_returns_1_for_single_line_string(self):
        self.assertEqual(get_line_number("Single line string", 0), 1)

    def test_returns_3_for_index_in_multiline_string_with_trailing_newlines(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3\n\n", 15), 3)
