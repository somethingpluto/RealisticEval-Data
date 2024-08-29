import unittest
import pandas as pd

class TestNaiveFfill(unittest.TestCase):

    def test_basic_forward_fill(self):
        df = pd.DataFrame({'A': [1, None, 3, None, 5]})
        naive_ffill(df, 'A')
        expected = pd.DataFrame({'A': [1.0, 1.0, 3.0, 3.0, 5.0]})
        pd.testing.assert_frame_equal(df, expected)

    def test_no_missing_values(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        naive_ffill(df, 'A')
        expected = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        pd.testing.assert_frame_equal(df, expected)

    def test_all_missing_values(self):
        df = pd.DataFrame({'A': [None, None, None, None, None]})
        naive_ffill(df, 'A')
        expected = pd.DataFrame({'A': [None, None, None, None, None]})
        pd.testing.assert_frame_equal(df, expected)

    def test_non_existent_column(self):
        df = pd.DataFrame({'A': [1, 2, 3]})
        with self.assertRaises(KeyError):
            naive_ffill(df, 'B')

    def test_multiple_columns(self):
        df = pd.DataFrame({'A': [1, None, 3], 'B': [None, 2, None]})
        naive_ffill(df, 'A')
        expected = pd.DataFrame({'A': [1.0, 1.0, 3.0], 'B': [None, 2, None]})
        pd.testing.assert_frame_equal(df, expected)
import pandas as pd


def naive_ffill(df: pd.DataFrame, column: str) -> None:
    """
    Forward fills missing values in a specified column of a pandas DataFrame using a naive method.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.
    column (str): The name of the column in which to forward fill missing values.

    Returns:
    None: The function modifies the DataFrame in place.

    Raises:
    KeyError: If the specified column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame.")

    last_valid = None
    for idx, value in df[column].items():
        if pd.isna(value):
            df.loc[idx, column] = last_valid
        else:
            last_valid = value