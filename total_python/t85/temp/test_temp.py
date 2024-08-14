import unittest

import pandas as pd


class TestFillNaWithLastValid(unittest.TestCase):
    def setUp(self):
        # Common DataFrame used for testing
        self.data = {
            'A': [1, 2, None, 4, None, None, 7],
            'B': ['a', 'b', 'c', None, None, 'f', 'g']
        }
        self.df = pd.DataFrame(self.data)

    def test_fill_na_success(self):
        # Test filling NA successfully
        result_df = fill_na_with_last_valid(self.df.copy(), 'A')
        expected = pd.DataFrame({
            'A': [1, 2, 2, 4, 2, 2, 7],
            'B': ['a', 'b', 'c', None, None, 'f', 'g']
        })
        pd.testing.assert_frame_equal(result_df, expected)

    def test_fill_na_no_na(self):
        # Test column with no NA values
        result_df = fill_na_with_last_valid(self.df.copy(), 'B')
        expected = pd.DataFrame({
            'A': [1, 2, None, 4, None, None, 7],
            'B': ['a', 'b', 'c', 'c', 'c', 'f', 'g']
        })
        pd.testing.assert_frame_equal(result_df, expected)

    def test_nonexistent_column(self):
        # Test with a column that does not exist
        with self.assertRaises(ValueError):
            fill_na_with_last_valid(self.df.copy(), 'C')

    def test_empty_dataframe(self):
        # Test with an empty DataFrame
        empty_df = pd.DataFrame()
        with self.assertRaises(ValueError):
            fill_na_with_last_valid(empty_df, 'A')

    def test_no_na_in_dataframe(self):
        # Test DataFrame that has no NA at all
        df_no_na = pd.DataFrame({
            'A': [1, 2, 3, 4, 5, 6, 7],
            'B': ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        })
        result_df = fill_na_with_last_valid(df_no_na.copy(), 'A')
        pd.testing.assert_frame_equal(result_df, df_no_na)
import pandas as pd

def fill_na_with_last_valid(df, column_name):
    """
    Populates subsequent NA values in the specified column of the DataFrame with the last valid value.

    Args:
    df (pd.DataFrame): The DataFrame to process.
    column_name (str): The name of the column to fill NA values in.

    Returns:
    pd.DataFrame: The DataFrame with NA values filled.
    """
    if column_name in df.columns:
        df[column_name] = df[column_name].fillna(method='ffill')
    else:
        raise ValueError(f"Column '{column_name}' not found in DataFrame.")
    return df