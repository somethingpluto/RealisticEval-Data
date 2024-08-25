import unittest
import pandas as pd
import os


class TestCommonColumns(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory
        self.test_dir = "test_dir"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Remove created files and directory after each test
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
        self.assertEqual(set(find_common_columns(self.test_dir)), set(['C', 'B', 'A']))

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
        self.assertEqual(find_common_columns(self.test_dir), [])

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
        self.assertEqual(find_common_columns(self.test_dir), ['C'])

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
        self.assertEqual(set(find_common_columns(self.test_dir)), set(['B', 'C']))
