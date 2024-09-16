import unittest
import pandas as pd

class TestNaiveFfill(unittest.TestCase):

    def test_basic_forward_fill(self):
        df = pd.DataFrame({'A': [1, None, 3, None, 5]})
        naive_ffill(df, 'A')
        expected = pd.DataFrame({'A': [1, 1, 3, 3, 5]})
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
        expected = pd.DataFrame({'A': [1, 1, 3], 'B': [None, 2, None]})
        pd.testing.assert_frame_equal(df, expected)