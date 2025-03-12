import pandas as pd

def fill_missing_with_first_valid(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    # Get the first not-null value for the specified column
    first_valid = df[column_name].dropna().iloc[0]

    # Fill missing values in the specified column with the first valid value
    df[column_name].fillna(first_valid, inplace=True)

    return df
import unittest

import pandas as pd


class TestFillMissingWithFirstValid(unittest.TestCase):

    def test_basic_filling(self):
        df = pd.DataFrame({'A': [1, None, 3, None], 'B': ['foo', 'bar', None, 'baz']})
        result = fill_missing_with_first_valid(df, 'B')
        expected = pd.DataFrame({'A': [1, None, 3, None], 'B': ['foo', 'bar', 'foo', 'baz']})
        pd.testing.assert_frame_equal(result, expected)

    def test_no_missing_values(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': ['foo', 'bar', 'baz']})
        result = fill_missing_with_first_valid(df, 'B')
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': ['foo', 'bar', 'baz']})
        pd.testing.assert_frame_equal(result, expected)


    def test_single_valid_value(self):
        df = pd.DataFrame({'A': [1, None, None, 4], 'B': [None, 'bar', None, None]})
        result = fill_missing_with_first_valid(df, 'B')
        expected = pd.DataFrame({'A': [1, None, None, 4], 'B': ['bar', 'bar', 'bar', 'bar']})
        pd.testing.assert_frame_equal(result, expected)

    def test_multiple_valid_values(self):
        df = pd.DataFrame({'A': [1, None, 3, 4], 'B': [None, 'bar', 'foo', None]})
        result = fill_missing_with_first_valid(df, 'B')
        expected = pd.DataFrame({'A': [1, None, 3, 4], 'B': ['bar', 'bar', 'foo', 'bar']})
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()