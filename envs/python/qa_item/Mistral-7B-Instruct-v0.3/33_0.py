import xml.etree.ElementTree as ET
import pandas as pd

def parse_xml_to_dataframe(xml_file: str) -> pd.DataFrame:
    """
    Convert the XML file into a pandas DataFrame, where each <sequence> tag is treated as a row record in the XML,
    and the tag and text content of each sub-element are treated as columns of the DataFrame.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        pd.DataFrame: DataFrame containing the data extracted from the XML file.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initialize an empty list to store the data
    data = []

    # Iterate through each <sequence> tag
    for sequence in root.findall('sequence'):
        row = {}

        # Iterate through each sub-element of the current <sequence> tag
        for element in sequence:
            # Add the tag name as the column name and the text content as the value
            row[element.tag] = element.text

        # Append the row to the data list
        data.append(row)

    # Convert the data list into a DataFrame
    df = pd.DataFrame(data)

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
        df = parse_xml_to_dataframe(xml_input)
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
        df = parse_xml_to_dataframe(xml_input)
        expected = pd.DataFrame([{'name': 'Alice', 'age': '25'}, {'name': 'Bob', 'age': '22'}])
        pd.testing.assert_frame_equal(df, expected)

    def test_empty_sequence(self):
        xml_data = """<root>
                        <sequence></sequence>
                      </root>"""
        xml_input = StringIO(xml_data)
        df = parse_xml_to_dataframe(xml_input)
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
        df = parse_xml_to_dataframe(xml_input)
        expected = pd.DataFrame([{'name': 'Chris', 'age': None}, {'name': None, 'age': '28'}])
        pd.testing.assert_frame_equal(df, expected)

    def test_no_sequences(self):
        xml_data = """<root></root>"""
        xml_input = StringIO(xml_data)
        df = parse_xml_to_dataframe(xml_input)
        expected = pd.DataFrame()
        pd.testing.assert_frame_equal(df, expected)

if __name__ == '__main__':
    unittest.main()