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
