from typing import Dict
import xml.etree.ElementTree as ET

def parse_xaml_to_dict(xaml_file: str) -> Dict[str, str]:
    """
    Parse the XAML file, extract the key-value pairs within the String element, and return the result in a dictionary.

    Args:
        xaml_file (str): Path to the XAML file.

    Returns:
        A dictionary containing the key-value pairs extracted from 'String' elements.
    """
    # Parse the XAML file
    tree = ET.parse(xaml_file)
    root = tree.getroot()

    # Namespace dictionary to handle namespaces in XAML
    namespaces = {'x': 'http://schemas.microsoft.com/winfx/2006/xaml/presentation'}

    # Dictionary to store the key-value pairs
    result_dict = {}

    # Find all 'String' elements
    for string_element in root.findall('.//x:String', namespaces):
        # Extract the key and value
        key = string_element.get('Key')
        value = string_element.text

        # Add the key-value pair to the dictionary
        if key and value:
            result_dict[key] = value

    return result_dict
import unittest
import xml.etree.ElementTree as ET
from io import StringIO


class TestParseXamlToDict(unittest.TestCase):
    def test_valid_strings(self):
        xaml_data = """<root>
                         <String Key="Username">Alice</String>
                         <String Key="Password">secret</String>
                       </root>"""
        xaml_input = StringIO(xaml_data)
        expected = {'Username': 'Alice', 'Password': 'secret'}
        result = parse_xaml_to_dict(xaml_input)
        self.assertEqual(result, expected)

    def test_missing_key_attribute(self):
        xaml_data = """<root>
                         <String>Alice</String>
                       </root>"""
        xaml_input = StringIO(xaml_data)
        expected = {}
        result = parse_xaml_to_dict(xaml_input)
        self.assertEqual(result, expected)


    def test_no_string_tags(self):
        xaml_data = """<root>
                         <Data>Some question</Data>
                       </root>"""
        xaml_input = StringIO(xaml_data)
        expected = {}
        result = parse_xaml_to_dict(xaml_input)
        self.assertEqual(result, expected)

    def test_nested_string_tags(self):
        xaml_data = """<root>
                         <Container>
                           <String Key="Username">Bob</String>
                         </Container>
                         <String Key="Location">Earth</String>
                       </root>"""
        xaml_input = StringIO(xaml_data)
        expected = {'Username': 'Bob', 'Location': 'Earth'}
        result = parse_xaml_to_dict(xaml_input)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()