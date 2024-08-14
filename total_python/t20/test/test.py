import unittest


class TestProcessMarkdown(unittest.TestCase):
    def test_basic_asterisks(self):
        content = "*some*text*"
        expected = "*sometext*"
        self.assertEqual(process_markdown(content), expected)

    def test_nested_asterisks(self):
        content = "*some*more**complex*text**"
        expected = "*somemore complex text*"
        self.assertEqual(process_markdown(content), expected)

    def test_multiple_emphasis_blocks(self):
        content = "*hello* world, this is *some*text*"
        expected = "*hello* world, this is *sometext*"
        self.assertEqual(process_markdown(content), expected)

    def test_no_asterisks(self):
        content = "No asterisks here"
        expected = "No asterisks here"
        self.assertEqual(process_markdown(content), expected)

    def test_asterisks_with_spaces(self):
        content = "* some * *text* here *"
        expected = "* some * *text* here *"
        self.assertEqual(process_markdown(content), expected)
