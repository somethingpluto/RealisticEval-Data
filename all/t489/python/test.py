import unittest

class TestMarkdownTableFunction(unittest.TestCase):

    def test_basic_table(self):
        data = [
            {"Name": "Alice", "Age": 30, "City": "New York"},
            {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
        ]
        expected_output = (
            "| Name  | Age | City        |\n"
            "| ---   | --- | ---         |\n"
            "| Alice | 30  | New York    |\n"
            "| Bob   | 25  | Los Angeles |"
        )
        self.assertEqual(dict_list_to_markdown_table(data), expected_output)

    def test_empty_list(self):
        data = []
        expected_output = "No data available."
        self.assertEqual(dict_list_to_markdown_table(data), expected_output)

    def test_single_entry(self):
        data = [
            {"Name": "Charlie", "Age": 35, "City": "Chicago"}
        ]
        expected_output = (
            "| Name    | Age | City   |\n"
            "| ---     | --- | ---    |\n"
            "| Charlie | 35  | Chicago |"
        )
        self.assertEqual(dict_list_to_markdown_table(data), expected_output)

    def test_varied_length(self):
        data = [
            {"Name": "Alice", "Age": 30},
            {"Name": "Bob", "City": "Los Angeles"},
            {"Age": 35, "City": "Chicago"}
        ]
        expected_output = (
            "| Name  | Age | City        |\n"
            "| ---   | --- | ---         |\n"
            "| Alice | 30  |             |\n"
            "| Bob   |     | Los Angeles |\n"
            "|       | 35  | Chicago     |"
        )
        self.assertEqual(dict_list_to_markdown_table(data), expected_output)

    def test_different_types(self):
        data = [
            {"Name": "Eve", "Age": 28, "Is_Student": True},
            {"Name": "Frank", "Age": 22, "Is_Student": False}
        ]
        expected_output = (
            "| Name  | Age | Is_Student |\n"
            "| ---   | --- | ---        |\n"
            "| Eve   | 28  | True       |\n"
            "| Frank | 22  | False      |"
        )
        self.assertEqual(dict_list_to_markdown_table(data), expected_output)