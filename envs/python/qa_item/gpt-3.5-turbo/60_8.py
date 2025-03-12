from typing import List
import os
import pandas as pd

def get_common_columns_from_csvs(directory: str) -> List:
    common_columns = None
    first = True
    
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            df = pd.read_csv(file_path)
            columns = set(df.columns)
            
            if first:
                common_columns = columns
                first = False
            else:
                common_columns = common_columns.intersection(columns)
    
    return list(common_columns) if common_columns else []
import unittest
import pandas as pd
import os


class TestCommonColumns(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory
        self.test_dir = "test_dir"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Remove created files and directory after each test.js
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))
        os.rmdir(self.test_dir)

    def test_all_same_columns(self):
        # All CSV files have the same columns
        data1 = "A,B,C\n1,2,3"
        data2 = "A,B,C\n4,5,6"
        data3 = "A,B,C\n7,8,9"
        filenames = ['file1.csv', 'file2.csv', 'file3.csv']
        datas = [data1, data2, data3]
        for filename, data in zip(filenames, datas):
            with open(os.path.join(self.test_dir, filename), 'w') as f:
                f.write(data)
        self.assertEqual(set(get_common_columns_from_csvs(self.test_dir)), set(['C', 'B', 'A']))

    def test_no_common_columns(self):
        # No common columns
        data1 = "A,B,C\n1,2,3"
        data2 = "D,E,F\n4,5,6"
        data3 = "G,H,I\n7,8,9"
        filenames = ['file1.csv', 'file2.csv', 'file3.csv']
        datas = [data1, data2, data3]
        for filename, data in zip(filenames, datas):
            with open(os.path.join(self.test_dir, filename), 'w') as f:
                f.write(data)
        self.assertEqual(get_common_columns_from_csvs(self.test_dir), [])

    def test_some_common_columns(self):
        # Some common columns
        data1 = "A,B,C\n1,2,3"
        data2 = "B,C,D\n4,5,6"
        data3 = "C,D,E\n7,8,9"
        filenames = ['file1.csv', 'file2.csv', 'file3.csv']
        datas = [data1, data2, data3]
        for filename, data in zip(filenames, datas):
            with open(os.path.join(self.test_dir, filename), 'w') as f:
                f.write(data)
        self.assertEqual(get_common_columns_from_csvs(self.test_dir), ['C'])

    def test_mixed_common_and_unique_columns(self):
        # Mixed common and unique columns
        data1 = "A,B,C\n1,2,3"
        data2 = "B,C,D\n4,5,6"
        data3 = "B,C,E\n7,8,9"
        filenames = ['file1.csv', 'file2.csv', 'file3.csv']
        datas = [data1, data2, data3]
        for filename, data in zip(filenames, datas):
            with open(os.path.join(self.test_dir, filename), 'w') as f:
                f.write(data)
        self.assertEqual(set(get_common_columns_from_csvs(self.test_dir)), set(['B', 'C']))

if __name__ == '__main__':
    unittest.main()