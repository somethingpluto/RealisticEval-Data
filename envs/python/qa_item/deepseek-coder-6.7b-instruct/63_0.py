import pandas as pd

def convert_dataframe_to_markdown(df: pd.DataFrame, md_path: str) -> str:
    """
    Convert a DataFrame object to a table in markdown format and save it to a file.

    Args:
        df (DataFrame): DataFrame to be converted.
        md_path (str): Output markdown file path.

    Returns:
        str: Markdown file content as a string.
    """
    # Create the markdown table header
    markdown_header = "| " + " | ".join(df.columns) + " |\n"
    markdown_header += "| " + " | ".join(["---"] * len(df.columns)) + " |\n"

    # Create the markdown table rows
    markdown_rows = []
    for _, row in df.iterrows():
        markdown_rows.append("| " + " | ".join(map(str, row)) + " |")

    # Combine header and rows
    markdown_content = markdown_header + "\n".join(markdown_rows)

    # Write to the markdown file
    with open(md_path, 'w') as md_file:
        md_file.write(markdown_content)

    return markdown_content
import unittest
=import pandas as pd


class TestDataframeToMarkdown(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame
        self.data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
        self.df = pd.DataFrame(self.data)

    def test_df_to_str(self):
        # Test that the function writes the correct markdown to a file
        expected_markdown = "| Name   |   Age |\n|:-------|------:|\n| Alice  |    25 |\n| Bob    |    30 |"
        result = convert_dataframe_to_markdown(self.df, 'dummy_path.md')
        self.assertEqual(result, expected_markdown)

    def test_empty_dataframe(self):
        # Test how the function handles an empty DataFrame
        df_empty = pd.DataFrame()
        expected_markdown = ""
        result = convert_dataframe_to_markdown(df_empty, 'dummy_path.md')
        self.assertEqual(result, expected_markdown)

    def test_single_row_dataframe(self):
        # Test with a DataFrame that contains only one row
        df_single_row = pd.DataFrame({'Name': ['Alice'], 'Age': [30]})
        expected_markdown = "| Name   |   Age |\n|:-------|------:|\n| Alice  |    30 |"
        result = convert_dataframe_to_markdown(df_single_row, 'dummy_path.md')
        self.assertEqual(result, expected_markdown)

    def test_non_string_columns(self):
        # Test with non-string question types in the DataFrame
        df_non_string = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30], 'Height': [5.5, 6.0]})
        expected_markdown = ('| Name   |   Age |   Height |\n'
                             '|:-------|------:|---------:|\n'
                             '| Alice  |    25 |      5.5 |\n'
                             '| Bob    |    30 |      6   |')
        result = convert_dataframe_to_markdown(df_non_string, 'dummy_path.md')
        self.assertEqual(result, expected_markdown)

    def test_special_characters(self):
        # Test handling of special characters in DataFrame
        df_special_chars = pd.DataFrame(
            {'Name': ['Alice', 'Bob'], 'Comments': ['Good@Work!', 'Excellent & Commendable']})
        expected_markdown = ('| Name   | Comments                |\n'
                             '|:-------|:------------------------|\n'
                             '| Alice  | Good@Work!              |\n'
                             '| Bob    | Excellent & Commendable |')
        result = convert_dataframe_to_markdown(df_special_chars, 'dummy_path.md')
        self.assertEqual(result, expected_markdown)


if __name__ == '__main__':
    unittest.main()