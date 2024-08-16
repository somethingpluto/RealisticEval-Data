import unittest
import pandas as pd


class TestPopulateNAWithFirstValid(unittest.TestCase):

    def test_normal_case(self):
        """ Test with normal input where replacement is possible. """
        df = pd.DataFrame({'A': [None, 2, None, 4]})
        expected = pd.DataFrame({'A': [2, 2, 2, 4]})
        result = populate_na_with_first_valid(df, 'A')
        pd.testing.assert_frame_equal(result, expected)

    def test_all_na(self):
        """ Test a column that is entirely NA to see if it remains unchanged. """
        df = pd.DataFrame({'A': [None, None, None, None]})
        expected = pd.DataFrame({'A': [None, None, None, None]})
        result = populate_na_with_first_valid(df, 'A')
        pd.testing.assert_frame_equal(result, expected)

    def test_no_na(self):
        """ Test a column with no NA values to see if it remains unchanged. """
        df = pd.DataFrame({'A': [1, 2, 3, 4]})
        expected = pd.DataFrame({'A': [1, 2, 3, 4]})
        result = populate_na_with_first_valid(df, 'A')
        pd.testing.assert_frame_equal(result, expected)

    def test_invalid_column(self):
        """ Test with a column name that does not exist in the DataFrame. """
        df = pd.DataFrame({'A': [1, 2, 3, 4]})
        with self.assertRaises(ValueError):
            populate_na_with_first_valid(df, 'B')

    def test_first_entry_na(self):
        """ Test when the first entry is NA but there is a valid entry later. """
        df = pd.DataFrame({'A': [None, None, 2, None]})
        expected = pd.DataFrame({'A': [2, 2, 2, 2]})
        result = populate_na_with_first_valid(df, 'A')
        pd.testing.assert_frame_equal(result, expected)