import unittest


class TestFillNaWithLastValid(unittest.TestCase):
    def setUp(self):
        # Common DataFrame used for testing
        self.data = {
            'A': [None, 2, None, 4, None, None, 7],
            'B': ['a', None, None, 'd', 'e', None, 'g']
        }
        self.df = pd.DataFrame(self.data)

    def test_fill_na_in_int_column(self):
        # Test filling NA in integer column
        df = self.df.copy()
        result_df = fill_na_with_last_valid(df, 'A')
        expected_data = [None, 2, 2, 4, 4, 4, 7]
        pd.testing.assert_series_equal(result_df['A'], pd.Series(expected_data, name='A'))

    def test_fill_na_in_string_column(self):
        # Test filling NA in string column
        df = self.df.copy()
        result_df = fill_na_with_last_valid(df, 'B')
        expected_data = ['a', 'a', 'a', 'd', 'e', 'e', 'g']
        pd.testing.assert_series_equal(result_df['B'], pd.Series(expected_data, name='B'))

    def test_nonexistent_column(self):
        # Test with a column that does not exist
        df = self.df.copy()
        with self.assertRaises(ValueError):
            fill_na_with_last_valid(df, 'C')

    def test_empty_dataframe(self):
        # Test with an empty DataFrame
        df = pd.DataFrame()
        with self.assertRaises(ValueError):
            fill_na_with_last_valid(df, 'A')

    def test_no_na_to_fill(self):
        # Test DataFrame where no NA exists in the specified column
        data = {'A': [1, 2, 3, 4, 5, 6, 7]}
        df = pd.DataFrame(data)
        result_df = fill_na_with_last_valid(df, 'A')
        expected_df = pd.DataFrame(data)
        pd.testing.assert_frame_equal(result_df, expected_df)