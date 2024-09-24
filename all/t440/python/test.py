import unittest

import pandas as pd


class TestCountValueFrequencies(unittest.TestCase):

    def test_single_value_column(self):
        df = pd.DataFrame({'A': [1, 1, 1, 1]})
        expected = pd.Series([4], index=[1], name='A')
        result = count_value_frequencies(df, 'A')
        pd.testing.assert_series_equal(result, expected)

    def test_multiple_values(self):
        df = pd.DataFrame({'A': [1, 2, 2, 3, 1]})
        expected = pd.Series([2, 2, 1], index=[1, 2, 3], name='A')
        result = count_value_frequencies(df, 'A')
        pd.testing.assert_series_equal(result, expected)

    def test_empty_column(self):
        df = pd.DataFrame({'A': []})
        expected = pd.Series(dtype=int, name='A')
        result = count_value_frequencies(df, 'A')
        pd.testing.assert_series_equal(result, expected)

    def test_nonexistent_column(self):
        df = pd.DataFrame({'A': [1, 2, 3]})
        with self.assertRaises(KeyError):
            count_value_frequencies(df, 'B')

    def test_string_values(self):
        df = pd.DataFrame({'B': ['apple', 'banana', 'apple', 'orange', 'banana']})
        expected = pd.Series([2, 2, 1], index=['apple', 'banana', 'orange'], name='B')
        result = count_value_frequencies(df, 'B')
        pd.testing.assert_series_equal(result, expected)
