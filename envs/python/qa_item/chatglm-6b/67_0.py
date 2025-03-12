
from typing import Dict

def parse_xaml_to_dict(xaml_file: str) -> Dict[str, str]:
    """
    Parse the XAML file, extract the key-value pairs within the String element, and return the model_answer_result in a dictionary
    Args:
        xaml_file (str): Path to the XAML file.

    Returns:
        A dictionary containing the key-value pairs extracted from 'String' elements.
    """
    # Load the XAML file using the XAML解析器
     XAML_parser = XAML_parser.Parse(xaml_file)

    # 提取字符串元素
    string_elements = XAML_parser.GetElements("String")

    # 将字符串元素转换为字典
    model_answer_result = {}
    for string_element in string_elements:
        # 遍历字符串元素中的所有子元素
        for child in string_element.GetChildren():
            # 提取子元素中的字符串
            string_value = child.GetText()
            # 将字符串值添加到字典中
            model_answer_result[string_value] = True

    return model_answer_result

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