import pandas as pd

def process_csv(file_path: str, output_path: str):
    """
    Processes a CSV file and removes rows with two or more empty columns. If the file is empty, return an empty string.

    Args:
        file_path (str): The path to the input CSV file.
        output_path (str): The path where the processed CSV file will be saved.

    Returns:
        None
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Check if the DataFrame is empty
        if df.empty:
            return ""
        
        # Remove rows with two or more empty columns
        df_cleaned = df.dropna(thresh=df.shape[1] - 1)
        
        # Save the cleaned DataFrame to a new CSV file
        df_cleaned.to_csv(output_path, index=False)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
import unittest
import pandas as pd
from io import StringIO

import os


# Assuming process_csv function is imported from the module
# from your_module import process_csv

class TestProcessCSV(unittest.TestCase):

    def setUp(self):
        self.input_data_1 = """A,B,C
1,2,3
4,,6
7,8,
9,10,11"""


        self.input_data_2 = """A,B,C,D
,,
1,,3,4
2,3,,5
,,,"""


        self.input_data_3 = """A
1
2
3"""


    def process_data(self, input_data):
        input_file = StringIO(input_data)
        output_file = StringIO()
        input_file_path = "input.csv"
        output_file_path = "output.csv"

        # Write input data to a temp CSV file
        with open(input_file_path, 'w') as f:
            f.write(input_data)

        # Process the CSV
        process_csv(input_file_path, output_file_path)

        # Read the output
        with open(output_file_path, 'r') as f:
            output_data = f.read()

        # Clean up temp files
        os.remove(input_file_path)
        os.remove(output_file_path)

        return output_data

    def test_case_1(self):
        output = self.process_data(self.input_data_1)
        expected_output = """A,B,C\n1,2.0,3.0\n4,,6.0\n7,8.0,\n9,10.0,11.0\n"""
        self.assertEqual(output, expected_output)

    def test_case_2(self):
        output = self.process_data(self.input_data_2)
        expected_output = """A,B,C,D\n1.0,,3.0,4.0\n2.0,3.0,,5.0\n"""
        self.assertEqual(output, expected_output)

    def test_case_3(self):
        output = self.process_data(self.input_data_3)
        expected_output = """A\n1\n2\n3\n"""  # Single-column CSV should remain unchanged
        self.assertEqual(output, expected_output)
if __name__ == '__main__':
    unittest.main()