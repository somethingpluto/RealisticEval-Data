import pandas as pd

def convert_dataframe_to_markdown(df: pd.DataFrame, md_path: str) -> str:
    md_content = ""
    md_content += "| " + " | ".join(df.columns) + " |\n"
    md_content += "| " + " | ".join(["---" for _ in range(len(df.columns))]) + " |\n"
    
    for index, row in df.iterrows():
        md_content += "| " + " | ".join([str(val) for val in row]) + " |\n"

    with open(md_path, "w") as f:
        f.write(md_content)
    
    return md_content
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