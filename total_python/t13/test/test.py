import unittest

from total.t13.adapted import parse_markdown_table


class TestMarkdownTableParsing(unittest.TestCase):
    def test_basic_table_parsing(self):
        markdown = """
        | Name  | Age | Gender |
        |-------|-----|--------|
        | Alice | 24  | Female |
        | Bob   | 29  | Male   |
        """
        expected_output = [
            ('Name', 'Age', 'Gender'),
            ('Alice', '24', 'Female'),
            ('Bob', '29', 'Male')
        ]
        self.assertEqual(parse_markdown_table(markdown), expected_output)

    def test_incorrect_cells_count(self):
        markdown = """
        | Name  | Age | Gender |
        |-------|-----|--------|
        | Alice | 24  |
        """
        with self.assertRaises(ValueError):
            parse_markdown_table(markdown)
