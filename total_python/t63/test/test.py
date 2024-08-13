import unittest
import pandas as pd

class TestDataFrameToMarkdown(unittest.TestCase):

    def test_empty_dataframe(self):
        """ Test an empty DataFrame """
        df = pd.DataFrame()
        expected_output = "| \n| --- \n"
        self.assertEqual(dataframe_to_markdown(df), expected_output)

    def test_single_column_single_row(self):
        """ Test a DataFrame with one column and one row """
        df = pd.DataFrame({
            'Name': ['Alice']
        })
        expected_output = "| Name |\n| --- |\n| Alice |\n"
        self.assertEqual(dataframe_to_markdown(df), expected_output)

    def test_multiple_columns_multiple_rows(self):
        """ Test a DataFrame with multiple columns and multiple rows """
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob'],
            'Age': [25, 30]
        })
        expected_output = "| Name | Age |\n| --- | --- |\n| Alice | 25 |\n| Bob | 30 |\n"
        self.assertEqual(dataframe_to_markdown(df), expected_output)

    def test_numeric_columns(self):
        """ Test a DataFrame with numeric columns """
        df = pd.DataFrame({
            1: [100, 200],
            2: [300, 400]
        })
        expected_output = "| 1 | 2 |\n| --- | --- |\n| 100 | 300 |\n| 200 | 400 |\n"
        self.assertEqual(dataframe_to_markdown(df), expected_output)

    def test_mixed_types(self):
        """ Test a DataFrame with mixed data types """
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob'],
            'Age': [25, 30],
            'Married': [True, False]
        })
        expected_output = "| Name | Age | Married |\n| --- | --- | --- |\n| Alice | 25 | True |\n| Bob | 30 | False |\n"
        self.assertEqual(dataframe_to_markdown(df), expected_output)