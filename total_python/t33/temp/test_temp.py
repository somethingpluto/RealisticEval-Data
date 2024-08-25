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

import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_dataframe(xml_file):
    """
    Convert an XML file into a pandas DataFrame. Each <sequence> tag is treated as a row,
    and each sub-element within <sequence> is treated as a column.

    Args:
    xml_file (str): Path to the XML file.

    Returns:
    pd.DataFrame: DataFrame containing the data from the XML file.
    """
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Prepare a list to hold all rows
    rows = []

    # Iterate over each <sequence> element in the XML file
    for sequence in root.findall('sequence'):
        row_data = {}
        # Iterate over each child of the <sequence> element
        for child in sequence:
            # Use the tag as the column name and the text content as the data
            row_data[child.tag] = child.text
        rows.append(row_data)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(rows)

    return df