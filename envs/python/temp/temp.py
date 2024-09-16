import pandas as pd
import xmltodict
import os

def xml_to_dataframe(xml_file: str) -> pd.DataFrame:
    """
    Convert the XML file into a pandas DataFrame.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        pd.DataFrame: DataFrame containing the question from the XML file.
    """
    # Check if the file exists
    if not os.path.exists(xml_file):
        raise FileNotFoundError(f"The file {xml_file} does not exist.")

    # Parse the XML file into a dictionary
    with open(xml_file, 'r') as f:
        data = xmltodict.parse(f.read())

    # Extract the sequence tags
    sequences = data['sequence']

    # If there's only one sequence, convert it to a list
    if not isinstance(sequences, list):
        sequences = [sequences]

    # Initialize an empty list to store the question
    data_list = []

    # Iterate over the sequence tags
    for sequence in sequences:
        # Initialize an empty dictionary to store the question for the current sequence
        sequence_data = {}

        # Iterate over the sub-elements
        for key, value in sequence.items():
            # If the value is a dictionary, recursively extract the question
            if isinstance(value, dict):
                sub_elements = {sub_key: sub_value for sub_key, sub_value in value.items() if sub_key!='sequence'}
                sequence_data.update(sub_elements)
            else:
                # Otherwise, add the key-value pair to the dictionary
                sequence_data[key] = value

        # Add the question for the current sequence to the list
        data_list.append(sequence_data)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data_list)

    return df
import unittest
import pandas as pd
from io import StringIO
import xml.etree.ElementTree as ET

class TestXmlToDataFrame(unittest.TestCase):
    def test_single_sequence(self):
        xml_data = """<root>
                        <sequence>
                            <name>John</name>
                            <age>30</age>
                        </sequence>
                      </root>"""
        xml_input = StringIO(xml_data)
        df = xml_to_dataframe(xml_input)
        expected = pd.DataFrame([{'name': 'John', 'age': '30'}])
        pd.testing.assert_frame_equal(df, expected)

    def test_multiple_sequences(self):
        xml_data = """<root>
                        <sequence>
                            <name>Alice</name>
                            <age>25</age>
                        </sequence>
                        <sequence>
                            <name>Bob</name>
                            <age>22</age>
                        </sequence>
                      </root>"""
        xml_input = StringIO(xml_data)
        df = xml_to_dataframe(xml_input)
        expected = pd.DataFrame([{'name': 'Alice', 'age': '25'}, {'name': 'Bob', 'age': '22'}])
        pd.testing.assert_frame_equal(df, expected)

    def test_empty_sequence(self):
        xml_data = """<root>
                        <sequence></sequence>
                      </root>"""
        xml_input = StringIO(xml_data)
        df = xml_to_dataframe(xml_input)
        expected = pd.DataFrame([{}])
        pd.testing.assert_frame_equal(df, expected)

    def test_mixed_content(self):
        xml_data = """<root>
                        <sequence>
                            <name>Chris</name>
                        </sequence>
                        <sequence>
                            <age>28</age>
                        </sequence>
                      </root>"""
        xml_input = StringIO(xml_data)
        df = xml_to_dataframe(xml_input)
        expected = pd.DataFrame([{'name': 'Chris', 'age': None}, {'name': None, 'age': '28'}])
        pd.testing.assert_frame_equal(df, expected)

    def test_no_sequences(self):
        xml_data = """<root></root>"""
        xml_input = StringIO(xml_data)
        df = xml_to_dataframe(xml_input)
        expected = pd.DataFrame()
        pd.testing.assert_frame_equal(df, expected)

if __name__ == '__main__':    unittest.main()