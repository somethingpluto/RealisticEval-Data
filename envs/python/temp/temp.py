import xml.etree.ElementTree as ET


def parse_xaml_to_dict(xaml_file):
    """
    Parse a XAML file and extract key-value pairs from 'String' elements.

    Args:
    xaml_file (str): Path to the XAML file.

    Returns:
    dict: A dictionary containing the key-value pairs extracted from 'String' elements.
    """
    try:
        # Parse the XAML file
        tree = ET.parse(xaml_file)
        root = tree.getroot()

        # Dictionary to hold the key-value pairs
        result_dict = {}

        # Iterate through all 'String' elements in the XAML file
        for string_element in root.findall(".//String"):
            key = string_element.get('Key')
            if key:
                if string_element.text is None:
                    result_dict[key] = ""
                else:
                    result_dict[key] = string_element.text

        return result_dict

    except ET.ParseError as e:
        print(f"Error parsing the XAML file: {e}")
        return {}
    except FileNotFoundError:
        print(f"Error: The file {xaml_file} does not exist.")
        return {}

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