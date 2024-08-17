import unittest


class TestProcessMarkdown(unittest.TestCase):

    def test_simple_case(self):
        # Test with simple asterisks case
        self.assertEqual(process_markdown("*some*text*"), "*sometime *")

    def test_multiple_asterisks_case(self):
        # Test with multiple asterisks surrounding the text
        self.assertEqual(process_markdown("***bold**text*"), "*boldtext*")

    def test_no_asterisks_case(self):
        # Test with no asterisks in the text
        self.assertEqual(process_markdown("plain text"), "plain text")

    def test_nested_asterisks_case(self):
        # Test with nested asterisks in the text
        self.assertEqual(process_markdown("*nest*ed*text*"), "*nestedtext*")

    def test_outermost_asterisks_case(self):
        # Test with multiple layers of outer asterisks
        self.assertEqual(process_markdown("****outer**most*"), "*outermost*")
