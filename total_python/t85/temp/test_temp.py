import unittest

import pandas as pd


class TestNaiveFfill(unittest.TestCase):
    def setUp(self):
        # Setup a DataFrame with mixed types and missing values
        self.df = pd.DataFrame({
            'A': [1, None, 3, None, 5],
            'B': ['x', 'y', None, 'z', 'a']
        })

    def test_forward_fill_numeric(self):
        # Test forward-filling on a numeric column
        naive_ffill(self.df, 'A')
        expected = pd.Series([1, 1, 3, 3, 5], name='A')
        pd.testing.assert_series_equal(self.df['A'], expected)

    def test_forward_fill_string(self):
        # Test forward-filling on a string column
        naive_ffill(self.df, 'B')
        expected = pd.Series(['x', 'y', 'y', 'z', 'a'], name='B')
        pd.testing.assert_series_equal(self.df['B'], expected)

    def test_no_missing_values(self):
        # Test on a column without missing values
        self.df['C'] = [1, 2, 3, 4, 5]  # Add a column with no NaNs
        naive_ffill(self.df, 'C')
        expected = pd.Series([1, 2, 3, 4, 5], name='C')
        pd.testing.assert_series_equal(self.df['C'], expected)

    def test_invalid_column_name(self):
        # Test with an invalid column name
        with self.assertRaises(KeyError):
            naive_ffill(self.df, 'Z')  # Nonexistent column

    def test_empty_dataframe(self):
        # Test forward-filling on an empty DataFrame
        empty_df = pd.DataFrame()
        with self.assertRaises(KeyError):
            naive_ffill(empty_df, 'A')
import pandas as pd

def naive_ffill(df, column):
    """
    Forward fills the missing values in a specified column of a DataFrame using the last valid value.

    Args:
    df (pd.DataFrame): The DataFrame to process.
    column (str): The name of the column in which to fill missing values.

    Returns:
    None: Modifies the DataFrame in place.

    Raises:
    KeyError: If the specified column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame.")

    last_valid = None
    for idx, value in df[column].iteritems():  # use iteritems() for compatibility
        if pd.isna(value):
            df.at[idx, column] = last_valid
        else:
            last_valid = value