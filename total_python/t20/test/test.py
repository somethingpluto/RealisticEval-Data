import unittest


class TestProcessMarkdown(unittest.TestCase):


    def test_single_asterisk_pair(self):
        content = "This is a *test* string."
        expected = "This is a *test* string."
        self.assertEqual(process_markdown(content), expected)

    def test_nested_asterisks(self):
        content = "Example of **nested *asterisks***."
        expected = "Example of *nested asterisks*."
        self.assertEqual(process_markdown(content), expected)

    def test_multiple_asterisk_pairs(self):
        content = "*Multiple* pairs of *asterisks* in *one* sentence."
        expected = "*Multiple pairs of asterisks in one* sentence."
        self.assertEqual(process_markdown(content), expected)

    def test_asterisks_with_no_text(self):
        content = "Asterisks with ** no text."
        expected = "Asterisks with ** no text."
        self.assertEqual(process_markdown(content), expected)

    def test_asterisks_around_spaces(self):
        content = "Asterisks around * *spaces* * are tricky."
        expected = "Asterisks around * spaces * are tricky."
        self.assertEqual(process_markdown(content), expected)