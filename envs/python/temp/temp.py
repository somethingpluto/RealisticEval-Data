import pandas as pd

def count_value_frequencies(df, column_name):
    """
    Count the frequency of different values in a specified column of a DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to count values.

    Returns:
    pd.Series: A Series with values and their corresponding frequencies.
    """
    return df[column_name].value_counts().to_list()
import unittest

import pandas as pd


class TestCountValueFrequencies(unittest.TestCase):

    def setUp(self):
        # Create sample DataFrames for testing
        self.df1 = pd.DataFrame({
            'A': ['apple', 'banana', 'apple', 'orange', 'banana', 'banana'],
            'B': [1, 2, 3, 4, 5, 6]
        })

        self.df2 = pd.DataFrame({
            'A': ['red', 'blue', 'green', 'blue', 'red', 'red'],
            'B': [10, 20, 30, 40, 50, 60]
        })

        self.df3 = pd.DataFrame({
            'A': [],
            'B': []
        })

        self.df4 = pd.DataFrame({
            'A': ['cat', 'dog', 'cat', 'cat', 'dog', 'mouse'],
            'B': [100, 200, 300, 400, 500, 600]
        })

        self.df5 = pd.DataFrame({
            'A': [None, None, None, None],
            'B': [7, 8, 9, 10]
        })

    def test_basic_frequencies(self):
        result = count_value_frequencies(self.df1, 'A')
        expected = pd.Series({'banana': 3, 'apple': 2, 'orange': 1})
        expected = expected.sort_index()  # Sort for comparison
        result = result.sort_index()  # Sort for comparison
        pd.testing.assert_series_equal(result, expected)

    def test_different_values(self):
        result = count_value_frequencies(self.df2, 'A')
        expected = pd.Series({'red': 3, 'blue': 2, 'green': 1})
        expected = expected.sort_index()  # Sort for comparison
        result = result.sort_index()  # Sort for comparison
        pd.testing.assert_series_equal(result, expected)

    def test_empty_dataframe(self):
        result = count_value_frequencies(self.df3, 'A')
        expected = pd.Series(dtype='int64')  # Expect an empty Series
        pd.testing.assert_series_equal(result, expected)

    def test_multiple_same_values(self):
        result = count_value_frequencies(self.df4, 'A')
        expected = pd.Series({'cat': 3, 'dog': 2, 'mouse': 1})
        expected = expected.sort_index()  # Sort for comparison
        result = result.sort_index()  # Sort for comparison
        pd.testing.assert_series_equal(result, expected)

    def test_null_values(self):
        result = count_value_frequencies(self.df5, 'A')
        expected = pd.Series({None: 4})  # Expect a Series with None counted
        pd.testing.assert_series_equal(result, expected)
if __name__ == '__main__':
    unittest.main()