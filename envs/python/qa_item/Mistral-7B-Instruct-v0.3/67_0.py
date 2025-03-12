import xml.etree.ElementTree as ET
from typing import Dict

def parse_xaml_to_dict(xaml_file: str) -> Dict[str, str]:
    try:
        tree = ET.parse(xaml_file)
        root = tree.getroot()

        model_answer_result = {}
        for string_element in root.findall('String'):
            key_value_pair = string_element.text
            key, value = key_value_pair.split('=', 1)
            model_answer_result[key.strip()] = value.strip()

        return model_answer_result
    except Exception as e:
        print(f"Error occurred while parsing XAML file: {e}")
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