import unittest
from unittest.mock import mock_open, patch


class TestExtractParametersFromFile(unittest.TestCase):
    def setUp(self):
        # Example content of a Fortran file
        self.fortran_content = """
        real(r8), target, allocatable :: x ! x dimension [m]
        real(r8), target, allocatable :: y ! y dimension [cm]
        real(r8), target, allocatable :: z(10, 10) ! z dimension [mm]
        """

    @patch('builtins.open', new_callable=mock_open, read_data="real(r8), target, allocatable :: temp ! Temperature [K]")
    def test_single_parameter_extraction(self, mock_file):
        # Test extraction of a single parameter
        result = extract_parameters_from_file("dummy_path.f90")
        expected = [{'variable_name': 'temp', 'dimensions': None, 'description': 'Temperature', 'units': 'K'}]
        self.assertEqual(result, expected)

    @patch('builtins.open', mock_open(read_data=""))
    def test_no_parameters(self, mock_file):
        # Test file with no parameter declarations
        result = extract_parameters_from_file("empty.f90")
        self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open,
           read_data="real(r8), target, allocatable :: velocity ! Wind velocity [m/s]")
    def test_parameter_with_dimensions(self, mock_file):
        # Test extraction where dimensions are explicitly not given but might be inferred from context
        result = extract_parameters_from_file("velocity.f90")
        expected = [{'variable_name': 'velocity', 'dimensions': None, 'description': 'Wind velocity', 'units': 'm/s'}]
        self.assertEqual(result, expected)

    @patch('builtins.open', mock_open(read_data=fortran_content))
    def test_multiple_parameters(self, mock_file):
        # Test extraction of multiple parameters
        result = extract_parameters_from_file("multiple.f90")
        expected = [
            {'variable_name': 'x', 'dimensions': None, 'description': 'x dimension', 'units': 'm'},
            {'variable_name': 'y', 'dimensions': None, 'description': 'y dimension', 'units': 'cm'},
            {'variable_name': 'z', 'dimensions': '10, 10', 'description': 'z dimension', 'units': 'mm'}
        ]
        self.assertEqual(result, expected)

    @patch('builtins.open', mock_open(read_data="real(r8), target, allocatable :: invalid ! invalid format"))
    def test_incorrect_format(self, mock_file):
        # Test extraction with incorrect format that does not meet the regex pattern
        result = extract_parameters_from_file("incorrect.f90")
        self.assertEqual(result, [])

import re


def extract_parameters_from_file(file_path):
    """
    Extract parameters, descriptions, and units from a Fortran file.

    Args:
    file_path (str): Path to the Fortran file.

    Returns:
    list of dict: A list of dictionaries, each containing the variable name,
                  description, and units of a parameter.

    Raises:
    FileNotFoundError: If the specified file does not exist.
    """
    # Open the file safely, handling the file not found error
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")

    # Regular expression pattern to capture parameter declarations
    pattern = (
        r"\breal\(r8\)\s*,\s*target\s*,\s*allocatable\s*::\s*"
        r"(\w+)\s*(?:\((.*?)\))?\s*!\s*(.*?)\s*,\s*\[(.*?)\]"
    )
    matches = re.findall(pattern, content, re.IGNORECASE)

    # Create a list of dictionaries for each match
    extracted_data = [
        {
            "variable_name": match[0].strip(),
            "dimensions": match[1].strip() if match[1] else None,
            "description": match[2].strip(),
            "units": match[3].strip()
        }
        for match in matches
    ]

    return extracted_data
