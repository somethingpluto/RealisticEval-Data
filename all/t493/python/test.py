import unittest


class TestWrapContentGenerator(unittest.TestCase):
    def test_normal_text(self):
        content = "This is a test of the wrap function."
        expected_output = [
            'This is a test of the wrap function.\n'
        ]
        self.assertEqual(list(wrap_content_generator(content, width=50)), expected_output)

    def test_long_line(self):
        content = "This line is going to be very long and should be wrapped properly according to the specified width."
        expected_output = [
            'This line is going to be very long and should be wrapped\n',
            'properly according to the specified width.\n'
        ]
        self.assertEqual(list(wrap_content_generator(content, width=40)), expected_output)

    def test_multiple_lines(self):
        content = "First line.\nSecond line that is a bit longer.\nThird line."
        expected_output = [
            'First line.\n',
            'Second line that is a bit longer.\n',
            'Third line.\n'
        ]
        self.assertEqual(list(wrap_content_generator(content, width=30)), expected_output)

    def test_empty_lines(self):
        content = "First line.\n\nSecond line.\n\n\nThird line."
        expected_output = [
            'First line.\n',
            '\n',
            'Second line.\n',
            '\n',
            '\n',
            'Third line.\n'
        ]
        self.assertEqual(list(wrap_content_generator(content, width=50)), expected_output)

    def test_combined_cases(self):
        content = "This is a test.\n\nThis line is way too long to fit in one line and needs to be wrapped.\nFinal line."
        expected_output = [
            'This is a test.\n',
            '\n',
            'This line is way too long to fit in one line and\n',
            'needs to be wrapped.\n',
            'Final line.\n'
        ]
        self.assertEqual(list(wrap_content_generator(content, width=40)), expected_output)