from typing import Dict


def parse_xaml_to_dict(xaml_file: str) -> Dict[str, str]:
    """
    parse the XAML file, extract the key-value pairs within the String element, and return the model_result in a dictionary
    Args:
        xaml_file (str): Path to the XAML file.

    Returns:
        A dictionary containing the key-value pairs extracted from 'String' elements.
    """
