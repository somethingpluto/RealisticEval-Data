import unittest


class TestMarkdownProcessing(unittest.TestCase):
    def test_single_asterisk_pair(self):
        content = "* some text*"
        expected = "*some text*"
        self.assertEqual(process_markdown_content(content), expected, "Should remove spaces around single asterisk pair")

    def test_multiple_asterisk_pairs(self):
        content = "Here is * some * text * with * extra * spaces*."
        expected = "Here is *some* text *with* extra *spaces*."
        self.assertEqual(process_markdown_content(content), expected, "Should remove spaces in multiple asterisk pairs")

    def test_no_asterisks(self):
        content = "This is a test with no asterisks."
        expected = "This is a test with no asterisks."
        self.assertEqual(process_markdown_content(content), expected, "Should remain unchanged without asterisks")

    def test_asterisks_with_no_spaces(self):
        content = "Markdown with *correct*formatting."
        expected = "Markdown with *correct*formatting."
        self.assertEqual(process_markdown_content(content), expected, "Should remain unchanged with correct formatting")

    def test_edge_cases_with_spaces(self):
        content = "*  leading and trailing spaces  * are tricky!"
        expected = "*leading and trailing spaces* are tricky!"
        self.assertEqual(process_markdown_content(content), expected, "Should handle leading and trailing spaces inside asterisks")