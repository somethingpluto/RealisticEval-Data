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
