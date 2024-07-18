import unittest

from task_code.t5.adapted import parse_to_list


class TestParseToList(unittest.TestCase):
    def test_none_input(self):
        self.assertIsNone(parse_to_list(None), "Should return None for None input")

    def test_list_input(self):
        self.assertEqual(parse_to_list(["item1", "item2"]), "item1, item2", "Should handle list input correctly")

    def test_multiline_string(self):
        self.assertEqual(parse_to_list("item1\nitem2\nitem3"), "'item1', 'item2', 'item3'",
                         "Should handle multiline string correctly")

    def test_mixed_separators(self):
        self.assertEqual(parse_to_list("item1, item2; item3 * item4"), "'item1', 'item2', 'item3', 'item4'",
                         "Should handle mixed separators correctly")

    def test_complex_input(self):
        self.assertEqual(parse_to_list("item1 * item2\nitem3, item4\nitem5; item6"),
                         "'item1', 'item2', 'item3', 'item4', 'item5', 'item6'",
                         "Should handle complex input correctly")
