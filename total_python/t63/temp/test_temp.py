import unittest
import pandas as pd


class TestDataFrameToMarkdown(unittest.TestCase):

    def test_simple_dataframe(self):
        """Test converting a simple DataFrame to Markdown format."""
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob'],
            'Age': [25, 30]
        })
        expected_output = "| Name | Age |\n|------|-----|\n| Alice | 25 |\n| Bob | 30 |"
        result = dataframe_to_markdown(df)
        self.assertEqual(result.strip(), expected_output.strip())

    def test_empty_dataframe(self):
        """Test converting an empty DataFrame to Markdown format."""
        df = pd.DataFrame()
        expected_output = ""
        result = dataframe_to_markdown(df)
        self.assertEqual(result.strip(), expected_output.strip())

    def test_dataframe_with_special_characters(self):
        """Test a DataFrame with special characters in data."""
        df = pd.DataFrame({
            'Name': ['Alice & Bob', 'Charlie > Dave'],
            'Age': [25, 30]
        })
        expected_output = "| Name | Age |\n|----------|-----|\n| Alice & Bob | 25 |\n| Charlie > Dave | 30 |"
        result = dataframe_to_markdown(df)
        self.assertEqual(result.strip(), expected_output.strip())

    def test_large_dataframe(self):
        """Test converting a larger DataFrame to Markdown format."""
        df = pd.DataFrame({
            'Name': ['Alice'] * 100,
            'Age': list(range(100))
        })
        result = dataframe_to_markdown(df)
        self.assertIn('| Alice | 0 |', result)
        self.assertIn('| Alice | 99 |', result)

    def test_dataframe_with_different_data_types(self):
        """Test a DataFrame with different data types (strings, numbers, floats)."""
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob'],
            'Age': [25, 30],
            'Weight': [55.5, 60.0]
        })
        expected_output = "| Name | Age | Weight |\n|------|-----|--------|\n| Alice | 25 | 55.5 |\n| Bob | 30 | 60.0 |"
        result = dataframe_to_markdown(df)
        self.assertEqual(result.strip(), expected_output.strip())

import pandas as pd


def dataframe_to_markdown(df):
    """
    Convert a pandas DataFrame to a Markdown table format.

    Args:
    df (pd.DataFrame): The DataFrame to convert.

    Returns:
    str: A string representation of the DataFrame in Markdown table format.
    """
    # Start with an empty list to collect rows
    markdown_lines = []

    # Add the header with alignment (assuming left alignment for simplicity)
    header = "| " + " | ".join(df.columns) + " |"
    markdown_lines.append(header)
    markdown_lines.append("|" + "|".join(['---' * (len(col) // 3 + 1) for col in df.columns]) + "|")

    # Add the data rows
    for index, row in df.iterrows():
        row_str = "| " + " | ".join(str(value) for value in row.values) + " |"
        markdown_lines.append(row_str)

    # Join all lines into a single string
    markdown_str = "\n".join(markdown_lines)
    return markdown_str
