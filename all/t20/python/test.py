import unittest
import re


class TestTransformParentheses(unittest.TestCase):

    def test_basic_case(self):
        text = "Hello (*wo*rld*)!"
        expected = "Hello (*world*)!"
        self.assertEqual(transform_parentheses(text), expected)

    def test_multiple_asterisks(self):
        text = "(*he*l*lo*)"
        expected = "(*hello*)"
        self.assertEqual(transform_parentheses(text), expected)

    def test_no_asterisks_inside(self):
        text = "(*hello*)"
        expected = "(*hello*)"
        self.assertEqual(transform_parentheses(text), expected)

    def test_multiple_patterns(self):
        text = "(*hi*), (*there*), (*world*)!"
        expected = "(*hi*), (*there*), (*world*)!"
        self.assertEqual(transform_parentheses(text), expected)

    def test_no_matching_pattern(self):
        text = "This is a test without matching parentheses."
        expected = "This is a test without matching parentheses."
        self.assertEqual(transform_parentheses(text), expected)
