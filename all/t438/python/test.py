import os
import unittest

import pandas as pd


class TestReadCsvToDataFrame(unittest.TestCase):

    def setUp(self):
        # Create temporary CSV files for testing
        self.test_files = {
            'valid_csv': 'test_valid.csv',
            'empty_csv': 'test_empty.csv',
            'non_existent_csv': 'non_existent.csv',
            'invalid_csv': 'test_invalid.csv',
            'another_valid_csv': 'test_another_valid.csv',
        }

        # Valid CSV content
        with open(self.test_files['valid_csv'], 'w') as f:
            f.write("name,age\nAlice,30\nBob,25\n")

        # Empty CSV
        with open(self.test_files['empty_csv'], 'w') as f:
            f.write("")

        # Invalid CSV (unparsable)
        with open(self.test_files['invalid_csv'], 'w') as f:
            f.write("name;age\nAlice;30\nBob;25\n")  # wrong delimiter

        # Another valid CSV
        with open(self.test_files['another_valid_csv'], 'w') as f:
            f.write("item,price\napple,1.2\nbanana,0.8\n")

    def tearDown(self):
        # Remove the test CSV files after tests
        for file in self.test_files.values():
            if os.path.exists(file):
                os.remove(file)

    def test_read_valid_csv(self):
        df = read_csv_to_dataframe(self.test_files['valid_csv'])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)  # should have 2 rows of data
        self.assertIn('name', df.columns)
        self.assertIn('age', df.columns)

    def test_read_empty_csv(self):
        df = read_csv_to_dataframe(self.test_files['empty_csv'])
        self.assertIsNone(df)  # expect None for empty file

    def test_read_non_existent_csv(self):
        df = read_csv_to_dataframe(self.test_files['non_existent_csv'])
        self.assertIsNone(df)  # expect None for non-existent file

    def test_read_another_valid_csv(self):
        df = read_csv_to_dataframe(self.test_files['another_valid_csv'])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)  # should have 2 rows of data
        self.assertIn('item', df.columns)
        self.assertIn('price', df.columns)
