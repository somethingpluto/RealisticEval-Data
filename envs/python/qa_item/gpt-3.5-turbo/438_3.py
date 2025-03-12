import pandas as pd

def read_csv_to_dataframe(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and converts it to a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the data from the CSV file.
    """
    df = pd.read_csv(file_path)
    return df
import unittest
import pandas as pd
import os


class TestReadCsvToDataFrame(unittest.TestCase):

    def setUp(self):
        """Set up temporary CSV files for testing."""
        # Create a valid CSV file
        self.valid_csv_path = 'valid.csv'
        pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}).to_csv(self.valid_csv_path, index=False)

        # Create an empty CSV file
        self.empty_csv_path = 'empty.csv'
        open(self.empty_csv_path, 'w').close()

        # Create an invalid format CSV file
        self.invalid_csv_path = 'invalid.csv'
        with open(self.invalid_csv_path, 'w') as f:
            f.write("col1, col2\n1, 2\n3, 4\ninvalid_line")

    def tearDown(self):
        """Clean up temporary files after tests."""
        if os.path.exists(self.valid_csv_path):
            os.remove(self.valid_csv_path)
        if os.path.exists(self.empty_csv_path):
            os.remove(self.empty_csv_path)
        if os.path.exists(self.invalid_csv_path):
            os.remove(self.invalid_csv_path)

    def test_valid_csv(self):
        """Test reading a valid CSV file."""
        df = read_csv_to_dataframe(self.valid_csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2, 2))
        self.assertListEqual(list(df.columns), ['col1', 'col2'])



    def test_correct_data(self):
        """Test if the correct data is read from the CSV file."""
        df = read_csv_to_dataframe(self.valid_csv_path)
        expected_data = {'col1': [1, 2], 'col2': [3, 4]}
        pd.testing.assert_frame_equal(df, pd.DataFrame(expected_data))

    def test_read_csv_with_missing_values(self):
        """Test reading a CSV file with missing values."""
        missing_values_csv_path = 'missing_values.csv'
        pd.DataFrame({'col1': [1, None], 'col2': [None, 4]}).to_csv(missing_values_csv_path, index=False)
        df = read_csv_to_dataframe(missing_values_csv_path)
        self.assertTrue(df.isnull().values.any())
        os.remove(missing_values_csv_path)

    def test_large_csv_file(self):
        """Test reading a large CSV file."""
        large_csv_path = 'large.csv'
        large_df = pd.DataFrame({'col1': range(1000), 'col2': range(1000, 2000)})
        large_df.to_csv(large_csv_path, index=False)
        df = read_csv_to_dataframe(large_csv_path)
        self.assertEqual(df.shape, (1000, 2))
        os.remove(large_csv_path)
if __name__ == '__main__':
    unittest.main()